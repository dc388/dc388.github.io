package com.dc388.bibliagriega.data

import android.app.Activity
import android.content.Context
import com.android.billingclient.api.AcknowledgePurchaseParams
import com.android.billingclient.api.BillingClient
import com.android.billingclient.api.BillingClientStateListener
import com.android.billingclient.api.BillingFlowParams
import com.android.billingclient.api.BillingResult
import com.android.billingclient.api.PendingPurchasesParams
import com.android.billingclient.api.ProductDetails
import com.android.billingclient.api.Purchase
import com.android.billingclient.api.QueryProductDetailsParams
import com.android.billingclient.api.QueryPurchasesParams
import com.android.billingclient.api.acknowledgePurchase
import com.android.billingclient.api.queryPurchasesAsync
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.SupervisorJob
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import kotlinx.coroutines.suspendCancellableCoroutine
import kotlin.coroutines.resume

/**
 * La suscripción que quita los anuncios.
 *
 * Google Play es quien sabe si está pagada, no la aplicación: se le pregunta al
 * arrancar y cada vez que se vuelve del proceso de compra. No se guarda la
 * respuesta en el teléfono, porque un archivo local se edita y esto no es un
 * secreto que merezca la pena defender mal.
 *
 * Sin conexión, Play responde con lo último que sabe, así que quien haya pagado
 * sigue sin ver anuncios aunque abra la aplicación en modo avión.
 */
class Compras private constructor(context: Context) {

    private val alcance = CoroutineScope(SupervisorJob() + Dispatchers.IO)

    private val _sinAnuncios = MutableStateFlow(false)

    /** Si es cierto, la suscripción está activa y no se muestra publicidad. */
    val sinAnuncios: StateFlow<Boolean> = _sinAnuncios.asStateFlow()

    private val _estadoConocido = MutableStateFlow(false)

    /**
     * Cierto cuando Play ya ha contestado, para bien o para mal.
     *
     * Hace falta antes de arrancar los anuncios: mientras no se sabe, [sinAnuncios]
     * vale `false` por defecto, y arrancar con eso enseñaría publicidad a quien
     * la ha pagado.
     */
    val estadoConocido: StateFlow<Boolean> = _estadoConocido.asStateFlow()

    private val _precio = MutableStateFlow<String?>(null)

    /** El precio ya formateado en la moneda del usuario, tal y como lo da Play. */
    val precio: StateFlow<String?> = _precio.asStateFlow()

    private var detalles: ProductDetails? = null

    private val cliente = BillingClient.newBuilder(context.applicationContext)
        .enablePendingPurchases(PendingPurchasesParams.newBuilder().enableOneTimeProducts().build())
        .setListener { resultado, compras ->
            if (resultado.responseCode == BillingClient.BillingResponseCode.OK && compras != null) {
                alcance.launch { procesar(compras) }
            }
        }
        .build()

    init {
        conectar()
    }

    private fun conectar() {
        cliente.startConnection(object : BillingClientStateListener {
            override fun onBillingSetupFinished(resultado: BillingResult) {
                if (resultado.responseCode != BillingClient.BillingResponseCode.OK) {
                    // Sin Play —un teléfono sin servicios de Google, por ejemplo—
                    // no hay suscripción posible, pero tampoco hay que dejar la
                    // aplicación esperando una respuesta que no va a llegar.
                    _estadoConocido.value = true
                    return
                }
                alcance.launch {
                    consultarEstado()
                    consultarPrecio()
                }
            }

            override fun onBillingServiceDisconnected() {
                // Play se reinicia de vez en cuando; se reintenta al siguiente uso.
            }
        })
    }

    /** Pregunta a Play si la suscripción está activa. */
    suspend fun consultarEstado() {
        if (!cliente.isReady) return
        val respuesta = cliente.queryPurchasesAsync(
            QueryPurchasesParams.newBuilder()
                .setProductType(BillingClient.ProductType.SUBS)
                .build(),
        )
        procesar(respuesta.purchasesList)
    }

    private suspend fun procesar(compras: List<Purchase>) {
        val activa = compras.firstOrNull {
            Anuncios.SUSCRIPCION_SIN_ANUNCIOS in it.products &&
                it.purchaseState == Purchase.PurchaseState.PURCHASED
        }
        _sinAnuncios.value = activa != null
        _estadoConocido.value = true

        // Play reembolsa a los tres días lo que no se confirma.
        if (activa != null && !activa.isAcknowledged) {
            cliente.acknowledgePurchase(
                AcknowledgePurchaseParams.newBuilder()
                    .setPurchaseToken(activa.purchaseToken)
                    .build(),
            )
        }
    }

    private suspend fun consultarPrecio() {
        if (!cliente.isReady) return
        val consulta = QueryProductDetailsParams.newBuilder()
            .setProductList(
                listOf(
                    QueryProductDetailsParams.Product.newBuilder()
                        .setProductId(Anuncios.SUSCRIPCION_SIN_ANUNCIOS)
                        .setProductType(BillingClient.ProductType.SUBS)
                        .build(),
                ),
            )
            .build()
        // Desde la versión 8 de la biblioteca, la respuesta separa los productos
        // que sí llegaron de los que no, así que se pide por el listener y se
        // devuelve solo la primera lista.
        val encontrados = suspendCancellableCoroutine { continuacion ->
            cliente.queryProductDetailsAsync(consulta) { _, respuesta ->
                if (continuacion.isActive) continuacion.resume(respuesta.productDetailsList)
            }
        }
        detalles = encontrados.firstOrNull()
        _precio.value = detalles
            ?.subscriptionOfferDetails
            ?.firstOrNull()
            ?.pricingPhases
            ?.pricingPhaseList
            ?.firstOrNull()
            ?.formattedPrice
    }

    /** Abre el diálogo de compra de Play. Sin él no hay suscripción posible. */
    fun suscribirse(activity: Activity) {
        val producto = detalles ?: return
        val oferta = producto.subscriptionOfferDetails?.firstOrNull() ?: return
        cliente.launchBillingFlow(
            activity,
            BillingFlowParams.newBuilder()
                .setProductDetailsParamsList(
                    listOf(
                        BillingFlowParams.ProductDetailsParams.newBuilder()
                            .setProductDetails(producto)
                            .setOfferToken(oferta.offerToken)
                            .build(),
                    ),
                )
                .build(),
        )
    }

    companion object {
        @Volatile
        private var instancia: Compras? = null

        fun get(context: Context): Compras =
            instancia ?: synchronized(this) {
                instancia ?: Compras(context).also { instancia = it }
            }
    }
}
