"""Eclesiástico (Sirácida, Ben Sirá) en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Pero pocos
libros de fuera del canon se han leído tanto: el nombre latino, Ecclesiasticus,
quiere decir «el libro de la iglesia», porque durante siglos fue el manual con
el que se enseñaba a vivir a los recién bautizados.

Lo escribió en hebreo, en Jerusalén, hacia el año 180 antes de Cristo, un
escriba llamado Jesús hijo de Sirá. Su nieto lo tradujo al griego en Egipto, y
el prólogo que abre el libro es suyo: es el nieto quien habla, quien dice que
llegó a Egipto en el año treinta y ocho del rey Evérgetes, y quien pide perdón
por lo que se pierde al traducir —«porque no tienen la misma fuerza las cosas
dichas en hebreo que cuando se pasan a otra lengua»—. Es la queja más antigua
que se conserva de un traductor, y quien esto traduce la suscribe entera.

Ese prólogo tiene además un valor que no depende de la fe: es el testimonio más
antiguo de que la Biblia hebrea estaba ya dividida en tres partes, «la ley y los
profetas y los otros libros». Está ahí, dicho tres veces, hacia el 130 antes de
Cristo.

Por qué importa para leer el Nuevo Testamento: éste es el vocabulario moral en
el que se educó la generación de Jesús. Santiago está lleno de ecos suyos —el
«pronto para oír, tardo para hablar» de Santiago 1:19 está en 5:11; la prueba
que produce paciencia de Santiago 1:2-4 está en 2:1-5—; el perdonar al prójimo
para ser perdonado de Mateo 6:14 está en 28:2. Y el capítulo 24, donde la
Sabiduría habla en primera persona y planta su tienda en Jacob, es el fondo
sobre el que se lee «y habitó —plantó su tienda— entre nosotros» de Juan 1:14.

Los capítulos 44 al 50 son otra cosa: «Alabemos ahora a los varones ilustres»,
un desfile de los padres de Israel de Henoc a Nehemías, y al final el retrato
del sumo sacerdote Simón saliendo del santuario, que es la única descripción de
primera mano que tenemos del culto del segundo templo.

Hay que decir también lo incómodo. Ben Sirá es un hombre de su tiempo y hay
pasajes suyos sobre las mujeres (25:24, 42:9-14) y sobre los esclavos (33:25-30)
que hoy leemos con desagrado, y que aquí se traducen tal como están, sin
suavizarlos. Forman parte del documento; esconderlos sería falsearlo.

Sobre la numeración de esta edición griega: es un desorden, y no se ha
corregido. Faltan versículos enteros (en el capítulo 1, el 5, el 8, el 13 y el
21, que son añadidos tardíos ausentes de este manuscrito), y en muchos sitios el
editor metió dentro de un versículo el número del siguiente, volado o entre
paréntesis. Se ha respetado todo: la traducción lleva los mismos números
volados y los mismos paréntesis, en el mismo sitio, para que el griego y el
español se puedan seguir renglón por renglón. El prólogo del nieto va como
capítulo 0, versículo 0, que es donde lo pone esta edición.
"""

from __future__ import annotations

