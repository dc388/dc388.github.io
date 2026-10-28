package com.dc388.bibliagriega.data

import java.time.LocalDate

/**
 * El versículo del día, con la palabra del original que lo sostiene.
 *
 * Hay cincuenta aplicaciones que mandan un versículo cada mañana con una frase
 * de ánimo debajo. Lo que esta tiene y las otras no es el texto original, así
 * que la reflexión no es un comentario devocional: es **una palabra concreta
 * del griego o del hebreo y lo que esa palabra dice y la traducción no alcanza
 * a decir**. Ese es el único criterio. Si de un versículo no se puede sacar eso,
 * no entra en la lista, por conocido que sea.
 *
 * **Cada afirmación sale del propio texto o del léxico que la aplicación trae
 * dentro**, no de lo que uno recuerde. El análisis morfológico dice que el
 * קַוֵּה del Salmo 27:14 es piel y que el רֹעִי del 23:1 es participio; el
 * artículo de Brown-Driver-Briggs del H8159 es el que glosa «gaze not about».
 * La primera versión de Isaías 41:10 decía que «contigo» era la palabra de
 * estar del lado de alguien en un juicio: no lo es, era un matiz inventado, y
 * por eso la regla está escrita aquí arriba.
 *
 * El texto va aquí dentro y no se busca en la base de datos a propósito. El
 * aviso de la mañana tiene que poder componerse sin abrir la base, y además así
 * lo que se publica es exactamente lo aprobado. Está copiado de
 * `biblia/datos`, que es de donde sale también lo que muestra el lector, con
 * una sola excepción anotada abajo.
 */
data class VersiculoDiario(
    val referencia: String,
    /** Colección y código del libro, para poder abrir el lector donde toca. */
    val coleccion: String,
    val codigo: String,
    val capitulo: Int,
    val versiculo: Int,
    /** El texto en griego o en hebreo, tal como lo muestra el lector. */
    val original: String,
    /** La traducción, Reina-Valera de 1909, tal como la muestra el lector. */
    val espanol: String,
    /** La palabra del original de la que trata la reflexión. */
    val palabra: String,
    /** Cómo se lee esa palabra, para quien no conoce el alfabeto. */
    val translit: String,
    /** Qué dice esa palabra y la traducción no alcanza a decir. Dos o tres líneas. */
    val reflexion: String,
)

object VersiculoDelDia {

    /**
     * Devuelve el versículo de una fecha.
     *
     * Se reparte por el día del año y no al azar: dos personas que hablen el
     * mismo día tienen que haber recibido lo mismo, que es justo lo que hace
     * que alguien reenvíe el mensaje a otro. Mientras la lista no llegue a 366
     * entradas, el día del año da la vuelta sobre las que hay.
     */
    fun de(fecha: LocalDate): VersiculoDiario =
        CATALOGO[(fecha.dayOfYear - 1) % CATALOGO.size]

    /** Cuántos versículos hay escritos y aprobados. La lista crece por tandas. */
    val escritos: Int get() = CATALOGO.size

