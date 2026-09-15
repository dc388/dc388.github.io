package com.dc388.bibliagriega.data

import com.dc388.bibliagriega.BuildConfig

/**
 * Identificadores de AdMob y de la suscripción.
 *
 * Los valores no están escritos aquí: los genera `app/build.gradle.kts` a partir
 * de las variables ADMOB_APP_ID y ADMOB_BANNER, y por defecto usa los de prueba
 * de Google, que enseñan un anuncio de mentira y no pagan nada. El manifiesto
 * recibe el mismo identificador como recurso, así que no pueden discrepar.
 *
 * Una compilación de publicación con los de prueba falla a propósito.
 * Ver docs/ANUNCIOS_Y_SUSCRIPCION.md.
 */
object Anuncios {
    /** Identificador de la aplicación en AdMob; va también en el manifiesto. */
    const val APP_ID: String = BuildConfig.ADMOB_APP_ID

    /** Bloque de anuncios del banner que va al pie del lector. */
    const val BANNER: String = BuildConfig.ADMOB_BANNER

    /** Producto de suscripción que quita los anuncios, creado en Play Console. */
    const val SUSCRIPCION_SIN_ANUNCIOS = "sin_anuncios_mensual"

    /** Cierto mientras se usen los identificadores de prueba de Google. */
    const val EN_PRUEBAS: Boolean = BuildConfig.ADMOB_DE_PRUEBA
}
