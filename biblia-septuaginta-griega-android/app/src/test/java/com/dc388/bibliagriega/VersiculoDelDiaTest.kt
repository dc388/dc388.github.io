package com.dc388.bibliagriega

import com.dc388.bibliagriega.data.VersiculoDelDia
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.LocalDate

/**
 * El versículo del día.
 *
 * Dos cosas hay que sujetar aquí. La primera es que el reparto sea el mismo
 * para todos: lo que hace que alguien reenvíe el mensaje de la mañana es que
 * quien lo recibe tenga ese mismo versículo, y eso se rompe en silencio en
 * cuanto alguien mete azar o la hora del teléfono en el cálculo.
 *
 * La segunda es la promesa que distingue a esta aplicación de las otras
 * cincuenta que mandan un versículo al día: cada entrada trae una palabra del
 * original y una reflexión sobre esa palabra. Una entrada sin eso es una frase
 * devocional cualquiera y no debe salir de aquí.
 */
class VersiculoDelDiaTest {

    @Test
    fun `el mismo dia da el mismo versiculo`() {
        val dia = LocalDate.of(2026, 3, 14)
        assertEquals(VersiculoDelDia.de(dia), VersiculoDelDia.de(dia))
    }

    @Test
    fun `todos los dias del ano tienen versiculo, tambien el bisiesto`() {
        // 2024 es bisiesto: llega al día 366. Ese es justo el caso que se
        // saltaría un cálculo hecho sobre 365.
        var dia = LocalDate.of(2024, 1, 1)
        while (dia.year == 2024) {
            assertNotNull("sin versículo el $dia", VersiculoDelDia.de(dia))
            dia = dia.plusDays(1)
        }
    }

    @Test
    fun `mientras la lista sea corta, da la vuelta por el dia del ano`() {
        val largo = VersiculoDelDia.escritos
        val primero = LocalDate.of(2026, 1, 1)
        assertEquals(
            VersiculoDelDia.de(primero),
            VersiculoDelDia.de(primero.plusDays(largo.toLong())),
        )
    }

    @Test
    fun `cada entrada trae palabra del original y reflexion sobre ella`() {
        var dia = LocalDate.of(2026, 1, 1)
        repeat(VersiculoDelDia.escritos) {
            val v = VersiculoDelDia.de(dia)
            assertTrue("referencia vacía", v.referencia.isNotBlank())
            assertTrue("${v.referencia}: sin original", v.original.isNotBlank())
            assertTrue("${v.referencia}: sin español", v.espanol.isNotBlank())
            assertTrue("${v.referencia}: sin libro", v.codigo.isNotBlank())
            assertTrue("${v.referencia}: capítulo inválido", v.capitulo > 0)
            assertTrue("${v.referencia}: sin palabra", v.palabra.isNotBlank())
            assertTrue("${v.referencia}: sin transliteración", v.translit.isNotBlank())
            assertTrue("${v.referencia}: sin reflexión", v.reflexion.isNotBlank())
            dia = dia.plusDays(1)
        }
    }

    @Test
    fun `la palabra esta en griego o en hebreo, no en espanol`() {
        // Si una entrada se cuela con la palabra en español, la aplicación
        // pierde lo único que no tienen las demás.
        var dia = LocalDate.of(2026, 1, 1)
        repeat(VersiculoDelDia.escritos) {
            val v = VersiculoDelDia.de(dia)
            val original = v.palabra.any { c ->
                Character.UnicodeBlock.of(c).let {
                    it == Character.UnicodeBlock.GREEK ||
                        it == Character.UnicodeBlock.GREEK_EXTENDED ||
                        it == Character.UnicodeBlock.HEBREW
                }
            }
            assertTrue("${v.referencia}: «${v.palabra}» no es griego ni hebreo", original)
            dia = dia.plusDays(1)
        }
    }

    @Test
    fun `la palabra que se analiza esta en el versiculo`() {
        // Una reflexión sobre una palabra que no sale en el texto citado es una
        // reflexión sobre otro versículo. Se compara sin los acentos de
        // cantilación hebreos, que el texto lleva y la forma citada no, y en
        // minúscula, porque el griego abre el versículo con mayúscula
        // (Πάντα ἰσχύω) y el lema se cita en minúscula.
        var dia = LocalDate.of(2026, 1, 1)
        repeat(VersiculoDelDia.escritos) {
            val v = VersiculoDelDia.de(dia)
            val texto = sinCantilacion(v.original)
            val palabra = sinCantilacion(v.palabra)
            assertTrue(
                "${v.referencia}: «${v.palabra}» no aparece en el versículo",
                texto.contains(palabra),
            )
            dia = dia.plusDays(1)
        }
    }

    @Test
    fun `ninguna referencia se repite`() {
        val vistas = mutableSetOf<String>()
        var dia = LocalDate.of(2026, 1, 1)
        repeat(VersiculoDelDia.escritos) {
            val ref = VersiculoDelDia.de(dia).referencia
            assertTrue("$ref aparece dos veces", vistas.add(ref))
            dia = dia.plusDays(1)
        }
    }

    private fun sinCantilacion(texto: String): String =
        texto.filterNot { it.code in 0x0591..0x05AF }.lowercase()

    @Test
    fun `la reflexion no es un eslogan de una linea`() {
        // No es longitud por longitud: una reflexión de cuatro palabras no
        // puede estar explicando lo que dice un verbo griego.
        var dia = LocalDate.of(2026, 1, 1)
        repeat(VersiculoDelDia.escritos) {
            val v = VersiculoDelDia.de(dia)
            assertTrue("${v.referencia}: reflexión demasiado corta", v.reflexion.length > 60)
            assertFalse("${v.referencia}: reflexión sin terminar", v.reflexion.endsWith(","))
            dia = dia.plusDays(1)
        }
    }
}