ECLESIASTICO_ES: dict[tuple[int, ...], str] = {
    # Prólogo del nieto del autor
    (0, 0): "PRÓLOGO. Habiéndosenos dado muchas y grandes cosas por medio de la "
            "ley y de los profetas y de los otros que vinieron tras ellos, por "
            "las cuales conviene alabar a Israel por su instrucción y su "
            "sabiduría; y como no sólo conviene que se hagan entendidos los "
            "que leen, sino que también los amantes del saber puedan ser "
            "útiles a los de fuera, de palabra y por escrito; mi abuelo Jesús, "
            "habiéndose entregado largamente a la lectura de la ley y de los "
            "profetas y de los demás libros de nuestros padres, y habiendo "
            "adquirido en ellos bastante dominio, se sintió llevado también él "
            "a escribir algo de lo que toca a la instrucción y a la sabiduría, "
            "para que los amantes del saber, apropiándose también de esto, "
            "aprovechen mucho más viviendo conforme a la ley. Se os ruega, "
            "pues, que hagáis la lectura con benevolencia y atención, y que "
            "tengáis indulgencia allí donde parezca que, con todo el esfuerzo "
            "puesto en la traducción, nos quedamos cortos en algunas "
            "expresiones; porque no tienen la misma fuerza las cosas dichas en "
            "hebreo que cuando se pasan a otra lengua. Y no sólo éstas, sino "
            "que también la ley misma y las profecías y los demás libros "
            "presentan no poca diferencia al leerse en su propia lengua. "
            "Porque, habiendo llegado a Egipto el año treinta y ocho, bajo el "
            "rey Evérgetes, y habiendo pasado allí un tiempo, encontré un "
            "ejemplar de no pequeña enseñanza. Tuve, pues, por muy necesario "
            "poner yo mismo alguna diligencia y afán en traducir este libro; "
            "porque, empleando mucho desvelo y saber en aquel espacio de "
            "tiempo, lo llevé a término y lo di a la luz, también para los que "
            "en el destierro quieren aprender y disponen sus costumbres para "
            "vivir conforme a la ley.",
    # Capítulo 1
    (1, 1): "Toda sabiduría viene del Señor, y con él está para siempre.",
    (1, 2): "La arena de los mares y las gotas de la lluvia y los días de la "
            "eternidad, ¿quién los contará?",
    (1, 3): "La altura del cielo y la anchura de la tierra y el abismo y la "
            "sabiduría, ¿quién los rastreará?",
    (1, 4): "Antes que todas las cosas fue creada la sabiduría, y la "
            "inteligencia prudente desde la eternidad.",
    (1, 6): "La raíz de la sabiduría, ¿a quién ha sido revelada? Y sus "
            "habilidades, ¿quién las conoció?",
    (1, 7): "Uno solo es sabio, temible en gran manera, sentado sobre su "
            "trono.",
    (1, 9): "El Señor \\u2079mismo la creó, y la vio y la contó, \\u207d\\u00b9\\u2070\\u207e "
            "y la derramó sobre todas sus obras,",
    (1, 10): "sobre todo viviente, conforme a su don, y la dio en abundancia a "
             "los que lo aman.",
    (1, 11): "El temor del Señor es gloria y motivo de orgullo y alegría y "
             "corona de regocijo.",
    (1, 12): "El temor del Señor deleitará el corazón, y dará alegría y gozo y "
             "largura de días. Al que teme al Señor le irá bien al final, y en "
             "el día de su muerte hallará gracia.",
    (1, 14): "Principio de la sabiduría es temer a Dios, y con los fieles fue "
             "creada juntamente en el seno materno;",
    (1, 15): "y entre los hombres hizo su nido, cimiento eterno, y con su "
             "descendencia será fiel.",
    (1, 16): "Plenitud de la sabiduría es temer al Señor, y los embriaga con "
             "sus frutos.",
    (1, 17): "Toda su casa la llenará de cosas deseables, y sus graneros de sus "
             "productos.",
    (1, 18): "Corona de la sabiduría es el temor del Señor, que hace florecer "
             "la paz y la salud de la curación.",
    (1, 19): "Y la vio y la contó; \\u207d\\u00b2\\u2074\\u207e hizo llover ciencia y "
             "conocimiento de entendimiento, y exaltó la gloria de los que la "
             "poseen.",
    (1, 20): "Raíz de la sabiduría es temer al Señor, y sus ramas son largura "
             "de días.",
    (1, 22): "No podrá justificarse la ira injusta, porque el peso de su furor "
             "es su propia caída.",
    (1, 23): "Hasta su tiempo aguantará el que es paciente, y después le "
             "brotará la alegría.",
    (1, 24): "Hasta su tiempo ocultará sus palabras, y los labios de los fieles "
             "contarán su prudencia.",
    (1, 25): "En los tesoros de la sabiduría están las sentencias del saber; "
             "pero para el pecador la piedad es abominación.",
    (1, 26): "¿Deseas la sabiduría? Guarda los mandamientos, y el Señor te la "
             "dará.",
    (1, 27): "Porque sabiduría e instrucción es el temor del Señor, y lo que a "
             "él le agrada \\u207d\\u00b3\\u2075\\u207e es la fidelidad y la mansedumbre.",
    (1, 28): "No seas rebelde al temor del Señor, ni te acerques a él con "
             "corazón doble.",
    (1, 29): "No seas hipócrita en boca de los hombres, y vigila tus labios.",
    (1, 30): "No te ensalces, para que no caigas y atraigas la deshonra sobre "
             "tu alma, \\u207d\\u00b3\\u2079\\u207e y el Señor descubra lo que escondes y te "
             "derribe en medio de la asamblea, \\u207d\\u2074\\u2070\\u207e porque no te "
             "acercaste con temor del Señor y tu corazón estaba lleno de "
             "engaño.",

    # Capítulo 2
    (2, 1): "Hijo, si te llegas a servir al Señor Dios, prepara tu alma para la "
            "prueba.",
    (2, 2): "Endereza tu corazón y sé firme, y no te precipites en tiempo de "
            "adversidad.",
    (2, 3): "Únete a él y no te apartes, para que crezcas al final de tus días.",
    (2, 4): "Todo lo que te sobrevenga, acéptalo, y en los reveses de tu "
            "humillación ten paciencia;",
    (2, 5): "porque en el fuego se prueba el oro, y los hombres aceptos en el "
            "horno de la humillación.",
    (2, 6): "Confía en él, y él te sostendrá; endereza tus caminos y espera en "
            "él.",
    (2, 7): "Los que teméis al Señor, aguardad su misericordia, y no os "
            "desviéis, para que no caigáis.",
    (2, 8): "Los que teméis al Señor, confiad en él, y no se os frustrará "
            "vuestra recompensa.",
    (2, 9): "Los que teméis al Señor, esperad bienes y alegría eterna y "
            "misericordia.",
    (2, 10): "Mirad a las generaciones antiguas y ved: ¿quién confió en el "
             "Señor y quedó avergonzado? \u207d\u00b9\u00b2\u207e ¿O quién "
             "perseveró en su temor y fue abandonado? ¿O quién lo invocó, y él "
             "lo despreció?",
    (2, 11): "Porque compasivo y misericordioso es el Señor, y perdona los "
             "pecados y salva en tiempo de tribulación.",
    (2, 12): "¡Ay de los corazones cobardes y de las manos flojas, y del "
             "pecador que anda por dos sendas!",
    (2, 13): "¡Ay del corazón flojo, porque no cree! Por eso no será "
             "protegido.",
    (2, 14): "¡Ay de vosotros, los que habéis perdido la paciencia! ¿Y qué "
             "haréis cuando el Señor os visite?",
    (2, 15): "Los que temen al Señor no serán rebeldes a sus palabras, y los "
             "que lo aman guardarán sus caminos.",
    (2, 16): "Los que temen al Señor buscarán lo que le agrada, y los que lo "
             "aman se saciarán de la ley.",
    (2, 17): "Los que temen al Señor prepararán sus corazones, y delante de él "
             "humillarán sus almas.",
    (2, 18): "Caigamos en manos del Señor y no en manos de los hombres; "
             "\u207d\u00b2\u00b3\u207e porque, como es su grandeza, así es también su "
             "misericordia.",
    # Capítulo 3
    (3, 1): "Escuchadme a mí, vuestro padre, hijos, y obrad así para que os "
            "salvéis.",
    (3, 2): "Porque el Señor ha glorificado al padre sobre los hijos, y ha "
            "afirmado sobre los hijos el derecho de la madre.",
    (3, 3): "El que honra a su padre expía sus pecados;",
    (3, 4): "y como el que atesora es el que glorifica a su madre.",
    (3, 5): "El que honra a su padre tendrá alegría en sus hijos; y como el que "
            "atesora es el que glorifica a su madre; y en el día de su oración "
            "será escuchado.",
    (3, 6): "El que glorifica a su padre tendrá larga vida, y el que obedece al "
            "Señor dará descanso a su madre,",
    (3, 7): "y servirá como a señores a los que lo engendraron.",
    (3, 8): "De obra y de palabra honra a tu padre, \u207d\u00b9\u2070\u207e para que "
            "venga sobre ti su bendición;",
    (3, 9): "porque la bendición del padre afianza las casas de los hijos, y la "
            "maldición de la madre arranca los cimientos.",
    (3, 10): "No te gloríes en la deshonra de tu padre, porque la deshonra de "
             "tu padre no es gloria para ti;",
    (3, 11): "porque la gloria del hombre viene de la honra de su padre, y es "
             "oprobio para los hijos una madre sin honor.",
    (3, 12): "Hijo, socorre a tu padre en su vejez, y no lo entristezcas "
             "mientras viva;",
    (3, 13): "y aunque le falte el entendimiento, ten indulgencia, y no lo "
             "menosprecies en la plenitud de tu fuerza.",
    (3, 14): "Porque la caridad para con el padre no será olvidada, "
             "\u207d\u00b9\u2076\u207e y en lugar de tus pecados \u207d\u00b9\u2077\u207e te será "
             "edificada;",
    (3, 15): "en el día de tu tribulación se acordará de ti; como el buen "
             "tiempo deshace la escarcha, así se disolverán tus pecados.",
    (3, 16): "Como un blasfemo es el que abandona a su padre, y maldito del "
             "Señor el que exaspera a su madre.",
    (3, 17): "Hijo, lleva a cabo tus obras con mansedumbre, y serás amado más "
             "que el hombre generoso.",
    (3, 18): "Cuanto más grande seas, tanto más humíllate, y ante el Señor "
             "hallarás gracia;",
    (3, 20): "porque grande es el poder del Señor, y es glorificado por los "
             "humildes.",
    (3, 21): "No busques lo que es demasiado difícil para ti, ni escudriñes lo "
             "que excede tus fuerzas.",
    (3, 22): "Lo que se te ha mandado, eso medita; \u207d\u00b2\u00b3\u207e porque no "
             "tienes necesidad de lo que está oculto.",
    (3, 23): "En lo que sobrepasa tus obras no te metas; \u207d\u00b2\u2075\u207e porque "
             "más de lo que alcanza el entendimiento humano se te ha "
             "mostrado.",
    (3, 25): "Porque a muchos los extravió su presunción, y una mala sospecha "
             "hizo resbalar su entendimiento.",
    (3, 26): "Y el que ama el peligro caerá en él; el corazón duro será "
             "maltratado al final; el corazón duro se hará pesado al final.",
    (3, 27): "El corazón duro se cargará de dolores, y el pecador añadirá "
             "pecado a pecados.",
    (3, 28): "Para la desgracia del soberbio no hay remedio, porque la planta "
             "de la maldad ha echado raíz en él.",
    (3, 29): "El corazón del inteligente meditará la sentencia, y el oído que "
             "escucha es el deseo del sabio.",
    (3, 30): "El agua apaga el fuego que arde, y la limosna expía los pecados.",
    (3, 31): "El que devuelve favores se acuerda de lo que vendrá después, y en "
             "el tiempo de su caída hallará apoyo.",

    # Capítulo 4
    (4, 1): "Hijo, no le quites al pobre su sustento, ni hagas esperar a los "
            "ojos del necesitado.",
    (4, 2): "No entristezcas al alma hambrienta, ni exasperes al hombre en su "
            "indigencia.",
    (4, 3): "No turbes más un corazón ya irritado, ni difieras la limosna al "
            "que la pide.",
    (4, 4): "No rechaces al suplicante afligido, ni apartes tu rostro del "
            "pobre.",
    (4, 5): "No apartes tus ojos del que te pide, ni des ocasión a que un "
            "hombre te maldiga;",
    (4, 6): "porque, si te maldice en la amargura de su alma, el que lo hizo "
            "escuchará su súplica.",
    (4, 7): "Hazte amable a la asamblea, y ante un poderoso inclina tu cabeza.",
    (4, 8): "Inclina tu oído al pobre, y respóndele con palabras de paz y con "
            "mansedumbre.",
    (4, 9): "Libra al oprimido de la mano del opresor, y no seas pusilánime al "
            "juzgar.",
    (4, 10): "Sé para los huérfanos como un padre, y como un marido para su "
             "madre; \u207d\u00b9\u00b9\u207e y serás como hijo del Altísimo, y él te "
             "amará más que tu madre.",
    (4, 11): "La sabiduría exalta a sus hijos, y recoge a los que la buscan.",
    (4, 12): "El que la ama, ama la vida, y los que madrugan por ella se "
             "llenarán de alegría.",
    (4, 13): "El que la posee heredará gloria, y donde ella entra, el Señor "
             "bendice.",
    (4, 14): "Los que le dan culto sirven al Santo, y a los que la aman los ama "
             "el Señor.",
    (4, 15): "El que la obedece juzgará a las naciones, y el que se llega a "
             "ella habitará seguro.",
    (4, 16): "Si confías en ella, la heredarás, y sus generaciones la "
             "poseerán;",
    (4, 17): "porque al principio camina con él por sendas torcidas, "
             "\u207d\u00b9\u2079\u207e y hace venir sobre él temor y miedo, y lo atormenta "
             "con su disciplina hasta confiar en su alma; y lo prueba con sus "
             "preceptos.",
    (4, 18): "Y de nuevo volverá derecha hacia él y lo alegrará, "
             "\u207d\u00b2\u00b9\u207e y le revelará sus secretos.",
    (4, 19): "Y si se extravía, lo abandonará y lo entregará en manos de su "
             "propia ruina.",
    (4, 20): "Observa la ocasión y guárdate del mal, \u207d\u00b2\u2074\u207e y no te "
             "avergüences de ti mismo;",
    (4, 21): "porque hay una vergüenza que acarrea pecado, y hay una vergüenza "
             "que es gloria y gracia.",
    (4, 22): "No tengas acepción de personas contra ti mismo, "
             "\u207d\u00b2\u2077\u207e ni te avergüences para tu propia caída.",
    (4, 23): "No retengas la palabra en el momento oportuno,",
    (4, 24): "porque en la palabra se reconoce la sabiduría, y la instrucción "
             "en lo que dice la lengua.",
    (4, 25): "No contradigas a la verdad, y avergüénzate de tu ignorancia.",
    (4, 26): "No te avergüences de confesar tus pecados, \u207d\u00b3\u00b2\u207e ni "
             "fuerces la corriente del río.",
    (4, 27): "Y no te postres ante un hombre necio, ni hagas acepción del "
             "poderoso.",
    (4, 28): "Lucha hasta la muerte por la verdad, y el Señor Dios peleará por "
             "ti.",
    (4, 29): "No seas áspero en tu lengua, ni flojo y descuidado en tus obras.",
    (4, 30): "No seas como un león en tu casa, ni fantasioso con tus criados.",
    (4, 31): "No esté tu mano extendida para recibir y encogida para dar.",
    # Capítulo 5
    (5, 1): "No te apoyes en tus riquezas, ni digas: «Me basta con lo que "
            "tengo.»",
    (5, 2): "No te dejes llevar de tu apetito y de tu fuerza, andando tras los "
            "deseos de tu corazón.",
    (5, 3): "Y no digas: «¿Quién podrá conmigo?», porque el Señor, vengando, te "
            "tomará cuenta.",
    (5, 4): "No digas: «Pequé, ¿y qué me ha pasado?», porque el Señor es "
            "paciente.",
    (5, 5): "No estés sin temor respecto al perdón, añadiendo pecado a "
            "pecados;",
    (5, 6): "y no digas: «Su compasión es grande, perdonará la multitud de mis "
            "pecados»; \u207d\u2077\u207e porque de él vienen la misericordia y la "
            "ira, y sobre los pecadores descansa su furor.",
    (5, 7): "No tardes en volverte al Señor, ni lo dejes de un día para otro; "
            "\u207d\u2079\u207e porque de repente saldrá la ira del Señor, y en el "
            "tiempo del castigo perecerás.",
    (5, 8): "No te apoyes en riquezas injustas, porque de nada te servirán en "
            "el día de la desgracia.",
    (5, 9): "No avientes a todos los vientos, ni vayas por todo sendero: así es "
            "el pecador de lengua doble.",
    (5, 10): "Mantente firme en tu convicción, y sea una sola tu palabra.",
    (5, 11): "Sé pronto para escuchar, y responde con calma.",
    (5, 12): "Si tienes entendimiento, responde a tu prójimo; y si no, tu mano "
             "esté sobre tu boca.",
    (5, 13): "Gloria y deshonra están en el hablar, y la lengua del hombre es "
             "su caída.",
    (5, 14): "No te ganes fama de chismoso, ni tiendas emboscadas con tu "
             "lengua; \u207d\u00b9\u2077\u207e porque para el ladrón hay vergüenza, y "
             "mala condena para el de lengua doble.",
    (5, 15): "Ni en lo grande ni en lo pequeño cometas falta,",
    # Capítulo 6
    (6, 1): "y de amigo no te vuelvas enemigo; porque un mal nombre hereda "
            "vergüenza y oprobio: así es el pecador de lengua doble.",
    (6, 2): "No te dejes llevar del arrebato de tu alma, para que tu alma no "
            "sea destrozada como un toro;",
    (6, 3): "devorarás tus hojas y perderás tus frutos, y te quedarás como un "
            "árbol seco.",
    (6, 4): "El alma malvada pierde al que la tiene, y lo hace el escarnio de "
            "sus enemigos.",
    (6, 5): "La garganta dulce multiplica los amigos, y la lengua amable "
            "multiplica las palabras cordiales.",
    (6, 6): "Sean muchos los que viven en paz contigo, pero tus consejeros, uno "
            "de mil.",
    (6, 7): "Si adquieres un amigo, adquiérelo probándolo, y no te fíes de él "
            "demasiado pronto.",
    (6, 8): "Porque hay amigo que lo es para su propia ocasión, y no permanece "
            "en el día de tu tribulación;",
    (6, 9): "y hay amigo que se vuelve enemigo, y descubre la disputa para "
            "afrenta tuya;",
    (6, 10): "y hay amigo que lo es de la mesa, y no permanece en el día de tu "
             "tribulación;",
    (6, 11): "y en tu prosperidad será como tú, y con tus criados hablará con "
             "desenvoltura;",
    (6, 12): "si vienes a menos, se pondrá contra ti, y de tu presencia se "
             "esconderá.",
    (6, 13): "Apártate de tus enemigos, y ten cuidado con tus amigos.",
    (6, 14): "Un amigo fiel es refugio seguro; el que lo halla, halló un "
             "tesoro.",
    (6, 15): "Para un amigo fiel no hay precio, ni hay peso que mida su valor.",
    (6, 16): "Un amigo fiel es medicina de vida, y los que temen al Señor lo "
             "encontrarán.",
    (6, 17): "El que teme al Señor endereza su amistad, porque como es él, así "
             "es también su prójimo.",
    (6, 18): "Hijo, desde tu juventud escoge la instrucción, y hasta las canas "
             "hallarás sabiduría.",
    (6, 19): "Acércate a ella como el que ara y el que siembra, y aguarda sus "
             "buenos frutos; \u207d\u00b2\u2070\u207e porque en labrarla te fatigarás "
             "poco, y pronto comerás de sus productos.",
    (6, 20): "¡Qué áspera resulta a los ignorantes! Y el insensato no persevera "
             "en ella;",
    (6, 21): "pesará sobre él como piedra de prueba, y no tardará en echarla de "
             "sí.",
    (6, 22): "Porque la sabiduría es conforme a su nombre, y no se manifiesta a "
             "muchos.",
    (6, 23): "Escucha, hijo, y acepta mi parecer, y no rechaces mi consejo;",
    (6, 24): "y mete tus pies en sus grillos, y tu cuello en su collar.",
    (6, 25): "Ofrece tu hombro y llévala, y no te fastidien sus ataduras.",
    (6, 26): "Acércate a ella con toda tu alma, y con toda tu fuerza guarda sus "
             "caminos.",
    (6, 27): "Rastréala y búscala, y se te dará a conocer; y una vez que la "
             "tengas, no la sueltes;",
    (6, 28): "porque al fin hallarás en ella el descanso, y se te trocará en "
             "alegría;",
    (6, 29): "y sus grillos serán para ti amparo poderoso, y sus collares "
             "vestidura de gloria.",
    (6, 30): "Porque hay sobre ella un adorno de oro, y sus ataduras son hilo "
             "de púrpura.",
    (6, 31): "Vestidura de gloria te pondrás con ella, y corona de regocijo te "
             "ceñirás.",
    (6, 32): "Si quieres, hijo, serás instruido, y si aplicas tu alma, serás "
             "sagaz.",
    (6, 33): "Si te gusta escuchar, recibirás; y si inclinas tu oído, serás "
             "sabio.",
    (6, 34): "Ponte en medio de la asamblea de los ancianos, y al que sea "
             "sabio, únete a él.",
    (6, 35): "Quiere escuchar toda narración divina, y no se te escapen los "
             "proverbios de la prudencia.",
    (6, 36): "Si ves a un hombre entendido, madruga hacia él, y que tu pie gaste "
             "los escalones de su puerta.",
    (6, 37): "Medita en los preceptos del Señor, y ocúpate de continuo en sus "
             "mandamientos; él afianzará tu corazón, y el deseo de sabiduría te "
             "será concedido.",

    # Capítulo 7
    (7, 1): "No hagas el mal, y el mal no te alcanzará.",
    (7, 2): "Apártate de lo injusto, y se apartará de ti.",
    (7, 3): "Hijo, no siembres en surcos de injusticia, y no los segarás siete "
            "veces.",
    (7, 4): "No pidas al Señor el mando, ni al rey un asiento de honor.",
    (7, 5): "No te tengas por justo delante del Señor, ni te hagas el sabio "
            "ante el rey.",
    (7, 6): "No pretendas ser juez, no sea que no tengas fuerza para acabar con "
            "las injusticias; no sea que te intimides ante el poderoso y "
            "pongas un tropiezo en tu rectitud.",
    (7, 7): "No peques contra la multitud de la ciudad, ni te rebajes ante la "
            "turba.",
    (7, 8): "No ates dos veces el pecado, porque ni con uno solo quedarás sin "
            "culpa.",
    (7, 9): "No digas: «Mirará la cantidad de mis ofrendas, y cuando yo las "
            "presente al Dios altísimo, las aceptará.»",
    (7, 10): "No seas pusilánime en tu oración, ni descuides el dar limosna.",
    (7, 11): "No te burles del hombre que está en la amargura de su alma, "
             "porque hay quien humilla y quien ensalza.",
    (7, 12): "No ares la mentira contra tu hermano, ni hagas lo mismo con tu "
             "amigo.",
    (7, 13): "No quieras decir ninguna clase de mentira, porque la costumbre de "
             "mentir no lleva a nada bueno.",
    (7, 14): "No parlotees en la asamblea de los ancianos, ni repitas palabras "
             "en tu oración.",
    (7, 15): "No aborrezcas el trabajo fatigoso ni la labranza, creada por el "
             "Altísimo.",
    (7, 16, "a"): "No te cuentes entre la multitud de los pecadores;",
    (7, 16, "b"): "acuérdate de que la ira no tardará.",
    (7, 17, "a"): "Humilla mucho tu alma,",
    (7, 17, "b"): "porque el castigo del impío es fuego y gusano.",
    (7, 18): "No cambies un amigo por algo sin valor, ni un hermano de verdad "
             "por el oro de Ofir.",
    (7, 19): "No desdeñes a una mujer sabia y buena, porque su gracia vale más "
             "que el oro.",
    (7, 20): "No maltrates al criado que trabaja con lealtad, ni al jornalero "
             "que se entrega de alma.",
    (7, 21): "Ame tu alma al criado bueno, y no le niegues la libertad.",
    (7, 22): "¿Tienes ganado? Cuídalo; y si te es útil, consérvalo.",
    (7, 23): "¿Tienes hijos? Edúcalos, y doblégales el cuello desde la "
             "juventud.",
    (7, 24): "¿Tienes hijas? Vela por su cuerpo, y no les muestres un rostro "
             "demasiado risueño.",
    (7, 25): "Casa a tu hija, y habrás llevado a cabo una gran obra; y dásela a "
             "un hombre sensato.",
    (7, 26): "¿Tienes mujer conforme a tu alma? No la eches.",
    (7, 27): "Con todo el corazón \u207d\u00b2\u2079\u207e glorifica a tu padre, y no "
             "olvides los dolores de tu madre.",
    (7, 28): "Acuérdate de que por ellos naciste; ¿y qué les darás tú a cambio "
             "de lo que ellos te dieron?",
    (7, 29): "Con toda tu alma reverencia al Señor, y venera a sus sacerdotes.",
    (7, 30): "Con toda tu fuerza ama al que te hizo, y no abandones a sus "
             "ministros.",
    (7, 31): "Teme al Señor y honra al sacerdote, \u207d\u00b3\u2074\u207e y dale su "
             "parte como se te ha mandado desde el principio: "
             "\u207d\u00b3\u2075\u207e el sacrificio por la culpa y la ofrenda de las "
             "espaldillas y el sacrificio de consagración y las primicias.",
    (7, 32): "Y al pobre tiéndele tu mano, para que sea perfecta tu bendición.",
    (7, 33): "El favor de un regalo alcanza a todo viviente, y tampoco al "
             "muerto le niegues tu favor.",
    (7, 34): "No te apartes de los que lloran, y haz duelo con los que hacen "
             "duelo.",
    (7, 35): "No te pese visitar al enfermo, porque por esas cosas serás "
             "amado.",
    (7, 36): "En todas tus palabras acuérdate de tu fin, y jamás pecarás.",
    # Capítulo 8
    (8, 1): "No contiendas con un hombre poderoso, no sea que caigas en sus "
            "manos.",
    (8, 2): "No riñas con un hombre rico, no sea que su peso te aplaste; "
            "\u207d\u00b3\u207e porque a muchos perdió el oro, y torció los corazones "
            "de los reyes.",
    (8, 3): "No contiendas con un hombre deslenguado, ni amontones leña sobre "
            "su fuego.",
    (8, 4): "No bromees con el ignorante, para que no queden deshonrados tus "
            "antepasados.",
    (8, 5): "No eches en cara su pecado al hombre que se aparta de él; "
            "acuérdate de que todos somos dignos de castigo.",
    (8, 6): "No desprecies a un hombre en su vejez, porque también nosotros "
            "envejecemos.",
    (8, 7): "No te alegres por un muerto; acuérdate de que todos morimos.",
    (8, 8): "No desdeñes la enseñanza de los sabios, y frecuenta sus "
            "proverbios; \u207d\u00b9\u2070\u207e porque de ellos aprenderás la "
            "instrucción y a servir a los grandes.",
    (8, 9): "No desprecies lo que cuentan los ancianos, porque también ellos lo "
            "aprendieron de sus padres; porque de ellos aprenderás el "
            "entendimiento, y a dar respuesta en el momento necesario.",
    (8, 10): "No atices las brasas del pecador, no sea que te quemes en la "
             "llama de su fuego.",
    (8, 11): "No te levantes ante la cara del insolente, para que no se ponga "
             "como emboscada contra tu boca.",
    (8, 12): "No prestes a un hombre más fuerte que tú; y si le prestas, dalo "
             "por perdido.",
    (8, 13): "No salgas fiador por encima de tus fuerzas; y si sales fiador, "
             "cuenta con tener que pagar.",
    (8, 14): "No pleitees con un juez, porque lo juzgarán conforme a su "
             "dignidad.",
    (8, 15): "No emprendas camino con un temerario, no sea que se te haga "
             "pesado; porque él hará su voluntad, y perecerás con él por su "
             "insensatez.",
    (8, 16): "No riñas con un colérico, ni atravieses con él el desierto; "
             "porque la sangre no es nada a sus ojos, y donde no haya auxilio "
             "te derribará.",
    (8, 17): "No tomes consejo de un necio, porque no podrá guardar el "
             "secreto.",
    (8, 18): "Delante de un extraño no hagas nada secreto, porque no sabes lo "
             "que va a parir.",
    (8, 19): "No abras tu corazón a cualquier hombre, ni te devuelva mal por "
             "bien.",
    # Capítulo 9
    (9, 1): "No tengas celos de la mujer de tu seno, ni le enseñes contra ti "
            "mismo una mala lección.",
    (9, 2): "No entregues tu alma a una mujer, para que no se enseñoree de tu "
            "fuerza.",
    (9, 3): "No salgas al encuentro de una mujer ligera, no sea que caigas en "
            "sus lazos.",
    (9, 4): "No frecuentes a una cantora, no sea que quedes preso en sus "
            "artes.",
    (9, 5): "No fijes la vista en una doncella, no sea que tropieces y tengas "
            "que pagar por ella.",
    (9, 6): "No entregues tu alma a las prostitutas, para que no pierdas tu "
            "herencia.",
    (9, 7): "No andes mirando por las calles de la ciudad, ni vagues por sus "
            "lugares solitarios.",
    (9, 8): "Aparta tus ojos de la mujer hermosa, y no te quedes mirando la "
            "belleza ajena; \u207d\u2079\u207e por la belleza de una mujer muchos se "
            "perdieron, y de ahí el amor se enciende como fuego.",
    (9, 9): "Con mujer casada no te sientes nunca, \u207d\u00b9\u00b3\u207e ni te "
            "sientes a beber vino con ella, no sea que tu alma se incline "
            "hacia ella y con tu pasión resbales a la perdición.",
    (9, 10): "No abandones al amigo antiguo, porque el nuevo no es igual a él; "
             "\u207d\u00b9\u2075\u207e vino nuevo, amigo nuevo: si envejece, lo beberás "
             "con gusto.",
    (9, 11): "No envidies la gloria del pecador, porque no sabes cuál será su "
             "ruina.",
    (9, 12): "No te complazcas en lo que complace a los impíos; acuérdate de "
             "que hasta el sepulcro no serán justificados.",
    (9, 13): "Mantente lejos del hombre que tiene poder para matar, y no "
             "tendrás que temer el miedo de la muerte; \u207d\u00b9\u2079\u207e y si te "
             "acercas a él, no cometas falta, para que no te quite la vida; "
             "\u207d\u00b2\u2070\u207e date cuenta de que caminas en medio de trampas y "
             "andas sobre las almenas de la ciudad.",
    (9, 14): "Según tus fuerzas, mide a tus prójimos, y toma consejo de los "
             "sabios;",
    (9, 15): "y sea con los entendidos tu conversación, y todo lo que digas, en "
             "la ley del Altísimo.",
    (9, 16): "Sean hombres justos tus comensales, y esté tu orgullo en el temor "
             "del Señor.",
    (9, 17): "Por la mano de los artesanos se alaba la obra, y el que gobierna "
             "al pueblo es sabio en su palabra.",
    (9, 18): "Temible es en su ciudad el hombre deslenguado, y el atropellado "
             "al hablar será aborrecido.",
}
