package com.dc388.bibliagriega

import androidx.compose.ui.test.ComposeTimeoutException
import androidx.compose.ui.test.hasText
import androidx.compose.ui.test.junit4.createAndroidComposeRule
import androidx.compose.ui.test.onAllNodesWithText
import androidx.compose.ui.test.onFirst
import androidx.compose.ui.test.onNodeWithContentDescription
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.onRoot
import androidx.compose.ui.test.performClick
import androidx.compose.ui.test.performScrollTo
import androidx.compose.ui.test.performTextInput
import androidx.compose.ui.test.printToString
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.uiautomator.UiDevice
import org.junit.Rule
import org.junit.Test
import org.junit.runner.RunWith

/**
 * Toma las capturas de pantalla que pide Google Play, de la aplicación de
 * verdad corriendo en un emulador.
 *
 * No es una maqueta ni un montaje: es la misma aplicación que se instala, con
 * la base de datos completa, fotografiada mientras alguien la usa. Play exige
 * que las capturas representen lo que el usuario se va a encontrar, y esta es
 * la única forma de garantizarlo sin tener el teléfono delante.
 *
 * Los archivos quedan en el directorio externo de la aplicación, de donde el
 * flujo de trabajo los saca con `adb pull`. Play pide entre 2 y 8, en
 * proporción 16:9 o 9:16, así que el emulador tiene que ser de 1080×1920.
 */
@RunWith(AndroidJUnit4::class)
class CapturasTest {

    @get:Rule
    val regla = createAndroidComposeRule<MainActivity>()

    private val dispositivo: UiDevice
        get() = UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())

    /**
     * Dónde se guardan las imágenes: una carpeta del almacenamiento compartido,
     * escrita por el shell.
     *
     * No se usa el directorio de ninguna de las dos aplicaciones porque
     * `getExternalFilesDir` devuelve null en este emulador, y entonces la ruta
     * queda relativa y no se escribe nada. El shell sí puede escribir en
     * /sdcard siempre, y es de donde el flujo las recoge con `adb pull`.
     */
    private val carpeta = "/sdcard/capturas"

    private var numero = 0

    private fun capturar(nombre: String) {
        regla.waitForIdle()
        // Un fotograma de margen: al emulador le cuesta terminar de dibujar la
        // sombra de una hoja o el tinte de una fila recién tocada, y sale a
        // medias en la imagen.
        Thread.sleep(700)
        numero += 1
        val ruta = "%s/%d-%s.png".format(carpeta, numero, nombre)
        // `screencap` es lo que usa `adb screenshot` por dentro: fotografía la
        // pantalla entera, con barra de estado, y la escribe como shell.
        dispositivo.executeShellCommand("screencap -p $ruta")
        val bytes = dispositivo.executeShellCommand("stat -c %s $ruta").trim()
        val tamano = bytes.toLongOrNull() ?: 0L
        check(tamano > 1_000) {
            "La captura $ruta no se escribió o salió vacía: stat devolvió «$bytes»"
        }
    }

    private fun esperar(texto: String, ms: Long = 180_000) {
        try {
            regla.waitUntil(timeoutMillis = ms) {
                regla.onAllNodes(hasText(texto, substring = true))
                    .fetchSemanticsNodes().isNotEmpty()
            }
        } catch (e: ComposeTimeoutException) {
            throw AssertionError(
                "No apareció «$texto» en ${ms / 1000} s. Esto había en pantalla:\n" +
                    regla.onRoot().printToString(maxDepth = 12),
                e,
            )
        }
    }

    @Test
    fun capturas_para_la_ficha_de_play() {
        dispositivo.executeShellCommand("rm -rf $carpeta")
        dispositivo.executeShellCommand("mkdir -p $carpeta")

        // 1. La biblioteca, con las tres colecciones.
        esperar("AT hebreo")
        capturar("biblioteca")

        // 2. El Nuevo Testamento griego con la traducción debajo.
        regla.onNodeWithText("NT griego").performClick()
        esperar("Juan")
        regla.onAllNodesWithText("Juan").onFirst().performClick()
        esperar("21")
        regla.onAllNodesWithText("1").onFirst().performClick()
        esperar("Ἐν ἀρχῇ")
        capturar("nt-griego")

        // 3. El mismo capítulo en modo interlineal, que es lo que distingue a
        //    esta aplicación de cualquier otra Biblia.
        regla.onNodeWithContentDescription("Tipografía").performClick()
        esperar("Modo interlineal")
        // Hay que bajar hasta la fila: desde que Ajustes empieza por la tarjeta
        // de la suscripción, «Modo interlineal» queda fuera de la pantalla, y
        // Compose no deja pulsar lo que no se ve.
        regla.onNodeWithText("Modo interlineal").performScrollTo().performClick()
        regla.waitForIdle()
        regla.onNodeWithContentDescription("Atrás").performClick()
        // En interlineal el versículo deja de ser una frase: cada palabra es su
        // propio nodo, con su transliteración, su glosa y su número Strong. Por
        // eso no se espera «Ἐν ἀρχῇ», que ya no existe seguido, sino el Strong
        // de la primera palabra, que solo aparece en este modo.
        esperar("G1722")
        capturar("interlineal")

        // 4. El hebreo con su vocalización, de derecha a izquierda.
        regla.onNodeWithContentDescription("Atrás").performClick()
        regla.onNodeWithContentDescription("Atrás").performClick()
        esperar("AT hebreo")
        regla.onNodeWithText("AT hebreo").performClick()
        esperar("Génesis")
        regla.onAllNodesWithText("Génesis").onFirst().performClick()
        esperar("50")
        regla.onAllNodesWithText("1").onFirst().performClick()
        esperar("בְּרֵאשִׁית")
        capturar("hebreo")

        // 5. La búsqueda sin acentos, abierta desde el lector.
        regla.onNodeWithContentDescription("Buscar").performClick()
        esperar("Buscar")
        regla.onNode(hasText("Palabra griega o hebrea", substring = true))
            .performTextInput("λογ")
        esperar("λόγος")
        capturar("busqueda")

        // 6. Las licencias: de dónde sale cada texto.
        //
        // Se vuelve al lector, no a la biblioteca: la búsqueda se abrió desde
        // aquí, así que atrás devuelve al capítulo. Y desde el lector, los
        // ajustes se abren con «Tipografía», que es como se llama ese botón en
        // la barra superior; «Ajustes» solo existe en la pantalla de inicio.
        regla.onNodeWithContentDescription("Atrás").performClick()
        esperar("בְּרֵאשִׁית")
        regla.onNodeWithContentDescription("Tipografía").performClick()
        esperar("Swete")
        regla.onNodeWithText("Textos y licencias").performScrollTo()
        capturar("ajustes")

        val listado = dispositivo.executeShellCommand("ls $carpeta").trim()
        val hechas = listado.lines().count { it.isNotBlank() }
        check(hechas >= 2) { "Play pide 2 capturas como mínimo y solo salieron $hechas: $listado" }
        println("Capturas en $carpeta: $hechas\n$listado")
    }
}
