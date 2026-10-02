"""El Pastor de Hermas, traducido del griego.

Lo escribió en Roma, a mediados del siglo II, un cristiano llamado Hermas, que
había sido esclavo. Son visiones, mandamientos y semejanzas que le comunican
una señora anciana —la Iglesia— y después un ángel vestido de pastor, el ángel
de la penitencia. Su tema es si el cristiano que peca después del bautismo
puede todavía arrepentirse, y responde que sí, una vez. Fue uno de los libros
más leídos de la iglesia antigua: el Códice Sinaítico lo copia a continuación
del Nuevo Testamento.

Los capítulos van numerados de corrido, del 1 al 114, como en las ediciones
modernas: las Visiones son 1-25, los Mandamientos 26-49 y las Semejanzas
50-114. El final se ha perdido en griego y se conoce sólo por el latín: la
fuente lo trae con letras griegas por un error de conversión, y aquí se traduce
del latín, marcado con [Latín] al principio de cada versículo.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

HERMAS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "El que me crió me vendió a una tal Rode, en Roma. Después de "
            "muchos años volví a encontrarla, y comencé a amarla como a una "
            "hermana.",
    (1, 2): "Pasado algún tiempo la vi bañándose en el río Tíber, y le tendí "
            "la mano y la saqué del río. Y viendo su hermosura, pensaba en mi "
            "corazón, diciendo: Dichoso sería yo si tuviera una mujer así, "
            "tanto en hermosura como en carácter. Sólo esto pensé, y ninguna "
            "otra cosa.",
    (1, 3): "Pasado algún tiempo, yendo yo a Cumas y glorificando las "
            "criaturas de Dios, cuán grandes y magníficas y poderosas son, "
            "mientras caminaba me quedé dormido. Y un espíritu me tomó y me "
            "llevó por un lugar sin camino, por donde hombre alguno podía "
            "transitar; y el lugar era escarpado y cortado por las aguas. "
            "Habiendo, pues, cruzado aquel río, llegué a terreno llano, y me "
            "pongo de rodillas, y comencé a orar al Señor y a confesar mis "
            "pecados.",
    (1, 4): "Y mientras yo oraba, se abrió el cielo, y veo a aquella mujer a "
            "quien yo había deseado, que me saludaba desde el cielo, "
            "diciendo: Hermas, salud.",
    (1, 5): "Y mirándola, le digo: Señora, ¿qué haces tú aquí? Y ella me "
            "respondió: Fui llevada arriba para acusar tus pecados delante "
            "del Señor.",
    (1, 6): "Le digo: ¿Eres tú ahora mi acusadora? No, dice, sino oye las "
            "palabras que te voy a decir. Dios, que habita en los cielos, y "
            "que creó de lo que no es las cosas que son, y las multiplicó y "
            "acrecentó por causa de su santa iglesia, está airado contigo, "
            "porque pecaste contra mí.",
    (1, 7): "Respondiéndole, digo: ¿Contra ti pequé? ¿En qué lugar, o cuándo "
            "te dije palabra deshonesta? ¿No te tuve siempre por diosa? ¿No "
            "te respeté siempre como a una hermana? ¿Por qué me levantas "
            "falsamente, oh mujer, estas cosas malas e impuras?",
    (1, 8): "Ella, riéndose, me dice: Subió a tu corazón el deseo de la "
            "maldad. ¿O no te parece que es cosa mala para un hombre justo "
            "que suba a su corazón el mal deseo? Pecado es, en verdad, y "
            "grande, dice. Porque el hombre justo piensa cosas justas. Y en "
            "pensar cosas justas se afirma su gloria en los cielos, y tiene "
            "propicio al Señor en todo su obrar; pero los que piensan cosas "
            "malas en sus corazones atraen sobre sí muerte y cautiverio, "
            "sobre todo los que se granjean este siglo y se jactan de sus "
            "riquezas, y no se aferran a los bienes venideros.",
    (1, 9): "Se arrepentirán sus almas, las de los que no tienen esperanza, "
            "sino que han desesperado de sí mismos y de su vida. Mas tú ora a "
            "Dios, y él sanará tus pecados, y los de toda tu casa, y los de "
            "todos los santos.",

    # Capítulo 2
    (2, 1): "Después que ella dijo estas palabras, se cerraron los cielos; y "
            "yo estaba todo estremecido y afligido. Y decía dentro de mí: Si "
            "este pecado se me apunta, ¿cómo podré ser salvo? ¿O cómo "
            "aplacaré a Dios por mis pecados consumados? ¿O con qué palabras "
            "rogaré al Señor para que me sea propicio?",
    (2, 2): "Mientras yo meditaba y discurría estas cosas en mi corazón, veo "
            "delante de mí una silla grande, blanca, hecha de lana como la "
            "nieve; y vino una mujer anciana, con vestido resplandeciente, "
            "que tenía un libro en las manos, y se sentó sola y me saluda: "
            "Hermas, salud. Y yo, afligido y llorando, dije: Señora, salud.",
    (2, 3): "Y me dijo: ¿Por qué tan sombrío, Hermas? Tú, el paciente y "
            "sosegado, el que siempre ríe, ¿por qué tan abatido de semblante "
            "y no alegre? Y yo le dije: Por causa de una mujer muy buena, que "
            "dice que pequé contra ella.",
    (2, 4): "Y ella dijo: ¡De ninguna manera tal cosa en el siervo de Dios! "
            "Pero, de cierto, subió a tu corazón acerca de ella. Para los "
            "siervos de Dios tal pensamiento acarrea pecado; porque es mal "
            "pensamiento, y asombroso, en un espíritu venerable y ya probado, "
            "el desear una obra mala; y sobre todo en Hermas el continente, "
            "el que se abstiene de todo mal deseo y está lleno de toda "
            "sencillez y de gran inocencia.",

    # Capítulo 3
    (3, 1): "Pero no es por esto por lo que Dios está airado contigo, sino "
            "para que conviertas a tu casa, que obró inicuamente contra el "
            "Señor y contra vosotros, sus padres. Mas tú, por amor a tus "
            "hijos, no amonestabas a tu casa, sino que la dejaste corromperse "
            "terriblemente; por esto está airado contigo el Señor. Pero él "
            "sanará todos los males que antes sucedieron en tu casa; porque "
            "por los pecados e iniquidades de ellos tú fuiste arruinado en "
            "los negocios de esta vida.",
    (3, 2): "Pero la gran misericordia del Señor tuvo compasión de ti y de tu "
            "casa, y te fortalecerá y te afirmará en su gloria. Tú solamente "
            "no seas negligente, sino ten buen ánimo y fortalece a tu casa. "
            "Porque así como el herrero, a fuerza de martillar su obra, "
            "consigue lo que quiere, así también la palabra justa de cada día "
            "vence toda maldad. No dejes, pues, de amonestar a tus hijos. "
            "Porque sé que, si se arrepienten de todo su corazón, serán "
            "inscritos en los libros de la vida con los santos.",
    (3, 3): "Cuando cesaron estas palabras suyas, me dice: ¿Quieres oírme "
            "leer? Digo yo: Quiero, señora. Me dice: Sé oyente, y oye las "
            "glorias de Dios. Oí cosas grandes y maravillosas, que no pude "
            "retener en la memoria; porque todas las palabras eran "
            "espantosas, que el hombre no puede soportar. Retuve, pues, las "
            "últimas palabras, porque nos eran provechosas y apacibles:",
    (3, 4): "He aquí el Dios de las potencias, a quien amo, que con fuerza "
            "poderosa y con su gran inteligencia creó el mundo, y con su "
            "glorioso consejo revistió de hermosura a su creación, y con su "
            "palabra fuerte fijó el cielo y fundó la tierra sobre las aguas, "
            "y con su propia sabiduría y providencia creó su santa iglesia, a "
            "la cual también bendijo: he aquí, él traslada los cielos, y los "
            "montes, y los collados, y los mares, y todo se hace llano para "
            "sus escogidos, para darles la promesa que prometió con mucha "
            "gloria y gozo, si guardan los preceptos de Dios que recibieron "
            "con gran fe.",

    # Capítulo 4
    (4, 1): "Cuando, pues, acabó de leer y se levantó de la silla, vinieron "
            "cuatro jóvenes y alzaron la silla y se fueron hacia el oriente.",
    (4, 2): "Y ella me llama, y me tocó el pecho, y me dice: ¿Te agradó mi "
            "lectura? Y le digo: Señora, estas últimas cosas me agradan, pero "
            "las primeras son difíciles y duras. Y ella me habló diciendo: "
            "Estas últimas son para los justos, y las primeras para los "
            "gentiles y para los apóstatas.",
    (4, 3): "Mientras ella hablaba conmigo, aparecieron dos hombres, y la "
            "tomaron de los brazos y se fueron hacia el oriente, adonde había "
            "ido la silla. Y ella se fue alegre, y al irse me dice: Pórtate "
            "varonilmente, Hermas.",

    # Capítulo 5
    (5, 1): "Yendo yo a Cumas por el mismo tiempo que el año anterior, "
            "mientras caminaba me acordé de la visión del año pasado; y otra "
            "vez me toma un espíritu y me lleva al mismo lugar que el año "
            "anterior.",
    (5, 2): "Llegado, pues, al lugar, me pongo de rodillas y comencé a orar "
            "al Señor y a glorificar su nombre, porque me tuvo por digno y me "
            "dio a conocer mis pecados de antes.",
    (5, 3): "Y después que me levanté de la oración, veo delante de mí a la "
            "anciana que había visto el año anterior, que caminaba y leía un "
            "librito, y me dice: ¿Puedes anunciar estas cosas a los escogidos "
            "de Dios? Le digo: Señora, no puedo recordar tantas cosas; pero "
            "dame el librito para que lo copie. Tómalo, dice, y me lo "
            "devolverás.",
    (5, 4): "Lo tomé yo, y retirándome a cierto lugar del campo, lo copié "
            "todo letra por letra, porque no hallaba las sílabas. Y cuando "
            "hube acabado las letras del librito, de repente me fue "
            "arrebatado de la mano el librito; mas por quién, no lo vi.",

    # Capítulo 6
    (6, 1): "Y después de quince días, habiendo yo ayunado y rogado mucho al "
            "Señor, me fue revelado el conocimiento de lo escrito. Y estaba "
            "escrito esto:",
    (6, 2): "Tu descendencia, Hermas, ha desechado a Dios, y ha blasfemado "
            "contra el Señor, y ha traicionado a sus padres con gran maldad, "
            "y han sido llamados traidores de sus padres, y habiendo "
            "traicionado no sacaron provecho, sino que aún añadieron a sus "
            "pecados las lascivias y las mezclas de maldad; y así se colmaron "
            "sus iniquidades.",
    (6, 3): "Pero da a conocer estas palabras a todos tus hijos, y a tu "
            "compañera, que ha de ser tu hermana; porque también ella no "
            "refrena la lengua, con la cual obra mal; pero oyendo estas "
            "palabras se refrenará y alcanzará misericordia.",
    (6, 4): "Después que les hayas dado a conocer estas palabras, que el "
            "Soberano me mandó que te fueran reveladas, entonces les son "
            "perdonados todos los pecados que antes pecaron, y a todos los "
            "santos que han pecado hasta este día, si se arrepienten de todo "
            "corazón y quitan de su corazón las dudas.",
    (6, 5): "Porque el Soberano juró por su gloria acerca de sus escogidos: "
            "que si, fijado este día, todavía hubiere pecado, no tendrán "
            "salvación; porque el arrepentimiento para los justos tiene "
            "término: se han cumplido los días del arrepentimiento para todos "
            "los santos; mas para los gentiles hay arrepentimiento hasta el "
            "último día.",
    (6, 6): "Dirás, pues, a los que presiden la iglesia que enderecen sus "
            "caminos en justicia, para que reciban en plenitud las promesas "
            "con mucha gloria.",
    (6, 7): "Perseverad, pues, los que obráis la justicia, y no dudéis, para "
            "que vuestro tránsito sea con los santos ángeles. Bienaventurados "
            "vosotros cuantos soportáis la gran tribulación que viene, y "
            "cuantos no negarán su vida.",
    (6, 8): "Porque el Señor juró por su Hijo que los que negaren a su Cristo "
            "han sido desechados de su vida, esto es, los que ahora van a "
            "negarle en los días venideros; mas a los que antes le negaron, "
            "por su gran misericordia les ha sido propicio.",

    # Capítulo 7
    (7, 1): "Mas tú, Hermas, no guardes ya rencor a tus hijos, ni abandones a "
            "tu hermana, para que sean limpiados de sus pecados anteriores. "
            "Porque serán corregidos con justa corrección, si tú no les "
            "guardas rencor. El rencor obra muerte. Y tú, Hermas, tuviste "
            "grandes tribulaciones personales por las transgresiones de tu "
            "casa, porque no te cuidaste de ellos; sino que te descuidaste, y "
            "te enredaste en tus malos negocios.",
    (7, 2): "Pero te salva el no haberte apartado del Dios vivo, y tu "
            "sencillez y tu mucha continencia; estas cosas te han salvado, si "
            "perseveras, y salvan a todos los que obran tales cosas y andan "
            "en inocencia y sencillez. Estos prevalecerán sobre toda maldad y "
            "permanecerán para la vida eterna.",
    (7, 3): "Bienaventurados todos los que obran la justicia. No perecerán "
            "jamás.",
    (7, 4): "Y dirás a Máximo: He aquí viene tribulación; si te parece bien, "
            "niega otra vez. Cercano está el Señor a los que se convierten, "
            "como está escrito en Eldad y Modat, que profetizaron al pueblo "
            "en el desierto.",

    # Capítulo 8
    (8, 1): "Y me fue revelado, hermanos, mientras dormía, por un joven "
            "hermosísimo, que me decía: La anciana de quien recibiste el "
            "librito, ¿quién piensas que es? Yo digo: La Sibila. Te engañas, "
            "dice, no lo es. ¿Quién es, pues?, digo. La Iglesia, dice. Le "
            "dije: ¿Por qué, pues, es anciana? Porque, dice, fue creada antes "
            "que todas las cosas; por eso es anciana; y por causa de ella fue "
            "formado el mundo.",
    (8, 2): "Y después vi una visión en mi casa. Vino la anciana y me "
            "preguntó si ya había dado el libro a los presbíteros. Dije que "
            "no lo había dado. Bien has hecho, dice, porque tengo palabras "
            "que añadir. Cuando, pues, acabe todas las palabras, por medio de "
            "ti serán dadas a conocer a todos los escogidos.",
    (8, 3): "Escribirás, pues, dos libritos, y enviarás uno a Clemente y otro "
            "a Grapte. Y Clemente lo enviará a las ciudades de fuera, porque "
            "a él le ha sido encomendado; y Grapte amonestará a las viudas y "
            "a los huérfanos. Y tú lo leerás en esta ciudad con los "
            "presbíteros que presiden la iglesia.",

    # Capítulo 9
    (9, 1): "La que vi, hermanos, fue de esta manera.",
    (9, 2): "Habiendo ayunado muchas veces y rogado al Señor que me "
            "manifestase la revelación que me había prometido mostrar por "
            "medio de aquella anciana, esa misma noche se me apareció la "
            "anciana y me dijo: Ya que estás tan necesitado y tan deseoso de "
            "conocerlo todo, ve al campo donde cultivas espelta, y hacia la "
            "hora quinta me manifestaré a ti y te mostraré lo que debes ver.",
    (9, 3): "Le pregunté diciendo: Señora, ¿a qué lugar del campo? Donde "
            "quieras, dice. Escogí un lugar hermoso y apartado. Pero antes de "
            "hablarle y decirle el lugar, me dice: Iré allí donde tú quieras.",
    (9, 4): "Fui, pues, hermanos, al campo, y conté las horas, y llegué al "
            "lugar donde le había señalado que viniese, y veo un banco de "
            "marfil puesto allí, y sobre el banco había un cojín de lino, y "
            "encima un paño de lino fino extendido.",
    (9, 5): "Viendo estas cosas allí puestas, y que no había nadie en el "
            "lugar, quedé asombrado, y como un temblor se apoderó de mí, y se "
            "me erizaron los cabellos; y como un espanto me sobrevino, "
            "estando yo solo. Volviendo, pues, en mí, y acordándome de la "
            "gloria de Dios, y cobrando ánimo, me puse de rodillas y "
            "confesaba otra vez mis pecados al Señor, como también antes.",
    (9, 6): "Y ella vino con seis jóvenes, a los que también antes había "
            "visto, y se puso junto a mí, y escuchaba atentamente mientras yo "
            "oraba y confesaba mis pecados al Señor. Y tocándome, dice: "
            "Hermas, deja ya de pedir en todo por tus pecados; pide también "
            "por la justicia, para que recibas alguna parte de ella para tu "
            "casa.",
    (9, 7): "Y me levanta de la mano, y me lleva al banco, y dice a los "
            "jóvenes: Id y edificad.",
    (9, 8): "Y después que los jóvenes se retiraron y quedamos solos, me "
            "dice: Siéntate aquí. Le digo: Señora, deja que los presbíteros "
            "se sienten primero. Lo que te digo, dice, siéntate.",
    (9, 9): "Queriendo yo, pues, sentarme a la parte derecha, no me dejó, "
            "sino que me hace señal con la mano para que me siente a la parte "
            "izquierda. Y estando yo pensativo y afligido porque no me dejó "
            "sentarme a la parte derecha, me dice: ¿Te entristeces, Hermas? "
            "El lugar de la parte derecha es de otros, de los que ya "
            "agradaron a Dios y padecieron por causa del Nombre; y a ti te "
            "falta mucho para sentarte con ellos. Pero así como permaneces en "
            "tu sencillez, permanece, y te sentarás con ellos, tú y cuantos "
            "obren las obras de ellos y soporten lo que también ellos "
            "soportaron.",

    # Capítulo 10
    (10, 1): "¿Qué soportaron?, digo. Oye, dice: azotes, cárceles, grandes "
             "tribulaciones, cruces, fieras, por causa del Nombre. Por esto "
             "de ellos es la parte derecha del santuario, y de todo aquel que "
             "padezca por el Nombre; y de los demás es la parte izquierda. "
             "Pero de ambos, de los que se sientan a la derecha y de los que "
             "se sientan a la izquierda, son los mismos dones y las mismas "
             "promesas; sólo que aquéllos se sientan a la derecha y tienen "
             "cierta gloria.",
    (10, 2): "Y tú deseas ardientemente sentarte a la derecha con ellos, pero "
             "tus faltas son muchas. Mas serás limpiado de tus faltas; y "
             "todos los que no duden serán limpiados de todos los pecados "
             "hasta este día.",
    (10, 3): "Dicho esto, quería irse; pero cayendo yo a sus pies, le rogué "
             "por el Señor que me mostrase la visión que había prometido.",
    (10, 4): "Y ella otra vez me tomó de la mano, y me levanta, y me sienta "
             "en el banco a la izquierda; y ella misma se sentaba a la "
             "derecha. Y alzando una vara resplandeciente, me dice: ¿Ves una "
             "cosa grande? Le digo: Señora, nada veo. Me dice: Tú, mira, ¿no "
             "ves delante de ti una gran torre que se edifica sobre las "
             "aguas, con piedras cuadradas resplandecientes?",
    (10, 5): "Y la torre se edificaba en cuadro por los seis jóvenes que "
             "habían venido con ella; y otros millares de hombres traían "
             "piedras, unos de lo profundo, otros de la tierra, y las "
             "entregaban a los seis jóvenes; y ellos las tomaban y "
             "edificaban.",
    (10, 6): "Las piedras sacadas de lo profundo las ponían todas, tal como "
             "estaban, en el edificio, porque estaban ajustadas y concordaban "
             "en su juntura con las otras; y de tal manera se unían unas con "
             "otras que no se veía su juntura. Y el edificio de la torre "
             "parecía como edificado de una sola piedra.",
    (10, 7): "De las otras piedras que se traían de la tierra seca, a unas "
             "las desechaban, a otras las ponían en el edificio, y a otras "
             "las hacían pedazos y las arrojaban lejos de la torre.",
    (10, 8): "Y muchas otras piedras yacían alrededor de la torre, y no las "
             "usaban para el edificio; porque algunas de ellas estaban "
             "roñosas, otras tenían grietas, otras estaban mutiladas, y otras "
             "eran blancas y redondas, y no se ajustaban al edificio.",
    (10, 9): "Y veía otras piedras arrojadas lejos de la torre, que venían al "
             "camino y no se quedaban en el camino, sino que rodaban del "
             "camino a lugares sin camino; y otras que caían en el fuego y se "
             "quemaban; y otras que caían cerca de las aguas y no podían "
             "rodar al agua, aunque querían rodar y llegar al agua.",

    # Capítulo 11
    (11, 1): "Habiéndome mostrado estas cosas, quería irse deprisa. Le digo: "
             "Señora, ¿de qué me sirve haber visto estas cosas y no saber qué "
             "significan? Respondiéndome, dice: Hombre astuto eres, que "
             "quieres saber lo tocante a la torre. Sí, digo, señora, para "
             "anunciarlo a los hermanos, y para que se alegren más, y oyendo "
             "estas cosas conozcan al Señor en mucha gloria.",
    (11, 2): "Y ella dijo: Muchos lo oirán; y oyéndolo, algunos de ellos se "
             "gozarán, y otros llorarán; pero también éstos, si oyen y se "
             "arrepienten, también ellos se gozarán. Oye, pues, las parábolas "
             "de la torre, porque te lo revelaré todo. Y no me des ya más "
             "molestias acerca de revelaciones, porque estas revelaciones "
             "tienen fin, pues están cumplidas. Pero no cesarás de pedir "
             "revelaciones, porque eres importuno.",
    (11, 3): "La torre que ves edificarse soy yo, la Iglesia, que se te ha "
             "aparecido ahora y antes. Pregunta, pues, lo que quieras acerca "
             "de la torre, y te lo revelaré, para que te goces con los "
             "santos.",
    (11, 4): "Le digo: Señora, ya que una vez me tuviste por digno de "
             "revelármelo todo, revélamelo. Y ella me dice: Lo que pueda "
             "serte revelado, te será revelado. Solamente esté tu corazón "
             "vuelto hacia Dios, y no dudes de lo que veas.",
    (11, 5): "Le pregunté: ¿Por qué la torre está edificada sobre las aguas, "
             "señora? Te lo dije, dice, también antes, y lo investigas con "
             "diligencia; investigando, pues, hallas la verdad. Oye, pues, "
             "por qué la torre está edificada sobre las aguas: porque vuestra "
             "vida fue salvada por el agua y será salvada. Y la torre ha sido "
             "fundada por la palabra del Nombre omnipotente y glorioso, y es "
             "sostenida por el poder invisible del Soberano.",

    # Capítulo 12
    (12, 1): "Respondiendo, le digo: Señora, grande y maravillosa es esta "
             "cosa. Y los seis jóvenes que edifican, ¿quiénes son, señora? "
             "Éstos son los santos ángeles de Dios, los primeros creados, a "
             "quienes el Señor entregó toda su creación para que la "
             "acrecentaran y edificaran y señorearan sobre toda la creación. "
             "Por medio de éstos, pues, se acabará el edificio de la torre.",
    (12, 2): "Y los otros, los que traen las piedras, ¿quiénes son? También "
             "ellos son santos ángeles de Dios; pero estos seis son "
             "superiores a ellos. Se acabará, pues, el edificio de la torre, "
             "y todos juntos se regocijarán alrededor de la torre y "
             "glorificarán a Dios, porque se acabó el edificio de la torre.",
    (12, 3): "Le pregunté diciendo: Señora, quisiera conocer el destino de "
             "las piedras y su significado, cuál es. Respondiéndome, dice: No "
             "es que tú seas más digno que todos para que te sea revelado; "
             "porque hay otros antes que tú y mejores que tú, a quienes "
             "debían ser reveladas estas visiones; sino que, para que sea "
             "glorificado el nombre de Dios, te fue revelado y te será "
             "revelado por causa de los de doble ánimo, que discurren en sus "
             "corazones si estas cosas son o no son. Diles que todas estas "
             "cosas son verdaderas, y que nada hay fuera de la verdad, sino "
             "que todas son firmes y seguras y bien fundadas.",

    # Capítulo 13
    (13, 1): "Oye ahora acerca de las piedras que van al edificio. Las "
             "piedras cuadradas y blancas, que concuerdan en sus junturas, "
             "éstas son los apóstoles, y obispos, y maestros, y diáconos, que "
             "anduvieron conforme a la santidad de Dios, y ejercieron el "
             "episcopado, y enseñaron, y sirvieron pura y santamente a los "
             "escogidos de Dios; unos ya han dormido, y otros aún viven. Y "
             "siempre estuvieron de acuerdo entre sí, y tuvieron paz entre "
             "sí, y se escuchaban unos a otros; por eso en el edificio de la "
             "torre concuerdan sus junturas.",
    (13, 2): "Y las que se sacan de lo profundo y se ponen en el edificio, y "
             "concuerdan en sus junturas con las otras piedras ya edificadas, "
             "¿quiénes son? Éstos son los que padecieron por causa del nombre "
             "del Señor.",
    (13, 3): "Y quiero saber quiénes son las otras piedras que se traen de la "
             "tierra seca, señora. Dijo: Las que van al edificio sin ser "
             "labradas, a éstas las aprobó el Señor, porque anduvieron en la "
             "rectitud del Señor y cumplieron sus mandamientos.",
    (13, 4): "Y las que se traen y se ponen en el edificio, ¿quiénes son? Son "
             "nuevos en la fe, y fieles. Y son amonestados por los ángeles a "
             "hacer el bien, porque se halló en ellos maldad.",
    (13, 5): "Y las que desechaban y arrojaban, ¿quiénes son? Éstos son los "
             "que han pecado y quieren arrepentirse; por esto no fueron "
             "arrojados lejos de la torre, porque serán útiles para el "
             "edificio si se arrepienten. Los que, pues, han de arrepentirse, "
             "si se arrepienten, serán fuertes en la fe, si se arrepienten "
             "ahora, mientras se edifica la torre. Pero si se acaba el "
             "edificio, ya no tienen lugar, sino que serán desechados; sólo "
             "esto tienen: yacer junto a la torre.",

    # Capítulo 14
    (14, 1): "¿Y quieres saber de las que se hacían pedazos y se arrojaban "
             "lejos de la torre? Éstos son los hijos de la iniquidad; "
             "creyeron con hipocresía, y ninguna maldad se apartó de ellos. "
             "Por esto no tienen salvación, porque no son útiles para el "
             "edificio a causa de sus maldades. Por esto fueron hechos "
             "pedazos y arrojados lejos a causa de la ira del Señor, porque "
             "le provocaron a ira.",
    (14, 2): "Y las otras, que has visto yacer en gran número sin ir al "
             "edificio: las que están roñosas son los que conocieron la "
             "verdad, pero no permanecieron en ella.",
    (14, 3): "Y las que tienen grietas, ¿quiénes son? Éstos son los que "
             "tienen algo unos contra otros en sus corazones y no tienen paz "
             "entre sí, sino que tienen apariencia de paz; mas cuando se "
             "apartan unos de otros, sus maldades permanecen en sus "
             "corazones. Éstas, pues, son las grietas que tienen las piedras.",
    (14, 4): "Y las mutiladas, éstos son los que han creído y tienen la mayor "
             "parte en la justicia, pero tienen algunas partes de iniquidad; "
             "por esto están mutiladas y no enteras.",
    (14, 5): "Y las blancas y redondas, que no se ajustan al edificio, "
             "¿quiénes son, señora? Respondiéndome, dice: ¿Hasta cuándo serás "
             "necio e insensato, que todo lo preguntas y nada entiendes? "
             "Éstos son los que tienen fe, pero tienen también riquezas de "
             "este siglo; cuando viene la tribulación, por sus riquezas y por "
             "sus negocios niegan a su Señor.",
    (14, 6): "Y respondiéndole, digo: Señora, ¿cuándo, pues, serán útiles "
             "para el edificio? Cuando, dice, les sea cortada la riqueza que "
             "seduce sus almas, entonces serán útiles a Dios. Porque así como "
             "la piedra redonda, si no es cortada y pierde algo de sí, no "
             "puede hacerse cuadrada, así también los que son ricos en este "
             "siglo, si no les es cortada su riqueza, no pueden hacerse "
             "útiles al Señor.",
    (14, 7): "Conócelo primero por ti mismo: cuando eras rico, eras inútil; "
             "mas ahora eres útil y provechoso para la vida. Haceos útiles a "
             "Dios; porque también tú mismo eres sacado de las mismas "
             "piedras.",

    # Capítulo 15
    (15, 1): "Y las otras piedras que viste arrojadas lejos de la torre, y "
             "que caían en el camino y rodaban del camino a lugares sin "
             "camino, éstos son los que han creído, pero por su doble ánimo "
             "dejan su camino verdadero; pensando, pues, que pueden hallar un "
             "camino mejor, se extravían y andan miserables por lugares sin "
             "camino.",
    (15, 2): "Y las que caen en el fuego y se queman, éstos son los que se "
             "apartaron para siempre del Dios vivo, y ya no les subió al "
             "corazón el arrepentirse, a causa de los deseos de su lascivia y "
             "de las maldades que obraron.",
    (15, 3): "¿Y quieres saber quiénes son las otras, las que caen cerca de "
             "las aguas y no pueden rodar al agua? Éstos son los que oyeron "
             "la palabra y quieren ser bautizados en el nombre del Señor; mas "
             "luego, cuando les viene a la memoria la pureza de la verdad, se "
             "vuelven atrás y andan otra vez en pos de sus malos deseos.",
    (15, 4): "Acabó, pues, la explicación de la torre.",
    (15, 5): "Siendo todavía importuno, le pregunté si todas estas piedras "
             "que fueron desechadas y no se ajustaban al edificio de la torre "
             "tenían arrepentimiento y lugar en esta torre. Tienen, dice, "
             "arrepentimiento, pero no pueden ajustarse a esta torre;",
    (15, 6): "mas se ajustarán en otro lugar mucho menor, y esto cuando hayan "
             "sido atormentados y hayan cumplido los días de sus pecados. Y "
             "por esto serán trasladados, porque participaron de la palabra "
             "justa. Y entonces les acontecerá ser trasladados de sus "
             "tormentos, a causa de las malas obras que hicieron. Pero si no "
             "les sube al corazón, no son salvos, a causa de la dureza de su "
             "corazón.",

    # Capítulo 16
    (16, 1): "Cuando, pues, dejé de preguntarle acerca de todas estas cosas, "
             "me dice: ¿Quieres ver otra cosa? Deseoso como estaba de "
             "contemplar, me llené de gozo por ver.",
    (16, 2): "Mirándome, se sonrió y me dice: ¿Ves siete mujeres alrededor de "
             "la torre? Las veo, señora, digo. Esta torre es sostenida por "
             "ellas, por mandato del Señor.",
    (16, 3): "Oye ahora sus operaciones. La primera de ellas, la que tiene "
             "las manos entrelazadas, se llama Fe; por ella se salvan los "
             "escogidos de Dios.",
    (16, 4): "Y la segunda, la que está ceñida y se porta varonilmente, se "
             "llama Continencia; ésta es hija de la Fe. El que la siguiere, "
             "pues, será bienaventurado en su vida, porque se abstendrá de "
             "todas las malas obras, creyendo que, si se abstiene de todo mal "
             "deseo, heredará la vida eterna.",
    (16, 5): "Y las otras, señora, ¿quiénes son? Son hijas unas de otras; y "
             "se llaman: la una Sencillez, la otra Ciencia, la otra "
             "Inocencia, la otra Santidad, la otra Amor. Cuando, pues, hagas "
             "todas las obras de su madre, podrás vivir.",
    (16, 6): "Quisiera saber, señora, digo, qué poder tiene cada una de "
             "ellas. Oye, dice, los poderes que tienen.",
    (16, 7): "Sus poderes se sostienen unos a otros, y se siguen unas a otras "
             "según el orden en que fueron engendradas. De la Fe nace la "
             "Continencia, de la Continencia la Sencillez, de la Sencillez la "
             "Inocencia, de la Inocencia la Santidad, de la Santidad la "
             "Ciencia, de la Ciencia el Amor. Las obras de éstas, pues, son "
             "puras, y santas, y divinas.",
    (16, 8): "El que las sirviere, pues, y tuviere fuerza para retener sus "
             "obras, tendrá su morada en la torre con los santos de Dios.",
    (16, 9): "Y le preguntaba acerca de los tiempos, si ya es la consumación. "
             "Y ella clamó a gran voz, diciendo: Hombre insensato, ¿no ves "
             "que la torre todavía se está edificando? Cuando, pues, la torre "
             "que se edifica sea acabada, viene el fin. Pero pronto será "
             "edificada. No me preguntes ya nada más; bástente a ti y a los "
             "santos este recordatorio y la renovación de vuestros espíritus.",
    (16, 10): "Pero no te han sido reveladas estas cosas a ti solo, sino para "
              "que las muestres a todos,",
    (16, 11): "después de tres días, porque primero es necesario que tú las "
              "entiendas. Y te mando primero a ti, Hermas, que las palabras "
              "que te voy a decir las digas todas a los oídos de los santos, "
              "para que, oyéndolas y poniéndolas por obra, sean limpiados de "
              "sus maldades, y tú también con ellos.",

    # Capítulo 17
    (17, 1): "Oídme, hijos: yo os crié con mucha sencillez, e inocencia, y "
             "santidad, por la misericordia del Señor, que destiló sobre "
             "vosotros la justicia, para que fueseis justificados y "
             "santificados de toda maldad y de toda perversidad; mas vosotros "
             "no queréis cesar de vuestra maldad.",
    (17, 2): "Ahora, pues, oídme, y tened paz entre vosotros, y visitaos unos "
             "a otros, y socorreos unos a otros; y no toméis vosotros solos "
             "con abundancia de las criaturas de Dios, sino repartid también "
             "a los necesitados.",
    (17, 3): "Porque unos, por los muchos manjares, atraen enfermedad a su "
             "carne y dañan su carne; y la carne de los que no tienen "
             "manjares se daña por no tener lo suficiente de alimento, y su "
             "cuerpo se consume.",
    (17, 4): "Esta falta de igualdad, pues, os es dañosa a vosotros los que "
             "tenéis y no repartís con los necesitados.",
    (17, 5): "Mirad el juicio que viene. Vosotros, pues, los que tenéis de "
             "sobra, buscad a los hambrientos mientras la torre no está aún "
             "acabada; porque después que la torre sea acabada, querréis "
             "hacer el bien, y no tendréis lugar.",
    (17, 6): "Mirad, pues, vosotros los que os jactáis de vuestras riquezas, "
             "no sea que giman los necesitados, y su gemido suba al Señor, y "
             "seáis excluidos con vuestros bienes fuera de la puerta de la "
             "torre.",
    (17, 7): "Ahora, pues, os digo a vosotros los que presidís la iglesia y a "
             "los que ocupáis los primeros asientos: No seáis semejantes a "
             "los hechiceros. Porque los hechiceros llevan sus drogas en "
             "cajitas, mas vosotros lleváis vuestra droga y vuestro veneno en "
             "el corazón.",
    (17, 8): "Estáis endurecidos, y no queréis limpiar vuestros corazones y "
             "mezclar vuestro sentir en uno solo con corazón puro, para que "
             "alcancéis misericordia del gran Rey.",
    (17, 9): "Mirad, pues, hijos, que estas disensiones no os priven de "
             "vuestra vida.",
    (17, 10): "¿Cómo queréis vosotros corregir a los escogidos del Señor, si "
              "vosotros mismos no tenéis corrección? Corregíos, pues, unos a "
              "otros, y tened paz entre vosotros, para que también yo, "
              "estando alegre delante del Padre, dé cuenta de todos vosotros "
              "al Señor.",

    # Capítulo 18
    (18, 1): "Cuando, pues, cesó de hablar conmigo, vinieron los seis jóvenes "
             "que edificaban y la llevaron a la torre, y otros cuatro alzaron "
             "el banco y lo llevaron también a la torre. A éstos no les vi el "
             "rostro, porque estaban vueltos de espaldas.",
    (18, 2): "Y mientras ella se iba, le rogaba que me revelase acerca de las "
             "tres formas en que se me había aparecido. Respondiéndome, dice: "
             "Acerca de esto debes preguntar a otro, para que te sea "
             "revelado.",
    (18, 3): "Y se me apareció, hermanos, en la primera visión, la del año "
             "pasado, muy anciana y sentada en una silla.",
    (18, 4): "Y en la segunda visión tenía el rostro más joven, pero la carne "
             "y los cabellos de anciana, y me hablaba de pie; y estaba más "
             "alegre que antes.",
    (18, 5): "Y en la tercera visión era toda joven y de hermosura "
             "extraordinaria, y sólo los cabellos tenía de anciana; y estaba "
             "alegre en extremo, y sentada sobre un banco.",
    (18, 6): "Acerca de estas cosas estaba yo muy triste por conocer esta "
             "revelación, y veo a la anciana en una visión de la noche, que "
             "me decía: Toda pregunta requiere humildad. Ayuna, pues, y "
             "recibirás del Señor lo que pides.",
    (18, 7): "Ayuné, pues, un día, y esa misma noche se me apareció un joven "
             "y me dice: ¿Por qué pides tú a cada momento revelaciones en tu "
             "oración? Mira no sea que, pidiendo muchas cosas, dañes tu "
             "carne.",
    (18, 8): "Bástente estas revelaciones. ¿Acaso puedes ver revelaciones más "
             "fuertes que las que has visto?",
    (18, 9): "Respondiéndole, digo: Señor, sólo esto pido: que acerca de las "
             "tres formas de la anciana se haga una revelación completa. "
             "Respondiéndome, dice: ¿Hasta cuándo seréis insensatos? Pero "
             "vuestras dudas os hacen insensatos, y el no tener vuestro "
             "corazón vuelto al Señor.",
    (18, 10): "Respondiéndole otra vez, dije: Pero por ti, señor, las "
              "conoceremos con más exactitud.",

    # Capítulo 19
    (19, 1): "Oye, dice, acerca de las formas que buscas.",
    (19, 2): "En la primera visión, ¿por qué se te apareció anciana y sentada "
             "en una silla? Porque vuestro espíritu es anciano y ya marchito, "
             "y no tiene fuerza por vuestras flaquezas y dudas.",
    (19, 3): "Porque así como los ancianos, no teniendo ya esperanza de "
             "rejuvenecer, no esperan otra cosa sino su sueño de muerte, así "
             "también vosotros, debilitados por los negocios de esta vida, os "
             "entregasteis a la desidia, y no echasteis vuestras "
             "preocupaciones sobre el Señor; sino que vuestro entendimiento "
             "se quebrantó, y os envejecisteis con vuestras tristezas.",
    (19, 4): "Quisiera saber, pues, señor, por qué estaba sentada en una "
             "silla. Porque todo enfermo se sienta en una silla a causa de su "
             "enfermedad, para que sea sostenida la flaqueza de su cuerpo. "
             "Tienes la figura de la primera visión.",

    # Capítulo 20
    (20, 1): "Y en la segunda visión la viste de pie, y con el rostro más "
             "joven y más alegre que antes, pero la carne y los cabellos de "
             "anciana. Oye, dice, también esta parábola:",
    (20, 2): "Cuando alguno ya anciano, que ha desesperado de sí mismo por su "
             "enfermedad y su pobreza, no espera otra cosa sino el último día "
             "de su vida, y de repente le queda una herencia, al oírlo se "
             "levanta, y lleno de gozo se reviste de fuerza; y ya no está "
             "recostado, sino que se pone en pie, y se renueva su espíritu, "
             "ya corrompido por sus obras anteriores, y ya no está sentado, "
             "sino que se porta varonilmente: así también vosotros, oyendo la "
             "revelación que el Señor os reveló,",
    (20, 3): "porque tuvo compasión de vosotros, renovasteis vuestros "
             "espíritus, y depusisteis vuestras flaquezas, y os vino "
             "fortaleza, y fuisteis fortalecidos en la fe; y viendo el Señor "
             "vuestro fortalecimiento, se gozó; y por esto os mostró el "
             "edificio de la torre, y os mostrará otras cosas, si de todo "
             "corazón tenéis paz entre vosotros.",

    # Capítulo 21
    (21, 1): "Y en la tercera visión la viste más joven, y hermosa, y alegre, "
             "y hermosa su forma.",
    (21, 2): "Porque así como cuando a alguno que está triste le llega alguna "
             "buena noticia, al punto se olvida de sus tristezas anteriores y "
             "no espera otra cosa sino la noticia que oyó, y en adelante se "
             "fortalece para el bien, y se renueva su espíritu por el gozo "
             "que recibió: así también vosotros habéis recibido la renovación "
             "de vuestros espíritus viendo estos bienes.",
    (21, 3): "Y que la viste sentada sobre un banco: firme es la posición, "
             "porque el banco tiene cuatro pies y se sostiene firmemente; "
             "porque también el mundo se sostiene por medio de cuatro "
             "elementos.",
    (21, 4): "Los que se han arrepentido, pues, serán del todo nuevos y bien "
             "fundados, los que se han arrepentido de todo corazón. Tienes "
             "completa la revelación; no pidas ya nada más acerca de "
             "revelación; y si algo fuere necesario, te será revelado.",

    # Capítulo 22
    (22, 1): "La que vi, hermanos, veinte días después de la visión anterior, "
             "en figura de la tribulación que viene.",
    (22, 2): "Iba yo al campo por la Vía Campana. Desde el camino público "
             "está como a diez estadios; y el lugar se anda con facilidad.",
    (22, 3): "Caminando, pues, solo, ruego al Señor que lleve a término las "
             "revelaciones y visiones que me mostró por medio de su santa "
             "Iglesia, para que me fortalezca y dé el arrepentimiento a sus "
             "siervos que han tropezado, para que sea glorificado su nombre "
             "grande y glorioso, porque me tuvo por digno de mostrarme sus "
             "maravillas.",
    (22, 4): "Y mientras yo le glorificaba y le daba gracias, me respondió "
             "como el sonido de una voz: No dudes, Hermas. Comencé a "
             "discurrir dentro de mí y a decir: ¿Yo, qué motivo tengo para "
             "dudar, estando tan bien fundado por el Señor, y habiendo visto "
             "cosas gloriosas?",
    (22, 5): "Y avancé un poco, hermanos, y he aquí, veo una polvareda como "
             "hasta el cielo, y comencé a decir dentro de mí: ¿Serán acaso "
             "ganados que vienen y levantan polvo? Y estaba de mí como a un "
             "estadio.",
    (22, 6): "Haciéndose la polvareda cada vez mayor, sospeché que era algo "
             "divino. Brilló un poco el sol, y he aquí, veo una bestia "
             "grandísima, como un monstruo marino, y de su boca salían "
             "langostas de fuego. Y la bestia tenía de largo como cien pies, "
             "y la cabeza la tenía como una vasija de barro.",
    (22, 7): "Y comencé a llorar y a rogar al Señor que me librase de ella; y "
             "me acordé de la palabra que había oído: No dudes, Hermas.",
    (22, 8): "Revestido, pues, hermanos, de la fe del Señor, y acordándome de "
             "las grandezas que me había enseñado, cobrando ánimo me entregué "
             "a la bestia. Y venía la bestia con tal ímpetu que podía "
             "destruir una ciudad.",
    (22, 9): "Llego cerca de ella, y aquel monstruo tan grande se tiende en "
             "el suelo, y no hacía más que sacar la lengua, y no se movió en "
             "absoluto hasta que pasé de ella.",
    (22, 10): "Y tenía la bestia sobre la cabeza cuatro colores: negro, luego "
              "color de fuego y de sangre, luego de oro, luego blanco.",

    # Capítulo 23
    (23, 1): "Y después de haber pasado de la bestia y haber avanzado como "
             "treinta pies, he aquí, me sale al encuentro una virgen adornada "
             "como quien sale de la cámara nupcial, toda vestida de blanco y "
             "con sandalias blancas, cubierta con un velo hasta la frente, y "
             "su velo era una mitra; y tenía los cabellos blancos.",
    (23, 2): "Conocí yo, por las visiones anteriores, que era la Iglesia, y "
             "me alegré más. Me saluda diciendo: Salud a ti, hombre. Y yo la "
             "saludé a mi vez: Señora, salud.",
    (23, 3): "Respondiéndome, dice: ¿No te salió nada al encuentro? Le digo: "
             "Señora, una bestia tan grande, capaz de destruir pueblos; pero "
             "por el poder del Señor y por su gran misericordia escapé de "
             "ella.",
    (23, 4): "Bien escapaste, dice, porque echaste tu preocupación sobre Dios "
             "y abriste tu corazón al Señor, creyendo que por ningún otro "
             "puedes ser salvo sino por el Nombre grande y glorioso. Por esto "
             "el Señor envió a su ángel, el que está sobre las bestias, cuyo "
             "nombre es Tegri, y le cerró la boca, para que no te dañase. De "
             "una gran tribulación has escapado por tu fe, y porque, viendo "
             "una bestia tan grande, no dudaste.",
    (23, 5): "Ve, pues, y cuenta a los escogidos del Señor sus grandezas, y "
             "diles que esta bestia es figura de la gran tribulación que ha "
             "de venir. Si, pues, os preparáis de antemano y os arrepentís de "
             "todo vuestro corazón volviéndoos al Señor, podréis escapar de "
             "ella, si vuestro corazón se hace puro y sin mancha, y servís al "
             "Señor sin reproche los días que os quedan de vuestra vida. "
             "Echad vuestras preocupaciones sobre el Señor, y él las "
             "enderezará.",
    (23, 6): "Creed al Señor, vosotros los de doble ánimo, que todo lo puede, "
             "y aparta de vosotros su ira, y envía azotes sobre vosotros los "
             "de doble ánimo. ¡Ay de los que oyen estas palabras y las "
             "desoyen! Mejor les fuera no haber nacido.",

    # Capítulo 24
    (24, 1): "Le pregunté acerca de los cuatro colores que tenía la bestia en "
             "la cabeza. Y ella, respondiéndome, dice: Otra vez eres curioso "
             "acerca de tales cosas. Sí, digo, señora; hazme saber qué son "
             "estas cosas.",
    (24, 2): "Oye, dice: el negro es este mundo en que habitáis;",
    (24, 3): "y el color de fuego y de sangre significa que este mundo ha de "
             "perecer por sangre y fuego;",
    (24, 4): "y la parte de oro sois vosotros, los que habéis huido de este "
             "mundo. Porque así como el oro se prueba por el fuego y se hace "
             "útil, así también vosotros, los que habitáis en él, sois "
             "probados. Los que, pues, permanecéis y sois pasados por el "
             "fuego por ellos, seréis purificados. Así como el oro arroja su "
             "escoria, así también vosotros arrojaréis toda tristeza y "
             "angustia, y seréis purificados y seréis útiles para el edificio "
             "de la torre.",
    (24, 5): "Y la parte blanca es el siglo venidero, en el cual habitarán "
             "los escogidos de Dios; porque sin mancha y puros serán los "
             "escogidos por Dios para la vida eterna.",
    (24, 6): "Tú, pues, no dejes de hablar a los oídos de los santos. Tenéis "
             "también la figura de la gran tribulación que viene. Y si "
             "vosotros queréis, no será nada. Acordaos de lo que antes se ha "
             "escrito.",
    (24, 7): "Dicho esto, se fue, y no vi a qué lugar se fue, porque se hizo "
             "una nube; y yo me volví atrás atemorizado, pensando que venía "
             "la bestia.",

    # Capítulo 25
    (25, 1): "Estando yo orando en la casa y sentado sobre el lecho, entró un "
             "hombre de aspecto glorioso, en traje de pastor, cubierto con "
             "una piel blanca de cabra, con un zurrón sobre los hombros y un "
             "cayado en la mano. Y me saludó, y yo le devolví el saludo.",
    (25, 2): "Y en seguida se sentó junto a mí y me dice: Fui enviado por el "
             "ángel más venerable, para morar contigo los días que restan de "
             "tu vida.",
    (25, 3): "Yo pensé que venía a tentarme, y le digo: Pues ¿quién eres tú? "
             "Porque yo, digo, sé a quién fui entregado. Me dice: ¿No me "
             "reconoces? No, digo. Yo, dice, soy el pastor a quien fuiste "
             "entregado.",
    (25, 4): "Estando él aún hablando, se mudó su aspecto, y le reconocí, que "
             "era aquel a quien fui entregado; y en seguida quedé confuso, y "
             "me tomó el temor, y quedé enteramente abatido de tristeza, por "
             "haberle respondido tan mala y neciamente.",
    (25, 5): "Mas él, respondiéndome, dice: No te turbes, sino fortalécete en "
             "mis mandamientos que he de mandarte. Porque fui enviado, dice, "
             "para mostrarte de nuevo todas las cosas que viste antes, esto "
             "es, los puntos principales que os son provechosos. Ante todo "
             "escribe mis mandamientos y las parábolas; y lo demás lo "
             "escribirás así como te lo mostraré. Por esto, dice, te mando "
             "que escribas primero los mandamientos y las parábolas, para que "
             "las leas a mano y puedas guardarlas.",
    (25, 6): "Escribí, pues, los mandamientos y las parábolas, así como me lo "
             "mandó.",
    (25, 7): "Si, pues, habiéndolas oído, las guardáis y andáis en ellas y "
             "las ponéis por obra con corazón puro, recibiréis del Señor "
             "cuanto os ha prometido; mas si, habiéndolas oído, no os "
             "arrepentís, sino que añadís aún a vuestros pecados, recibiréis "
             "del Señor lo contrario. Todas estas cosas me mandó que las "
             "escribiese así el pastor, el ángel de la penitencia.",

    # Capítulo 26
    (26, 1): "Ante todo cree que uno es Dios, el que creó y ordenó todas las "
             "cosas, y las hizo todas pasar de lo que no es a ser, y que lo "
             "contiene todo, siendo él solo incontenible.",
    (26, 2): "Cree, pues, en él, y témele, y temiéndole, sé continente. "
             "Guarda estas cosas, y echarás de ti toda maldad, y te vestirás "
             "de toda virtud de justicia, y vivirás para Dios, si guardas "
             "este mandamiento.",

    # Capítulo 27
    (27, 1): "Me dice: Ten sencillez y sé inocente, y serás como los niños "
             "pequeños, que no conocen la maldad que destruye la vida de los "
             "hombres.",
    (27, 2): "Primeramente, no hables mal de nadie, ni oigas con gusto al que "
             "habla mal; de otra manera, también tú, que oyes, serás culpable "
             "del pecado del que murmura, si das crédito a la murmuración que "
             "oigas; porque, creyéndola, también tú mismo tendrás algo contra "
             "tu hermano; así, pues, serás culpable del pecado del que "
             "murmura.",
    (27, 3): "Mala es la murmuración; es un demonio inquieto, que nunca está "
             "en paz, sino que siempre habita en disensiones. Apártate, pues, "
             "de ella, y tendrás siempre bienestar con todos.",
    (27, 4): "Vístete de la gravedad, en la cual no hay ningún tropiezo malo, "
             "sino que todo es llano y alegre. Obra el bien, y de tus "
             "trabajos, que Dios te da, da con sencillez a todos los "
             "necesitados, sin dudar a quién darás o a quién no darás. Da a "
             "todos, porque Dios quiere que a todos se dé de sus propios "
             "dones.",
    (27, 5): "Los que reciben, pues, darán cuenta a Dios de por qué "
             "recibieron y para qué; porque los que reciben estando en "
             "aflicción no serán juzgados, mas los que reciben con hipocresía "
             "pagarán la pena.",
    (27, 6): "El que da, pues, es inocente; porque, así como recibió del "
             "Señor el ministerio de cumplirlo, lo cumplió con sencillez, sin "
             "hacer distinción alguna a quién daría o no daría. Este "
             "ministerio, pues, cumplido con sencillez, fue glorioso delante "
             "de Dios. El que así sirve a Dios con sencillez, vivirá.",
    (27, 7): "Guarda, pues, este mandamiento, como te lo he hablado, para que "
             "tu penitencia y la de tu casa se halle en sencillez, y tu "
             "inocencia sea pura y sin mancha.",

    # Capítulo 28
    (28, 1): "Otra vez me dice: Ama la verdad, y toda verdad salga de tu "
             "boca, para que el espíritu que Dios hizo morar en esta carne se "
             "halle verdadero delante de todos los hombres, y así será "
             "glorificado el Señor que mora en ti; porque el Señor es "
             "verdadero en toda palabra, y no hay en él mentira alguna.",
    (28, 2): "Los que mienten, pues, desechan al Señor y se hacen "
             "defraudadores del Señor, no devolviéndole el depósito que "
             "recibieron. Porque recibieron de él un espíritu sin mentira. Si "
             "lo devuelven mentiroso, contaminaron el mandamiento del Señor y "
             "se hicieron defraudadores.",
    (28, 3): "Oyendo, pues, yo estas cosas, lloré mucho. Y viéndome llorar, "
             "me dice: ¿Por qué lloras? Porque, digo, señor, no sé si puedo "
             "ser salvo. ¿Por qué? dice. Porque nunca, digo, señor, en mi "
             "vida hablé palabra verdadera, sino que siempre hablé con "
             "astucia con todos, e hice pasar mi mentira por verdad delante "
             "de todos los hombres; y nunca nadie me contradijo, sino que se "
             "dio crédito a mi palabra. ¿Cómo, pues, digo, señor, puedo vivir "
             "habiendo hecho estas cosas?",
    (28, 4): "Tú, dice, piensas bien y con verdad; porque convenía que tú, "
             "como siervo de Dios, anduvieses en verdad, y que una mala "
             "conciencia no morase con el espíritu de la verdad, ni causases "
             "tristeza al espíritu venerable y verdadero. Nunca, digo, señor, "
             "oí con exactitud tales palabras.",
    (28, 5): "Ahora, pues, dice, las oyes: guárdalas, para que también las "
             "cosas falsas que antes hablaste en tus negocios, hallándose "
             "verdaderas estas, también aquellas se hagan dignas de fe; "
             "porque también aquellas pueden hacerse dignas de fe. Si guardas "
             "estas cosas, y desde ahora hablas toda verdad, podrás adquirir "
             "para ti la vida; y cualquiera que oiga este mandamiento y se "
             "aparte de la mentira, que es malísima, vivirá para Dios.",

    # Capítulo 29
    (29, 1): "Te mando, dice, que guardes la castidad, y que no suba a tu "
             "corazón pensamiento de mujer ajena, ni de fornicación alguna, "
             "ni de otras cosas malas semejantes. Porque, haciendo esto, "
             "obras gran pecado. Mas acordándote siempre de tu propia mujer, "
             "nunca pecarás.",
    (29, 2): "Porque si este deseo sube a tu corazón, pecarás; y si otras "
             "cosas igualmente malas, obras pecado; porque este deseo es "
             "pecado grande para el siervo de Dios; y si alguno pone por obra "
             "esta mala acción, obra para sí la muerte.",
    (29, 3): "Mira, pues, tú: apártate de este deseo; porque donde mora la "
             "gravedad, allí no debe subir la iniquidad al corazón del varón "
             "justo.",
    (29, 4): "Le digo: Señor, permíteme hacerte unas pocas preguntas. Di, "
             "dice. Señor, digo, si uno tiene mujer fiel en el Señor, y la "
             "halla en algún adulterio, ¿peca acaso el marido si vive con "
             "ella?",
    (29, 5): "Mientras lo ignora, dice, no peca; mas si el marido conoce el "
             "pecado de ella, y la mujer no se arrepiente, sino que persiste "
             "en su fornicación, y el marido vive con ella, se hace culpable "
             "del pecado de ella y partícipe de su adulterio.",
    (29, 6): "¿Qué hará, pues, digo, señor, el marido, si la mujer persiste "
             "en esta pasión? Despídala, dice, y quédese el marido solo; mas "
             "si, despedida su mujer, se casa con otra, también él comete "
             "adulterio.",
    (29, 7): "Si, pues, digo, señor, después de despedida la mujer, la mujer "
             "se arrepiente y quiere volver a su propio marido, ¿no será "
             "recibida?",
    (29, 8): "Ciertamente, dice; si el marido no la recibe, peca y atrae "
             "sobre sí gran pecado; antes bien, es necesario recibir al que "
             "ha pecado y se arrepiente, pero no muchas veces; porque para "
             "los siervos de Dios hay una sola penitencia. Por causa de la "
             "penitencia, pues, no debe casarse el marido. Esta conducta se "
             "aplica a la mujer y al marido.",
    (29, 9): "No solo, dice, es adulterio si alguno contamina su carne, sino "
             "que también el que hace cosas semejantes a las de los gentiles "
             "comete adulterio. De modo que, si alguno persiste también en "
             "tales obras y no se arrepiente, apártate de él y no vivas con "
             "él; de otra manera, también tú eres partícipe de su pecado.",
    (29, 10): "Por esto se os mandó quedaros solos, sea el marido, sea la "
              "mujer; porque en tales casos puede haber penitencia.",
    (29, 11): "Yo, pues, dice, no doy ocasión para que esta conducta se lleve "
              "a cabo así, sino para que el que ha pecado no peque más. Mas "
              "en cuanto a su pecado anterior, hay quien puede dar la "
              "curación; porque él es el que tiene la potestad sobre todas "
              "las cosas.",

    # Capítulo 30
    (30, 1): "Le pregunté otra vez, diciendo: Puesto que el Señor me tuvo por "
             "digno de que tú morases siempre conmigo, sopórtame todavía unas "
             "pocas palabras, pues nada entiendo y mi corazón está endurecido "
             "por mis obras anteriores. Dame entendimiento, porque soy muy "
             "necio y nada comprendo en absoluto.",
    (30, 2): "Respondiéndome, dice: Yo, dice, estoy puesto sobre la "
             "penitencia, y doy entendimiento a todos los que se arrepienten. "
             "¿O no te parece, dice, que esto mismo, el arrepentirse, es "
             "entendimiento? El arrepentirse, dice, es gran entendimiento; "
             "porque el que ha pecado entiende que ha hecho lo malo delante "
             "del Señor, y sube a su corazón la acción que hizo, y se "
             "arrepiente, y ya no obra lo malo, sino que obra el bien con "
             "abundancia, y humilla su alma y la atormenta, porque pecó. Ves, "
             "pues, que la penitencia es gran entendimiento.",
    (30, 3): "Por esto, pues, digo, señor, lo inquiero todo con exactitud de "
             "ti; primeramente, porque soy pecador, para saber qué obras he "
             "de hacer para vivir, porque mis pecados son muchos y variados.",
    (30, 4): "Vivirás, dice, si guardas mis mandamientos y andas en ellos; y "
             "cualquiera que, habiendo oído estos mandamientos, los guarde, "
             "vivirá para Dios.",

    # Capítulo 31
    (31, 1): "Todavía, digo, señor, añadiré una pregunta. Di, dice. Oí, digo, "
             "señor, de algunos maestros, que no hay otra penitencia sino "
             "aquella, cuando descendimos al agua y recibimos la remisión de "
             "nuestros pecados anteriores.",
    (31, 2): "Me dice: Bien oíste; porque así es. Porque convenía que el que "
             "ha recibido la remisión de los pecados no pecase más, sino que "
             "viviese en castidad.",
    (31, 3): "Mas puesto que todo lo inquieres con exactitud, también esto te "
             "declararé, sin dar ocasión a los que han de creer o a los que "
             "ahora han creído en el Señor. Porque los que ahora han creído o "
             "han de creer no tienen penitencia de pecados, sino que tienen "
             "remisión de sus pecados anteriores.",
    (31, 4): "A los que fueron llamados antes de estos días, pues, el Señor "
             "les puso penitencia; porque el Señor, siendo conocedor de los "
             "corazones y conociéndolo todo de antemano, conoció la flaqueza "
             "de los hombres y la mucha astucia del diablo, que hará algún "
             "mal a los siervos de Dios y obrará con malicia contra ellos.",
    (31, 5): "Siendo, pues, el Señor muy misericordioso, tuvo misericordia de "
             "su criatura y puso esta penitencia, y a mí me fue dada la "
             "potestad sobre esta penitencia.",
    (31, 6): "Mas yo te digo, dice: después de aquel llamamiento grande y "
             "venerable, si alguno, tentado por el diablo, peca, tiene una "
             "sola penitencia; mas si peca a cada paso y se arrepiente, no le "
             "aprovecha a tal hombre; porque difícilmente vivirá.",
    (31, 7): "Le digo: Recobré la vida al oír de ti estas cosas tan "
             "exactamente; porque sé que, si no añado más a mis pecados, seré "
             "salvo. Serás salvo, dice, tú y todos cuantos hagan estas cosas.",

    # Capítulo 32
    (32, 1): "Le pregunté otra vez, diciendo: Señor, puesto que una vez me "
             "soportas, declárame todavía también esto. Di, dice. Si una "
             "mujer, digo, señor, o a su vez un marido, muere, y el que queda "
             "de ellos se casa, ¿acaso peca el que se casa?",
    (32, 2): "No peca, dice; mas si alguno se queda solo, adquiere para sí "
             "mayor honra y gloria grande delante del Señor; pero si también "
             "se casa, no peca.",
    (32, 3): "Guarda, pues, la castidad y la gravedad, y vivirás para Dios. "
             "Estas cosas que te hablo y he de hablarte, guárdalas desde "
             "ahora, desde el día en que me fuiste entregado, y habitaré en "
             "tu casa.",
    (32, 4): "Y a tus faltas anteriores habrá remisión, si guardas mis "
             "mandamientos; y también a todos habrá remisión, si guardan "
             "estos mis mandamientos y andan en esta pureza.",

    # Capítulo 33
    (33, 1): "Sé paciente, dice, y prudente, y te enseñorearás de todas las "
             "malas obras, y obrarás toda justicia.",
    (33, 2): "Porque si eres paciente, el Espíritu Santo que mora en ti será "
             "puro, no oscurecido por otro espíritu malo, sino que, morando "
             "en lugar espacioso, se regocijará y se alegrará con el vaso en "
             "que mora, y servirá a Dios con mucha alegría, teniendo en sí el "
             "bienestar.",
    (33, 3): "Mas si sobreviene alguna ira, en seguida el Espíritu Santo, que "
             "es delicado, se angustia, no teniendo el lugar puro, y busca "
             "apartarse del lugar; porque es sofocado por el espíritu malo, "
             "no teniendo lugar para servir al Señor como quiere, siendo "
             "contaminado por la ira. Porque en la paciencia mora el Señor, "
             "mas en la ira el diablo.",
    (33, 4): "Así que, morando ambos espíritus en un mismo lugar, es cosa sin "
             "provecho y mala para aquel hombre en quien moran.",
    (33, 5): "Porque si tomas un poquito de ajenjo y lo echas en una vasija "
             "de miel, ¿no se echa a perder toda la miel, y tanta miel se "
             "pierde por el poquísimo ajenjo, y pierde la dulzura de la miel, "
             "y ya no tiene la misma estima ante su dueño, porque se amargó y "
             "perdió su utilidad? Mas si no se echa el ajenjo en la miel, la "
             "miel se halla dulce y se hace útil a su dueño.",
    (33, 6): "Ves que la paciencia es dulcísima, más que la miel, y es útil "
             "al Señor, y él mora en ella. Mas la ira es amarga e inútil. Si, "
             "pues, la ira se mezcla con la paciencia, la paciencia se "
             "contamina, y su oración ya no es útil para Dios.",
    (33, 7): "Quisiera, digo, señor, conocer la operación de la ira, para "
             "guardarme de ella. Ciertamente, dice, si no te guardas de ella "
             "tú y tu casa, has perdido toda tu esperanza. Pero guárdate de "
             "ella, porque yo estoy contigo. Y también se apartarán de ella "
             "todos cuantos se arrepientan de todo su corazón; porque yo "
             "estaré con ellos y los guardaré; pues todos fueron justificados "
             "por el ángel más venerable.",

    # Capítulo 34
    (34, 1): "Oye ahora, dice, la operación de la ira, cuán mala es, y cómo "
             "trastorna a mis siervos con su operación, y cómo los desvía de "
             "la justicia. Pero no desvía a los que están llenos en la fe, ni "
             "puede obrar en ellos, porque mi poder está con ellos; mas "
             "desvía a los vacíos y a los de doble ánimo.",
    (34, 2): "Y cuando ve a tales hombres en sosiego, se introduce en el "
             "corazón de aquel hombre, y por nada el varón o la mujer se "
             "llena de amargura, a causa de negocios de la vida, o por "
             "comidas, o por alguna menudencia, o por algún amigo, o por dar "
             "o recibir, o por otras cosas necias semejantes; porque todas "
             "estas cosas son necias y vanas e insensatas y sin provecho para "
             "los siervos de Dios.",
    (34, 3): "Mas la paciencia es grande y fuerte, y tiene poder robusto, y "
             "prospera en gran anchura; es alegre, se regocija, está libre de "
             "cuidados, glorifica al Señor en todo tiempo, no tiene en sí "
             "nada amargo, y permanece siempre mansa y sosegada. Esta "
             "paciencia, pues, mora con los que tienen la fe entera.",
    (34, 4): "Mas la ira es primeramente necia, liviana e insensata. Después, "
             "de la insensatez nace la amargura, de la amargura el enojo, del "
             "enojo la ira, y de la ira el rencor; después, este rencor, "
             "compuesto de tantos males, se hace pecado grande e incurable.",
    (34, 5): "Porque cuando estos espíritus moran en un mismo vaso donde "
             "también mora el Espíritu Santo, no cabe aquel vaso, sino que "
             "rebosa.",
    (34, 6): "El espíritu delicado, pues, no teniendo costumbre de morar con "
             "espíritu malo ni con dureza, se aparta de tal hombre y busca "
             "morar con mansedumbre y sosiego.",
    (34, 7): "Después, cuando se aparta de aquel hombre en quien mora, aquel "
             "hombre queda vacío del espíritu justo, y en adelante, lleno de "
             "los espíritus malos, anda inquieto en toda su conducta, "
             "arrastrado de acá para allá por los espíritus malos, y queda "
             "del todo ciego para el buen pensamiento. Así, pues, les "
             "acontece a todos los iracundos.",
    (34, 8): "Apártate, pues, de la ira, el espíritu malísimo; y vístete de "
             "la paciencia, y resiste a la ira y a la amargura, y te hallarás "
             "con la gravedad amada del Señor. Mira, pues, no descuides jamás "
             "este mandamiento; porque si te enseñoreas de este mandamiento, "
             "podrás guardar también los demás mandamientos que he de "
             "mandarte. Sé fuerte en ellos y fortalécete, y fortalézcanse "
             "todos cuantos quieran andar en ellos.",

    # Capítulo 35
    (35, 1): "Te mandé, dice, en el primer mandamiento, que guardases la fe y "
             "el temor y la continencia. Sí, digo, señor. Pero ahora, dice, "
             "quiero declararte también sus virtudes, para que entiendas cuál "
             "de ellas tiene qué virtud y operación; porque sus operaciones "
             "son dobles. Se aplican, pues, a lo justo y a lo injusto.",
    (35, 2): "Tú, pues, confía en lo justo, y no confíes en lo injusto; "
             "porque lo justo tiene camino recto, mas lo injusto, torcido. "
             "Pero tú anda por el camino recto y llano, y deja el torcido.",
    (35, 3): "Porque el camino torcido no tiene sendas, sino lugares sin "
             "camino y muchos tropiezos, y es áspero y espinoso. Es, pues, "
             "dañoso para los que andan en él.",
    (35, 4): "Mas los que andan por el camino recto caminan llanamente y sin "
             "tropiezo; porque no es áspero ni espinoso. Ves, pues, que es "
             "más provechoso andar por este camino.",
    (35, 5): "Me agrada, digo, señor, andar por este camino. Andarás, dice; y "
             "cualquiera que se convierta al Señor de todo corazón andará en "
             "él.",

    # Capítulo 36
    (36, 1): "Oye ahora, dice, acerca de la fe. Dos ángeles hay con el "
             "hombre: uno de la justicia y otro de la maldad.",
    (36, 2): "¿Cómo, pues, digo, señor, conoceré sus operaciones, puesto que "
             "ambos ángeles moran conmigo?",
    (36, 3): "Oye, dice, y las entenderás. El ángel de la justicia es "
             "delicado y pudoroso y manso y sosegado. Cuando, pues, este sube "
             "a tu corazón, en seguida habla contigo de justicia, de "
             "castidad, de gravedad, de contentamiento, de toda obra justa y "
             "de toda virtud gloriosa. Cuando todas estas cosas suben a tu "
             "corazón, sabe que el ángel de la justicia está contigo. Estas, "
             "pues, son las obras del ángel de la justicia. A este, pues, "
             "cree, y a sus obras.",
    (36, 4): "Mira, pues, también las obras del ángel de la maldad. Ante "
             "todo, es iracundo y amargo e insensato, y sus obras son malas, "
             "y trastornan a los siervos de Dios. Cuando, pues, este sube a "
             "tu corazón, conócelo por sus obras.",
    (36, 5): "Cómo, digo, señor, lo he de conocer, no lo sé. Oye, dice. "
             "Cuando te sobreviene alguna ira o amargura, sabe que él está en "
             "ti; después, el deseo de muchas ocupaciones, y el lujo de "
             "muchas comidas y bebidas, y de muchas borracheras, y de "
             "variados manjares que no convienen, y los deseos de mujeres y "
             "de codicias, y una soberbia muy grande, y la jactancia, y "
             "cuantas cosas son parecidas y semejantes a estas. Cuando, pues, "
             "estas cosas suben a tu corazón, sabe que el ángel de la maldad "
             "está en ti.",
    (36, 6): "Tú, pues, reconociendo sus obras, apártate de él y no le creas "
             "en nada, porque sus obras son malas y sin provecho para los "
             "siervos de Dios. Tienes, pues, las operaciones de ambos "
             "ángeles: entiéndelas y cree al ángel de la justicia;",
    (36, 7): "mas del ángel de la maldad apártate, porque su enseñanza es "
             "mala en toda obra. Porque aunque un hombre sea fiel, si el "
             "pensamiento de este ángel sube a su corazón, es necesario que "
             "aquel varón o aquella mujer cometa algún pecado.",
    (36, 8): "Y a su vez, aunque un varón o una mujer sea malísimo, si suben "
             "a su corazón las obras del ángel de la justicia, por fuerza ha "
             "de hacer algún bien.",
    (36, 9): "Ves, pues, dice, que es bueno seguir al ángel de la justicia y "
             "renunciar al ángel de la maldad.",
    (36, 10): "Lo que toca a la fe, esto declara este mandamiento: que creas "
              "a las obras del ángel de la justicia, y obrándolas vivas para "
              "Dios. Y cree que las obras del ángel de la maldad son "
              "perniciosas; no obrándolas, pues, vivirás para Dios.",

    # Capítulo 37
    (37, 1): "Teme, dice, al Señor y guarda sus mandamientos. Guardando, "
             "pues, los mandamientos de Dios, serás poderoso en toda obra, y "
             "tu obra será incomparable. Porque temiendo al Señor, todo lo "
             "harás bien; y este es el temor con que debes temer, y ser "
             "salvo.",
    (37, 2): "Mas al diablo no temas; porque temiendo al Señor te "
             "enseñorearás del diablo, porque no hay poder en él. Y en quien "
             "no hay poder, tampoco hay temor; mas en quien hay poder "
             "glorioso, también hay temor de él. Porque todo el que tiene "
             "poder infunde temor; mas el que no tiene poder es despreciado "
             "de todos.",
    (37, 3): "Mas teme las obras del diablo, porque son malas. Temiendo, "
             "pues, al Señor, no las harás, sino que te apartarás de ellas.",
    (37, 4): "Dobles son, pues, los temores; porque si quieres obrar el mal, "
             "teme al Señor, y no lo obrarás; y si a su vez quieres obrar el "
             "bien, teme al Señor, y lo obrarás. De modo que el temor del "
             "Señor es fuerte y grande y glorioso. Teme, pues, al Señor, y "
             "vivirás para él; y cuantos le teman y guarden sus mandamientos "
             "vivirán para Dios.",
    (37, 5): "¿Por qué, digo, señor, dijiste acerca de los que guardan sus "
             "mandamientos: Vivirán para Dios? Porque, dice, toda la creación "
             "teme al Señor, pero no guarda sus mandamientos. De los que le "
             "temen y guardan sus mandamientos, pues, de esos es la vida "
             "delante de Dios; mas de los que no guardan sus mandamientos, "
             "tampoco hay vida en ellos.",

    # Capítulo 38
    (38, 1): "Te dije, dice, que las criaturas de Dios son dobles; porque "
             "también la continencia es doble. Porque de algunas cosas "
             "conviene abstenerse, y de otras no conviene.",
    (38, 2): "Hazme saber, digo, señor, de qué cosas conviene abstenerse y de "
             "cuáles no conviene. Oye, dice. Abstente de lo malo y no lo "
             "hagas; mas de lo bueno no te abstengas, sino hazlo. Porque si "
             "te abstienes de hacer lo bueno, obras gran pecado; mas si te "
             "abstienes de hacer lo malo, obras gran justicia. Abstente, "
             "pues, de toda maldad, obrando el bien.",
    (38, 3): "¿Cuáles son, digo, señor, las maldades de que debemos "
             "abstenernos? Oye, dice: del adulterio y de la fornicación, de "
             "la embriaguez de la iniquidad, de los deleites malos, de las "
             "muchas comidas y del lujo de la riqueza, y de la jactancia y de "
             "la altivez y de la soberbia; y de la mentira y de la "
             "murmuración y de la hipocresía, del rencor y de toda blasfemia.",
    (38, 4): "Estas obras son las más malas de todas en la vida de los "
             "hombres. De estas obras, pues, debe abstenerse el siervo de "
             "Dios; porque el que no se abstiene de ellas no puede vivir para "
             "Dios. Oye, pues, también las que siguen a estas.",
    (38, 5): "¿Pues hay todavía, digo, señor, otras obras malas? Y por cierto "
             "muchas, dice, de las cuales debe abstenerse el siervo de Dios: "
             "el hurto, la mentira, el despojo, el falso testimonio, la "
             "avaricia, el mal deseo, el engaño, la vanagloria, la jactancia, "
             "y cuantas cosas son semejantes a estas.",
    (38, 6): "¿No te parece que estas cosas son malas? Y muy malas, digo, "
             "para los siervos de Dios. De todas estas debe abstenerse el que "
             "sirve a Dios. Abstente, pues, de todas ellas, para que vivas "
             "para Dios y seas inscrito con los que se abstienen de ellas. "
             "Estas, pues, son las cosas de que debes abstenerte.",
    (38, 7): "Mas las cosas de que no debes abstenerte, dice, sino hacerlas, "
             "oye. De lo bueno no te abstengas, sino hazlo.",
    (38, 8): "Declárame, digo, señor, también la virtud de las cosas buenas, "
             "para que ande en ellas y las sirva, a fin de que, obrándolas, "
             "pueda ser salvo. Oye, dice, también las obras de las cosas "
             "buenas, que debes obrar y no abstenerte de ellas.",
    (38, 9): "Ante todo, la fe, el temor del Señor, el amor, la concordia, "
             "las palabras de justicia, la verdad, la paciencia; nada hay "
             "mejor que estas cosas en la vida de los hombres. Si alguno "
             "guarda estas cosas y no se abstiene de ellas, se hace "
             "bienaventurado en su vida.",
    (38, 10): "Después, oye las que siguen a estas: servir a las viudas, "
              "visitar a los huérfanos y a los necesitados, rescatar de sus "
              "aprietos a los siervos de Dios, ser hospitalario (porque en la "
              "hospitalidad se halla a veces ocasión de hacer el bien), no "
              "oponerse a nadie, ser sosegado, hacerse más necesitado que "
              "todos los hombres, honrar a los ancianos, practicar la "
              "justicia, conservar la fraternidad, soportar la afrenta, ser "
              "paciente, no guardar rencor, consolar a los que están "
              "fatigados de alma, no desechar a los que han tropezado en la "
              "fe, sino hacerlos volver y darles buen ánimo, amonestar a los "
              "que pecan, no oprimir a los deudores y necesitados, y cuantas "
              "otras cosas son semejantes a estas.",
    (38, 11): "¿Te parece, dice, que estas cosas son buenas? Pues ¿qué hay, "
              "digo, señor, mejor que ellas? Anda, pues, dice, en ellas y no "
              "te abstengas de ellas, y vivirás para Dios.",
    (38, 12): "Guarda, pues, este mandamiento: si haces el bien y no te "
              "abstienes de él, vivirás para Dios, y todos los que así hacen "
              "vivirán para Dios. Y a su vez, si no haces el mal y te "
              "abstienes de él, vivirás para Dios, y vivirán para Dios todos "
              "cuantos guarden estos mandamientos y anden en ellos.",

    # Capítulo 39
    (39, 1): "Me dice: Quita de ti la doblez de ánimo, y no dudes en absoluto "
             "con doble ánimo en pedir algo a Dios, diciendo en ti mismo: "
             "¿Cómo puedo pedir al Señor y recibir, habiendo pecado tanto "
             "contra él?",
    (39, 2): "No razones así, sino conviértete al Señor de todo tu corazón, y "
             "pídele sin vacilar, y conocerás su mucha misericordia, que de "
             "ninguna manera te desamparará, sino que cumplirá la petición de "
             "tu alma.",
    (39, 3): "Porque Dios no es como los hombres, que guardan rencor, sino "
             "que él no guarda rencor y tiene misericordia de su criatura.",
    (39, 4): "Tú, pues, limpia tu corazón de todas las vanidades de este "
             "siglo y de las palabras que antes te fueron dichas, y pide al "
             "Señor, y lo recibirás todo, y no quedarás falto de ninguna de "
             "tus peticiones, si pides al Señor sin vacilar.",
    (39, 5): "Mas si vacilas en tu corazón, no recibirás ninguna de tus "
             "peticiones. Porque los que vacilan respecto de Dios, estos son "
             "los de doble ánimo, y no alcanzan en absoluto nada de sus "
             "peticiones.",
    (39, 6): "Mas los que son perfectos en la fe lo piden todo confiando en "
             "el Señor, y reciben, porque piden sin vacilar, sin tener doble "
             "ánimo en nada. Porque todo varón de doble ánimo, si no se "
             "arrepiente, difícilmente será salvo.",
    (39, 7): "Limpia, pues, tu corazón de la doblez de ánimo, y vístete de la "
             "fe, porque es fuerte, y cree a Dios que recibirás todas las "
             "peticiones que pides; y si alguna vez, habiendo pedido al Señor "
             "alguna petición, la recibes más tarde, no tengas doble ánimo "
             "porque no recibiste pronto la petición de tu alma; porque sin "
             "duda a causa de alguna tentación o de alguna falta que tú "
             "ignoras recibes más tarde tu petición.",
    (39, 8): "Tú, pues, no ceses de pedir la petición de tu alma, y la "
             "recibirás; mas si desfalleces y tienes doble ánimo al pedir, "
             "cúlpate a ti mismo y no al que te da.",
    (39, 9): "Mira esta doblez de ánimo; porque es mala e insensata, y "
             "desarraiga de la fe a muchos, y aun a los muy fieles y fuertes. "
             "Porque esta doblez de ánimo es hija del diablo, y obra con gran "
             "malicia contra los siervos de Dios.",
    (39, 10): "Desprecia, pues, la doblez de ánimo y enseñoréate de ella en "
              "todo asunto, vistiéndote de la fe fuerte y poderosa; porque la "
              "fe todo lo promete, todo lo perfecciona; mas la doblez de "
              "ánimo, no confiando en sí misma, fracasa en todas las obras "
              "que hace.",
    (39, 11): "Ves, pues, dice, que la fe es de arriba, del Señor, y tiene "
              "gran poder; mas la doblez de ánimo es espíritu terreno, del "
              "diablo, que no tiene poder.",
    (39, 12): "Tú, pues, sirve a la fe, que tiene poder, y apártate de la "
              "doblez de ánimo, que no tiene poder, y vivirás para Dios; y "
              "todos los que piensan así vivirán para Dios.",

    # Capítulo 40
    (40, 1): "Quita de ti, dice, la tristeza; porque también ella es hermana "
             "de la doblez de ánimo y de la ira.",
    (40, 2): "¿Cómo, digo, señor, es hermana de estas? Porque me parece que "
             "una cosa es la ira, y otra la doblez de ánimo, y otra la "
             "tristeza. Insensato eres, oh hombre, dice, ¿y no entiendes que "
             "la tristeza es más mala que todos los espíritus, y la más "
             "terrible para los siervos de Dios, y más que todos los "
             "espíritus corrompe al hombre, y quebranta al Espíritu Santo, y "
             "a su vez salva?",
    (40, 3): "Yo, digo, señor, soy insensato y no entiendo estas parábolas. "
             "Porque ¿cómo puede quebrantar y a su vez salvar? No lo "
             "entiendo.",
    (40, 4): "Oye, dice: los que nunca han investigado acerca de la verdad, "
             "ni han inquirido acerca de la divinidad, sino que solamente han "
             "creído, y están enredados en negocios y riquezas y amistades de "
             "gentiles y en otros muchos negocios de este siglo; cuantos, "
             "pues, están apegados a estas cosas, no entienden las parábolas "
             "de la divinidad; porque son oscurecidos por estas ocupaciones y "
             "se corrompen y se vuelven yermos.",
    (40, 5): "Así como las viñas buenas, cuando son descuidadas, se vuelven "
             "yermas por las espinas y diversas hierbas, así los hombres que "
             "han creído y caen en estas muchas ocupaciones antes dichas se "
             "extravían de su entendimiento y no entienden nada en absoluto "
             "acerca de la justicia; antes bien, aun cuando oyen acerca de la "
             "divinidad y de la verdad, su mente está ocupada en sus "
             "negocios, y no entienden nada en absoluto.",
    (40, 6): "Mas los que tienen temor de Dios e investigan acerca de la "
             "divinidad y de la verdad, y tienen el corazón vuelto hacia el "
             "Señor, entienden y comprenden con más presteza todo lo que se "
             "les dice, porque tienen en sí el temor del Señor; porque donde "
             "mora el Señor, allí hay también mucho entendimiento. Allégate, "
             "pues, al Señor, y todo lo comprenderás y entenderás.",

    # Capítulo 41
    (41, 1): "Oye, pues, dice, oh necio, cómo la tristeza quebranta al "
             "Espíritu Santo y a su vez salva.",
    (41, 2): "Cuando el de doble ánimo emprende alguna obra y fracasa en ella "
             "a causa de su doblez de ánimo, esta tristeza entra en el hombre "
             "y contrista al Espíritu Santo y lo quebranta.",
    (41, 3): "Después, a su vez, cuando la ira se apega al hombre por algún "
             "asunto, y se amarga mucho, otra vez la tristeza entra en el "
             "corazón del hombre que se airó, y se entristece por la acción "
             "que hizo, y se arrepiente porque obró el mal.",
    (41, 4): "Esta tristeza, pues, parece traer salvación, porque, habiendo "
             "hecho el mal, se arrepintió. Ambas acciones, pues, contristan "
             "al Espíritu: la doblez de ánimo, porque no logró su obra; y la "
             "ira contrista al Espíritu, porque hizo el mal. Ambas, pues, son "
             "causa de tristeza para el Espíritu Santo, la doblez de ánimo y "
             "la ira.",
    (41, 5): "Quita, pues, de ti la tristeza, y no aflijas al Espíritu Santo "
             "que mora en ti, no sea que interceda ante Dios contra ti y se "
             "aparte de ti.",
    (41, 6): "Porque el Espíritu de Dios que fue dado a esta carne no soporta "
             "la tristeza ni la angustia.",

    # Capítulo 42
    (42, 1): "Vístete, pues, de la alegría, que siempre halla gracia delante "
             "de Dios y le es acepta, y deléitate en ella. Porque todo varón "
             "alegre obra lo bueno, y piensa lo bueno, y desprecia la "
             "tristeza.",
    (42, 2): "Mas el varón triste siempre obra el mal: primeramente obra el "
             "mal, porque contrista al Espíritu Santo, que fue dado alegre al "
             "hombre; y en segundo lugar, contristando al Espíritu Santo, "
             "obra iniquidad, no orando ni confesando al Señor. Porque la "
             "oración del varón triste nunca tiene poder para subir al altar "
             "de Dios.",
    (42, 3): "¿Por qué, digo, no sube al altar la oración del que está "
             "triste? Porque, dice, la tristeza está asentada en su corazón. "
             "Mezclada, pues, la tristeza con la oración, no deja que la "
             "oración suba pura al altar. Porque así como el vinagre y el "
             "vino, mezclados en uno, no tienen el mismo sabor, así también "
             "la tristeza, mezclada con el Espíritu Santo, no tiene la misma "
             "oración.",
    (42, 4): "Límpiate, pues, de esta mala tristeza, y vivirás para Dios; y "
             "todos cuantos echen de sí la tristeza y se vistan de toda "
             "alegría vivirán para Dios.",

    # Capítulo 43
    (43, 1): "Me mostró unos hombres sentados sobre un banco, y otro hombre "
             "sentado en una silla, y me dice: ¿Ves a los que están sentados "
             "sobre el banco? Veo, digo, señor. Estos, dice, son fieles, y el "
             "que está sentado en la silla es un falso profeta, que destruye "
             "el entendimiento de los siervos de Dios; pero destruye el de "
             "los de doble ánimo, no el de los fieles.",
    (43, 2): "Estos de doble ánimo, pues, vienen a él como a un adivino, y le "
             "preguntan qué les sucederá; y aquel falso profeta, no teniendo "
             "en sí ningún poder de espíritu divino, les habla conforme a sus "
             "preguntas y conforme a los deseos de su maldad, y llena sus "
             "almas como ellos mismos quieren.",
    (43, 3): "Porque, siendo él vacío, también responde cosas vacías a los "
             "vacíos; porque cualquier cosa que se le pregunte, responde "
             "conforme a la vaciedad del hombre. Pero también dice algunas "
             "palabras verdaderas; porque el diablo lo llena de su propio "
             "espíritu, por si puede quebrantar a alguno de los justos.",
    (43, 4): "Cuantos, pues, son fuertes en la fe del Señor, vestidos de la "
             "verdad, no se allegan a tales espíritus, sino que se apartan de "
             "ellos; mas cuantos son de doble ánimo y se arrepienten a "
             "menudo, consultan adivinos como también los gentiles, y atraen "
             "sobre sí mayor pecado, cometiendo idolatría; porque el que "
             "pregunta a un falso profeta acerca de algún asunto es idólatra, "
             "y vacío de la verdad, e insensato.",
    (43, 5): "Porque ningún espíritu dado por Dios es consultado, sino que, "
             "teniendo el poder de la divinidad, lo habla todo por sí mismo, "
             "porque es de arriba, del poder del espíritu divino.",
    (43, 6): "Mas el espíritu que es consultado y habla conforme a los deseos "
             "de los hombres es terreno y liviano, y no tiene poder; y no "
             "habla en absoluto si no es preguntado.",
    (43, 7): "¿Cómo, pues, digo, señor, sabrá un hombre cuál de ellos es "
             "profeta y cuál falso profeta? Oye, dice, acerca de ambos "
             "profetas; y como voy a decirte, así probarás al profeta y al "
             "falso profeta. Por la vida prueba al hombre que tiene el "
             "espíritu divino.",
    (43, 8): "Primeramente, el que tiene el espíritu de arriba es manso y "
             "sosegado y humilde, y se aparta de toda maldad y del vano deseo "
             "de este siglo, y se hace más necesitado que todos los hombres, "
             "y no responde nada a nadie cuando es preguntado, ni habla a "
             "solas; ni habla el Espíritu Santo cuando el hombre quiere "
             "hablar, sino que habla entonces, cuando Dios quiere que hable.",
    (43, 9): "Cuando, pues, el hombre que tiene el espíritu divino viene a "
             "una asamblea de varones justos que tienen fe en el espíritu "
             "divino, y se hace oración a Dios por la asamblea de aquellos "
             "varones, entonces el ángel del espíritu profético que está "
             "puesto sobre él llena al hombre, y el hombre, lleno del "
             "Espíritu Santo, habla a la multitud como el Señor quiere.",
    (43, 10): "Así, pues, será manifiesto el espíritu de la divinidad. Tal "
              "es, pues, el poder del Señor en lo que toca al espíritu de la "
              "divinidad.",
    (43, 11): "Oye ahora, dice, acerca del espíritu terreno y vacío, que no "
              "tiene poder, sino que es necio.",
    (43, 12): "Primeramente, aquel hombre que parece tener espíritu se "
              "ensalza a sí mismo y quiere tener el primer asiento, y en "
              "seguida es atrevido y desvergonzado y hablador, y vive en "
              "muchos deleites y en otros muchos engaños, y recibe paga por "
              "su profecía; y si no la recibe, no profetiza. ¿Puede, pues, un "
              "espíritu divino recibir paga y profetizar? No es posible que "
              "un profeta de Dios haga esto, sino que el espíritu de tales "
              "profetas es terreno.",
    (43, 13): "Después, no se acerca en absoluto a la asamblea de los varones "
              "justos, sino que huye de ellos; y se allega a los de doble "
              "ánimo y a los vacíos, y les profetiza en un rincón, y los "
              "engaña hablándoles todo vanamente conforme a sus deseos; "
              "porque también a vacíos responde. Porque el vaso vacío, puesto "
              "con los vacíos, no se quiebra, sino que concuerdan unos con "
              "otros.",
    (43, 14): "Mas cuando viene a una asamblea llena de varones justos que "
              "tienen espíritu de divinidad, y se hace oración por ellos, "
              "aquel hombre queda vacío, y el espíritu terreno huye de él por "
              "el temor, y aquel hombre enmudece y queda del todo "
              "quebrantado, sin poder hablar nada.",
    (43, 15): "Porque si en una bodega almacenas vino o aceite, y pones entre "
              "ellos una vasija vacía, y luego quieres vaciar la bodega, "
              "aquella vasija que pusiste vacía, vacía también la hallarás; "
              "así también los profetas vacíos, cuando vienen a los espíritus "
              "de los justos, tales como vinieron, tales se hallan.",
    (43, 16): "Tienes la vida de ambos profetas. Prueba, pues, por las obras "
              "y por la vida al hombre que dice ser portador del Espíritu.",
    (43, 17): "Y tú cree al espíritu que viene de Dios y tiene poder; mas al "
              "espíritu terreno y vacío no le creas en nada, porque no hay "
              "poder en él; porque viene del diablo.",
    (43, 18): "Oye, pues, la parábola que voy a decirte: toma una piedra y "
              "arrójala al cielo; mira si puedes alcanzarlo. O también, toma "
              "una jeringa de agua y lánzala al cielo; mira si puedes horadar "
              "el cielo.",
    (43, 19): "¿Cómo, digo, señor, pueden hacerse estas cosas? Porque ambas "
              "cosas que has dicho son imposibles. Así como estas cosas, "
              "pues, dice, son imposibles, así también los espíritus terrenos "
              "son impotentes y sin fuerza.",
    (43, 20): "Toma, pues, el poder que viene de arriba: el granizo es un "
              "granito pequeñísimo, y cuando cae sobre la cabeza de un "
              "hombre, ¡cómo causa dolor! O también, toma una gota que cae "
              "del tejado al suelo y horada la piedra.",
    (43, 21): "Ves, pues, que las cosas más pequeñas que caen de arriba sobre "
              "la tierra tienen gran poder; así también el espíritu divino "
              "que viene de arriba es poderoso. A este espíritu, pues, cree, "
              "y del otro apártate.",

    # Capítulo 44
    (44, 1): "Me dice: Quita de ti todo mal deseo, y vístete del deseo bueno "
             "y venerable; porque, vestido de este deseo, aborrecerás el mal "
             "deseo y lo refrenarás como quieras.",
    (44, 2): "Porque el mal deseo es fiero y difícilmente se amansa. Porque "
             "es terrible, y con su fiereza consume en gran manera a los "
             "hombres; y sobre todo, si un siervo de Dios cae en él y no es "
             "prudente, es consumido por él terriblemente. Y consume a los "
             "tales, que no tienen el vestido del deseo bueno, sino que están "
             "enredados en este siglo; a estos, pues, los entrega a la "
             "muerte.",
    (44, 3): "¿Cuáles son, digo, señor, las obras del mal deseo que entregan "
             "a los hombres a la muerte? Házmelas saber, para que me aparte "
             "de ellas. Oye, dice, en qué obras el mal deseo da muerte a los "
             "siervos de Dios.",

    # Capítulo 45
    (45, 1): "Sobre todos está el deseo de mujer ajena o de marido ajeno, y "
             "del lujo de la riqueza, y de muchas comidas vanas, y de "
             "bebidas, y de otros muchos deleites necios; porque todo deleite "
             "es necio y vano para los siervos de Dios.",
    (45, 2): "Estos deseos, pues, son malos, y dan muerte a los siervos de "
             "Dios; porque este mal deseo es hija del diablo. Es necesario, "
             "pues, apartarse de los malos deseos, para que, apartándoos, "
             "viváis para Dios.",
    (45, 3): "Mas cuantos sean dominados por ellos y no les resistan, morirán "
             "para siempre; porque estos deseos son mortíferos.",
    (45, 4): "Mas tú vístete del deseo de la justicia, y armándote del temor "
             "del Señor, resísteles; porque el temor de Dios mora en el deseo "
             "bueno. Si el mal deseo te ve armado del temor de Dios y "
             "resistiéndole, huirá lejos de ti y no te será visto más, "
             "temiendo tus armas.",
    (45, 5): "Tú, pues, vencedor y coronado sobre él, ve al deseo de la "
             "justicia, y entregándole la victoria que recibiste, sírvele "
             "como él quiere. Si sirves al deseo bueno y te sometes a él, "
             "podrás enseñorearte del mal deseo y sujetarlo como quieras.",

    # Capítulo 46
    (46, 1): "Quisiera, dije, señor, saber de qué maneras debo servir al "
             "deseo bueno. Oye, dijo: obra justicia y virtud, verdad y temor "
             "del Señor, fe y mansedumbre, y cuantos bienes son semejantes a "
             "estos. Obrando estas cosas serás siervo agradable a Dios y "
             "vivirás para él; y todo aquel que sirva al deseo bueno vivirá "
             "para Dios.",
    (46, 2): "Acabó, pues, los doce mandamientos, y me dice: Tienes estos "
             "mandamientos; anda en ellos, y exhorta a los que los oyen, para "
             "que su penitencia sea pura los días que quedan de su vida.",
    (46, 3): "Este ministerio que te doy, cúmplelo con diligencia, y harás "
             "mucho; porque hallarás gracia entre los que han de "
             "arrepentirse, y ellos obedecerán tus palabras; porque yo estaré "
             "contigo y los obligaré a obedecerte.",
    (46, 4): "Le digo: Señor, estos mandamientos son grandes, y hermosos, y "
             "gloriosos, y capaces de alegrar el corazón del hombre que pueda "
             "guardarlos. Pero no sé si estos mandamientos pueden ser "
             "guardados por hombre, porque son muy duros.",
    (46, 5): "Respondiendo, me dice: Si tú te propones que pueden ser "
             "guardados, fácilmente los guardarás y no serán duros; mas si ya "
             "ha subido a tu corazón que no pueden ser guardados por hombre, "
             "no los guardarás.",
    (46, 6): "Pero ahora te digo: si no los guardas, sino que los descuidas, "
             "no tendrás salvación, ni tus hijos, ni tu casa, pues ya has "
             "juzgado para contigo mismo que estos mandamientos no pueden ser "
             "guardados por hombre.",

    # Capítulo 47
    (47, 1): "Y estas cosas me las habló muy airado, de modo que quedé "
             "confundido y le temí en gran manera; porque su figura se "
             "transformó, de suerte que un hombre no podía soportar su ira.",
    (47, 2): "Mas viéndome todo turbado y confundido, comenzó a hablarme con "
             "más blandura y alegría, y dice: Insensato, sin entendimiento y "
             "de doble ánimo, ¿no entiendes la gloria de Dios, cuán grande "
             "es, y fuerte, y admirable, que creó el mundo por causa del "
             "hombre, y sujetó toda su creación al hombre, y le dio toda "
             "potestad para señorear sobre todas las cosas que están debajo "
             "del cielo?",
    (47, 3): "Si, pues, dijo, el hombre es señor de todas las criaturas de "
             "Dios y señorea sobre todas, ¿no puede también señorear sobre "
             "estos mandamientos? Puede, dijo, señorear sobre todas las cosas "
             "y sobre todos estos mandamientos el hombre que tiene al Señor "
             "en su corazón.",
    (47, 4): "Mas los que tienen al Señor en los labios, pero su corazón "
             "endurecido, y están lejos del Señor, para esos estos "
             "mandamientos son duros e intransitables.",
    (47, 5): "Poned, pues, vosotros, los que sois vanos y livianos en la fe, "
             "a vuestro Señor en el corazón, y conoceréis que nada hay más "
             "fácil que estos mandamientos, ni más dulce, ni más manso.",
    (47, 6): "Convertíos vosotros los que andáis en los mandamientos del "
             "diablo, los difíciles, y amargos, y salvajes, y disolutos, y no "
             "temáis al diablo, porque en él no hay poder contra vosotros;",
    (47, 7): "porque yo estaré con vosotros, el ángel de la penitencia, que "
             "señoreo sobre él. El diablo solo tiene temor, pero su temor no "
             "tiene vigor; no le temáis, pues, y huirá de vosotros.",

    # Capítulo 48
    (48, 1): "Le digo: Señor, óyeme unas pocas palabras. Di, dijo, lo que "
             "quieras. El hombre, dije, señor, está pronto a guardar los "
             "mandamientos de Dios, y no hay nadie que no pida al Señor ser "
             "fortalecido en sus mandamientos y sujetarse a ellos; pero el "
             "diablo es duro y los tiraniza.",
    (48, 2): "No puede, dijo, tiranizar a los siervos de Dios que de todo "
             "corazón esperan en él. El diablo puede luchar contra ellos, "
             "pero derribarlos no puede. Si, pues, le resistís, vencido huirá "
             "de vosotros avergonzado. Pero cuantos, dijo, están medio vacíos "
             "temen al diablo como si tuviera poder.",
    (48, 3): "Cuando un hombre ha llenado muchísimas tinajas de buen vino, y "
             "entre aquellas tinajas hay unas pocas medio vacías, viene a las "
             "tinajas y no examina las llenas, porque sabe que están llenas; "
             "mas examina las medio vacías, temiendo que se hayan agriado; "
             "porque pronto se agrian las tinajas medio vacías, y se pierde "
             "el gusto del vino.",
    (48, 4): "Así también el diablo viene a todos los siervos de Dios "
             "tentándolos. Cuantos, pues, están llenos en la fe le resisten "
             "fuertemente, y él se aparta de ellos, no teniendo lugar por "
             "donde entrar. Viene entonces a los medio vacíos, y teniendo "
             "lugar entra en ellos, y hace en ellos lo que quiere, y se le "
             "vuelven esclavos.",

    # Capítulo 49
    (49, 1): "Mas yo os digo, el ángel de la penitencia: no temáis al diablo. "
             "Porque fui enviado, dijo, para estar con vosotros los que os "
             "arrepentís de todo vuestro corazón, y para fortaleceros en la "
             "fe.",
    (49, 2): "Creed, pues, a Dios, vosotros que por vuestros pecados habéis "
             "desesperado de vuestra vida, y añadís pecados, y hacéis pesada "
             "vuestra vida, que si os volvéis al Señor de todo vuestro "
             "corazón, y obráis la justicia los días que quedan de vuestra "
             "vida, y le servís rectamente conforme a su voluntad, él dará "
             "sanidad a vuestros pecados anteriores, y tendréis poder para "
             "señorear sobre las obras del diablo. Y la amenaza del diablo no "
             "la temáis en absoluto, porque no tiene vigor, como los nervios "
             "de un muerto.",
    (49, 3): "Oídme, pues, y temed a aquel que todo lo puede, salvar y "
             "destruir, y guardad estos mandamientos, y viviréis para Dios.",
    (49, 4): "Le digo: Señor, ahora he sido fortalecido en todas las "
             "ordenanzas del Señor, porque tú estás conmigo; y sé que "
             "quebrantarás todo el poder del diablo, y nosotros señorearemos "
             "sobre él y prevaleceremos sobre todas sus obras. Y espero, "
             "señor, poder guardar estos mandamientos que has mandado, "
             "fortaleciéndome el Señor.",
    (49, 5): "Los guardarás, dijo, si tu corazón se hace puro para con el "
             "Señor; y también los guardarán todos cuantos purifiquen sus "
             "corazones de los vanos deseos de este siglo, y vivirán para "
             "Dios.",

    # Capítulo 50
    (50, 1): "Me dice: Sabéis, dijo, que vosotros, los siervos de Dios, "
             "habitáis en tierra extraña; porque vuestra ciudad está lejos de "
             "esta ciudad. Si, pues, conocéis, dijo, vuestra ciudad, en la "
             "cual habéis de habitar, ¿por qué os preparáis aquí campos, y "
             "aparatos costosos, y edificios, y moradas vanas?",
    (50, 2): "El que prepara estas cosas para esta ciudad no puede volver a "
             "su propia ciudad.",
    (50, 3): "Hombre insensato, y de doble ánimo, y miserable, ¿no entiendes "
             "que todas estas cosas son ajenas y están bajo la potestad de "
             "otro? Porque dirá el señor de esta ciudad: No quiero que "
             "habites en mi ciudad; sal de esta ciudad, porque no te sirves "
             "de mis leyes.",
    (50, 4): "Tú, pues, que tienes campos, y moradas, y muchas otras "
             "posesiones, cuando seas echado por él, ¿qué harás de tu campo, "
             "y de tu casa, y de todo lo demás que te preparaste? Porque te "
             "dice con justicia el señor de esta tierra: O te sirves de mis "
             "leyes, o sal de mi tierra.",
    (50, 5): "Tú, pues, ¿qué vas a hacer, teniendo una ley en tu ciudad? ¿Por "
             "causa de tus campos y de tus demás posesiones negarás del todo "
             "tu ley, y andarás según la ley de esta ciudad? Mira que no te "
             "conviene negar tu ley; porque si quieres volver a tu ciudad, no "
             "serás recibido, porque negaste la ley de tu ciudad, y te será "
             "cerrada.",
    (50, 6): "Mira, pues, tú: como quien habita en tierra extraña, no te "
             "prepares nada más que lo suficiente que te baste; y está "
             "preparado, para que, cuando el dueño de esta ciudad quiera "
             "echarte por haberte opuesto a su ley, salgas de su ciudad y te "
             "vayas a tu ciudad, y te sirvas de tu ley sin afrenta, "
             "regocijándote.",
    (50, 7): "Mirad, pues, vosotros los que servís al Señor y le tenéis en el "
             "corazón: obrad las obras de Dios, acordándoos de sus "
             "mandamientos y de las promesas que prometió, y creedle que las "
             "cumplirá, si sus mandamientos son guardados.",
    (50, 8): "En lugar de campos, pues, comprad almas afligidas, según cada "
             "uno pueda, y visitad a las viudas y a los huérfanos, y no los "
             "desatendáis; y gastad vuestra riqueza y todos vuestros "
             "aparatos, que recibisteis de Dios, en tales campos y casas.",
    (50, 9): "Porque para esto os enriqueció el Señor, para que le cumpláis "
             "estos ministerios. Mucho mejor es comprar tales campos, y "
             "posesiones, y casas, que hallarás en tu ciudad cuando llegues a "
             "morar en ella.",
    (50, 10): "Este lujo es bueno y santo, que no tiene tristeza ni temor, "
              "sino que tiene gozo. No practiquéis, pues, el lujo de los "
              "gentiles, porque no os conviene a vosotros, los siervos de "
              "Dios.",
    (50, 11): "Mas practicad vuestro propio lujo, en el cual podéis gozaros; "
              "y no falsifiquéis, ni toquéis lo ajeno, ni lo codiciéis; "
              "porque malo es codiciar lo ajeno. Mas haz tu propia obra, y "
              "serás salvo.",

    # Capítulo 51
    (51, 1): "Andando yo por el campo, y considerando un olmo y una vid, y "
             "discurriendo acerca de ellos y de sus frutos, se me aparece el "
             "pastor y dice: ¿Qué buscas en ti mismo acerca del olmo y de la "
             "vid? Discurro, dije, señor, que se convienen muy bien el uno a "
             "la otra.",
    (51, 2): "Estos dos árboles, dijo, están puestos como figura para los "
             "siervos de Dios. Quisiera, dije, conocer la figura de estos "
             "árboles de que hablas. ¿Ves, dijo, el olmo y la vid? Los veo, "
             "dije, señor.",
    (51, 3): "Esta vid, dijo, lleva fruto, mas el olmo es un árbol sin fruto; "
             "pero esta vid, si no sube sobre el olmo, no puede dar mucho "
             "fruto, tendida en el suelo, y el fruto que lleva, lo lleva "
             "podrido, por no estar colgada del olmo. Cuando, pues, la vid se "
             "echa sobre el olmo, da fruto de sí misma y también por el olmo.",
    (51, 4): "Ves, pues, que también el olmo da mucho fruto, no menos que la "
             "vid, sino antes más. ¿Cómo más, señor?, dije. Porque, dijo, la "
             "vid colgada del olmo da su fruto abundante y hermoso, pero "
             "tendida en el suelo lo lleva escaso y podrido. Esta semejanza, "
             "pues, está puesta para los siervos de Dios, para el pobre y el "
             "rico.",
    (51, 5): "¿Cómo, señor?, dije; házmelo saber. Oye, dijo: el rico tiene "
             "bienes, pero en las cosas del Señor es pobre, distraído en "
             "torno a su riqueza, y tiene muy poca oración y confesión para "
             "con el Señor, y la que tiene es floja, y pequeña, y sin otra "
             "fuerza. Cuando, pues, el rico se apoya en el pobre y le "
             "suministra lo necesario, cree que, si obra en favor del pobre, "
             "podrá hallar la recompensa delante de Dios; porque el pobre es "
             "rico en la oración y en la confesión, y su oración tiene gran "
             "poder delante de Dios. Suministra, pues, el rico al pobre todas "
             "las cosas sin vacilar.",
    (51, 6): "Y el pobre, sustentado por el rico, intercede ante Dios dándole "
             "gracias por el que le da; y aquel se afana todavía más por el "
             "pobre, para que no le falte nada en su vida; porque sabe que la "
             "oración del pobre es acepta y rica delante del Señor.",
    (51, 7): "Ambos, pues, cumplen la obra: el pobre obra con la oración, en "
             "la cual es rico, la cual recibió del Señor; esta la devuelve al "
             "Señor que le suministra. Y el rico, asimismo, la riqueza que "
             "recibió del Señor la da sin vacilar al pobre. Y esta es obra "
             "grande y acepta delante de Dios, porque entendió acerca de su "
             "riqueza, y obró en favor del pobre de los dones del Señor, y "
             "cumplió rectamente el ministerio.",
    (51, 8): "Entre los hombres, pues, parece que el olmo no lleva fruto, y "
             "no saben ni entienden que, cuando viene la sequía, el olmo, que "
             "tiene agua, nutre a la vid, y la vid, teniendo agua sin cesar, "
             "da doble fruto, por sí misma y por el olmo. Así también los "
             "pobres, intercediendo ante el Señor por los ricos, colman la "
             "riqueza de ellos; y a su vez los ricos, suministrando a los "
             "pobres lo necesario, colman las oraciones de ellos.",
    (51, 9): "Ambos, pues, se hacen partícipes de la obra justa. El que hace "
             "estas cosas no será desamparado por Dios, sino que estará "
             "escrito en los libros de los vivientes.",
    (51, 10): "Bienaventurados los que tienen y entienden que son "
              "enriquecidos por el Señor; porque el que entiende esto podrá "
              "también hacer algún bien.",

    # Capítulo 52
    (52, 1): "Me mostró muchos árboles que no tenían hojas, sino que me "
             "parecían como secos; porque todos eran semejantes. Y me dice: "
             "¿Ves estos árboles? Los veo, dije, señor, semejantes y secos. "
             "Respondiendo, me dice: Estos árboles que ves son los que "
             "habitan en este siglo.",
    (52, 2): "¿Por qué, pues, dije, señor, están como secos y semejantes? "
             "Porque, dijo, ni los justos ni los pecadores se distinguen en "
             "este siglo, sino que son semejantes; porque este siglo es "
             "invierno para los justos, y no se distinguen, pues habitan con "
             "los pecadores.",
    (52, 3): "Porque así como en el invierno los árboles, habiendo perdido "
             "las hojas, son semejantes, y no se distingue cuáles son los "
             "secos y cuáles los vivos, así en este siglo no se distinguen ni "
             "los justos ni los pecadores, sino que todos son semejantes.",

    # Capítulo 53
    (53, 1): "Me mostró otra vez muchos árboles, unos que brotaban y otros "
             "secos, y me dice: ¿Ves, dijo, estos árboles? Los veo, dije, "
             "señor, unos brotando y otros secos.",
    (53, 2): "Estos árboles que brotan, dijo, son los justos que han de "
             "habitar en el siglo venidero; porque el siglo venidero es "
             "verano para los justos, y para los pecadores invierno. Cuando, "
             "pues, resplandezca la misericordia del Señor, entonces serán "
             "manifestados los que sirven a Dios, y todos serán manifestados.",
    (53, 3): "Porque así como en el verano se manifiestan los frutos de cada "
             "árbol, y se conoce de qué clase son, así también los frutos de "
             "los justos serán manifiestos, y todos serán conocidos, lozanos "
             "en aquel siglo.",
    (53, 4): "Mas los gentiles y los pecadores, que son los árboles secos que "
             "viste, tales serán hallados, secos y sin fruto, en aquel siglo, "
             "y como leña serán quemados, y será manifiesto que su conducta "
             "fue mala en su vida. Porque los pecadores serán quemados porque "
             "pecaron y no se arrepintieron; y los gentiles serán quemados "
             "porque no conocieron al que los creó.",
    (53, 5): "Tú, pues, da fruto, para que en aquel verano sea conocido tu "
             "fruto; y abstente de muchos negocios, y en nada pecarás. Porque "
             "los que hacen muchos negocios, también pecan mucho, distraídos "
             "en torno a sus negocios y sin servir en nada a su Señor.",
    (53, 6): "¿Cómo, pues, dijo, podrá el tal pedir algo al Señor y "
             "recibirlo, no sirviendo al Señor? Los que le sirven, esos "
             "recibirán sus peticiones; mas los que no sirven al Señor, esos "
             "nada recibirán.",
    (53, 7): "Pero si uno se ocupa en un solo negocio, puede también servir "
             "al Señor; porque su entendimiento no será corrompido "
             "apartándose del Señor, sino que le servirá teniendo su "
             "entendimiento puro.",
    (53, 8): "Si, pues, haces estas cosas, puedes dar fruto para el siglo "
             "venidero; y cualquiera que haga estas cosas dará fruto.",

    # Capítulo 54
    (54, 1): "Estando yo ayunando y sentado en cierto monte, y dando gracias "
             "al Señor por todas las cosas que había hecho conmigo, veo al "
             "pastor sentado junto a mí, y que me dice: ¿Por qué has venido "
             "aquí tan de mañana? Porque, dije, señor, tengo estación.",
    (54, 2): "¿Qué es, dijo, estación? Ayuno, dije, señor. ¿Y qué ayuno es "
             "este, dijo, que ayunáis? Como acostumbraba, dije, señor, así "
             "ayuno.",
    (54, 3): "No sabéis, dijo, ayunar al Señor, y no es ayuno este ayuno "
             "inútil que le ayunáis. ¿Por qué, dije, señor, dices esto? Te "
             "digo, dijo, que no es ayuno este que pensáis ayunar; pero yo te "
             "enseñaré qué es ayuno acepto y cumplido para el Señor. Oye, "
             "dijo.",
    (54, 4): "Dios no quiere tal ayuno vano; porque ayunando así a Dios nada "
             "obrarás para la justicia. Mas ayuna a Dios un ayuno como este:",
    (54, 5): "No hagas mal ninguno en tu vida, sino sirve al Señor con "
             "corazón puro; guarda sus mandamientos, andando en sus "
             "preceptos, y no suba a tu corazón ningún deseo malo; y cree a "
             "Dios que, si obras estas cosas, y le temes, y te abstienes de "
             "toda mala acción, vivirás para Dios; y si obras estas cosas, "
             "harás un gran ayuno, y acepto a Dios.",

    # Capítulo 55
    (55, 1): "Oye la semejanza que voy a decirte, que atañe al ayuno.",
    (55, 2): "Tenía uno un campo y muchos siervos, y en una parte del campo "
             "plantó una viña; y escogiendo a un siervo fiel, y agradable, y "
             "estimado, lo llamó y le dice: Toma esta viña que he plantado, y "
             "ponle estacas hasta que yo venga, y no hagas otra cosa a la "
             "viña; y guarda este mandamiento mío, y serás libre en mi casa. "
             "Y salió el señor del siervo a su viaje.",
    (55, 3): "Habiendo él salido, tomó el siervo y puso estacas a la viña. Y "
             "acabada la estacada de la viña, vio que la viña estaba llena de "
             "hierbas.",
    (55, 4): "Razonó, pues, en sí mismo, diciendo: Este mandamiento del señor "
             "lo he cumplido; ahora cavaré esta viña, y estará más hermosa "
             "cavada, y no teniendo hierbas dará más fruto, no siendo ahogada "
             "por las hierbas. Tomando, cavó la viña, y arrancó todas las "
             "hierbas que había en la viña. Y aquella viña quedó hermosísima "
             "y lozana, no teniendo hierbas que la ahogasen.",
    (55, 5): "Pasado un tiempo vino el señor del siervo y del campo, y entró "
             "en la viña. Y viendo la viña hermosamente estacada, y además "
             "cavada, y todas las hierbas arrancadas, y las vides lozanas, se "
             "gozó mucho de las obras del siervo.",
    (55, 6): "Llamando, pues, a su hijo amado, a quien tenía por heredero, y "
             "a los amigos que tenía por consejeros, les dice cuanto había "
             "mandado a su siervo y cuanto había hallado hecho. Y ellos se "
             "congratularon con el siervo por el testimonio que el señor dio "
             "de él.",
    (55, 7): "Y les dice: Yo prometí a este siervo la libertad si guardaba mi "
             "mandamiento que le mandé; y guardó mi mandamiento, y añadió a "
             "la viña una buena obra, y me agradó mucho. Por esta obra que "
             "hizo, pues, quiero hacerle coheredero con mi hijo, porque, "
             "habiendo pensado lo bueno, no lo descuidó, sino que lo cumplió.",
    (55, 8): "En este parecer el hijo del señor consintió con él, que el "
             "siervo fuese hecho coheredero con el hijo.",
    (55, 9): "Pocos días después hizo un banquete, y le envió del banquete "
             "muchos manjares. Y recibiendo el siervo los manjares que le "
             "envió el señor, tomó lo que le bastaba, y lo demás lo repartió "
             "a sus consiervos.",
    (55, 10): "Y sus consiervos, recibiendo los manjares, se gozaron, y "
              "comenzaron a orar por él, para que hallase mayor gracia "
              "delante del señor, porque así se había portado con ellos.",
    (55, 11): "Todas estas cosas que habían sucedido las oyó su señor, y otra "
              "vez se gozó mucho de su proceder. Convocando otra vez el señor "
              "a los amigos y a su hijo, les contó el proceder del siervo, lo "
              "que había hecho con los manjares que había recibido; y ellos "
              "consintieron aún más en que el siervo fuese hecho coheredero "
              "con su hijo.",

    # Capítulo 56
    (56, 1): "Digo: Señor, yo no conozco estas semejanzas, ni puedo "
             "entenderlas si no me las declaras.",
    (56, 2): "Todo te lo declararé, dijo, y cuanto hable contigo.",
    (56, 3): "Te mostraré sus mandamientos; pero si haces algún bien fuera "
             "del mandamiento de Dios, te ganarás gloria más abundante, y "
             "serás más glorioso delante de Dios de lo que habías de ser. Si, "
             "pues, guardando los mandamientos de Dios, añades también estos "
             "servicios, te gozarás, si los guardas conforme a mi "
             "mandamiento.",
    (56, 4): "Le digo: Señor, lo que me mandes, lo guardaré; porque sé que tú "
             "estás conmigo. Estaré, dijo, contigo, porque tienes tal celo de "
             "hacer el bien; y estaré también, dijo, con todos cuantos tienen "
             "este celo.",
    (56, 5): "Este ayuno, dijo, guardándose los mandamientos del Señor, es "
             "muy bueno. Así, pues, guardarás este ayuno que vas a observar:",
    (56, 6): "Primero de todo, guárdate de toda palabra mala y de todo deseo "
             "malo, y purifica tu corazón de todas las vanidades de este "
             "siglo. Si guardas estas cosas, este ayuno será para ti "
             "perfecto.",
    (56, 7): "Y así harás: cumplido lo que está escrito, en aquel día en que "
             "ayunes no gustarás nada sino pan y agua; y de los manjares que "
             "habías de comer, calculando la cantidad del gasto de aquel día "
             "que habías de hacer, lo darás a una viuda, o a un huérfano, o a "
             "un necesitado; y así serás humilde, para que por tu humildad el "
             "que lo recibió sacie su alma y ore por ti al Señor.",
    (56, 8): "Si, pues, cumples así el ayuno, como te he mandado, tu "
             "sacrificio será acepto delante de Dios, y este ayuno quedará "
             "escrito; y el servicio que así se hace es bueno, y alegre, y "
             "agradable al Señor.",
    (56, 9): "Estas cosas las guardarás así tú con tus hijos y toda tu casa; "
             "y guardándolas serás bienaventurado; y cuantos, habiéndolas "
             "oído, las guarden, serán bienaventurados, y todo lo que pidan "
             "al Señor lo recibirán.",

    # Capítulo 57
    (57, 1): "Le rogué mucho que me declarase la semejanza del campo, y del "
             "señor, y de la viña, y del siervo que puso estacas a la viña, y "
             "de las estacas, y de las hierbas arrancadas de la viña, y del "
             "hijo, y de los amigos consejeros; porque entendí que todas "
             "estas cosas son una semejanza.",
    (57, 2): "Y él, respondiendo, me dijo: Eres muy atrevido en preguntar. No "
             "debes, dijo, preguntar nada en absoluto; porque si es menester "
             "que se te declare, se te declarará. Le digo: Señor, cuanto me "
             "muestres y no me declares, en vano lo habré visto, sin entender "
             "qué es; asimismo, si me hablas semejanzas y no me las declaras, "
             "en vano habré oído algo de ti.",
    (57, 3): "Y él me respondió otra vez, diciendo: Cualquiera, dijo, que sea "
             "siervo de Dios y tenga a su Señor en el corazón, le pide "
             "entendimiento y lo recibe, y declara toda semejanza, y le son "
             "conocidas las palabras del Señor dichas por semejanzas; mas "
             "cuantos son flojos y perezosos para la oración, esos vacilan en "
             "pedir al Señor;",
    (57, 4): "pero el Señor es muy misericordioso, y a todos los que le "
             "piden, les da sin cesar. Mas tú, que has sido fortalecido por "
             "el santo ángel, y has recibido de él tal oración, y no eres "
             "perezoso, ¿por qué no pides al Señor entendimiento y lo recibes "
             "de él?",
    (57, 5): "Le digo: Señor, teniéndote a ti conmigo, tengo necesidad de "
             "pedirte a ti y de preguntarte a ti; porque tú me muestras todas "
             "las cosas y hablas conmigo; pero si sin ti las viera u oyera, "
             "preguntaría al Señor para que me fuesen declaradas.",

    # Capítulo 58
    (58, 1): "Te dije, dijo, hace un momento, que eres astuto y atrevido, "
             "preguntando las declaraciones de las semejanzas. Pero ya que "
             "eres tan perseverante, te declararé la semejanza del campo y de "
             "todo lo demás que sigue, para que lo hagas conocer a todos. Oye "
             "ahora, dijo, y entiéndelo.",
    (58, 2): "El campo es este mundo; y el señor del campo es el que creó "
             "todas las cosas, y las perfeccionó, y les dio poder; y el "
             "siervo es el Hijo de Dios; y las vides son este pueblo que él "
             "mismo plantó;",
    (58, 3): "y las estacas son los santos ángeles del Señor, que mantienen "
             "unido a su pueblo; y las hierbas arrancadas de la viña son las "
             "iniquidades de los siervos de Dios; y los manjares que le envió "
             "del banquete son los mandamientos que dio a su pueblo por medio "
             "de su Hijo; y los amigos y consejeros son los santos ángeles "
             "que fueron creados primero; y el viaje del señor es el tiempo "
             "que queda hasta su venida.",
    (58, 4): "Le digo: Señor, todas las cosas son grandes y admirables, y "
             "todas son gloriosas. ¿Acaso, pues, dije, podía yo entender "
             "estas cosas? Ni otro alguno de los hombres, aunque sea muy "
             "entendido, puede entenderlas. Todavía, dije, señor, declárame "
             "lo que voy a preguntarte.",
    (58, 5): "Di, dijo, si algo quieres. ¿Por qué, dije, señor, el Hijo de "
             "Dios está puesto en la semejanza en figura de siervo?",

    # Capítulo 59
    (59, 1): "Oye, dijo: el Hijo de Dios no está puesto en figura de siervo, "
             "sino que está puesto en gran potestad y señorío. ¿Cómo, señor?, "
             "dije; no lo entiendo.",
    (59, 2): "Porque, dijo, Dios plantó la viña, esto es, creó al pueblo y lo "
             "entregó a su Hijo; y el Hijo puso a los ángeles sobre ellos "
             "para que los guardasen; y él mismo purificó sus pecados, "
             "trabajando mucho y soportando muchos trabajos; porque ninguna "
             "viña puede ser cavada sin trabajo o fatiga.",
    (59, 3): "Él, pues, habiendo purificado los pecados del pueblo, les "
             "mostró las sendas de la vida, dándoles la ley que recibió de su "
             "Padre.",
    (59, 4): "Y cómo el Señor tomó por consejeros a su Hijo y a los ángeles "
             "gloriosos acerca de la herencia del siervo, oye:",
    (59, 5): "El Espíritu Santo, que preexiste, que creó toda la creación, "
             "Dios lo hizo habitar en una carne que él quiso. Esta carne, "
             "pues, en la cual habitó el Espíritu Santo, sirvió bien al "
             "Espíritu, andando en honestidad y pureza, sin mancillar en nada "
             "al Espíritu.",
    (59, 6): "Habiendo, pues, ella vivido bien y castamente, y trabajado "
             "juntamente con el Espíritu, y cooperado en toda cosa, "
             "conduciéndose con fuerza y valentía, la escogió por compañera "
             "con el Espíritu Santo; porque agradó la conducta de esta carne, "
             "que no se mancilló sobre la tierra teniendo al Espíritu Santo.",
    (59, 7): "Tomó, pues, por consejeros al Hijo y a los ángeles gloriosos, "
             "para que también esta carne, que sirvió al Espíritu sin "
             "reprensión, tuviese algún lugar de morada y no pareciese haber "
             "perdido la recompensa de su servicio; porque toda carne que sea "
             "hallada sin mancilla y sin mancha, en la cual haya habitado el "
             "Espíritu Santo, recibirá recompensa.",
    (59, 8): "Tienes también la declaración de esta semejanza.",

    # Capítulo 60
    (60, 1): "Me he alegrado, dije, señor, al oír esta declaración. Oye "
             "ahora, dijo: guarda esta carne tuya pura y sin mancilla, para "
             "que el espíritu que habita en ella le dé testimonio, y tu carne "
             "sea justificada.",
    (60, 2): "Mira que no suba a tu corazón que esta carne tuya es "
             "corruptible, y abuses de ella en alguna contaminación. Si "
             "mancillas tu carne, mancillarás también al Espíritu Santo; y si "
             "mancillas la carne, no vivirás.",
    (60, 3): "Pero si ha habido, dije, señor, ignorancia anterior, antes que "
             "se oyesen estas palabras, ¿cómo se salvará el hombre que "
             "mancilló su carne? Acerca de las ignorancias anteriores, dijo, "
             "solo a Dios le es posible dar sanidad, porque suya es toda "
             "potestad,",
    (60, 4): "si en adelante no mancillas tu carne ni el espíritu; porque "
             "ambos son comunes, y no pueden ser mancillados el uno sin el "
             "otro. Guarda, pues, ambos puros, y vivirás para Dios.",

    # Capítulo 61
    (61, 1): "Estando sentado en mi casa, y glorificando al Señor por todas "
             "las cosas que había visto, y discurriendo acerca de los "
             "mandamientos, que son hermosos, y poderosos, y alegres, y "
             "gloriosos, y capaces de salvar el alma del hombre, decía en mí "
             "mismo: Bienaventurado seré si ando en estos mandamientos, y "
             "cualquiera que ande en ellos será bienaventurado.",
    (61, 2): "Mientras decía estas cosas en mí mismo, lo veo de repente "
             "sentado junto a mí, y que decía esto: ¿Por qué eres de doble "
             "ánimo acerca de los mandamientos que te he mandado? Son "
             "hermosos; no seas en absoluto de doble ánimo, sino vístete de "
             "la fe del Señor, y andarás en ellos; porque yo te fortaleceré "
             "en ellos.",
    (61, 3): "Estos mandamientos son provechosos para los que han de "
             "arrepentirse; porque si no andan en ellos, en vano es su "
             "penitencia.",
    (61, 4): "Vosotros, pues, los que os arrepentís, desechad las maldades de "
             "este siglo que os destruyen; y vestidos de toda virtud de "
             "justicia podréis guardar estos mandamientos y no añadir más a "
             "vuestros pecados. Andad, pues, en estos mandamientos míos, y "
             "viviréis para Dios. Todas estas cosas os han sido habladas por "
             "mí.",
    (61, 5): "Y después de hablar conmigo estas cosas, me dice: Vamos al "
             "campo, y te mostraré los pastores de las ovejas. Vamos, señor, "
             "dije. Y llegamos a una llanura, y me muestra un pastor joven "
             "vestido de un conjunto de vestiduras de color azafranado.",
    (61, 6): "Y apacentaba muchísimas ovejas, y estas ovejas estaban como "
             "regaladas y muy dadas a los placeres, y estaban alegres, "
             "saltando de aquí para allá; y el mismo pastor estaba muy alegre "
             "con su rebaño; y el mismo aspecto del pastor era muy alegre, y "
             "corría de un lado a otro entre las ovejas.",

    # Capítulo 62
    (62, 1): "Y me dice: ¿Ves a este pastor? Lo veo, dije, señor. Este, dijo, "
             "es el ángel del regalo y del engaño. Este destruye las almas de "
             "los siervos de Dios y los aparta de la verdad, engañándolos con "
             "los deseos malos, en los cuales perecen.",
    (62, 2): "Porque se olvidan de los mandamientos del Dios vivo, y andan en "
             "engaños y placeres vanos, y son destruidos por este ángel, unos "
             "para muerte, y otros para corrupción.",
    (62, 3): "Le digo: Señor, yo no sé qué es para muerte y qué para "
             "corrupción. Oye, dijo: las ovejas que viste alegres y saltando, "
             "estos son los que se han apartado de Dios para siempre y se han "
             "entregado a los deseos de este siglo. En estos, pues, no hay "
             "penitencia de vida, porque añadieron a sus pecados y "
             "blasfemaron contra el nombre de Dios. De los tales, pues, es la "
             "muerte.",
    (62, 4): "Y las ovejas que viste que no saltaban, sino que pacían en un "
             "mismo lugar, estos son los que se han entregado a los placeres "
             "y engaños, pero no blasfemaron en nada contra el Señor; estos, "
             "pues, están corrompidos, apartados de la verdad. En estos hay "
             "esperanza de penitencia, en la cual pueden vivir. La "
             "corrupción, pues, tiene esperanza de alguna renovación, mas la "
             "muerte tiene perdición eterna.",
    (62, 5): "Otra vez avancé un poco, y me muestra un pastor grande, como de "
             "aspecto salvaje, cubierto de una piel de cabra blanca; y tenía "
             "un zurrón sobre los hombros, y un cayado muy duro y lleno de "
             "nudos, y un gran látigo; y tenía la mirada muy amarga, de modo "
             "que tuve miedo de él: tal era su mirada.",
    (62, 6): "Este pastor, pues, recibía del pastor joven las ovejas, "
             "aquellas que se regalaban y vivían en placeres, pero no "
             "saltaban, y las echaba en un lugar escarpado, y lleno de "
             "espinos y abrojos, de modo que las ovejas no podían "
             "desenredarse de los espinos y abrojos, sino que se enredaban en "
             "los espinos y abrojos.",
    (62, 7): "Estas, pues, enredadas, pacían entre los espinos y abrojos, y "
             "padecían mucho, azotadas por él; y las arreaba de aquí para "
             "allá, y no les daba descanso, y aquellas ovejas no tenían "
             "sosiego alguno.",

    # Capítulo 63
    (63, 1): "Viéndolas, pues, tan azotadas y maltratadas, me entristecía por "
             "ellas, porque así eran atormentadas y no tenían tregua alguna.",
    (63, 2): "Digo al pastor que hablaba conmigo: Señor, ¿quién es este "
             "pastor tan despiadado y amargo, y que no tiene compasión alguna "
             "de estas ovejas? Este, dijo, es el ángel del castigo; es de los "
             "ángeles justos, pero está puesto sobre el castigo.",
    (63, 3): "Recibe, pues, a los que se extravían de Dios y andan en los "
             "deseos y engaños de este siglo, y los castiga, según son "
             "dignos, con terribles y diversos castigos.",
    (63, 4): "Quisiera, dije, señor, conocer estos diversos castigos, de qué "
             "clase son. Oye, dijo, los diversos tormentos y castigos. Los "
             "tormentos son de esta vida; porque unos son castigados con "
             "pérdidas, otros con privaciones, otros con enfermedades "
             "diversas, otros con toda clase de desasosiego, otros siendo "
             "afrentados por gente indigna y padeciendo en otros muchos "
             "asuntos.",
    (63, 5): "Porque muchos, siendo inconstantes en sus consejos, emprenden "
             "muchas cosas, y nada en absoluto les sale adelante. Y dicen de "
             "sí mismos que no prosperan en sus negocios, y no sube a su "
             "corazón que hicieron malas obras, sino que culpan al Señor.",
    (63, 6): "Cuando, pues, son afligidos con toda aflicción, entonces me son "
             "entregados a mí para buena corrección, y son fortalecidos en la "
             "fe del Señor, y los días que quedan de su vida sirven al Señor "
             "con corazón puro. Y si se arrepienten, entonces suben a su "
             "corazón las obras malas que hicieron, y entonces glorifican a "
             "Dios, diciendo que es juez justo y que con justicia padecieron "
             "cada uno conforme a sus obras; y en adelante sirven al Señor "
             "con su corazón puro, y prosperan en todo negocio suyo, "
             "recibiendo del Señor todo cuanto piden; y entonces glorifican "
             "al Señor porque me fueron entregados a mí, y ya no padecen nada "
             "de los males.",

    # Capítulo 64
    (64, 1): "Le digo: Señor, declárame todavía esto. ¿Qué, dijo, buscas? Si "
             "acaso, dije, señor, los que viven en regalos y engaños son "
             "atormentados el mismo tiempo que se regalan y son engañados. Me "
             "dice: El mismo tiempo son atormentados.",
    (64, 2): "Muy poco, dije, señor, son atormentados; porque convenía que "
             "los que así se regalan y se olvidan de Dios fuesen atormentados "
             "siete veces más.",
    (64, 3): "Me dice: Insensato eres, y no entiendes la fuerza del tormento. "
             "Porque si la entendiera, dije, señor, no preguntaría para que "
             "me la declarases. Oye, dijo, la fuerza de ambos.",
    (64, 4): "El tiempo del regalo y del engaño es una hora; pero la hora del "
             "tormento tiene la fuerza de treinta días. Si, pues, uno se "
             "regala y es engañado un día, y es atormentado un día, el día "
             "del tormento vale un año entero. Cuantos días, pues, se regale "
             "uno, tantos años es atormentado. Ves, pues, dijo, que el tiempo "
             "del regalo y del engaño es brevísimo, y el del castigo y del "
             "tormento, largo.",

    # Capítulo 65
    (65, 1): "Todavía, dije, señor, no he entendido del todo lo del tiempo "
             "del engaño, y del regalo, y del tormento; decláramelo más "
             "claramente.",
    (65, 2): "Respondiendo, me dice: Tu insensatez es persistente, y no "
             "quieres purificar tu corazón y servir a Dios. Mira, dijo, no "
             "sea que se cumpla el tiempo y tú seas hallado insensato. Oye, "
             "pues, dijo, como quieres, para que lo entiendas.",
    (65, 3): "El que se regala y es engañado un día, y hace lo que quiere, "
             "está vestido de mucha insensatez y no entiende lo que hace; "
             "porque al día siguiente se olvida de lo que hizo el día antes; "
             "porque el regalo y el engaño no tienen memoria, a causa de la "
             "insensatez de que está vestido; mas el castigo y el tormento, "
             "cuando se pegan al hombre un día, es castigado y atormentado "
             "hasta un año; porque el castigo y el tormento tienen gran "
             "memoria.",
    (65, 4): "Siendo, pues, atormentado y castigado todo el año, se acuerda "
             "entonces del regalo y del engaño, y conoce que por ellos padece "
             "los males. Todo hombre, pues, que se regala y es engañado, es "
             "así atormentado, porque, teniendo vida, se entregaron a sí "
             "mismos a la muerte.",
    (65, 5): "¿Qué regalos, dije, señor, son dañosos? Toda acción, dijo, que "
             "el hombre hace con gusto es regalo para él; porque también el "
             "iracundo, dando satisfacción a su pasión, se regala; y el "
             "adúltero, y el borracho, y el calumniador, y el mentiroso, y el "
             "avaro, y el defraudador, y el que hace cosas semejantes a "
             "estas, da satisfacción a su propia enfermedad; se regala, pues, "
             "en su acción.",
    (65, 6): "Todos estos regalos son dañosos para los siervos de Dios. Por "
             "estos engaños, pues, padecen los que son castigados y "
             "atormentados.",
    (65, 7): "Pero hay también regalos que salvan a los hombres; porque "
             "muchos, obrando el bien, se regalan, llevados por su propio "
             "gusto. Este regalo, pues, es provechoso para los siervos de "
             "Dios, y gana vida para el tal hombre; mas los regalos dañosos "
             "antes dichos les ganan tormentos y castigos; y si perseveran y "
             "no se arrepienten, se ganan la muerte.",

    # Capítulo 66
    (66, 1): "Pocos días después lo vi en la misma llanura donde también "
             "había visto a los pastores, y me dice: ¿Qué buscas? Estoy aquí, "
             "señor, dije, para que mandes al pastor castigador que salga de "
             "mi casa, porque me aflige mucho. Es menester, dijo, que seas "
             "afligido; porque así, dijo, lo ordenó acerca de ti el ángel "
             "glorioso; pues quiere que seas probado. ¿Pues qué, dije, señor, "
             "he hecho tan malo para ser entregado a este ángel?",
    (66, 2): "Oye, dijo: tus pecados son muchos, pero no tantos como para que "
             "seas entregado a este ángel; mas tu casa ha cometido grandes "
             "iniquidades y pecados, y el ángel glorioso se ha amargado por "
             "sus obras, y por eso mandó que fueses afligido por algún "
             "tiempo, para que también ellos se arrepientan y se purifiquen "
             "de todo deseo de este siglo. Cuando, pues, se arrepientan y "
             "sean purificados, entonces se apartará de ti el ángel del "
             "castigo.",
    (66, 3): "Le digo: Señor, si ellos hicieron tales cosas que el ángel "
             "glorioso se amargó, ¿qué he hecho yo? De otro modo, dijo, no "
             "pueden ellos ser afligidos, si no eres afligido tú, la cabeza "
             "de la casa; porque siendo tú afligido, por necesidad también "
             "ellos serán afligidos; pero estando tú en prosperidad, no "
             "pueden tener aflicción alguna.",
    (66, 4): "Pero he aquí, dije, señor, que se han arrepentido de todo su "
             "corazón. Sé también yo, dijo, que se han arrepentido de todo su "
             "corazón; ¿piensas, pues, que a los que se arrepienten se les "
             "perdonan en seguida los pecados? No del todo; sino que es "
             "menester que el que se arrepiente atormente su propia alma, y "
             "se humille fuertemente en toda acción suya, y sea afligido con "
             "toda clase de aflicciones; y si soporta las aflicciones que le "
             "sobrevienen, ciertamente tendrá compasión el que creó todas las "
             "cosas y les dio poder, y le dará alguna sanidad;",
    (66, 5): "y esto ciertamente, si ve el corazón del que se arrepiente puro "
             "de toda mala acción. Y a ti y a tu casa os conviene ahora ser "
             "afligidos. ¿Pero para qué te digo muchas cosas? Es menester que "
             "seas afligido, como lo ordenó aquel ángel del Señor que te "
             "entregó a mí; y da gracias al Señor por esto, porque te tuvo "
             "por digno de declararte de antemano la aflicción, para que, "
             "conociéndola de antemano, la soportes con fortaleza.",
    (66, 6): "Le digo: Señor, está tú conmigo, y podré soportar toda "
             "aflicción. Yo, dijo, estaré contigo; y rogaré también al ángel "
             "castigador que te aflija más levemente; pero por poco tiempo "
             "serás afligido, y otra vez serás restablecido en tu casa. "
             "Solamente persevera humillándote y sirviendo al Señor con todo "
             "corazón puro, tú y tus hijos y tu casa, y anda en mis "
             "mandamientos que te mando, y tu penitencia podrá ser fuerte y "
             "pura;",
    (66, 7): "y si los guardas con tu casa, se apartará de ti toda aflicción; "
             "y también, dijo, se apartará la aflicción de todos cuantos "
             "anden en estos mis mandamientos.",

    # Capítulo 67
    (67, 1): "Me mostró un sauce grande, que cubría llanuras y montes, y bajo "
             "la sombra del sauce habían venido todos los que han sido "
             "llamados en el nombre del Señor.",
    (67, 2): "Y estaba junto al sauce un ángel del Señor glorioso, muy alto, "
             "que tenía una gran hoz, y cortaba ramas del sauce y las "
             "repartía al pueblo cubierto por el sauce; y les repartía varas "
             "pequeñas, como de un codo.",
    (67, 3): "Después que todos recibieron las varas, el ángel dejó la hoz, y "
             "aquel árbol estaba sano, tal como yo lo había visto.",
    (67, 4): "Y yo me maravillaba en mí mismo, diciendo: ¿Cómo, habiéndose "
             "cortado tantas ramas, el árbol está sano? Me dice el pastor: No "
             "te maravilles de que este árbol haya quedado sano, habiéndose "
             "cortado tantas ramas; pero cuando lo hayas visto todo, dijo, se "
             "te declarará qué es.",
    (67, 5): "El ángel que había repartido al pueblo las varas se las volvió "
             "a pedir; y según las habían recibido, así también eran llamados "
             "ante él, y cada uno de ellos devolvía las varas. Y el ángel del "
             "Señor las recibía y las examinaba.",
    (67, 6): "De algunos recibía las varas secas y como comidas de polilla; "
             "el ángel mandó que los que habían entregado tales varas se "
             "pusieran aparte.",
    (67, 7): "Y otros las entregaban secas, pero no estaban comidas de "
             "polilla; y también a estos mandó que se pusieran aparte.",
    (67, 8): "Y otros las entregaban medio secas; y también estos se ponían "
             "aparte.",
    (67, 9): "Y otros entregaban sus varas medio secas y con grietas; y "
             "también estos se ponían aparte.",
    (67, 10): "Y otros entregaban sus varas verdes y con grietas; y también "
              "estos se ponían aparte.",
    (67, 11): "Y otros entregaban sus varas la mitad seca y la otra mitad "
              "verde; y también estos se ponían aparte.",
    (67, 12): "Y otros presentaban sus varas con las dos partes de la vara "
              "verdes y la tercera seca; y también estos se ponían aparte.",
    (67, 13): "Y otros las entregaban con las dos partes secas y la tercera "
              "verde; y también estos se ponían aparte.",
    (67, 14): "Y otros entregaban sus varas casi enteramente verdes, y era "
              "seca una parte mínima de sus varas, la misma punta; pero "
              "tenían grietas en ellas; y también estos se ponían aparte.",
    (67, 15): "Y de otros era verde una parte mínima, y lo demás de las "
              "varas, seco; y también estos se ponían aparte.",
    (67, 16): "Y otros venían trayendo las varas verdes, como las habían "
              "recibido del ángel; y la mayor parte de la multitud entregaba "
              "tales varas. Y el ángel se gozó mucho por estos; y también "
              "estos se ponían aparte.",
    (67, 17): "Y otros entregaban sus varas verdes y con retoños; y también "
              "estos se ponían aparte; y el ángel se gozó mucho por estos.",
    (67, 18): "Y otros entregaban sus varas verdes y con retoños; y sus "
              "retoños tenían como algún fruto; y aquellos hombres cuyas "
              "varas fueron halladas tales estaban muy alegres. Y el ángel se "
              "regocijaba por estos, y el pastor estaba muy alegre por ellos.",

    # Capítulo 68
    (68, 1): "Y el ángel del Señor mandó que se trajesen coronas. Y fueron "
             "traídas coronas hechas como de palmas, y coronó a los hombres "
             "que habían entregado las varas que tenían los renuevos y algún "
             "fruto, y los despidió a la torre.",
    (68, 2): "Y a los otros también los envió a la torre, a los que habían "
             "entregado las varas verdes y con renuevos, pero cuyos renuevos "
             "no tenían fruto, dándoles sellos.",
    (68, 3): "Y todos los que iban a la torre tenían la misma vestidura, "
             "blanca como la nieve.",
    (68, 4): "Y a los que habían entregado las varas verdes tal como las "
             "recibieron, los despidió, dándoles vestidura y sellos.",
    (68, 5): "Después que el ángel hubo acabado estas cosas, dice al pastor: "
             "Yo me voy; y tú despedirás a éstos a los muros, según cada uno "
             "sea digno de morar. Mas examina sus varas con cuidado, y así "
             "despídelos; con cuidado examínalas. Mira que ninguno se te "
             "pase, dice; y si alguno se te pasa, yo los probaré en el altar. "
             "Dicho esto al pastor, se fue.",
    (68, 6): "Y después que el ángel se hubo ido, me dice el pastor: Tomemos "
             "las varas de todos y plantémoslas, por si algunas de ellas "
             "pueden vivir. Le digo: Señor, estas secas, ¿cómo pueden vivir?",
    (68, 7): "Respondiendo, me dice: Este árbol es un sauce, y su especie es "
             "amiga de la vida; si, pues, se plantan las varas y reciben un "
             "poco de humedad, vivirán muchas de ellas; y luego probemos "
             "también a echarles agua. Si alguna de ellas puede vivir, me "
             "alegraré con ellas; y si no vive, no seré yo hallado "
             "negligente.",
    (68, 8): "Y me mandó el pastor que los llamase, según cada uno de ellos "
             "había sido colocado. Vinieron por órdenes, orden tras orden, y "
             "entregaban las varas al pastor; y el pastor tomaba las varas y "
             "las plantó por órdenes, y después de plantarlas les echó mucha "
             "agua, de modo que por el agua no se veían las varas.",
    (68, 9): "Y después de haber regado las varas, me dice: Vámonos, y dentro "
             "de pocos días volvamos y visitemos todas las varas; porque el "
             "que creó este árbol quiere que vivan todos los que recibieron "
             "ramas de este árbol. Y espero yo también que estas varillas, "
             "habiendo recibido humedad y siendo regadas con agua, vivirán en "
             "su mayor parte.",

    # Capítulo 69
    (69, 1): "Le digo: Señor, hazme saber qué es este árbol; porque estoy "
             "perplejo acerca de él, de que, habiéndose cortado tantas ramas, "
             "el árbol está sano y no parece que se le haya cortado nada; en "
             "esto, pues, estoy perplejo.",
    (69, 2): "Escucha, dice: este árbol grande que cubre llanuras y montes y "
             "toda la tierra es la ley de Dios, que fue dada a todo el mundo; "
             "y esta ley es el Hijo de Dios, predicado hasta los confines de "
             "la tierra; y los pueblos que están bajo su sombra son los que "
             "oyeron la predicación y creyeron en él.",
    (69, 3): "Y el ángel grande y glorioso es Miguel, el que tiene la "
             "potestad sobre este pueblo y lo gobierna; porque éste es el que "
             "les da la ley en los corazones de los que creen; los visita, "
             "pues, a aquellos a quienes la dio, para ver si acaso la han "
             "guardado.",
    (69, 4): "Y ves las varas de cada uno; porque las varas son la ley. Ves, "
             "pues, muchas varas inutilizadas, y conocerás que son todos los "
             "que no guardaron la ley; y verás la morada de cada uno.",
    (69, 5): "Le digo: Señor, ¿por qué a unos los despidió a la torre, y a "
             "otros te los dejó a ti? Cuantos, dice, transgredieron la ley "
             "que recibieron de él, los dejó bajo mi potestad para "
             "penitencia; y cuantos ya agradaron a la ley y la han guardado, "
             "los tiene bajo su propia potestad.",
    (69, 6): "¿Quiénes son, pues, digo, señor, los coronados y que van a la "
             "torre? Cuantos, dice, lucharon contra el diablo y lo vencieron, "
             "están coronados; éstos son los que padecieron por la ley.",
    (69, 7): "Y los otros, que también entregaron las varas verdes y con "
             "renuevos, pero sin fruto, son los que fueron atribulados por la "
             "ley, pero no padecieron ni negaron su ley.",
    (69, 8): "Y los que las entregaron verdes, tal como las recibieron, son "
             "los venerables y justos, y que anduvieron sobremanera con "
             "corazón puro y guardaron los mandamientos del Señor. Y lo demás "
             "lo sabrás cuando yo examine estas varas que han sido plantadas "
             "y regadas.",

    # Capítulo 70
    (70, 1): "Y después de pocos días vinimos al lugar, y el pastor se sentó "
             "en el lugar del ángel, y yo me puse junto a él. Y me dice: "
             "Cíñete un delantal de lino crudo y sírveme. Me ceñí un delantal "
             "limpio hecho de tela de saco.",
    (70, 2): "Y viéndome ceñido y pronto para servirle, dice: Llama a los "
             "hombres cuyas varas están plantadas, según el orden en que cada "
             "uno entregó las varas. Y fui al llano y los llamé a todos; y se "
             "pusieron todos por órdenes, orden tras orden.",
    (70, 3): "Les dice: Cada uno arranque sus propias varas y tráigalas a mí.",
    (70, 4): "Primero las entregaron los que las habían tenido secas y "
             "roídas; y como éstas fueron halladas secas y roídas, mandó que "
             "se pusieran aparte.",
    (70, 5): "Luego las entregaron los que las tenían secas pero no roídas; y "
             "algunos de ellos entregaron las varas verdes, y otros secas y "
             "roídas como por la polilla. A los que las entregaron verdes, "
             "pues, mandó que se pusieran aparte, y a los que las entregaron "
             "secas y roídas mandó que se pusieran con los primeros.",
    (70, 6): "Luego las entregaron los que las tenían medio secas y con "
             "grietas; y muchos de ellos las entregaron verdes y sin grietas; "
             "y algunos verdes y con renuevos, y en los renuevos frutos, como "
             "los que tenían los que fueron coronados a la torre. Y algunos "
             "las entregaron secas y comidas, y otros secas y no comidas, y "
             "otros tales cuales eran, medio secas y con grietas. Mandó que "
             "cada uno de ellos se pusiera aparte, unos con sus propios "
             "órdenes, y otros aparte.",

    # Capítulo 71
    (71, 1): "Luego las entregaban los que tenían las varas verdes, pero con "
             "grietas; éstos todos las entregaron verdes y se pusieron en su "
             "propio orden. Y el pastor se alegró por éstos, porque todos "
             "habían sido cambiados y se habían despojado de sus grietas.",
    (71, 2): "Y las entregaron también los que las tenían la mitad verde y la "
             "mitad seca; de algunos, pues, fueron halladas las varas "
             "enteramente verdes, de otros medio secas, de otros secas y "
             "comidas, y de otros verdes y con renuevos; éstos todos fueron "
             "despedidos, cada uno a su orden.",
    (71, 3): "Luego las entregaron los que tenían dos partes verdes y la "
             "tercera seca. Muchos de ellos las entregaron verdes, y muchos "
             "medio secas, y otros secas y comidas; éstos todos se pusieron "
             "en su propio orden.",
    (71, 4): "Luego las entregaron los que tenían dos partes secas y la "
             "tercera verde; muchos de ellos las entregaron medio secas, y "
             "algunos secas y comidas, y otros medio secas y con grietas, y "
             "pocos verdes; éstos todos se pusieron en su propio orden.",
    (71, 5): "Y las entregaron los que habían tenido sus varas verdes, pero "
             "con un poquito seco y con grietas; de éstos algunos las "
             "entregaron verdes, y otros verdes y con renuevos; se fueron "
             "también éstos a su orden.",
    (71, 6): "Luego las entregaron los que tenían un poquito verde y las "
             "demás partes secas; las varas de éstos fueron halladas en su "
             "mayor parte verdes y con renuevos, y fruto en los renuevos, y "
             "otras enteramente verdes. Por estas varas se alegró el pastor "
             "sobremanera, porque así fueron halladas. Y éstos se fueron cada "
             "uno a su propio orden.",

    # Capítulo 72
    (72, 1): "Después que el pastor hubo examinado las varas de todos, me "
             "dice: Te dije que este árbol es amigo de la vida. ¿Ves, dice, "
             "cuántos se arrepintieron y fueron salvos? Lo veo, digo, señor. "
             "Para que veas, dice, la gran misericordia del Señor, que es "
             "grande y gloriosa, y que dio espíritu a los que eran dignos de "
             "penitencia.",
    (72, 2): "¿Por qué, pues, digo, señor, no se arrepintieron todos? A "
             "aquellos cuyo corazón vio que había de hacerse puro y servirle "
             "de todo corazón, a éstos dio la penitencia; mas a aquellos en "
             "quienes vio el engaño y la maldad, que habían de arrepentirse "
             "con hipocresía, a ésos no les dio penitencia, no sea que otra "
             "vez profanen su nombre.",
    (72, 3): "Le digo: Señor, declárame, pues, ahora a los que entregaron las "
             "varas, qué clase de hombre es cada uno de ellos, y la morada de "
             "éstos, para que, oyéndolo los que creyeron y recibieron el "
             "sello y lo quebrantaron y no lo guardaron sano, reconociendo "
             "sus propias obras se arrepientan, recibiendo de ti un sello, y "
             "glorifiquen al Señor, porque tuvo compasión de ellos y te envió "
             "a renovar sus espíritus.",
    (72, 4): "Escucha, dice: aquellos cuyas varas fueron halladas secas y "
             "comidas por la polilla, éstos son los apóstatas y traidores de "
             "la iglesia, y los que blasfemaron al Señor en sus pecados, y "
             "además se avergonzaron del nombre del Señor que fue invocado "
             "sobre ellos. Éstos, pues, perecieron del todo para Dios. Y ves "
             "que ni uno solo de ellos se arrepintió, aunque oyeron las "
             "palabras que les hablaste, las que yo te mandé; de los tales la "
             "vida se apartó.",
    (72, 5): "Y los que entregaron las secas y no podridas, también éstos "
             "están cerca de ellos; porque eran hipócritas, e introducían "
             "doctrinas extrañas y pervertían a los siervos de Dios, sobre "
             "todo a los que habían pecado, no dejándolos arrepentirse, sino "
             "persuadiéndolos con sus doctrinas necias. Éstos, pues, tienen "
             "esperanza de arrepentirse.",
    (72, 6): "Y ves que muchos de ellos también se han arrepentido desde que "
             "les hablé mis mandamientos; y aún se arrepentirán. Y cuantos no "
             "se arrepientan, perdieron su vida. Mas cuantos de ellos se "
             "arrepintieron, se hicieron buenos, y su morada fue en los "
             "primeros muros; y algunos también subieron a la torre. Ves, "
             "pues, dice, que la penitencia de los pecados tiene vida, y el "
             "no arrepentirse, muerte.",

    # Capítulo 73
    (73, 1): "Y cuantos las entregaron medio secas y tenían grietas en ellas, "
             "escucha también acerca de ellos. Aquellos cuyas varas estaban "
             "medio secas son los de doble ánimo; porque ni viven ni están "
             "muertos.",
    (73, 2): "Y los que las tenían medio secas y con grietas en ellas, éstos "
             "son de doble ánimo y murmuradores, y nunca tienen paz entre sí, "
             "sino que siempre andan en disensiones. Pero también a éstos, "
             "dice, les está puesta delante la penitencia. Ves, dice, que "
             "algunos de ellos se han arrepentido. Y aún, dice, hay en ellos "
             "esperanza de penitencia.",
    (73, 3): "Y cuantos de ellos, dice, se han arrepentido, tendrán su morada "
             "en la torre; y cuantos de ellos se han arrepentido más tarde, "
             "morarán en los muros; y cuantos no se arrepienten, sino que "
             "permanecen en sus obras, morirán de muerte.",
    (73, 4): "Y los que entregaron sus varas verdes y con grietas, éstos "
             "fueron siempre fieles y buenos, pero tenían entre sí cierta "
             "envidia acerca de los primeros puestos y acerca de alguna "
             "gloria; mas todos éstos son necios, teniendo entre sí envidia "
             "acerca de los primeros puestos.",
    (73, 5): "Pero también éstos, oyendo mis mandamientos, siendo buenos, se "
             "purificaron a sí mismos y se arrepintieron pronto. Su morada, "
             "pues, fue en la torre; pero si alguno vuelve otra vez a la "
             "disensión, será echado fuera de la torre y perderá su vida.",
    (73, 6): "La vida es de todos los que guardan los mandamientos del Señor; "
             "y en los mandamientos no se trata de primeros puestos ni de "
             "gloria alguna, sino de longanimidad y de humildad del hombre. "
             "En los tales, pues, está la vida del Señor, mas en los "
             "sediciosos e inicuos, la muerte.",

    # Capítulo 74
    (74, 1): "Y los que entregaron las varas mitad verdes y mitad secas, "
             "éstos son los que están enredados en los negocios y no se "
             "juntan a los santos; por esto la mitad de ellos vive, y la "
             "mitad está muerta.",
    (74, 2): "Muchos, pues, habiendo oído mis mandamientos, se arrepintieron. "
             "Cuantos, pues, se arrepintieron, su morada es en la torre. Pero "
             "algunos de ellos se apartaron del todo. Éstos, pues, no tienen "
             "penitencia; porque a causa de sus negocios blasfemaron al Señor "
             "y lo negaron. Perdieron, pues, su vida por la maldad que "
             "hicieron.",
    (74, 3): "Y muchos de ellos dudaron con doble ánimo. Éstos todavía tienen "
             "penitencia, si se arrepienten pronto, y su morada será en la "
             "torre; pero si se arrepienten más tarde, morarán en los muros; "
             "y si no se arrepienten, también ellos perdieron su vida.",
    (74, 4): "Y los que entregaron las varas con dos partes verdes y la "
             "tercera seca, éstos son los que negaron con diversas "
             "negaciones.",
    (74, 5): "Muchos, pues, de ellos se arrepintieron y se fueron a morar a "
             "la torre; pero muchos se apartaron del todo de Dios; éstos "
             "perdieron del todo el vivir. Y algunos de ellos dudaron con "
             "doble ánimo y anduvieron en disensiones. Para éstos, pues, hay "
             "penitencia, si se arrepienten pronto y no permanecen en sus "
             "placeres; pero si permanecen en sus obras, también éstos se "
             "acarrean la muerte a sí mismos.",

    # Capítulo 75
    (75, 1): "Y los que entregaron las varas con dos partes secas y la "
             "tercera verde, éstos son los que fueron fieles, pero "
             "enriquecieron y se hicieron ilustres entre los gentiles; se "
             "vistieron de gran soberbia y se hicieron altivos, y abandonaron "
             "la verdad y no se juntaron a los justos, sino que vivieron con "
             "los gentiles, y este camino les fue más agradable; pero no se "
             "apartaron de Dios, sino que permanecieron en la fe, aunque no "
             "obraban las obras de la fe.",
    (75, 2): "Muchos, pues, de ellos se arrepintieron, y su morada fue en la "
             "torre.",
    (75, 3): "Y otros, viviendo hasta el fin con los gentiles y "
             "corrompiéndose con las vanaglorias de los gentiles, se "
             "apartaron de Dios e hicieron las obras de los gentiles. Éstos "
             "fueron contados con los gentiles.",
    (75, 4): "Y otros de ellos dudaron con doble ánimo, no esperando ser "
             "salvos por las obras que habían hecho; y otros dudaron con "
             "doble ánimo e hicieron divisiones entre sí. Para éstos, pues, "
             "que dudaron con doble ánimo a causa de sus obras, todavía hay "
             "penitencia; pero su penitencia debe ser pronta, para que su "
             "morada sea en la torre; mas para los que no se arrepienten, "
             "sino que permanecen en sus placeres, la muerte está cerca.",

    # Capítulo 76
    (76, 1): "Y los que entregaron las varas verdes, pero con las puntas "
             "mismas secas y con grietas, éstos fueron siempre buenos y "
             "fieles y gloriosos delante de Dios, pero pecaron un poquito a "
             "causa de pequeñas concupiscencias y por tener pequeñas cosas "
             "unos contra otros; mas oyendo mis palabras, la mayor parte se "
             "arrepintió pronto, y su morada fue en la torre.",
    (76, 2): "Y algunos de ellos dudaron con doble ánimo, y algunos, habiendo "
             "dudado, hicieron mayor disensión. En éstos, pues, hay esperanza "
             "de penitencia, porque siempre fueron buenos; y difícilmente "
             "morirá alguno de ellos.",
    (76, 3): "Y los que entregaron sus varas secas, pero con un poquito "
             "verde, éstos son los que solamente creyeron, pero obraron las "
             "obras de la iniquidad; mas nunca se apartaron de Dios, y "
             "llevaron el nombre con gusto, y con gusto recibieron en sus "
             "casas a los siervos de Dios. Oyendo, pues, esta penitencia, se "
             "arrepintieron sin vacilar, y obran toda virtud y justicia.",
    (76, 4): "Y algunos de ellos aun tienen temor, conociendo las obras que "
             "hicieron. De todos éstos, pues, la morada será en la torre.",

    # Capítulo 77
    (77, 1): "Y después que hubo acabado las explicaciones de todas las "
             "varas, me dice: Ve y di a todos que se arrepientan, y vivirán "
             "para Dios; porque el Señor, movido a compasión, me envió a dar "
             "a todos la penitencia, aunque algunos no son dignos a causa de "
             "sus obras; mas siendo longánimo el Señor, quiere que el "
             "llamamiento hecho por medio de su Hijo sea salvo.",
    (77, 2): "Le digo: Señor, espero que todos, habiéndolo oído, se "
             "arrepentirán; porque estoy persuadido de que cada uno, "
             "reconociendo sus propias obras y temiendo a Dios, se "
             "arrepentirá.",
    (77, 3): "Respondiendo, me dice: Cuantos, dice, se arrepientan de todo su "
             "corazón y se purifiquen de sus maldades antes dichas, y ya no "
             "añadan nada más a sus pecados, recibirán del Señor sanidad de "
             "sus pecados anteriores, si no dudan con doble ánimo acerca de "
             "estos mandamientos, y vivirán para Dios. Mas cuantos, dice, "
             "añadan a sus pecados y anden en las concupiscencias de este "
             "siglo, se condenarán a sí mismos a muerte.",
    (77, 4): "Pero tú anda en mis mandamientos, y vivirás para Dios; y "
             "cuantos anduvieren en ellos y obraren rectamente, vivirán para "
             "Dios.",
    (77, 5): "Habiéndome mostrado estas cosas y hablado todas, me dice: Y lo "
             "demás te lo mostraré dentro de pocos días.",

    # Capítulo 78
    (78, 1): "Después que hube escrito los mandamientos y las semejanzas del "
             "pastor, el ángel de la penitencia, vino a mí y me dice: Quiero "
             "mostrarte cuanto te mostró el Espíritu Santo que habló contigo "
             "en forma de la Iglesia; porque aquel Espíritu es el Hijo de "
             "Dios.",
    (78, 2): "Porque, como eras más débil en la carne, no te fue declarado "
             "por medio de un ángel. Mas cuando fuiste fortalecido por el "
             "Espíritu y te hiciste fuerte en tu fuerza, de modo que pudieses "
             "ver aun a un ángel, entonces te fue manifestada por medio de la "
             "Iglesia la edificación de la torre; bien y dignamente lo has "
             "visto todo como de parte de una virgen. Y ahora lo ves de parte "
             "de un ángel, aunque por el mismo Espíritu.",
    (78, 3): "Pero es menester que lo aprendas todo de mí con más exactitud. "
             "Porque para esto también fui dado por el ángel glorioso para "
             "morar en tu casa, para que lo veas todo con firmeza, sin "
             "acobardarte en nada, como antes.",
    (78, 4): "Y me llevó a Arcadia, a un monte de forma redondeada como un "
             "pecho, y me sentó sobre la cumbre del monte, y me mostró una "
             "llanura grande, y alrededor de la llanura doce montes, teniendo "
             "los montes cada uno diferente aspecto.",
    (78, 5): "El primero era negro como el hollín; y el segundo pelado, sin "
             "hierbas; y el tercero lleno de espinos y abrojos;",
    (78, 6): "y el cuarto tenía hierbas medio secas, verdes en lo alto de las "
             "hierbas, y secas junto a las raíces; y algunas hierbas, cuando "
             "el sol las quemaba, se secaban;",
    (78, 7): "y el quinto monte tenía hierbas verdes y era escabroso. Y el "
             "sexto monte estaba todo lleno de grietas, unas pequeñas y otras "
             "grandes; y las grietas tenían hierbas, mas las hierbas no eran "
             "muy lozanas, sino más bien como marchitas.",
    (78, 8): "Y el séptimo monte tenía hierbas alegres, y todo el monte era "
             "próspero, y toda especie de ganados y de aves pacían en aquel "
             "monte; y cuanto más pacían los ganados y las aves, tanto más y "
             "más florecían las hierbas de aquel monte. Y el octavo monte "
             "estaba lleno de fuentes, y toda especie de la creación del "
             "Señor bebía de las fuentes de aquel monte.",
    (78, 9): "Y el noveno monte no tenía agua alguna y era todo desierto. Y "
             "tenía en él fieras y reptiles mortíferos que destruían a los "
             "hombres. Y el décimo monte tenía árboles grandísimos y era todo "
             "sombrío, y bajo la sombra de los árboles estaban echadas "
             "ovejas, descansando y rumiando.",
    (78, 10): "Y el undécimo monte estaba muy poblado de árboles, y aquellos "
              "árboles estaban cargados de fruto, adornados cada uno con "
              "diversos frutos, para que quien los viese desease comer de sus "
              "frutos. Y el duodécimo monte era todo blanco, y su aspecto era "
              "alegre; y el monte era en sí mismo hermosísimo.",

    # Capítulo 79
    (79, 1): "Y en medio de la llanura me mostró una roca grande y blanca que "
             "se levantaba de la llanura. Y la roca era más alta que los "
             "montes, cuadrada, de modo que podía contener al mundo entero.",
    (79, 2): "Y aquella roca era antigua, y tenía una puerta labrada en ella; "
             "y la labra de la puerta me parecía reciente. Y la puerta "
             "resplandecía más que el sol, de tal manera que yo me "
             "maravillaba del brillo de la puerta.",
    (79, 3): "Y alrededor de la puerta estaban de pie doce vírgenes. Las "
             "cuatro, pues, que estaban en las esquinas me parecían más "
             "gloriosas; pero también las otras eran gloriosas. Y estaban de "
             "pie en los cuatro lados de la puerta, y entre ellas, de dos en "
             "dos, vírgenes.",
    (79, 4): "Y estaban vestidas de túnicas de lino y ceñidas con gracia, "
             "teniendo fuera los hombros derechos, como quienes han de llevar "
             "alguna carga. Así estaban preparadas; porque estaban muy "
             "alegres y dispuestas.",
    (79, 5): "Después que vi estas cosas, me maravillaba dentro de mí, porque "
             "veía cosas grandes y gloriosas. Y otra vez estaba perplejo "
             "acerca de las vírgenes, de que, siendo tan delicadas, "
             "estuvieran de pie varonilmente, como quienes han de llevar el "
             "cielo entero.",
    (79, 6): "Y me dice el pastor: ¿Por qué razonas dentro de ti y estás "
             "perplejo y te acarreas tristeza? Porque lo que no puedes "
             "entender, no lo intentes, si eres prudente; sino pide al Señor, "
             "para que, recibiendo entendimiento, lo entiendas.",
    (79, 7): "Lo que está detrás de ti no lo puedes ver, pero lo que está "
             "delante de ti lo ves. Lo que, pues, no puedes ver, déjalo, y no "
             "te atormentes; mas lo que ves, enseñoréate de ello, y acerca de "
             "lo demás no seas curioso; y yo te declararé todo cuanto te "
             "muestre. Mira, pues, lo que resta.",

    # Capítulo 80
    (80, 1): "Vi que habían venido seis hombres altos y gloriosos y "
             "semejantes en el aspecto; y llamaron a una multitud de hombres. "
             "Y también aquellos que habían venido eran hombres altos y "
             "hermosos y fuertes; y los seis hombres les mandaron que "
             "edificasen sobre la roca una torre. Y había gran alboroto de "
             "aquellos hombres que habían venido a edificar la torre, que "
             "corrían de acá para allá alrededor de la puerta.",
    (80, 2): "Y las vírgenes que estaban alrededor de la puerta decían a los "
             "hombres que se apresurasen a edificar la torre; y las vírgenes "
             "habían extendido las manos, como quienes han de recibir algo de "
             "los hombres.",
    (80, 3): "Y los seis hombres mandaban que subiesen piedras de cierto "
             "abismo y fuesen a la edificación de la torre. Y subieron diez "
             "piedras cuadradas, resplandecientes, no labradas.",
    (80, 4): "Y los seis hombres llamaban a las vírgenes y les mandaron que "
             "llevasen todas las piedras que habían de ir a la edificación de "
             "la torre, y que pasasen por la puerta y las entregasen a los "
             "hombres que habían de edificar la torre.",
    (80, 5): "Y las vírgenes se ponían unas a otras las diez primeras piedras "
             "que habían subido del abismo, y llevaban juntas cada piedra, "
             "una por una.",

    # Capítulo 81
    (81, 1): "Y así como se habían puesto juntas alrededor de la puerta, así "
             "las llevaban: las que parecían ser fuertes se habían metido "
             "debajo de las esquinas de la piedra, y las otras se habían "
             "metido debajo de los costados de la piedra; y así llevaban "
             "todas las piedras. Y las pasaban por la puerta, como se les "
             "había mandado, y las entregaban a los hombres para la torre; y "
             "ellos, tomando las piedras, edificaban.",
    (81, 2): "Y la edificación de la torre se hacía sobre la roca grande y "
             "encima de la puerta. Fueron, pues, ajustadas aquellas diez "
             "piedras y llenaron toda la roca; y ellas vinieron a ser el "
             "cimiento de la edificación de la torre; y la roca y la puerta "
             "sostenían toda la torre.",
    (81, 3): "Y después de las diez piedras subieron del abismo otras veinte "
             "piedras; y también éstas fueron ajustadas en la edificación de "
             "la torre, llevadas por las vírgenes como las primeras. Y "
             "después de éstas subieron treinta y cinco, y también éstas "
             "fueron ajustadas igualmente en la torre. Y después de éstas "
             "subieron otras cuarenta piedras, y todas éstas fueron puestas "
             "en la edificación de la torre; hubo, pues, cuatro hileras en "
             "los cimientos de la torre.",
    (81, 4): "Y cesaron de subir del abismo; y cesaron también un poco los "
             "que edificaban. Y otra vez los seis hombres ordenaron a la "
             "multitud de gente que trajesen piedras de los montes para la "
             "edificación de la torre.",
    (81, 5): "Eran traídas, pues, de todos los montes, de diversos colores, "
             "labradas por los hombres, y eran entregadas a las vírgenes; y "
             "las vírgenes las pasaban por la puerta y las entregaban para la "
             "edificación de la torre. Y cuando las piedras de diversos "
             "colores fueron puestas en la edificación, se volvieron iguales, "
             "blancas, y cambiaban sus diversos colores.",
    (81, 6): "Pero algunas piedras eran entregadas por los hombres para la "
             "edificación y no se volvían resplandecientes, sino que tales "
             "cuales fueron puestas, tales fueron también halladas; porque no "
             "habían sido entregadas por las vírgenes ni pasadas por la "
             "puerta. Estas piedras, pues, eran impropias en la edificación "
             "de la torre.",
    (81, 7): "Y viendo los seis hombres las piedras impropias en la "
             "edificación, mandaron que fuesen quitadas y llevadas abajo, a "
             "su propio lugar, de donde habían sido traídas.",
    (81, 8): "Y dicen a los hombres que traían las piedras: No entreguéis "
             "vosotros en absoluto piedras para la edificación; sino ponedlas "
             "junto a la torre, para que las vírgenes las pasen por la puerta "
             "y las entreguen para la edificación. Porque si no son pasadas "
             "por la puerta por las manos de estas vírgenes, dicen, no pueden "
             "cambiar sus colores; no trabajéis, pues, dicen, en vano.",

    # Capítulo 82
    (82, 1): "Y en aquel día se acabó la edificación, pero la torre no quedó "
             "terminada; porque había de ser edificada todavía más; y hubo "
             "una pausa en la edificación. Y los seis hombres mandaron a "
             "todos los que edificaban que se retirasen un poco y "
             "descansasen; pero a las vírgenes les ordenaron que no se "
             "retirasen de la torre. Y me parecía que las vírgenes habían "
             "sido dejadas para guardar la torre.",
    (82, 2): "Y después que todos se retiraron y descansaron, digo al pastor: "
             "¿Por qué, digo, señor, no fue acabada la edificación de la "
             "torre? Todavía no, dice, puede ser terminada la torre, hasta "
             "que venga su señor y pruebe esta edificación, para que, si se "
             "hallan algunas piedras podridas, las cambie; porque la torre se "
             "edifica conforme a la voluntad de él.",
    (82, 3): "Quisiera, digo, señor, saber de esta torre qué es esta "
             "edificación, y acerca de la roca y de la puerta y de los montes "
             "y de las vírgenes, y de las piedras que subieron del abismo y "
             "no fueron labradas, sino que así fueron a la edificación.",
    (82, 4): "Y por qué primero fueron puestas en los cimientos diez piedras, "
             "luego veinte, luego treinta y cinco, luego cuarenta; y acerca "
             "de las piedras que fueron a la edificación y otra vez fueron "
             "quitadas y puestas aparte en su propio lugar; acerca de todas "
             "estas cosas haz descansar mi alma, señor, y házmelas saber.",
    (82, 5): "Si no eres hallado, dice, afanoso en vano, lo sabrás todo; "
             "porque dentro de pocos días vendremos aquí, y verás lo demás "
             "que ha de sobrevenir a esta torre, y conocerás con exactitud "
             "todas las semejanzas.",
    (82, 6): "Y dentro de pocos días vinimos al lugar donde nos habíamos "
             "sentado, y me dice: Vamos a la torre; porque el dueño de la "
             "torre viene a examinarla. Y fuimos a la torre; y no había "
             "absolutamente nadie junto a ella, sino solamente las vírgenes.",
    (82, 7): "Y el pastor pregunta a las vírgenes si acaso había llegado el "
             "señor de la torre. Y ellas dijeron que estaba a punto de venir "
             "a examinar la edificación.",

    # Capítulo 83
    (83, 1): "Y he aquí, al poco rato veo una formación de muchos hombres que "
             "venían; y en medio de ellos un hombre tan alto de estatura que "
             "sobrepasaba la torre.",
    (83, 2): "Y los seis hombres que estaban puestos sobre la edificación "
             "caminaban con él a la derecha y a la izquierda, y todos los que "
             "habían trabajado en la edificación estaban con él, y otros "
             "muchos gloriosos alrededor de él. Y las vírgenes que guardaban "
             "la torre, corriendo hacia él, lo besaron y comenzaron a caminar "
             "cerca de él alrededor de la torre.",
    (83, 3): "Y aquel hombre examinaba la edificación con exactitud, tanto "
             "que palpaba cada piedra una por una. Y teniendo una vara en la "
             "mano, golpeaba una por una las piedras edificadas.",
    (83, 4): "Y cuando golpeaba, algunas de ellas se volvían negras como el "
             "hollín, y otras sarnosas, y otras con grietas, y otras "
             "mutiladas, y otras ni blancas ni negras, y otras ásperas y que "
             "no concordaban con las demás piedras, y otras con muchas "
             "manchas; éstas eran las variedades de las piedras que fueron "
             "halladas podridas en la edificación.",
    (83, 5): "Mandó, pues, que todas éstas fuesen sacadas de la torre y "
             "puestas junto a la torre, y que se trajesen otras piedras y se "
             "pusiesen en su lugar.",
    (83, 6): "Y le preguntaron los que edificaban de qué monte quería que se "
             "trajesen piedras para ponerlas en su lugar. Y no mandó que se "
             "trajesen de los montes, sino que mandó que se trajesen de "
             "cierta llanura que estaba cerca.",
    (83, 7): "Y fue cavada la llanura, y se hallaron piedras resplandecientes "
             "cuadradas, y algunas también redondas. Y todas cuantas piedras "
             "había en aquella llanura fueron traídas, y eran llevadas por "
             "las vírgenes a través de la puerta.",
    (83, 8): "Y las piedras cuadradas fueron labradas y puestas en el lugar "
             "de las que habían sido quitadas; pero las redondas no fueron "
             "puestas en la edificación, porque eran duras para labrarlas, y "
             "se hacía lentamente. Y fueron puestas junto a la torre, como "
             "que habían de ser labradas y puestas en la edificación; porque "
             "eran muy resplandecientes.",

    # Capítulo 84
    (84, 1): "Habiendo, pues, acabado estas cosas el hombre glorioso y señor "
             "de toda la torre, llamó al pastor y le entregó todas las "
             "piedras que estaban junto a la torre, las que habían sido "
             "desechadas de la edificación, y le dice:",
    (84, 2): "Limpia con cuidado estas piedras y ponlas en la edificación de "
             "la torre, las que puedan ajustarse con las demás; y las que no "
             "se ajusten, arrójalas lejos de la torre.",
    (84, 3): "Habiendo mandado esto al pastor, se fue de la torre con todos "
             "aquellos con quienes había venido; y las vírgenes estaban de "
             "pie alrededor de la torre guardándola.",
    (84, 4): "Digo al pastor: ¿Cómo pueden estas piedras ir a la edificación "
             "de la torre, habiendo sido reprobadas? Respondiendo, me dice: "
             "¿Ves, dice, estas piedras? Las veo, digo, señor. Yo, dice, "
             "labraré la mayor parte de estas piedras y las pondré en la "
             "edificación, y se ajustarán con las demás piedras.",
    (84, 5): "¿Cómo, digo, señor, pueden, siendo recortadas, llenar el mismo "
             "lugar? Respondiendo, me dice: Cuantas sean halladas pequeñas "
             "serán puestas en medio de la edificación, y cuantas mayores, "
             "serán puestas más afuera y las sujetarán.",
    (84, 6): "Habiéndome hablado estas cosas, me dice: Vámonos, y dentro de "
             "dos días volvamos y limpiemos estas piedras y pongámoslas en la "
             "edificación; porque todo lo que está alrededor de la torre debe "
             "ser limpiado, no sea que el señor venga de repente y halle "
             "sucio lo que está en torno a la torre y se enoje, y estas "
             "piedras no vayan a la edificación de la torre, y yo parezca "
             "negligente delante del señor.",
    (84, 7): "Y dentro de dos días fuimos a la torre, y me dice: Examinemos "
             "todas las piedras y veamos las que pueden ir a la edificación. "
             "Le digo: Señor, examinémoslas.",

    # Capítulo 85
    (85, 1): "Y comenzando, examinamos primero las piedras negras. Y tales "
             "cuales fueron sacadas de la edificación, tales fueron también "
             "halladas. Y el pastor mandó que fuesen llevadas lejos de la "
             "torre y separadas.",
    (85, 2): "Luego examinó las sarnosas, y tomándolas labró muchas de ellas, "
             "y mandó a las vírgenes que las alzasen y pusiesen en la "
             "edificación. Y las vírgenes las alzaron y las pusieron en medio "
             "de la edificación de la torre. Y a las demás mandó que fuesen "
             "puestas con las negras; porque también éstas fueron halladas "
             "negras.",
    (85, 3): "Luego examinaba las que tenían grietas; y de éstas labró "
             "muchas, y mandó que fuesen llevadas por medio de las vírgenes a "
             "la edificación; y fueron puestas más afuera, porque fueron "
             "halladas más sanas. Pero las demás, por la multitud de sus "
             "grietas, no pudieron ser labradas; por esta causa, pues, fueron "
             "desechadas de la edificación de la torre.",
    (85, 4): "Luego examinaba las mutiladas, y se hallaron muchas negras "
             "entre ellas, y algunas que habían hecho grandes grietas; y "
             "mandó que también éstas fuesen puestas con las desechadas. Y "
             "las que de ellas sobraban, habiéndolas limpiado y labrado, "
             "mandó que fuesen puestas en la edificación. Y las vírgenes, "
             "alzándolas, las ajustaron en medio de la edificación de la "
             "torre; porque eran más débiles.",
    (85, 5): "Luego examinaba las que eran mitad blancas y mitad negras; y "
             "muchas de ellas fueron halladas negras. Y mandó que también "
             "éstas fuesen quitadas con las desechadas. Y todas las demás "
             "fueron alzadas por las vírgenes; porque, siendo blancas, fueron "
             "ajustadas por las mismas vírgenes en la edificación; y fueron "
             "puestas más afuera, porque fueron halladas sanas, de modo que "
             "podían sostener a las que habían sido puestas en medio; porque "
             "nada en absoluto de ellas fue mutilado.",
    (85, 6): "Luego examinaba las ásperas y duras; y pocas de ellas fueron "
             "desechadas por no poder ser labradas; porque fueron halladas "
             "muy duras. Y las demás de ellas fueron labradas y alzadas por "
             "las vírgenes, y ajustadas en medio de la edificación de la "
             "torre; porque eran más débiles.",
    (85, 7): "Luego examinaba las que tenían las manchas; y de éstas "
             "poquísimas se habían ennegrecido y fueron desechadas con las "
             "demás. Y las que sobraban fueron halladas resplandecientes y "
             "sanas; y éstas fueron ajustadas por las vírgenes en la "
             "edificación, y fueron puestas más afuera a causa de su "
             "fortaleza.",

    # Capítulo 86
    (86, 1): "Luego vino a examinar las piedras blancas y redondas, y me "
             "dice: ¿Qué hacemos con estas piedras? ¿Qué sé yo, digo, señor? "
             "¿No discurres, pues, nada acerca de ellas?",
    (86, 2): "Yo, digo, señor, no tengo este oficio, ni soy cantero, ni puedo "
             "entenderlo. ¿No ves, dice, que son muy redondas? Y si quiero "
             "hacerlas cuadradas, mucho ha de ser cortado de ellas; y sin "
             "embargo es menester por necesidad que algunas de ellas sean "
             "puestas en la edificación.",
    (86, 3): "Si, pues, digo, señor, es necesario, ¿por qué te atormentas y "
             "no escoges para la edificación las que quieras y las ajustas en "
             "ella? Escogió de ellas las mayores y resplandecientes y las "
             "labró; y las vírgenes, alzándolas, las ajustaron en las partes "
             "más exteriores de la edificación.",
    (86, 4): "Y las demás que sobraron fueron alzadas y puestas aparte en la "
             "llanura de donde habían sido traídas; pero no fueron "
             "desechadas: Porque, dice, le falta todavía a la torre un poco "
             "por edificarse. Y el señor de la torre quiere que todas estas "
             "piedras sean ajustadas en la edificación, porque son muy "
             "resplandecientes.",
    (86, 5): "Y fueron llamadas doce mujeres, hermosísimas de figura, "
             "vestidas de negro, ceñidas y con los hombros descubiertos y los "
             "cabellos sueltos; y me parecía que estas mujeres eran feroces. "
             "Y el pastor les mandó que alzasen las piedras desechadas de la "
             "edificación y las llevasen a los montes de donde también habían "
             "sido traídas.",
    (86, 6): "Y ellas, alegres, alzaron y llevaron todas las piedras y las "
             "pusieron de donde habían sido tomadas. Y después que fueron "
             "alzadas todas las piedras y ya no quedaba piedra alguna "
             "alrededor de la torre, me dice el pastor: Rodeemos la torre y "
             "veamos si hay en ella algún defecto. Y yo la rodeaba con él.",
    (86, 7): "Y viendo el pastor que la torre era hermosa en su edificación, "
             "estaba muy alegre; porque la torre estaba edificada de tal "
             "manera que yo, al verla, codiciaba su edificación; porque "
             "estaba edificada como si fuese de una sola piedra, sin tener "
             "una sola juntura en sí. Y la piedra parecía como labrada de la "
             "roca; porque me parecía que era de una sola piedra.",

    # Capítulo 87
    (87, 1): "Y yo, caminando con él, estaba alegre viendo tales bienes. Y me "
             "dice el pastor: Ve y trae cal y teja molida fina, para que yo "
             "rellene las marcas de las piedras que fueron alzadas y puestas "
             "en la edificación; porque todo lo que está alrededor de la "
             "torre debe quedar liso.",
    (87, 2): "E hice como me mandó, y se lo traje. Sírveme, dice, y pronto se "
             "acabará la obra. Rellenó, pues, las marcas de las piedras que "
             "habían ido a la edificación, y mandó que se barriese alrededor "
             "de la torre y quedase limpio.",
    (87, 3): "Y las vírgenes, tomando escobas, barrieron, y quitaron de la "
             "torre toda la basura, y rociaron agua; y el lugar de la torre "
             "se hizo alegre y hermosísimo.",
    (87, 4): "Me dice el pastor: Todo, dice, ha sido limpiado; si viene el "
             "señor a visitar la torre, no tiene nada que reprendernos. Dicho "
             "esto, quería irse.",
    (87, 5): "Pero yo lo así de su zurrón y comencé a conjurarle por el Señor "
             "que me explicase lo que me había mostrado. Me dice: Tengo que "
             "ausentarme un poco, y te lo explicaré todo; espérame aquí hasta "
             "que vuelva.",
    (87, 6): "Le digo: Señor, estando solo aquí, ¿qué haré yo? No estás, "
             "dice, solo; porque estas vírgenes están contigo. Entrégame, "
             "pues, digo, a ellas. El pastor las llama y les dice: Os "
             "encomiendo a éste hasta que vuelva; y se fue.",
    (87, 7): "Y yo estaba solo con las vírgenes; y ellas estaban muy alegres "
             "y eran bondadosas conmigo; sobre todo las cuatro más gloriosas "
             "de ellas.",

    # Capítulo 88
    (88, 1): "Me dicen las vírgenes: Hoy el pastor no viene aquí. ¿Qué haré, "
             "pues, yo?, digo. Espéralo, dicen, hasta la tarde; y si viene, "
             "hablará contigo; y si no viene, te quedarás aquí con nosotras "
             "hasta que venga.",
    (88, 2): "Les digo: Lo esperaré hasta la tarde; y si no viene, me iré a "
             "casa y volveré de mañana. Y ellas, respondiendo, me dicen: A "
             "nosotras fuiste entregado; no puedes apartarte de nosotras.",
    (88, 3): "¿Dónde, pues, digo, me quedaré? Con nosotras, dicen, dormirás "
             "como hermano, y no como varón; porque eres nuestro hermano, y "
             "en adelante hemos de morar contigo, porque te amamos mucho. Y "
             "yo me avergonzaba de quedarme con ellas.",
    (88, 4): "Y la que parecía ser la primera de ellas comenzó a besarme y "
             "abrazarme. Y las otras, viendo que aquélla me abrazaba, también "
             "ellas comenzaron a besarme y a llevarme alrededor de la torre y "
             "a jugar conmigo.",
    (88, 5): "Y yo me había vuelto como más joven, y comencé también yo a "
             "jugar con ellas; porque unas danzaban en coro, otras bailaban, "
             "otras cantaban; y yo, guardando silencio, caminaba con ellas "
             "alrededor de la torre y estaba alegre con ellas.",
    (88, 6): "Y llegada la tarde, quería irme a casa; pero ellas no me "
             "dejaron, sino que me retuvieron. Y me quedé con ellas aquella "
             "noche y dormí junto a la torre.",
    (88, 7): "Porque las vírgenes tendieron en el suelo sus túnicas de lino y "
             "me hicieron recostar en medio de ellas, y no hacían "
             "absolutamente nada sino orar; y yo oraba con ellas sin cesar, y "
             "no menos que ellas. Y las vírgenes se gozaban de que yo orase "
             "así. Y me quedé allí hasta el día siguiente, hasta la hora "
             "segunda, con las vírgenes.",
    (88, 8): "Luego llegó el pastor, y dice a las vírgenes: ¿No le habéis "
             "hecho alguna afrenta? Pregúntale, dicen, a él. Le digo: Señor, "
             "me he regocijado quedándome con ellas. ¿Qué cenaste?, dice. "
             "Cené, digo, señor, palabras del Señor toda la noche. ¿Te "
             "recibieron bien?, dice. Sí, digo, señor.",
    (88, 9): "Ahora, dice, ¿qué quieres oír primero? Según, digo, señor, me "
             "lo mostraste desde el principio; te ruego, señor, que según yo "
             "te pregunte, así también me lo declares. Como quieras, dice, "
             "así también te lo explicaré, y no te ocultaré absolutamente "
             "nada.",

    # Capítulo 89
    (89, 1): "Primero de todo, digo, señor, declárame esto: la roca y la "
             "puerta, ¿qué es? Esta roca, dice, y la puerta es el Hijo de "
             "Dios. ¿Cómo, digo, señor, la roca es antigua, y la puerta "
             "nueva? Escucha, dice, y entiende, falto de entendimiento.",
    (89, 2): "El Hijo de Dios es anterior a toda su creación, de modo que fue "
             "consejero del Padre en su creación; por esto también la roca es "
             "antigua. Y la puerta, ¿por qué es nueva, digo, señor?",
    (89, 3): "Porque, dice, fue manifestado en los postreros días de la "
             "consumación; por esto la puerta se hizo nueva, para que los que "
             "han de ser salvos entren por ella en el reino de Dios.",
    (89, 4): "¿Viste, dice, que las piedras que entraron por la puerta fueron "
             "puestas en la edificación de la torre, y las que no entraron "
             "fueron desechadas otra vez a su propio lugar? Lo vi, digo, "
             "señor. Así, dice, nadie entrará en el reino de Dios si no "
             "recibe su santo nombre.",
    (89, 5): "Porque si quieres entrar en alguna ciudad, y aquella ciudad "
             "está amurallada alrededor y tiene una sola puerta, ¿acaso "
             "puedes entrar en aquella ciudad sino por la puerta que tiene? "
             "¿Pues cómo, digo, señor, puede ser de otro modo? Si, pues, no "
             "puedes entrar en la ciudad sino por la puerta que tiene, así, "
             "dice, tampoco en el reino de Dios puede el hombre entrar de "
             "otro modo sino por el nombre de su Hijo, el amado por él.",
    (89, 6): "¿Viste, dice, la multitud que edificaba la torre? La vi, digo, "
             "señor. Aquéllos, dice, son todos ángeles gloriosos; con éstos, "
             "pues, está amurallado el Señor. Y la puerta es el Hijo de Dios; "
             "ésta es la única entrada al Señor. De otro modo, pues, nadie "
             "entrará a él sino por su Hijo.",
    (89, 7): "¿Viste, dice, a los seis hombres, y al hombre glorioso y grande "
             "en medio de ellos, el que caminaba alrededor de la torre y "
             "reprobó las piedras de la edificación? Lo vi, digo, señor.",
    (89, 8): "El hombre glorioso, dice, es el Hijo de Dios, y aquellos seis "
             "son los ángeles gloriosos que lo acompañan a derecha e "
             "izquierda. De estos ángeles gloriosos, dice, ninguno entrará a "
             "Dios sin él; el que no reciba su nombre no entrará en el reino "
             "de Dios.",

    # Capítulo 90
    (90, 1): "Y la torre, dije yo, ¿qué es? La torre, dijo, es la iglesia.",
    (90, 2): "Y estas vírgenes, ¿quiénes son? Éstas, dijo, son espíritus "
             "santos; y de otra manera no puede el hombre hallarse en el "
             "reino de Dios, si éstas no le visten de su vestidura; porque si "
             "recibes sólo el nombre, y no recibes de ellas la vestidura, de "
             "nada te aprovechará; porque estas vírgenes son potencias del "
             "Hijo de Dios. Si llevas el nombre, y no llevas su potencia, en "
             "vano llevarás su nombre.",
    (90, 3): "Y las piedras, dijo, que viste desechadas, éstos llevaron el "
             "nombre, mas no se vistieron del vestido de las vírgenes. ¿Cuál "
             "es, dije yo, su vestido, señor? Los mismos nombres, dijo, son "
             "su vestido. El que lleva el nombre del Hijo de Dios, debe "
             "llevar también los nombres de éstas; porque aun el mismo Hijo "
             "lleva los nombres de estas vírgenes.",
    (90, 4): "Cuantas piedras viste, dijo, que entraron en la edificación de "
             "la torre, entregadas por las manos de ellas y que permanecieron "
             "en la edificación, éstos están vestidos de la potencia de estas "
             "vírgenes.",
    (90, 5): "Por esto ves la torre hecha de una sola piedra con la roca; así "
             "también los que creyeron al Señor por medio de su Hijo, y se "
             "visten de estos espíritus, serán un solo espíritu, un solo "
             "cuerpo, y un solo color será el de sus vestidos. Y de los tales "
             "que llevan los nombres de las vírgenes es la morada en la "
             "torre.",
    (90, 6): "Entonces, señor, dije yo, las piedras desechadas, ¿por qué "
             "fueron desechadas? Porque pasaron por la puerta, y por las "
             "manos de las vírgenes fueron puestas en la edificación de la "
             "torre. Ya que de todo te cuidas, dijo, e inquieres con "
             "diligencia, oye acerca de las piedras desechadas.",
    (90, 7): "Éstos, dijo, todos recibieron el nombre del Hijo de Dios, y "
             "recibieron también la potencia de estas vírgenes. Habiendo, "
             "pues, recibido estos espíritus, fueron fortalecidos y estaban "
             "con los siervos de Dios, y era de ellos un solo espíritu y un "
             "solo cuerpo y una sola vestidura; porque sentían lo mismo y "
             "obraban justicia.",
    (90, 8): "Mas después de algún tiempo fueron persuadidos por las mujeres "
             "que viste vestidas de ropas negras, que tenían los hombros "
             "descubiertos y los cabellos sueltos, y eran hermosas; al verlas "
             "las codiciaron, y se vistieron de la potencia de ellas, y se "
             "despojaron de la vestidura y de la potencia de las vírgenes.",
    (90, 9): "Éstos, pues, fueron desechados de la casa de Dios y entregados "
             "a aquéllas; mas los que no fueron engañados por la hermosura de "
             "estas mujeres permanecieron en la casa de Dios. Tienes, dijo, "
             "la explicación de los desechados.",

    # Capítulo 91
    (91, 1): "¿Qué, pues, señor, dije yo, si estos hombres, siendo tales, se "
             "arrepienten y desechan los deseos de estas mujeres, y se "
             "vuelven a las vírgenes y andan en la potencia de ellas y en sus "
             "obras, no entrarán en la casa de Dios?",
    (91, 2): "Entrarán, dijo, si desechan las obras de estas mujeres, y "
             "vuelven a tomar la potencia de las vírgenes y andan en sus "
             "obras; porque por esto también hubo pausa en la edificación, "
             "para que, si éstos se arrepienten, vayan a la edificación de la "
             "torre. Mas si no se arrepienten, entonces entrarán otros, y "
             "éstos serán echados fuera para siempre.",
    (91, 3): "Por todas estas cosas di gracias al Señor, porque tuvo "
             "misericordia de todos los que invocan su nombre, y envió al "
             "ángel de la penitencia a nosotros los que habíamos pecado "
             "contra él, y renovó nuestro espíritu, y cuando estábamos ya "
             "corrompidos y sin esperanza de vivir, renovó nuestra vida.",
    (91, 4): "Ahora, señor, dije yo, declárame por qué la torre no está "
             "edificada sobre el suelo, sino sobre la roca y sobre la puerta. "
             "¿Todavía, dijo, eres necio y sin entendimiento? Necesidad "
             "tengo, señor, dije yo, de preguntártelo todo, porque en "
             "absoluto nada puedo entender; porque todas las cosas son "
             "grandes y gloriosas y difíciles de entender para los hombres.",
    (91, 5): "Oye, dijo: el nombre del Hijo de Dios es grande e "
             "incomprensible, y sostiene al mundo entero. Si, pues, toda la "
             "creación es sostenida por el Hijo de Dios, ¿qué piensas de los "
             "que son llamados por él, y llevan el nombre del Hijo de Dios y "
             "andan en sus mandamientos?",
    (91, 6): "¿Ves, pues, a quiénes sostiene? A los que de todo corazón "
             "llevan su nombre. Él mismo, pues, fue hecho fundamento para "
             "ellos, y de buena gana los sostiene, porque no se avergüenzan "
             "de llevar su nombre.",

    # Capítulo 92
    (92, 1): "Declárame, señor, dije yo, los nombres de las vírgenes y de las "
             "mujeres vestidas de ropas negras. Oye, dijo, los nombres de las "
             "vírgenes más fuertes, las que estaban puestas en los ángulos.",
    (92, 2): "La primera es Fe, la segunda Continencia, la tercera Potencia, "
             "la cuarta Longanimidad; y las otras, puestas entre éstas, "
             "tienen estos nombres: Sencillez, Inocencia, Pureza, Alegría, "
             "Verdad, Entendimiento, Concordia, Amor. El que lleva estos "
             "nombres y el nombre del Hijo de Dios, podrá entrar en el reino "
             "de Dios.",
    (92, 3): "Oye, dijo, también los nombres de las mujeres que tienen las "
             "ropas negras. También de éstas cuatro son más poderosas: la "
             "primera Incredulidad, la segunda Incontinencia, la tercera "
             "Desobediencia, la cuarta Engaño. Y sus seguidoras se llaman "
             "Tristeza, Maldad, Lascivia, Ira, Mentira, Insensatez, "
             "Maledicencia, Odio. El siervo de Dios que lleva estos nombres "
             "verá ciertamente el reino de Dios, mas no entrará en él.",
    (92, 4): "Y las piedras, señor, dije yo, que fueron ajustadas en la "
             "edificación desde lo profundo, ¿quiénes son? Las primeras, "
             "dijo, las diez que fueron puestas en los cimientos, son la "
             "primera generación; las veinticinco, la segunda generación de "
             "varones justos; las treinta y cinco son los profetas de Dios y "
             "sus ministros; las cuarenta, los apóstoles y maestros de la "
             "predicación del Hijo de Dios.",
    (92, 5): "¿Por qué, pues, señor, dije yo, las vírgenes entregaron también "
             "estas piedras para la edificación de la torre, llevándolas a "
             "través de la puerta?",
    (92, 6): "Porque éstos, dijo, fueron los primeros en llevar estos "
             "espíritus, y en ninguna manera se apartaron unos de otros, ni "
             "los espíritus de los hombres ni los hombres de los espíritus, "
             "sino que los espíritus permanecieron con ellos hasta su "
             "dormición. Y si no hubieran tenido consigo estos espíritus, no "
             "habrían sido útiles para la edificación de esta torre.",

    # Capítulo 93
    (93, 1): "Declárame aún, señor, dije yo. ¿Qué, dijo, buscas? ¿Por qué, "
             "señor, dije yo, las piedras subieron de lo profundo y fueron "
             "puestas en la edificación de la torre, habiendo llevado estos "
             "espíritus?",
    (93, 2): "Necesidad tenían, dijo, de subir por el agua, para ser "
             "vivificados; porque no podían de otra manera entrar en el reino "
             "de Dios, si no se despojaban de la mortandad de su vida "
             "anterior.",
    (93, 3): "Recibieron, pues, también éstos que habían dormido el sello del "
             "Hijo de Dios, y entraron en el reino de Dios; porque antes, "
             "dijo, que el hombre lleve el nombre del Hijo de Dios, está "
             "muerto; mas cuando recibe el sello, se despoja de la mortandad "
             "y recibe la vida.",
    (93, 4): "El sello, pues, es el agua; en el agua, pues, descienden "
             "muertos y suben vivos. También a aquéllos, pues, les fue "
             "predicado este sello, y se valieron de él para entrar en el "
             "reino de Dios.",
    (93, 5): "¿Por qué, señor, dije yo, también las cuarenta piedras subieron "
             "con ellas de lo profundo, habiendo tenido ya el sello? Porque "
             "éstos, dijo, los apóstoles y los maestros que predicaron el "
             "nombre del Hijo de Dios, habiendo dormido en la potencia y en "
             "la fe del Hijo de Dios, predicaron también a los que habían "
             "dormido antes, y ellos mismos les dieron el sello de la "
             "predicación.",
    (93, 6): "Descendieron, pues, con ellos al agua, y subieron de nuevo; mas "
             "éstos descendieron vivos y subieron vivos, y aquéllos que "
             "habían dormido antes descendieron muertos y subieron vivos.",
    (93, 7): "Por medio de éstos, pues, fueron vivificados y conocieron el "
             "nombre del Hijo de Dios; por esto también subieron juntamente "
             "con ellos, y fueron ajustados en la edificación de la torre, y "
             "sin ser labrados fueron edificados juntamente; porque durmieron "
             "en justicia y en gran pureza; sólo que no tenían este sello. "
             "Tienes, pues, también la explicación de éstos. La tengo, señor, "
             "dije yo.",

    # Capítulo 94
    (94, 1): "Ahora, pues, señor, declárame acerca de los montes: ¿por qué "
             "son diversas y variadas sus formas? Oye, dijo: estos montes son "
             "las doce tribus que habitan el mundo entero. A éstas, pues, fue "
             "predicado el Hijo de Dios por medio de los apóstoles.",
    (94, 2): "Mas ¿por qué son variados los montes, y cada uno de forma "
             "distinta? Declárámelo, señor. Oye, dijo: estas doce tribus que "
             "habitan el mundo entero son doce naciones; y son variadas en "
             "prudencia y en entendimiento; cuales viste, pues, los montes "
             "variados, tales son también las variedades del entendimiento y "
             "la prudencia de estas naciones. Y te declararé también la "
             "conducta de cada una.",
    (94, 3): "Primero, señor, dije yo, declárame esto: ¿por qué, siendo los "
             "montes tan variados, cuando sus piedras fueron puestas en la "
             "edificación, se volvieron resplandecientes de un solo color, "
             "como también las piedras que habían subido de lo profundo?",
    (94, 4): "Porque, dijo, todas las naciones que habitan debajo del cielo, "
             "habiendo oído y creído, fueron llamadas por el nombre del Hijo "
             "de Dios. Habiendo, pues, recibido el sello, tuvieron una sola "
             "prudencia y un solo entendimiento, y una sola fe fue la de "
             "ellos y un solo amor, y llevaron los espíritus de las vírgenes "
             "junto con el nombre; por esto la edificación de la torre se "
             "volvió de un solo color, resplandeciente como el sol.",
    (94, 5): "Mas después que entraron juntos y fueron hechos un solo cuerpo, "
             "algunos de ellos se contaminaron a sí mismos y fueron echados "
             "del linaje de los justos, y volvieron a ser cuales eran antes, "
             "y aun peores.",

    # Capítulo 95
    (95, 1): "¿Cómo, señor, dije yo, se hicieron peores, habiendo conocido a "
             "Dios? El que no conoce a Dios, dijo, y obra el mal, tiene algún "
             "castigo por su maldad; mas el que ha conocido a Dios ya no debe "
             "obrar el mal, sino hacer el bien.",
    (95, 2): "Si, pues, el que debe hacer el bien obra el mal, ¿no parece que "
             "comete mayor maldad que el que no conoce a Dios? Por esto los "
             "que no han conocido a Dios y obran el mal están condenados a "
             "muerte; mas los que han conocido a Dios y han visto sus "
             "maravillas, y obran el mal, serán castigados doblemente y "
             "morirán para siempre. Así, pues, será purificada la iglesia de "
             "Dios.",
    (95, 3): "Y como viste las piedras quitadas de la torre y entregadas a "
             "los espíritus malos, y echadas de allí: ʽy será un solo cuerpo "
             "el de los purificados, así como también la torre vino a ser "
             "como hecha de una sola piedra después de ser purificadaʼ, así "
             "será también la iglesia de Dios después de ser purificada y de "
             "ser desechados los malos, y los hipócritas, y los blasfemos, y "
             "los de doble ánimo, y los que obran el mal con diversas "
             "maldades.",
    (95, 4): "Después que éstos sean desechados, la iglesia de Dios será un "
             "solo cuerpo, una sola prudencia, un solo entendimiento, una "
             "sola fe, un solo amor; y entonces el Hijo de Dios se regocijará "
             "y se alegrará en ellos, habiendo recibido a su pueblo puro. "
             "Grandes, señor, dije yo, y gloriosas son todas estas cosas.",
    (95, 5): "Declárame aún, señor, dije yo, la potencia y las obras de cada "
             "uno de los montes, para que toda alma que confía en el Señor, "
             "al oírlo, glorifique su nombre grande y maravilloso y glorioso. "
             "Oye, dijo, la variedad de los montes y de las doce naciones.",

    # Capítulo 96
    (96, 1): "Los que creyeron del primer monte, el negro, son tales como "
             "éstos: apóstatas y blasfemos contra el Señor, y traidores de "
             "los siervos de Dios. Para éstos no hay penitencia, sino que hay "
             "muerte, y por esto también son negros; porque su linaje es "
             "inicuo.",
    (96, 2): "Y los que creyeron del segundo monte, el pelado, son tales como "
             "éstos: hipócritas y maestros de maldad. También éstos, pues, "
             "son semejantes a los primeros, no teniendo fruto de justicia; "
             "porque como su monte es sin fruto, así también los hombres "
             "tales tienen nombre, mas están vacíos de la fe, y no hay en "
             "ellos ningún fruto de verdad. Para éstos, pues, hay penitencia, "
             "si se arrepienten pronto; mas si tardan, su muerte será con la "
             "de los primeros.",
    (96, 3): "¿Por qué, señor, dije yo, para éstos hay penitencia, y para los "
             "primeros no la hay? Pues casi las mismas son sus obras. Por "
             "esto, dijo, hay penitencia para éstos, porque no blasfemaron a "
             "su Señor ni fueron traidores de los siervos de Dios; sino que "
             "por el deseo de ganancia fingieron, y enseñó cada uno conforme "
             "a los deseos de los hombres que pecan. Mas pagarán alguna pena; "
             "con todo, hay penitencia para ellos, por no haber sido "
             "blasfemos ni traidores.",

    # Capítulo 97
    (97, 1): "Y los que creyeron del tercer monte, el que tiene espinas y "
             "abrojos, son tales como éstos: de ellos, unos son ricos, y "
             "otros están enredados en muchos negocios. Los abrojos son los "
             "ricos, y las espinas los que están enredados en los diversos "
             "negocios.",
    (97, 2): "Éstos, pues, los que están enredados en muchos y diversos "
             "negocios, no se juntan con los siervos de Dios, sino que se "
             "descarrían, ahogados por sus ocupaciones; y los ricos "
             "difícilmente se juntan con los siervos de Dios, temiendo que "
             "éstos les pidan algo. Los tales, pues, difícilmente entrarán en "
             "el reino de Dios.",
    (97, 3): "Porque así como es difícil andar entre abrojos con los pies "
             "desnudos, así también a los tales les es difícil entrar en el "
             "reino de Dios.",
    (97, 4): "Mas para todos éstos hay penitencia, pero pronta, para que lo "
             "que no obraron en los tiempos anteriores, lo recobren ahora en "
             "estos días, y hagan algún bien. Si, pues, se arrepienten y "
             "hacen algún bien, vivirán para Dios; mas si permanecen en sus "
             "ocupaciones, serán entregados a aquellas mujeres, las cuales "
             "les darán muerte.",

    # Capítulo 98
    (98, 1): "Y los que creyeron del cuarto monte, el que tiene muchas "
             "hierbas, verdes en lo alto de las hierbas y secas junto a las "
             "raíces, y algunas también secándose por el sol, son tales como "
             "éstos: unos son de doble ánimo, y otros tienen al Señor en los "
             "labios, mas no le tienen en el corazón.",
    (98, 2): "Por esto sus cimientos están secos y sin fuerza, y sólo sus "
             "palabras viven, mas sus obras están muertas. Los tales ni viven "
             "ni están muertos. Son, pues, semejantes a los de doble ánimo; "
             "porque también los de doble ánimo no están ni verdes ni secos; "
             "porque ni viven ni están muertos.",
    (98, 3): "Porque así como estas hierbas, al ver el sol, se secaron, así "
             "también los de doble ánimo, cuando oyen de tribulación, por su "
             "cobardía sirven a los ídolos y se avergüenzan del nombre de su "
             "Señor.",
    (98, 4): "Los tales, pues, ni viven ni están muertos. Mas también éstos, "
             "si se arrepienten pronto, podrán vivir; mas si no se "
             "arrepienten, ya están entregados a las mujeres que les quitan "
             "la vida.",

    # Capítulo 99
    (99, 1): "Y los que creyeron del quinto monte, el que tiene hierbas "
             "verdes y es escabroso, son tales como éstos: fieles "
             "ciertamente, mas tardos para aprender, y arrogantes, y "
             "complacientes consigo mismos, queriendo saberlo todo, y no "
             "saben nada en absoluto.",
    (99, 2): "Por esta su arrogancia se apartó de ellos el entendimiento, y "
             "entró en ellos una necia insensatez. Y se alaban a sí mismos "
             "como quienes tienen entendimiento, y quieren ser maestros por "
             "su propia cuenta, siendo insensatos.",
    (99, 3): "Por esta altivez, pues, muchos se vaciaron, ensalzándose a sí "
             "mismos; porque gran demonio es la arrogancia y la vana "
             "confianza. De éstos, pues, muchos fueron desechados; mas "
             "algunos se arrepintieron y creyeron, y se sometieron a los que "
             "tienen entendimiento, reconociendo su propia insensatez.",
    (99, 4): "Y también para los demás que son tales hay penitencia; porque "
             "no fueron malos, sino más bien necios y sin entendimiento. "
             "Éstos, pues, si se arrepienten, vivirán para Dios; mas si no se "
             "arrepienten, habitarán con las mujeres que obran el mal contra "
             "ellos.",

    # Capítulo 100
    (100, 1): "Y los que creyeron del sexto monte, el que tiene hendiduras "
              "grandes y pequeñas, y en las hendiduras hierbas marchitas, son "
              "tales como éstos:",
    (100, 2): "los que tienen las hendiduras pequeñas, éstos son los que "
              "tienen algo unos contra otros, y por sus maledicencias están "
              "marchitos en la fe; mas muchos de ellos se arrepintieron. Y "
              "también los demás se arrepentirán cuando oigan mis "
              "mandamientos; porque sus maledicencias son pequeñas, y pronto "
              "se arrepentirán.",
    (100, 3): "Mas los que tienen hendiduras grandes, éstos persisten en sus "
              "maledicencias y se vuelven rencorosos, airándose unos contra "
              "otros; éstos, pues, fueron arrojados de la torre y reprobados "
              "para su edificación. Los tales, pues, difícilmente vivirán.",
    (100, 4): "Si Dios y Señor nuestro, que se enseñorea de todas las cosas y "
              "tiene la potestad sobre toda su creación, no guarda rencor a "
              "los que confiesan sus pecados, sino que se hace propicio, ¿el "
              "hombre, que es corruptible y lleno de pecados, guarda rencor "
              "al hombre, como si pudiera perderle o salvarle?",
    (100, 5): "Y os digo yo, el ángel de la penitencia: cuantos tenéis esta "
              "secta, desechadla y arrepentíos, y el Señor sanará vuestros "
              "pecados anteriores, si os purificáis de este demonio; y si no, "
              "seréis entregados a él para muerte.",

    # Capítulo 101
    (101, 1): "Y los que creyeron del séptimo monte, en el cual había hierbas "
              "verdes y lozanas, y todo el monte era fértil, y toda clase de "
              "ganado y las aves del cielo pacían las hierbas en este monte, "
              "y las hierbas que pacían se volvían más lozanas, son tales "
              "como éstos:",
    (101, 2): "siempre fueron sencillos e inocentes y bienaventurados, no "
              "teniendo nada unos contra otros, sino regocijándose siempre en "
              "los siervos de Dios, y vestidos del Espíritu Santo de estas "
              "vírgenes, y teniendo siempre entrañas de misericordia para con "
              "todo hombre; y de sus trabajos suministraron a todo hombre sin "
              "reproche y sin vacilar.",
    (101, 3): "El Señor, pues, viendo su sencillez y toda su candidez de "
              "niños, los multiplicó en los trabajos de sus manos y les dio "
              "gracia en toda su conducta.",
    (101, 4): "Y os digo yo, el ángel de la penitencia, a vosotros los que "
              "sois tales: permaneced tales, y vuestra simiente no será "
              "borrada jamás; porque el Señor os probó y os inscribió en "
              "nuestro número, y toda vuestra simiente habitará con el Hijo "
              "de Dios; porque de su Espíritu recibisteis.",

    # Capítulo 102
    (102, 1): "Y los que creyeron del octavo monte, donde estaban las muchas "
              "fuentes, y toda la creación del Señor bebía de las fuentes, "
              "son tales como éstos:",
    (102, 2): "apóstoles y maestros que predicaron en todo el mundo, y que "
              "enseñaron con gravedad y pureza la palabra del Señor, y en "
              "nada defraudaron para mal deseo, sino que anduvieron siempre "
              "en justicia y en verdad, así como también recibieron el "
              "Espíritu Santo. La entrada de los tales, pues, es con los "
              "ángeles.",

    # Capítulo 103
    (103, 1): "Y los que creyeron del noveno monte, el desierto, el que tiene "
              "en sí los reptiles y las fieras que destruyen a los hombres, "
              "son tales como éstos:",
    (103, 2): "los que tienen las manchas son diáconos que sirvieron mal, y "
              "que despojaron la vida de viudas y huérfanos, y se "
              "enriquecieron a sí mismos con el ministerio que habían "
              "recibido para servir. Si, pues, permanecen en el mismo deseo, "
              "están muertos y no hay para ellos esperanza alguna de vida; "
              "mas si se vuelven y cumplen con pureza su ministerio, podrán "
              "vivir.",
    (103, 3): "Y los sarnosos, éstos son los que negaron y no se volvieron a "
              "su Señor, sino que se volvieron yermos y desiertos; no "
              "juntándose con los siervos de Dios, sino viviendo solos, "
              "pierden sus propias almas.",
    (103, 4): "Porque así como la vid dejada en algún cercado, cayendo en "
              "descuido, se corrompe y es asolada por las hierbas, y con el "
              "tiempo se vuelve silvestre, y ya no es útil a su dueño, así "
              "también los hombres tales se han abandonado a sí mismos, y se "
              "vuelven inútiles a su Señor, habiéndose embrutecido.",
    (103, 5): "Para éstos, pues, hay penitencia, si no se hallan haber negado "
              "de corazón; mas si alguno se halla haber negado de corazón, no "
              "sé si puede vivir.",
    (103, 6): "Y esto no lo digo para estos días, para que alguno que niegue "
              "reciba penitencia; porque imposible es que se salve el que "
              "ahora vaya a negar a su Señor; sino que para aquellos que "
              "negaron hace tiempo parece que hay penitencia. Si alguno, "
              "pues, ha de arrepentirse, sea pronto, antes que la torre sea "
              "acabada; y si no, será destruido por las mujeres hasta la "
              "muerte.",
    (103, 7): "Y los mutilados, éstos son engañosos y maldicientes; y las "
              "fieras que viste en el monte, éstos son. Porque así como las "
              "fieras con su veneno destruyen al hombre y le pierden, así "
              "también las palabras de los hombres tales destruyen al hombre "
              "y le pierden.",
    (103, 8): "Éstos, pues, están mutilados en su fe por la conducta que "
              "tienen en sí mismos; mas algunos se arrepintieron y fueron "
              "salvos. Y los demás que son tales pueden ser salvos, si se "
              "arrepienten; mas si no se arrepienten, morirán a manos de "
              "aquellas mujeres cuya potencia tienen.",

    # Capítulo 104
    (104, 1): "Y los que creyeron del décimo monte, donde había árboles que "
              "cubrían a unas ovejas, son tales como éstos:",
    (104, 2): "obispos y hospitalarios, que siempre recibieron de buena gana "
              "en sus casas a los siervos de Dios sin hipocresía; y los "
              "obispos siempre, con su ministerio, cubrieron sin cesar a los "
              "necesitados y a las viudas, y se condujeron siempre con "
              "pureza.",
    (104, 3): "Éstos, pues, todos serán cubiertos por el Señor para siempre. "
              "Los que han obrado estas cosas, pues, son gloriosos delante de "
              "Dios, y ya su lugar es con los ángeles, si perseveran hasta el "
              "fin sirviendo al Señor.",

    # Capítulo 105
    (105, 1): "Y los que creyeron del undécimo monte, donde había árboles "
              "llenos de frutos, adornados cada uno de diversos frutos, son "
              "tales como éstos:",
    (105, 2): "los que padecieron por el nombre del Hijo de Dios, los cuales "
              "también padecieron con prontitud de todo su corazón, y "
              "entregaron sus vidas.",
    (105, 3): "¿Por qué, pues, señor, dije yo, todos los árboles tienen "
              "frutos, pero algunos frutos de ellos son más hermosos? Oye, "
              "dijo: cuantos alguna vez padecieron por el nombre son "
              "gloriosos delante de Dios, y los pecados de todos ellos fueron "
              "quitados, porque padecieron por el nombre del Hijo de Dios. "
              "Mas oye por qué sus frutos son diversos, y algunos "
              "sobresalientes.",
    (105, 4): "Cuantos, dijo, llevados ante la autoridad fueron interrogados "
              "y no negaron, sino que padecieron con prontitud, éstos son aún "
              "más gloriosos delante del Señor; de éstos es el fruto "
              "sobresaliente. Mas cuantos fueron cobardes y estuvieron en "
              "duda, y razonaron en sus corazones si negarían o confesarían, "
              "y padecieron, los frutos de éstos son menores, porque subió a "
              "su corazón este designio; porque malo es este designio, que un "
              "siervo niegue a su propio señor.",
    (105, 5): "Mirad, pues, vosotros los que tales cosas deliberáis, no sea "
              "que este designio permanezca en vuestros corazones y muráis "
              "para Dios. Mas vosotros los que padecéis por causa del nombre "
              "debéis glorificar a Dios, porque Dios os tuvo por dignos de "
              "llevar este nombre, y de que todos vuestros pecados sean "
              "sanados.",
    (105, 6): "Así que, teneos por bienaventurados; antes bien, pensad que "
              "habéis hecho una gran obra, si alguno de vosotros padece por "
              "causa de Dios. Vida os concede el Señor, y no lo entendéis; "
              "porque vuestros pecados os habían agobiado, y si no hubierais "
              "padecido por causa del nombre del Señor, por vuestros pecados "
              "habríais muerto para Dios.",
    (105, 7): "Esto os digo a vosotros los que dudáis entre negar o confesar: "
              "confesad que tenéis Señor, no sea que, negando, seáis "
              "entregados a la cárcel.",
    (105, 8): "Si los gentiles castigan a sus siervos, cuando alguno niega a "
              "su señor, ¿qué pensáis que os hará el Señor, que tiene la "
              "potestad sobre todas las cosas? Quitad estos designios de "
              "vuestros corazones, para que viváis para Dios para siempre.",

    # Capítulo 106
    (106, 1): "Y los que creyeron del duodécimo monte, el blanco, son tales "
              "como éstos: son como niños pequeños, a quienes ninguna malicia "
              "sube al corazón, ni conocieron qué es la maldad, sino que "
              "siempre permanecieron en la inocencia de niños.",
    (106, 2): "Los tales, pues, habitarán sin duda en el reino de Dios, "
              "porque en ninguna cosa mancillaron los mandamientos de Dios, "
              "sino que con inocencia de niños permanecieron todos los días "
              "de su vida en el mismo sentir.",
    (106, 3): "Cuantos, pues, permaneciereis, dijo, y fuereis como los niños, "
              "no teniendo malicia, seréis más gloriosos que todos los ya "
              "dichos; porque todos los niños son gloriosos delante de Dios, "
              "y los primeros junto a él. Bienaventurados, pues, vosotros, "
              "cuantos quitareis de vosotros la maldad y os vistiereis de la "
              "inocencia; los primeros de todos viviréis para Dios.",
    (106, 4): "Después que acabó las semejanzas de los montes, le digo: "
              "Señor, declárame ahora acerca de las piedras quitadas de la "
              "llanura y puestas en la edificación en lugar de las piedras "
              "quitadas de la torre, y de las redondas que fueron puestas en "
              "la edificación, y de las que todavía están redondas.",

    # Capítulo 107
    (107, 1): "Oye, dijo, también acerca de todas estas cosas. Las piedras "
              "quitadas de la llanura y puestas en la edificación de la torre "
              "en lugar de las desechadas son las raíces del monte blanco.",
    (107, 2): "Pues como los que creyeron del monte blanco fueron todos "
              "hallados inocentes, mandó el señor de la torre que éstos, de "
              "las raíces de este monte, fuesen puestos en la edificación de "
              "la torre; porque supo que, si estas piedras iban a la "
              "edificación de la torre, permanecerían resplandecientes y "
              "ninguna de ellas se ennegrecería.",
    (107, 3): "[Latín] Mas si hubiera añadido de los otros montes, habría "
              "tenido necesidad de visitar de nuevo esa torre y purificarla. "
              "Y todos éstos fueron hallados blancos, los que creyeron y los "
              "que han de creer; porque son del mismo linaje. Bienaventurado "
              "este linaje, porque es inocente.",
    (107, 4): "Oye ahora también acerca de las piedras redondas y "
              "resplandecientes. También éstas son todas del monte blanco. "
              "[Latín] Oye, pues, por qué fueron halladas redondas. Sus "
              "riquezas los oscurecieron un poco apartándolos de la verdad, y "
              "los ofuscaron; mas de Dios nunca se apartaron, ni salió de su "
              "boca palabra mala alguna, sino toda equidad y virtud de "
              "verdad.",
    (107, 5): "[Latín] Viendo, pues, el Señor el ánimo de éstos, que podían "
              "favorecer la verdad y permanecer también buenos, mandó que sus "
              "riquezas fuesen cortadas, mas no quitadas del todo, para que "
              "puedan hacer algún bien con lo que les ha quedado, y vivirán "
              "para Dios, porque son de buen linaje. Por esto, pues, fueron "
              "cortados un poco y fueron puestos en la edificación de esta "
              "torre.",

    # Capítulo 108
    (108, 1): "[Latín] Mas los demás, que permanecieron todavía redondos y no "
              "fueron ajustados en esa edificación, porque aún no han "
              "recibido el sello, fueron vueltos a poner en su lugar; porque "
              "fueron hallados muy redondos.",
    (108, 2): "[Latín] Es menester, pues, que se corte de ellos este siglo y "
              "las vanidades de sus riquezas, y entonces serán aptos para el "
              "reino de Dios. Porque es necesario que entren en el reino de "
              "Dios; pues a este linaje inocente lo bendijo el Señor. De este "
              "linaje, pues, no perecerá ninguno. Porque aunque alguno de "
              "ellos, tentado por el malvadísimo diablo, haya delinquido en "
              "algo, pronto volverá corriendo a su Señor.",
    (108, 3): "[Latín] Bienaventurados os juzgo a todos, yo, el ángel de la "
              "penitencia, cuantos sois inocentes como niños, porque vuestra "
              "parte es buena y honrada delante de Dios.",
    (108, 4): "[Latín] Y os digo a todos vosotros, cuantos habéis recibido "
              "este sello, que tengáis sencillez, y no guardéis memoria de "
              "las ofensas, ni permanezcáis en vuestra malicia o en la "
              "memoria de la amargura de las ofensas; que os hagáis cada uno "
              "de un solo espíritu, y que remediéis y quitéis de vosotros "
              "estas malas hendiduras, para que el Señor de los rebaños se "
              "goce en ellas.",
    (108, 5): "Y se regocijará si todas las halla sanas, y ninguna de ellas "
              "descarriada. Mas si halla alguna de ellas descarriada, ¡ay de "
              "los pastores!",
    (108, 6): "Y si los mismos pastores son hallados descarriados, ¿qué dirán "
              "al dueño del rebaño? ¿Que por las ovejas se descarriaron? No "
              "serán creídos; porque cosa increíble es que un pastor padezca "
              "algo por las ovejas; antes bien serán castigados por su "
              "mentira. [Latín] Y yo soy pastor, y es muy necesario que dé "
              "cuenta de vosotros.",

    # Capítulo 109
    (109, 1): "[Latín] Remediaos, pues, mientras la torre aún se edifica.",
    (109, 2): "[Latín] El Señor habita en los varones que aman la paz; porque "
              "a él en verdad la paz le es cara; mas de los contenciosos y de "
              "los perdidos en la malicia está lejos. Devolvedle, pues, el "
              "espíritu entero, así como lo recibisteis.",
    (109, 3): "[Latín] Porque si das al batanero un vestido nuevo, entero, y "
              "lo quieres recibir otra vez entero, y el batanero te lo "
              "devuelve roto, ¿lo recibirás? ¿No te encenderás al punto y le "
              "perseguirás con injurias, diciendo: Un vestido entero te di; "
              "¿por qué lo rompiste y lo dejaste inútil? Y por la rotura que "
              "en él hiciste no puede estar en uso. ¿No dirás, pues, todas "
              "estas palabras al batanero, aun acerca de la rotura que hizo "
              "en tu vestido?",
    (109, 4): "[Latín] Si así, pues, tú te dueles de tu vestido y te quejas "
              "porque no lo recibes entero, ¿qué piensas que te hará el "
              "Señor, que te dio el espíritu entero, y tú lo has dejado del "
              "todo inútil, de modo que en nada pueda servir a su Señor? "
              "Porque su uso comenzó a ser inútil, siendo corrompido por ti. "
              "¿No te castigará, pues, con la muerte el Señor de este "
              "espíritu por este hecho tuyo?",
    (109, 5): "[Latín] Ciertamente, dije yo, castigará a todos aquellos que "
              "halle permanecer en la memoria de las ofensas. No holléis, "
              "dijo, su clemencia, sino antes bien honradle, porque es tan "
              "paciente con vuestros delitos y no es como vosotros. Haced, "
              "pues, penitencia provechosa para vosotros.",

    # Capítulo 110
    (110, 1): "[Latín] Todas estas cosas que arriba están escritas, yo, el "
              "pastor, el ángel de la penitencia, las he mostrado y hablado a "
              "los siervos de Dios. Si, pues, creyereis y oyereis mis "
              "palabras, y anduviereis en ellas y enderezareis vuestros "
              "caminos, podréis vivir. Mas si permaneciereis en la malicia y "
              "en la memoria de las ofensas, ninguno de los tales vivirá para "
              "Dios. Todas estas cosas que yo había de deciros os han sido "
              "dichas.",
    (110, 2): "[Latín] Me dijo el mismo pastor: ¿Me lo has preguntado todo? Y "
              "dije: Sí, señor. ¿Por qué, pues, no me has preguntado acerca "
              "de las marcas de las piedras puestas en la edificación, por "
              "qué rellenamos las marcas? Y dije: Lo olvidé, señor.",
    (110, 3): "[Latín] Oye ahora, dijo, acerca de ellas. Éstos son los que "
              "ahora oyeron mis mandamientos e hicieron penitencia de todo "
              "corazón. Y viendo el Señor que su penitencia era buena y pura, "
              "y que podían permanecer en ella, mandó que sus pecados "
              "anteriores fuesen borrados. Porque estas marcas eran sus "
              "pecados, y fueron allanadas para que no aparecieran.",

    # Capítulo 111
    (111, 1): "[Latín] Después que hube escrito por completo este libro, vino "
              "aquel ángel que me había entregado a este pastor, a la casa en "
              "que yo estaba, y se sentó sobre el lecho, y este pastor se "
              "puso a su derecha. Luego me llamó y me dijo estas cosas:",
    (111, 2): "[Latín] Te he entregado, dijo, a ti y a tu casa a este pastor, "
              "para que puedas ser protegido por él. Así es, señor, dije yo. "
              "Si quieres, pues, dijo, ser protegido de toda vejación y de "
              "toda crueldad, y tener buen suceso en toda obra buena y "
              "palabra, y toda virtud de equidad, anda en los mandamientos de "
              "éste, que te he dado, y podrás enseñorearte de toda maldad.",
    (111, 3): "[Latín] Porque si guardas los mandamientos de éste, te estará "
              "sujeta toda codicia y dulzura de este siglo, y el buen suceso "
              "te seguirá en todo buen negocio. Recibe en ti la gravedad y la "
              "modestia de éste, y di a todos que él está en gran honra y "
              "dignidad delante del Señor, y que es presidente de gran "
              "potestad y poderoso en su oficio. A él solo en todo el orbe le "
              "ha sido dada la potestad de la penitencia. ¿Te parece que es "
              "poderoso? Mas vosotros despreciáis su gravedad y la modestia "
              "que tiene para con vosotros.",

    # Capítulo 112
    (112, 1): "[Latín] Le digo: Pregúntale a él mismo, señor, si desde que "
              "está en mi casa he hecho algo fuera de orden, con lo que le "
              "haya ofendido.",
    (112, 2): "[Latín] Y yo, dijo, sé que nada has hecho fuera de orden ni lo "
              "harás. Y por esto hablo contigo estas cosas, para que "
              "perseveres. Porque éste ha dado buen parecer de ti delante de "
              "mí. Y tú dirás a los demás estas palabras, para que también "
              "aquellos que han hecho o harán penitencia sientan lo mismo que "
              "tú, y éste hable bien de ellos delante de mí, y yo delante del "
              "Señor.",
    (112, 3): "[Latín] Y yo, dije, señor, anuncio a todo hombre las "
              "maravillas del Señor; y espero que todos los que antes "
              "pecaron, si oyen estas cosas, harán de buena gana penitencia, "
              "recobrando la vida.",
    (112, 4): "[Latín] Permanece, pues, dijo, en este ministerio y cúmplelo. "
              "Y cuantos cumplen los mandamientos de éste tendrán vida, y "
              "éste tendrá gran honra delante del Señor. Mas cuantos no "
              "guardan los mandamientos de éste, huyen de su propia vida y le "
              "son contrarios; ni siguen sus mandamientos, sino que se "
              "entregan a la muerte, y cada uno de ellos se hace reo de su "
              "propia sangre. Y a ti te digo que sirvas a estos mandamientos, "
              "y tendrás remedio de tus pecados.",

    # Capítulo 113
    (113, 1): "[Latín] Y te he enviado estas vírgenes para que habiten "
              "contigo; porque he visto que te son afables. Las tienes, pues, "
              "por ayudadoras, para que puedas guardar mejor los mandamientos "
              "de éste; porque no puede ser que sin estas vírgenes se guarden "
              "estos mandamientos. Y veo que están de buena gana contigo; mas "
              "yo les mandaré que en ninguna manera se aparten de tu casa.",
    (113, 2): "[Latín] Tú solamente limpia tu casa; porque en casa limpia "
              "habitarán de buena gana; porque son limpias y castas y "
              "diligentes, y todas tienen gracia delante del Señor. Por "
              "tanto, si hallan tu casa pura, permanecerán contigo. Mas si "
              "sobreviene un poco de impureza, al instante se apartarán de tu "
              "casa; porque estas vírgenes no aman en ninguna manera impureza "
              "alguna.",
    (113, 3): "[Latín] Le digo: Espero, señor, agradarles, de modo que "
              "habiten siempre de buena gana en mi casa. Y así como éste, a "
              "quien me entregaste, no se queja de mí, tampoco éstas se "
              "quejarán de mí.",
    (113, 4): "Dice al pastor: Sé que el siervo de Dios quiere vivir, y "
              "guardará estos mandamientos, y mantendrá a las vírgenes en "
              "pureza.",
    (113, 5): "Dicho esto al pastor, me entregó otra vez a él, y llamando a "
              "las vírgenes […] les dice: [Latín] Porque veo que habitáis de "
              "buena gana en la casa de éste, os lo encomiendo a él y a su "
              "casa, para que en ninguna manera os apartéis de su casa. Y "
              "ellas oyeron de buena gana estas palabras.",

    # Capítulo 114
    (114, 1): "[Latín] Me dijo luego: Condúcete varonilmente en este "
              "ministerio; anuncia a todo hombre las maravillas del Señor, y "
              "tendrás gracia en este ministerio. Cualquiera, pues, que "
              "anduviere en estos mandamientos vivirá y será dichoso en su "
              "vida; mas cualquiera que los descuidare no vivirá y será "
              "desdichado en su vida.",
    (114, 2): "[Latín] Di a todos que no cesen, cuantos pueden obrar "
              "rectamente; les es provechoso ejercitar buenas obras. Y digo "
              "que es menester librar a todo hombre de sus apuros. Porque el "
              "que está necesitado y padece apuros en la vida cotidiana está "
              "en gran tormento y necesidad.",
    (114, 3): "[Latín] El que libra, pues, de la necesidad a un alma tal, "
              "adquiere para sí gran gozo. Porque el que es afligido por "
              "semejante apuro es atormentado con igual tormento que el que "
              "está en cadenas, y se atormenta. Porque muchos, por semejantes "
              "calamidades, no pudiendo soportarlas, se dan muerte a sí "
              "mismos. El que conoce, pues, la calamidad de un hombre tal y "
              "no le libra, comete gran pecado y se hace reo de su sangre.",
    (114, 4): "[Latín] Haced, pues, buenas obras, cuantos habéis recibido del "
              "Señor, no sea que, mientras tardáis en hacerlas, se acabe la "
              "edificación de la torre. Porque por vosotros se ha "
              "interrumpido la obra de su edificación. Si no os apresuráis, "
              "pues, a obrar rectamente, se acabará la torre, y seréis "
              "excluidos.",
    (114, 5): "[Latín] Y después que habló conmigo, se levantó del lecho, y "
              "tomando al pastor y a las vírgenes se fue, diciéndome que me "
              "enviaría de nuevo aquel pastor y las vírgenes a mi casa.",
}
