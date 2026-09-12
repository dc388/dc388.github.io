package com.dc388.bibliagriega.data

import android.content.Context
import android.database.Cursor
import android.database.sqlite.SQLiteDatabase
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock
import kotlinx.coroutines.withContext
import java.io.File
import java.text.Normalizer

/**
 * Acceso de solo lectura a `assets/biblia.db`.
 *
 * SQLite no puede abrir un archivo dentro del APK, así que la base se copia una vez
 * a los archivos privados de la app y se reutiliza mientras no cambie la versión.
 */
class BibleRepository private constructor(private val appContext: Context) {

    private val mutex = Mutex()
    private var db: SQLiteDatabase? = null

    private suspend fun database(): SQLiteDatabase = mutex.withLock {
        db?.takeIf { it.isOpen } ?: withContext(Dispatchers.IO) {
            val file = ensureDatabaseFile()
            SQLiteDatabase.openDatabase(file.path, null, SQLiteDatabase.OPEN_READONLY)
                .also { db = it }
        }
    }

    private fun ensureDatabaseFile(): File {
        val target = File(appContext.filesDir, DB_NAME)
        val stamp = File(appContext.filesDir, "$DB_NAME.stamp")
        val expected = appContext.packageManager
            .getPackageInfo(appContext.packageName, 0)
            .let { "${it.versionName}/${DB_NAME}" }

        if (target.exists() && stamp.exists() && stamp.readText() == expected) return target

        appContext.assets.open(DB_NAME).use { input ->
            val tmp = File(appContext.filesDir, "$DB_NAME.tmp")
            tmp.outputStream().use { output -> input.copyTo(output, DEFAULT_BUFFER_SIZE * 8) }
            if (target.exists()) target.delete()
            check(tmp.renameTo(target)) { "No se pudo instalar la base de datos" }
        }
        stamp.writeText(expected)
        return target
    }

    suspend fun collections(): List<BibleCollection> = query(
        "SELECT id, name, short_name, edition, license, source_url, language, rtl" +
            " FROM collections ORDER BY sort_order"
    ) {
        BibleCollection(
            id = it.getString(0),
            name = it.getString(1),
            shortName = it.getString(2),
            edition = it.getString(3),
            license = it.getString(4),
            sourceUrl = it.getString(5),
            language = it.getString(6),
            rtl = it.getInt(7) == 1,
        )
    }

    suspend fun books(collectionId: String): List<Book> = query(
        BOOK_COLUMNS + " WHERE b.collection_id = ? ORDER BY b.sort_order",
        arrayOf(collectionId),
        ::readBook,
    )

    suspend fun book(bookId: Long): Book? = query(
        BOOK_COLUMNS + " WHERE b.id = ?",
        arrayOf(bookId.toString()),
        ::readBook,
    ).firstOrNull()

    suspend fun chapter(bookId: Long, chapter: Int): List<Verse> = query(
        "SELECT id, book_id, chapter, verse, suffix, text FROM verses" +
            " WHERE book_id = ? AND chapter = ? ORDER BY verse, suffix",
        arrayOf(bookId.toString(), chapter.toString()),
        ::readVerse,
    )

    suspend fun verse(ref: VerseRef): VerseHit? = query(
        "SELECT v.id, v.book_id, v.chapter, v.verse, v.suffix, v.text, b.name_es," +
            " b.collection_id FROM verses v JOIN books b ON b.id = v.book_id" +
            " WHERE v.book_id = ? AND v.chapter = ? AND v.verse = ? AND v.suffix = ?",
        arrayOf(ref.bookId.toString(), ref.chapter.toString(), ref.verse.toString(), ref.suffix),
        ::readHit,
    ).firstOrNull()

    suspend fun verses(refs: List<VerseRef>): List<VerseHit> = refs.mapNotNull { verse(it) }

