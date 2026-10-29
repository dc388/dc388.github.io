package com.dc388.bibliagriega

import android.Manifest
import android.content.Context
import android.os.Build
import androidx.test.ext.junit.runners.AndroidJUnit4
import androidx.test.platform.app.InstrumentationRegistry
import androidx.test.uiautomator.By
import androidx.test.uiautomator.UiDevice
import androidx.test.uiautomator.Until
import com.dc388.bibliagriega.data.AvisoDiario
import com.dc388.bibliagriega.data.VersiculoDelDia
import org.junit.After
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import java.time.LocalDate

/**
 * Que el aviso de cada mañana salga de verdad.
 *
 * Esto no se puede comprobar con una prueba de Compose: la notificación no es
 * una pantalla de la aplicación, es una fila en la persiana del sistema, y
 * entre el código y esa fila hay un canal que crear, un permiso que tener y un
 * icono que Android puede rechazar. Cada una de esas tres cosas falla en
 * silencio —no hay excepción, simplemente no sale nada—, que es la peor forma
 * de fallar que hay. De ahí que se mire con UiAutomator, abriendo la persiana
 * como la abriría una persona.
 */
@RunWith(AndroidJUnit4::class)
class AvisoDiarioTest {

    private val instrumentacion = InstrumentationRegistry.getInstrumentation()
    private val contexto: Context get() = instrumentacion.targetContext
    private val dispositivo: UiDevice get() = UiDevice.getInstance(instrumentacion)

    @Before
    fun conceder_el_permiso() {
        // Desde Android 13 sin esto no sale nada, y la prueba diría que el
        // aviso está roto cuando lo que falta es el permiso.
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
            runCatching {
                instrumentacion.uiAutomation.grantRuntimePermission(
                    contexto.packageName,
                    Manifest.permission.POST_NOTIFICATIONS,
                )
            }
        }
    }

    @After
    fun recoger() {
        AvisoDiario.cancelar(contexto)
        dispositivo.pressBack()
        dispositivo.pressHome()
    }

    @Test
    fun el_aviso_sale_con_la_referencia_y_el_versiculo() {
        val hoy = VersiculoDelDia.de(LocalDate.of(2026, 1, 1))
        AvisoDiario.mostrar(contexto, hoy)
        dispositivo.openNotification()

        assertTrue(
            "no salió la referencia «${hoy.referencia}» en la persiana",
            dispositivo.wait(Until.hasObject(By.textContains(hoy.referencia)), ESPERA),
        )
        // Un trozo corto del principio: la fila plegada recorta el texto y el
        // final puede no estar.
        val principio = hoy.espanol.take(15)
        assertTrue(
            "la referencia salió pero el versículo no: faltaba «$principio»",
            dispositivo.hasObject(By.textContains(principio)),
        )
    }

    @Test
    fun programar_y_cancelar_la_alarma_no_revienta() {
        // Parece poca prueba y no lo es: esto corre en el arranque del
        // teléfono, donde una excepción no es un aviso que no sale, es la
        // aplicación cerrándose sola.
        AvisoDiario.programar(contexto, 7)
        AvisoDiario.programar(contexto, 23)
        AvisoDiario.cancelar(contexto)
    }

    private companion object {
        const val ESPERA = 10_000L
    }
}
