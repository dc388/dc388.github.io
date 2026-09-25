"""A Diogneto, traducido del griego.

Una apología dirigida a un pagano culto, de autor desconocido y fecha incierta
—quizá finales del siglo II—, que sobrevivió en un solo manuscrito, destruido
en 1870. Los capítulos 5 y 6 dicen lo que son los cristianos en el mundo: «lo
que el alma es en el cuerpo, eso son los cristianos en el mundo». Los dos
últimos capítulos parecen de otra mano.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

DIOGNETO_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "Puesto que veo, excelentísimo Diogneto, que pones grandísimo "
            "empeño en aprender la religión de los cristianos, y que muy "
            "clara y cuidadosamente preguntas acerca de ellos: en qué Dios "
            "confían y cómo le rinden culto, de modo que todos desprecian el "
            "mundo y tienen en poco la muerte, y ni tienen por dioses a los "
            "que los griegos reputan tales, ni guardan la superstición de los "
            "judíos; y qué amor entrañable se tienen unos a otros; y por qué, "
            "en fin, esta nueva raza o modo de vida ha entrado en el mundo "
            "ahora y no antes: acepto de buen grado este tu celo, y a Dios, "
            "que nos concede así el hablar como el oír, le pido que a mí me "
            "sea dado hablar de tal manera que, oyéndome, llegues a ser "
            "mejor, y a ti oír de tal manera que no se entristezca el que "
            "habló.",

    # Capítulo 2
    (2, 1): "¡Ea, pues! Limpiándote de todos los razonamientos que de "
            "antemano ocupan tu entendimiento, y desechando la costumbre que "
            "te engaña, y haciéndote como desde el principio un hombre nuevo, "
            "como quien ha de ser oyente de una palabra también nueva, según "
            "tú mismo confesaste: mira no sólo con los ojos, sino también con "
            "la inteligencia, de qué sustancia o de qué forma son esos que "
            "llamáis y tenéis por dioses.",
    (2, 2): "¿No es uno de ellos piedra, semejante a la que se pisa; otro "
            "bronce, no mejor que los utensilios forjados para nuestro uso; "
            "otro madera, ya incluso podrida; otro plata, que necesita de un "
            "hombre que la guarde para que no la roben; otro hierro, corroído "
            "por el orín; otro barro cocido, en nada más hermoso que el que "
            "se fabrica para el más vil servicio?",
    (2, 3): "¿No son todos ellos de materia corruptible? ¿No están forjados "
            "con hierro y fuego? ¿No los modeló a uno el cantero, a otro el "
            "broncista, a otro el platero, a otro el alfarero? ¿No era cada "
            "uno de ellos, antes de ser moldeado por las artes de éstos en la "
            "forma que tienen, y aun ahora, capaz de ser transformado en "
            "cualquier otra cosa? ¿No podrían los utensilios que ahora son de "
            "la misma materia, si dieran con los mismos artífices, volverse "
            "semejantes a éstos?",
    (2, 4): "¿No podrían a su vez éstos, que ahora adoráis vosotros, ser "
            "hechos por los hombres utensilios semejantes a los demás? ¿No "
            "son todos sordos? ¿No son ciegos? ¿No son sin alma? ¿No son "
            "insensibles? ¿No son inmóviles? ¿No se pudren todos? ¿No se "
            "corrompen todos?",
    (2, 5): "¿A esto llamáis dioses? ¿A esto servís? A esto adoráis, y al fin "
            "os hacéis semejantes a ello.",
    (2, 6): "¿Por eso aborrecéis a los cristianos, porque no tienen a éstos "
            "por dioses?",
    (2, 7): "Porque vosotros, que pensáis y creéis alabarlos, ¿no los "
            "despreciáis mucho más? ¿No os burláis de ellos y los ultrajáis "
            "mucho más, cuando a los de piedra y barro los veneráis sin "
            "guardarlos, y a los de plata y oro los encerráis de noche y de "
            "día les ponéis guardias, para que no los roben?",
    (2, 8): "Y con los honores que pensáis ofrecerles, si sienten, más bien "
            "los castigáis; y si no sienten, les dais culto con sangre y "
            "grasa quemada, poniéndolos en evidencia.",
    (2, 9): "Que alguno de vosotros sufra esto, que alguno consienta que se "
            "le haga esto a sí mismo. Pero ni un solo hombre soportará de "
            "buen grado este castigo, porque tiene sentido y razón; la "
            "piedra, en cambio, lo soporta, porque no siente. ¿No ponéis, "
            "pues, en evidencia su insensibilidad?",
    (2, 10): "Acerca, pues, de que los cristianos no sean esclavos de tales "
             "dioses, muchas otras cosas podría decir; mas si a alguno no le "
             "parecieran suficientes aun éstas, tengo por superfluo decir "
             "más.",

    # Capítulo 3
    (3, 1): "A continuación pienso que deseas sobre todo oír por qué no dan "
            "culto a Dios de la misma manera que los judíos.",
    (3, 2): "Los judíos, pues, en cuanto se apartan de este culto antes "
            "dicho, hacen bien en venerar a un solo Dios de todas las cosas y "
            "en tenerle por Señor; pero en cuanto le ofrecen este culto de "
            "manera semejante a los antes dichos, yerran por completo.",
    (3, 3): "Porque lo que los griegos, ofreciéndolo a cosas insensibles y "
            "sordas, dan como muestra de insensatez, eso mismo éstos, "
            "pensando ofrecerlo a Dios como si Él tuviera necesidad, con "
            "razón habrían de tenerlo más bien por necedad que por religión.",
    (3, 4): "Porque el que hizo el cielo y la tierra y todo lo que en ellos "
            "hay, y a todos nosotros nos provee de lo que necesitamos, no "
            "podría Él mismo necesitar ninguna de estas cosas que Él mismo "
            "proporciona a los que piensan dárselas.",
    (3, 5): "Y los que piensan ofrecerle sacrificios con sangre y grasa "
            "quemada y holocaustos, y honrarle con estos honores, en nada me "
            "parece que se diferencian de los que muestran la misma solicitud "
            "para con las cosas sordas: los unos, ofreciendo a quienes no "
            "pueden participar del honor; los otros, pensando ofrecerlo al "
            "que de nada tiene necesidad.",

    # Capítulo 4
    (4, 1): "Pero en cuanto a su escrupuloso temor acerca de las comidas, y a "
            "su superstición sobre los sábados, y a su jactancia de la "
            "circuncisión, y a su fingimiento acerca del ayuno y la luna "
            "nueva, cosas ridículas e indignas de toda palabra, no creo que "
            "tengas necesidad de aprenderlas de mí.",
    (4, 2): "Porque de las cosas creadas por Dios para uso de los hombres, "
            "recibir unas como bien creadas y rechazar otras como inútiles y "
            "superfluas, ¿cómo no ha de ser impío?",
    (4, 3): "Y calumniar a Dios como si prohibiera hacer algo bueno en el día "
            "de los sábados, ¿cómo no ha de ser irreligioso?",
    (4, 4): "Y jactarse también de la mutilación de la carne como testimonio "
            "de elección, como si por esto fueran amados de Dios de manera "
            "singular, ¿cómo no ha de ser digno de burla?",
    (4, 5): "Y que, acechando a los astros y a la luna, hagan la observancia "
            "de los meses y de los días, y repartan las disposiciones de Dios "
            "y los cambios de las estaciones según sus propios impulsos, unas "
            "para fiestas y otras para duelos: ¿quién tendría esto por "
            "muestra de religión, y no mucho más de insensatez?",
    (4, 6): "Que los cristianos, pues, se apartan con razón de la común "
            "vanidad y engaño, y de la curiosidad y jactancia de los judíos, "
            "pienso que lo has aprendido suficientemente; pero el misterio de "
            "su propia religión no esperes poder aprenderlo de hombre alguno.",

    # Capítulo 5
    (5, 1): "Porque los cristianos no se distinguen de los demás hombres ni "
            "por la tierra, ni por la lengua, ni por las costumbres.",
    (5, 2): "Porque ni habitan en ciudades propias, ni usan de alguna lengua "
            "extraña, ni llevan un género de vida singular.",
    (5, 3): "Esta doctrina suya no ha sido hallada por algún pensamiento o "
            "cavilación de hombres curiosos, ni son, como algunos, defensores "
            "de una doctrina humana.",
    (5, 4): "Sino que, habitando ciudades griegas y bárbaras, según a cada "
            "uno le cupo en suerte, y siguiendo las costumbres del país en el "
            "vestido, en la comida y en el resto de la vida, muestran un modo "
            "de vivir admirable y, según confiesan todos, extraño.",
    (5, 5): "Habitan sus propias patrias, pero como forasteros; participan en "
            "todo como ciudadanos, y todo lo soportan como extranjeros; toda "
            "tierra extraña es patria para ellos, y toda patria, tierra "
            "extraña.",
    (5, 6): "Se casan como todos, engendran hijos; pero no desechan a los que "
            "nacen.",
    (5, 7): "Ponen mesa común, pero no lecho común.",
    (5, 8): "Están en la carne, pero no viven según la carne.",
    (5, 9): "Pasan su vida en la tierra, pero son ciudadanos del cielo.",
    (5, 10): "Obedecen las leyes establecidas, y con su propia vida "
             "sobrepujan las leyes.",
    (5, 11): "Aman a todos, y por todos son perseguidos.",
    (5, 12): "Se los desconoce, y se los condena; se los mata, y reciben la "
             "vida.",
    (5, 13): "Son pobres, y enriquecen a muchos; carecen de todo, y en todo "
             "abundan.",
    (5, 14): "Son deshonrados, y en las deshonras son glorificados. Se los "
             "calumnia, y son justificados.",
    (5, 15): "Se los insulta, y bendicen; se los ultraja, y honran.",
    (5, 16): "Haciendo el bien, son castigados como malhechores; castigados, "
             "se gozan como quienes reciben la vida.",
    (5, 17): "Los judíos les hacen guerra como a extranjeros, y los griegos "
             "los persiguen; y los que los aborrecen no saben decir la causa "
             "de su enemistad.",

    # Capítulo 6
    (6, 1): "Para decirlo en una palabra: lo que el alma es en el cuerpo, eso "
            "son los cristianos en el mundo.",
    (6, 2): "El alma está esparcida por todos los miembros del cuerpo, y los "
            "cristianos por las ciudades del mundo.",
    (6, 3): "El alma habita en el cuerpo, pero no es del cuerpo; y los "
            "cristianos habitan en el mundo, pero no son del mundo.",
    (6, 4): "El alma invisible está guardada en el cuerpo visible; y los "
            "cristianos son conocidos como que están en el mundo, pero su "
            "religión permanece invisible.",
    (6, 5): "La carne aborrece al alma y le hace guerra, sin haber recibido "
            "de ella agravio alguno, porque le impide gozar de los placeres; "
            "también el mundo aborrece a los cristianos, sin haber recibido "
            "de ellos agravio alguno, porque se oponen a los placeres.",
    (6, 6): "El alma ama a la carne que la aborrece, y a los miembros; y los "
            "cristianos aman a los que los aborrecen.",
    (6, 7): "El alma está encerrada en el cuerpo, pero ella es la que "
            "mantiene unido al cuerpo; y los cristianos están detenidos en el "
            "mundo como en una cárcel, pero ellos son los que mantienen unido "
            "al mundo.",
    (6, 8): "El alma inmortal habita en una tienda mortal; y los cristianos "
            "habitan como forasteros en lo corruptible, esperando la "
            "incorrupción en los cielos.",
    (6, 9): "El alma, maltratada en comidas y bebidas, se hace mejor; y los "
            "cristianos, castigados, se multiplican más cada día.",
    (6, 10): "En tan alto puesto los colocó Dios, que no les es lícito "
             "desertar de él.",

    # Capítulo 7
    (7, 1): "Porque no es un hallazgo terreno, como dije, el que les fue "
            "entregado, ni es un pensamiento mortal el que estiman digno de "
            "guardar con tanto cuidado, ni se les ha confiado la "
            "administración de misterios humanos.",
    (7, 2): "Sino que el mismo Dios, verdaderamente todopoderoso, creador de "
            "todo e invisible, Él mismo desde los cielos estableció entre los "
            "hombres la verdad y la Palabra santa e incomprensible, y la "
            "asentó firmemente en sus corazones; no, como alguno podría "
            "imaginar, enviando a los hombres algún servidor, o un ángel, o "
            "un príncipe, o alguno de los que gobiernan las cosas terrenas, o "
            "alguno de aquellos a quienes están confiadas las "
            "administraciones en los cielos, sino al mismo Artífice y Hacedor "
            "del universo, por quien creó los cielos, por quien encerró el "
            "mar en sus propios límites, cuyos misterios guardan fielmente "
            "todos los elementos, de quien el sol recibió las medidas de sus "
            "carreras diarias para guardarlas, a quien obedece la luna cuando "
            "le manda brillar de noche, a quien obedecen las estrellas que "
            "siguen la carrera de la luna; por quien todo ha sido ordenado, y "
            "delimitado, y sometido: los cielos y lo que hay en los cielos, "
            "la tierra y lo que hay en la tierra, el mar y lo que hay en el "
            "mar, el fuego, el aire, el abismo, lo que está en las alturas, "
            "lo que está en las profundidades, lo que está en medio: a éste "
            "les envió.",
    (7, 3): "¿Acaso, como podría pensar alguno de los hombres, para tiranía, "
            "y temor, y espanto?",
    (7, 4): "De ninguna manera; sino que en mansedumbre y dulzura, como un "
            "rey que envía a su hijo rey, lo envió; como Dios lo envió; como "
            "hombre a los hombres lo envió; como quien salva lo envió, como "
            "quien persuade, no como quien fuerza: porque la violencia no es "
            "propia de Dios.",
    (7, 5): "Lo envió como quien llama, no como quien persigue; lo envió como "
            "quien ama, no como quien juzga.",
    (7, 6): "Porque lo enviará como juez; ¿y quién resistirá su venida? […]",
    (7, 7): "[…] ¿arrojados a las fieras para que nieguen al Señor, y no "
            "vencidos?",
    (7, 8): "¿No ves que, cuantos más son castigados, tanto más se "
            "multiplican los otros?",
    (7, 9): "Estas cosas no parecen obras de hombre; esto es poder de Dios; "
            "éstas son pruebas de su presencia.",

    # Capítulo 8
    (8, 1): "Porque ¿quién de los hombres sabía en absoluto qué es Dios, "
            "antes que Él viniese?",
    (8, 2): "¿O aceptas los discursos vanos y disparatados de aquellos "
            "filósofos dignos de crédito, de los cuales unos dijeron que Dios "
            "era fuego (aquello a donde ellos mismos han de ir, a eso llaman "
            "Dios), otros agua, otros algún otro de los elementos creados por "
            "Dios?",
    (8, 3): "Y ciertamente, si alguno de estos discursos es aceptable, "
            "también podría cada una de las demás criaturas ser declarada "
            "Dios de igual modo.",
    (8, 4): "Pero estas cosas son patrañas y engaño de embaucadores.",
    (8, 5): "Y ningún hombre le vio ni le dio a conocer, sino que Él mismo se "
            "manifestó a sí mismo.",
    (8, 6): "Y se manifestó por medio de la fe, a la cual sola le es "
            "concedido ver a Dios.",
    (8, 7): "Porque Dios, el Señor y Hacedor del universo, el que hizo todas "
            "las cosas y las dispuso en orden, no sólo fue amigo de los "
            "hombres, sino también longánimo.",
    (8, 8): "Sino que Él siempre fue tal, y lo es, y lo será: benigno, y "
            "bueno, y sin ira, y verdadero; y sólo Él es bueno.",
    (8, 9): "Y habiendo concebido un designio grande e inefable, lo comunicó "
            "sólo a su Hijo.",
    (8, 10): "Así pues, mientras mantenía en misterio y guardaba su sabio "
             "consejo, parecía que se desentendía de nosotros y no se "
             "cuidaba;",
    (8, 11): "mas cuando lo reveló por medio de su amado Hijo y manifestó lo "
             "que desde el principio estaba preparado, nos lo otorgó todo a "
             "la vez: participar de sus beneficios, y ver, y entender. ¿Quién "
             "de nosotros jamás lo hubiera esperado?",

    # Capítulo 9
    (9, 1): "Habiéndolo, pues, dispuesto ya todo en sí mismo con su Hijo, "
            "hasta el tiempo pasado nos dejó que fuésemos arrastrados, como "
            "queríamos, por impulsos desordenados, llevados por placeres y "
            "concupiscencias; no porque en modo alguno se complaciera en "
            "nuestros pecados, sino porque los soportaba; no porque aprobara "
            "aquel tiempo de la injusticia, sino porque estaba creando el "
            "tiempo presente de la justicia, para que, convictos en aquel "
            "tiempo por nuestras propias obras de ser indignos de la vida, "
            "ahora fuésemos hechos dignos por la bondad de Dios; y habiendo "
            "mostrado que por nosotros mismos éramos incapaces de entrar en "
            "el reino de Dios, fuésemos hechos capaces por el poder de Dios.",
    (9, 2): "Y cuando nuestra injusticia se hubo colmado y se hubo "
            "manifestado del todo que su paga, el castigo y la muerte, era lo "
            "que se esperaba, y llegó el tiempo que Dios había determinado "
            "para manifestar en adelante su bondad y su poder (¡oh "
            "sobreabundante amor a los hombres y caridad de Dios!), no nos "
            "aborreció, ni nos rechazó, ni guardó rencor, sino que fue "
            "longánimo, nos soportó; compadecido, Él mismo tomó sobre sí "
            "nuestros pecados; Él mismo entregó a su propio Hijo como rescate "
            "por nosotros: al santo por los inicuos, al inocente por los "
            "malos, al justo por los injustos, al incorruptible por los "
            "corruptibles, al inmortal por los mortales.",
    (9, 3): "Porque ¿qué otra cosa pudo cubrir nuestros pecados sino la "
            "justicia de Aquél?",
    (9, 4): "¿En quién era posible que fuésemos justificados nosotros, los "
            "inicuos e impíos, sino sólo en el Hijo de Dios?",
    (9, 5): "¡Oh dulce intercambio! ¡Oh obra inescrutable! ¡Oh beneficios "
            "inesperados! Que la iniquidad de muchos quedara escondida en un "
            "solo justo, y la justicia de uno solo justificara a muchos "
            "inicuos.",
    (9, 6): "Habiendo, pues, puesto en evidencia en el tiempo pasado la "
            "impotencia de nuestra naturaleza para alcanzar la vida, y "
            "habiéndonos mostrado ahora al Salvador, poderoso para salvar aun "
            "lo que es imposible, por ambas cosas quiso que creyésemos en su "
            "bondad, que le tuviésemos por sustentador, padre, maestro, "
            "consejero, médico, mente, luz, honra, gloria, fuerza, vida, y "
            "que no nos afanásemos por el vestido y el alimento.",

    # Capítulo 10
    (10, 1): "Si también tú deseas esta fe, y recibes primero el conocimiento "
             "del Padre […]",
    (10, 2): "Porque Dios amó a los hombres, por causa de los cuales hizo el "
             "mundo; a los cuales sometió todo lo que hay en la tierra; a los "
             "cuales dio la razón, a los cuales la mente; a los cuales solos "
             "permitió mirar hacia arriba, a Él; a los cuales formó de su "
             "propia imagen; a los cuales envió a su Hijo unigénito; a los "
             "cuales prometió el reino que está en el cielo, y lo dará a los "
             "que le hayan amado.",
    (10, 3): "Y habiéndole conocido, ¿de qué gozo piensas que serás lleno? ¿O "
             "cómo amarás a quien de tal manera te amó primero?",
    (10, 4): "Y amándole, serás imitador de su bondad. Y no te maravilles de "
             "que un hombre pueda llegar a ser imitador de Dios: puede, si Él "
             "lo quiere.",
    (10, 5): "Porque la felicidad no está en tiranizar al prójimo, ni en "
             "querer tener más que los más débiles, ni en enriquecerse y "
             "hacer violencia a los inferiores; ni en estas cosas puede nadie "
             "imitar a Dios, sino que estas cosas son ajenas a su majestad.",
    (10, 6): "Sino que quien toma sobre sí la carga de su prójimo, quien en "
             "aquello en que es superior quiere hacer bien a otro que está "
             "más necesitado, quien, dando a los que lo necesitan lo que ha "
             "recibido de Dios, se hace dios de los que lo reciben, éste es "
             "imitador de Dios.",
    (10, 7): "Entonces, estando en la tierra, contemplarás que Dios reina en "
             "los cielos; entonces comenzarás a hablar los misterios de Dios; "
             "entonces amarás y admirarás a los que son castigados por no "
             "querer negar a Dios; entonces condenarás el engaño y el "
             "extravío del mundo, cuando conozcas el verdadero vivir en el "
             "cielo, cuando desprecies la que aquí parece muerte, cuando "
             "temas la muerte verdadera, que está reservada a los que serán "
             "condenados al fuego eterno, el cual castigará hasta el fin a "
             "los que le fueren entregados.",
    (10, 8): "Entonces admirarás a los que soportan por la justicia el fuego "
             "temporal, y los llamarás bienaventurados, cuando conozcas aquel "
             "fuego.",

    # Capítulo 11
    (11, 1): "No hablo de cosas extrañas ni busco lo que es contra razón, "
             "sino que, habiendo sido discípulo de los apóstoles, me hago "
             "maestro de los gentiles; lo que me ha sido entregado lo "
             "administro dignamente a los que se hacen discípulos de la "
             "verdad.",
    (11, 2): "Porque ¿quién, rectamente enseñado y hecho amigo de la Palabra, "
             "no busca aprender claramente lo que por la Palabra fue mostrado "
             "abiertamente a los discípulos, a los cuales la Palabra, al "
             "aparecer, se lo manifestó, hablando con libertad, no entendida "
             "por los incrédulos, pero declarándolo a los discípulos, los "
             "cuales, tenidos por fieles por ella, conocieron los misterios "
             "del Padre?",
    (11, 3): "Por eso envió a la Palabra, para que se manifestase al mundo; "
             "la cual, deshonrada por el pueblo, predicada por los apóstoles, "
             "fue creída por los gentiles.",
    (11, 4): "Éste es el que era desde el principio, el que apareció nuevo y "
             "fue hallado antiguo, y que siempre nace nuevo en los corazones "
             "de los santos.",
    (11, 5): "Éste es el eterno, el que hoy es tenido por Hijo, por el cual "
             "la iglesia es enriquecida, y la gracia, desplegándose, se "
             "multiplica en los santos, dando entendimiento, manifestando "
             "misterios, anunciando los tiempos, gozándose en los fieles, "
             "dándose a los que la buscan, a aquellos por quienes no se "
             "quebrantan los juramentos de la fe ni se traspasan los linderos "
             "de los padres.",
    (11, 6): "Luego se canta el temor de la ley, y se conoce la gracia de los "
             "profetas, y se asienta la fe de los evangelios, y se guarda la "
             "tradición de los apóstoles, y salta de gozo la gracia de la "
             "iglesia.",
    (11, 7): "Si no contristas esta gracia, conocerás lo que la Palabra habla "
             "por medio de quienes quiere, cuando quiere.",
    (11, 8): "Porque de todo cuanto, por la voluntad de la Palabra que lo "
             "manda, fuimos movidos a declarar con trabajo, por amor de lo "
             "que nos ha sido revelado, nos hacemos partícipes con vosotros.",

    # Capítulo 12
    (12, 1): "Leyendo y oyendo con diligencia estas cosas, sabréis cuánto "
             "otorga Dios a los que le aman rectamente, los cuales se hacen "
             "un paraíso de delicias, haciendo brotar en sí mismos un árbol "
             "lozano y cargado de toda clase de frutos, adornados de frutos "
             "variados.",
    (12, 2): "Porque en este lugar fueron plantados el árbol del conocimiento "
             "y el árbol de la vida; pero no es el del conocimiento el que "
             "mata, sino que la desobediencia es la que mata.",
    (12, 3): "Porque no carece de significado lo que está escrito: que Dios "
             "desde el principio plantó el árbol del conocimiento y el árbol "
             "de la vida en medio del paraíso, mostrando la vida por medio "
             "del conocimiento; del cual, por no haber usado con pureza, los "
             "del principio quedaron desnudos por el engaño de la serpiente.",
    (12, 4): "Porque ni hay vida sin conocimiento, ni conocimiento seguro sin "
             "vida verdadera; por eso ambos fueron plantados uno junto al "
             "otro.",
    (12, 5): "Viendo el apóstol esta fuerza, y reprendiendo el conocimiento "
             "que se ejercita para la vida sin el precepto de la verdad, "
             "dice: La ciencia envanece, mas la caridad edifica.",
    (12, 6): "Porque el que piensa saber algo sin el conocimiento verdadero y "
             "atestiguado por la vida, no ha conocido; es engañado por la "
             "serpiente, porque no amó el vivir. Mas el que con temor ha "
             "conocido y busca la vida, planta en esperanza, aguardando el "
             "fruto.",
    (12, 7): "Sea para ti el corazón conocimiento, y la vida, la palabra "
             "verdadera, recibida dentro de ti.",
    (12, 8): "Llevando su árbol y cogiendo su fruto, cosecharás siempre lo "
             "que es deseable delante de Dios, lo cual la serpiente no toca "
             "ni el engaño contamina; ni Eva es corrompida, sino que una "
             "virgen es creída;",
    (12, 9): "y la salvación se muestra, y los apóstoles reciben "
             "entendimiento, y la Pascua del Señor avanza, y los tiempos se "
             "reúnen y se armonizan con el mundo, y la Palabra se goza "
             "enseñando a los santos, por la cual el Padre es glorificado: a "
             "Él sea la gloria por los siglos. Amén.",
}
