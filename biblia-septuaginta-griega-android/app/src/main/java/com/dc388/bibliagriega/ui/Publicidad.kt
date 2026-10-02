package com.dc388.bibliagriega.ui

import android.app.Activity
import android.content.Context
import android.content.ContextWrapper
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.viewinterop.AndroidView
import com.dc388.bibliagriega.data.Anuncios
import com.google.android.gms.ads.AdRequest
import com.google.android.gms.ads.AdSize
import com.google.android.gms.ads.AdView
import com.google.android.gms.ads.MobileAds
import com.google.android.gms.ads.RequestConfiguration
import com.google.android.ump.ConsentRequestParameters
import com.google.android.ump.UserMessagingPlatform
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow

private val _listos = MutableStateFlow(false)

/**
 * Cierto cuando la aplicación se está ejecutando desde las pruebas de interfaz.
 *
 * Espresso solo está en el classpath de las pruebas, nunca en el APK que se
 * publica, así que su presencia es una señal fiable. Con anuncios, las pruebas
 * dependerían de que haya red y de que AdMob tenga inventario que servir, y
 * fallarían por motivos que no tienen nada que ver con leer la Biblia.
 */
private val enPruebasDeInterfaz: Boolean by lazy {
    runCatching { Class.forName("androidx.test.espresso.Espresso") }.isSuccess
}

/**
 * Cierto cuando hay consentimiento y el SDK de anuncios ya está en marcha.
 *
 * Mientras valga `false` no se dibuja ningún anuncio, ni siquiera el hueco: es
 * lo que hace que [prepararAnuncios] pueda decidir no arrancarlo —porque la
 * suscripción está activa o porque el usuario dijo que no— y nadie más tenga
 * que enterarse.
 */
val anunciosListos: StateFlow<Boolean> = _listos.asStateFlow()

/**
 * Pide el consentimiento donde hace falta y arranca los anuncios.
 *
 * En el espacio económico europeo y en el Reino Unido, servir publicidad sin
 * preguntar antes es ilegal, y Google rechaza la aplicación si no se hace: la
 * plataforma de mensajes al usuario (UMP) enseña el formulario cuando toca y no
 * molesta al resto del mundo.
 *
 * El SDK de anuncios no se inicializa hasta tener respuesta, porque hacerlo
 * antes ya cuenta como tratar datos.
 */
fun prepararAnuncios(activity: Activity, alTerminar: () -> Unit = {}) {
    if (enPruebasDeInterfaz) {
        alTerminar()
        return
    }
    if (_listos.value) {
        alTerminar()
        return
    }
    val consentimiento = UserMessagingPlatform.getConsentInformation(activity)
    consentimiento.requestConsentInfoUpdate(
        activity,
        ConsentRequestParameters.Builder().build(),
        {
            UserMessagingPlatform.loadAndShowConsentFormIfRequired(activity) {
                if (consentimiento.canRequestAds()) iniciarSdk(activity, alTerminar)
            }
        },
        {
            // Si la consulta falla —sin red, por ejemplo— se sigue solo si ya
            // había consentimiento de una vez anterior.
            if (consentimiento.canRequestAds()) iniciarSdk(activity, alTerminar)
        },
    )
}

private fun iniciarSdk(activity: Activity, alTerminar: () -> Unit) {
    // La aplicación es para un público general, no para niños, y así se declara:
    // es lo que dice la política de privacidad y lo que exige AdMob que se diga.
    MobileAds.setRequestConfiguration(
        RequestConfiguration.Builder()
            .setTagForChildDirectedTreatment(
                RequestConfiguration.TAG_FOR_CHILD_DIRECTED_TREATMENT_FALSE,
            )
            .build(),
    )
    MobileAds.initialize(activity) {
        _listos.value = true
        alTerminar()
    }
}

/**
 * La Activity que hay detrás de un Context de Compose.
 *
 * `LocalContext` no siempre es la Activity: los temas y las vistas la envuelven
 * en ContextWrapper, y un `as? Activity` a secas devuelve null justo cuando se
 * necesita, que es al abrir el diálogo de compra.
 */
tailrec fun Context.actividad(): Activity? = when (this) {
    is Activity -> this
    is ContextWrapper -> baseContext.actividad()
    else -> null
}

/**
 * El banner del pie del lector.
 *
 * Se dibuja solo si no hay suscripción activa y el SDK ya arrancó; quien paga
 * no ve ni el hueco, y quien no dio su consentimiento tampoco.
 *
 * Es un banner adaptativo: ocupa el ancho de la pantalla y la altura que Google
 * considera adecuada para ese ancho, en vez de un tamaño fijo que en tabletas
 * queda ridículo.
 */
@Composable
fun Banner(modifier: Modifier = Modifier) {
    val listos by anunciosListos.collectAsState()
    if (!listos) return

    AndroidView(
        modifier = modifier.fillMaxWidth(),
        factory = { ctx ->
            AdView(ctx).apply {
                adUnitId = Anuncios.BANNER
                val metricas = ctx.resources.displayMetrics
                setAdSize(
                    AdSize.getCurrentOrientationAnchoredAdaptiveBannerAdSize(
                        ctx,
                        (metricas.widthPixels / metricas.density).toInt(),
                    ),
                )
                loadAd(AdRequest.Builder().build())
            }
        },
        onRelease = { it.destroy() },
    )
}
