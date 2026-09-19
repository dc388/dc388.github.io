package com.dc388.bibliagriega

import com.dc388.bibliagriega.data.Book
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Test

/**
 * La app daba por hecho que los capítulos de un libro son 1..N seguidos, y en la
 * Septuaginta no lo son. Estas pruebas fijan los tres casos que lo rompían, para
 * que no vuelvan si algún día se cambia la navegación.
 */
class NavegacionDeCapitulosTest {

    private fun libro(vararg capitulos: Int) = Book(
        id = 1,
        collectionId = "lxx",
        code = "XXX",
        nameEs = "Libro",
        nameOriginal = "",
        altName = null,
        sourceNote = null,
        chapterCount = capitulos.size,
        chapters = capitulos.toList(),
        verseCount = 0,
        rtl = false,
    )

    @Test
    fun `las Odas saltan del 3 al 5 porque a Swete le falta la 4`() {
        val odas = libro(1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        assertEquals(5, odas.chapterAfter(3))
        assertEquals(3, odas.chapterBefore(5))
    }

    @Test
    fun `se llega a la ultima Oda aunque haya un hueco en medio`() {
        val odas = libro(1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

        // Contando capítulos en vez de listarlos, la 14 quedaba fuera: son trece.
        assertEquals(13, odas.chapterCount)
        assertEquals(14, odas.chapters.last())
        assertEquals(14, odas.chapterAfter(13))
        assertNull(odas.chapterAfter(14))
    }

    @Test
    fun `Sabiduria salta del 14 al 16`() {
        val sabiduria = libro(*(1..14).toList().plus(16..20).toIntArray())

        assertEquals(16, sabiduria.chapterAfter(14))
        assertEquals(14, sabiduria.chapterBefore(16))
        assertEquals(20, sabiduria.chapters.last())
    }

    @Test
    fun `el primer capitulo no tiene anterior y el ultimo no tiene siguiente`() {
        val genesis = libro(*(1..50).toList().toIntArray())

        assertNull(genesis.chapterBefore(1))
        assertNull(genesis.chapterAfter(50))
        assertEquals(2, genesis.chapterAfter(1))
        assertEquals(49, genesis.chapterBefore(50))
    }

    @Test
    fun `el capitulo cero del Eclesiastico es el prologo del traductor`() {
        val eclesiastico = libro(*(0..51).toList().toIntArray())

        assertEquals("Pról.", eclesiastico.chapterLabel(0))
        assertEquals("1", eclesiastico.chapterLabel(1))
        assertEquals(1, eclesiastico.chapterAfter(0))
        assertNull(eclesiastico.chapterBefore(0))
    }

    @Test
    fun `un libro de un solo capitulo no navega a ninguna parte`() {
        val cartaDeJeremias = libro(1)

        assertNull(cartaDeJeremias.chapterAfter(1))
        assertNull(cartaDeJeremias.chapterBefore(1))
        assertEquals(1, cartaDeJeremias.chapterCount)
    }

    @Test
    fun `un capitulo que no existe no propone vecinos`() {
        val odas = libro(1, 2, 3, 5)

        // La 4 no está: preguntar por ella no puede devolver la 5 ni la 3.
        assertNull(odas.chapterAfter(4))
        assertNull(odas.chapterBefore(4))
    }

    @Test
    fun `el nombre muestra entre parentesis el que usan las biblias modernas`() {
        val base = libro(1)
        assertEquals("Libro", base.displayName)
        assertEquals("Libro (Otro)", base.copy(altName = "Otro").displayName)
    }
}
