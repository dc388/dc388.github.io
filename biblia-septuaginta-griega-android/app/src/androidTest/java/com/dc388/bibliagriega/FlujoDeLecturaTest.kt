package com.dc388.bibliagriega

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onAllNodesWithText
import androidx.compose.ui.test.onFirst
import androidx.compose.ui.test.onNodeWithContentDescription
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performTextInput
import androidx.test.ext.junit.runners.AndroidJUnit4
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

/**
 * Recorre la aplicación como la recorrería una persona, sobre la base de datos
 * de verdad: abre un libro, lee un capítulo, busca una palabra y consulta el
 * léxico. Necesita un emulador o un teléfono conectado.
 *
 * El primer arranque copia los 63 MB de la base desde el asset, así que las
 * esperas son generosas a propósito.
 */
@RunWith(AndroidJUnit4::class)
class FlujoDeLecturaTest {

    @get:Rule
    val regla = createAndroidComposeRule<MainActivity>()

    /** Espera a que aparezca algo, dando tiempo a la copia de la base. */
    private fun esperar(texto: String, substring: Boolean = true, ms: Long = 120_000) {
        regla.waitUntil(timeoutMillis = ms) {
            regla.onAllNodes(hasText(texto, substring = substring))
                .fetchSemanticsNodes().isNotEmpty()
        }
    }

    @Test
    fun la_biblioteca_trae_las_tres_colecciones() {
        esperar("Biblia Griega")

        regla.onNodeWithText("AT hebreo").assertIsDisplayed()
        regla.onNodeWithText("Septuaginta").assertIsDisplayed()
        regla.onNodeWithText("NT griego").assertIsDisplayed()
    }

    @Test
    fun se_puede_leer_un_capitulo_del_nuevo_testamento() {
        esperar("Biblia Griega")

        regla.onNodeWithText("NT griego").performClick()
        esperar("Juan")
        regla.onAllNodesWithText("Juan").onFirst().performClick()

        // Rejilla de capítulos: Juan tiene 21.
        esperar("21")
        regla.onAllNodesWithText("1").onFirst().performClick()

        // Juan 1:1. Si el texto griego no está, la base no se copió bien.
        esperar("Ἐν ἀρχῇ")
    }

    @Test
    fun el_hebreo_se_carga_con_su_vocalizacion() {
        esperar("Biblia Griega")

        regla.onNodeWithText("AT hebreo").performClick()
        esperar("Génesis")
        regla.onAllNodesWithText("Génesis").onFirst().performClick()

        esperar("50")
        regla.onAllNodesWithText("1").onFirst().performClick()

        // Génesis 1:1 con puntuación masorética: si saliera sin vocales, la
        // fuente o la importación estarían perdiendo los signos.
        esperar("בְּרֵאשִׁית")
    }

    @Test
    fun la_busqueda_encuentra_por_el_principio_de_la_palabra() {
        esperar("Biblia Griega")

        regla.onNodeWithContentDescription("Buscar").performClick()
        esperar("Buscar")
        regla.onNode(hasText("Palabra griega o hebrea", substring = true))
            .performTextInput("λογ")

        esperar("λόγος")
    }

    @Test
    fun los_ajustes_muestran_la_procedencia_de_cada_texto() {
        esperar("Biblia Griega")

        regla.onNodeWithContentDescription("Ajustes").performClick()
        esperar("Tamaño de letra")

        // La ficha de licencias es obligatoria: los textos son de terceros.
        esperar("Swete")
        esperar("Robinson")
    }
}
