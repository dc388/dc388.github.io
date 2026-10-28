package com.dc388.bibliagriega.ui

/**
 * El texto con el que un versículo sale de la aplicación.
 *
 * Hasta ahora se compartía «Juan 3:16» y el griego, y nada más. Cada versículo
 * que alguien reenviaba era un anuncio que no se cobraba: quien lo recibía no
 * tenía forma de saber de dónde salía ni dónde conseguirlo.
 *
 * El formato imita el de los mensajes que la gente ya reenvía por WhatsApp
 * —asterisco para negrita, guion bajo para cursiva— porque ahí es donde van a
 * acabar. No es decoración: en WhatsApp y Telegram eso se ve como negrita y
 * cursiva de verdad, y un versículo con la referencia destacada se lee de un
 * vistazo en una conversación.
 *
 * El español va primero y el original debajo. El español es lo que se reenvía y
 * lo que entiende quien lo recibe; el griego o el hebreo es lo que distingue a
 * esta aplicación de las otras cincuenta que mandan un versículo al día.
 */
object Compartir {

    const val ENLACE = "https://play.google.com/store/apps/details?id=com.dc388.bibliagriega"

    private const val NOMBRE = "Biblia Griega y Hebrea"

    /**
     * Arma el mensaje de un versículo.
     *
     * [espanol] y [reflexion] pueden faltar: la Septuaginta no lleva traducción
     * para todo, y la reflexión solo existe en los versículos del día. Cuando
     * faltan no se deja el hueco ni se escribe un sustituto: se omite el bloque.
     */
    fun versiculo(
        referencia: String,
        original: String,
        espanol: String? = null,
        reflexion: String? = null,
    ): String = buildString {
        append("✝ *").append(referencia).append("*\n")

        espanol?.takeIf { it.isNotBlank() }?.let {
            append("\n_«").append(it.trim()).append("»_\n")
        }

        if (original.isNotBlank()) {
            append("\n").append(original.trim()).append("\n")
        }

        reflexion?.takeIf { it.isNotBlank() }?.let {
            append("\n").append(it.trim()).append("\n")
        }

        append("\n📖 *").append(NOMBRE).append("*\n").append(ENLACE)
    }
}
