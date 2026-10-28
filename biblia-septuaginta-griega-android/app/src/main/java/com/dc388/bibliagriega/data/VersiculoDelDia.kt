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
        VersiculoDiario(
            referencia = "Juan 3:16",
            coleccion = "nt", codigo = "JUA", capitulo = 3, versiculo = 16,
            original = "Οὕτως γὰρ ἠγάπησεν ὁ θεὸς τὸν κόσμον, ὥστε τὸν υἱὸν " +
                "αὐτοῦ τὸν μονογενῆ ἔδωκεν, ἵνα πᾶς ὁ πιστεύων εἰς αὐτὸν " +
                "μὴ ἀπόληται, ἀλλ’ ἔχῃ ζωὴν αἰώνιον.",
            espanol = "Porque de tal manera amó Dios al mundo, que ha dado a su " +
                "Hijo unigénito, para que todo aquel que en él cree, no " +
                "se pierda, mas tenga vida eterna.",
            palabra = "οὕτως",
            translit = "hoútos",
            reflexion = "«De tal manera» no mide cantidad, mide modo: el adverbio " +
                "griego dice «así», de esta forma. La frase no es «amó " +
                "tanto» sino «así amó», y lo que viene detrás —que dio a " +
                "su Hijo— es ese así.",
        ),
        VersiculoDiario(
            referencia = "Proverbios 3:5",
            coleccion = "at", codigo = "PRO", capitulo = 3, versiculo = 5,
            original = "בְּטַ֣ח אֶל־יְ֭הוָה בְּכָל־לִבֶּ֑ךָ וְאֶל־בִּֽ֝ינָתְךָ֗ " +
                "אַל־תִּשָּׁעֵֽן׃",
            espanol = "Fíate de Jehová de todo tu corazón, y no estribes en tu " +
                "prudencia.",
            palabra = "לִבֶּךָ",
            translit = "libbejá",
            reflexion = "«Corazón» en hebreo no es el sentimiento frente a la " +
                "cabeza: לֵב es también la voluntad y el entendimiento. " +
                "El versículo no opone corazón a razón; opone confiar con " +
                "todo lo que uno es a apoyarse solo en lo que uno " +
                "entiende.",
        ),
        VersiculoDiario(
            referencia = "Josué 1:9",
            coleccion = "at", codigo = "JOS", capitulo = 1, versiculo = 9,
            original = "הֲל֤וֹא צִוִּיתִ֨יךָ֙ חֲזַ֣ק וֶאֱמָ֔ץ אַֽל־תַּעֲרֹ֖ץ " +
                "וְאַל־תֵּחָ֑ת כִּ֤י עִמְּךָ֙ יְהוָ֣ה אֱלֹהֶ֔יךָ בְּכֹ֖ל " +
                "אֲשֶׁ֥ר תֵּלֵֽךְ׃פ",
            espanol = "Mira que te mando que te esfuerces y seas valiente: no " +
                "temas ni desmayes, porque Jehová tu Dios será contigo en " +
                "donde quiera que fueres.",
            palabra = "צִוִּיתִיךָ",
            translit = "tsivvitíja",
            reflexion = "El valor aquí no es un consejo: es una orden, y en " +
                "perfecto —«ya te lo mandé»—, con el «te» dentro de la " +
                "misma palabra. Josué no tiene que fabricarse el ánimo: " +
                "tiene que obedecer algo que ya está mandado.",
        ),
        VersiculoDiario(
            referencia = "Jeremías 29:11",
            coleccion = "at", codigo = "JER", capitulo = 29, versiculo = 11,
            original = "כִּי֩ אָנֹכִ֨י יָדַ֜עְתִּי אֶת־הַמַּחֲשָׁבֹ֗ת אֲשֶׁ֧ר " +
                "אָנֹכִ֛י חֹשֵׁ֥ב עֲלֵיכֶ֖ם נְאֻם־יְהוָ֑ה מַחְשְׁב֤וֹת " +
                "שָׁלוֹם֙ וְלֹ֣א לְרָעָ֔ה לָתֵ֥ת לָכֶ֖ם אַחֲרִ֥ית " +
                "וְתִקְוָֽה׃",
            espanol = "Porque yo sé los pensamientos que tengo acerca de " +
                "vosotros, dice Jehová, pensamientos de paz, y no de mal, " +
                "para daros el fin que esperáis.",
            palabra = "מַחְשְׁבוֹת",
            translit = "majshevót",
            reflexion = "«Pensamientos» traduce una palabra de artesano: el plan " +
                "trazado, el diseño de lo que se va a fabricar. Y el " +
                "verbo que la acompaña va en participio: no los pensó una " +
                "vez, los está pensando.",
        ),
        VersiculoDiario(
            referencia = "Mateo 11:28",
            coleccion = "nt", codigo = "MAT", capitulo = 11, versiculo = 28,
            original = "Δεῦτε πρός με πάντες οἱ κοπιῶντες καὶ πεφορτισμένοι, " +
                "κἀγὼ ἀναπαύσω ὑμᾶς.",
            espanol = "Venid a mí todos los que estáis trabajados y cargados, " +
                "que yo os haré descansar.",
            palabra = "πεφορτισμένοι",
            translit = "pephortisménoi",
            reflexion = "«Cargados» es participio perfecto y pasivo: no se " +
                "cargaron solos, se lo echaron encima, y siguen así. " +
                "Jesús no llama a los que eligieron mal el peso; llama a " +
                "los que llevan uno que les pusieron.",
        ),
        VersiculoDiario(
            referencia = "Salmos 46:11",
            coleccion = "at", codigo = "SAL", capitulo = 46, versiculo = 11,
            original = "הַרְפּ֣וּ וּ֭דְעוּ כִּי־אָנֹכִ֣י אֱלֹהִ֑ים אָר֥וּם " +
                "בַּ֝גּוֹיִ֗ם אָר֥וּם בָּאָֽרֶץ׃",
            espanol = "Estad quietos, y conoced que yo soy Dios: ensalzado he " +
                "de ser entre las gentes, ensalzado seré en la tierra.",
            palabra = "הַרְפּוּ",
            translit = "harpú",
            reflexion = "«Estad quietos» es el verbo de aflojar la mano: soltad. " +
                "No pide silencio interior ni calma de ánimo; pide dejar " +
                "de agarrar. Y está dicho en plural, a un pueblo en medio " +
                "de la guerra.",
        ),
        VersiculoDiario(
            referencia = "Isaías 40:31",
            coleccion = "at", codigo = "ISA", capitulo = 40, versiculo = 31,
            original = "וְקוֹיֵ֤ יְהוָה֙ יַחֲלִ֣יפוּ כֹ֔חַ יַעֲל֥וּ אֵ֖בֶר " +
                "כַּנְּשָׁרִ֑ים יָר֨וּצוּ֙ וְלֹ֣א יִיגָ֔עוּ יֵלְכ֖וּ " +
                "וְלֹ֥א יִיעָֽפוּ׃פ",
            espanol = "Mas los que esperan a Jehová tendrán nuevas fuerzas; " +
                "levantarán las alas como águilas; correrán, y no se " +
                "cansarán; caminarán, y no se fatigarán.",
            palabra = "יַחֲלִיפוּ",
            translit = "yajalífu",
            reflexion = "«Tendrán nuevas fuerzas» traduce un verbo de cambiar: el " +
                "mismo con el que Jacob manda mudarse de ropa en Génesis " +
                "35. No les añaden fuerza a la que tienen: cambian la " +
                "suya por otra.",
        ),
        VersiculoDiario(
            referencia = "2 Corintios 5:17",
            coleccion = "nt", codigo = "2CO", capitulo = 5, versiculo = 17,
            original = "Ὥστε εἴ τις ἐν χριστῷ, καινὴ κτίσις· τὰ ἀρχαῖα παρῆλθεν, " +
                "ἰδού, γέγονεν καινὰ τὰ πάντα.",
            espanol = "De modo que si alguno está en Cristo, nueva criatura es: " +
                "las cosas viejas pasaron; he aquí todas son hechas " +
                "nuevas.",
            palabra = "κτίσις",
            translit = "ktísis",
            reflexion = "No dice «nueva criatura»: κτίσις es la creación, el acto " +
                "de crear. Y la frase no tiene verbo —«si alguno en " +
                "Cristo, creación nueva»—, así que no se dice cuándo " +
                "empieza ni cuánto dura. Se dice que es.",
        ),
        VersiculoDiario(
            referencia = "Gálatas 2:20",
            coleccion = "nt", codigo = "GAL", capitulo = 2, versiculo = 20,
            original = "Χριστῷ συνεσταύρωμαι· ζῶ δέ, οὐκέτι ἐγώ, ζῇ δὲ ἐν ἐμοὶ " +
                "χριστός· ὃ δὲ νῦν ζῶ ἐν σαρκί, ἐν πίστει ζῶ τῇ τοῦ υἱοῦ " +
                "τοῦ θεοῦ, τοῦ ἀγαπήσαντός με καὶ παραδόντος ἑαυτὸν ὑπὲρ " +
                "ἐμοῦ.",
            espanol = "Con Cristo estoy juntamente crucificado, y vivo, no ya " +
                "yo, mas vive Cristo en mí: y lo que ahora vivo en la " +
                "carne, lo vivo en la fe del Hijo de Dios, el cual me " +
                "amó, y se entregó a sí mismo por mí.",
            palabra = "συνεσταύρωμαι",
            translit = "synestaúromai",
            reflexion = "«Estoy crucificado» va en perfecto: una acción terminada " +
                "cuyo efecto sigue en pie. No dice que Pablo se " +
                "crucifique cada día; dice que aquello ya pasó y que " +
                "desde ahí vive. El συν- de delante es «junto con».",
        ),
        VersiculoDiario(
            referencia = "Efesios 2:8",
            coleccion = "nt", codigo = "EFE", capitulo = 2, versiculo = 8,
            original = "τῇ γὰρ χάριτί ἐστε σεσῳσμένοι διὰ τῆς πίστεως, καὶ τοῦτο " +
                "οὐκ ἐξ ὑμῶν· θεοῦ τὸ δῶρον·",
            espanol = "Porque por gracia sois salvos por la fe; y esto no de " +
                "vosotros, pues es don de Dios:",
            palabra = "σεσῳσμένοι",
            translit = "sesosménoi",
            reflexion = "«Sois salvos» son dos palabras en griego: «sois» más un " +
                "participio perfecto pasivo. Ni se está salvando uno ni " +
                "va a salvarse: la obra está hecha, la hizo otro, y el " +
                "estado dura.",
        ),
        VersiculoDiario(
            referencia = "Hebreos 11:1",
            coleccion = "nt", codigo = "HEB", capitulo = 11, versiculo = 1,
            original = "Ἔστιν δὲ πίστις ἐλπιζομένων ὑπόστασις, πραγμάτων ἔλεγχος " +
                "οὐ βλεπομένων.",
            espanol = "ES pues la fe la sustancia de las cosas que se esperan, " +
                "la demostración de las cosas que no se ven.",
            palabra = "ὑπόστασις",
            translit = "hypóstasis",
            reflexion = "ὑπόστασις es, al pie de la letra, «lo que se pone " +
                "debajo»: el cimiento. La fe no se define aquí como la " +
                "esperanza de que algo ocurra, sino como el suelo sobre " +
                "el que ya se está de pie mientras no se ve.",
        ),
        VersiculoDiario(
            referencia = "Santiago 1:2",
            coleccion = "nt", codigo = "SAN", capitulo = 1, versiculo = 2,
            original = "Πᾶσαν χαρὰν ἡγήσασθε, ἀδελφοί μου, ὅταν πειρασμοῖς " +
                "περιπέσητε ποικίλοις,",
            espanol = "Hermanos míos, tened por sumo gozo cuando cayereis en " +
                "diversas tentaciones;",
            palabra = "ἡγήσασθε",
            translit = "hēgḗsasthe",
            reflexion = "«Tened por» es el verbo de llevar la cuenta, de hacer el " +
                "cálculo. Santiago no manda sentir alegría en la prueba: " +
                "manda apuntarla en la columna de las ganancias. Lo " +
                "primero no se puede mandar; lo segundo sí.",
        ),
        VersiculoDiario(
            referencia = "1 Pedro 5:7",
            coleccion = "nt", codigo = "1PE", capitulo = 5, versiculo = 7,
            original = "πᾶσαν τὴν μέριμναν ὑμῶν ἐπιρρίψαντες ἐπ’ αὐτόν, ὅτι αὐτῷ " +
                "μέλει περὶ ὑμῶν.",
            espanol = "Echando toda vuestra solicitud en él, porque él tiene " +
                "cuidado de vosotros.",
            palabra = "μέλει",
            translit = "mélei",
            reflexion = "«Tiene cuidado de vosotros» es un verbo impersonal: «a " +
                "él le importa». Y lo que se le echa encima, μέριμνα, es " +
                "la misma palabra que Jesús prohíbe en Mateo 6. Lo que " +
                "allí se manda soltar, aquí se dice dónde ponerlo.",
        ),
        VersiculoDiario(
            referencia = "Romanos 12:2",
            coleccion = "nt", codigo = "ROM", capitulo = 12, versiculo = 2,
            original = "καὶ μὴ συσχηματίζεσθαι τῷ αἰῶνι τούτῳ, ἀλλὰ " +
                "μεταμορφοῦσθαι τῇ ἀνακαινώσει τοῦ νοὸς ὑμῶν, εἰς τὸ " +
                "δοκιμάζειν ὑμᾶς τί τὸ θέλημα τοῦ θεοῦ τὸ ἀγαθὸν καὶ " +
                "εὐάρεστον καὶ τέλειον.",
            espanol = "Y no os conforméis a este siglo; mas reformaos por la " +
                "renovación de vuestro entendimiento, para que " +
                "experimentéis cuál sea la buena voluntad de Dios, " +
                "agradable y perfecta.",
            palabra = "μεταμορφοῦσθαι",
            translit = "metamorphoûsthai",
            reflexion = "«Reformaos» es el verbo del que viene «metamorfosis», y " +
                "va en pasiva: no es «cambiad», es «dejaos cambiar». El " +
                "verbo de antes, el de amoldarse al siglo, va en media: " +
                "eso sí lo hace uno solo.",
        ),
        VersiculoDiario(
            referencia = "Filipenses 4:7",
            coleccion = "nt", codigo = "FIL", capitulo = 4, versiculo = 7,
            original = "Καὶ ἡ εἰρήνη τοῦ θεοῦ ἡ ὑπερέχουσα πάντα νοῦν, φρουρήσει " +
                "τὰς καρδίας ὑμῶν καὶ τὰ νοήματα ὑμῶν ἐν χριστῷ Ἰησοῦ.",
            espanol = "Y la paz de Dios, que sobrepuja todo entendimiento, " +
                "guardará vuestros corazones y vuestros entendimientos en " +
                "Cristo Jesús.",
            palabra = "φρουρήσει",
            translit = "phrourḗsei",
            reflexion = "«Guardará» es un verbo militar: montar guardia, poner " +
                "centinelas a las puertas. La paz de Dios no se describe " +
                "como un sentimiento, sino como una guarnición puesta " +
                "alrededor del corazón.",
        ),
        VersiculoDiario(
            referencia = "Mateo 5:4",
            coleccion = "nt", codigo = "MAT", capitulo = 5, versiculo = 4,
            original = "Μακάριοι οἱ πενθοῦντες· ὅτι αὐτοὶ παρακληθήσονται.",
            espanol = "Bienaventurados los que lloran: porque ellos recibirán " +
                "consolación.",
            palabra = "παρακληθήσονται",
            translit = "paraklēthḗsontai",
            reflexion = "«Recibirán consolación» es, literalmente, «serán " +
                "llamados al lado». Es el verbo del que sale Παράκλητος, " +
                "el que Jesús promete en Juan. No se promete que se les " +
                "pase el dolor: se promete que alguien se pondrá a su " +
                "lado.",
        ),
        VersiculoDiario(
            referencia = "Romanos 5:8",
            coleccion = "nt", codigo = "ROM", capitulo = 5, versiculo = 8,
            original = "Συνίστησιν δὲ τὴν ἑαυτοῦ ἀγάπην εἰς ἡμᾶς ὁ θεός, ὅτι ἔτι " +
                "ἁμαρτωλῶν ὄντων ἡμῶν χριστὸς ὑπὲρ ἡμῶν ἀπέθανεν.",
            espanol = "Mas Dios encarece su caridad para con nosotros, porque " +
                "siendo aún pecadores, Cristo murió por nosotros.",
            palabra = "συνίστησιν",
            translit = "synístēsin",
            reflexion = "«Encarece» es poner una cosa junto a otra para que se " +
                "vea: demostrar exhibiendo. Y va en presente, no en " +
                "pasado. Lo que se exhibe ocurrió hace dos mil años; la " +
                "exhibición sigue.",
        ),
        VersiculoDiario(
            referencia = "Miqueas 6:8",
            coleccion = "at", codigo = "MIQ", capitulo = 6, versiculo = 8,
            original = "הִגִּ֥יד לְךָ֛ אָדָ֖ם מַה־טּ֑וֹב וּמָֽה־יְהוָ֞ה " +
                "דּוֹרֵ֣שׁ מִמְּךָ֗ כִּ֣י אִם־עֲשׂ֤וֹת מִשְׁפָּט֙ " +
                "וְאַ֣הֲבַת חֶ֔סֶד וְהַצְנֵ֥עַ לֶ֖כֶת עִם־אֱלֹהֶֽיךָ׃פ",
            espanol = "Oh hombre, él te ha declarado qué sea lo bueno, y qué " +
                "pida de ti Jehová: solamente hacer juicio, y amar " +
                "misericordia, y humillarte para andar con tu Dios.",
            palabra = "הַצְנֵעַ",
            translit = "hatsnéa",
            reflexion = "Las tres cosas no son tres. Las dos primeras son hacer " +
                "juicio y amar misericordia; la tercera no es " +
                "«humillarte», sino «andar humildemente»: el verbo raro " +
                "va pegado a «andar» y le dice cómo. No se pide un " +
                "sentimiento, se pide un modo de caminar.",
        ),
        VersiculoDiario(
            referencia = "Sofonías 3:17",
            coleccion = "at", codigo = "SOF", capitulo = 3, versiculo = 17,
            original = "יְהוָ֧ה אֱלֹהַ֛יִךְ בְּקִרְבֵּ֖ך גִּבּ֣וֹר יוֹשִׁ֑יעַ " +
                "יָשִׂ֨ישׂ עָלַ֜יִךְ בְּשִׂמְחָ֗ה יַחֲרִישׁ֙ " +
                "בְּאַ֣הֲבָת֔וֹ יָגִ֥יל עָלַ֖יִךְ בְּרִנָּֽה׃",
            espanol = "Jehová en medio de ti, poderoso, él salvará; gozaráse " +
                "sobre ti con alegría, callará de amor, se regocijará " +
                "sobre ti con cantar.",
            palabra = "יַחֲרִישׁ",
            translit = "yajarísh",
            reflexion = "Entre dos verbos de alegría a gritos, uno de silencio: " +
                "«callará de amor». El hebreo pone a Dios gozándose, " +
                "callando y gritando por el mismo motivo. El silencio no " +
                "es aquí la ausencia de nada: va en la lista con los " +
                "otros dos.",
        ),
        VersiculoDiario(
            referencia = "Lamentaciones 3:23",
            coleccion = "at", codigo = "LAM", capitulo = 3, versiculo = 23,
            original = "חֲדָשִׁים֙ לַבְּקָרִ֔ים רַבָּ֖ה אֱמוּנָתֶֽךָ׃",
            espanol = "Nuevas son cada mañana; grande es tu fidelidad.",
            palabra = "אֱמוּנָתֶךָ",
            translit = "emunatejá",
            reflexion = "«Fidelidad» es, al pie de la letra, firmeza: lo que no " +
                "se mueve. De esa misma raíz sale el «amén». Lo que se " +
                "dice nuevo cada mañana no es un sentimiento de Dios: es " +
                "que sigue estando donde estaba.",
        ),
        VersiculoDiario(
            referencia = "Salmos 1:2",
            coleccion = "at", codigo = "SAL", capitulo = 1, versiculo = 2,
            original = "כִּ֤י אִ֥ם בְּתוֹרַ֥ת יְהוָ֗ה חֶ֫פְצ֥וֹ וּֽבְתוֹרָת֥וֹ " +
                "יֶהְגֶּ֗ה יוֹמָ֥ם וָלָֽיְלָה׃",
            espanol = "Antes en la ley de Jehová está su delicia, y en su ley " +
                "medita de día y de noche.",
            palabra = "יֶהְגֶּה",
            translit = "yehgué",
            reflexion = "«Medita» es un verbo de ruido: murmurar, repetir a media " +
                "voz. Es el mismo que Isaías usa del león que ruge sobre " +
                "su presa. Meditar aquí no es quedarse callado pensando: " +
                "es ir diciendo el texto por lo bajo.",
        ),
        VersiculoDiario(
            referencia = "Salmos 139:14",
            coleccion = "at", codigo = "SAL", capitulo = 139, versiculo = 14,
            original = "אֽוֹדְךָ֗ עַ֤ל כִּ֥י נוֹרָא֗וֹת נִ֫פְלֵ֥יתִי נִפְלָאִ֥ים " +
                "מַעֲשֶׂ֑יךָ וְ֝נַפְשִׁ֗י יֹדַ֥עַת מְאֹֽד׃",
            espanol = "Te alabaré; porque formidables, maravillosas son tus " +
                "obras: estoy maravillado, y mi alma lo conoce mucho.",
            palabra = "נוֹרָאוֹת",
            translit = "noraót",
            reflexion = "«Formidables» es el participio del verbo temer: cosas " +
                "que dan temor reverente. Lo que el salmo dice de cómo " +
                "está hecho uno no es que sea bonito ni especial: es que " +
                "impone, como impone lo que hace Dios.",
        ),
        VersiculoDiario(
            referencia = "Deuteronomio 31:6",
            coleccion = "at", codigo = "DEU", capitulo = 31, versiculo = 6,
            original = "חִזְק֣וּ וְאִמְצ֔וּ אַל־תִּֽירְא֥וּ וְאַל־תַּעַרְצ֖וּ " +
                "מִפְּנֵיהֶ֑ם כִּ֣י ׀ יְהוָ֣ה אֱלֹהֶ֗יךָ ה֚וּא הַהֹלֵ֣ךְ " +
                "עִמָּ֔ךְ לֹ֥א יַרְפְּךָ֖ וְלֹ֥א יַעַזְבֶֽךָּ׃פ",
            espanol = "Esforzaos y cobrad ánimo; no temáis, ni tengáis miedo de " +
                "ellos: que Jehová tu Dios es el que va contigo: no te " +
                "dejará ni te desamparará.",
            palabra = "יַרְפְּךָ",
            translit = "yarpejá",
            reflexion = "«No te dejará» es el verbo de aflojar la mano, el mismo " +
                "que en el Salmo 46 se nos manda a nosotros: «soltad». A " +
                "nosotros se nos manda soltar; de él se dice que no " +
                "soltará.",
        ),
    )
}
