package com.dc388.bibliagriega

import com.dc388.bibliagriega.ui.Compartir
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * Lo que sale de la aplicación cuando alguien comparte un versículo.
 *
 * Importa más de lo que parece: durante meses el mensaje llevaba la referencia
 * y el griego y nada más, así que quien lo recibía no tenía forma de saber de
 * dónde venía. Cada reenvío era un anuncio que no se cobraba.
 *
 * Estas pruebas fijan las dos cosas que no pueden perderse —el enlace a la
 * tienda y que los bloques vacíos no dejen hueco— porque son justo las que se
 * rompen sin que nadie lo note al tocar el formato.
 */
class CompartirTest {

    @Test
    fun `el mensaje siempre lleva el enlace a la tienda`() {
        val texto = Compartir.versiculo(
            referencia = "Juan 3:16",
            original = "Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον",
        )
        assertTrue(texto.contains(Compartir.ENLACE))
    }

    @Test
    fun `el espanol va antes que el original`() {
        val texto = Compartir.versiculo(
            referencia = "Juan 3:16",
            original = "Οὕτως γὰρ ἠγάπησεν",
            espanol = "Porque de tal manera amó Dios al mundo",
        )
        assertTrue(texto.indexOf("Porque de tal manera") < texto.indexOf("Οὕτως"))
    }

    @Test
    fun `sin traduccion no se deja el hueco`() {
        val texto = Compartir.versiculo(
            referencia = "Sabiduría 1:1",
            original = "Ἀγαπήσατε δικαιοσύνην",
            espanol = null,
        )
        assertFalse("no debe quedar una comilla sola", texto.contains("«»"))
        assertFalse("no deben quedar tres saltos seguidos", texto.contains("\n\n\n"))
    }

    @Test
    fun `una traduccion en blanco se trata como si no estuviera`() {
        val texto = Compartir.versiculo(
            referencia = "Sabiduría 1:1",
            original = "Ἀγαπήσατε δικαιοσύνην",
            espanol = "   ",
        )
        assertFalse(texto.contains("«"))
    }

    @Test
    fun `la reflexion solo aparece cuando la hay`() {
        val sin = Compartir.versiculo("Salmos 27:14", "ὑπόμεινον τὸν κύριον")
        val con = Compartir.versiculo(
            referencia = "Salmos 27:14",
            original = "ὑπόμεινον τὸν κύριον",
            reflexion = "Esperar aquí no es quedarse quieto.",
        )
        assertFalse(sin.contains("Esperar aquí"))
        assertTrue(con.contains("Esperar aquí no es quedarse quieto."))
    }

    @Test
    fun `la referencia va en negrita de WhatsApp`() {
        // Los asteriscos no son decoración: WhatsApp y Telegram los convierten
        // en negrita de verdad, y es ahí donde acaban estos mensajes.
        val texto = Compartir.versiculo("Juan 3:16", "Οὕτως")
        assertTrue(texto.contains("*Juan 3:16*"))
    }

    @Test
    fun `el mensaje no empieza ni acaba con lineas en blanco`() {
        val texto = Compartir.versiculo(
            referencia = "Juan 3:16",
            original = "Οὕτως",
            espanol = "Porque de tal manera",
            reflexion = "Una línea.",
        )
        assertEquals(texto, texto.trim())
    }
}
