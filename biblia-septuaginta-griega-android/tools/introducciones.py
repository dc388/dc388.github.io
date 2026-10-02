"""Qué es cada libro, para quien llega sin saberlo.

De los 138 libros de esta biblioteca, 33 llevan la cabecera del módulo que los
tradujo. Los otros 104 no tenían nada: su página eran cuarenta palabras de
navegación —el título, cuatro datos y una rejilla de números—, que no le sirve
de nada a quien llega buscando qué es Baruc o en qué se diferencia el Génesis
griego del hebreo.

Aquí va una introducción por libro. No es un comentario devocional ni un
resumen del argumento: es lo que hace falta saber para leer ESTA edición, que
es lo que este sitio tiene y otros no. En la Septuaginta, sobre todo, eso
significa decir en qué se aparta del texto hebreo, que es justamente la razón
de tenerla al lado.

Las claves son (colección, código), las mismas que usa el índice.
"""

from __future__ import annotations

INTRODUCCIONES: dict[tuple[str, str], str] = {

    # ---- Septuaginta: el Pentateuco --------------------------------------
    ("lxx", "GEN"): (
        "El primer libro que se tradujo al griego, en Alejandría, hacia el "
        "siglo III antes de Cristo, y el que abre la Septuaginta. Su diferencia "
        "más llamativa con el hebreo está en las genealogías de los capítulos 5 "
        "y 11: las edades a las que los patriarcas engendran no coinciden, y en "
        "varios casos el griego añade cien años. Sumadas, esas diferencias "
        "hacen que el mundo de la Septuaginta sea más de mil años más viejo que "
        "el del texto masorético. No es un descuido de copista: es otro cómputo, "
        "y los Padres de la Iglesia calcularon con él durante siglos."
    ),
    ("lxx", "EXO"): (
        "El Éxodo griego sigue al hebreo de cerca hasta llegar al tabernáculo. "
        "Los capítulos 35 al 40, que cuentan cómo se construyó, van en otro "
        "orden y dicen menos: faltan pasajes enteros y otros cambian de sitio. "
        "Es uno de los casos donde está más claro que el traductor griego tenía "
        "delante un texto hebreo distinto del que llegó hasta nosotros, y no "
        "que se tomara libertades."
    ),
    ("lxx", "LEV"): (
        "De los cinco libros de la Ley, el que más se ciñe al hebreo: la "
        "traducción es tan literal que a veces fuerza el griego. Eso lo hace "
        "menos interesante para comparar textos y más útil para lo contrario, "
        "para ver cómo el vocabulario del culto —holocausto, expiación, "
        "propiciatorio— pasó al griego y de ahí al Nuevo Testamento. Cuando "
        "Hebreos habla del sacrificio, habla con las palabras de este libro."
    ),
    ("lxx", "NUM"): (
        "Traducción cercana al hebreo, con el mismo cuidado que el Levítico. "
        "Lo que aquí importa son los nombres: los censos, los campamentos y las "
        "etapas del desierto traen decenas de nombres propios que la "
        "Septuaginta fija en griego, y que son los que usarán después los "
        "autores del Nuevo Testamento y los primeros cristianos."
    ),
    ("lxx", "DEU"): (
        "Guarda una de las variantes más discutidas de toda la Biblia. En 32:8, "
        "el cántico de Moisés, el griego dice que el Altísimo repartió las "
        "naciones «según el número de los ángeles de Dios», mientras el texto "
        "masorético dice «según el número de los hijos de Israel». Durante "
        "siglos se tuvo por un retoque griego, hasta que en Qumrán apareció un "
        "manuscrito hebreo que dice lo mismo que el griego. Ahora la mayoría de "
        "los críticos piensa que el masorético es el que cambió."
    ),

    # ---- Septuaginta: los históricos -------------------------------------
    ("lxx", "JOS"): (
        "El Josué griego es más corto que el hebreo: le faltan frases y algún "
        "pasaje, y en cambio añade una nota al final sobre los cuchillos de "
        "piedra de la circuncisión. Las listas de ciudades y de fronteras "
        "difieren lo bastante como para que se discuta cuál de los dos textos "
        "está más cerca del original."
    ),
    ("lxx", "JUE"): (
        "De los Jueces circulan en griego dos formas de texto tan distintas "
        "que las ediciones críticas las imprimen en columnas paralelas: la del "
        "Códice Alejandrino y la del Vaticano. No son dos copias con erratas, "
        "son dos traducciones o una traducción revisada a fondo. Esta edición "
        "sigue una de ellas."
    ),
    ("lxx", "RUT"): (
        "Traducción muy literal y breve. Lo que cambia respecto al hebreo no es "
        "el texto sino el sitio: en la Biblia hebrea Rut está entre los "
        "Escritos, junto a Ester y Lamentaciones, y aquí va detrás de los "
        "Jueces, que es donde la puso la Septuaginta y donde sigue en las "
        "Biblias cristianas."
    ),
    ("lxx", "1RE"): (
        "Lo que la Biblia hebrea llama 1 Samuel. La Septuaginta reunió Samuel y "
        "Reyes en cuatro libros seguidos y los llamó Reinos. Y este primero "
        "trae la diferencia más famosa de toda la Septuaginta: el relato de "
        "David y Goliat es aquí mucho más corto. Faltan unos treinta y nueve "
        "versículos, entre ellos los que cuentan que Saúl no reconoce a David "
        "después de haberlo tenido tocando el arpa en su casa. Sin ellos, el "
        "relato no se contradice; con ellos, sí."
    ),
    ("lxx", "2RE"): (
        "2 Samuel. Sigue al hebreo más de cerca que el libro anterior, pero con "
        "una peculiaridad que se nota al leer: a partir de cierto punto el "
        "griego cambia de estilo y se vuelve mucho más literal. Es la huella de "
        "una revisión antigua, la llamada kaige, que retocó la Septuaginta para "
        "acercarla al hebreo y que dejó su marca en trozos de estos libros."
    ),
    ("lxx", "3RE"): (
        "1 Reyes. Aquí el orden de los capítulos no coincide con el hebreo: hay "
        "material colocado en otro sitio y dos añadidos largos sobre Jeroboam "
        "que el masorético no tiene. Es uno de los libros donde más se discute "
        "qué texto es anterior."
    ),
    ("lxx", "4RE"): (
        "2 Reyes. Cierra la serie de los cuatro Reinos. Traducción cercana al "
        "hebreo, otra vez con la marca de la revisión kaige. Termina donde "
        "termina el hebreo, con la caída de Jerusalén y el destierro."
    ),
    ("lxx", "1PA"): (
        "1 Crónicas. El nombre griego, Paralipómenos, quiere decir «las cosas "
        "que se dejaron fuera», y se lo pusieron pensando que este libro "
        "recogía lo que Samuel y Reyes se habían saltado. No es exacto —las "
        "Crónicas cuentan la misma historia con otra intención—, pero el nombre "
        "se quedó y así aparece en los códices griegos."
    ),
    ("lxx", "2PA"): (
        "2 Crónicas. Al final de este libro, la Septuaginta trae la oración de "
        "Manasés en algunos manuscritos; en esta edición va aparte, entre las "
        "Odas. Por lo demás sigue al hebreo, con las listas y genealogías que "
        "hacen de las Crónicas el libro más difícil de traducir de todo el "
        "Antiguo Testamento."
    ),
    ("lxx", "2ES"): (
        "Esdras y Nehemías en un solo libro, que es como los tenía la tradición "
        "judía y como los da el griego. Se llama 2 Esdras porque la Septuaginta "
        "trae antes otro libro distinto, 1 Esdras, que cuenta en parte lo mismo "
        "con otro orden y que en esta biblioteca está entre los apócrifos. "
        "Tener los dos al lado es lo que permite ver la diferencia."
    ),
    ("lxx", "EST"): (
        "El Ester griego es otro libro. Tiene seis pasajes largos que el hebreo "
        "no trae —el sueño de Mardoqueo, los dos edictos del rey, las oraciones "
        "de Mardoqueo y de Ester— que suman más de cien versículos. Y cambia "
        "algo de fondo: el Ester hebreo no nombra a Dios ni una sola vez, y el "
        "griego lo nombra constantemente. Jerónimo separó esos añadidos y los "
        "mandó al final; aquí van donde los pone el griego."
    ),

    # ---- Septuaginta: los poéticos ---------------------------------------
    ("lxx", "SAL"): (
        "El Salterio griego numera distinto. Desde el salmo 9 la Septuaginta "
        "une dos salmos que el hebreo separa, y a partir de ahí va un número "
        "por detrás hasta casi el final. Por eso el salmo que muchos conocen "
        "como 51 aquí es el 50, y el 23 es el 22. Los títulos de los salmos "
        "también son más largos en griego, y varios añaden el nombre de un "
        "autor o una ocasión que el hebreo no da. Es el libro del Antiguo "
        "Testamento que más cita el Nuevo, y casi siempre lo cita por aquí."
    ),
    ("lxx", "PRO"): (
        "Los Proverbios griegos traen máximas que el hebreo no tiene y colocan "
        "los capítulos finales en otro orden. El traductor trabajó con más "
        "libertad que en la Ley: a veces parafrasea, a veces explica, y en "
        "algún sitio se le cuela vocabulario de la filosofía griega. Es un "
        "buen sitio para ver cómo la sabiduría de Israel se dijo en la lengua "
        "de Atenas."
    ),
    ("lxx", "JOB"): (
        "El Job griego es una sexta parte más corto que el hebreo: faltan unos "
        "cuatrocientos versículos, sobre todo en los discursos de los amigos. "
        "Orígenes ya lo notó y rellenó los huecos con la traducción de "
        "Teodoción, marcándolos con un asterisco. No se sabe con certeza si el "
        "traductor abrevió un texto largo o si el hebreo creció después."
    ),
    ("lxx", "CNT"): (
        "Traducción extremadamente literal, hasta el punto de calcar el orden "
        "de las palabras hebreas. Por eso se cree que es tardía, de la misma "
        "escuela que revisó otros libros para pegarlos al hebreo. Lo que no "
        "cambia es la dificultad: es un poema de amor, y las imágenes que en "
        "hebreo ya cuestan, en griego cuestan igual."
    ),

    # ---- Septuaginta: los profetas ---------------------------------------
    ("lxx", "ISA"): (
        "El traductor de Isaías es el más libre de toda la Septuaginta: "
        "interpreta, actualiza y a veces mete en el texto la situación de su "
        "propia época, el Egipto de los Ptolomeos. Eso lo hace menos fiable "
        "para reconstruir el hebreo y más valioso para otra cosa: es el Isaías "
        "que leyeron los apóstoles. Cuando Mateo cita «la virgen concebirá», "
        "cita esta palabra, παρθένος, que es la que puso este traductor donde "
        "el hebreo dice «la joven»."
    ),
    ("lxx", "JER"): (
        "El Jeremías griego es una octava parte más corto que el hebreo —unas "
        "2700 palabras menos— y además está ordenado de otra manera: los "
        "oráculos contra las naciones, que en el hebreo van al final, aquí "
        "están en medio del libro. Los manuscritos de Qumrán trajeron trozos de "
        "un Jeremías hebreo corto, parecido a éste. Hoy se piensa que hubo dos "
        "ediciones antiguas del libro y que el griego conserva la más breve."
    ),
    ("lxx", "LAM"): (
        "Traducción literal de los cinco poemas. En el hebreo, los cuatro "
        "primeros son acrósticos: cada estrofa empieza por una letra del "
        "alfabeto en orden. Eso en griego no se puede reproducir, y varios "
        "manuscritos lo resuelven poniendo delante de cada estrofa el nombre de "
        "la letra hebrea —alef, bet, guímel—, que es lo que se ve en esta "
        "edición."
    ),
    ("lxx", "EZE"): (
        "Algo más corto que el hebreo, con bastantes frases de menos. La "
        "traducción es cuidadosa y el vocabulario de la visión del carro y del "
        "templo nuevo es el que después usará el Apocalipsis. El papiro 967, "
        "uno de los testigos más antiguos, trae los capítulos en otro orden, lo "
        "que ha reabierto la discusión sobre cómo se formó el libro."
    ),
    ("lxx", "DAN"): (
        "El Daniel griego antiguo, el de los Setenta. Se apartaba tanto del "
        "hebreo y el arameo que la Iglesia acabó dejándolo de lado y poniendo "
        "en su sitio la versión de Teodoción, que es la que está en casi todos "
        "los manuscritos. El texto antiguo sobrevivió en dos códices y poco "
        "más. Tenerlo aquí, junto a la versión de Teodoción, permite ver lo "
        "raro que es el caso: un libro bíblico con dos traducciones griegas "
        "antiguas y muy distintas."
    ),
    ("lxx", "DAT"): (
        "El Daniel de Teodoción, que desplazó al de los Setenta y es el que "
        "leyó la Iglesia durante siglos. La revisión se atribuye a un Teodoción "
        "del siglo II después de Cristo, pero hay citas de este texto en "
        "autores anteriores, lo que ha hecho pensar en una revisión más "
        "antigua. Es el texto en el que Susana, y Bel y el Dragón, se leen "
        "como capítulos 13 y 14 del libro."
    ),

    # ---- Septuaginta: los doce, en el orden griego -----------------------
    ("lxx", "OSE"): (
        "Los doce profetas menores van en la Septuaginta en otro orden que en "
        "el hebreo: Oseas, Amós, Miqueas, Joel, Abdías, Jonás… El hebreo pone "
        "Joel en segundo lugar y el griego lo baja al cuarto. Se cree que el "
        "griego agrupó primero los tres más largos. Oseas abre la serie en las "
        "dos tradiciones, y su griego es difícil: el hebreo de Oseas está mal "
        "conservado y el traductor se las vio negras."
    ),
    ("lxx", "AMO"): (
        "Segundo de los doce en el orden griego. Trae en 9:12 una variante que "
        "pesó mucho: donde el hebreo dice que Israel poseerá «el resto de "
        "Edom», el griego dice que «el resto de los hombres» buscará al Señor. "
        "Es la forma que cita Santiago en Hechos 15 para defender la entrada de "
        "los gentiles en la Iglesia, y la que usan los apóstoles para zanjar la "
        "primera gran discusión del cristianismo."
    ),
    ("lxx", "MIQ"): (
        "Tercero en el orden griego, quinto en el hebreo. Traducción fiel, con "
        "el pasaje de Belén que cita Mateo 2. El griego llama a la aldea «Belén, "
        "casa de Efrata», resolviendo a su manera una expresión hebrea que "
        "admite varias lecturas."
    ),
    ("lxx", "JOE"): (
        "En el hebreo va el segundo de los doce; aquí, el cuarto. Es el profeta "
        "de la langosta y del derramamiento del Espíritu, y el griego de 2:28-32 "
        "es el que Pedro predica en Pentecostés, palabra por palabra."
    ),
    ("lxx", "ABD"): (
        "El libro más corto del Antiguo Testamento: un solo capítulo contra "
        "Edom. En griego, veintiún versículos."
    ),
    ("lxx", "JON"): (
        "Traducción clara y sin sobresaltos. La única diferencia que se nota es "
        "de tiempo: donde el hebreo da cuarenta días para que Nínive sea "
        "destruida, el griego da tres. No se sabe si el traductor leyó otro "
        "número o si lo cambió a propósito."
    ),
    ("lxx", "NAH"): (
        "Contra Nínive, la ciudad que en Jonás se había arrepentido. El hebreo "
        "es de los más duros de traducir de los doce, y el griego tiene pasajes "
        "en los que se ve al traductor adivinando."
    ),
    ("lxx", "HAB"): (
        "Trae en 2:4 la frase que Pablo pone en el centro de Romanos y de "
        "Gálatas: «el justo vivirá por la fe». El griego añade un posesivo que "
        "el hebreo no tiene, y esa pequeña diferencia ha dado siglos de "
        "discusión sobre de quién es la fe. El capítulo 3 es un salmo con "
        "indicaciones musicales, y en los manuscritos griegos va también entre "
        "las Odas."
    ),
    ("lxx", "SOF"): (
        "Traducción cercana al hebreo. El «día del Señor» de este libro es el "
        "que está detrás del Dies irae medieval, que lo cita por la Vulgata, y "
        "la Vulgata lo toma de aquí."
    ),
    ("lxx", "AGE"): (
        "Dos capítulos sobre la reconstrucción del templo después del "
        "destierro. El griego es fiel y sin complicaciones; el interés del "
        "libro está en la fecha, que es de las más precisas de toda la Biblia: "
        "el segundo año de Darío."
    ),
    ("lxx", "ZAC"): (
        "Las visiones de Zacarías son de lo más oscuro del Antiguo Testamento, "
        "y el griego no lo aclara: en varios sitios se ve que el traductor no "
        "entendía su original. Aun así, este texto es el que citan los "
        "evangelios en la entrada en Jerusalén y en el precio de treinta "
        "monedas de plata."
    ),
    ("lxx", "MAL"): (
        "El último de los doce y el último profeta del Antiguo Testamento. Con "
        "él se cierra el canon hebreo y empieza el silencio que sólo rompen los "
        "Macabeos, que en esta biblioteca se pueden leer en español por primera "
        "vez. Su anuncio del mensajero que prepara el camino es el que los "
        "cuatro evangelios aplican a Juan el Bautista."
    ),

    # ---- Nuevo Testamento griego -----------------------------------------
    # La edición es el Texto Mayoritario de Robinson y Pierpont, que sigue la
    # lectura de la mayoría de los manuscritos bizantinos y no la de los pocos
    # códices antiguos en que se basan las ediciones críticas. Donde eso cambia
    # algo visible, se dice.
    ("nt", "MAT"): (
        "El evangelio que más cita el Antiguo Testamento, y casi siempre por la "
        "Septuaginta: cuando escribe «la virgen concebirá» está citando el "
        "Isaías griego que está en esta misma biblioteca, no el hebreo. Su "
        "griego es el más semítico de los cuatro, con giros que suenan a "
        "traducción del arameo. Y su capítulo 24 repite, palabra por palabra, "
        "la «abominación de la desolación» que aparece en 1 Macabeos 1:54, un "
        "libro que ninguna Biblia española gratuita trae y que aquí se puede "
        "leer al lado."
    ),
    ("nt", "MAR"): (
        "El más corto y el más rápido: todo pasa «en seguida», que es la "
        "palabra que más repite. Se tiene por el primero que se escribió. Su "
        "griego es tosco a propósito o por falta de escuela, con presentes "
        "históricos y frases pegadas con «y». El final es el problema textual "
        "más conocido del Nuevo Testamento: los versículos 16:9-20 faltan en "
        "los dos códices más antiguos. El Texto Mayoritario, que es el de esta "
        "edición, los trae."
    ),
    ("nt", "LUC"): (
        "El griego más culto de los evangelios, y el único que empieza con un "
        "prólogo a la manera de los historiadores griegos, dedicado a Teófilo. "
        "Su autor investigó, dice, «desde el principio». Los dos primeros "
        "capítulos cambian de registro y suenan a Septuaginta: los cánticos de "
        "María, de Zacarías y de Simeón están escritos con el vocabulario de "
        "los Salmos griegos, y los tres van también entre las Odas de esta "
        "biblioteca."
    ),
    ("nt", "JUA"): (
        "El vocabulario más sencillo del Nuevo Testamento y las ideas más "
        "difíciles. Se lee con doscientas palabras y se discute desde hace "
        "dieciocho siglos. Su primer versículo —«en el principio era el Verbo»— "
        "empieza con las mismas palabras con que empieza el Génesis griego, y "
        "quien lea las dos páginas de esta biblioteca lo verá: Ἐν ἀρχῇ. En "
        "1:14, «habitó entre nosotros» traduce un verbo que significa plantar "
        "la tienda, el mismo que usa el Eclesiástico cuando la Sabiduría planta "
        "su tienda en Jacob."
    ),
    ("nt", "HEC"): (
        "La segunda parte de Lucas, del mismo autor y para el mismo Teófilo. "
        "Cuenta treinta años y recorre medio imperio. En 15:17 los apóstoles "
        "zanjan la entrada de los gentiles citando a Amós, y lo citan por la "
        "Septuaginta: el hebreo de ese versículo dice otra cosa y no serviría "
        "para el argumento. Es uno de los sitios donde mejor se ve para qué "
        "sirve tener las dos columnas."
    ),
    ("nt", "ROM"): (
        "La carta más larga y más trabajada de Pablo, y la única escrita a una "
        "iglesia que no había fundado. Todo el argumento cuelga de una frase de "
        "Habacuc citada en 1:17, «el justo vivirá por la fe», que Pablo toma de "
        "la Septuaginta. El griego de los capítulos 9 al 11 está entre lo más "
        "denso del Nuevo Testamento."
    ),
    ("nt", "1CO"): (
        "Respuestas a los problemas concretos de una iglesia difícil: "
        "divisiones, pleitos, comida de los ídolos, desorden en las reuniones. "
        "En medio de todo eso está el capítulo 13, sobre el amor, que Pablo "
        "escribe sin previo aviso y con un griego distinto del que trae "
        "alrededor. Y el 15, la exposición más larga que hay sobre la "
        "resurrección."
    ),
    ("nt", "2CO"): (
        "La más personal y la más dolida. Pablo se defiende de quienes le "
        "disputan la autoridad, y al hacerlo cuenta de sí mismo lo que no "
        "cuenta en ninguna otra parte: los naufragios, los azotes, el aguijón "
        "en la carne. El griego es irregular, con frases que empieza y no "
        "termina, lo que muchos leen como señal de que dictó con emoción."
    ),
    ("nt", "GAL"): (
        "La carta más airada del Nuevo Testamento: es la única que no empieza "
        "dando gracias. Pablo se salta la cortesía y entra directo en la "
        "reprensión. Trata lo mismo que Romanos —la ley y la fe— pero en "
        "caliente y en cuatro capítulos. Al final escribe unas líneas de su "
        "puño y letra y hace notar el tamaño de sus letras."
    ),
    ("nt", "EFE"): (
        "Frases largas: el griego del primer capítulo es una sola oración de "
        "más de doscientas palabras, que ninguna traducción conserva entera "
        "porque en castellano sería ilegible. Varios manuscritos antiguos no "
        "traen «en Éfeso» en el primer versículo, lo que ha hecho pensar que "
        "era una carta circular."
    ),
    ("nt", "FIL"): (
        "Escrita desde la cárcel y, aun así, la más alegre: la palabra gozo y "
        "sus derivados salen dieciséis veces en cuatro capítulos. En 2:6-11 "
        "Pablo cita lo que casi todos consideran un himno anterior a él, con un "
        "ritmo y un vocabulario que no son los suyos."
    ),
    ("nt", "COL"): (
        "Contra una enseñanza que mezclaba ángeles, calendarios y reglas sobre "
        "la comida. El himno de 1:15-20, sobre Cristo como imagen del Dios "
        "invisible y primogénito de toda la creación, usa el mismo vocabulario "
        "que Sabiduría 7:26 —«resplandor de la luz eterna, espejo sin mancha»—, "
        "un libro que en esta biblioteca está traducido del griego."
    ),
    ("nt", "1TE"): (
        "Probablemente el escrito más antiguo del Nuevo Testamento, anterior a "
        "los evangelios. Se nota en lo que no tiene: ninguna de las discusiones "
        "que llenarán las cartas posteriores. Lo que preocupa aquí es qué pasa "
        "con los que ya murieron antes de que el Señor vuelva."
    ),
    ("nt", "2TE"): (
        "Escrita poco después y para corregir un malentendido: algunos habían "
        "dejado de trabajar creyendo que el día del Señor ya había llegado. El "
        "capítulo 2, con el hombre de pecado y lo que lo detiene, es de los "
        "pasajes más discutidos del Nuevo Testamento."
    ),
    ("nt", "1TI"): (
        "Instrucciones a un colaborador joven sobre cómo organizar una iglesia: "
        "qué se pide de un anciano, de un diácono, de las viudas. El "
        "vocabulario se aparta bastante del de las cartas mayores, y por eso "
        "hay quien discute la autoría. El Texto Mayoritario trae en 3:16 «Dios "
        "fue manifestado en carne», donde las ediciones críticas leen «el que "
        "fue manifestado»: una letra griega de diferencia."
    ),
    ("nt", "2TI"): (
        "La última carta, escrita esperando la ejecución: «el tiempo de mi "
        "partida está cercano». Pide que le lleven el capote que dejó en Troas "
        "y los libros, «mayormente los pergaminos». En 3:16, la frase sobre la "
        "Escritura inspirada usa una palabra, θεόπνευστος, que no aparece en "
        "ningún otro sitio de la Biblia."
    ),
    ("nt", "TIT"): (
        "Tres capítulos a otro colaborador, esta vez en Creta. Contiene la cita "
        "de un poeta cretense —«los cretenses, siempre mentirosos»— que Pablo "
        "aprueba, uno de los pocos sitios donde el Nuevo Testamento cita "
        "literatura griega pagana."
    ),
    ("nt", "FLM"): (
        "La más corta de Pablo: veinticinco versículos sobre un esclavo fugado "
        "llamado Onésimo. No condena la esclavitud ni la defiende; pide que "
        "reciban al fugado «no ya como esclavo, sino como hermano amado». "
        "Cabía en una sola hoja de papiro."
    ),
    ("nt", "HEB"): (
        "Nadie sabe quién la escribió, y ya Orígenes decía que sólo Dios lo "
        "sabe. Es el griego más elegante del Nuevo Testamento. Está construida "
        "entera sobre la Septuaginta: cita el Antiguo Testamento más de treinta "
        "veces y siempre por el griego, incluso cuando el hebreo dice otra "
        "cosa. Y en 11:35, cuando habla de los que «fueron atormentados, no "
        "aceptando el rescate, a fin de obtener mejor resurrección», está "
        "señalando a 2 Macabeos 7, que en esta biblioteca se puede leer en "
        "español: no hay otro pasaje al que pueda referirse."
    ),
    ("nt", "SAN"): (
        "Más cerca de la literatura sapiencial que de una carta: dichos "
        "encadenados, sin argumento seguido. Y llena de ecos del Eclesiástico, "
        "que está traducido en esta biblioteca: el «pronto para oír, tardo para "
        "hablar» de 1:19 ya está en Eclesiástico 5:11, y la prueba que produce "
        "paciencia de 1:2-4 está en 2:1-5. Era el vocabulario moral en que se "
        "educó su generación."
    ),
    ("nt", "1PE"): (
        "A cristianos dispersos por el norte de Asia Menor que están sufriendo "
        "por serlo. El griego es bueno, y el propio texto dice al final que la "
        "escribió «por medio de Silvano», lo que puede explicar la diferencia "
        "de estilo con la segunda."
    ),
    ("nt", "2PE"): (
        "El griego más rebuscado del Nuevo Testamento, con palabras que no "
        "salen en ningún otro sitio. Su capítulo 2 coincide casi frase por "
        "frase con la carta de Judas, y se discute cuál copió a cuál. En 3:16 "
        "llama «Escrituras» a las cartas de Pablo, que es la primera vez que un "
        "escrito cristiano las pone a ese nivel."
    ),
    ("nt", "1JN"): (
        "El mismo vocabulario cortísimo del cuarto evangelio: luz y tinieblas, "
        "verdad y mentira, amor y odio, sin términos medios. El pasaje de "
        "5:7-8 sobre los tres que dan testimonio en el cielo —la coma "
        "joanina— es la interpolación más famosa de la Biblia: no está en "
        "ningún manuscrito griego anterior al siglo XIV. El Texto Mayoritario "
        "de esta edición tampoco la trae."
    ),
    ("nt", "2JN"): (
        "Trece versículos a «la señora elegida y sus hijos», que casi con "
        "seguridad es una iglesia. Advierte contra los que niegan que Cristo "
        "vino en carne y manda no recibirlos en casa."
    ),
    ("nt", "3JN"): (
        "Catorce versículos, la carta más corta del Nuevo Testamento. Trata un "
        "problema muy concreto: un tal Diótrefes, «al cual le gusta tener el "
        "primer lugar», no recibe a los enviados y echa de la iglesia a los que "
        "sí los reciben."
    ),
    ("nt", "JUD"): (
        "Veinticinco versículos, y dentro dos citas de libros que no están en "
        "el canon: la disputa por el cuerpo de Moisés, que viene de la Asunción "
        "de Moisés, y la profecía de «Enoc, séptimo desde Adán», que es 1 Enoc "
        "1:9. Ese libro está traducido en esta biblioteca, y se puede ir a leer "
        "la frase que Judas cita."
    ),
    ("nt", "APO"): (
        "El griego más incorrecto del Nuevo Testamento, con faltas de "
        "concordancia que a veces parecen deliberadas. Está tejido de Antiguo "
        "Testamento —Daniel, Ezequiel, Zacarías, Isaías— pero no cita "
        "literalmente ni una vez: alude. Es también el libro con más variantes "
        "textuales, porque se copió menos y peor que los demás."
    ),

    # ---- Antiguo Testamento hebreo ---------------------------------------
    # La edición es el Códice de Leningrado, el manuscrito completo más antiguo
    # de la Biblia hebrea (año 1008), con sus vocales y sus acentos. Lo que se
    # dice aquí mira al hebreo; la diferencia con el griego se cuenta en la
    # página del mismo libro en la Septuaginta.
    ("at", "GEN"): (
        "Bereshit, «en el principio», que es como lo nombra la tradición judía: "
        "por su primera palabra. El hebreo de los once primeros capítulos es "
        "distinto del resto, más arcaico y más poético, y ahí están las "
        "genealogías cuyas cifras no coinciden con las del Génesis griego que "
        "está en esta misma biblioteca. Merece abrir los dos a la vez."
    ),
    ("at", "EXO"): (
        "Shemot, «nombres». El texto hebreo más citado del judaísmo: de aquí "
        "salen el Decálogo, la Pascua y el Shemá que lo precede en "
        "Deuteronomio. El nombre divino de 3:14 —«Yo soy el que soy»— está "
        "escrito con un juego de palabras sobre el verbo ser que ninguna "
        "traducción conserva entero."
    ),
    ("at", "LEV"): (
        "Vayikrá, «y llamó». El libro con el vocabulario técnico más cerrado de "
        "toda la Biblia hebrea: decenas de términos de sacrificio, de pureza y "
        "de enfermedad de la piel cuyo significado exacto se sigue discutiendo. "
        "Es donde más sirve el análisis palabra por palabra."
    ),
    ("at", "NUM"): (
        "Bamidbar, «en el desierto». Mezcla censos y listas con relatos —el "
        "agua de la roca, Balaam y su asna, las serpientes— y contiene en 6:24-26 "
        "la bendición sacerdotal, que es el texto bíblico más antiguo que se ha "
        "encontrado escrito: apareció en unos amuletos de plata de Jerusalén "
        "del siglo VII antes de Cristo."
    ),
    ("at", "DEU"): (
        "Devarim, «palabras». Escrito casi entero como discurso de Moisés antes "
        "de morir. Contiene el Shemá, la confesión de fe de Israel, y en 32:8 "
        "una variante que separa a este texto del griego y que en esta "
        "biblioteca se puede cotejar en un minuto."
    ),
    ("at", "JOS"): ("Abre los Profetas Anteriores, que en la Biblia hebrea no "
        "son historia sino profecía. Cuenta la entrada en la tierra, el reparto "
        "entre las tribus y las listas de fronteras, que son de los pasajes más "
        "difíciles de traducir porque están llenos de topónimos."),
    ("at", "JUE"): ("Doce ciclos de liberadores locales, no de jueces en el "
        "sentido de magistrados. El cántico de Débora, en el capítulo 5, está "
        "en un hebreo tan arcaico que se tiene por uno de los textos más "
        "antiguos de la Biblia, y por eso mismo es de los peor entendidos."),
    ("at", "1SA"): ("El paso de los jueces a la monarquía: Samuel, Saúl y el "
        "ascenso de David. El hebreo de este libro está peor conservado que el "
        "de casi ningún otro, con pasajes evidentemente corrompidos. Por eso la "
        "versión griega, que aquí es 1 Reinos, importa tanto: en el relato de "
        "David y Goliat es mucho más corta."),
    ("at", "2SA"): ("El reinado de David, contado sin adornarlo: el adulterio, "
        "el asesinato encargado, la rebelión del hijo. El relato de la sucesión "
        "al trono, capítulos 9 al 20, se considera una de las primeras piezas "
        "de prosa histórica de la literatura universal."),
    ("at", "1RY"): ("De la muerte de David al cisma y los primeros reyes de "
        "los dos reinos, con Elías al final. En griego este libro es 3 Reinos, "
        "y allí el orden de los capítulos no coincide con éste."),
    ("at", "2RY"): ("De Eliseo a la caída de Jerusalén. Termina con el rey "
        "Joaquín sacado de la cárcel en Babilonia, que es donde el canon hebreo "
        "deja la historia: sin final. Los Macabeos, que la continúan en "
        "griego, están en esta biblioteca traducidos al español."),
    ("at", "ISA"): ("Sesenta y seis capítulos que desde hace dos siglos casi "
        "todos leen como obra de más de una mano: el hebreo del capítulo 40 en "
        "adelante cambia de vocabulario y de situación. El rollo de Isaías de "
        "Qumrán, mil años anterior al Códice de Leningrado, confirmó que el "
        "texto se había transmitido con notable fidelidad."),
    ("at", "JER"): ("El profeta que más habla de sí mismo, con las llamadas "
        "confesiones, donde se queja a Dios de haber sido enviado. Su libro "
        "existe en dos ediciones antiguas: ésta, la larga, y la del griego, que "
        "es una octava parte más corta y trae los capítulos en otro orden. En "
        "Qumrán aparecieron las dos en hebreo."),
    ("at", "EZE"): ("Empieza con la visión del carro, que la tradición judía "
        "rodeó de tanta cautela que llegó a prohibirse explicarla en público. "
        "Termina con nueve capítulos de medidas de un templo que nunca se "
        "construyó. El hebreo es tardío y tiene aramaísmos."),
    ("at", "OSE"): ("El matrimonio del profeta con una mujer infiel como "
        "imagen de la alianza rota. Su hebreo es el peor conservado de los doce "
        "profetas menores, con versículos que nadie ha conseguido explicar del "
        "todo."),
    ("at", "JOE"): ("La plaga de langostas y el día del Señor. El pasaje del "
        "derramamiento del Espíritu, que en las Biblias cristianas es 2:28-32, "
        "en el hebreo es el capítulo 3 entero: la numeración no coincide."),
    ("at", "AMO"): ("El más antiguo de los profetas con libro propio, y el más "
        "duro con la injusticia social. Se presenta como pastor y cultivador de "
        "higos, no como profesional de la profecía. Su hebreo es limpio y "
        "directo."),
    ("at", "ABD"): ("Veintiún versículos contra Edom: el libro más corto de la "
        "Biblia hebrea. Buena parte coincide casi palabra por palabra con "
        "Jeremías 49."),
    ("at", "JON"): ("El único de los doce que es un relato sobre el profeta y "
        "no una colección de oráculos, y el único donde la ciudad pagana se "
        "arrepiente y el profeta se enfada por ello. Termina con una pregunta "
        "sin respuesta."),
    ("at", "MIQ"): ("Contemporáneo de Isaías y con algunos pasajes casi "
        "idénticos. De aquí sale Belén, y también la frase que resume toda la "
        "ética profética: «hacer justicia, amar misericordia y humillarte ante "
        "tu Dios»."),
    ("at", "NAH"): ("Contra Nínive, un siglo y medio después de que Jonás la "
        "viera arrepentirse. Su hebreo es de los más vigorosos de la Biblia: el "
        "capítulo 2, con los carros y los látigos, imita con el sonido lo que "
        "describe."),
    ("at", "HAB"): ("Empieza discutiendo con Dios en vez de hablar de su "
        "parte, que es raro en un profeta. De su 2:4 sale «el justo vivirá por "
        "su fe». El capítulo 3 es un salmo con indicaciones musicales, señal de "
        "que se cantaba."),
    ("at", "SOF"): ("El «día de ira» que la Edad Media convirtió en el Dies "
        "irae. Su genealogía lo remonta a Ezequías, lo que lo haría de sangre "
        "real."),
    ("at", "AGE"): ("Dos capítulos con fechas exactas, para que los que "
        "volvieron del destierro terminen el templo. Junto con Zacarías, es el "
        "testimonio más directo de aquel momento."),
    ("at", "ZAC"): ("Ocho visiones nocturnas en la primera mitad y, en la "
        "segunda, unos capítulos de estilo tan distinto que se discute si son "
        "del mismo autor. De aquí salen el rey que entra montado en un asno y "
        "las treinta piezas de plata."),
    ("at", "MAL"): ("«Mi mensajero», que es lo que significa el nombre y "
        "quizá no sea un nombre. Escrito en forma de disputa: Dios afirma, el "
        "pueblo replica, Dios responde. Cierra el canon hebreo de los profetas."),
    ("at", "SAL"): ("Ciento cincuenta poemas de muchas épocas, repartidos en "
        "cinco libros. Atención a la numeración: desde el salmo 9 la "
        "Septuaginta que está en esta biblioteca va un número por detrás, "
        "porque une dos salmos que aquí van separados. Por eso el salmo 51 "
        "hebreo es el 50 griego."),
    ("at", "PRO"): ("Sabiduría práctica, en su mayor parte en dísticos de dos "
        "versos que se responden. Los capítulos 1 al 9 son distintos del resto: "
        "ahí la Sabiduría habla en primera persona, y ese personaje es el que "
        "recogerán después el libro de la Sabiduría y el Eclesiástico, los dos "
        "traducidos en esta biblioteca."),
    ("at", "JOB"): ("El hebreo más difícil de toda la Biblia, con un "
        "vocabulario que no aparece en ningún otro sitio y pasajes que siguen "
        "sin entenderse. El libro griego es una sexta parte más corto, y "
        "comparar los dos es una de las cosas más instructivas que se pueden "
        "hacer aquí."),
    ("at", "CNT"): ("Un poema de amor sin una sola mención de Dios. Rabí Akiba "
        "lo llamó el santo de los santos de las Escrituras. Su hebreo tiene "
        "palabras de origen persa y griego, señal de que es tardío."),
    ("at", "RUT"): ("Cuatro capítulos sobre una moabita que acaba siendo "
        "bisabuela de David. En la Biblia hebrea está entre los Escritos y se "
        "lee en la fiesta de Pentecostés; las Biblias cristianas lo pusieron "
        "detrás de los Jueces siguiendo a la Septuaginta."),
    ("at", "LAM"): ("Cinco poemas por la destrucción de Jerusalén. Los cuatro "
        "primeros son acrósticos: cada estrofa empieza por una letra del "
        "alfabeto en orden. Eso se ve en el hebreo y se pierde en cualquier "
        "traducción; en el griego de esta biblioteca, los manuscritos lo "
        "marcan poniendo delante el nombre de la letra."),
    ("at", "ECL"): ("Kohélet, «el que reúne a la asamblea». El libro más "
        "escéptico de la Biblia: «vanidad de vanidades» traduce hével, que "
        "literalmente es vaho, aliento, lo que se disipa. Su hebreo es tardío y "
        "tiene aramaísmos."),
    ("at", "EST"): ("El único libro de la Biblia hebrea que no nombra a Dios "
        "ni una sola vez. El Ester griego que está en esta biblioteca sí lo "
        "nombra, y trae además seis pasajes largos que el hebreo no tiene: "
        "ponerlos al lado es la manera más clara de ver qué hizo la "
        "Septuaginta."),
    ("at", "DAN"): ("Bilingüe: empieza en hebreo, cambia a arameo en 2:4 y "
        "vuelve al hebreo en el capítulo 8. En la Biblia hebrea no está entre "
        "los profetas sino entre los Escritos. Las adiciones griegas —Susana, "
        "Bel y el Dragón, el cántico de los tres jóvenes— no están aquí; "
        "están traducidas en la sección de apócrifos."),
    ("at", "ESD"): ("La vuelta del destierro y la reconstrucción del templo. "
        "Tiene pasajes en arameo, que eran documentos oficiales del imperio "
        "persa. En la Septuaginta va unido a Nehemías como un solo libro, y "
        "además existe otro Esdras griego distinto que aquí está entre los "
        "apócrifos."),
    ("at", "NEH"): ("Las memorias de Nehemías, escritas en primera persona, "
        "sobre la reconstrucción de la muralla. El capítulo 8, con la lectura "
        "pública de la Ley, es el acta de nacimiento del judaísmo tal como "
        "llegó después."),
    ("at", "1CR"): ("Empieza con nueve capítulos de genealogías, de Adán en "
        "adelante. No es historia repetida: las Crónicas cuentan lo mismo que "
        "Samuel y Reyes con otra intención, y callan lo que no les sirve."),
    ("at", "2CR"): ("De Salomón a la vuelta del destierro. Cierra la Biblia "
        "hebrea, que no termina con los profetas sino aquí, con el permiso de "
        "Ciro para volver a Jerusalén: el último libro del canon judío acaba "
        "con una invitación a subir."),

    # ---- Los que se quedaron cortos en la primera pasada ------------------
    ("lxx", "ECL"): (
        "El Eclesiastés griego es la traducción más literal de toda la "
        "Septuaginta: calca el hebreo palabra por palabra, incluso cuando el "
        "resultado no es griego correcto. Llega a traducir la partícula hebrea "
        "que marca el complemento directo, que en griego no significa nada, "
        "con la preposición σύν. Por eso se atribuye a la escuela de Áquila, "
        "del siglo II después de Cristo, y no a los traductores alejandrinos. "
        "Es un caso extremo de un criterio que hoy nadie seguiría y que "
        "entonces se tenía por el más reverente: no poner ni quitar nada, "
        "aunque se pierda el sentido."
    ),
    ("lxx", "ABD"): (
        "El libro más corto del Antiguo Testamento: un solo capítulo contra "
        "Edom, el pueblo descendiente de Esaú, por haberse alegrado de la caída "
        "de Jerusalén. Veintiún versículos en griego. Buena parte del texto "
        "coincide casi palabra por palabra con Jeremías 49, y se discute cuál "
        "de los dos tomó del otro. En el orden griego de los doce profetas va "
        "el quinto; en el hebreo, el cuarto."
    ),
    ("lxx", "NAH"): (
        "Contra Nínive, la capital de Asiria, un siglo y medio después de que "
        "Jonás la viera arrepentirse. El hebreo de este libro es de los más "
        "vigorosos de la Biblia —el capítulo 2 imita con el sonido el ruido de "
        "los carros y los látigos— y es también de los peor conservados. El "
        "traductor griego se encontró con pasajes que no se entendían y hay "
        "sitios donde se le ve adivinando. Comparar las dos columnas en esos "
        "versículos enseña más sobre cómo se hizo la Septuaginta que cualquier "
        "explicación."
    ),
    ("lxx", "SOF"): (
        "Tres capítulos sobre el día del Señor, escritos poco antes de la "
        "reforma de Josías. De aquí, a través de la Vulgata, sale el Dies irae "
        "de la liturgia latina: «día de ira aquel día», que en griego es ἡμέρα "
        "ὀργῆς. La traducción es cercana al hebreo. En el orden griego de los "
        "doce va el noveno."
    ),
    ("lxx", "JOE"): (
        "La plaga de langostas como anuncio del día del Señor. En el orden "
        "griego de los doce va el cuarto; en el hebreo, el segundo. Su pasaje "
        "más conocido es el del derramamiento del Espíritu sobre toda carne, y "
        "conviene saber que la numeración no coincide: lo que las Biblias "
        "cristianas llaman 2:28-32 en el hebreo es el capítulo 3 entero. Es el "
        "texto que Pedro predica en Pentecostés, y lo predica en esta forma "
        "griega."
    ),
    ("lxx", "1PA"): (
        "1 Crónicas. Paralipómenos quiere decir «las cosas que se dejaron "
        "fuera», nombre que les pusieron los griegos creyendo que este libro "
        "recogía lo que Samuel y Reyes se habían saltado. No es exacto: las "
        "Crónicas cuentan la misma historia desde el templo y el culto, y "
        "callan lo que no les sirve —el adulterio de David no está aquí—. "
        "Empieza con nueve capítulos de genealogías desde Adán, que son de lo "
        "más difícil de traducir del Antiguo Testamento porque son cientos de "
        "nombres propios sin contexto."
    ),
    ("at", "1CR"): (
        "Empieza con nueve capítulos de genealogías, de Adán en adelante: "
        "cientos de nombres sin más contexto que su posición en una lista, lo "
        "que los convierte en el pasaje más difícil de traducir y de copiar de "
        "toda la Biblia hebrea. No es historia repetida. Las Crónicas cuentan "
        "lo mismo que Samuel y Reyes desde el templo y el culto, y callan lo "
        "que no les sirve: aquí no está el adulterio de David ni la rebelión de "
        "Absalón. En griego este libro es 1 Paralipómenos, «las cosas dejadas "
        "fuera»."
    ),
    ("at", "ECL"): (
        "Kohélet, «el que reúne a la asamblea», de donde sale el nombre griego "
        "Ἐκκλησιαστής. El libro más escéptico de la Biblia: «vanidad de "
        "vanidades» traduce hével, que literalmente es vaho, aliento, lo que se "
        "disipa en cuanto se nombra. Su hebreo es tardío, con aramaísmos y con "
        "palabras de origen persa, y eso lo sitúa después del destierro pese a "
        "atribuirse a Salomón. El griego que está al lado en esta biblioteca es "
        "un caso extremo de literalidad, de la escuela de Áquila."
    ),
}
