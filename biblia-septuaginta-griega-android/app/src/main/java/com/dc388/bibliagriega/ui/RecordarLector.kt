package com.dc388.bibliagriega.ui

import androidx.compose.runtime.Composable
import androidx.compose.runtime.DisposableEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.platform.LocalContext
import com.dc388.bibliagriega.data.Lector

/**
 * Un lector atado a la pantalla: se abre al entrar y se cierra al salir.
 *
 * El sintetizador del sistema es un servicio al que hay que conectarse. Dejarlo
 * conectado mientras la aplicación viva, por si acaso, es tener atado un
 * servicio del sistema en todas las pantallas donde no se usa.
 */
@Composable
fun recordarLector(): Lector {
    val contexto = LocalContext.current.applicationContext
    val lector = remember { Lector(contexto) }
    DisposableEffect(lector) { onDispose { lector.cerrar() } }
    return lector
}
