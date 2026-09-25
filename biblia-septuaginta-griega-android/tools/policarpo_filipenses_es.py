"""Policarpo de Esmirna a los Filipenses, traducida del griego.

Policarpo, que según Ireneo había conocido al apóstol Juan, escribe a Filipos
poco después de pasar Ignacio por allí. La carta es casi un tejido de citas del
Nuevo Testamento, y es uno de los primeros testigos de que las cartas de Pablo
se leían ya como Escritura. Los capítulos 10 al 12 y el 14 se conservan sólo
en latín: la fuente los trae con letras griegas por un error de conversión, y
aquí se traducen del latín, marcados con [Latín] al principio.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

POLICARPO_FILIPENSES_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Policarpo y los presbíteros que están con él, a la iglesia de "
            "Dios que peregrina en Filipos: misericordia y paz os sean "
            "multiplicadas de parte de Dios todopoderoso y de Jesucristo "
            "nuestro Salvador.",
    (1, 1): "Me he regocijado grandemente con vosotros en nuestro Señor "
            "Jesucristo, porque recibisteis las imágenes del verdadero amor, "
            "y acompañasteis, como os correspondía, a los que iban ceñidos de "
            "cadenas dignas de santos, las cuales son diademas de los "
            "verdaderamente escogidos por Dios y por nuestro Señor;",
    (1, 2): "y porque la firme raíz de vuestra fe, anunciada desde tiempos "
            "antiguos, permanece hasta ahora y da fruto en nuestro Señor "
            "Jesucristo, el cual soportó llegar hasta la muerte por nuestros "
            "pecados, a quien Dios resucitó, sueltos los dolores del Hades;",
    (1, 3): "en quien, sin haberle visto, creéis con gozo inefable y "
            "glorificado, en el cual muchos desean entrar, sabiendo que por "
            "gracia sois salvos, no por obras, sino por la voluntad de Dios "
            "por medio de Jesucristo.",

    # Capítulo 2
    (2, 1): "Por tanto, ceñidos vuestros lomos, servid a Dios con temor y en "
            "verdad, dejando la vana palabrería y el error de muchos, "
            "creyendo en el que resucitó de los muertos a nuestro Señor "
            "Jesucristo y le dio gloria y trono a su diestra; a quien están "
            "sujetas todas las cosas celestiales y terrenales, a quien sirve "
            "todo lo que respira, el cual viene como juez de vivos y muertos, "
            "cuya sangre demandará Dios de los que le desobedecen.",
    (2, 2): "Y el que le resucitó de los muertos, también a nosotros nos "
            "resucitará, si hacemos su voluntad y andamos en sus mandamientos "
            "y amamos lo que él amó, apartándonos de toda injusticia, "
            "avaricia, amor al dinero, maledicencia, falso testimonio; no "
            "devolviendo mal por mal, ni injuria por injuria, ni golpe por "
            "golpe, ni maldición por maldición;",
    (2, 3): "sino acordándonos de lo que dijo el Señor enseñando: «No "
            "juzguéis, para que no seáis juzgados; perdonad, y se os "
            "perdonará; tened misericordia, para que alcancéis misericordia; "
            "con la medida con que medís, se os volverá a medir»; y: "
            "«Bienaventurados los pobres y los que padecen persecución por "
            "causa de la justicia, porque de ellos es el reino de Dios».",

    # Capítulo 3
    (3, 1): "Estas cosas, hermanos, os escribo acerca de la justicia, no por "
            "mi propia iniciativa, sino porque vosotros me invitasteis "
            "primero.",
    (3, 2): "Porque ni yo ni otro semejante a mí puede seguir de cerca la "
            "sabiduría del bienaventurado y glorioso Pablo, el cual, estando "
            "entre vosotros, en presencia de los hombres de entonces, enseñó "
            "con exactitud y firmeza la palabra de la verdad; y que también, "
            "estando ausente, os escribió cartas, en las cuales, si las "
            "escudriñáis, podréis ser edificados en la fe que os ha sido "
            "dada;",
    (3, 3): "la cual es madre de todos nosotros, siguiéndola la esperanza y "
            "precediéndola el amor para con Dios y Cristo y para con el "
            "prójimo. Porque si alguno está en estas cosas, ha cumplido el "
            "mandamiento de la justicia; pues el que tiene amor está lejos de "
            "todo pecado.",

    # Capítulo 4
    (4, 1): "Y el principio de todos los males es el amor al dinero. "
            "Sabiendo, pues, que nada trajimos al mundo, y que tampoco "
            "podemos sacar nada, armémonos con las armas de la justicia, y "
            "enseñémonos a nosotros mismos primero a andar en el mandamiento "
            "del Señor;",
    (4, 2): "y luego también a nuestras mujeres, a andar en la fe que les ha "
            "sido dada, y en el amor y la castidad, queriendo a sus propios "
            "maridos en toda verdad y amando a todos por igual con toda "
            "continencia, y a criar a los hijos en la disciplina del temor de "
            "Dios;",
    (4, 3): "a las viudas, a ser prudentes en cuanto a la fe del Señor, "
            "intercediendo sin cesar por todos, estando lejos de toda "
            "calumnia, maledicencia, falso testimonio, amor al dinero y todo "
            "mal, sabiendo que son altar de Dios, y que él examina todas las "
            "cosas en busca de defecto, y que nada se le oculta, ni de los "
            "razonamientos, ni de los pensamientos, ni de ninguno de los "
            "secretos del corazón.",

    # Capítulo 5
    (5, 1): "Sabiendo, pues, que Dios no puede ser burlado, debemos andar de "
            "una manera digna de su mandamiento y de su gloria.",
    (5, 2): "Asimismo, que los diáconos sean irreprensibles delante de su "
            "justicia, como diáconos de Dios y de Cristo, y no de hombres; no "
            "calumniadores, no de doble lengua, no amadores del dinero, "
            "continentes en todo, compasivos, diligentes, andando conforme a "
            "la verdad del Señor, que se hizo servidor de todos. Si le "
            "agradamos en el siglo presente, recibiremos también el venidero, "
            "según nos prometió resucitarnos de los muertos; y que, si nos "
            "conducimos como ciudadanos dignos de él, también reinaremos con "
            "él, si es que creemos.",
    (5, 3): "Asimismo, que también los jóvenes sean irreprensibles en todo, "
            "cuidando ante todo de la castidad y refrenándose de todo mal. "
            "Porque bueno es ser cortado de las concupiscencias que hay en el "
            "mundo, porque toda concupiscencia milita contra el espíritu, y "
            "ni los fornicarios, ni los afeminados, ni los que se echan con "
            "varones heredarán el reino de Dios, ni los que hacen cosas "
            "indebidas. Por lo cual es necesario apartarse de todas estas "
            "cosas, sometiéndose a los presbíteros y diáconos como a Dios y a "
            "Cristo. Y que las vírgenes anden en conciencia irreprensible y "
            "pura.",

    # Capítulo 6
    (6, 1): "Y que también los presbíteros sean compasivos, misericordiosos "
            "para con todos, haciendo volver a los extraviados, visitando a "
            "todos los enfermos, no descuidando a la viuda, ni al huérfano, "
            "ni al pobre, sino procurando siempre lo bueno delante de Dios y "
            "de los hombres, apartándose de toda ira, acepción de personas, "
            "juicio injusto, estando lejos de todo amor al dinero, no "
            "creyendo de prisa nada contra nadie, no siendo severos en el "
            "juicio, sabiendo que todos somos deudores de pecado.",
    (6, 2): "Si, pues, rogamos al Señor que nos perdone, también nosotros "
            "debemos perdonar; porque estamos delante de los ojos del Señor y "
            "Dios, y es necesario que todos comparezcan ante el tribunal de "
            "Cristo, y que cada uno dé cuenta de sí mismo.",
    (6, 3): "Así, pues, sirvámosle con temor y toda reverencia, como él mismo "
            "lo mandó, y los apóstoles que nos evangelizaron, y los profetas "
            "que anunciaron de antemano la venida de nuestro Señor; siendo "
            "celosos de lo bueno, apartándonos de los escándalos, y de los "
            "falsos hermanos, y de los que llevan con hipocresía el nombre "
            "del Señor, los cuales extravían a los hombres vanos.",

    # Capítulo 7
    (7, 1): "Porque todo aquel que no confiesa que Jesucristo ha venido en "
            "carne, es anticristo; y el que no confiesa el testimonio de la "
            "cruz, es del diablo; y el que tuerce los dichos del Señor según "
            "sus propias concupiscencias, y dice que no hay resurrección ni "
            "juicio, éste es el primogénito de Satanás.",
    (7, 2): "Por lo cual, dejando la vanidad de muchos y las falsas "
            "doctrinas, volvámonos a la palabra que nos fue entregada desde "
            "el principio, velando en oración y perseverando en ayunos, "
            "pidiendo con súplicas al Dios que todo lo ve que no nos meta en "
            "tentación, según dijo el Señor: «El espíritu a la verdad está "
            "presto, mas la carne enferma».",

    # Capítulo 8
    (8, 1): "Perseveremos, pues, sin cesar en nuestra esperanza y en las "
            "arras de nuestra justicia, que es Cristo Jesús, el cual llevó "
            "nuestros pecados en su propio cuerpo sobre el madero, el cual no "
            "hizo pecado, ni fue hallado engaño en su boca; sino que por "
            "nosotros, para que vivamos en él, lo soportó todo.",
    (8, 2): "Seamos, pues, imitadores de su paciencia; y si padecemos por su "
            "nombre, glorifiquémosle. Porque este ejemplo nos dio en sí "
            "mismo, y nosotros lo hemos creído.",

    # Capítulo 9
    (9, 1): "Os exhorto, pues, a todos a obedecer la palabra de la justicia y "
            "a ejercitar toda paciencia, la cual visteis con vuestros propios "
            "ojos, no sólo en los bienaventurados Ignacio, y Zósimo, y Rufo, "
            "sino también en otros de entre vosotros, y en el mismo Pablo y "
            "en los demás apóstoles;",
    (9, 2): "persuadidos de que todos éstos no corrieron en vano, sino en fe "
            "y en justicia, y de que están en el lugar que les es debido "
            "junto al Señor, con quien también padecieron. Porque no amaron "
            "el siglo presente, sino a aquel que murió por nosotros y que por "
            "nosotros fue resucitado por Dios.",

    # Capítulo 10
    (10, 1): "[Latín] Permaneced, pues, en estas cosas, y seguid el ejemplo "
             "del Señor, firmes en la fe e inmutables, amadores de la "
             "fraternidad, amándoos unos a otros, unidos en la verdad, "
             "anticipándoos unos a otros en la mansedumbre del Señor, no "
             "despreciando a nadie.",
    (10, 2): "[Latín] Cuando podáis hacer bien, no lo difiráis, porque la "
             "limosna libra de la muerte. Estad todos sujetos unos a otros, "
             "teniendo vuestra manera de vivir irreprensible entre los "
             "gentiles, para que por vuestras buenas obras vosotros recibáis "
             "alabanza y el Señor no sea blasfemado en vosotros.",
    (10, 3): "[Latín] Mas ¡ay de aquel por quien es blasfemado el nombre del "
             "Señor! Enseñad, pues, a todos la sobriedad, en la cual también "
             "vosotros vivís.",

    # Capítulo 11
    (11, 1): "[Latín] Mucho me he entristecido por Valente, que en otro "
             "tiempo fue hecho presbítero entre vosotros, porque así "
             "desconoce el cargo que le fue dado. Os amonesto, pues, que os "
             "abstengáis de la avaricia, y que seáis castos y veraces. "
             "Absteneos de todo mal.",
    (11, 2): "[Latín] Porque el que no puede gobernarse a sí mismo en estas "
             "cosas, ¿cómo lo predicará a otro? Si alguno no se abstiene de "
             "la avaricia, será contaminado por la idolatría, y será juzgado "
             "como uno de los gentiles, que ignoran el juicio del Señor. ¿O "
             "no sabemos que los santos han de juzgar al mundo?, como enseña "
             "Pablo.",
    (11, 3): "[Latín] Mas yo no he percibido ni oído nada semejante en "
             "vosotros, entre los cuales trabajó el bienaventurado Pablo, que "
             "estáis en el principio de su carta. Porque de vosotros se "
             "gloría en todas las iglesias, las únicas que entonces conocían "
             "al Señor; pues nosotros aún no le habíamos conocido.",
    (11, 4): "[Latín] Mucho, pues, hermanos, me entristezco por él y por su "
             "mujer; el Señor les dé verdadero arrepentimiento. Sed, pues, "
             "también vosotros sobrios en esto; y no tengáis a los tales por "
             "enemigos, sino llamadlos de nuevo como a miembros dolientes y "
             "extraviados, para que salvéis el cuerpo de todos vosotros. "
             "Porque haciendo esto os edificáis a vosotros mismos.",

    # Capítulo 12
    (12, 1): "[Latín] Porque confío en que estáis bien ejercitados en las "
             "sagradas letras, y nada se os oculta; mas a mí no me ha sido "
             "concedido. Sólo digo, como está dicho en estas Escrituras: "
             "«Airaos, y no pequéis», y: «No se ponga el sol sobre vuestro "
             "enojo». Bienaventurado el que se acuerde de ello, lo cual creo "
             "que está en vosotros.",
    (12, 2): "[Latín] Y el Dios y Padre de nuestro Señor Jesucristo, y él "
             "mismo, el sumo sacerdote eterno, el Hijo de Dios, Jesucristo, "
             "os edifique en la fe y en la verdad, y en toda mansedumbre, y "
             "sin ira, y en paciencia, y en longanimidad, y tolerancia, y "
             "castidad; y os dé suerte y parte entre sus santos, y a nosotros "
             "con vosotros, y a todos los que están debajo del cielo, que han "
             "de creer en nuestro Señor y Dios Jesucristo y en su Padre, que "
             "le resucitó de los muertos.",
    (12, 3): "[Latín] Orad por todos los santos. Orad también por los reyes, "
             "y por las potestades, y por los príncipes, y por los que os "
             "persiguen y os aborrecen, y por los enemigos de la cruz, para "
             "que vuestro fruto sea manifiesto en todos, para que seáis "
             "perfectos en él.",

    # Capítulo 13
    (13, 1): "Me escribisteis, tanto vosotros como Ignacio, que si alguno va "
             "a Siria, lleve también vuestras cartas; lo cual haré si hallo "
             "ocasión oportuna, sea yo mismo, sea uno a quien envíe como "
             "embajador también de vuestra parte.",
    (13, 2): "Las cartas de Ignacio que él nos envió, y otras que teníamos en "
             "nuestro poder, os las hemos enviado, como mandasteis; las "
             "cuales van adjuntas a esta carta, y de ellas podréis sacar gran "
             "provecho. Porque contienen fe, y paciencia, y toda edificación "
             "que concierne a nuestro Señor. [Latín] Y lo que sepáis con más "
             "certeza del mismo Ignacio y de los que están con él, hacédnoslo "
             "saber.",

    # Capítulo 14
    (14, 1): "[Latín] Os he escrito estas cosas por medio de Crescente, a "
             "quien os recomendé hace poco y ahora os recomiendo. Porque se "
             "ha conducido entre nosotros sin reproche; y creo que también "
             "entre vosotros del mismo modo. Y tendréis también por "
             "recomendada a su hermana cuando llegue a vosotros. Estad sanos "
             "y salvos en el Señor Jesucristo, en gracia, con todos los "
             "vuestros. Amén.",
}
