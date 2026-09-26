package com.dc388.bibliagriega.data

import android.app.Activity
import android.content.Context
import androidx.activity.ComponentActivity
import androidx.activity.result.contract.ActivityResultContracts
import com.google.android.play.core.appupdate.AppUpdateInfo
import com.google.android.play.core.appupdate.AppUpdateManagerFactory
import com.google.android.play.core.appupdate.AppUpdateOptions
import com.google.android.play.core.install.InstallStateUpdatedListener
import com.google.android.play.core.install.model.AppUpdateType
import com.google.android.play.core.install.model.InstallStatus
import com.google.android.play.core.install.model.UpdateAvailability
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

/**
 * Las actualizaciones dentro de la app, en el modo flexible de Google Play.
 *
 * Al abrir la app se le pregunta a Play si hay una versión nueva. Si la hay, Play
 * ofrece descargarla con su propio diálogo, y la descarga sigue mientras se lee.
 * Cuando termina, [lista] pasa a true y la app ofrece reiniciar; hasta entonces
 * no se interrumpe nada.
 *
 * Si quien lee dice que no, no se le vuelve a preguntar por esa misma versión:
 * se guarda el código que rechazó y solo se insiste cuando salga otra. Nunca se
 * obliga a actualizar.
 *
 * Fuera de Play —un APK instalado a mano, el emulador de las pruebas— Play no
 * contesta, y esto no hace nada.
 *
 * Hay que crearla antes de que la actividad arranque, porque registra un
 * lanzador de resultados, y Android solo lo permite en ese momento.
 */
class Actualizaciones(private val actividad: ComponentActivity) {
    private val gestor = AppUpdateManagerFactory.create(actividad)
    private val preferencias = actividad.getSharedPreferences(ARCHIVO, Context.MODE_PRIVATE)

    private val _lista = MutableStateFlow(false)

    /** true cuando la versión nueva ya está descargada y solo falta reiniciar. */
    val lista: StateFlow<Boolean> = _lista.asStateFlow()

    /** El código de versión que Play está ofreciendo ahora mismo. */
    private var ofrecida = 0

    private val lanzador = actividad.registerForActivityResult(
        ActivityResultContracts.StartIntentSenderForResult(),
    ) { resultado ->
        if (resultado.resultCode != Activity.RESULT_OK && ofrecida != 0) {
            preferencias.edit().putInt(RECHAZADA, ofrecida).apply()
        }
    }

    private val oyente = InstallStateUpdatedListener { estado ->
        if (estado.installStatus() == InstallStatus.DOWNLOADED) _lista.value = true
    }

    /** Se llama una vez, al crear la actividad. */
    fun comprobar() {
        gestor.registerListener(oyente)
        gestor.appUpdateInfo.addOnSuccessListener { info ->
            if (info.installStatus() == InstallStatus.DOWNLOADED) {
                _lista.value = true
            } else if (seOfrece(info)) {
                ofrecida = info.availableVersionCode()
                gestor.startUpdateFlowForResult(
                    info,
                    lanzador,
                    AppUpdateOptions.newBuilder(AppUpdateType.FLEXIBLE).build(),
                )
            }
        }
    }

    /**
     * Al volver a la app: si la descarga terminó mientras estaba en segundo
     * plano, el oyente no se enteró, así que se pregunta otra vez.
     */
    fun alVolver() {
        gestor.appUpdateInfo.addOnSuccessListener { info ->
            if (info.installStatus() == InstallStatus.DOWNLOADED) _lista.value = true
        }
    }

    /** Instala lo descargado. Play cierra la app y la vuelve a abrir. */
    fun reiniciar() {
        gestor.completeUpdate()
    }

    /** Quien lee prefiere seguir: se le vuelve a ofrecer la próxima vez que abra. */
    fun despues() {
        _lista.value = false
    }

    fun cerrar() {
        gestor.unregisterListener(oyente)
    }

    private fun seOfrece(info: AppUpdateInfo): Boolean =
        info.updateAvailability() == UpdateAvailability.UPDATE_AVAILABLE &&
            info.isUpdateTypeAllowed(AppUpdateType.FLEXIBLE) &&
            info.availableVersionCode() != preferencias.getInt(RECHAZADA, 0)

    private companion object {
        const val ARCHIVO = "actualizaciones"
        const val RECHAZADA = "version_rechazada"
    }
}