    private val CATALOGO = listOf(
        VersiculoDiario(
            referencia = "Salmos 27:14",
            coleccion = "at", codigo = "SAL", capitulo = 27, versiculo = 14,
            original = "קַוֵּ֗ה אֶל־יְה֫וָ֥ה חֲ֭זַק וְיַאֲמֵ֣ץ לִבֶּ֑ךָ וְ֝קַוֵּ֗ה אֶל־יְהוָֽה׃",
            espanol = "Aguarda a Jehová; esfuérzate, y aliéntese tu corazón: " +
                "sí, espera a Jehová.",
            palabra = "קַוֵּה",
            translit = "qavvéh",
            reflexion = "La misma palabra abre y cierra el versículo, antes y después " +
                "de «esfuérzate». Y no es esperar de brazos cruzados: va en piel, la " +
                "forma intensiva, y el léxico la glosa «esperar, o mirar con ansia». " +
                "Es una espera que mira.",
        ),
        VersiculoDiario(
            referencia = "Juan 1:1",
            coleccion = "nt", codigo = "JUA", capitulo = 1, versiculo = 1,
            original = "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν, " +
                "καὶ θεὸς ἦν ὁ λόγος.",
            // La Reina-Valera de 1909 abre cada capítulo con la primera palabra en
            // versalitas, y así viene en los datos: «EN el principio». En el lector
            // se respeta, pero este texto sale a WhatsApp solo, sin el capítulo
            // alrededor, y allí parece una errata. Son 560 versículos en toda la
            // Biblia; arreglarlo de raíz es tarea de los datos, no de aquí.
            espanol = "En el principio era el Verbo, y el Verbo era con Dios, " +
                "y el Verbo era Dios.",
            palabra = "ἦν",
            translit = "ên",
            reflexion = "«Era» traduce un imperfecto, y Juan lo repite tres veces aquí. " +
                "Dos versículos después cambia de verbo: todo lo demás ἐγένετο, llegó " +
                "a ser. Cuando el principio empezó, el Verbo no empezó: ya era.",
        ),
        VersiculoDiario(
            referencia = "Mateo 6:34",
            coleccion = "nt", codigo = "MAT", capitulo = 6, versiculo = 34,
            original = "Μὴ οὖν μεριμνήσητε εἰς τὴν αὔριον· ἡ γὰρ αὔριον μεριμνήσει " +
                "τὰ ἑαυτῆς. Ἀρκετὸν τῇ ἡμέρᾳ ἡ κακία αὐτῆς.",
            espanol = "Así que, no os congojéis por el día de mañana; que el día de " +
                "mañana traerá su fatiga: basta al día su afán.",
            palabra = "μεριμνήσει",
            translit = "merimnḗsei",
            reflexion = "El mismo verbo aparece dos veces, y la segunda el sujeto es el " +
                "día: «el mañana se preocupará de lo suyo». Jesús no quita del medio la " +
                "preocupación; se la pasa al día al que le toca.",
        ),
        VersiculoDiario(
            referencia = "Romanos 8:28",
            coleccion = "nt", codigo = "ROM", capitulo = 8, versiculo = 28,
            original = "Οἴδαμεν δὲ ὅτι τοῖς ἀγαπῶσιν τὸν θεὸν πάντα συνεργεῖ εἰς " +
                "ἀγαθόν, τοῖς κατὰ πρόθεσιν κλητοῖς οὖσιν.",
            espanol = "Y sabemos que a los que a Dios aman, todas las cosas les ayudan " +
                "a bien, es a saber, a los que conforme al propósito son llamados.",
            palabra = "συνεργεῖ",
            translit = "synergeî",
            reflexion = "No dice que todo sea bueno. Dice que todo coopera —συν-, junto; " +
                "-εργεῖ, trabaja— hacia un bien, y el verbo va en singular con un sujeto " +
                "plural: las cosas no tiran cada una por su lado.",
        ),
        VersiculoDiario(
            referencia = "Filipenses 4:13",
            coleccion = "nt", codigo = "FIL", capitulo = 4, versiculo = 13,
            original = "Πάντα ἰσχύω ἐν τῷ ἐνδυναμοῦντί με χριστῷ.",
            espanol = "Todo lo puedo en Cristo que me fortalece.",
            palabra = "πάντα",
            translit = "pánta",
            reflexion = "Pablo acaba de decir qué entra en ese «todo»: sé estar humillado " +
                "y sé tener abundancia, hartura y hambre (v. 12). No es todo lo que uno " +
                "quiera; es todo aquello que ya le está tocando vivir.",
        ),
        VersiculoDiario(
            referencia = "Salmos 23:1",
            coleccion = "at", codigo = "SAL", capitulo = 23, versiculo = 1,
            original = "מִזְמ֥וֹר לְדָוִ֑ד יְהוָ֥ה רֹ֝עִ֗י לֹ֣א אֶחְסָֽר׃",
            espanol = "Salmo de David. JEHOVÁ es mi pastor; nada me faltará.",
            palabra = "רֹעִי",
            translit = "ro'í",
            reflexion = "«Mi pastor» no es un título: es un participio, «el que me " +
                "apacienta», un oficio en marcha. Y en hebreo no hay verbo entre las dos " +
                "palabras: Jehová, pastoreándome. La frase ya está completa antes de que " +
                "él haga nada.",
        ),
        VersiculoDiario(
            referencia = "Isaías 41:10",
            coleccion = "at", codigo = "ISA", capitulo = 41, versiculo = 10,
            original = "אַל־תִּירָא֙ כִּ֣י עִמְּךָ־אָ֔נִי אַל־תִּשְׁתָּ֖ע כִּֽי־אֲנִ֣י " +
                "אֱלֹהֶ֑יךָ אִמַּצְתִּ֨יךָ֙ אַף־עֲזַרְתִּ֔יךָ אַף־תְּמַכְתִּ֖יךָ " +
                "בִּימִ֥ין צִדְקִֽי׃",
            espanol = "No temas, que yo soy contigo; no desmayes, que yo soy tu Dios que " +
                "te esfuerzo: siempre te ayudaré, siempre te sustentaré con la diestra " +
                "de mi justicia.",
            palabra = "אַל־תִּשְׁתָּע",
            translit = "'al-tishtá'",
            reflexion = "«No desmayes» traduce un verbo cuya raíz es fijar la vista, y el " +
                "léxico glosa esta forma «no andes mirando alrededor». No pide aguantar " +
                "el golpe: pide dejar de buscar de dónde vendrá el siguiente.",
        ),
    )
}
