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
        "SELECT id, name, short_name, edition, license, source_url FROM collections ORDER BY sort_order"
    ) {
        BibleCollection(
            id = it.getString(0),
            name = it.getString(1),
            shortName = it.getString(2),
            edition = it.getString(3),
            license = it.getString(4),
            sourceUrl = it.getString(5),
        )
    }

    suspend fun books(collectionId: String): List<Book> = query(
        BOOK_COLUMNS + " WHERE collection_id = ? ORDER BY sort_order",
        arrayOf(collectionId),
        ::readBook,
    )

    suspend fun book(bookId: Long): Book? = query(
        BOOK_COLUMNS + " WHERE id = ?",
        arrayOf(bookId.toString()),
        ::readBook,
    ).firstOrNull()

    suspend fun chapter(bookId: Long, chapter: Int): List<Verse> = query(
        "SELECT book_id, chapter, verse, suffix, text FROM verses" +
            " WHERE book_id = ? AND chapter = ? ORDER BY verse, suffix",
        arrayOf(bookId.toString(), chapter.toString()),
        ::readVerse,
    )

    suspend fun verse(ref: VerseRef): VerseHit? = query(
        "SELECT v.book_id, v.chapter, v.verse, v.suffix, v.text, b.name_es, b.collection_id" +
            " FROM verses v JOIN books b ON b.id = v.book_id" +
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
                "SELECT v.book_id, v.chapter, v.verse, v.suffix, v.text, b.name_es, b.collection_id" +
                    " FROM verses v JOIN books b ON b.id = v.book_id" +
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
        nameGr = c.getString(4),
        altName = if (c.isNull(5)) null else c.getString(5),
        sourceNote = if (c.isNull(6)) null else c.getString(6),
        chapterCount = c.getInt(7),
        verseCount = c.getInt(8),
    )

    private fun readVerse(c: Cursor) = Verse(
        bookId = c.getLong(0),
        chapter = c.getInt(1),
        verse = c.getInt(2),
        suffix = c.getString(3) ?: "",
        text = c.getString(4),
    )

    private fun readHit(c: Cursor) = VerseHit(
        verse = readVerse(c),
        bookName = c.getString(5),
        collectionId = c.getString(6),
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
            "SELECT id, collection_id, code, name_es, name_gr, alt_name, source_note," +
                " chapter_count, verse_count FROM books"

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
