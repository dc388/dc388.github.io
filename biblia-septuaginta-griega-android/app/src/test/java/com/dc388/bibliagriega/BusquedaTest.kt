package com.dc388.bibliagriega

import com.dc388.bibliagriega.data.normalizarTexto
import com.dc388.bibliagriega.data.VerseRef
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * La normalización que usa la búsqueda tiene que dar exactamente lo mismo que la
 * columna `text_norm` que escribe tools/build_db.py. Si las dos se separan, la
 * búsqueda deja de encontrar lo que hay guardado, sin dar ningún error.
 */
class BusquedaTest {

    private fun norm(t: String) = normalizarTexto(t)

    @Test
    fun `quita los acentos y los espiritus del griego politonico`() {
        // Sale con sigma normal al final, no con sigma final: ver la prueba
        // siguiente. El iota suscrito de ῳ también desaparece.
        assertEquals("λογοσ", norm("λόγος"))
        assertEquals("λογω", norm("λόγῳ"))
        assertEquals("εν αρχη ην ο λογοσ", norm("Ἐν ἀρχῇ ἦν ὁ λόγος"))
        assertEquals("αδησ", norm("ᾅδης"))
    }

    @Test
    fun `la sigma final cuenta como sigma`() {
        // Sin esto, buscar «λογος» no encontraría «λόγος», que acaba en ς.
        assertEquals(norm("λόγοσ"), norm("λόγος"))
        assertEquals("σ", norm("ς"))
    }

    @Test
    fun `quita la vocalizacion del hebreo`() {
        assertEquals("ברא", norm("בָּרָא"))
        assertEquals("בראשית", norm("בְּרֵאשִׁית"))
    }

    @Test
    fun `la puntuacion se vuelve separacion y no pega palabras`() {
        assertEquals("θεον και", norm("θεόν, καὶ"))
        assertEquals("a b", norm("a·b"))
        assertEquals("fin", norm("  ¡fin!  "))
    }

    @Test
    fun `una busqueda anclada al principio distingue logos de flogos`() {
        // Es lo que hace la consulta: ' ' || text_norm LIKE '% ' || aguja || '%'
        fun empiezaAlguna(texto: String, aguja: String) =
            (" " + norm(texto)).contains(" " + norm(aguja))

        assertTrue(empiezaAlguna("ὁ λόγος ἦν", "λογ"))
        assertTrue(empiezaAlguna("ἐν λόγῳ", "λόγῳ"))
        assertTrue(empiezaAlguna("Λόγος ἦν", "λογος"))
        // φλογός contiene «λογ» en medio, y no debe salir.
        assertTrue(!empiezaAlguna("ἐκ φλογὸς πυρός", "λογ"))
    }

    @Test
    fun `una referencia de versiculo sobrevive a la ida y vuelta`() {
        val ref = VerseRef(bookId = 42, chapter = 3, verse = 16)
        assertEquals(ref, VerseRef.decode(ref.encode()))

        val conSufijo = VerseRef(bookId = 7, chapter = 15, verse = 12, suffix = "a")
        assertEquals(conSufijo, VerseRef.decode(conSufijo.encode()))
        assertEquals("7:15:12:a", conSufijo.encode())
    }

    @Test
    fun `una referencia estropeada no revienta, devuelve nulo`() {
        assertNull(VerseRef.decode(""))
        assertNull(VerseRef.decode("nada"))
        assertNull(VerseRef.decode("1:2"))
        assertNull(VerseRef.decode("x:2:3"))
    }
}
