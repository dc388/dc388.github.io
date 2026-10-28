package com.dc388.bibliagriega.data

import android.content.Context
import android.os.Handler
import android.os.Looper
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import java.util.Locale

/**
 * La voz que lee el texto en alto.
 *
 * Usa el sintetizador que ya trae el teléfono. No se graba ni se descarga nada:
 * la aplicación pesa lo mismo que antes, funciona sin conexión y no hay
 * licencias de locución que pagar ni que respetar. A cambio, la voz es la que
 * el usuario tenga instalada, y puede no tener ninguna para una lengua.
 *
 * **Qué lee.** En el Antiguo Testamento hebreo y en el Nuevo Testamento griego
 * hay traducción debajo de cada versículo, y es esa la que se lee: es la que
 * entiende quien escucha. Donde no hay traducción —la Septuaginta, los Padres,
 * los pseudoepígrafos— se intenta el original, y solo si el teléfono tiene voz
 * para el griego o para el hebreo. Si no la tiene, se dice; no se lee el griego
 * con voz española, que suena a disparate y no ayuda a nadie.
 *
 * El griego antiguo no existe como lengua para el sintetizador: lo que hay es
 * griego moderno, que lee el texto con la pronunciación de hoy. Es una de las
 * formas aceptadas de leer el koiné en voz alta, así que sirve. Con el hebreo
 * pasa lo mismo: la voz es de hebreo israelí.
 *
 * **El motor se cierra al salir de la pantalla.** Mantenerlo abierto toda la
 * vida de la aplicación deja atado un servicio del sistema sin motivo.
 */
class Lector(contexto: Context) {

    /** Qué se está leyendo ahora mismo, o `null` si no suena nada. */
    private val _leyendo = MutableStateFlow<String?>(null)
    val leyendo: StateFlow<String?> = _leyendo.asStateFlow()

    private var listo = false

    /**
     * Lo que se pidió leer antes de que el motor arrancara. Arrancar tarda unas
     * décimas, y quien toca el botón nada más abrir la pantalla llegaría antes
     * que el motor: sin esto, ese primer toque no haría nada.
     */
    private var enEspera: Peticion? = null

    private val motor = TextToSpeech(contexto.applicationContext) { estado ->
        listo = estado == TextToSpeech.SUCCESS
        val pendiente = enEspera
        enEspera = null
        if (listo && pendiente != null) {
            leer(pendiente.lengua, pendiente.trozos, pendiente.sinVoz)
        }
    }

    private data class Peticion(
        val lengua: Locale,
        val trozos: List<Trozo>,
        val sinVoz: (() -> Unit)?,
    )

    init {
        motor.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
            override fun onStart(id: String?) {
                _leyendo.value = id
            }

            override fun onDone(id: String?) {
                // Solo se apaga si el que acaba es el último que se puso a
                // sonar: con la cola llena, el onDone de un versículo llega
                // después de que el siguiente ya haya empezado.
                if (_leyendo.value == id) _leyendo.value = null
            }

            // La firma sin código de error está obsoleta pero sigue siendo
            // abstracta: hay que implementarla.
            override fun onError(id: String?) {
                if (_leyendo.value == id) _leyendo.value = null
            }

            override fun onError(id: String?, codigo: Int) {
                if (_leyendo.value == id) _leyendo.value = null
            }
        })
    }

    /** Un fragmento con su identificador, para saber cuál suena en cada momento. */
    data class Trozo(val id: String, val texto: String)

    /**
     * Lee los trozos seguidos, en una sola lengua. Lo que estuviera sonando se
     * corta.
     *
     * [sinVoz] se llama, en el hilo principal, si el teléfono no tiene voz para
     * esa lengua. La comprobación va aquí dentro y no fuera a propósito: antes
     * de que el motor termine de arrancar, preguntar por una lengua contesta
     * siempre que no, y quien toca el botón nada más abrir la pantalla llega
     * antes que el motor. Lo que se pide sin motor se guarda y se resuelve —se
     * lee o se avisa— cuando el motor ya puede contestar.
     */
    fun leer(lengua: Locale, trozos: List<Trozo>, sinVoz: (() -> Unit)? = null) {
        if (trozos.isEmpty()) return
        if (!listo) {
            enEspera = Peticion(lengua, trozos, sinVoz)
            return
        }
        if (sinVoz != null && motor.isLanguageAvailable(lengua) < TextToSpeech.LANG_AVAILABLE) {
            Handler(Looper.getMainLooper()).post(sinVoz)
            return
        }
        motor.stop()
        motor.language = lengua
        // Un punto por debajo del habla normal. El texto bíblico tiene frases
        // largas y la velocidad de fábrica las atropella.
        motor.setSpeechRate(0.92f)
        trozos.forEachIndexed { i, trozo ->
            val modo = if (i == 0) TextToSpeech.QUEUE_FLUSH else TextToSpeech.QUEUE_ADD
            motor.speak(trozo.texto, modo, null, trozo.id)
        }
    }

    fun detener() {
        if (listo) motor.stop()
        enEspera = null
        _leyendo.value = null
    }

    fun cerrar() {
        enEspera = null
        _leyendo.value = null
        runCatching {
            motor.stop()
            motor.shutdown()
        }
    }

    companion object {
        /**
         * El griego moderno, que es la única voz griega que existe. Lee el koiné
         * con la pronunciación de hoy: no es la de Atenas en el siglo V, pero es
         * una de las formas con las que hoy se lee el Nuevo Testamento en alto.
         */
        val GRIEGO: Locale = Locale.forLanguageTag("el")

        /** Hebreo israelí, por el mismo motivo. */
        val HEBREO: Locale = Locale.forLanguageTag("he")

        val ESPANOL: Locale = Locale.forLanguageTag("es")
    }
}
