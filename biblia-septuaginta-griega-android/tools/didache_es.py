"""La Didaché, o Enseñanza de los doce apóstoles, traducida del griego.

Un manual de la iglesia primitiva, de finales del siglo I o comienzos del II:
los dos caminos de la vida y de la muerte (1-6), el bautismo (7), el ayuno y el
padrenuestro (8), la eucaristía (9-10), cómo recibir a los apóstoles y
profetas itinerantes (11-13) y la espera del Señor (16). Estuvo perdida hasta
que en 1873 apareció un manuscrito en Constantinopla.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

DIDACHE_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "Dos caminos hay, uno de la vida y otro de la muerte, y grande es "
            "la diferencia entre los dos caminos.",
    (1, 2): "El camino de la vida es, pues, este: Primeramente, amarás a Dios "
            "que te hizo; en segundo lugar, a tu prójimo como a ti mismo; y "
            "todo lo que no quieras que se haga contigo, tampoco tú lo hagas "
            "a otro.",
    (1, 3): "Y la enseñanza de estas palabras es esta: Bendecid a los que os "
            "maldicen, y orad por vuestros enemigos, y ayunad por los que os "
            "persiguen; porque ¿qué gracia hay si amáis a los que os aman? "
            "¿No hacen también lo mismo los gentiles? Mas vosotros amad a los "
            "que os aborrecen, y no tendréis enemigo.",
    (1, 4): "Apártate de los deseos carnales y corporales. Si alguno te da "
            "una bofetada en la mejilla derecha, vuélvele también la otra, y "
            "serás perfecto; si alguno te obliga a ir con él una milla, ve "
            "con él dos; si alguno te quita el manto, dale también la túnica; "
            "si alguno te quita lo tuyo, no se lo reclames, porque tampoco "
            "puedes.",
    (1, 5): "A todo el que te pida, dale, y no se lo reclames; porque el "
            "Padre quiere que a todos se dé de sus propios dones. "
            "Bienaventurado el que da conforme al mandamiento, porque es "
            "inocente. ¡Ay del que recibe! Porque si alguno recibe teniendo "
            "necesidad, será inocente; pero el que no tiene necesidad dará "
            "cuenta de por qué recibió y para qué; y puesto en prisión, será "
            "examinado acerca de lo que hizo, y no saldrá de allí hasta que "
            "pague el último cuadrante.",
    (1, 6): "Pero también acerca de esto se ha dicho: Sude tu limosna en tus "
            "manos, hasta que sepas a quién la das.",

    # Capítulo 2
    (2, 1): "Y el segundo mandamiento de la enseñanza es:",
    (2, 2): "No matarás; no adulterarás; no corromperás a los niños; no "
            "fornicarás; no hurtarás; no practicarás la magia; no usarás "
            "hechicerías; no matarás al niño por aborto, ni darás muerte al "
            "recién nacido; no codiciarás los bienes de tu prójimo.",
    (2, 3): "No perjurarás; no dirás falso testimonio; no hablarás mal; no "
            "guardarás rencor.",
    (2, 4): "No serás de doble parecer ni de doble lengua, porque lazo de "
            "muerte es la doble lengua.",
    (2, 5): "Tu palabra no será mentirosa ni vana, sino llena de obra.",
    (2, 6): "No serás avaro, ni rapaz, ni hipócrita, ni malicioso, ni "
            "soberbio. No tomarás mal consejo contra tu prójimo.",
    (2, 7): "No aborrecerás a ningún hombre, sino que a unos reprenderás, por "
            "otros orarás, y a otros amarás más que a tu alma.",

    # Capítulo 3
    (3, 1): "Hijo mío, huye de todo mal y de todo lo que se le parezca.",
    (3, 2): "No seas iracundo, porque la ira conduce al homicidio; ni celoso, "
            "ni pendenciero, ni violento; porque de todas estas cosas nacen "
            "los homicidios.",
    (3, 3): "Hijo mío, no seas codicioso, porque la codicia conduce a la "
            "fornicación; ni deshonesto en el hablar, ni altivo de ojos; "
            "porque de todas estas cosas nacen los adulterios.",
    (3, 4): "Hijo mío, no seas agorero, pues conduce a la idolatría; ni "
            "encantador, ni astrólogo, ni hacedor de purificaciones, ni "
            "quieras siquiera ver estas cosas; porque de todas estas cosas "
            "nace la idolatría.",
    (3, 5): "Hijo mío, no seas mentiroso, pues la mentira conduce al hurto; "
            "ni amador del dinero, ni vanaglorioso; porque de todas estas "
            "cosas nacen los hurtos.",
    (3, 6): "Hijo mío, no seas murmurador, pues conduce a la blasfemia; ni "
            "arrogante, ni de mal pensamiento; porque de todas estas cosas "
            "nacen las blasfemias.",
    (3, 7): "Sé, en cambio, manso, pues los mansos heredarán la tierra.",
    (3, 8): "Sé longánime, y misericordioso, y sin malicia, y sosegado, y "
            "bueno, y temblando siempre ante las palabras que has oído.",
    (3, 9): "No te ensalzarás a ti mismo, ni darás osadía a tu alma. No se "
            "juntará tu alma con los altivos, sino que andarás con los justos "
            "y humildes.",
    (3, 10): "Los sucesos que te acontezcan recíbelos como bienes, sabiendo "
             "que sin Dios nada sucede.",

    # Capítulo 4
    (4, 1): "Hijo mío, del que te habla la palabra de Dios te acordarás noche "
            "y día, y le honrarás como al Señor; porque donde se anuncia la "
            "soberanía del Señor, allí está el Señor.",
    (4, 2): "Y buscarás cada día el rostro de los santos, para que descanses "
            "en sus palabras.",
    (4, 3): "No desearás la división, sino que pondrás paz entre los que "
            "contienden; juzgarás con justicia; no harás acepción de personas "
            "al reprender las transgresiones.",
    (4, 4): "No andarás con doble ánimo sobre si será o no será.",
    (4, 5): "No seas de los que extienden las manos para recibir y las "
            "encogen para dar.",
    (4, 6): "Si tienes algo por el trabajo de tus manos, darás rescate por "
            "tus pecados.",
    (4, 7): "No dudarás en dar, ni al dar murmurarás; porque conocerás quién "
            "es el buen remunerador de la recompensa.",
    (4, 8): "No rechazarás al necesitado, sino que compartirás todas las "
            "cosas con tu hermano, y no dirás que son tuyas propias; porque "
            "si sois partícipes en lo inmortal, ¡cuánto más en las cosas "
            "mortales!",
    (4, 9): "No apartarás tu mano de tu hijo o de tu hija, sino que desde la "
            "juventud les enseñarás el temor de Dios.",
    (4, 10): "No mandarás con amargura a tu siervo o a tu sierva, que esperan "
             "en el mismo Dios, no sea que dejen de temer al Dios que está "
             "sobre ambos; porque no viene a llamar según la apariencia de "
             "las personas, sino a aquellos que el Espíritu preparó.",
    (4, 11): "Y vosotros, siervos, estaréis sujetos a vuestros señores, como "
             "a imagen de Dios, con reverencia y temor.",
    (4, 12): "Aborrecerás toda hipocresía y todo lo que no agrada al Señor.",
    (4, 13): "No abandones en modo alguno los mandamientos del Señor, sino "
             "guardarás lo que recibiste, sin añadir ni quitar nada.",
    (4, 14): "En la iglesia confesarás tus transgresiones, y no te acercarás "
             "a tu oración con mala conciencia. Este es el camino de la vida.",

    # Capítulo 5
    (5, 1): "Y el camino de la muerte es este: Ante todo, es malo y lleno de "
            "maldición: homicidios, adulterios, codicias, fornicaciones, "
            "hurtos, idolatrías, magias, hechicerías, rapiñas, falsos "
            "testimonios, hipocresías, doblez de corazón, engaño, soberbia, "
            "malicia, arrogancia, avaricia, deshonestidad en el hablar, "
            "celos, osadía, altivez, jactancia.",
    (5, 2): "Perseguidores de los buenos, que aborrecen la verdad, que aman "
            "la mentira, que no conocen la recompensa de la justicia, que no "
            "se adhieren al bien ni al juicio justo, que velan no para el "
            "bien, sino para el mal; lejos de los cuales están la mansedumbre "
            "y la paciencia; que aman las cosas vanas, que persiguen la "
            "retribución, que no se compadecen del pobre, que no se afanan "
            "por el oprimido, que no conocen a aquel que los hizo; matadores "
            "de niños, corruptores de la criatura de Dios, que rechazan al "
            "necesitado, que oprimen al afligido, abogados de los ricos, "
            "jueces inicuos de los pobres, pecadores en todo. ¡Seáis "
            "librados, hijos, de todas estas cosas!",

    # Capítulo 6
    (6, 1): "Mira que nadie te desvíe de este camino de la enseñanza, pues te "
            "enseña fuera de Dios.",
    (6, 2): "Porque si puedes llevar todo el yugo del Señor, serás perfecto; "
            "pero si no puedes, haz lo que puedas.",
    (6, 3): "Y en cuanto a la comida, lleva lo que puedas; pero guárdate "
            "mucho de lo sacrificado a los ídolos, porque es culto de dioses "
            "muertos.",

    # Capítulo 7
    (7, 1): "Y en cuanto al bautismo, bautizad de esta manera: habiendo dicho "
            "antes todas estas cosas, bautizad en el nombre del Padre, y del "
            "Hijo, y del Espíritu Santo, en agua viva.",
    (7, 2): "Y si no tienes agua viva, bautiza en otra agua; y si no puedes "
            "en agua fría, en caliente.",
    (7, 3): "Y si no tienes ni una ni otra, derrama agua sobre la cabeza tres "
            "veces en el nombre del Padre, y del Hijo, y del Espíritu Santo.",
    (7, 4): "Y antes del bautismo ayunen el que bautiza y el que es "
            "bautizado, y algunos otros si pueden; y al que es bautizado le "
            "mandarás ayunar uno o dos días antes.",

    # Capítulo 8
    (8, 1): "Y vuestros ayunos no sean con los hipócritas; porque ellos "
            "ayunan el segundo día de la semana y el quinto; mas vosotros "
            "ayunad el cuarto y el de la preparación.",
    (8, 2): "Ni oréis como los hipócritas, sino como mandó el Señor en su "
            "evangelio, así orad: Padre nuestro que estás en el cielo, "
            "santificado sea tu nombre. Venga tu reino. Hágase tu voluntad, "
            "como en el cielo, así también en la tierra. El pan nuestro de "
            "cada día, dánoslo hoy. Y perdónanos nuestra deuda, como también "
            "nosotros perdonamos a nuestros deudores. Y no nos metas en "
            "tentación, mas líbranos del mal; porque tuyo es el poder y la "
            "gloria por los siglos.",
    (8, 3): "Tres veces al día orad así.",

    # Capítulo 9
    (9, 1): "Y en cuanto a la eucaristía, dad gracias de esta manera:",
    (9, 2): "Primeramente, acerca del cáliz: Te damos gracias, Padre nuestro, "
            "por la santa vid de David tu siervo, la cual nos diste a conocer "
            "por medio de Jesús tu siervo. A ti sea la gloria por los siglos.",
    (9, 3): "Y acerca del pan partido: Te damos gracias, Padre nuestro, por "
            "la vida y el conocimiento que nos diste a conocer por medio de "
            "Jesús tu siervo. A ti sea la gloria por los siglos.",
    (9, 4): "Como este pan partido estaba disperso sobre los montes, y "
            "reunido se hizo uno, así sea reunida tu iglesia desde los "
            "confines de la tierra en tu reino; porque tuya es la gloria y el "
            "poder por medio de Jesucristo por los siglos.",
    (9, 5): "Y nadie coma ni beba de vuestra eucaristía, sino los bautizados "
            "en el nombre del Señor; porque también acerca de esto ha dicho "
            "el Señor: No deis lo santo a los perros.",

    # Capítulo 10
    (10, 1): "Y después de haberos saciado, dad gracias de esta manera:",
    (10, 2): "Te damos gracias, Padre santo, por tu santo nombre, que hiciste "
             "habitar en nuestros corazones, y por el conocimiento, y la fe, "
             "y la inmortalidad que nos diste a conocer por medio de Jesús tu "
             "siervo. A ti sea la gloria por los siglos.",
    (10, 3): "Tú, Soberano todopoderoso, creaste todas las cosas por causa de "
             "tu nombre, y diste a los hombres alimento y bebida para que los "
             "disfrutasen, a fin de que te diesen gracias; mas a nosotros nos "
             "hiciste la gracia de un alimento y una bebida espirituales, y "
             "de la vida eterna, por medio de tu siervo.",
    (10, 4): "Ante todo, te damos gracias porque eres poderoso. A ti sea la "
             "gloria por los siglos.",
    (10, 5): "Acuérdate, Señor, de tu iglesia, para librarla de todo mal y "
             "perfeccionarla en tu amor; y reúnela de los cuatro vientos, a "
             "ella, la santificada, en tu reino, que le preparaste; porque "
             "tuyo es el poder y la gloria por los siglos.",
    (10, 6): "Venga la gracia, y pase este mundo. Hosanna al Dios de David. "
             "Si alguno es santo, que venga; si alguno no lo es, que se "
             "arrepienta. Maranatha. Amén.",
    (10, 7): "Mas a los profetas permitidles dar gracias cuanto quieran.",

    # Capítulo 11
    (11, 1): "Así pues, a cualquiera que venga y os enseñe todas estas cosas "
             "que se han dicho antes, recibidle.",
    (11, 2): "Pero si el mismo que enseña, pervertido, enseña otra doctrina "
             "para destruir, no le escuchéis; mas si es para añadir justicia "
             "y conocimiento del Señor, recibidle como al Señor.",
    (11, 3): "Y en cuanto a los apóstoles y profetas, conforme a la ordenanza "
             "del evangelio, haced así.",
    (11, 4): "Todo apóstol que venga a vosotros sea recibido como el Señor.",
    (11, 5): "Pero no se quedará sino un día; y si hay necesidad, también el "
             "siguiente; pero si se queda tres, es un falso profeta.",
    (11, 6): "Y al partir, el apóstol no tome nada sino pan, hasta que llegue "
             "a donde pase la noche; pero si pide dinero, es un falso "
             "profeta.",
    (11, 7): "Y a todo profeta que habla en espíritu no le tentaréis ni le "
             "juzgaréis; porque todo pecado será perdonado, mas este pecado "
             "no será perdonado.",
    (11, 8): "Pero no todo el que habla en espíritu es profeta, sino si tiene "
             "la conducta del Señor. Así pues, por la conducta se conocerá al "
             "falso profeta y al profeta.",
    (11, 9): "Y todo profeta que en espíritu manda poner una mesa no comerá "
             "de ella; y si no, es un falso profeta.",
    (11, 10): "Y todo profeta que enseña la verdad, si no hace lo que enseña, "
              "es un falso profeta.",
    (11, 11): "Y todo profeta probado, verdadero, que obra en orden al "
              "misterio terreno de la iglesia, pero no enseña a hacer lo que "
              "él mismo hace, no será juzgado por vosotros; porque su juicio "
              "lo tiene con Dios; pues así hicieron también los antiguos "
              "profetas.",
    (11, 12): "Y al que diga en espíritu: Dame dinero, u otras cosas, no le "
              "escucharéis; pero si dice que se dé para otros que están "
              "necesitados, nadie le juzgue.",

    # Capítulo 12
    (12, 1): "Y todo el que venga en el nombre del Señor sea recibido; y "
             "después, probándole, le conoceréis, porque tendréis "
             "entendimiento de la derecha y de la izquierda.",
    (12, 2): "Si el que viene es un caminante de paso, ayudadle cuanto "
             "podáis; pero no se quedará con vosotros sino dos o tres días, "
             "si hay necesidad.",
    (12, 3): "Pero si quiere establecerse entre vosotros, siendo artesano, "
             "que trabaje y coma.",
    (12, 4): "Y si no tiene oficio, proveed según vuestro entendimiento, de "
             "modo que no viva ocioso entre vosotros un cristiano.",
    (12, 5): "Y si no quiere hacerlo así, es un traficante de Cristo. "
             "Guardaos de los tales.",

    # Capítulo 13
    (13, 1): "Y todo profeta verdadero que quiera establecerse entre vosotros "
             "es digno de su alimento.",
    (13, 2): "Asimismo el maestro verdadero es digno también él, como el "
             "obrero, de su alimento.",
    (13, 3): "Tomarás, pues, todas las primicias de los frutos del lagar y de "
             "la era, de los bueyes y de las ovejas, y darás las primicias a "
             "los profetas; porque ellos son vuestros sumos sacerdotes.",
    (13, 4): "Y si no tenéis profeta, dadlas a los pobres.",
    (13, 5): "Si haces pan, toma las primicias y dalas conforme al "
             "mandamiento.",
    (13, 6): "Asimismo, al abrir una vasija de vino o de aceite, toma las "
             "primicias y dalas a los profetas.",
    (13, 7): "Y del dinero, y del vestido, y de toda posesión, toma las "
             "primicias, según te parezca, y dalas conforme al mandamiento.",

    # Capítulo 14
    (14, 1): "Y en el día del Señor, el del Señor, reunidos, partid el pan y "
             "dad gracias, habiendo antes confesado vuestras transgresiones, "
             "para que vuestro sacrificio sea puro.",
    (14, 2): "Y todo el que tenga contienda con su compañero no se junte con "
             "vosotros hasta que se hayan reconciliado, para que no sea "
             "profanado vuestro sacrificio.",
    (14, 3): "Porque este es el sacrificio del que habló el Señor: En todo "
             "lugar y tiempo ofrecerme un sacrificio puro; porque soy un gran "
             "rey, dice el Señor, y mi nombre es admirable entre las gentes.",

    # Capítulo 15
    (15, 1): "Elegid, pues, para vosotros obispos y diáconos dignos del "
             "Señor, varones mansos, y no amadores del dinero, y verdaderos, "
             "y probados; porque también ellos os sirven en el ministerio de "
             "los profetas y maestros.",
    (15, 2): "No los menospreciéis, pues, porque ellos son los honrados de "
             "entre vosotros, juntamente con los profetas y maestros.",
    (15, 3): "Y corregíos los unos a los otros, no con ira, sino en paz, como "
             "lo tenéis en el evangelio; y a todo el que falte contra otro, "
             "nadie le hable, ni oiga palabra de vosotros, hasta que se "
             "arrepienta.",
    (15, 4): "Y vuestras oraciones, y las limosnas, y todas vuestras acciones "
             "hacedlas así como lo tenéis en el evangelio de nuestro Señor.",

    # Capítulo 16
    (16, 1): "Velad por vuestra vida; no se apaguen vuestras lámparas, ni se "
             "desciñan vuestros lomos, sino estad preparados; porque no "
             "sabéis la hora en que viene nuestro Señor.",
    (16, 2): "Y reuníos con frecuencia, buscando lo que conviene a vuestras "
             "almas; porque de nada os aprovechará todo el tiempo de vuestra "
             "fe, si no sois hallados perfectos en el último tiempo.",
    (16, 3): "Porque en los últimos días se multiplicarán los falsos profetas "
             "y los corruptores, y las ovejas se convertirán en lobos, y el "
             "amor se convertirá en odio.",
    (16, 4): "Porque creciendo la iniquidad, se aborrecerán unos a otros, y "
             "se perseguirán y se entregarán; y entonces aparecerá el "
             "engañador del mundo como hijo de Dios, y hará señales y "
             "prodigios, y la tierra será entregada en sus manos, y hará "
             "iniquidades que jamás se han hecho desde el principio del "
             "mundo.",
    (16, 5): "Entonces la creación de los hombres vendrá al fuego de la "
             "prueba, y muchos se escandalizarán y perecerán; pero los que "
             "perseveren en su fe serán salvos por la misma maldición.",
    (16, 6): "Y entonces aparecerán las señales de la verdad: primero, la "
             "señal de la abertura en el cielo; después, la señal del sonido "
             "de la trompeta; y la tercera, la resurrección de los muertos.",
    (16, 7): "Mas no de todos, sino como fue dicho: Vendrá el Señor, y todos "
             "los santos con él.",
    (16, 8): "Entonces verá el mundo al Señor viniendo sobre las nubes del "
             "cielo.",
}
