package com.dc388.bibliagriega.data

import java.text.Normalizer

private val ESPACIOS = Regex("\\s+")

/**
 * Deja el texto como la columna `text_norm` que escribe `tools/build_db.py`:
 * minúsculas, sin acentos ni espíritus griegos, sin vocalización hebrea, con la
 * puntuación convertida en separación y la sigma final unificada.
 *
 * Las dos implementaciones tienen que dar exactamente lo mismo. Si se separan,
 * la búsqueda deja de encontrar lo que hay guardado y no salta ningún error: el
 * usuario solo ve que no aparece nada. `BusquedaTest` fija el comportamiento.
 *
 * Vive fuera del repositorio, y no en su companion, porque no depende de Android
 * ni de la base de datos: así se puede probar en la JVM, sin emulador.
 */
fun normalizarTexto(text: String): String {
    val descompuesto = Normalizer.normalize(text.lowercase(), Normalizer.Form.NFD)
    val sb = StringBuilder(descompuesto.length)
    for (ch in descompuesto) {
        when {
            Character.getType(ch) == Character.NON_SPACING_MARK.toInt() -> Unit
            ch == '\u03c2' -> sb.append('\u03c3')
            ch.isLetterOrDigit() -> sb.append(ch)
            else -> sb.append(' ')
        }
    }
    return sb.toString().trim().replace(ESPACIOS, " ")
}