    /**
     * Busca sin exigir diacríticos y por el comienzo de la palabra: «λογ» encuentra
     * «λόγος», «λόγῳ» y «λόγον» —útil en una lengua flexiva— pero no «φλογός».
     * [collectionId] nulo busca en toda la Biblia.
     */
    suspend fun search(rawQuery: String, collectionId: String?, limit: Int = 300): List<VerseHit> {
        val needle = normalize(rawQuery)
        if (needle.length < 2) return emptyList()

        val sql = buildString {
            append(
                "SELECT v.id, v.book_id, v.chapter, v.verse, v.suffix, v.text, b.name_es," +
                    " b.collection_id FROM verses v JOIN books b ON b.id = v.book_id" +
                    // El espacio inicial hace que el patrón «% needle%» ancle en inicio de palabra.
                    " WHERE ' ' || v.text_norm LIKE ?"
            )
            if (collectionId != null) append(" AND b.collection_id = ?")
            append(" ORDER BY b.collection_id, b.sort_order, v.chapter, v.verse")
            append(" LIMIT ${limit.coerceIn(1, 2000)}")
        }
        val args = buildList {
            add("% $needle%")
            if (collectionId != null) add(collectionId)
        }.toTypedArray()

        return query(sql, args, ::readHit)
    }

    private fun readBook(c: Cursor) = Book(
        id = c.getLong(0),
        collectionId = c.getString(1),
        code = c.getString(2),
        nameEs = c.getString(3),
        nameOriginal = c.getString(4),
        altName = if (c.isNull(5)) null else c.getString(5),
        sourceNote = if (c.isNull(6)) null else c.getString(6),
        chapterCount = c.getInt(7),
        verseCount = c.getInt(8),
        rtl = c.getInt(9) == 1,
    )

    private fun readVerse(c: Cursor) = Verse(
        id = c.getLong(0),
        bookId = c.getLong(1),
        chapter = c.getInt(2),
        verse = c.getInt(3),
        suffix = c.getString(4) ?: "",
        text = c.getString(5),
    )

    private fun readHit(c: Cursor) = VerseHit(
        verse = readVerse(c),
        bookName = c.getString(6),
        collectionId = c.getString(7),
    )

    // --- Interlineal y léxico -------------------------------------------------

    /**
     * Análisis palabra por palabra de todo un capítulo, agrupado por id de versículo.
     * Devuelve un mapa vacío en los textos que todavía no están etiquetados.
     */
    suspend fun wordsOfChapter(bookId: Long, chapter: Int): Map<Long, List<InterlinearWord>> {
        val rows = query(
            "SELECT w.verse_id, w.position, w.surface, w.strong, w.homonym, w.morph," +
                " m.description, l.lemma, l.translit, d.gloss" +
                " FROM words w" +
                " JOIN verses v ON v.id = w.verse_id" +
                " LEFT JOIN morph_codes m ON m.code = w.morph" +
                " LEFT JOIN lexicon l ON l.strong = w.strong" +
                " LEFT JOIN articles d ON d.strong = w.strong AND d.homonym = w.homonym" +
                " WHERE v.book_id = ? AND v.chapter = ?" +
                " ORDER BY w.verse_id, w.position",
            arrayOf(bookId.toString(), chapter.toString()),
        ) {
            it.getLong(0) to InterlinearWord(
                position = it.getInt(1),
                surface = it.getString(2),
                strong = it.getString(3),
                homonym = it.getString(4) ?: "",
                morphCode = it.getString(5),
                morphology = if (it.isNull(6)) null else it.getString(6),
                lemma = if (it.isNull(7)) null else it.getString(7),
                transliteration = if (it.isNull(8)) null else it.getString(8),
                gloss = if (it.isNull(9)) null else it.getString(9),
            )
        }
        return rows.groupBy({ it.first }, { it.second })
    }

