package com.dc388.bibliagriega.data

/** Una de las dos colecciones que trae la app: Septuaginta o Nuevo Testamento. */
data class BibleCollection(
    val id: String,
    val name: String,
    val shortName: String,
    val edition: String,
    val license: String,
    val sourceUrl: String,
)

data class Book(
    val id: Long,
    val collectionId: String,
    val code: String,
    val nameEs: String,
    val nameGr: String,
    /** Nombre con el que el libro se conoce en las biblias hebreas/modernas, si difiere. */
    val altName: String?,
    /** Nota de procedencia cuando el texto no viene de la edición principal. */
    val sourceNote: String?,
    val chapterCount: Int,
    val verseCount: Int,
) {
    val displayName: String get() = if (altName != null) "$nameEs ($altName)" else nameEs
}

data class Verse(
    val id: Long,
    val bookId: Long,
    val chapter: Int,
    val verse: Int,
    /** Sufijo de versículo de la LXX, p. ej. el «a» de Josué 15:59a. */
    val suffix: String,
    val text: String,
) {
    val label: String get() = "$verse$suffix"
}

/** Un versículo con su libro resuelto, para búsqueda y marcadores. */
data class VerseHit(
    val verse: Verse,
    val bookName: String,
    val collectionId: String,
) {
    val reference: String get() = "$bookName ${verse.chapter}:${verse.label}"
}

/** Una palabra del texto griego con su análisis Strong y morfológico. */
data class InterlinearWord(
    val position: Int,
    /** La palabra tal como aparece en el texto, con su puntuación. */
    val surface: String,
    val strong: String,
    val morphCode: String,
    /** Descripción morfológica en español, ya resuelta desde `morph_codes`. */
    val morphology: String?,
    val lemma: String?,
    val transliteration: String?,
)

/** Entrada del diccionario griego de Strong. */
data class LexiconEntry(
    val strong: String,
    val lemma: String,
    val transliteration: String?,
    val derivation: String?,
    val definition: String?,
    val kjvUsage: String?,
)

/** Referencia serializable que identifica una posición de lectura. */
data class VerseRef(val bookId: Long, val chapter: Int, val verse: Int, val suffix: String = "") {
    fun encode(): String = "$bookId:$chapter:$verse:$suffix"

    companion object {
        fun decode(raw: String): VerseRef? {
            val parts = raw.split(":")
            if (parts.size < 3) return null
            val bookId = parts[0].toLongOrNull() ?: return null
            val chapter = parts[1].toIntOrNull() ?: return null
            val verse = parts[2].toIntOrNull() ?: return null
            return VerseRef(bookId, chapter, verse, parts.getOrElse(3) { "" })
        }
    }
}
