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

Sobre el texto griego mismo: esta digitalización arrastra muchos errores de OCR
—letras cambiadas, palabras pegadas, una palabra que se quedó al final del
versículo anterior—. Donde el error es evidente se traduce la palabra que el
editor quiso poner, sin señalarlo; donde falta algo que no se puede recuperar,
va […]. Los títulos de sección que Swete imprime dentro del texto («Dominio del
alma», «Himno de los padres») se traducen en el sitio donde están.
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
    (1, 9): "El Señor \u2079mismo la creó, y la vio y la contó, \u207d\u00b9\u2070\u207e "
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
    (1, 19): "Y la vio y la contó; \u207d\u00b2\u2074\u207e hizo llover ciencia y "
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
             "él le agrada \u207d\u00b3\u2075\u207e es la fidelidad y la mansedumbre.",
    (1, 28): "No seas rebelde al temor del Señor, ni te acerques a él con "
             "corazón doble.",
    (1, 29): "No seas hipócrita en boca de los hombres, y vigila tus labios.",
    (1, 30): "No te ensalces, para que no caigas y atraigas la deshonra sobre "
             "tu alma, \u207d\u00b3\u2079\u207e y el Señor descubra lo que escondes y te "
             "derribe en medio de la asamblea, \u207d\u2074\u2070\u207e porque no te "
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

    # Capítulo 10
    (10, 1): "El juez sabio instruirá a su pueblo, y el gobierno del prudente "
             "será ordenado.",
    (10, 2): "Según el juez del pueblo, así son sus ministros; y según el que "
             "gobierna la ciudad, así todos los que habitan en ella.",
    (10, 3): "El rey sin instrucción arruinará a su pueblo, y la ciudad será "
             "poblada por la prudencia de los poderosos.",
    (10, 4): "En la mano del Señor está el poder sobre la tierra, y a su "
             "tiempo levantará sobre ella al que conviene.",
    (10, 5): "En la mano del Señor está la prosperidad del hombre, y sobre el "
             "rostro del escriba pondrá su gloria.",
    (10, 6): "Por ninguna injuria guardes rencor a tu prójimo, y no hagas "
             "nada con obras de soberbia.",
    (10, 7): "Odiosa es la soberbia delante del Señor y de los hombres, y "
             "para ambos es falta la injusticia.",
    (10, 8): "El reino pasa de una nación a otra por causa de las "
             "injusticias, de las violencias y de las riquezas.",
    (10, 9): "¿De qué se ensoberbece la tierra y la ceniza? Porque aun en "
             "vida he arrojado sus entrañas.",
    (10, 10): "Larga enfermedad: el médico se burla; y el que hoy es rey, "
              "mañana morirá.",
    (10, 11): "Porque cuando el hombre muere, heredará reptiles y fieras y "
              "gusanos.",
    (10, 12): "El principio de la soberbia del hombre es apartarse del Señor, "
              "⁽¹⁵⁾ y su corazón se apartó del que lo hizo.",
    (10, 13): "Porque el principio de la soberbia es el pecado, y el que se "
              "aferra a él derramará abominación como lluvia. ⁽¹⁶⁾ Por eso el "
              "Señor hizo extraordinarios sus castigos, y los destruyó por "
              "completo.",
    (10, 14): "El Señor derribó los tronos de los príncipes, y sentó en su "
              "lugar a los mansos.",
    (10, 15): "El Señor arrancó las raíces de las naciones, y plantó en su "
              "lugar a los humildes.",
    (10, 16): "El Señor trastornó las tierras de las naciones, y las destruyó "
              "hasta los cimientos de la tierra.",
    (10, 17): "Secó a algunos de ellos y los destruyó, e hizo cesar de la "
              "tierra su memoria.",
    (10, 18): "No fue creada la soberbia para los hombres, ni la furia de la "
              "ira para los nacidos de mujer.",
    (10, 19): "¿Qué linaje es honroso? El linaje del hombre. ¿Qué linaje es "
              "honroso? Los que temen al Señor. ¿Qué linaje es deshonroso? El "
              "linaje del hombre. ¿Qué linaje es deshonroso? Los que "
              "traspasan los mandamientos.",
    (10, 20): "En medio de los hermanos, el que los gobierna es honrado; y "
              "los que temen al Señor, a sus ojos.",
    (10, 22): "El rico y el ilustre y el pobre: su gloria es el temor del "
              "Señor.",
    (10, 23): "No es justo deshonrar al pobre entendido, ni conviene "
              "glorificar al hombre pecador.",
    (10, 24): "El magnate y el juez y el poderoso serán honrados, pero "
              "ninguno de ellos es mayor que el que teme al Señor.",
    (10, 25): "Al siervo sabio le servirán los libres, y el hombre entendido "
              "no murmurará.",
    (10, 26): "No te hagas el sabio para hacer tu trabajo, ni te glorifiques "
              "en el tiempo de tu estrechez.",
    (10, 27): "Mejor es el que trabaja y abunda en todo que el que anda "
              "glorificándose y carece de pan.",
    (10, 28): "Hijo, glorifica tu alma con mansedumbre, y dale honra según lo "
              "que merece.",
    (10, 29): "Al que peca contra su propia alma, ¿quién lo justificará? ¿Y "
              "quién glorificará al que deshonra su propia vida?",
    (10, 30): "El pobre es honrado por su saber, y el rico es honrado por su "
              "riqueza.",
    (10, 31): "Pero el que es honrado en la pobreza, ¡cuánto más en la "
              "riqueza! Y el que es despreciado en la riqueza, ¡cuánto más en "
              "la pobreza!",

    # Capítulo 11
    (11, 1): "La sabiduría del humilde le hace levantar la cabeza, y lo "
             "sentará en medio de los magnates.",
    (11, 2): "No alabes a un hombre por su hermosura, ni abomines de un "
             "hombre por su apariencia.",
    (11, 3): "Pequeña es la abeja entre los que vuelan, pero su fruto es el "
             "primero entre las dulzuras.",
    (11, 4): "No te gloríes del vestido que te cubre, ni te engrías en el día "
             "de la gloria; porque admirables son las obras del Señor, y "
             "ocultas a los hombres sus obras.",
    (11, 5): "Muchos tiranos se sentaron en el suelo, y el que nadie "
             "sospechaba llevó la diadema.",
    (11, 6): "Muchos poderosos fueron deshonrados en gran manera, y los "
             "ilustres fueron entregados en manos de otros.",
    (11, 7): "Antes de examinar, no reprendas; considera primero, y entonces "
             "censura.",
    (11, 8): "Antes de oír, no respondas, y no te entrometas en medio de las "
             "palabras ajenas.",
    (11, 9): "No disputes por asunto que no te concierne, y no te sientes con "
             "los pecadores cuando juzgan.",
    (11, 10): "Hijo, no se ocupen tus acciones en muchas cosas; si las "
              "multiplicas, no quedarás sin culpa; y aunque corras tras "
              "ellas, no las alcanzarás, ni escaparás aunque huyas.",
    (11, 11): "Hay quien se fatiga y trabaja y se apresura, y tanto más se "
              "queda atrás.",
    (11, 12): "Hay quien es tardo y necesitado de socorro, falto de fuerzas y "
              "sobrado de pobreza; ⁽¹³⁾ y los ojos del Señor lo miraron para "
              "bien, y lo levantó de su abatimiento,",
    (11, 13): "y le hizo levantar la cabeza, y muchos se maravillaron de él.",
    (11, 14): "Lo bueno y lo malo, la vida y la muerte, la pobreza y la "
              "riqueza, vienen del Señor.",
    (11, 17): "El don del Señor permanece con los piadosos, y su favor "
              "prosperará para siempre.",
    (11, 18): "Hay quien se enriquece a fuerza de cuidado y de tacañería, y "
              "ésta es la parte de su recompensa:",
    (11, 19): "cuando dice: «He hallado descanso, y ahora comeré de mis "
              "bienes», ⁽²⁰⁾ no sabe cuánto tiempo pasará, y los dejará a "
              "otros y morirá.",
    (11, 20): "Mantente firme en tu compromiso y ocúpate en él, y envejece en "
              "tu trabajo.",
    (11, 21): "No te maravilles de las obras del pecador; confía en el Señor "
              "y persevera en tu trabajo; ⁽²³⁾ porque es cosa fácil a los "
              "ojos del Señor enriquecer de repente, en un instante, al "
              "pobre.",
    (11, 22): "La bendición del Señor está en la recompensa del piadoso, y en "
              "una hora repentina hace florecer su bendición.",
    (11, 23): "No digas: «¿Qué necesidad tengo? ¿Y qué bienes tendré de ahora "
              "en adelante?»",
    (11, 24): "No digas: «Tengo bastante; ¿y qué mal me podrá venir de ahora "
              "en adelante?»",
    (11, 25): "En el día de los bienes se olvidan los males, y en el día de "
              "los males no se acuerda uno de los bienes;",
    (11, 26): "porque es cosa fácil delante del Señor, en el día de la "
              "muerte, dar al hombre según sus caminos.",
    (11, 27): "El mal de una hora hace olvidar el deleite, y en el fin del "
              "hombre se descubren sus obras.",
    (11, 28): "Antes de la muerte no llames dichoso a nadie; en sus hijos "
              "será conocido el hombre.",
    (11, 29): "No metas a todo hombre en tu casa, porque muchas son las "
              "asechanzas del engañoso.",
    (11, 30): "Perdiz cazadora en la jaula, así es el corazón del soberbio; y "
              "como el espía, acecha tu caída.",
    (11, 31): "Porque trocando el bien en mal, pone asechanzas, y en las "
              "cosas escogidas echará tacha.",
    (11, 32): "De una chispa de fuego se multiplican las brasas, y el hombre "
              "pecador pone asechanzas para derramar sangre.",
    (11, 33): "Guárdate del malhechor, porque trama maldades, no sea que te "
              "eche una mancha para siempre.",
    (11, 34): "Hospeda en tu casa al extraño, y te trastornará con alborotos "
              "y te hará ajeno a los tuyos.",

    # Capítulo 12
    (12, 1): "Si haces el bien, mira a quién lo haces, y tendrás "
             "agradecimiento por tus beneficios.",
    (12, 2): "Haz el bien al piadoso, y hallarás recompensa; y si no de él, "
             "al menos del Altísimo.",
    (12, 3): "No hay bien para el que persiste en el mal, ni para el que no "
             "hace limosna.",
    (12, 4): "Da al piadoso, y no socorras al pecador.",
    (12, 5): "Haz el bien al humilde, y no des al impío; niégale su pan y no "
             "se lo des, para que con él no te domine; ⁽⁷⁾ porque recibirás "
             "doble mal por todos los bienes que le hayas hecho.",
    (12, 6): "Porque también el Altísimo aborrece a los pecadores, y a los "
             "impíos les dará su castigo.",
    (12, 7): "Da al bueno, y no socorras al pecador.",
    (12, 8): "No se conocerá al amigo en la prosperidad, ni se ocultará el "
             "enemigo en la adversidad.",
    (12, 9): "En la prosperidad del hombre sus enemigos están tristes, y en "
             "su adversidad aun el amigo se aparta.",
    (12, 10): "No te fíes jamás de tu enemigo; porque como el bronce se cubre "
              "de herrumbre, así es su maldad.",
    (12, 11): "Y aunque se humille y ande encorvado, pon atención en tu alma "
              "y guárdate de él; y serás para él como quien ha limpiado un "
              "espejo, y sabrás que no se ha empañado del todo.",
    (12, 12): "No lo pongas junto a ti, no sea que te derribe y se ponga en "
              "tu lugar; no lo sientes a tu derecha, no sea que busque tu "
              "asiento, y al fin reconozcas mis palabras y te duelas de mis "
              "dichos.",
    (12, 13): "¿Quién tendrá compasión del encantador mordido por la "
              "serpiente, y de todos los que se acercan a las fieras?",
    (12, 14): "Así tampoco del que se junta con el hombre pecador y se "
              "revuelve en sus pecados.",
    (12, 15): "Una hora permanecerá contigo, y si tropiezas, no aguantará.",
    (12, 16): "Con sus labios el enemigo endulzará sus palabras, y en su "
              "corazón tramará echarte en la fosa; ⁽¹⁶⁾ con sus ojos llorará "
              "el enemigo, y si halla ocasión, no se saciará de sangre.",
    (12, 17): "Si te sobreviene algún mal, lo hallarás allí antes que tú, "
              "⁽¹⁸⁾ y como quien te ayuda te echará la zancadilla.",
    (12, 18): "Moverá la cabeza y batirá las manos, y murmurará mucho y "
              "mudará el semblante.",

    # Capítulo 13
    (13, 1): "El que toca la pez se mancha, y el que se junta con el soberbio "
             "se hará semejante a él.",
    (13, 2): "No cargues un peso superior a ti, y no te asocies con quien es "
             "más fuerte y más rico que tú. ⁽³⁾ ¿Qué comunión tendrá la olla "
             "con el caldero? Éste chocará, y aquélla se quebrará.",
    (13, 3): "El rico comete injusticia, y encima se indigna; el pobre sufre "
             "injusticia, y encima tiene que suplicar.",
    (13, 4): "Si le eres útil, se servirá de ti; y si te quedas sin nada, te "
             "abandonará.",
    (13, 5): "Si tienes, vivirá contigo y te dejará vacío, y él no sentirá "
             "pena.",
    (13, 6): "¿Tiene necesidad de ti? Te engañará, y te sonreirá y te dará "
             "esperanza; te hablará bellas palabras y te dirá: «¿Qué "
             "necesitas?»",
    (13, 7): "Y te avergonzará con sus manjares, hasta dejarte vacío dos y "
             "tres veces, y al fin se burlará de ti; después te verá y te "
             "abandonará, y moverá la cabeza contra ti.",
    (13, 8): "Cuídate de no ser engañado, y de no ser humillado en tu "
             "alegría.",
    (13, 9): "Cuando te invite un poderoso, retírate, y tanto más te "
             "invitará.",
    (13, 10): "No te entrometas, para que no seas rechazado; ni te alejes "
              "mucho, para que no seas olvidado.",
    (13, 11): "No pretendas hablar con él de igual a igual, ni te fíes de sus "
              "muchas palabras; porque con su mucho hablar te pondrá a "
              "prueba, y como sonriendo te examinará.",
    (13, 12): "Despiadado es el que no guarda las palabras, y no se abstendrá "
              "del maltrato ni de las cadenas.",
    (13, 13): "Guárdalo y pon mucha atención, porque andas en compañía de tu "
              "propia caída.",
    (13, 15): "Todo animal ama a su semejante, y todo hombre a su prójimo.",
    (13, 16): "Toda carne se junta según su especie, y el hombre se allegará "
              "a su semejante.",
    (13, 17): "¿Qué comunión tendrá el lobo con el cordero? Así el pecador "
              "con el piadoso.",
    (13, 18): "¿Qué paz hay entre la hiena y el perro? ¿Y qué paz entre el "
              "rico y el pobre?",
    (13, 19): "Presa de los leones son los asnos monteses en el desierto; así "
              "los pobres son pasto de los ricos.",
    (13, 20): "Abominación es para el soberbio la humildad; así es "
              "abominación para el rico el pobre.",
    (13, 21): "El rico que vacila es sostenido por sus amigos, pero el "
              "humilde que cae es rechazado aun por sus amigos.",
    (13, 22): "Cuando el rico resbala, muchos son los que lo socorren; habló "
              "cosas indecibles, y lo justificaron. ⁽²⁷⁾ Resbaló el humilde, "
              "y encima lo reprendieron; habló con prudencia, y no se le dio "
              "lugar.",
    (13, 23): "Habló el rico, y todos callaron, y ensalzaron su palabra hasta "
              "las nubes. ⁽²⁹⁾ Habló el pobre, y dijeron: «¿Quién es éste?» Y "
              "si tropieza, acabarán de derribarlo.",
    (13, 24): "Buena es la riqueza en la que no hay pecado, y mala es la "
              "pobreza en boca del impío.",
    (13, 25): "El corazón del hombre muda su semblante, ya sea para bien, ya "
              "sea para mal.",
    (13, 26): "Señal de un corazón que está en el bien es un rostro alegre; y "
              "hallar parábolas es trabajo de pensamientos fatigosos.",

    # Capítulo 14
    (14, 1): "Dichoso el hombre que no ha resbalado con su boca, y no ha sido "
             "punzado por la tristeza del pecado.",
    (14, 2): "Dichoso aquel a quien su alma no condena, y que no ha caído de "
             "su esperanza.",
    (14, 3): "Al hombre mezquino no le sienta bien la riqueza, y al hombre "
             "envidioso, ¿de qué le sirven los bienes?",
    (14, 4): "El que junta privándose a sí mismo, junta para otros, y con sus "
             "bienes se regalarán otros.",
    (14, 5): "El que es malo consigo mismo, ¿para quién será bueno? No se "
             "alegrará con sus bienes.",
    (14, 6): "No hay nadie peor que el que es envidioso consigo mismo, y ésta "
             "es la paga de su maldad.",
    (14, 7): "Y si hace el bien, lo hace por descuido, y al fin deja ver su "
             "maldad.",
    (14, 8): "Malo es el que tiene ojo envidioso, que aparta el rostro y "
             "desprecia a las almas.",
    (14, 9): "El ojo del codicioso no se sacia con su parte, y la injusticia "
             "maligna reseca el alma.",
    (14, 10): "El ojo malo es envidioso del pan, y en su propia mesa anda "
              "escaso.",
    (14, 11): "Hijo, según lo que tengas, haz el bien a ti mismo, y presenta "
              "dignamente ofrendas al Señor.",
    (14, 12): "Acuérdate de que la muerte no tardará, y de que el decreto del "
              "Hades no te ha sido mostrado.",
    (14, 13): "Antes que mueras, haz el bien a tu amigo, y según tus fuerzas "
              "extiende la mano y dale.",
    (14, 14): "No te prives de un día bueno, y no se te pase la parte de un "
              "buen deseo.",
    (14, 15): "¿No dejarás a otro el fruto de tus penas, y tus trabajos para "
              "ser repartidos por suerte?",
    (14, 16): "Da y recibe, y recrea tu alma, ⁽¹⁷⁾ porque en el Hades no hay "
              "que buscar deleite.",
    (14, 17): "Toda carne envejece como un vestido; ⁽¹²⁾ porque el decreto "
              "desde la eternidad es: «Morirás de muerte».",
    (14, 18): "Como las hojas que brotan en un árbol frondoso, ⁽¹⁹⁾ que unas "
              "caen y otras nacen, así es la generación de la carne y de la "
              "sangre: una muere y otra nace.",
    (14, 19): "Toda obra corruptible se acaba, y el que la hace se irá con "
              "ella.",
    (14, 20): "Dichoso el hombre que medita en la sabiduría, y que discurre "
              "con su inteligencia;",
    (14, 21): "el que considera en su corazón los caminos de ella, y "
              "entenderá sus secretos.",
    (14, 22): "Sal tras ella como quien sigue el rastro, y acecha en sus "
              "entradas.",
    (14, 23): "El que se asoma por sus ventanas, y escucha a sus puertas;",
    (14, 24): "el que se hospeda cerca de su casa, y clava una estaca en sus "
              "paredes;",
    (14, 25): "plantará su tienda junto a ella, y se hospedará en una morada "
              "de bienes;",
    (14, 26): "pondrá a sus hijos bajo su amparo, y morará bajo sus ramas;",
    (14, 27): "por ella será cubierto contra el calor, y se hospedará en su "
              "gloria.",

    # Capítulo 15
    (15, 1): "El que teme al Señor hará esto, y el que es dueño de la ley la "
             "alcanzará.",
    (15, 2): "Y le saldrá al encuentro como una madre, y como la esposa de su "
             "juventud lo recibirá.",
    (15, 3): "Le dará a comer el pan del entendimiento, y le dará a beber el "
             "agua de la sabiduría.",
    (15, 4): "Se apoyará en ella y no se doblegará, ⁽⁴⁾ y se asirá de ella y "
             "no será avergonzado.",
    (15, 5): "Y lo ensalzará sobre sus prójimos, ⁽⁵⁾ y en medio de la "
             "asamblea le abrirá la boca.",
    (15, 6): "Heredará alegría y corona de júbilo y un nombre eterno.",
    (15, 7): "No la alcanzarán los hombres insensatos, y los hombres "
             "pecadores no la verán.",
    (15, 8): "Lejos está de la soberbia, ⁽⁸⁾ y los hombres mentirosos no se "
             "acordarán de ella.",
    (15, 9): "No es hermosa la alabanza en la boca del pecador, ⁽¹⁰⁾ porque "
             "no le fue enviada por el Señor.",
    (15, 10): "Porque la alabanza se dirá con sabiduría, y el Señor la hará "
              "prosperar.",
    (15, 11): "No digas: «Por causa del Señor me aparté»; porque lo que él "
              "aborrece, no lo harás.",
    (15, 12): "No digas: «Él me hizo errar»; porque no tiene necesidad del "
              "hombre pecador.",
    (15, 13): "Toda abominación la aborrece el Señor, y no es amable para los "
              "que le temen.",
    (15, 14): "Él mismo hizo al hombre al principio, y lo dejó en manos de su "
              "propio albedrío.",
    (15, 15): "Si quieres, guardarás los mandamientos, y hacer lo que le "
              "agrada es cosa de fidelidad.",
    (15, 16): "Ha puesto delante de ti el fuego y el agua: a lo que quieras "
              "extenderás tu mano.",
    (15, 17): "Delante de los hombres están la vida y la muerte, y lo que "
              "cada uno prefiera, eso se le dará.",
    (15, 18): "Porque grande es la sabiduría del Señor; fuerte es en poder, y "
              "lo ve todo;",
    (15, 19): "y sus ojos están sobre los que le temen, y él conoce toda obra "
              "del hombre.",
    (15, 20): "A nadie mandó ser impío, y a nadie dio licencia para pecar.",

    # Capítulo 16
    (16, 1): "No desees multitud de hijos inútiles, ⁽¹⁾ ni te alegres de "
             "hijos impíos.",
    (16, 2): "Si se multiplican, no te alegres por ellos, si no está con "
             "ellos el temor del Señor.",
    (16, 3): "No te fíes de su vida, ni cuentes con su suerte; ⁽³⁾ porque "
             "mejor es uno que mil, ⁽⁴⁾ y morir sin hijos que tener hijos "
             "impíos.",
    (16, 4): "Porque por un solo hombre entendido se poblará una ciudad, pero "
             "la tribu de los inicuos quedará desierta.",
    (16, 5): "Muchas cosas como éstas he visto con mis ojos, y otras más "
             "fuertes que éstas ha oído mi oído.",
    (16, 6): "En la reunión de los pecadores se encenderá fuego, y en la "
             "nación rebelde se inflamó la ira.",
    (16, 7): "No se aplacó en favor de los antiguos gigantes, que se "
             "rebelaron confiados en su fuerza.",
    (16, 8): "No perdonó a los vecinos de Lot, a quienes abominó por su "
             "soberbia.",
    (16, 9): "No tuvo compasión de la nación de perdición, de los que se "
             "ensoberbecían en sus pecados;",
    (16, 10): "y así también a los seiscientos mil hombres de a pie que se "
              "juntaron en la dureza de su corazón.",
    (16, 11): "Y aunque fuera uno solo el de dura cerviz, sería de maravillar "
              "que quedase sin castigo; ⁽¹²⁾ porque misericordia e ira están "
              "en él: poderoso para perdonar y para derramar la ira.",
    (16, 12): "Cuanto es grande su misericordia, tan grande es también su "
              "reprensión; al hombre lo juzgará según sus obras.",
    (16, 13): "No escapará el pecador con sus rapiñas, y no quedará frustrada "
              "la paciencia del piadoso.",
    (16, 14): "A toda limosna le hará lugar; cada uno hallará según sus "
              "obras.",
    (16, 17): "No digas: «Me esconderé del Señor; ¿acaso alguien se acordará "
              "de mí allá en lo alto? ⁽¹⁷⁾ Entre un pueblo tan numeroso no "
              "seré recordado; porque ¿qué es mi alma en una creación sin "
              "medida?»",
    (16, 18): "He aquí el cielo, y el cielo de los cielos de Dios, el abismo "
              "y la tierra se estremecerán cuando él los visite;",
    (16, 19): "a una los montes y los cimientos de la tierra tiemblan de "
              "espanto cuando él los mira.",
    (16, 20): "Y en estas cosas no pensará el corazón; ⁽²¹⁾ y sus caminos, "
              "¿quién los considerará?",
    (16, 21): "Y hay una tempestad que el hombre no verá; ⁽²²⁾ y la mayor "
              "parte de sus obras están en lo oculto.",
    (16, 22): "Las obras de la justicia, ¿quién las anunciará? ¿O quién las "
              "aguardará? Porque lejos está el pacto.",
    (16, 23): "El que es falto de corazón piensa estas cosas, y el hombre "
              "insensato y extraviado piensa necedades.",
    (16, 24): "Escúchame, hijo, y aprende la ciencia, y pon tu corazón en mis "
              "palabras.",
    (16, 25): "Muestro la instrucción con medida, y anuncio la ciencia con "
              "exactitud.",
    (16, 26): "Por el juicio del Señor fueron sus obras desde el principio, y "
              "desde que las hizo les señaló sus partes.",
    (16, 27): "Ordenó para siempre sus obras, y sus principios por sus "
              "generaciones; no tuvieron hambre ni se fatigaron, y no "
              "desistieron de sus obras.",
    (16, 28): "Ninguna oprimió a su vecina, y jamás ⁽²⁹⁾ desobedecerán su "
              "palabra.",
    (16, 29): "Y después de esto el Señor miró a la tierra, y la llenó de sus "
              "bienes.",
    (16, 30): "Con toda clase de seres vivientes cubrió su faz, y a ella "
              "vuelven.",

    # Capítulo 17
    (17, 1): "El Señor creó al hombre de la tierra, y de nuevo lo hizo volver "
             "a ella.",
    (17, 2): "Días contados y un tiempo fijo les dio, y les dio potestad "
             "sobre las cosas que hay en ella.",
    (17, 3): "Conforme a sí mismo los revistió de fuerza, ⁽¹ᵇ⁾ y a su imagen "
             "los hizo;",
    (17, 4): "y puso el temor de él sobre toda carne, para que dominara sobre "
             "las fieras y las aves.",
    (17, 6): "Consejo y lengua y ojos, oídos y corazón les dio para pensar;",
    (17, 7): "de ciencia de entendimiento los llenó, y el bien y el mal les "
             "mostró;",
    (17, 8): "puso su ojo sobre sus corazones, para mostrarles la grandeza de "
             "sus obras;",
    (17, 9): "para que cuenten las grandezas de sus obras.",
    (17, 10): "Y alabarán el nombre de su santidad,",
    (17, 11): "Les añadió la ciencia, y la ley de vida les dio en herencia;",
    (17, 12): "¹² una alianza eterna estableció con ellos, y sus juicios les "
              "mostró;",
    (17, 13): "la grandeza de su gloria vieron sus ojos, y la gloria de su "
              "voz oyó su oído;",
    (17, 14): "y les dijo: Guardaos de toda injusticia; ⁽¹²⁾ y les dio "
              "mandamiento a cada uno acerca de su prójimo.",
    (17, 15): "Sus caminos están delante de él en todo tiempo, no se "
              "ocultarán a sus ojos.",
    (17, 17): "A cada nación le puso un gobernante, ⁽¹⁵⁾ pero la porción del "
              "Señor es Israel.",
    (17, 19): "Todas sus obras están como el sol delante de él, y sus ojos "
              "están de continuo sobre sus caminos;",
    (17, 20): "no se le ocultaron sus injusticias, y todos sus pecados están "
              "delante del Señor.",
    (17, 22): "La limosna del hombre es como un sello junto a él, y la bondad "
              "del hombre la guardará como la niña de sus ojos.",
    (17, 23): "Después se levantará y les dará su paga, y hará caer su "
              "recompensa sobre su cabeza;",
    (17, 24): "pero a los que se arrepienten les concedió el regreso, y "
              "consoló a los que desfallecían en la paciencia.",
    (17, 25): "Vuélvete al Señor y deja los pecados, ⁽²²⁾ suplica delante de "
              "su rostro y disminuye el tropiezo;",
    (17, 26): "vuelve al Altísimo y apártate de la injusticia, y aborrece en "
              "gran manera la abominación.",
    (17, 27): "Al Altísimo, ¿quién lo alabará en el Hades, ⁽²⁵⁾ en lugar de "
              "los vivos y de los que le tributan alabanza?",
    (17, 28): "Del muerto, como del que no existe, perece la alabanza; ⁽²⁷⁾ "
              "el que vive y está sano alabará al Señor.",
    (17, 29): "¡Cuán grande es la misericordia del Señor, y su perdón para "
              "los que se vuelven a él!",
    (17, 30): "Porque no puede haberlo todo en los hombres, pues no es "
              "inmortal el hijo del hombre.",
    (17, 31): "¿Qué cosa más luminosa que el sol? Y aun éste se eclipsa; y el "
              "malo pondrá su pensamiento en la carne y la sangre.",
    (17, 32): "Él pasa revista al ejército de lo alto del cielo, y los "
              "hombres todos son tierra y ceniza.",

    # Capítulo 18
    (18, 1): "El que vive para siempre creó todas las cosas juntamente;",
    (18, 2): "sólo el Señor será reconocido justo.",
    (18, 4): "A nadie ha concedido anunciar sus obras; y ⁽³⁾ ¿quién rastreará "
             "sus grandezas?",
    (18, 5): "La fuerza de su majestad, ¿quién la medirá? ¿Y quién podrá "
             "además contar sus misericordias?",
    (18, 6): "No es posible quitar ni añadir, ni es posible rastrear las "
             "maravillas del Señor;",
    (18, 7): "cuando el hombre ha acabado, entonces comienza; y cuando se "
             "detiene, entonces queda perplejo.",
    (18, 8): "¿Qué es el hombre, y de qué sirve? ¿Cuál es su bien, y cuál es "
             "su mal?",
    (18, 9): "El número de los días del hombre, mucho es si llega a cien "
             "años;",
    (18, 10): "como una gota de agua del mar y un grano de arena, así son sus "
              "pocos años en el día de la eternidad.",
    (18, 11): "Por eso el Señor tuvo paciencia con ellos, y derramó sobre "
              "ellos su misericordia;",
    (18, 12): "vio y conoció que su fin es malo; ⁽¹¹⁾ por eso multiplicó su "
              "perdón.",
    (18, 13): "La misericordia del hombre es para su prójimo, pero la "
              "misericordia del Señor es para toda carne; ⁽¹³⁾ reprende y "
              "corrige y enseña, y hace volver, como el pastor a su rebaño.",
    (18, 14): "Tiene misericordia de los que reciben la corrección, y de los "
              "que se apresuran a cumplir sus juicios.",
    (18, 15): "Hijo, en tus beneficios no pongas tacha, ni en ninguna dádiva "
              "la tristeza de las palabras.",
    (18, 16): "¿No calma el rocío el viento abrasador? Así es mejor la "
              "palabra que la dádiva.",
    (18, 17): "¿No es acaso la palabra mejor que un buen regalo? Y ambas "
              "cosas se hallan en el hombre lleno de gracia.",
    (18, 18): "El necio reprocha sin gracia, y la dádiva del envidioso "
              "consume los ojos.",
    (18, 19): "Antes de hablar, aprende; y antes de la enfermedad, cuídate;",
    (18, 20): "antes del juicio, examínate a ti mismo, y en la hora de la "
              "visitación hallarás perdón;",
    (18, 21): "antes de caer enfermo, humíllate, y en el tiempo de los "
              "pecados muestra conversión.",
    (18, 22): "Que nada te impida cumplir tu voto a su tiempo, y no aguardes "
              "hasta la muerte para justificarte;",
    (18, 23): "antes de hacer voto, prepárate a ti mismo, y no seas como el "
              "hombre que tienta al Señor.",
    (18, 24): "Acuérdate de la ira en los días del fin, y del tiempo de la "
              "venganza, cuando él aparte su rostro.",
    (18, 25): "Acuérdate del tiempo del hambre en el tiempo de la hartura, de "
              "la pobreza y la necesidad en los días de la riqueza.",
    (18, 26): "De la mañana a la tarde cambia el tiempo, y todo es pasajero "
              "delante del Señor.",
    (18, 27): "El hombre sabio en todo será cauto, y en los días de los "
              "pecados se guardará de la falta.",
    (18, 28): "Todo hombre entendido conoce la sabiduría, y al que la halló "
              "le tributará alabanza.",
    (18, 29): "Los entendidos en palabras también ellos se hicieron sabios, y "
              "derramaron como lluvia proverbios certeros. Dominio del alma.",
    (18, 30): "No vayas en pos de tus deseos, y refrénate de tus apetitos;",
    (18, 31): "si concedes a tu alma el gusto del deseo, te hará la burla de "
              "tus enemigos.",
    (18, 32): "No te regocijes en mucha molicie, ni te ates a los gastos de "
              "sus banquetes;",
    (18, 33): "no te hagas pobre dando banquetes con dinero prestado, cuando "
              "nada tienes en la bolsa.",

    # Capítulo 19
    (19, 1): "El obrero borracho no se enriquecerá; el que desprecia lo poco, "
             "poco a poco caerá.",
    (19, 2): "El vino y las mujeres descarrían a los entendidos, y el que se "
             "junta con rameras se hará más temerario;",
    (19, 3): "la podredumbre y los gusanos lo heredarán, y el alma temeraria "
             "será arrancada.",
    (19, 4): "El que pronto se fía es ligero de corazón, y el que peca contra "
             "su propia alma comete falta.",
    (19, 5): "El que se regocija en su corazón será condenado,",
    (19, 6): "y el que aborrece la charlatanería disminuye la maldad.",
    (19, 7): "Nunca repitas lo que se dice, y en nada saldrás menoscabado.",
    (19, 8): "Ni con amigo ni con enemigo lo cuentes, y si no te es pecado, "
             "no lo descubras;",
    (19, 9): "porque te ha oído y se guardará de ti, y a su tiempo te "
             "aborrecerá.",
    (19, 10): "¿Has oído una palabra? Muera contigo; ten ánimo, que no te "
              "hará reventar.",
    (19, 11): "Por una palabra sufre dolores el necio, como por la criatura "
              "la que da a luz.",
    (19, 12): "Como flecha clavada en el muslo de la carne, así es la palabra "
              "en el vientre del necio.",
    (19, 13): "Reprende al amigo: quizá no lo hizo; y si algo hizo, para que "
              "no lo vuelva a hacer.",
    (19, 14): "Reprende al amigo: quizá no lo dijo; y si lo ha dicho, para "
              "que no lo repita.",
    (19, 15): "Reprende al amigo, porque muchas veces hay calumnia, ⁽¹⁶⁾ y no "
              "creas toda palabra.",
    (19, 16): "Hay quien resbala, pero no de corazón; ⁽¹⁷⁾ ¿y quién no ha "
              "pecado con su lengua?",
    (19, 17): "Reprende a tu prójimo antes de amenazarlo, ⁽¹⁸⁾ y da lugar a "
              "la ley del Altísimo.",
    (19, 20): "Toda sabiduría es temor del Señor, y en toda sabiduría está el "
              "cumplimiento de la ley.",
    (19, 22): "Y no es sabiduría el conocimiento de la maldad, ni hay "
              "prudencia donde está el consejo de los pecadores.",
    (19, 23): "Hay una maldad, y ésta es abominación; y hay un insensato que "
              "es falto de sabiduría.",
    (19, 24): "Más vale el pobre de entendimiento que teme a Dios que el que "
              "abunda en prudencia y traspasa la ley.",
    (19, 25): "Hay una astucia sutil, y ésta es injusta; y hay quien tuerce "
              "el favor para hacer prevalecer su juicio.",
    (19, 26): "Hay quien obra el mal encorvado de luto, y por dentro está "
              "lleno de engaño;",
    (19, 27): "baja el rostro y se hace el sordo; donde no lo conocen, se te "
              "adelantará;",
    (19, 28): "y si por falta de fuerzas se le impide pecar, cuando halle "
              "ocasión hará el mal.",
    (19, 29): "Por la vista se conoce al hombre, y por el semblante del "
              "rostro se conoce al sensato;",
    (19, 30): "el vestido del hombre y la risa de sus dientes y el andar del "
              "hombre anuncian lo que hay en él.",

    # Capítulo 20
    (20, 1): "Hay reprensión que no es oportuna, y hay quien calla, y él es "
             "el prudente.",
    (20, 2): "¡Cuánto mejor es reprender que enojarse! Y el que reconoce su "
             "falta será preservado del menoscabo.",
    (20, 4): "Como el deseo del eunuco de desflorar a una doncella, así es el "
             "que hace justicia por la violencia.",
    (20, 5): "Hay quien calla y es tenido por sabio, y hay quien se hace "
             "aborrecible por su mucho hablar.",
    (20, 6): "Hay quien calla porque no tiene respuesta, y hay quien calla "
             "porque conoce el momento.",
    (20, 7): "El hombre sabio callará hasta el momento oportuno, pero el "
             "jactancioso y el insensato dejarán pasar el momento.",
    (20, 8): "El que se excede en palabras será abominado, y el que se arroga "
             "autoridad será aborrecido.",
    (20, 9): "Hay buen suceso en los males para el hombre, y hay ganancia que "
             "es para pérdida.",
    (20, 10): "Hay dádiva que no te aprovechará, y hay dádiva cuya recompensa "
              "es doble.",
    (20, 11): "Hay humillación a causa de la gloria, y hay quien desde la "
              "humillación levantó la cabeza.",
    (20, 12): "Hay quien compra mucho por poco, y lo paga siete veces.",
    (20, 13): "El sabio con sus palabras se hará amable, pero las gracias de "
              "los necios serán derramadas en vano.",
    (20, 14): "La dádiva del insensato no te aprovechará, porque sus ojos, en "
              "lugar de uno, son muchos.",
    (20, 15): "Poco dará y mucho reprochará, y abrirá su boca como un "
              "pregonero; ⁽¹⁶⁾ hoy presta y mañana lo reclama: aborrecible es "
              "el hombre así.",
    (20, 16): "El necio dirá: No tengo amigo, y no hay gratitud por mis "
              "beneficios; ⁽¹⁸⁾ los que comen mi pan son de mala lengua.",
    (20, 17): "¡Cuántas veces y cuántos se burlarán de él!",
    (20, 18): "Mejor es resbalar en el suelo que resbalar con la lengua; así "
              "la caída de los malos vendrá con presteza.",
    (20, 19): "Hombre sin gracia, cuento fuera de tiempo: en boca de los "
              "ignorantes andará de continuo.",
    (20, 20): "De boca del necio será desechado el proverbio, porque no lo "
              "dirá a su debido tiempo.",
    (20, 21): "Hay a quien la pobreza impide pecar, y en su descanso no "
              "sentirá remordimiento.",
    (20, 22): "Hay quien pierde su alma por vergüenza, y por el rostro del "
              "insensato la perderá.",
    (20, 23): "Hay quien por vergüenza hace promesas a su amigo, y se lo gana "
              "de balde por enemigo.",
    (20, 24): "Mancha fea en el hombre es la mentira; en boca de los "
              "ignorantes andará de continuo.",
    (20, 25): "Preferible es el ladrón al que persiste en la mentira, pero "
              "ambos heredarán la perdición.",
    (20, 26): "La costumbre del hombre mentiroso es deshonra, y su vergüenza "
              "está con él de continuo. Palabras de proverbios.",
    (20, 27): "El sabio con sus palabras se abrirá camino, y el hombre "
              "prudente agradará a los grandes;",
    (20, 28): "el que labra la tierra levantará alto su montón de mieses, y "
              "el que agrada a los grandes alcanzará perdón de la injusticia.",
    (20, 29): "Presentes y regalos ciegan los ojos de los sabios, y como "
              "bozal en la boca apartan las reprensiones.",
    (20, 30): "Sabiduría escondida y tesoro invisible, ¿qué provecho hay en "
              "ambos?",
    (20, 31): "Mejor es el hombre que esconde su necedad que el hombre que "
              "esconde su sabiduría.",

    # Capítulo 21
    (21, 1): "Hijo, ¿has pecado? No vuelvas a hacerlo, y por tus pecados "
             "pasados suplica.",
    (21, 2): "Como de delante de la serpiente, huye del pecado; porque si te "
             "acercas, te morderá; ⁽³⁾ dientes de león son sus dientes, que "
             "quitan la vida a las almas de los hombres.",
    (21, 3): "Como espada de dos filos es toda iniquidad; para su herida no "
             "hay curación.",
    (21, 4): "El espanto y la insolencia asolarán la riqueza; así la casa del "
             "soberbio será asolada.",
    (21, 5): "La súplica del pobre va de su boca a los oídos de él, y el "
             "juicio a su favor viene con presteza.",
    (21, 6): "El que aborrece la reprensión anda en la huella del pecador, "
             "pero el que teme al Señor se convertirá de corazón.",
    (21, 7): "De lejos es conocido el poderoso de lengua, pero el sensato "
             "sabe cuándo aquél resbala.",
    (21, 8): "El que edifica su casa con dinero ajeno es como el que junta "
             "sus piedras para el invierno.",
    (21, 9): "Estopa amontonada es la reunión de los inicuos, y su fin es "
             "llama de fuego.",
    (21, 10): "El camino de los pecadores está allanado y sin piedras, pero a "
              "su término está la fosa del Hades.",
    (21, 11): "El que guarda la ley domina su pensamiento, ⁽¹³⁾ y la "
              "perfección del temor del Señor es la sabiduría.",
    (21, 12): "No será instruido el que no es hábil; ⁽¹⁵⁾ pero hay una "
              "habilidad que multiplica la amargura.",
    (21, 13): "El conocimiento del sabio crecerá como una inundación, y su "
              "consejo como fuente de vida.",
    (21, 14): "Las entrañas del necio son como vasija quebrada, y no retendrá "
              "conocimiento alguno.",
    (21, 15): "Si el entendido oye una palabra sabia, la alabará y le "
              "añadirá; la oyó el disoluto y le desagradó, y la echó a sus "
              "espaldas.",
    (21, 16): "La explicación del necio es como carga en el camino, pero en "
              "los labios del entendido se hallará gracia.",
    (21, 17): "La boca del prudente será buscada en la asamblea, y sus "
              "palabras serán meditadas en el corazón.",
    (21, 18): "Como casa arruinada, así es la sabiduría para el necio, y el "
              "conocimiento del insensato son palabras sin examen.",
    (21, 19): "Grillos en los pies es la instrucción para los insensatos, y "
              "como esposas en la mano derecha.",
    (21, 20): "El necio, al reír, levanta su voz, pero el hombre sagaz apenas "
              "sonreirá en silencio.",
    (21, 21): "Como adorno de oro es la instrucción para el prudente, y como "
              "brazalete en el brazo derecho.",
    (21, 22): "El pie del necio se apresura a entrar en la casa, pero el "
              "hombre de mucha experiencia se avergonzará ante la presencia "
              "de los de dentro.",
    (21, 23): "El insensato se asoma desde la puerta al interior de la casa, "
              "pero el hombre bien instruido se quedará fuera.",
    (21, 24): "Falta de educación es en el hombre escuchar junto a la puerta, "
              "y el prudente lo tendrá por pesada deshonra.",
    (21, 25): "Los labios de los extraños se harán pesados en estas cosas, "
              "pero las palabras de los prudentes se pesarán en balanza.",
    (21, 26): "En la boca de los necios está su corazón, pero el corazón de "
              "los sabios es su boca.",
    (21, 27): "Cuando el impío maldice a Satanás, maldice su propia alma.",
    (21, 28): "El murmurador mancha su propia alma, y en su vecindad será "
              "aborrecido.",

    # Capítulo 22
    (22, 1): "A una piedra embarrada es comparado el perezoso, y todos "
             "silbarán ante su deshonra.",
    (22, 2): "Al estiércol de los muladares es comparado el perezoso; todo el "
             "que lo levanta se sacudirá la mano.",
    (22, 3): "Vergüenza del padre es haber engendrado un hijo mal educado, y "
             "la hija nace para su menoscabo.",
    (22, 4): "La hija prudente heredará un marido, pero la que causa "
             "vergüenza es tristeza para el que la engendró;",
    (22, 5): "la desvergonzada avergüenza al padre y al marido, y por ambos "
             "será despreciada.",
    (22, 6): "Música en el duelo es discurso fuera de tiempo; pero los azotes "
             "y la corrección son sabiduría en todo tiempo.",
    (22, 7): "El que enseña al necio es como quien pega los pedazos de un "
             "tiesto, ⁽⁸⁾ como quien despierta al que duerme de un sueño "
             "profundo;",
    (22, 8): "habla con uno que dormita el que habla con el necio; y al final "
             "dirá: ¿Qué es?",
    (22, 11): "Llora por el muerto, porque le faltó la luz; y llora por el "
              "necio, porque le faltó el entendimiento; ⁽¹¹⁾ llora más "
              "suavemente por el muerto, porque halló descanso, ⁽¹²⁾ pero la "
              "vida del necio es peor que la muerte.",
    (22, 12): "¹² El duelo por el muerto dura siete días, pero el del necio y "
              "del impío, todos los días de su vida.",
    (22, 13): "Con el insensato no multipliques palabras, y no vayas a casa "
              "del que no tiene entendimiento; ⁽¹⁵⁾ guárdate de él, para que "
              "no tengas molestia y no te manches cuando él se sacuda; ⁽¹⁶⁾ "
              "apártate de él y hallarás descanso, y no te hastiarás con su "
              "locura.",
    (22, 14): "¿Qué cosa es más pesada que el plomo? ¿Y qué nombre tiene sino "
              "necio?",
    (22, 15): "Arena y sal y una masa de hierro son más fáciles de llevar que "
              "un hombre sin entendimiento.",
    (22, 16): "El maderamen trabado y atado en un edificio no se deshará con "
              "el terremoto; así el corazón afirmado en un pensamiento de "
              "consejo ⁽²⁰⁾ no temerá en su tiempo.",
    (22, 17): "El corazón asentado sobre un pensamiento de inteligencia es "
              "como el revoque de arena en una pared pulida.",
    (22, 18): "Las estacas puestas en lo alto no resistirán frente al viento; "
              "⁽²³⁾ así el corazón cobarde, con el pensamiento del necio, no "
              "resistirá frente a ningún temor.",
    (22, 19): "El que hiere el ojo hace brotar lágrimas, y el que hiere el "
              "corazón hace aparecer el sentimiento.",
    (22, 20): "El que arroja una piedra a los pájaros los espanta, y el que "
              "afrenta al amigo deshace la amistad.",
    (22, 21): "Aunque contra el amigo hayas sacado la espada, no desesperes, "
              "porque hay regreso.",
    (22, 22): "Si contra el amigo ⁽²⁷⁾ has abierto la boca, no temas, porque "
              "hay reconciliación; salvo el ultraje y la soberbia y la "
              "revelación del secreto y el golpe traicionero: en estos casos "
              "huirá todo amigo.",
    (22, 23): "Gánate la confianza del prójimo en su pobreza, para que en sus "
              "bienes te sacies juntamente con él; ⁽²⁹⁾ en el tiempo de la "
              "tribulación permanece con él, para que en su herencia seas "
              "coheredero.",
    (22, 24): "Antes del fuego, el vapor del horno y el humo; así, antes de "
              "la sangre, los insultos.",
    (22, 25): "No me avergonzaré de proteger al amigo, y no me esconderé de "
              "su presencia;",
    (22, 26): "y si por causa de él me sobreviene mal, ⁽³²⁾ todo el que lo "
              "oiga se guardará de él.",
    (22, 27): "¿Quién pondrá guarda sobre mi boca, y sobre mis labios un "
              "sello astuto, para que no caiga por causa de ella, y mi lengua "
              "no me pierda?",

    # Capítulo 23
    (23, 1): "Señor, Padre y Soberano de mi vida, no me abandones al consejo "
             "de ellos, no me dejes caer por ellos.",
    (23, 2): "¿Quién pondrá azotes sobre mi pensamiento, y sobre mi corazón "
             "la corrección de la sabiduría, para que no perdonen mis "
             "ignorancias, ni se pasen por alto sus pecados?",
    (23, 3): "Para que no se multipliquen mis ignorancias, ni abunden mis "
             "pecados, y caiga yo delante de mis adversarios, y se alegre de "
             "mí mi enemigo.",
    (23, 4): "Señor, Padre y Dios de mi vida, ⁽⁵⁾ no me des la altivez de los "
             "ojos,",
    (23, 5): "y aparta de mí el deseo;",
    (23, 6): "que el apetito del vientre y la unión carnal no se apoderen de "
             "mí, y no me entregues a un alma desvergonzada. Instrucción de "
             "la boca.",
    (23, 7): "Oíd, hijos, la instrucción de la boca; el que la guarda no será "
             "atrapado;",
    (23, 8): "por sus labios ⁸ será atrapado el pecador, y el maldiciente y "
             "el soberbio tropezarán en ellos.",
    (23, 9): "No acostumbres tu boca al juramento, ⁽¹⁰⁾ ni te habitúes a "
             "nombrar al Santo.",
    (23, 10): "Porque así como el esclavo que es interrogado continuamente no "
              "se verá libre de cardenales, así también el que jura y "
              "pronuncia el Nombre a todas horas no quedará limpio de pecado.",
    (23, 11): "El hombre que mucho jura se llenará de iniquidad, y no se "
              "apartará el azote de su casa; ⁽¹³⁾ si falta, su pecado está "
              "sobre él, y si lo desatiende, ha pecado doblemente; ⁽¹⁴⁾ y si "
              "juró en vano, no será justificado, porque su casa se llenará "
              "de calamidades.",
    (23, 12): "Hay un hablar que está revestido de muerte: ¡que no se halle "
              "en la heredad de Jacob! ⁽¹⁶⁾ Porque de los piadosos se "
              "apartarán todas estas cosas, y no se revolcarán en los "
              "pecados.",
    (23, 13): "No acostumbres tu boca a la grosería indecente, porque hay en "
              "ella palabra de pecado.",
    (23, 14): "Acuérdate de tu padre y de tu madre, cuando te sientes en "
              "medio de los grandes; ⁽¹⁹⁾ no sea que te olvides delante de "
              "ellos, y por tu costumbre te vuelvas necio, y desees no haber "
              "nacido, y maldigas el día de tu nacimiento.",
    (23, 15): "El hombre que se acostumbra a palabras de oprobio no se "
              "corregirá en todos los días de su vida.",
    (23, 16): "Dos clases de hombres multiplican los pecados, y la tercera "
              "atrae la ira: ⁽²²⁾ el alma ardiente como fuego encendido, que "
              "no se apagará hasta ser consumida; ⁽²³⁾ el hombre fornicario "
              "en el cuerpo de su carne, que no cesará hasta que el fuego lo "
              "abrase;",
    (23, 17): "al hombre fornicario todo pan le es dulce; no se cansará hasta "
              "que muera.",
    (23, 18): "El hombre que es infiel a su lecho dice en su alma: ¿Quién me "
              "ve? ⁽²⁶⁾ Tinieblas hay a mi alrededor, y las paredes me "
              "cubren, y nadie me ve; ¿qué he de temer? De mis pecados no se "
              "acordará el Altísimo.",
    (23, 19): "Y los ojos de los hombres son su temor, ⁽²⁸⁾ y no sabe que los "
              "ojos del Señor son diez mil veces más luminosos que el sol, "
              "que miran todos los caminos de los hombres y penetran en los "
              "lugares escondidos.",
    (23, 20): "Antes que fueran creadas todas las cosas, le eran conocidas, y "
              "así también después de acabadas.",
    (23, 21): "Éste será castigado en las plazas de la ciudad, y donde no lo "
              "sospechaba será apresado.",
    (23, 22): "Así también la mujer que abandona a su marido y le presenta un "
              "heredero habido de otro;",
    (23, 23): "porque, primeramente, desobedeció la ley del Altísimo; y en "
              "segundo lugar, faltó contra su marido; y en tercer lugar, "
              "cometió adulterio con fornicación y presentó hijos de un "
              "hombre extraño.",
    (23, 24): "Ésta será llevada ante la asamblea, y sobre sus hijos vendrá "
              "la visitación;",
    (23, 25): "sus hijos no echarán raíces, y sus ramas no darán fruto;",
    (23, 26): "dejará su memoria para maldición, y su oprobio no será "
              "borrado;",
    (23, 27): "y conocerán los que queden que nada hay mejor que el temor del "
              "Señor, y nada más dulce que atender a los mandamientos del "
              "Señor. Alabanza de la sabiduría.",

    # Capítulo 24
    (24, 1): "La sabiduría alabará su propia alma, y en medio de su pueblo se "
             "gloriará.",
    (24, 2): "En la asamblea del Altísimo abrirá su boca, y delante de su "
             "poder se gloriará:",
    (24, 3): "Yo salí de la boca del Altísimo, ⁽⁶⁾ y como niebla cubrí la "
             "tierra;",
    (24, 4): "yo planté mi tienda en las alturas, y mi trono estaba en una "
             "columna de nube;",
    (24, 5): "el círculo del cielo lo recorrí yo sola, y por la profundidad "
             "de los abismos me paseé;",
    (24, 6): "en las olas del mar ⁽⁹⁾ y en toda la tierra, ⁽¹⁰⁾ y en todo "
             "pueblo y nación tomé posesión.",
    (24, 7): "Con todos éstos busqué reposo, y ¿en la heredad de quién "
             "fijaría mi morada?",
    (24, 8): "Entonces me dio orden el creador de todas las cosas, y el que "
             "me creó hizo reposar mi tienda, ⁽¹³⁾ y dijo: Planta tu tienda "
             "en Jacob, y toma tu herencia en Israel.",
    (24, 9): "Antes de los siglos, desde el principio, me creó, y hasta los "
             "siglos no dejaré de ser.",
    (24, 10): "En la tienda santa ministré delante de él, ⁽¹⁵⁾ y así en Sión "
              "quedé establecida;",
    (24, 11): "en la ciudad amada me hizo reposar igualmente, y en Jerusalén "
              "está mi potestad;",
    (24, 12): "y eché raíces en un pueblo glorificado, en la porción del "
              "Señor, su heredad.",
    (24, 13): "Como cedro fui exaltada en el Líbano, y como ciprés en los "
              "montes del Hermón;",
    (24, 14): "como palmera fui exaltada en las riberas, y como plantíos de "
              "rosas en Jericó; ⁽¹⁹⁾ como olivo hermoso en la llanura, y fui "
              "exaltada como plátano.",
    (24, 15): "Como cinamomo y aspálato aromático di fragancia, y como mirra "
              "escogida esparcí buen olor; como gálbano y ónice y estacte, y "
              "como vapor de incienso en la tienda.",
    (24, 16): "Yo, como terebinto, extendí mis ramas, y mis ramas son ramas "
              "de gloria y de gracia.",
    (24, 17): "Yo, como vid, hice brotar gracia, y mis flores son fruto de "
              "gloria y de riqueza.",
    (24, 19): "Venid a mí los que me deseáis, y saciaos de mis frutos;",
    (24, 20): "porque mi recuerdo es más dulce que la miel, y mi heredad más "
              "que el panal de miel.",
    (24, 21): "Los que me comen tendrán aún hambre, y los que me beben "
              "tendrán aún sed.",
    (24, 22): "El que me obedece no será avergonzado, y los que obran en mí "
              "no pecarán.",
    (24, 23): "Todo esto es el libro de la alianza del Dios Altísimo, la ley "
              "que mandó Moisés, herencia para las congregaciones de Jacob;",
    (24, 25): "la que hace rebosar la sabiduría como el Fisón, y como el "
              "Tigris en los días de los frutos nuevos;",
    (24, 26): "la que colma la inteligencia como el Éufrates, y como el "
              "Jordán en los días de la siega;",
    (24, 27): "la que hace brillar la instrucción como la luz, como el Gihón "
              "en los días de la vendimia.",
    (24, 28): "No acabó el primero de conocerla, y así tampoco el último la "
              "ha rastreado;",
    (24, 29): "porque más que el mar se ha colmado su pensamiento, y su "
              "consejo más que el gran abismo.",
    (24, 30): "Y yo, como canal que sale de un río, y como acequia, salí "
              "hacia el paraíso.",
    (24, 31): "Dije: Regaré mi huerto, y embriagaré de agua mi era; ⁽⁴³⁾ y he "
              "aquí que el canal se me hizo río, y mi río se hizo mar.",
    (24, 32): "Aún haré brillar la instrucción como la aurora, y la haré "
              "resplandecer hasta lejos;",
    (24, 33): "aún derramaré la enseñanza como profecía, y la dejaré a las "
              "generaciones de los siglos.",
    (24, 34): "Ved que no he trabajado sólo para mí, sino para todos los que "
              "la buscan.",

    # Capítulo 25
    (25, 1): "En tres cosas me hermoseé, y me levanté hermosa delante del "
             "Señor y de los hombres: ⁽²⁾ la concordia de los hermanos, y la "
             "amistad de los prójimos, y mujer y marido que se avienen el uno "
             "con el otro.",
    (25, 2): "Pero tres clases de personas aborreció mi alma, y me irrita en "
             "gran manera su vida: el pobre ⁽⁴⁾ soberbio, y el rico "
             "mentiroso, y el viejo adúltero falto de juicio.",
    (25, 3): "Si en la juventud no has recogido, ¿cómo hallarás en tu vejez?",
    (25, 4): "¡Qué hermoso es el juicio en las canas, y en los ancianos saber "
             "dar consejo!",
    (25, 5): "¡Qué hermosa es la sabiduría de los ancianos, y en los hombres "
             "honrados la reflexión y el consejo!",
    (25, 6): "Corona de los ancianos es la mucha experiencia, y su orgullo es "
             "el temor del Señor.",
    (25, 7): "Nueve cosas que he pensado he tenido por dichosas en mi "
             "corazón, y la décima la diré con mi lengua: ⁽¹⁰⁾ el hombre que "
             "se alegra en sus hijos, el que vive y ve la caída de sus "
             "enemigos;",
    (25, 8): "dichoso el que convive con una mujer inteligente, y el que no "
             "resbaló con su lengua, y el que no sirvió a uno indigno de él;",
    (25, 9): "dichoso el que halló prudencia, y el que habla a oídos que "
             "escuchan;",
    (25, 10): "¡cuán grande es el que halló la sabiduría! pero no está por "
              "encima del que teme al Señor.",
    (25, 11): "El temor del Señor lo sobrepasa todo; el que lo posee, ¿a "
              "quién será comparado?",
    (25, 13): "Cualquier herida, pero no la herida del corazón; y cualquier "
              "maldad, pero no la maldad de la mujer;",
    (25, 14): "cualquier calamidad, pero no la calamidad que traen los que "
              "aborrecen; ⁽²¹⁾ y cualquier venganza, pero no la venganza de "
              "los enemigos.",
    (25, 15): "No hay cabeza por encima de la cabeza de la serpiente, y no "
              "hay furor por encima del furor del enemigo.",
    (25, 16): "Preferiré vivir con un león y con un dragón antes que habitar "
              "con una mujer malvada.",
    (25, 17): "La maldad de la mujer altera su semblante, y oscurece su "
              "rostro como un saco.",
    (25, 18): "En medio de sus prójimos ⁽²⁵⁾ se sienta a la mesa su marido, y "
              "al oírlo gime amargamente.",
    (25, 19): "Pequeña es toda malicia comparada con la malicia de la mujer; "
              "la suerte del pecador caiga sobre ella.",
    (25, 20): "Cuesta arenosa para los pies del anciano, así es la mujer "
              "habladora para el marido sosegado.",
    (25, 21): "No te arrojes ante la belleza de una mujer, ni codicies a una "
              "mujer.",
    (25, 22): "Ira e impudencia y gran vergüenza es la mujer si es ella quien "
              "mantiene a su marido.",
    (25, 23): "Corazón abatido y rostro sombrío y herida del corazón es la "
              "mujer malvada; ⁽³²⁾ manos caídas y rodillas paralizadas, la "
              "que no hace dichoso a su marido.",
    (25, 24): "Por la mujer fue el principio del pecado, y por causa de ella "
              "morimos todos.",
    (25, 25): "No des salida al agua, ni a la mujer malvada libertad.",
    (25, 26): "Si no anda conforme a tu mano, ⁽³⁶⁾ córtala de tus carnes.",

    # Capítulo 26
    (26, 1): "Dichoso el marido de una mujer buena, y el número de sus días "
             "será doble.",
    (26, 2): "La mujer valerosa alegra a su marido, y él cumplirá sus años en "
             "paz.",
    (26, 3): "La mujer buena es una buena porción; en la porción de los que "
             "temen al Señor será dada.",
    (26, 4): "Sea rico o pobre, su corazón está contento; en todo tiempo su "
             "rostro está alegre.",
    (26, 5): "De tres cosas ha temido mi corazón, y ante la cuarta he "
             "suplicado: la calumnia ⁽⁹⁾ de la ciudad, y el tumulto de la "
             "muchedumbre, ⁽⁷⁾ y la acusación falsa; todas son peores que la "
             "muerte.",
    (26, 6): "Pero dolor de corazón y llanto es la mujer celosa de otra "
             "mujer, y azote de la lengua que con todos se comunica.",
    (26, 7): "Yugo de bueyes que se sacude es la mujer malvada; el que la "
             "sujeta es como el que agarra un escorpión.",
    (26, 8): "Gran ira es la mujer borracha, y no encubrirá su propia "
             "vergüenza.",
    (26, 9): "La fornicación de la mujer está en la altivez de sus ojos, y en "
             "sus párpados se conocerá.",
    (26, 10): "Sobre la hija desvergonzada refuerza la guardia, no sea que, "
              "hallando soltura, se aproveche de ella.",
    (26, 11): "Guárdate de ir tras un ojo impúdico, y no te maravilles si "
              "peca contra ti.",
    (26, 12): "Como el caminante sediento abre la boca, y de toda agua "
              "cercana bebe, frente a toda estaca se sentará, y ante toda "
              "flecha abrirá la aljaba.",
    (26, 13): "La gracia de la mujer deleita a su marido, y su saber le "
              "engordará los huesos.",
    (26, 14): "Don del Señor es la mujer callada, ⁽⁸⁾ y no hay precio para un "
              "alma bien instruida.",
    (26, 15): "Gracia sobre gracia es la mujer pudorosa, y no hay peso que "
              "valga lo que un alma continente.",
    (26, 16): "Como el sol que sale en las alturas del Señor, así la belleza "
              "de la mujer buena en el adorno de su casa;",
    (26, 17): "como lámpara que resplandece sobre el candelero santo, así la "
              "belleza del rostro sobre una estatura firme;",
    (26, 18): "como columnas de oro sobre basa de plata, así los pies "
              "hermosos sobre el pecho de la mujer firme.",
    (26, 28): "Por dos cosas se entristece mi corazón, y por la tercera me "
              "sobrevino la ira: ⁽²⁶⁾ el guerrero que desfallece por la "
              "pobreza, y los hombres inteligentes si son tenidos por basura; "
              "⁽²⁷⁾ el que se vuelve de la justicia al pecado: el Señor lo "
              "preparará para la espada.",
    (26, 29): "Difícilmente escapará el mercader de la falta, y no será "
              "justificado el tendero de pecado.",

    # Capítulo 27
    (27, 1): "Por una cosa sin importancia muchos pecaron, y el que busca "
             "multiplicar aparta el ojo.",
    (27, 2): "Entre las junturas de las piedras se hinca la estaca, y entre "
             "la venta y la compra se estruja el pecado.",
    (27, 3): "Si uno no se mantiene con empeño en el temor del Señor, pronto "
             "será derribada su casa.",
    (27, 4): "Al sacudir la criba queda la basura; así los desechos del "
             "hombre en su razonamiento.",
    (27, 5): "Las vasijas del alfarero las prueba el horno, y la prueba del "
             "hombre está en su razonamiento.",
    (27, 6): "El cultivo del árbol lo manifiesta su fruto; así la palabra, el "
             "pensamiento del corazón del hombre.",
    (27, 7): "Antes de que razone no alabes a un hombre, porque ésta es la "
             "prueba de los hombres.",
    (27, 8): "Si persigues lo justo, lo alcanzarás, y te lo vestirás como "
             "túnica talar de gloria.",
    (27, 9): "Las aves se posan con sus semejantes, y la verdad volverá a los "
             "que la practican.",
    (27, 10): "El león acecha la presa; así los pecados a los que obran la "
              "injusticia.",
    (27, 11): "La conversación del piadoso es siempre sabiduría, pero el "
              "necio cambia como la luna.",
    (27, 12): "En medio de insensatos aguarda la ocasión, pero en medio de "
              "los reflexivos persevera.",
    (27, 13): "La conversación de los necios es cosa aborrecible, y su risa "
              "está en el desenfreno del pecado.",
    (27, 14): "El hablar del que jura mucho eriza los cabellos, y su pelea "
              "hace taparse los oídos.",
    (27, 15): "Derramamiento de sangre es la pelea de los soberbios, y sus "
              "injurias mutuas son cosa penosa de oír.",
    (27, 16): "El que descubre secretos pierde el crédito, y no hallará amigo "
              "conforme a su alma.",
    (27, 17): "Ama al amigo y sé fiel con él; ⁽¹⁹⁾ pero si descubres sus "
              "secretos, no vayas tras él.",
    (27, 18): "Porque como un hombre acaba con su enemigo, así acabaste tú "
              "con la amistad del prójimo;",
    (27, 19): "y como soltaste un ave de tu mano, así dejaste ir al prójimo, "
              "y no lo volverás a cazar.",
    (27, 20): "No lo persigas, porque se alejó mucho, y escapó como gacela "
              "del lazo.",
    (27, 21): "Porque la herida se puede ⁽²³⁾ vendar, y para la injuria hay "
              "reconciliación; ⁽²⁴⁾ pero el que descubrió secretos perdió la "
              "esperanza.",
    (27, 22): "El que guiña el ojo trama males, y nadie lo apartará de ello.",
    (27, 23): "Delante de tus ojos endulzará tu boca, y de tus palabras se "
              "admirará; pero después torcerá su boca, y en tus palabras "
              "pondrá tropiezo.",
    (27, 24): "Muchas cosas he aborrecido, pero ninguna he igualado a él, y "
              "el Señor lo aborrecerá.",
    (27, 25): "El que lanza una piedra a lo alto, sobre su cabeza la lanza, y "
              "el golpe traicionero reparte heridas.",
    (27, 26): "El que cava una fosa caerá en ella, y el que tiende un lazo "
              "será atrapado en él.",
    (27, 27): "Al que hace el mal, sobre él le rodará, y no sabrá de dónde le "
              "viene.",
    (27, 28): "Burla y ultraje son cosa de soberbios, y la venganza, como "
              "león, lo acechará.",
    (27, 29): "En el lazo caerán los que se alegran de la caída de los "
              "piadosos, y el dolor los consumirá antes de su muerte.",
    (27, 30): "Rencor e ira, también éstas son abominaciones, y el hombre "
              "pecador se aferrará a ellas.",

    # Capítulo 28
    (28, 1): "El que se venga hallará la venganza de parte del Señor, y él le "
             "llevará estrecha cuenta de sus pecados.",
    (28, 2): "Perdona a tu prójimo el agravio, y entonces, cuando ores, te "
             "serán perdonados tus pecados.",
    (28, 3): "Un hombre guarda ira contra otro hombre, ¿y busca del Señor la "
             "curación?",
    (28, 4): "Con un hombre semejante a él no tiene misericordia, ¿y ruega "
             "por sus propios pecados?",
    (28, 5): "Él, que es carne, guarda rencor; ¿quién hará expiación por sus "
             "pecados?",
    (28, 6): "Acuérdate de las postrimerías y deja de enemistarte; ⁽⁷⁾ de la "
             "corrupción y de la muerte, y permanece en los mandamientos.",
    (28, 7): "Acuérdate de los mandamientos y no guardes rencor al prójimo, "
             "⁽⁹⁾ y de la alianza del Altísimo, y pasa por alto la "
             "ignorancia.",
    (28, 8): "Apártate de la contienda, y disminuirás los pecados; porque el "
             "hombre iracundo enciende la contienda,",
    (28, 9): "y el hombre pecador turba a los amigos, y entre los que viven "
             "en paz siembra la calumnia.",
    (28, 10): "Según la materia del fuego, así arderá; según la fuerza del "
              "hombre será su furor, y según su riqueza levantará su ira; y "
              "según la porfía de la contienda se encenderá.",
    (28, 11): "La disputa apresurada enciende el fuego, y la pelea apresurada "
              "derrama sangre.",
    (28, 12): "Si soplas la chispa, se encenderá, y si escupes sobre ella, se "
              "apagará; y ambas cosas salen de tu boca.",
    (28, 13): "Maldecid al murmurador y al de doble lengua, porque han "
              "perdido a muchos que vivían en paz.",
    (28, 14): "La lengua tercera ha sacudido a muchos y los ha dispersado de "
              "nación en nación, ⁽¹⁷⁾ y ha derribado ciudades fortificadas, y "
              "ha trastornado las casas de los magnates.",
    (28, 15): "La lengua tercera ha echado fuera a mujeres valerosas, y las "
              "ha privado del fruto de sus trabajos.",
    (28, 16): "El que le presta atención no hallará reposo, ni morará en "
              "quietud.",
    (28, 17): "El golpe del látigo produce cardenales, pero el golpe de la "
              "lengua quebranta los huesos.",
    (28, 18): "Muchos cayeron a filo de espada, pero no tantos como los que "
              "cayeron por la lengua.",
    (28, 19): "Dichoso el que está protegido de ella, el que no pasó por su "
              "furor, el que no arrastró su yugo, y no fue atado con sus "
              "cadenas;",
    (28, 20): "porque su yugo es yugo de hierro, y sus cadenas son cadenas de "
              "bronce.",
    (28, 21): "Muerte mala es la muerte que ella da, y más provechoso que "
              "ella es el sepulcro.",
    (28, 22): "No dominará a los piadosos, y en su llama no se quemarán.",
    (28, 23): "Los que abandonan al Señor caerán en ella, y en ellos arderá y "
              "no se apagará; será enviada contra ellos como un león, y como "
              "un leopardo los destrozará.",
    (28, 24): "[…] cerca tu posesión con espinos, ⁽²⁹⁾ ata tu plata y tu oro;",
    (28, 25): "y para tus palabras haz balanza y pesa, y para tu boca haz "
              "puerta y cerrojo.",
    (28, 26): "Cuida de no resbalar en ella, no sea que caigas delante del "
              "que te acecha.",

    # Capítulo 29
    (29, 1): "El que hace misericordia presta a su prójimo, y el que lo "
             "sostiene con su mano guarda los mandamientos.",
    (29, 2): "Presta a tu prójimo en el tiempo de su necesidad, y a tu vez "
             "devuelve al prójimo a su debido tiempo.",
    (29, 3): "Mantén tu palabra y sé fiel con él, y en todo tiempo hallarás "
             "lo que necesites.",
    (29, 4): "Muchos tuvieron el préstamo por un hallazgo, y causaron "
             "molestia a los que los ayudaron.",
    (29, 5): "Hasta que recibe, besa la mano del otro, y por los bienes del "
             "prójimo humilla la voz; ⁽⁶⁾ pero al tiempo de devolver alarga "
             "el plazo, y paga con palabras de desgana, y echa la culpa al "
             "tiempo.",
    (29, 6): "Si el otro puede, apenas recobrará la mitad, y lo tendrá por un "
             "hallazgo; ⁽⁸⁾ y si no, lo ha despojado de sus bienes, y se ha "
             "ganado un enemigo sin motivo; con maldiciones e injurias le "
             "pagará, y en lugar de honra le pagará con deshonra.",
    (29, 7): "Muchos, a causa de esta maldad, se volvieron atrás; temieron "
             "ser despojados sin razón.",
    (29, 8): "Con todo, sé paciente con el humilde, y no le hagas esperar la "
             "limosna.",
    (29, 9): "Por causa del mandamiento socorre al pobre, y en su necesidad "
             "no lo despidas vacío.",
    (29, 10): "Pierde tu dinero por el hermano y el amigo, y no se enmohezca "
              "bajo la piedra para perdición.",
    (29, 11): "Pon tu tesoro conforme a los mandamientos del Altísimo, y te "
              "aprovechará más que el oro.",
    (29, 12): "Encierra la limosna en tus despensas, y ella te librará de "
              "toda aflicción;",
    (29, 13): "más que escudo fuerte y más que lanza poderosa, peleará por ti "
              "frente al enemigo.",
    (29, 14): "El hombre bueno sale fiador de su prójimo, y el que ha perdido "
              "la vergüenza lo abandonará.",
    (29, 15): "No olvides los favores del fiador, porque dio su vida por ti.",
    (29, 16): "El pecador echa a perder los bienes de su fiador, y el ingrato "
              "de corazón abandonará al que lo libró.",
    (29, 18): "La fianza ha arruinado a muchos que prosperaban, y los ha "
              "sacudido como ola del mar; ⁽²⁵⁾ a hombres poderosos los "
              "desterró, y anduvieron errantes entre naciones extrañas.",
    (29, 19): "El pecador que cae en fianzas y persigue ganancias de "
              "contratas caerá en pleitos.",
    (29, 20): "Socorre al prójimo según tus fuerzas, y guárdate a ti mismo de "
              "caer.",
    (29, 21): "Lo primero para la vida es el agua y el pan y el vestido, y "
              "una casa que cubra la desnudez.",
    (29, 22): "Mejor es la vida del pobre bajo un techo de vigas que manjares "
              "espléndidos en casa ajena.",
    (29, 23): "Con lo poco y con lo mucho vive contento.",
    (29, 24): "Mala vida es ir de casa en casa, y donde uno es forastero no "
              "abrirá la boca.",
    (29, 25): "Hospedarás y darás de beber a ingratos, y además de esto oirás "
              "cosas amargas:",
    (29, 26): "«Ven acá, forastero, pon la mesa, y si tienes algo en la mano, "
              "dame de comer»;",
    (29, 27): "«Sal, forastero, deja el sitio a uno de honra; ha venido a "
              "hospedarse conmigo mi hermano, necesito la casa».",
    (29, 28): "Pesadas son estas cosas para el hombre que tiene juicio: el "
              "reproche de la casa y el ultraje del acreedor. Acerca de los "
              "hijos.",

    # Capítulo 30
    (30, 1): "El que ama a su hijo le aplicará el azote sin cesar, para "
             "alegrarse de él al final.",
    (30, 2): "El que corrige a su hijo sacará provecho de él, y entre sus "
             "conocidos se gloriará de él.",
    (30, 3): "El que enseña a su hijo dará celos al enemigo, y delante de sus "
             "amigos se regocijará en él.",
    (30, 4): "Murió su padre, y es como si no hubiera muerto, porque dejó "
             "tras de sí uno semejante a él.",
    (30, 5): "En su vida lo vio y se alegró, y en su muerte no se "
             "entristeció;",
    (30, 6): "frente a los enemigos dejó un vengador, y para los amigos uno "
             "que les devuelva el favor.",
    (30, 7): "El que mima a su hijo vendará sus heridas, y a cada grito se le "
             "conmoverán las entrañas.",
    (30, 8): "El caballo no domado sale reacio, y el hijo dejado a su antojo "
             "sale atrevido.",
    (30, 9): "Mima al niño, y te dejará espantado; juega con él, y te "
             "entristecerá.",
    (30, 10): "No rías con él, para que no tengas que dolerte con él, y al "
              "final te rechinarán los dientes.",
    (30, 11): "No le des libertad en su juventud.",
    (30, 12): "Quiébrale las costillas mientras es niño, no sea que, "
              "endurecido, te desobedezca.",
    (30, 13): "Educa a tu hijo y trabaja en él, para que no tropieces con "
              "su deshonra.",
    (30, 13, "b"): "El corazón espléndido y bueno a la mesa se cuidará de sus "
              "manjares.",
    (30, 14): "Mejor es el pobre sano y fuerte de constitución que el rico "
              "azotado en su cuerpo.",
    (30, 15): "La salud y el buen estado valen más que todo el oro, y un "
              "cuerpo robusto más que una dicha sin medida. Acerca de los "
              "alimentos.",
    (30, 16): "No hay riqueza mejor que la salud del cuerpo, ni alegría por "
              "encima del gozo del corazón.",
    (30, 17): "Mejor es la muerte que una vida amarga, o que una enfermedad "
              "persistente. Bienes derramados sobre una boca cerrada son como "
              "ofrendas de manjares puestas sobre un sepulcro.",
    (30, 19): "¿De qué le sirve al ídolo la ofrenda? Porque ni come ni huele; "
              "⁽²⁰⁾ así es el que es perseguido por el Señor:",
    (30, 20): "ve con sus ojos y gime, como el eunuco que abraza a una virgen "
              "y gime.",
    (30, 21): "No entregues tu alma a la tristeza, ni te atormentes a ti "
              "mismo con tus cavilaciones.",
    (30, 22): "La alegría del corazón es la vida del hombre, y el regocijo "
              "del varón es largura de días.",
    (30, 23): "Ama tu alma y consuela tu corazón, y aleja de ti la tristeza "
              "prolongada; ⁽²⁵⁾ porque a muchos ha matado la tristeza, y no "
              "hay provecho en ella.",
    (30, 24): "Los celos y la ira acortan los días, y la preocupación trae la "
              "vejez antes de tiempo.",

    # Capítulo 31
    (31, 1): "El desvelo por la riqueza consume las carnes, y la preocupación "
             "por ella aleja el sueño.",
    (31, 2): "La preocupación del desvelo reclama la somnolencia, y la "
             "enfermedad grave ahuyenta el sueño.",
    (31, 3): "Se afanó el rico amontonando riquezas, y en el descanso se "
             "sacia de sus deleites.",
    (31, 4): "Se afanó el pobre en la escasez de su vida, y en el descanso "
             "queda necesitado.",
    (31, 5): "El que ama el oro no será justificado, y el que persigue la "
             "corrupción, de ella se hartará.",
    (31, 6): "Muchos fueron entregados a la ruina por causa del oro, y su "
             "perdición estuvo delante de sus ojos.",
    (31, 7): "Madero de tropiezo es para los que se apasionan por él, y todo "
             "insensato quedará preso en él.",
    (31, 8): "Bienaventurado el rico que fue hallado sin tacha, y que no "
             "anduvo tras el oro.",
    (31, 9): "¿Quién es, y lo llamaremos bienaventurado? Porque hizo "
             "maravillas en su pueblo.",
    (31, 10): "¿Quién fue probado en ello y fue hallado perfecto? Sea para él "
              "motivo de gloria. ¿Quién pudo transgredir y no transgredió, y "
              "hacer el mal y no lo hizo?",
    (31, 11): "Se afianzarán sus bienes, y la asamblea contará sus limosnas.",
    (31, 12): "¿Te has sentado a una mesa grande? No abras sobre ella tu "
              "garganta, ⁽¹³⁾ ni digas: «¡Cuántas cosas hay sobre ella!»",
    (31, 13): "Acuérdate de que mala cosa es el ojo malo; ⁽¹⁵⁾ ¿qué cosa fue "
              "creada más mala que el ojo? Por eso derrama lágrimas ante todo "
              "rostro.",
    (31, 14): "A donde él mire, no extiendas la mano, ⁽¹⁷⁾ ni te estrujes con "
              "él en el plato.",
    (31, 15): "¹⁵Juzga lo de tu prójimo por ti mismo, y en todo asunto "
              "reflexiona.",
    (31, 16): "Come como hombre lo que se te pone delante, y no mastiques con "
              "ansia, para que no te aborrezcan.",
    (31, 17): "Deja de comer el primero por cortesía, y no seas insaciable, "
              "no sea que ofendas.",
    (31, 18): "Y si te has sentado en medio de muchos, no extiendas tu mano "
              "antes que ellos.",
    (31, 19): "¡Cuán suficiente es lo poco para el hombre bien educado! Y en "
              "su lecho no jadea.",
    (31, 20): "Sueño sano con vientre moderado: se levanta de mañana, y su "
              "alma está consigo. ⁽²³⁾ El tormento del desvelo, y el cólico, "
              "y el retortijón están con el hombre insaciable.",
    (31, 21): "Y si te has visto forzado en las comidas, levántate a mitad de "
              "ellas, y hallarás descanso.",
    (31, 22): "Escúchame, hijo, y no me desprecies, y al final comprenderás "
              "mis palabras. ⁽²⁷⁾ En todas tus obras sé diligente, y ninguna "
              "enfermedad te sobrevendrá.",
    (31, 23): "Al que es espléndido en los panes lo bendecirán los labios, y "
              "el testimonio de su generosidad es fiel.",
    (31, 24): "Contra el que es mezquino en el pan murmurará la ciudad, y el "
              "testimonio de su mezquindad es exacto.",
    (31, 25): "No te hagas el valiente con el vino, porque a muchos ha "
              "perdido el vino.",
    (31, 26): "El horno prueba el temple del acero en el baño; así el vino "
              "prueba los corazones en la contienda de los soberbios.",
    (31, 27): "Como la vida es el vino para el hombre, si lo bebes con su "
              "medida; ³¿qué vida tiene aquel a quien le falta el vino? ⁽³⁵⁾ "
              "Y él fue creado para alegría de los hombres.",
    (31, 28): "Alegría del corazón y gozo del alma es el vino bebido a su "
              "tiempo y con mesura.",
    (31, 29): "Amargura del alma es el vino bebido en abundancia, con "
              "provocación y tropiezo.",
    (31, 30): "La embriaguez acrecienta el furor del insensato para su caída, "
              "disminuyendo la fuerza y añadiendo heridas.",
    (31, 31): "En un banquete de vino no reprendas al prójimo, ni lo "
              "desprecies en su alegría; ⁽⁴²⁾ no le digas palabra de afrenta, "
              "y no lo aflijas reclamándole.",

    # Capítulo 32
    (32, 1): "¿Te han puesto por presidente? No te enaltezcas; sé entre ellos "
             "como uno de ellos; ⁽²⁾ cuida de ellos, y así siéntate.",
    (32, 2): "Y cumplido todo tu deber, reclínate, ⁽³⁾ para que te alegres "
             "por causa de ellos y recibas la corona por tu buen orden.",
    (32, 3): "Habla, anciano, porque te corresponde, ⁽⁵⁾ con ciencia exacta, "
             "y no estorbes la música.",
    (32, 4): "Donde hay audición, no derrames palabrería, y no te hagas el "
             "sabio fuera de tiempo.",
    (32, 5): "Sello de carbunclo en adorno de oro es un concierto de músicos "
             "en un banquete de vino.",
    (32, 6): "Sello de esmeralda en engaste de oro es la melodía de los "
             "músicos junto al vino dulce.",
    (32, 7): "Habla, joven, si hay necesidad de ti, ⁽¹¹⁾ apenas dos veces, si "
             "se te pregunta.",
    (32, 8): "Resume tu palabra, mucho en pocas; sé como quien sabe y a la "
             "vez calla.",
    (32, 9): "En medio de los grandes no te hagas su igual, y cuando otro "
             "habla no charles mucho.",
    (32, 10): "Antes del trueno se apresura el relámpago, y delante del "
              "modesto irá la gracia.",
    (32, 11): "A su hora levántate, y no seas el último; corre a tu casa, y "
              "no seas perezoso.",
    (32, 12): "Allí diviértete y haz lo que tienes en el pensamiento, pero no "
              "peques con palabra soberbia.",
    (32, 13): "Y por estas cosas bendice al que te hizo y te embriaga de sus "
              "bienes.",
    (32, 14): "El que teme al Señor recibirá la instrucción, y los que "
              "madrugan hallarán su favor.",
    (32, 15): "El que busca la ley se saciará de ella, pero el hipócrita "
              "tropezará en ella.",
    (32, 16): "Los que temen al Señor hallarán el juicio, y harán brillar "
              "como luz sus justos decretos.",
    (32, 17): "El hombre pecador rehúye la reprensión, y conforme a su "
              "voluntad hallará excusa.",
    (32, 18): "El hombre de consejo no desdeñará la reflexión; el extraño y "
              "el soberbio no se encogerá de temor, ⁽²³⁾ ni aun después de "
              "haber obrado por sí sin consejo.",
    (32, 19): "Sin consejo no hagas nada, y una vez hecho, no te arrepientas.",
    (32, 20): "No andes por camino de tropiezo, y no tropezarás en los "
              "pedregales.",
    (32, 21): "No te fíes del camino sin tropiezos,",
    (32, 22): "y guárdate de tus hijos.",
    (32, 23): "En toda obra confía en tu alma, porque también esto es guardar "
              "los mandamientos.",
    (32, 24): "El que cree en la ley atiende a los mandamientos, y el que "
              "confía en el Señor no sufrirá menoscabo.",

    # Capítulo 33
    (33, 1): "Al que teme al Señor no le sobrevendrá mal, sino que aun en la "
             "prueba lo librará de nuevo.",
    (33, 2): "El hombre sabio no aborrecerá la ley, pero el que finge en ella "
             "es como nave en la tempestad.",
    (33, 3): "El hombre inteligente confiará en la ley, y la ley le es fiel "
             "⁽⁴⁾ como la consulta de los justos.",
    (33, 4): "Prepara tu palabra, y así serás escuchado; ata bien tu "
             "instrucción, y responde.",
    (33, 5): "Rueda de carro son las entrañas del necio, y como eje que gira "
             "es su razonamiento.",
    (33, 6): "Como caballo padre es el amigo burlón: relincha debajo de "
             "cualquiera que lo monta.",
    (33, 7): "¿Por qué un día aventaja a otro día, si toda la luz de los días "
             "del año viene del sol?",
    (33, 8): "Por la ciencia del Señor fueron distinguidos, y él dispuso "
             "diversos tiempos y fiestas.",
    (33, 9): "A algunos de ellos los ensalzó y santificó, y a otros los puso "
             "en el número de los días.",
    (33, 10): "Y todos los hombres son del polvo del suelo, y de la tierra "
              "fue creado Adán.",
    (33, 11): "En la plenitud de su ciencia el Señor los distinguió, y "
              "diversificó sus caminos.",
    (33, 12): "A algunos de ellos los bendijo y ensalzó, y a otros los "
              "santificó y los acercó a sí; a otros los maldijo y humilló, y "
              "los derribó de su puesto.",
    (33, 13): "Como el barro del alfarero en su mano ⁽¹⁴⁾ —todos sus caminos "
              "son según su beneplácito—, así están los hombres en la mano "
              "del que los hizo, para darles conforme a su juicio.",
    (33, 14): "Frente al mal está el bien, y frente a la muerte la vida; así, "
              "frente al piadoso, el pecador.",
    (33, 15): "Y así contempla todas las obras del Altísimo: de dos en dos, "
              "una frente a la otra.",
    (33, 16, "a"): "Y yo, el último, me desvelé,",
    (33, 25): "²⁵como quien rebusca tras los vendimiadores; ⁽¹⁷⁾ por la "
              "bendición del Señor llegué primero, y como vendimiador llené "
              "el lagar.",
    (33, 26): "Considerad que no he trabajado para mí solo, sino para todos "
              "los que buscan la instrucción.",
    (33, 27): "Escuchadme, grandes del pueblo, y vosotros, jefes de la "
              "asamblea, prestad oído.",
    (33, 28): "Ni al hijo ni a la mujer, ni al hermano ni al amigo des poder "
              "sobre ti mientras vivas; y no des a otro tus bienes, no sea "
              "que, arrepentido, tengas que suplicar por ellos.",
    (33, 29): "Mientras aún vivas y haya aliento en ti, no te entregues en "
              "trueque a ninguna carne.",
    (33, 30): "Porque mejor es que tus hijos te supliquen a ti, que no que tú "
              "mires a las manos de tus hijos.",
    (33, 31): "En todas tus obras sé superior; no pongas mancha en tu gloria.",
    (33, 32): "En el día en que se acaben los días de tu vida, y en el tiempo "
              "de tu muerte, reparte la herencia.",
    (33, 33): "Forraje, vara y carga para el asno; pan, disciplina y trabajo "
              "para el siervo.",
    (33, 34): "Haz trabajar al esclavo, y hallarás descanso; déjale libres "
              "las manos, y buscará la libertad.",
    (33, 35): "El yugo y la correa doblegan la cerviz, y para el siervo "
              "malhechor, potro y tormentos.",
    (33, 36): "Mételo en el trabajo, para que no esté ocioso,",
    (33, 37): "porque mucha maldad ha enseñado la ociosidad.",
    (33, 38): "Ponlo a trabajar como le conviene, y si no obedece, hazle más "
              "pesados los grilletes. Pero no te excedas con ninguna carne, y "
              "sin juicio no hagas nada.",
    (33, 39): "Si tienes un siervo, sea como tú, porque con sangre lo "
              "adquiriste; si tienes un siervo, trátalo como a ti mismo, "
              "porque lo necesitas como a tu propia alma.",
    (33, 40): "Si lo maltratas, y él se levanta y huye, ⁽³³⁾ ¿por qué camino "
              "lo buscarás?",

    # Capítulo 34
    (34, 1): "Esperanzas vanas y falsas son las del hombre sin entendimiento, "
             "y los sueños dan alas a los insensatos.",
    (34, 2): "Como quien atrapa una sombra y persigue el viento, así es el "
             "que se atiene a los sueños.",
    (34, 3): "Esto frente a aquello es la visión de los sueños: frente a un "
             "rostro, la semejanza de un rostro.",
    (34, 4): "De lo impuro, ¿qué será purificado? Y de lo mentiroso, ¿qué "
             "dirá verdad?",
    (34, 5): "Adivinaciones, agüeros y sueños son vanidad, ⁽⁶⁾ y el corazón "
             "se forja fantasías como el de la mujer que está de parto.",
    (34, 6): "Si no son enviados por el Altísimo en visitación, no pongas en "
             "ellos tu corazón;",
    (34, 7): "porque a muchos extraviaron los sueños, y cayeron los que en "
             "ellos esperaban.",
    (34, 8): "Sin mentira se cumplirá la ley, y la sabiduría en boca fiel es "
             "perfección.",
    (34, 9): "El hombre instruido conoce muchas cosas, y el de mucha "
             "experiencia expondrá con inteligencia.",
    (34, 10): "El que no ha sido probado sabe poco,",
    (34, 11): "pero el que ha andado errante acrecienta su sagacidad.",
    (34, 12): "Muchas cosas he visto en mis andanzas, y mi entendimiento es "
              "mayor que mis palabras.",
    (34, 13): "Muchas veces corrí peligro hasta la muerte, y me salvé gracias "
              "a estas cosas.",
    (34, 14): "El espíritu de los que temen al Señor vivirá,",
    (34, 15): "porque su esperanza está en el que los salva.",
    (34, 16): "El que teme al Señor no se amedrentará ni se acobardará, "
              "porque él es su esperanza.",
    (34, 17): "Del que teme al Señor, bienaventurada es el alma.",
    (34, 18): "¿En quién se apoya? ¿Y quién es su sostén?",
    (34, 19): "Los ojos del Señor están sobre los que le aman: escudo "
              "poderoso y apoyo de fortaleza, abrigo contra el viento "
              "abrasador y sombra contra el mediodía, ⁽²⁰⁾ guarda contra el "
              "tropiezo y socorro contra la caída.",
    (34, 20): "Él levanta el alma e ilumina los ojos, y da salud, vida y "
              "bendición.",
    (34, 21): "El que sacrifica de lo mal adquirido, su ofrenda es escarnio,",
    (34, 22): "y no son aceptos los dones escarnecidos de los inicuos.",
    (34, 23): "No se complace el Altísimo en las ofrendas de los impíos, ni "
              "por la multitud de sacrificios perdona los pecados.",
    (34, 24): "Como el que degüella al hijo delante de su padre es el que "
              "ofrece sacrificio de los bienes de los pobres.",
    (34, 25): "El pan de los necesitados es la vida de los pobres; el que se "
              "lo quita es hombre sanguinario.",
    (34, 26): "Mata a su prójimo el que le quita el sustento,",
    (34, 27): "y derrama sangre el que priva al jornalero de su salario.",
    (34, 28): "Uno edifica y otro derriba: ¿qué provecho sacaron sino fatiga?",
    (34, 29): "Uno ora y otro maldice: ¿la voz de cuál escuchará el Soberano?",
    (34, 30): "El que se lava por haber tocado un muerto y lo vuelve a tocar, "
              "¿de qué le sirvió su baño?",
    (34, 31): "Así el hombre que ayuna por sus pecados y vuelve otra vez a "
              "hacer lo mismo: ¿quién escuchará su oración, y de qué le "
              "sirvió humillarse?",

    # Capítulo 35
    (35, 1): "El que guarda la ley multiplica las ofrendas;",
    (35, 2): "ofrece sacrificio de salvación el que atiende a los "
             "mandamientos.",
    (35, 3): "El que devuelve un favor ofrece flor de harina,",
    (35, 4): "y el que hace limosna ofrece sacrificio de alabanza.",
    (35, 5): "Agrado del Señor es apartarse de la maldad, y expiación, "
             "apartarse de la injusticia.",
    (35, 6): "No te presentes vacío delante del Señor,",
    (35, 7): "porque todas estas cosas se hacen por causa del mandamiento.",
    (35, 8): "La ofrenda del justo unge de grosura el altar, y su buen olor "
             "sube delante del Altísimo.",
    (35, 9): "El sacrificio del varón justo es acepto, y su memorial no será "
             "olvidado.",
    (35, 10): "Con ojo generoso glorifica al Señor, y no escatimes las "
              "primicias de tus manos.",
    (35, 11): "En toda dádiva muestra alegre tu rostro, y con gozo consagra "
              "el diezmo.",
    (35, 12): "Da al Altísimo según él te ha dado, y con ojo generoso, "
              "conforme a lo que alcance tu mano;",
    (35, 13): "porque el Señor es el que retribuye, y te devolverá siete "
              "veces más.",
    (35, 14): "No intentes sobornarle con dádivas, porque no las aceptará,",
    (35, 15): "y no te apoyes en sacrificio injusto; porque el Señor es juez, "
              "y no hay en él acepción de personas.",
    (35, 16): "No hará acepción de personas en perjuicio del pobre, y "
              "escuchará la súplica del agraviado.",
    (35, 17): "No desdeñará la súplica del huérfano, ni a la viuda cuando "
              "derrama su queja.",
    (35, 18): "¿No bajan las lágrimas de la viuda por su mejilla,",
    (35, 19): "y su clamor contra el que las hizo correr?",
    (35, 20): "El que sirve a Dios con agrado será acogido, y su súplica "
              "llegará hasta las nubes.",
    (35, 21): "La oración del humilde atraviesa las nubes, y hasta que no "
              "llega no se consuela; y no se aparta hasta que el Altísimo la "
              "atienda,",
    (35, 22): "y juzgue con justicia y haga juicio. Y el Señor no tardará, ni "
              "tendrá paciencia con ellos, hasta que quebrante los lomos de "
              "los despiadados,",
    (35, 23): "y dé a las naciones su merecido castigo; hasta que extirpe la "
              "multitud de los insolentes y quebrante los cetros de los "
              "injustos;",
    (35, 24): "hasta que pague al hombre según sus acciones, y las obras de "
              "los hombres según sus pensamientos;",
    (35, 25): "hasta que juzgue la causa de su pueblo y los alegre con su "
              "misericordia.",
    (35, 26): "Hermosa es la misericordia en el tiempo de la aflicción, como "
              "las nubes de lluvia en tiempo de sequía.",

    # Capítulo 36
    (36, 1): "Ten piedad de nosotros, Soberano, Dios de todas las cosas,",
    (36, 2): "y mira, ⁽²⁾ y arroja tu temor sobre todas las naciones.",
    (36, 3): "Levanta tu mano contra las naciones extranjeras, y vean tu "
             "poderío.",
    (36, 4): "Como delante de ellas te mostraste santo en nosotros, así "
             "delante de nosotros seas engrandecido en ellas;",
    (36, 5): "y te conozcan, como también nosotros hemos conocido que no hay "
             "Dios fuera de ti, Señor.",
    (36, 6): "Renueva las señales y repite los prodigios,",
    (36, 7): "glorifica tu mano y tu brazo derecho;",
    (36, 8): "despierta el furor y derrama la ira,",
    (36, 9): "extirpa al adversario y aplasta al enemigo.",
    (36, 10): "Apresura el tiempo y acuérdate del juramento, y cuenten ellos "
              "tus grandezas.",
    (36, 11): "En el ardor del fuego sea devorado el que escape, y los que "
              "maltratan a tu pueblo hallen la perdición.",
    (36, 12): "Quebranta las cabezas de los príncipes enemigos, que dicen: "
              "«No hay otro fuera de nosotros».",
    (36, 13, "a"): "Reúne a todas las tribus de Jacob,",
    (36, 16, "b"): "y tómalos por heredad tuya como al principio.",
    (36, 17): "Ten piedad, Señor, del pueblo llamado con tu nombre, y de "
              "Israel, a quien hiciste semejante a un primogénito.",
    (36, 18): "Compadécete de la ciudad de tu santuario, Jerusalén, ciudad de "
              "tu reposo.",
    (36, 19): "Llena a Sión de la alabanza de tus proezas, y de tu gloria a "
              "tu pueblo.",
    (36, 20): "Da testimonio en favor de los que fueron tus criaturas desde "
              "el principio, y cumple las profecías hechas en tu nombre.",
    (36, 21): "Da recompensa a los que te esperan, y sean hallados fieles tus "
              "profetas.",
    (36, 22): "Escucha, Señor, la súplica de tus siervos, ⁽¹⁹⁾ conforme a la "
              "bendición de Aarón sobre tu pueblo, y conocerán todos los que "
              "están sobre la tierra que tú eres el Señor, el Dios de los "
              "siglos.",
    (36, 23): "Todo alimento lo come el vientre, pero hay alimento mejor que "
              "otro alimento.",
    (36, 24): "El paladar distingue los manjares de la caza; así el corazón "
              "inteligente, las palabras mentirosas.",
    (36, 25): "El corazón torcido causará tristeza, pero el hombre de mucha "
              "experiencia le dará su merecido.",
    (36, 26): "La mujer acepta a cualquier varón, pero hay hija mejor que "
              "otra hija.",
    (36, 27): "La belleza de la mujer alegra el rostro, y sobrepasa todo "
              "deseo del hombre.",
    (36, 28): "Si hay en su lengua misericordia y mansedumbre, su marido no "
              "es como los hijos de los hombres.",
    (36, 29): "El que adquiere mujer comienza su hacienda: una ayuda "
              "semejante a él y columna de reposo.",
    (36, 30): "Donde no hay cerca, la propiedad será saqueada; y donde no hay "
              "mujer, gemirá el hombre errante.",
    (36, 31): "Porque ¿quién se fiará de un salteador ágil que salta de "
              "ciudad en ciudad? Así del hombre que no tiene nido y se aloja "
              "dondequiera que le sorprende la noche.",

    # Capítulo 37
    (37, 1): "Todo amigo dirá: «También yo soy su amigo»; pero hay amigo que "
             "sólo de nombre es amigo.",
    (37, 2): "¿No es una tristeza que dura hasta la muerte ⁽²⁾ el compañero y "
             "amigo que se vuelve enemigo?",
    (37, 3): "¡Oh mala inclinación! ¿De dónde saliste rodando para cubrir de "
             "engaño la tierra seca?",
    (37, 4): "El compañero se regocija con el amigo en la alegría, y en el "
             "tiempo de la aflicción estará en contra.",
    (37, 5): "El compañero se afana con el amigo por causa del vientre; ante "
             "la guerra tomará el escudo.",
    (37, 6): "No te olvides del amigo en tu alma, y no dejes de acordarte de "
             "él en tus riquezas.",
    (37, 7): "Todo consejero ensalza su consejo, pero hay quien aconseja en "
             "provecho propio.",
    (37, 8): "Guarda tu alma del consejero, y conoce primero qué necesidad "
             "tiene, porque también él aconsejará para sí mismo, ⁽¹⁰⁾ no sea "
             "que eche sobre ti la suerte",
    (37, 9): "y te diga: ⁽¹¹⁾ «Bueno es tu camino», y se ponga enfrente para "
             "ver lo que te sucede.",
    (37, 10): "No consultes con el que te mira con recelo, y a los que te "
              "envidian oculta tu consejo;",
    (37, 11): "¹¹ni con una mujer acerca de su rival, ni con un cobarde "
              "acerca de la guerra, ni con un mercader acerca del negocio, ni "
              "con un comprador acerca de la venta, ni con un envidioso "
              "acerca de la gratitud, ni con un despiadado acerca de la "
              "bondad, ni con un perezoso acerca de cualquier trabajo, ni con "
              "un jornalero sin hogar acerca de acabar la obra, ni con un "
              "siervo ocioso acerca de mucho trabajo: no te apoyes en éstos "
              "para ningún consejo.",
    (37, 12): "Antes bien, trata asiduamente con el hombre piadoso, al que "
              "sepas que guarda los mandamientos, ⁽¹⁶⁾ que en su alma es "
              "conforme a tu alma, y que, si tropiezas, se dolerá contigo.",
    (37, 13): "Y afirma el consejo de tu corazón, porque no hay para ti nadie "
              "más fiel que él;",
    (37, 14): "porque el alma del hombre suele a veces avisar más que siete "
              "centinelas sentados en lo alto de una atalaya.",
    (37, 15): "Y sobre todo esto, suplica al Altísimo que enderece tu camino "
              "en la verdad.",
    (37, 16): "Principio de toda obra es la palabra, y antes de toda acción, "
              "el consejo.",
    (37, 17): "La huella de la mudanza está en el corazón:",
    (37, 18): "cuatro partes brotan de él: el bien y el mal, la vida y la "
              "muerte; y la que continuamente las domina es la lengua.",
    (37, 19): "Hay hombre astuto que es maestro de muchos, y para su propia "
              "alma es inútil.",
    (37, 20): "Hay quien se hace el sabio en palabras y es aborrecido; éste "
              "quedará privado de todo alimento;",
    (37, 21): "porque no le fue dada gracia de parte del Señor, pues de toda "
              "sabiduría fue despojado.",
    (37, 22): "Hay quien es sabio para su propia alma, y los frutos de su "
              "inteligencia son fieles en su boca.",
    (37, 23): "El hombre sabio instruirá a su propio pueblo, y los frutos de "
              "su inteligencia son fieles.",
    (37, 24): "El hombre sabio será colmado de bendición, y lo llamarán "
              "dichoso todos los que lo vean.",
    (37, 25): "La vida del hombre está en número de días, pero los días de "
              "Israel son innumerables.",
    (37, 26): "El sabio heredará la confianza en su pueblo, y su nombre "
              "vivirá para siempre.",
    (37, 27): "Hijo, en tu vida pon a prueba tu alma, y mira qué le es malo, "
              "y no se lo des;",
    (37, 28): "porque no todo conviene a todos, ni toda alma se complace en "
              "todo.",
    (37, 29): "No seas insaciable en toda delicia, y no te derrames sobre los "
              "manjares;",
    (37, 30): "porque en la mucha comida habrá dolencia, y la glotonería "
              "llegará hasta el cólico.",
    (37, 31): "Por la glotonería muchos murieron; pero el que se guarda "
              "prolongará su vida.",

    # Capítulo 38
    (38, 1): "Honra al médico con los honores que le son debidos, según la "
             "necesidad, porque también a él lo creó el Señor;",
    (38, 2): "porque del Altísimo viene la curación, y del rey recibirá "
             "dádivas.",
    (38, 3): "La ciencia del médico le hará levantar la cabeza, y delante de "
             "los magnates será admirado.",
    (38, 4): "El Señor creó de la tierra los remedios, y el hombre prudente "
             "no los desdeñará.",
    (38, 5): "¿No fue endulzada el agua con un leño, ⁽⁶⁾ para que se "
             "conociera su virtud?",
    (38, 6): "Y él dio a los hombres la ciencia, para ser glorificado en sus "
             "maravillas.",
    (38, 7): "Con ellas cura y quita el dolor;",
    (38, 8): "el perfumista hace con ellas sus mezclas; y no tendrán fin sus "
             "obras, ⁽⁸⁾ y la paz viene de él sobre la faz de la tierra.",
    (38, 9): "Hijo, en tu enfermedad no te descuides, sino ruega al Señor, y "
             "él te sanará.",
    (38, 10): "Aparta el pecado y endereza tus manos, y limpia el corazón de "
              "todo pecado.",
    (38, 11): "Ofrece suave olor y el memorial de flor de harina, y haz "
              "pingüe la ofrenda, como si ya no hubieras de existir.",
    (38, 12): "Y da lugar al médico, ⁽¹²⁾ porque también a él lo creó el "
              "Señor; y no se aparte de ti, porque también lo necesitas.",
    (38, 13): "Hay tiempo en que en sus manos está el buen éxito;",
    (38, 14): "porque también ellos rogarán al Señor que les conceda dar "
              "alivio y curación para conservar la vida.",
    (38, 15): "El que peca delante del que lo hizo, caiga en manos del "
              "médico.",
    (38, 16): "Hijo, derrama lágrimas sobre el muerto, y como quien padece "
              "cosas terribles comienza el lamento; y según lo que le "
              "corresponde amortaja su cuerpo, y no descuides su sepultura.",
    (38, 17): "Haz amargo el llanto y ardiente el duelo, ⁽¹⁸⁾ y guarda luto "
              "según lo que él merece, un día o dos, para evitar la "
              "murmuración; y después consuélate de tu tristeza;",
    (38, 18): "porque de la tristeza sale la muerte, y la tristeza del "
              "corazón doblega la fuerza.",
    (38, 19): "En la desgracia permanece también la tristeza, y la vida del "
              "pobre es contra el corazón.",
    (38, 20): "No entregues tu corazón a la tristeza; apártala, acordándote "
              "de las postrimerías.",
    (38, 21): "No lo olvides, porque no hay regreso; a él no le aprovecharás, "
              "y a ti mismo te harás daño.",
    (38, 22): "Acuérdate de que su sentencia será también la tuya: a mí ayer, "
              "y a ti hoy.",
    (38, 23): "Cuando el muerto reposa, deja reposar su memoria, y consuélate "
              "de él cuando su espíritu se ha ido.",
    (38, 24): "La sabiduría del escriba se adquiere en la oportunidad del "
              "ocio, y el que tiene poca ocupación se hará sabio.",
    (38, 25): "¿Cómo se hará sabio ⁽²⁶⁾ el que empuña el arado y se gloría en "
              "el asta de la aguijada, el que guía los bueyes y anda metido "
              "en sus trabajos, y cuya conversación es de novillos?",
    (38, 26): "Pone su corazón en abrir surcos, y su desvelo en el forraje de "
              "las novillas.",
    (38, 27): "Así todo artesano y maestro de obras, que pasa la noche como "
              "el día; los que graban las figuras de los sellos, y su "
              "paciencia está en variar el dibujo; pone su corazón en "
              "reproducir la pintura, y su desvelo en acabar la obra.",
    (38, 28): "Así el herrero, sentado junto al yunque y atento al hierro sin "
              "labrar: el vapor del fuego le reseca las carnes, y en el calor "
              "del horno pelea; ⁽³⁰⁾ el ruido del martillo le aturde el oído, "
              "y sus ojos están fijos en el modelo de la pieza; ⁽³¹⁾ pone su "
              "corazón en acabar las obras, y su desvelo en pulirlas hasta el "
              "fin.",
    (38, 29): "Así el alfarero, sentado en su obra y haciendo girar con sus "
              "pies la rueda, que está siempre con cuidado por su obra, y "
              "toda su labor es por número;",
    (38, 30): "con su brazo modela el barro, y ante sus pies doblega su "
              "fuerza; ⁽³⁴⁾ pone su corazón en acabar el barniz, y su desvelo "
              "en limpiar el horno.",
    (38, 31): "Todos éstos confían en sus manos, y cada uno es sabio en su "
              "oficio.",
    (38, 32): "Sin ellos no se edificará ciudad, ⁽³⁷⁾ ni se habitará en ella "
              "ni se andará por ella;",
    (38, 33): "pero en la asamblea no sobresaldrán, y no entenderán el pacto "
              "del juicio; ⁽³⁸⁾ en la silla del juez no se sentarán, ni "
              "declararán la justicia y el derecho, y no se hallarán entre "
              "los que dicen parábolas;",
    (38, 34): "sino que sostienen la creación del mundo, y su oración está en "
              "el ejercicio de su oficio. No así el que entrega su alma y "
              "medita en la ley del Altísimo:",

    # Capítulo 39
    (39, 1): "buscará la sabiduría de todos los antiguos, y se ocupará en las "
             "profecías;",
    (39, 2): "guardará las narraciones de los varones famosos, y penetrará en "
             "los giros de las parábolas;",
    (39, 3): "buscará los secretos de los proverbios, y se ocupará en los "
             "enigmas de las parábolas.",
    (39, 4): "Servirá en medio de los magnates, y aparecerá delante del que "
             "gobierna; ⁽⁵⁾ viajará por la tierra de naciones extrañas, "
             "porque ha probado el bien y el mal entre los hombres.",
    (39, 5): "Pondrá su corazón en madrugar hacia el Señor que lo hizo, y "
             "suplicará delante del Altísimo; ⁽⁷⁾ abrirá su boca en oración, "
             "y pedirá por sus pecados.",
    (39, 6): "Si el Señor, el grande, lo quiere, será lleno de espíritu de "
             "inteligencia; ⁽⁹⁾ él derramará como lluvia palabras de "
             "sabiduría, y en la oración alabará al Señor;",
    (39, 7): "⁷ él dirigirá su consejo y su ciencia, y meditará en sus "
             "misterios;",
    (39, 8): "él dará a conocer la instrucción de su enseñanza, y se gloriará "
             "en la ley del pacto del Señor.",
    (39, 9): "Muchos alabarán su inteligencia, y jamás será borrada; ⁽¹³⁾ no "
             "se apartará su memoria, y su nombre vivirá de generación en "
             "generación.",
    (39, 10): "Las naciones contarán su sabiduría, y la asamblea anunciará su "
              "alabanza.",
    (39, 11): "Si permanece, dejará un nombre mayor que mil; y si descansa, "
              "eso le basta.",
    (39, 12): "Aún diré más, después de haberlo meditado, porque estoy lleno "
              "como la luna llena.",
    (39, 13): "Escuchadme, hijos santos, y floreced como la rosa que crece "
              "junto a la corriente del campo;",
    (39, 14): "y como el incienso dad olor suave, ⁽¹⁹⁾ y echad flor como el "
              "lirio; esparcid fragancia y cantad un cántico; bendecid al "
              "Señor por todas sus obras;",
    (39, 15): "dad magnificencia a su nombre, y confesadlo con su alabanza, "
              "con cánticos de los labios y con cítaras; y así diréis en "
              "vuestra alabanza:",
    (39, 16): "Las obras del Señor son todas en gran manera buenas, y todo "
              "mandato suyo se cumplirá a su tiempo.",
    (39, 17): "No hay por qué decir: ¿Qué es esto? ¿Para qué es esto? porque "
              "todo será buscado a su tiempo. ⁽²²⁾ A su palabra se detuvo el "
              "agua como un montón, y a la palabra de su boca, los depósitos "
              "de las aguas.",
    (39, 18): "Por su mandato se cumple todo su beneplácito, y no hay quien "
              "pueda menguar su salvación.",
    (39, 19): "Las obras de toda carne están delante de él, y no es posible "
              "esconderse de sus ojos.",
    (39, 20): "Desde la eternidad hasta la eternidad mira, y nada hay "
              "maravilloso delante de él.",
    (39, 21): "No hay por qué decir: ¿Qué es esto? ¿Para qué es esto? porque "
              "todas las cosas fueron creadas para su uso.",
    (39, 22): "Su bendición cubrió como un río, ⁽²⁸⁾ y como un diluvio empapó "
              "la tierra seca;",
    (39, 23): "así heredarán las naciones su ira, ⁽²⁹⁾ como cuando convirtió "
              "las aguas en salmuera.",
    (39, 24): "Sus caminos son rectos para los santos, y asimismo tropiezos "
              "para los inicuos.",
    (39, 25): "Los bienes fueron creados desde el principio para los buenos, "
              "y asimismo los males para los pecadores.",
    (39, 26): "Lo principal de todo lo que es necesario para la vida del "
              "hombre: agua, fuego y hierro y sal, y flor de harina de trigo, "
              "y miel y leche, sangre de uva y aceite y vestido.",
    (39, 27): "Todas estas cosas son para bien de los piadosos, y asimismo "
              "para los pecadores se volverán en mal.",
    (39, 28): "Hay vientos que fueron creados para castigo, y en su furor "
              "endurecen sus azotes; ⁽³⁴⁾ y en el tiempo de la consumación "
              "derraman su fuerza, y aplacan el furor del que los hizo.",
    (39, 29): "Fuego y granizo, hambre y muerte, todas estas cosas fueron "
              "creadas para castigo;",
    (39, 30): "los dientes de las fieras, y los escorpiones y las víboras, y "
              "la espada que castiga a los impíos para destrucción;",
    (39, 31): "se alegrarán en su mandamiento, y estarán preparados sobre la "
              "tierra para cuando se necesiten, y a su tiempo no traspasarán "
              "su palabra.",
    (39, 32): "Por eso desde el principio me afirmé, y lo medité, y lo dejé "
              "por escrito:",
    (39, 33): "Las obras del Señor son todas buenas, y a toda necesidad "
              "proveerá en su hora;",
    (39, 34): "y no hay por qué decir: Esto es peor que aquello, porque todo "
              "será aprobado a su tiempo.",
    (39, 35): "Y ahora, con todo el corazón y con la boca, cantad himnos, y "
              "bendecid el nombre del Señor.",

    # Capítulo 40
    (40, 1): "Gran afán fue creado para todo hombre, y yugo pesado sobre los "
             "hijos de Adán, desde el día en que salen del vientre de su "
             "madre hasta el día en que vuelven a la madre de todos:",
    (40, 2): "sus pensamientos y el temor del corazón, la imaginación de lo "
             "que aguardan, el día de la muerte;",
    (40, 3): "desde el que se sienta en trono de gloria hasta el humillado en "
             "tierra y ceniza,",
    (40, 4): "desde el que viste de jacinto y lleva corona hasta el que se "
             "cubre de lino crudo:",
    (40, 5): "furor y celos y turbación e inquietud, y temor de la muerte, y "
             "rencor y contienda; ⁽⁵⁾ y en el tiempo del descanso, sobre el "
             "lecho, el sueño de la noche le trastorna el entendimiento.",
    (40, 6): "Poco, casi nada, es su descanso, y después, en sueños, como en "
             "día de guardia, ⁽⁷⁾ se turba con la visión de su corazón, como "
             "el que huye de delante de la batalla;",
    (40, 7): "en el momento de ponerse a salvo despierta, y se maravilla de "
             "que no hubiera nada que temer.",
    (40, 8): "Así con toda carne, desde el hombre hasta la bestia, y sobre "
             "los pecadores siete veces más que esto:",
    (40, 9): "muerte y sangre y contienda y espada,",
    (40, 10): "contra los inicuos fueron creadas todas estas cosas, y por "
              "causa de ellos vino el diluvio.",
    (40, 11): "Todo lo que viene de la tierra vuelve a la tierra, y lo que "
              "viene de las aguas retorna al mar.",
    (40, 12): "Todo soborno e injusticia será borrado, y la fidelidad "
              "permanecerá para siempre.",
    (40, 13): "Las riquezas de los injustos se secarán como un río, y como un "
              "gran trueno en la lluvia resonarán y pasarán.",
    (40, 14): "Cuando él abre las manos se alegrará; así los transgresores "
              "desfallecerán del todo.",
    (40, 15): "Los retoños de los impíos no multiplicarán sus ramas, y son "
              "raíces impuras sobre peña escarpada;",
    (40, 16): "el junco que crece junto a toda agua y a la orilla del río "
              "será arrancado antes que toda hierba.",
    (40, 17): "La bondad es como un paraíso de bendiciones, y la limosna "
              "permanece para siempre.",
    (40, 18): "La vida del que se basta a sí mismo y del trabajador será "
              "dulce, y más que ambos el que halla un tesoro.",
    (40, 19): "Los hijos y la fundación de una ciudad afirman el nombre, y "
              "más que ambos es estimada la mujer intachable.",
    (40, 20): "El vino y la música alegran el corazón, y más que ambos el "
              "amor de la sabiduría.",
    (40, 21): "La flauta y el salterio hacen dulce la melodía, y más que "
              "ambos la lengua suave.",
    (40, 22): "La gracia y la belleza deseará tu ojo, y más que ambas el "
              "verdor de la sementera.",
    (40, 23): "El amigo y el compañero se encuentran a su tiempo, y más que "
              "ambos la mujer con su marido.",
    (40, 24): "Los hermanos y el socorro son para el tiempo de la aflicción, "
              "y más que ambos libra la limosna.",
    (40, 25): "El oro y la plata afirman el pie, y más que ambos es estimado "
              "el consejo.",
    (40, 26): "Las riquezas y la fuerza exaltan el corazón, y más que ambas "
              "el temor del Señor; ⁽²⁷⁾ en el temor del Señor no hay mengua, "
              "y con él no hay que buscar otro socorro.",
    (40, 27): "El temor del Señor es como un paraíso de bendición, y lo "
              "cubrieron por encima de toda gloria.",
    (40, 28): "Hijo, no vivas vida de mendigo; más vale morir que mendigar.",
    (40, 29): "El hombre que mira a la mesa ajena, su vida no se cuenta como "
              "vida; mancha su alma con manjares ajenos; ⁽³¹⁾ pero el hombre "
              "entendido e instruido se guardará de ello.",
    (40, 31): "En la boca del desvergonzado será dulce el mendigar, pero en "
              "su vientre arderá un fuego.",

    # Capítulo 41
    (41, 1): "¡Oh muerte, cuán amargo es tu recuerdo para el hombre que vive "
             "en paz en medio de sus bienes, ⁽²⁾ para el varón sin cuidados, "
             "a quien todo le sale bien y que aún tiene fuerzas para tomar "
             "alimento!",
    (41, 2): "¡Oh muerte, buena es tu sentencia para el hombre necesitado y "
             "falto de fuerzas, ⁽⁴⁾ muy anciano y agobiado por todas las "
             "cosas, rebelde y que ha perdido la paciencia!",
    (41, 3): "No temas la sentencia de la muerte; acuérdate de los que fueron "
             "antes de ti y de los que vendrán después.",
    (41, 4): "Ésta es la sentencia del Señor sobre toda carne; ⁽⁶⁾ ¿y por qué "
             "rechazas el beneplácito del Altísimo? Sean diez, o cien, o mil "
             "años, ⁽⁷⁾ en el Hades no se piden cuentas de la vida.",
    (41, 5): "Hijos abominables son los hijos de los pecadores, y los que "
             "frecuentan las moradas de los impíos.",
    (41, 6): "La herencia de los hijos de los pecadores perecerá, y con su "
             "descendencia persistirá el oprobio.",
    (41, 7): "Al padre impío lo culparán sus hijos, porque por causa de él "
             "serán afrentados.",
    (41, 8): "¡Ay de vosotros, hombres impíos, que abandonasteis la ley del "
             "Dios Altísimo!",
    (41, 9): "Si nacéis, para maldición naceréis; y si morís, la maldición "
             "será vuestra porción.",
    (41, 10): "Todo lo que es de la tierra volverá a la tierra; así los "
              "impíos, de la maldición a la perdición.",
    (41, 11): "El duelo de los hombres es por sus cuerpos, pero el nombre de "
              "los pecadores, que no es bueno, será borrado.",
    (41, 12): "Cuida de tu nombre, porque él te permanecerá más que mil "
              "grandes tesoros de oro.",
    (41, 13): "La vida buena tiene contados sus días, pero el buen nombre "
              "permanece para siempre.",
    (41, 14): "Guardad la instrucción en paz, hijos; sabiduría escondida y "
              "tesoro que no se ve, ¿qué provecho hay en ninguno de los dos?",
    (41, 15): "Mejor es el hombre que esconde su necedad que el hombre que "
              "esconde su sabiduría.",
    (41, 16): "Por tanto, tened vergüenza conforme a mi palabra; ⁽²⁰⁾ porque "
              "no es bueno guardar toda clase de vergüenza, ni todas las "
              "cosas son aprobadas por todos en verdad.",
    (41, 17): "Avergonzaos ante el padre y la madre de la fornicación, y ante "
              "el que gobierna y el poderoso, de la mentira;",
    (41, 18): "ante el juez y el magistrado, del delito; ante la congregación "
              "y el pueblo, de la iniquidad; ⁽²³⁾ ante el compañero y el "
              "amigo, de la injusticia;",
    (41, 19): "y ante el lugar donde habitas, ⁽²⁴⁾ del robo; y ante la verdad "
              "de Dios y el pacto; y de apoyar el codo sobre los panes; del "
              "desdén al recibir y al dar;",
    (41, 20): "y ante los que te saludan, del silencio; de mirar a la mujer "
              "ramera;",
    (41, 21): "y de apartar el rostro de tu pariente; de quitar la porción y "
              "el don; ⁽²⁷⁾ y de fijar los ojos en la mujer casada;",
    (41, 22): "de entrometerte con su criada —y no te acerques a su lecho—; "
              "⁽²⁸⁾ ante los amigos, de palabras de afrenta —y después de "
              "dar, no afrentes—;",

    # Capítulo 42
    (42, 1): "de repetir la palabra que oíste, y de revelar palabras "
             "secretas; y así serás verdaderamente pudoroso, y hallarás "
             "gracia delante de todo hombre. De estas cosas no te "
             "avergüences, y no hagas acepción de personas para pecar:",
    (42, 2): "de la ley del Altísimo y del pacto, y del juicio para hacer "
             "justicia aun al impío;",
    (42, 3): "de la cuenta con el socio y con los compañeros de camino; de "
             "dar la herencia a los compañeros;",
    (42, 4): "de la exactitud de la balanza y de las pesas; de adquirir mucho "
             "o poco;",
    (42, 5): "de la ganancia en la venta con los mercaderes; y de la mucha "
             "corrección de los hijos, y de hacer sangrar el costado del "
             "siervo malo.",
    (42, 6): "Sobre la mujer mala es bueno el sello, ⁽⁷⁾ y donde hay muchas "
             "manos, cierra con llave;",
    (42, 7): "lo que entregues, sea por número y peso, y el dar y el recibir, "
             "todo por escrito;",
    (42, 8): "de la corrección del insensato y del necio, y del muy anciano "
             "que contiende con los jóvenes; y serás verdaderamente instruido "
             "y aprobado delante de todo viviente.",
    (42, 9): "La hija es para el padre un desvelo secreto, y el cuidado por "
             "ella le quita el sueño: en su juventud, no sea que se le pase "
             "la edad; y casada, no sea que sea aborrecida;",
    (42, 10): "en su virginidad, no sea que sea profanada y quede encinta en "
              "la casa de su padre; estando con marido, no sea que sea "
              "infiel; y casada, no sea que sea estéril.",
    (42, 11): "Sobre la hija desvergonzada refuerza la guardia, no sea que te "
              "haga objeto de burla para tus enemigos, habladuría en la "
              "ciudad y escándalo ante el pueblo, y te avergüence delante de "
              "la multitud.",
    (42, 12): "No pongas los ojos en la belleza de ningún hombre, y no te "
              "sientes en medio de las mujeres;",
    (42, 13): "porque de los vestidos sale la polilla, y de la mujer la "
              "maldad de la mujer.",
    (42, 14): "Mejor es la maldad del hombre que la mujer que hace el bien; y "
              "la mujer que avergüenza trae oprobio.",
    (42, 15): "Recordaré ahora las obras del Señor, y contaré lo que he "
              "visto: por las palabras del Señor fueron hechas sus obras.",
    (42, 16): "El sol que alumbra mira sobre todas las cosas, y de su gloria "
              "está llena su obra.",
    (42, 17): "No concedió el Señor a los santos contar todas sus maravillas, "
              "las que el Señor todopoderoso afianzó, para que el universo "
              "quedara firme en su gloria.",
    (42, 18): "Él escudriñó el abismo y el corazón, y penetró sus astucias; "
              "⁽¹⁹⁾ porque el Señor conoce toda ciencia, y miró la señal de "
              "los siglos,",
    (42, 19): "anunciando lo pasado y lo venidero, y revelando las huellas de "
              "lo escondido.",
    (42, 20): "No se le escapa ningún pensamiento, ni se le oculta una sola "
              "palabra.",
    (42, 21): "Él ordenó las grandezas de su sabiduría, porque él es antes de "
              "los siglos y por los siglos; ⁽²²⁾ nada se le ha añadido ni "
              "quitado, y no ha necesitado de consejero alguno.",
    (42, 22): "¡Cuán deseables son todas sus obras, aun lo que se ve como una "
              "chispa!",
    (42, 23): "Todas estas cosas viven y permanecen para siempre, para todos "
              "los usos, y todas obedecen.",
    (42, 24): "Todas las cosas son dobles, la una frente a la otra, y nada "
              "hizo que fuese defectuoso;",
    (42, 25): "una cosa afianza el bien de la otra; ¿y quién se saciará de "
              "contemplar su gloria?",

    # Capítulo 43
    (43, 1): "Orgullo de la altura es el firmamento de pureza, la apariencia "
             "del cielo en visión de gloria.",
    (43, 2): "El sol, cuando aparece, anuncia al salir: instrumento "
             "admirable, obra del Altísimo.",
    (43, 3): "En su mediodía reseca la tierra, y ¿quién resistirá delante de "
             "su ardor?",
    (43, 4): "El que atiza un horno trabaja en medio del ardor; ⁽⁴⁾ tres "
             "veces más abrasa el sol los montes; exhalando vapores de fuego "
             "y lanzando sus rayos, ciega los ojos.",
    (43, 5): "Grande es el Señor que lo hizo, y por sus palabras apresura su "
             "carrera.",
    (43, 6): "Y la luna, en todo, a su tiempo, para señalar los tiempos y "
             "como señal perpetua.",
    (43, 7): "De la luna viene la señal de la fiesta; es lumbrera que mengua "
             "hasta desaparecer.",
    (43, 8): "El mes lleva su nombre, y crece maravillosamente en sus "
             "cambios; ⁽⁹⁾ es instrumento de los ejércitos en lo alto, que "
             "resplandece en el firmamento del cielo.",
    (43, 9): "La hermosura del cielo es la gloria de las estrellas, adorno "
             "que alumbra en las alturas del Señor.",
    (43, 10): "Por las palabras del Santo están firmes según su orden, y no "
              "desfallecen en sus vigilias.",
    (43, 11): "Mira el arco iris, y bendice al que lo hizo; es hermosísimo en "
              "su resplandor.",
    (43, 12): "Rodeó el cielo con un círculo de gloria; las manos del "
              "Altísimo lo tendieron.",
    (43, 13): "Con su mandato hace caer aprisa la nieve, y apresura los "
              "relámpagos de su juicio.",
    (43, 14): "Por eso se abrieron los tesoros, y volaron las nubes como "
              "aves.",
    (43, 15): "En su grandeza da fuerza a las nubes, y se desmenuzan las "
              "piedras de granizo.",
    (43, 16): "Ante su mirada se estremecen los montes; por su voluntad sopla "
              "el viento del sur.",
    (43, 17): "La voz de su trueno hace temblar la tierra, y también el "
              "huracán del norte y el torbellino del viento. ⁽¹⁹⁾ Como aves "
              "que se posan esparce la nieve, y su descenso es como langosta "
              "que se asienta;",
    (43, 18): "el ojo se maravilla de la hermosura de su blancura, y el "
              "corazón se pasma de su lluvia.",
    (43, 19): "Derrama también sobre la tierra la escarcha como sal, y al "
              "helarse se vuelve puntas de espinos.",
    (43, 20): "Sopla el frío viento del norte, y se congela el hielo sobre el "
              "agua; se posa sobre toda reunión de aguas, y el agua se "
              "reviste como de coraza.",
    (43, 21): "Devora los montes y abrasa el desierto, y consume la hierba "
              "como fuego.",
    (43, 22): "Remedio de todo es la nube que viene presto; el rocío que "
              "llega tras el calor trae alegría.",
    (43, 23): "Con su designio aplacó el abismo, y plantó en él islas.",
    (43, 24): "Los que navegan el mar cuentan sus peligros, y al oírlo con "
              "nuestros oídos nos maravillamos;",
    (43, 25): "allí están también las obras extrañas y maravillosas, la "
              "variedad de todo animal, la creación de los monstruos marinos.",
    (43, 26): "Por él llega su camino a buen fin, y por su palabra todas las "
              "cosas subsisten.",
    (43, 27): "Mucho diremos, y no llegaremos al cabo; y la suma de las "
              "palabras es: Él es el todo.",
    (43, 28): "¿Dónde hallaremos fuerzas para glorificarlo? Porque él es el "
              "grande, por encima de todas sus obras.",
    (43, 29): "Temible es el Señor y grande en gran manera, y maravilloso su "
              "poder.",
    (43, 30): "Al glorificar al Señor, exaltadlo cuanto podáis, porque aún os "
              "sobrepasará; ⁽³⁴⁾ y al exaltarlo redoblad vuestras fuerzas; no "
              "os canséis, porque no llegaréis al cabo.",
    (43, 31): "¿Quién lo ha visto, para que pueda contarlo? ¿Y quién lo "
              "engrandecerá como él es?",
    (43, 32): "Muchas cosas escondidas hay mayores que éstas, porque pocas de "
              "sus obras hemos visto.",
    (43, 33): "Porque el Señor lo hizo todo, y a los piadosos dio la "
              "sabiduría. Himno de los padres.",

    # Capítulo 44
    (44, 1): "Alabemos ahora a los varones ilustres, y a nuestros padres "
             "según sus generaciones.",
    (44, 2): "Mucha gloria creó el Señor, su grandeza desde la eternidad.",
    (44, 3): "Hubo quienes dominaron en sus reinos, y varones famosos por su "
             "poder; consejeros por su inteligencia, que anunciaron en "
             "profecías;",
    (44, 4): "guías del pueblo con sus consejos, y con la inteligencia de las "
             "letras del pueblo; sabias eran las palabras de su enseñanza;",
    (44, 5): "los que buscaron melodías musicales y compusieron cantos por "
             "escrito;",
    (44, 6): "varones ricos, dotados de fuerza, que vivían en paz en sus "
             "moradas:",
    (44, 7): "todos éstos fueron glorificados en sus generaciones, y fueron "
             "la gloria de sus días.",
    (44, 8): "Hay entre ellos quienes dejaron un nombre, para que se cuenten "
             "sus alabanzas;",
    (44, 9): "y hay otros de quienes no queda memoria, y perecieron como si "
             "no hubieran existido, y fueron como si no hubieran nacido, y "
             "sus hijos después de ellos.",
    (44, 10): "Pero éstos fueron varones de misericordia, cuyas obras de "
              "justicia no han sido olvidadas;",
    (44, 11): "con su descendencia permanecerá ⁽¹²⁾ una buena herencia, sus "
              "descendientes;",
    (44, 12): "en los pactos ¹² se mantuvo firme su descendencia, ⁽¹³⁾ y sus "
              "hijos por causa de ellos;",
    (44, 13): "para siempre permanecerá su descendencia, y su gloria no será "
              "borrada.",
    (44, 14): "Sus cuerpos fueron sepultados en paz, y su nombre vive por "
              "generaciones.",
    (44, 15): "Los pueblos contarán su sabiduría, y la asamblea anunciará su "
              "alabanza.",
    (44, 16): "Henoc agradó al Señor y fue trasladado, ejemplo de "
              "arrepentimiento para las generaciones.",
    (44, 17): "Noé fue hallado perfecto y justo; en el tiempo de la ira fue "
              "rescate; ⁽¹⁸⁾ por eso quedó un remanente en la tierra cuando "
              "vino el diluvio.",
    (44, 18): "Pactos eternos fueron establecidos con él, para que no fuese "
              "borrada toda carne por el diluvio.",
    (44, 19): "Abraham fue gran padre de multitud de naciones, y no se halló "
              "otro semejante a él en la gloria;",
    (44, 20): "él guardó la ley del Altísimo, y entró en pacto con él; ⁽²¹⁾ "
              "en su carne estableció el pacto, y en la prueba fue hallado "
              "fiel.",
    (44, 21): "Por eso le aseguró con juramento que las naciones serían "
              "bendecidas en su descendencia, que lo multiplicaría como el "
              "polvo de la tierra, ⁽²³⁾ y exaltaría su descendencia como las "
              "estrellas, y les daría en herencia desde un mar hasta el otro "
              "mar, y desde el río hasta los confines de la tierra.",
    (44, 22): "Y también a Isaac se lo aseguró así, por causa de Abraham su "
              "padre: ⁽²⁵⁾ la bendición de todos los hombres y el pacto;",
    (44, 23): "y la hizo reposar sobre la cabeza de Jacob; ⁽²⁶⁾ lo reconoció "
              "en sus bendiciones, y le dio su herencia; y dividió sus "
              "porciones, y las repartió entre las doce tribus. ⁽²⁷⁾ E hizo "
              "salir de él un varón de misericordia, que halló gracia a los "
              "ojos de toda carne,",

    # Capítulo 45
    (45, 1): "Amado de Dios y de los hombres, Moisés, cuya memoria es en "
             "bendiciones.",
    (45, 2): "Lo hizo semejante en gloria a los santos, y lo engrandeció para "
             "terror de los enemigos.",
    (45, 3): "Por sus palabras hizo cesar las señales; ⁽³⁾ lo glorificó "
             "delante de los reyes; le dio mandamientos para su pueblo, y le "
             "mostró parte de su gloria.",
    (45, 4): "En su fidelidad y mansedumbre lo santificó; lo escogió de entre "
             "toda carne.",
    (45, 5): "Le hizo oír su voz, y lo introdujo en la oscuridad, ⁽⁶⁾ y le "
             "dio cara a cara los mandamientos, ley de vida y de ciencia, "
             "para enseñar a Jacob el pacto, y sus juicios a Israel.",
    (45, 6): "Ensalzó a Aarón, santo semejante a él, su hermano, de la tribu "
             "de Leví.",
    (45, 7): "Estableció con él un pacto eterno, y le dio el sacerdocio del "
             "pueblo; lo hizo dichoso con hermosos atavíos, ⁽⁹⁾ y lo ciñó con "
             "vestidura de gloria.",
    (45, 8): "Lo vistió de la perfección del esplendor, y lo afirmó con "
             "ornamentos de fortaleza, ⁽¹⁰⁾ los calzones, la túnica talar y "
             "el efod.",
    (45, 9): "Y lo rodeó de granadas, y de muchísimas campanillas de oro "
             "alrededor, ⁽¹¹⁾ para que resonara su sonido a sus pasos, para "
             "hacer oír su tañido en el templo, como memorial para los hijos "
             "de su pueblo;",
    (45, 10): "con vestidura santa, de oro y de azul y de púrpura, obra de "
              "bordador; con el pectoral del juicio y las señales de la "
              "verdad;",
    (45, 11): "de carmesí torcido, obra de artífice; con piedras preciosas "
              "grabadas como sellos, engastadas en oro, obra de lapidario, "
              "como memorial en escritura grabada, según el número de las "
              "tribus de Israel;",
    (45, 12): "una corona de oro sobre la mitra, con la inscripción del sello "
              "de santidad, gloria de honra, obra de poder, delicia de los "
              "ojos, bellamente adornada.",
    (45, 13): "Hermosas cosas; ¹³ antes de él no hubo semejantes; jamás ⁽¹⁶⁾ "
              "las vistió extranjero alguno, sino sólo sus hijos, y sus "
              "descendientes para siempre.",
    (45, 14): "Sus sacrificios serán consumidos enteramente, cada día, "
              "continuamente, dos veces.",
    (45, 15): "Moisés le llenó las manos y lo ungió con el aceite santo; ⁽¹⁹⁾ "
              "le fue por pacto eterno, a él y a su descendencia mientras "
              "duren los días del cielo, para que le ministrara y a la vez "
              "ejerciera el sacerdocio, y bendijera a su pueblo en su nombre.",
    (45, 16): "Lo escogió de entre todo viviente para ofrecer holocausto al "
              "Señor, incienso y olor grato como memorial, para hacer "
              "expiación por tu pueblo.",
    (45, 17): "Le dio en sus mandamientos autoridad sobre los estatutos de "
              "los juicios, para enseñar a Jacob los testimonios, y para "
              "iluminar a Israel con su ley.",
    (45, 18): "Se conjuraron contra él extraños, y le tuvieron envidia en el "
              "desierto, los hombres de Datán y Abiram, y la congregación de "
              "Coré, con furor e ira.",
    (45, 19): "Lo vio el Señor y no le agradó, y fueron consumidos en el "
              "furor de su ira; ⁽²⁴⁾ hizo contra ellos prodigios, para "
              "consumirlos en el fuego de su llama.",
    (45, 20): "Y añadió gloria a Aarón, y le dio heredad; le repartió las "
              "primicias de los primeros frutos, ⁽²⁶⁾ y ante todo le preparó "
              "pan en abundancia;",
    (45, 21): "porque también comen los sacrificios del Señor, que él dio a "
              "él y a su descendencia.",
    (45, 22): "Pero en la tierra del pueblo no tendrá heredad, ni tiene parte "
              "en medio del pueblo; porque tú mismo eres su parte y su "
              "heredad.",
    (45, 23): "Y Finees hijo de Eleazar es el tercero en gloria, por haber "
              "tenido celo en el temor del Señor ⁽²⁹⁾ y haberse mantenido "
              "firme cuando el pueblo se apartó, con la bondad y la prontitud "
              "de su alma; e hizo expiación por Israel.",
    (45, 24): "Por eso se estableció con él un pacto de paz, para que fuese "
              "jefe del santuario y de su pueblo, a fin de que a él y a su "
              "descendencia perteneciera la dignidad del sacerdocio para "
              "siempre.",
    (45, 25): "Y hubo también un pacto con David hijo de Isaí, de la tribu de "
              "Judá: la herencia del rey pasa sólo de hijo a hijo; la "
              "herencia de Aarón es también para su descendencia.",
    (45, 26): "Dios os dé sabiduría en vuestro corazón para juzgar a su "
              "pueblo con justicia, para que no se desvanezcan sus bienes, ni "
              "su gloria por sus generaciones.",

    # Capítulo 46
    (46, 1): "Valiente en las guerras fue Josué hijo de Nun, y sucesor de "
             "Moisés en las profecías; el cual fue, conforme a su nombre, ⁽²⁾ "
             "grande para la salvación de sus escogidos, para tomar venganza "
             "de los enemigos que se levantaban, a fin de dar a Israel su "
             "heredad.",
    (46, 2): "¡Cuán glorioso fue cuando alzó sus manos y blandió la espada "
             "contra las ciudades!",
    (46, 3): "¿Quién antes de él se mantuvo así firme? Porque el Señor mismo "
             "le traía a los enemigos.",
    (46, 4): "¿No se detuvo el sol por su mano, y un día se hizo como dos?",
    (46, 5): "Invocó al Altísimo, al Poderoso, cuando los enemigos lo "
             "apretaban por todas partes; y el gran Señor le oyó con piedras "
             "de granizo de fuerza poderosa.",
    (46, 6): "Hizo caer la guerra sobre aquella nación, y en la bajada "
             "destruyó a los que le resistían, ⁽⁸⁾ para que las naciones "
             "conocieran su armadura, que su guerra era delante del Señor; "
             "porque él siguió en pos del Poderoso.",
    (46, 7): "Y en los días de Moisés hizo misericordia, él y Caleb hijo de "
             "Jefone, oponiéndose al enemigo, apartando al pueblo del pecado "
             "y haciendo cesar la murmuración de maldad.",
    (46, 8): "Y ellos dos solos fueron salvados de entre seiscientos mil de a "
             "pie, para introducirlos en la heredad, en la tierra que fluye "
             "leche y miel.",
    (46, 9): "Y dio el Señor a Caleb fuerza, y le duró hasta la vejez, para "
             "que subiera a las alturas de la tierra; y su descendencia "
             "retuvo la heredad;",
    (46, 10): "para que vieran todos los hijos de Israel que es bueno andar "
              "en pos del Señor.",
    (46, 11): "Y los jueces, cada uno con su nombre, ⁽¹⁴⁾ aquellos cuyo "
              "corazón no fornicó y que no se apartaron del Señor: sea su "
              "memoria en bendiciones.",
    (46, 12): "Florezcan sus huesos desde su lugar, ⁽¹⁵⁾ y su nombre se "
              "renueve en los hijos de aquellos varones glorificados.",
    (46, 13): "Amado de su Señor, el profeta del Señor estableció el reino, y "
              "ungió príncipes sobre su pueblo.",
    (46, 14): "Por la ley del Señor juzgó a la congregación, y el Señor "
              "visitó a Jacob.",
    (46, 15): "Por su fidelidad fue acreditado como profeta, ⁽¹⁸⁾ y por su "
              "fidelidad fue conocido fiel en la visión.",
    (46, 16): "E invocó al Señor, al Poderoso, cuando sus enemigos lo "
              "apretaban por todas partes, con la ofrenda de un cordero de "
              "leche.",
    (46, 17): "Y tronó el Señor desde el cielo, y con gran estruendo hizo oír "
              "su voz,",
    (46, 18): "y quebrantó a los jefes de los tirios y a todos los príncipes "
              "de los filisteos.",
    (46, 19): "Y antes del tiempo de su sueño eterno dio testimonio delante "
              "del Señor y de su ungido: «Bienes, ni siquiera un par de "
              "sandalias, he tomado de hombre alguno»; y nadie le acusó.",
    (46, 20): "Y aun después de dormirse profetizó, y declaró al rey su fin, "
              "y levantó su voz desde la tierra en profecía, para borrar la "
              "iniquidad del pueblo.",

    # Capítulo 47
    (47, 1): "Y después de él se levantó Natán para profetizar en los días de "
             "David.",
    (47, 2): "Como la grosura apartada del sacrificio de paz, así fue David "
             "apartado de entre los hijos de Israel.",
    (47, 3): "Con los leones jugó como con cabritos, y con los osos como con "
             "corderos de las ovejas.",
    (47, 4): "En su juventud ⁽⁴⁾ ¿no mató al gigante, y quitó el oprobio del "
             "pueblo, ⁽⁵⁾ cuando alzó la mano con la piedra de la honda y "
             "abatió la jactancia de Goliat?",
    (47, 5): "Porque invocó al Señor, el Altísimo, y él dio fuerza a su "
             "diestra para derribar a un hombre poderoso en la guerra, y para "
             "levantar el cuerno de su pueblo.",
    (47, 6): "Así lo glorificaron por sus diez millares, y lo alabaron con "
             "las bendiciones del Señor, cuando le fue traída la diadema de "
             "gloria.",
    (47, 7): "Porque quebrantó a los enemigos de alrededor, y anonadó a los "
             "filisteos, sus adversarios; hasta hoy quebrantó su cuerno.",
    (47, 8): "En toda obra suya dio alabanza al Santo, al Altísimo, con "
             "palabras de gloria; ⁽¹⁰⁾ con todo su corazón cantó himnos, y "
             "amó al que lo hizo.",
    (47, 9): "Y puso cantores delante del altar, para endulzar con su voz los "
             "cantos.",
    (47, 10): "Dio esplendor a las fiestas, y ordenó con hermosura los "
              "tiempos hasta el cumplimiento, cuando alababan su santo nombre "
              "y desde la mañana resonaba el santuario.",
    (47, 11): "El Señor le quitó sus pecados, y ensalzó para siempre su "
              "cuerno, y le dio el pacto de los reyes y un trono de gloria en "
              "Israel.",
    (47, 12): "Después de él se levantó un hijo sabio, y por causa de él "
              "habitó en holgura.",
    (47, 13): "Salomón reinó en días de paz, a quien Dios dio reposo en "
              "derredor, para que edificara una casa a su nombre y preparara "
              "un santuario para siempre.",
    (47, 14): "¡Cuán sabio fuiste en tu juventud, ⁽¹⁶⁾ y te llenaste de "
              "inteligencia como un río!",
    (47, 15): "Tu alma cubrió la tierra, ⁽¹⁷⁾ y la llenaste de parábolas y "
              "enigmas.",
    (47, 16): "Hasta las islas lejanas llegó tu nombre, y fuiste amado en tu "
              "paz.",
    (47, 17): "Por tus cantares y proverbios y parábolas, y por tus "
              "interpretaciones, te admiraron los países.",
    (47, 18): "En el nombre del Señor Dios, que es llamado Dios de Israel, "
              "⁽²⁰⁾ amontonaste el oro como estaño, y multiplicaste la plata "
              "como plomo.",
    (47, 19): "Inclinaste tus lomos a las mujeres, y te dejaste dominar en tu "
              "cuerpo.",
    (47, 20): "Pusiste mancha en tu gloria, y profanaste tu descendencia, "
              "para traer la ira sobre tus hijos; y me dolí de tu insensatez,",
    (47, 21): "porque el reino se partió en dos, y de Efraín surgió un reino "
              "rebelde.",
    (47, 22): "Pero el Señor no abandonará su misericordia, ni dejará perecer "
              "ninguna de sus obras, ni borrará la posteridad de su escogido, "
              "ni extirpará la descendencia del que le amó; ⁽²⁵⁾ y dio a "
              "Jacob un remanente, y a David una raíz salida de él.",
    (47, 23): "Y durmió Salomón con sus padres, ⁽²⁷⁾ y dejó tras sí, de su "
              "descendencia, la locura del pueblo ⁽²⁸⁾ y al falto de "
              "entendimiento, Roboam, que apartó al pueblo con su consejo; "
              "⁽²⁹⁾ y a Jeroboam hijo de Nabat, que hizo pecar a Israel y "
              "mostró a Efraín el camino del pecado.",
    (47, 24): "Y se multiplicaron sus pecados en gran manera, ⁽³⁰⁾ hasta "
              "desterrarlos de su tierra;",
    (47, 25): "y buscaron toda maldad, hasta que vino sobre ellos la "
              "venganza.",

    # Capítulo 48
    (48, 1): "Y se levantó el profeta Elías como un fuego, y su palabra ardía "
             "como una antorcha.",
    (48, 2): "Él trajo sobre ellos el hambre, y con su celo los redujo a "
             "pocos.",
    (48, 3): "Por la palabra del Señor cerró el cielo; así hizo descender "
             "fuego tres veces.",
    (48, 4): "¡Cuán glorioso fuiste, Elías, en tus maravillas! ¿Y quién podrá "
             "gloriarse semejante a ti?",
    (48, 5): "Tú, que levantaste a un muerto de la muerte y del Hades, por la "
             "palabra del Altísimo;",
    (48, 6): "que hiciste bajar a reyes a la perdición, y a hombres ilustres "
             "de su lecho;",
    (48, 7): "que oíste en el Sinaí la reprensión, y en Horeb los juicios de "
             "venganza;",
    (48, 8): "que ungiste reyes para dar el pago, y profetas que te "
             "sucedieran;",
    (48, 9): "que fuiste arrebatado en un torbellino de fuego, en un carro de "
             "caballos de fuego;",
    (48, 10): "que fuiste designado en las reprensiones para los tiempos "
              "venideros, para apaciguar la ira antes del furor, para volver "
              "el corazón del padre al hijo, y para restablecer las tribus de "
              "Jacob.",
    (48, 11): "¹¹ Dichosos los que te vieron, y los que fueron adornados con "
              "el amor; ⁽¹²⁾ porque también nosotros viviremos con vida.",
    (48, 12): "Elías fue el que quedó cubierto en el torbellino; y Eliseo fue "
              "lleno de su espíritu; y en sus días no tembló ante ningún "
              "príncipe, y nadie lo sojuzgó.",
    (48, 13): "Ninguna palabra lo sobrepasó, y aun en el sueño de la muerte "
              "profetizó su cuerpo.",
    (48, 14): "En su vida hizo prodigios, y en su muerte fueron maravillosas "
              "sus obras.",
    (48, 15): "Con todo esto no se arrepintió el pueblo, ni se apartó de sus "
              "pecados, hasta que fueron llevados cautivos de su tierra y "
              "esparcidos por toda la tierra; ⁽¹⁷⁾ y quedó el pueblo muy "
              "reducido, y un príncipe en la casa de David.",
    (48, 16): "Algunos de ellos hicieron lo que agrada a Dios, pero otros "
              "multiplicaron los pecados.",
    (48, 17): "Ezequías fortificó su ciudad, e introdujo el agua en medio de "
              "ella; horadó con el hierro la roca, y construyó cisternas para "
              "las aguas.",
    (48, 18): "En sus días subió Senaquerib, y envió al Rabsaces, y se "
              "retiró; y alzó su mano contra Sion, y se jactó con soberbia.",
    (48, 19): "Entonces temblaron sus corazones y sus manos, y tuvieron "
              "dolores como las que dan a luz;",
    (48, 20): "e invocaron al Señor, el misericordioso, extendiendo sus manos "
              "hacia él. Y el Santo los oyó presto desde el cielo, ⁽²³⁾ y los "
              "redimió por mano de Isaías.",
    (48, 21): "Hirió el campamento de los asirios, y su ángel los destruyó.",
    (48, 22): "Porque Ezequías hizo lo que agrada al Señor, y se mantuvo "
              "firme en los caminos de David su padre, que le mandó el "
              "profeta Isaías, grande y fiel en su visión.",
    (48, 23): "En sus días retrocedió el sol, y añadió vida al rey.",
    (48, 24): "Con gran espíritu vio las cosas postreras, y consoló a los que "
              "lloraban en Sion.",
    (48, 25): "Hasta la eternidad mostró lo que había de suceder, y las cosas "
              "ocultas antes que acontecieran.",

    # Capítulo 49
    (49, 1): "La memoria de Josías es como una mezcla de incienso preparada "
             "por obra del perfumista; ⁽²⁾ en toda boca será dulce como la "
             "miel, y como la música en un banquete de vino.",
    (49, 2): "Él anduvo rectamente en la conversión del pueblo, y quitó las "
             "abominaciones de la iniquidad.",
    (49, 3): "Enderezó su corazón hacia el Señor; en los días de los impíos "
             "hizo fuerte la piedad.",
    (49, 4): "Fuera de David y de Ezequías y de Josías, todos cometieron "
             "pecado; ⁽⁶⁾ porque abandonaron la ley del Altísimo; los reyes "
             "de Judá desaparecieron.",
    (49, 5): "Porque dieron su poder a otros, y su gloria a una nación "
             "extraña.",
    (49, 6): "Ésta prendió fuego a la ciudad escogida del santuario, y "
             "dejaron desiertos sus caminos,",
    (49, 7): "por mano de Jeremías; porque lo maltrataron, a él, que desde el "
             "vientre fue consagrado profeta, para desarraigar y destruir y "
             "arruinar, y asimismo para edificar y plantar.",
    (49, 8): "Ezequiel fue el que vio la visión de gloria que le mostró sobre "
             "el carro de los querubines.",
    (49, 9): "Porque también se acordó de los enemigos en la tempestad, y de "
             "hacer bien a los que enderezan sus caminos.",
    (49, 10): "Y los huesos de los doce profetas florezcan desde su lugar; "
              "porque consolaron a Jacob, y lo redimieron con la fidelidad de "
              "la esperanza.",
    (49, 11): "¿Cómo engrandeceremos a Zorobabel? También él fue como un "
              "anillo de sello en la mano derecha.",
    (49, 12): "Así también Jesúa hijo de Josadac; los cuales en sus días "
              "edificaron la casa y levantaron al Señor un templo santo, "
              "preparado para gloria eterna.",
    (49, 13): "Y de Nehemías es grande la memoria, que nos levantó los muros "
              "caídos, y puso puertas y cerrojos, y reedificó nuestras casas.",
    (49, 14): "Nadie fue creado sobre la tierra semejante a Enoc; porque "
              "también él fue arrebatado de la tierra.",
    (49, 15): "Y José fue varón, jefe de sus hermanos, sostén del pueblo; "
              "⁽¹⁸⁾ y sus huesos fueron visitados.",
    (49, 16): "Sem y Set fueron glorificados entre los hombres, y sobre todo "
              "viviente en la creación está Adán.",

    # Capítulo 50
    (50, 1): "Simón hijo de Onías, el sumo sacerdote, que en su vida reparó "
             "la casa, y en sus días fortificó el templo.",
    (50, 2): "Por él fue cimentada la altura doble, el alto contrafuerte del "
             "recinto del templo.",
    (50, 3): "En sus días fue excavado el depósito de las aguas, un estanque "
             "de bronce, cuyo contorno era como el de un mar.",
    (50, 4): "Él cuidó de su pueblo para librarlo de la ruina, y fortificó la "
             "ciudad contra el asedio.",
    (50, 5): "¡Cuán glorioso era, rodeado del pueblo, cuando salía de la casa "
             "del velo!",
    (50, 6): "Como el lucero de la mañana en medio de las nubes, como la luna "
             "llena en sus días;",
    (50, 7): "como el sol que resplandece sobre el templo del Altísimo, y "
             "como el arco que brilla entre las nubes de gloria;",
    (50, 8): "como la flor de los rosales en los días de primavera, como los "
             "lirios junto a las corrientes de agua, como el retoño del "
             "incienso en los días del verano;",
    (50, 9): "como el fuego y el incienso en el incensario; ⁽¹⁰⁾ como un vaso "
             "de oro macizo, adornado con toda piedra preciosa;",
    (50, 10): "como el olivo que brota cargado de fruto, y como el ciprés que "
              "se eleva hasta las nubes.",
    (50, 11): "Cuando tomaba la vestidura de gloria y se vestía de la "
              "perfección del esplendor, ⁽¹²⁾ al subir al santo altar, "
              "glorificaba el recinto del santuario.",
    (50, 12): "Y cuando recibía las porciones de manos de los sacerdotes, "
              "estando él de pie junto al hogar del altar, con la corona de "
              "sus hermanos en derredor, como renuevos de cedro en el Líbano, "
              "⁽¹⁴⁾ lo rodeaban como troncos de palmeras;",
    (50, 13): "y todos los hijos de Aarón en su gloria, ⁽¹⁵⁾ con la ofrenda "
              "del Señor en sus manos, delante de toda la asamblea de Israel;",
    (50, 14): "y acabando el ministerio sobre los altares, para ordenar la "
              "ofrenda del Altísimo, el Todopoderoso,",
    (50, 15): "extendía su mano sobre la copa de libación, y derramaba de la "
              "sangre de la uva, ⁽¹⁷⁾ la derramaba al pie del altar, olor "
              "grato al Altísimo, Rey de todas las cosas.",
    (50, 16): "Entonces clamaban los hijos de Aarón, tocaban las trompetas de "
              "metal batido, y hacían oír un gran sonido como memorial "
              "delante del Altísimo.",
    (50, 17): "Entonces todo el pueblo a una se apresuraba, y caían rostro en "
              "tierra para adorar a su Señor, el Todopoderoso, Dios Altísimo.",
    (50, 18): "Y los cantores alababan con sus voces; en la casa colmada "
              "resonaba dulce la melodía.",
    (50, 19): "Y el pueblo rogaba al Señor Altísimo en oración delante del "
              "Misericordioso, hasta que se cumplía el culto del Señor y "
              "acababan su ministerio.",
    (50, 20): "Entonces, descendiendo, alzaba sus manos sobre toda la "
              "asamblea de los hijos de Israel, para dar con sus labios la "
              "bendición del Señor y gloriarse en su nombre;",
    (50, 21): "y por segunda vez se postraban en adoración, para recibir la "
              "bendición de parte del Altísimo.",
    (50, 22): "Y ahora bendecid todos a Dios, que hace en todo lugar grandes "
              "cosas, que exalta nuestros días desde el vientre, y obra con "
              "nosotros conforme a su misericordia.",
    (50, 23): "Él os dé alegría de corazón, y que haya paz en nuestros días "
              "en Israel, como en los días de la eternidad;",
    (50, 24): "que confíe a nosotros su misericordia, y en sus días nos "
              "redima.",
    (50, 25): "Dos naciones aborrece mi alma, y la tercera no es nación:",
    (50, 26): "los que habitan en el monte de Samaria, los filisteos, y el "
              "pueblo necio que mora en Siquem.",
    (50, 27): "Instrucción de inteligencia y de ciencia he grabado en este "
              "libro yo, Jesús hijo de Sirac Eleazar, de Jerusalén, que "
              "derramé como lluvia la sabiduría de mi corazón.",
    (50, 28): "Dichoso el que se ocupe en estas cosas; y el que las ponga en "
              "su corazón se hará sabio.",
    (50, 29): "Porque si las pone por obra, para todo será fuerte; porque la "
              "luz del Señor es su huella. ⁽¹⁾ Oración de Jesús hijo de "
              "Sirac.",

    # Capítulo 51
    (51, 1): "Te alabaré, Señor Rey, y te ensalzaré, oh Dios, Salvador mío; "
             "⁽²⁾ alabo tu nombre;",
    (51, 2): "porque fuiste mi protector y mi ayuda, ⁽³⁾ y redimiste mi "
             "cuerpo de la perdición, y del lazo de la lengua calumniadora, "
             "de los labios que obran mentira; y delante de los que estaban "
             "presentes",
    (51, 3): "fuiste mi ayuda, ³ y me redimiste, conforme a la grandeza de tu "
             "misericordia y de tu nombre, de las dentelladas de los que "
             "estaban prontos a devorarme, ⁽⁵⁾ de la mano de los que buscaban "
             "mi alma, de las muchas tribulaciones que padecí;",
    (51, 4): "de la asfixia del fuego que me cercaba, y de en medio del fuego "
             "que yo no había encendido;",
    (51, 5): "de lo profundo del vientre del Hades, y de la lengua impura y "
             "de la palabra mentirosa.",
    (51, 6): "Ante el rey, la calumnia de la lengua injusta; ⁽⁸⁾ mi alma se "
             "acercó hasta la muerte, ⁽⁹⁾ y mi vida estaba cerca del Hades "
             "abajo.",
    (51, 7): "Me rodeaban por todas partes, y no había quien me ayudara; "
             "buscaba con la mirada el socorro de los hombres, y no lo había.",
    (51, 8): "Y me acordé de tu misericordia, Señor, y de tus obras desde la "
             "eternidad, ⁽¹²⁾ que libras a los que esperan en ti y los salvas "
             "de la mano de las naciones.",
    (51, 9): "Y levanté desde la tierra mi súplica, y rogué ser librado de la "
             "muerte.",
    (51, 10): "Invoqué al Señor, Padre de mi Señor, que no me abandonara en "
              "los días de la tribulación, en el tiempo de los soberbios, "
              "cuando no hay ayuda.",
    (51, 11): "Alabaré tu nombre continuamente, y te cantaré himnos con "
              "acción de gracias; y fue escuchada mi oración.",
    (51, 12): "Porque me salvaste de la perdición, y me libraste del tiempo "
              "malo; ⁽¹⁷⁾ por eso te daré gracias y te alabaré, y bendeciré "
              "el nombre del Señor.",
    (51, 13): "Siendo aún joven, antes de andar errante, busqué abiertamente "
              "la sabiduría en mi oración.",
    (51, 14): "Delante del templo la pedía, y hasta el fin la buscaré.",
    (51, 15): "Desde la flor hasta la uva que madura ⁽²⁰⁾ se alegró mi "
              "corazón en ella; mi pie anduvo en rectitud; desde mi juventud "
              "seguí sus huellas.",
    (51, 16): "Incliné un poco mi oído y la recibí, y hallé para mí mucha "
              "instrucción.",
    (51, 17): "Tuve provecho en ella; ⁽²³⁾ al que me da la sabiduría daré "
              "gloria.",
    (51, 18): "Porque resolví ponerla por obra, y tuve celo por el bien, y no "
              "seré avergonzado.",
    (51, 19): "Mi alma ha luchado por ella, y en el cumplimiento de la ley "
              "fui diligente; ⁽²⁶⁾ extendí mis manos hacia lo alto, y lloré "
              "mi ignorancia de ella.",
    (51, 20): "Dirigí mi alma hacia ella, y con ellas adquirí corazón desde "
              "el principio, y en la pureza la hallé; por eso no seré "
              "abandonado.",
    (51, 21): "Y mis entrañas se conmovieron por buscarla; por eso adquirí "
              "una buena posesión.",
    (51, 22): "El Señor me dio una lengua como recompensa, y con ella le "
              "alabaré.",
    (51, 23): "Acercaos a mí, los que carecéis de instrucción, y morad en la "
              "casa de la instrucción.",
    (51, 24): "¿Por qué decís que os faltan estas cosas, y vuestras almas "
              "tienen tanta sed?",
    (51, 25): "Abrí mi boca y hablé: Adquiridla para vosotros sin plata.",
    (51, 26): "Poned vuestro cuello bajo el yugo, y reciba vuestra alma la "
              "instrucción; cerca está para hallarla.",
    (51, 27): "Ved con vuestros ojos que poco trabajé, y hallé para mí mucho "
              "descanso.",
    (51, 28): "Tomad parte en la instrucción, aunque sea a gran precio de "
              "plata, y con ella adquiriréis mucho oro.",
    (51, 29): "Alégrese vuestra alma en su misericordia, y no os avergoncéis "
              "de alabarle.",
    (51, 30): "Haced vuestra obra antes del tiempo, y él os dará vuestra "
              "recompensa a su tiempo.",
}