    suspend fun lexiconEntry(strong: String): LexiconEntry? = query(
        "SELECT strong, lemma, translit, derivation, definition, kjv_usage" +
            " FROM lexicon WHERE strong = ?",
        arrayOf(strong),
    ) {
        LexiconEntry(
            strong = it.getString(0),
            lemma = it.getString(1),
            transliteration = if (it.isNull(2)) null else it.getString(2),
            derivation = if (it.isNull(3)) null else it.getString(3),
            definition = if (it.isNull(4)) null else it.getString(4),
            kjvUsage = if (it.isNull(5)) null else it.getString(5),
        )
    }.firstOrNull()

    /** Artículo del léxico de referencia de una palabra, si lo tiene. */
    suspend fun articleOf(strong: String, homonym: String): LexiconArticle? = query(
        "SELECT strong, homonym, source, headword, gloss, pos, article FROM articles" +
            " WHERE strong = ? AND homonym = ?",
        arrayOf(strong, homonym),
    ) {
        LexiconArticle(
            strong = it.getString(0),
            homonym = it.getString(1),
            source = it.getString(2),
            headword = if (it.isNull(3)) null else it.getString(3),
            gloss = if (it.isNull(4)) null else it.getString(4),
            partOfSpeech = if (it.isNull(5)) null else it.getString(5),
            article = it.getString(6),
        )
    }.firstOrNull()

    /** Cuántas veces aparece un número Strong en todo el corpus etiquetado. */
    suspend fun occurrenceCount(strong: String): Int = query(
        "SELECT COUNT(*) FROM words WHERE strong = ?",
        arrayOf(strong),
    ) { it.getInt(0) }.firstOrNull() ?: 0

    /** Concordancia: versículos donde aparece un número Strong. */
    suspend fun occurrences(strong: String, limit: Int = 500): List<VerseHit> = query(
        "SELECT DISTINCT v.id, v.book_id, v.chapter, v.verse, v.suffix, v.text, b.name_es," +
            " b.collection_id, b.sort_order FROM words w" +
            " JOIN verses v ON v.id = w.verse_id" +
            " JOIN books b ON b.id = v.book_id" +
            " WHERE w.strong = ?" +
            " ORDER BY b.sort_order, v.chapter, v.verse" +
            " LIMIT ${limit.coerceIn(1, 2000)}",
        arrayOf(strong),
        ::readHit,
    )

    private suspend fun <T> query(
        sql: String,
        args: Array<String>? = null,
        map: (Cursor) -> T,
    ): List<T> = withContext(Dispatchers.IO) {
        database().rawQuery(sql, args).use { cursor ->
            buildList {
                while (cursor.moveToNext()) add(map(cursor))
            }
        }
    }

    companion object {
        private const val DB_NAME = "biblia.db"

        private const val BOOK_COLUMNS =
            "SELECT b.id, b.collection_id, b.code, b.name_es, b.name_orig, b.alt_name," +
                " b.source_note, b.chapter_count, b.verse_count, c.rtl" +
                " FROM books b JOIN collections c ON c.id = b.collection_id"

        @Volatile
        private var instance: BibleRepository? = null

        fun get(context: Context): BibleRepository =
            instance ?: synchronized(this) {
                instance ?: BibleRepository(context.applicationContext).also { instance = it }
            }

        /** Misma normalización que usa `tools/build_db.py` para la columna `text_norm`. */
        fun normalize(text: String): String {
            val decomposed = Normalizer.normalize(text.lowercase(), Normalizer.Form.NFD)
            val sb = StringBuilder(decomposed.length)
            for (ch in decomposed) {
                when {
                    Character.getType(ch) == Character.NON_SPACING_MARK.toInt() -> Unit
                    ch == 'ς' -> sb.append('σ')
                    ch.isLetterOrDigit() -> sb.append(ch)
                    else -> sb.append(' ')
                }
            }
            return sb.toString().trim().replace(WHITESPACE, " ")
        }

        private val WHITESPACE = Regex("\\s+")
    }
}
