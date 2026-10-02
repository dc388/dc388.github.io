"""Enoc en español, traducido del griego del Códice Panopolitano.

Enoc estaba aquí solo en griego, y un libro que no se puede leer no sirve para
estudiarlo: quien abre Enoc 2 y encuentra una columna de griego sin más se
queda igual que antes. Y no es un libro cualquiera para el lector evangélico:
Judas 14-15 cita Enoc 1:9 casi palabra por palabra, así que es el pseudoepígrafo
que de verdad hace falta poder leer.

No hay traducción española libre que copiar. Las cuatro Biblias en dominio
público que existen en español —Reina-Valera 1909, Biblia en Español Sencillo,
Palabra de Dios para Ti, Versión Biblia Libre— traen los 66 libros y ninguna
más. Así que esto está traducido a mano, del griego, versículo por versículo.

Criterios, para que lo que se añada después siga los mismos:

- Se traduce del griego que está en la aplicación, no de una traducción inglesa.
  Traducir una traducción es como sacar una fotocopia de una fotocopia.
- El griego del Panopolitano viene con erratas de copista y con lagunas. Las
  erratas se corrigen en silencio cuando la palabra es obvia —«οὐρονοῦ» por
  «οὐρανοῦ»— y las lagunas se marcan con […], porque un hueco callado es una
  mentira: quien estudia tiene que saber dónde se acabó el papiro.
- Los corchetes del editor griego se conservan: marcan lo que probablemente
  añadió un copista posterior, y en exégesis eso se discute.
- Registro sobrio y actual, sin arcaísmos de adorno. «Los Vigilantes», no «los
  egrégoros»; pero «miríadas» se queda, porque es el término que usa Judas.
- Los nombres propios, en su forma castellana corriente: Enoc, Semyaza, Azazel,
  Sinaí.

Está entero lo que el Panopolitano conserva: los 222 versículos de los capítulos
1 a 32, salvo el 4 y los versículos sueltos que el papiro perdió. El resto del
libro —hasta el 108— solo sobrevive completo en etíope, y es otro trabajo.
"""

from __future__ import annotations

# {(capítulo, versículo): texto en español}
ENOC_ES: dict[tuple[int, int], str] = {
    # --- 1. El oráculo de bendición; la teofanía -----------------------------
    (1, 1): "Palabra de bendición de Enoc, con la que bendijo a los escogidos y "
            "justos, los que estarán en el día de la angustia, cuando sean "
            "quitados todos los enemigos; y los justos serán salvados.",
    (1, 2): "Y tomando su parábola, dijo Enoc —hombre justo, a quien Dios le "
            "había abierto una visión—: teniendo yo la visión del Santo en los "
            "cielos, […] me la mostraron; y oí las palabras de los santos, y "
            "según se las oí, todo lo entendí al contemplarlo. Y no pensaba en "
            "esta generación, sino en una que está lejos: de ella hablo.",
    (1, 3): "Y de los escogidos hablo ahora, y por ellos tomé mi parábola: "
            "saldrá mi Santo, el Grande, de su morada,",
    (1, 4): "y el Dios eterno pisará la tierra sobre el monte Sinaí, y se "
            "mostrará desde su campamento, y se mostrará en el poder de su "
            "fuerza desde el cielo de los cielos.",
    (1, 5): "Y temerán todos, y los Vigilantes creerán, y entonarán cánticos "
            "ocultos en todos los confines de la tierra; y se estremecerán "
            "todos los confines de la tierra, y se apoderará de ellos temblor y "
            "gran temor hasta los extremos de la tierra.",
    (1, 6): "Y se estremecerán y caerán y se desharán los montes altos, y serán "
            "abatidas las colinas altas hasta desmoronarse los montes, y se "
            "fundirán como cera ante el fuego, en su llama.",
    (1, 7): "Y la tierra se partirá con una hendidura, con una grieta, y todo "
            "cuanto hay sobre ella perecerá. Y habrá juicio contra todos.",
    (1, 8): "Y con los justos hará la paz, y sobre los […]",
    (1, 9): "porque viene con sus miríadas y con sus santos, a hacer juicio "
            "contra todos; y destruirá a todos los impíos, y reprenderá a toda "
            "carne por todas las obras de impiedad que cometieron, y por las "
            "palabras duras que hablaron, y por todo lo que contra él dijeron "
            "los pecadores impíos.",

    # --- 2. El orden del cielo y de la tierra --------------------------------
    (2, 1): "Considerad todas las obras que hay en el cielo: cómo no alteraron "
            "sus caminos; y las lumbreras que hay en el cielo, cómo todas salen "
            "y se ponen, cada una ordenada en el tiempo que le está señalado; y "
            "en sus fiestas aparecen y no se salen del orden que les es propio.",
    (2, 2): "Mirad la tierra y reflexionad sobre las obras que en ella se hacen, "
            "desde el principio hasta el fin [son corruptibles]: cómo nada de lo "
            "que hay sobre la tierra se altera, sino que todas las obras de Dios "
            "se os muestran. Mirad el verano y el invierno […]",

    # --- 3. Los árboles ------------------------------------------------------
    (3, 1): "Aprended y mirad todos los árboles, […]",

    # --- 5. La acusación, la maldición y la promesa --------------------------
    (5, 1): "[…] cómo sus hojas verdes los cubren, y todo su fruto es para honra "
            "y gloria. Reflexionad y conoced todas sus obras, y entended que el "
            "Dios vivo las hizo así, y que él vive por todos los siglos.",
    (5, 3): "Mirad cómo el mar y los ríos cumplen igualmente su tarea, y no "
            "alteran sus obras, conforme a las palabras de él.",
    (5, 4): "Pero vosotros no permanecisteis ni obrasteis conforme a sus "
            "mandamientos, sino que os apartasteis y hablasteis palabras grandes "
            "y duras con vuestra boca inmunda contra su grandeza. Porque "
            "hablasteis con vuestras mentiras, duros de corazón: no hay paz para "
            "vosotros.",
    (5, 5): "Por eso maldijisteis vuestros propios días, y los años de vuestra "
            "vida perecerán, y los años de vuestra perdición se multiplicarán en "
            "maldición eterna, y no habrá para vosotros ni misericordia ni paz.",
    (5, 6): "Entonces vuestros nombres serán maldición eterna para todos los "
            "justos, y en vosotros maldecirán todos los que maldicen, y por "
            "vosotros jurarán todos los pecadores e impíos. [Y todos los que no "
            "tienen mancha se alegrarán, y habrá para ellos perdón de pecados y "
            "toda misericordia y paz y clemencia; habrá para ellos salvación, luz "
            "buena, y ellos heredarán la tierra; y para vosotros los pecadores no "
            "habrá salvación, sino que sobre todos vosotros caerá maldición.]",
    (5, 7): "Y para los escogidos habrá luz y gracia y paz, y ellos heredarán la "
            "tierra; pero para vosotros los impíos habrá maldición.",
    (5, 8): "Entonces se dará a los escogidos luz y gracia, y ellos heredarán la "
            "tierra; entonces se dará a todos los escogidos sabiduría, y todos "
            "ellos vivirán y no volverán a pecar, ni por olvido ni por soberbia; "
            "y habrá luz en el hombre iluminado, y entendimiento en el hombre "
            "que sabe.",
    (5, 9): "Y no cometerán falta ni pecarán en todos los días de su vida, ni "
            "morirán en ardor de ira, sino que cumplirán el número de los días de "
            "su vida; y su vida crecerá en paz, y los años de su gozo se "
            "multiplicarán en alegría y en paz eterna, todos los días de su vida.",

    # --- 6. Los Vigilantes conspiran ----------------------------------------
    (6, 1): "En aquellos días les nacieron hijas hermosas y bellas.",
    (6, 2): "Y las vieron los ángeles, hijos del cielo, y las desearon, y se "
            "dijeron unos a otros: «Venid, escojamos para nosotros mujeres de "
            "entre los hombres, y engendremos hijos para nosotros».",
    (6, 3): "Y les dijo Semyaza, que era su jefe: «Temo que no queráis llevar a "
            "cabo este asunto, y quede yo solo como deudor de un gran pecado».",
    (6, 4): "Le respondieron entonces todos: «Juremos todos con juramento y "
            "comprometámonos unos a otros bajo anatema a no apartarnos de este "
            "propósito hasta cumplirlo y llevar a cabo este asunto».",
    (6, 5): "Entonces juraron todos juntos y se comprometieron unos a otros bajo "
            "anatema, allí en el monte.",
    (6, 7): "Y estos son los nombres de sus jefes: Semyaza —éste era su jefe—, "
            "Aratac, Kimbrá, Daniel, Aredrós, Semiel, Yomeiel, Jocariel, "
            "Ezequiel, Batriel, Satiel, Atriel, Tamiel, Baraquiel, Anantná, "
            "Ramiel, Aseal, Raquiel, Turiel.",
    (6, 8): "Éstos son sus jefes, los que mandan de diez en diez.",

    # --- 7. Las mujeres, los gigantes y la sangre ---------------------------
    (7, 1): "Y tomaron para sí mujeres: cada uno escogió la suya. Y sucedió que, "
            "cuando se multiplicaron los hijos de los hombres, les nacieron "
            "hijas hermosas; y los Vigilantes las desearon y se extraviaron tras "
            "ellas, y se dijeron unos a otros: «Escojamos para nosotros mujeres "
            "de entre las hijas de los hombres de la tierra». Y Semyaza, su "
            "jefe, les dijo: «Temo que no queráis llevar a cabo este asunto, y "
            "quede yo solo como deudor de un gran pecado». Y le respondieron "
            "todos y dijeron: «Juremos todos con juramento y comprometámonos "
            "unos a otros bajo anatema a no apartarnos de este propósito hasta "
            "cumplirlo». Entonces juraron todos juntos y se comprometieron unos "
            "a otros bajo anatema. Eran doscientos los que descendieron en los "
            "días de Jared a la cumbre del monte Hermoniim; y llamaron al monte "
            "Hermón, porque en él juraron y se comprometieron unos a otros bajo "
            "anatema. Y estos son los nombres de sus jefes: 1.º Semyaza, su "
            "jefe; 2.º Atarcuf; 3.º Araquiel; 4.º Jobabiel; 5.º Orammamé; "
            "6.º Ramiel; 7.º Sampsij; 8.º Zaquiel; 9.º Balquiel; 10.º Azael; "
            "11.º Farmarós; 12.º Amariel; 13.º Anaguemás; 14.º Tausael; "
            "15.º Samiel; 16.º Sarinás; 17.º Toemiel; 18.º Turiel; 19.º Yumiel; "
            "20.º Sariel. Éstos y todos los demás, en el año mil ciento setenta "
            "y siete del mundo, tomaron para sí mujeres y se unieron a ellas "
            "hasta el diluvio. Y ellas les dieron a luz tres linajes: primero, "
            "gigantes grandes; y los gigantes engendraron a los nefilim, y a los "
            "nefilim les nacieron los eliud. Y crecían conforme a su grandeza, y "
            "se enseñaron a sí mismos y a sus mujeres hechicerías y "
            "encantamientos. […] tomaron para sí mujeres, y comenzaron a entrar "
            "a ellas y a mancharse con ellas, y les enseñaron hechicerías y "
            "encantamientos y el corte de raíces, y les mostraron las hierbas.",
    (7, 2): "Y ellas, habiendo concebido, dieron a luz gigantes grandes, de tres "
            "mil codos,",
    (7, 3): "los cuales devoraban el trabajo de los hombres. Y como los hombres "
            "ya no pudieron sostenerlos,",
    (7, 4): "los gigantes se volvieron contra ellos y devoraban a los hombres.",
    (7, 5): "Y comenzaron a pecar contra las aves y las fieras y los reptiles y "
            "los peces, y a devorar las carnes unos de otros; y bebían la sangre.",
    (7, 6): "Entonces la tierra presentó su acusación contra los inicuos.",

    # --- 8. Lo que los Vigilantes enseñaron ---------------------------------
    (8, 1): "Azael enseñó a los hombres a hacer espadas y armas y escudos y "
            "corazas [enseñanzas de ángeles]; y les mostró los metales y su "
            "labrado, y los brazaletes y los adornos, y el antimonio y el afeite "
            "de los ojos, y toda clase de piedras escogidas, y los tintes.",
    (8, 2): "Y hubo mucha impiedad, y fornicaron y se extraviaron y se "
            "corrompieron en todos sus caminos.",
    (8, 3): "Semyaza enseñó encantamientos y el corte de raíces; Armarós, cómo "
            "deshacer los encantamientos; Raquiel, la astrología; Jojiel, los "
            "signos; Satiel […]; Seriel, los cursos de la luna.",
    (8, 4): "Y mientras los hombres perecían, el clamor subió hasta los cielos. "
            "Primero Azael, el décimo de los jefes, enseñó a hacer espadas y "
            "corazas y todo instrumento de guerra, y los metales de la tierra y "
            "el oro: cómo trabajarlos y hacer con ellos adornos para las "
            "mujeres, y la plata. Y les mostró también el bruñir, el pintarse "
            "con antimonio y el embellecerse, y las piedras escogidas y los "
            "tintes. Y los hijos de los hombres los hicieron para sí y para sus "
            "hijas, y traspasaron los límites y extraviaron a los santos; y hubo "
            "mucha impiedad sobre la tierra, y corrompieron sus caminos. Y "
            "también su jefe principal, Semyaza, enseñó encantamientos contra la "
            "mente y raíces de las hierbas de la tierra. El undécimo, Farmarós, "
            "enseñó hechicerías, encantamientos de sabiduría y remedios contra "
            "los encantamientos. El noveno enseñó la observación de los astros. "
            "El cuarto enseñó la astrología. El octavo enseñó la observación del "
            "aire. El tercero enseñó los signos de la tierra. El séptimo enseñó "
            "los signos del sol. El vigésimo enseñó los signos de la luna. Todos "
            "éstos comenzaron a revelar los misterios a sus mujeres y a sus "
            "hijos. Y después de esto, los gigantes comenzaron a devorar las "
            "carnes de los hombres, y los hombres comenzaron a disminuir sobre "
            "la tierra. Y los que quedaban clamaron al cielo por su aflicción, "
            "pidiendo que su memorial fuese llevado ante el Señor. Y al oírlo "
            "los cuatro grandes arcángeles, Miguel y Uriel y Rafael y Gabriel, "
            "miraron hacia la tierra desde el santuario del cielo. Y viendo "
            "mucha sangre derramada sobre la tierra y toda impiedad e iniquidad "
            "cometida en ella, entraron y se dijeron unos a otros que los "
            "espíritus y las almas de los hombres gimen suplicando y diciendo: "
            "«Llevad nuestra causa ante el Altísimo, y nuestra perdición ante la "
            "gloria de la majestad, ante el Señor de todos los señores en la "
            "majestad». Y dijeron al Señor de los siglos: «Tú eres el Dios de "
            "los dioses y el Señor de los señores y el Rey de los que reinan y "
            "Dios de los siglos; y el trono de tu gloria es por todas las "
            "generaciones de los siglos, y tu nombre es santo y bendito por "
            "todos los siglos».",

    # --- 9. El clamor de la tierra y la súplica de los arcángeles -----------
    (9, 1): "Entonces, asomándose desde el cielo, Miguel y Uriel y Gabriel "
            "vieron mucha sangre derramada sobre la tierra,",
    (9, 2): "y se dijeron unos a otros: «La voz de los que claman desde la "
            "tierra llega hasta las puertas del cielo».",
    (9, 3): "Las almas de los hombres suplican diciendo: «Llevad nuestra causa "
            "ante el Altísimo».",
    (9, 4): "Y dijeron al Señor: «Tú eres Señor de los señores y Dios de los "
            "dioses y Rey de los siglos. El trono de tu gloria es por todas las "
            "generaciones del siglo, y tu nombre es santo y grande y bendito por "
            "todos los siglos;",
    (9, 5): "porque tú hiciste todas las cosas y tienes toda potestad, y todo "
            "está delante de ti manifiesto y descubierto, y tú lo ves todo […]",
    (9, 6): "lo que hizo Azael, que enseñó todas las injusticias sobre la tierra "
            "y reveló los misterios del siglo, los que están en el cielo, los "
            "que los hombres se afanan por",
    (9, 7): "conocer; y a Semyaza, a quien diste potestad de mandar sobre los "
            "que están con él.",
    (9, 8): "Y fueron a las hijas de los hombres de la tierra y se acostaron con "
            "ellas y se mancharon, y les revelaron todos los pecados.",
    (9, 9): "Y las mujeres dieron a luz titanes, por los cuales toda la tierra "
            "[se llenó de sangre]. Entonces clamaron los hombres al cielo, "
            "diciendo: «Llevad nuestra causa ante el Altísimo, y nuestra "
            "perdición ante la gloria grande, ante el Señor de todos los señores "
            "en la majestad». Y al oírlo los cuatro grandes arcángeles, Miguel y "
            "Uriel y Rafael y Gabriel, se asomaron a la tierra desde el santuario "
            "del cielo; y viendo mucha sangre derramada sobre la tierra y toda "
            "iniquidad e impiedad cometida en ella, entraron y se dijeron unos a "
            "otros que los espíritus y las almas de los hombres suplican gimiendo "
            "y diciendo: «Llevad nuestra súplica ante el Altísimo». Y "
            "acercándose los cuatro arcángeles, dijeron al Señor: «Tú eres Dios "
            "de los dioses y Señor de los señores y Rey de los reyes y Dios de "
            "los siglos; y el trono de tu gloria es por todas las generaciones "
            "de los siglos, y tu nombre es santo y bendito por todos los siglos. "
            "Porque tú eres el que hizo todas las cosas y el que tiene potestad "
            "sobre todas, y todo está delante de ti manifiesto y descubierto, y "
            "todo lo ves, y no hay nada que pueda esconderse de ti. Ves cuánto "
            "hizo Azael, cuánto introdujo y cuánto enseñó: injusticias y pecados "
            "sobre la tierra, y todo engaño sobre la tierra seca. Porque enseñó "
            "los misterios y reveló al mundo lo que está en el cielo; y los "
            "hijos de los hombres se afanan en sus prácticas para conocer los "
            "misterios. A Semyaza le diste potestad de mandar sobre los que "
            "están con él. Y fueron a las hijas de los hombres de la tierra y se "
            "acostaron con ellas y se mancharon con las mujeres, y les revelaron "
            "todos los pecados y les enseñaron a hacer filtros de odio. Y ahora, "
            "he aquí, las hijas de los hombres dieron a luz de ellos hijos "
            "gigantes, engendros bastardos sobre la tierra; la sangre de los "
            "hombres ha sido derramada, y toda la tierra está llena de "
            "injusticia. Y ahora, he aquí, los espíritus de las almas de los "
            "hombres muertos suplican, y hasta las puertas del cielo subió su "
            "gemido, y no puede salir de delante de las injusticias que se "
            "cometen sobre la tierra. Y la tierra se ha llenado de sangre y de "
            "injusticia».",
    (9, 10): "Y ahora, he aquí, claman las almas de los que han muerto, y "
             "suplican hasta las puertas del cielo; y su gemido subió, y no "
             "puede salir de delante de las iniquidades que se cometen sobre la "
             "tierra.",
    (9, 11): "Y tú lo sabes todo antes de que suceda, y ves esto y los dejas, y "
             "ni siquiera nos dices qué hay que hacer con ellos por estas cosas.",

    # --- 10. La sentencia: Noé, Azael, los gigantes, la tierra limpia -------
    (10, 1): "Entonces el Altísimo habló [acerca de esto], el Grande, el Santo, "
             "y dijo, y envió a Istrael al hijo de Lamec:",
    (10, 2): "«Dile en mi nombre: Escóndete. Y revélale el fin que viene, porque "
             "toda la tierra perece, y va a haber un diluvio sobre toda la "
             "tierra, y destruirá todo cuanto hay en ella.",
    (10, 3): "Y enséñale cómo escapar, para que su descendencia permanezca por "
             "todas las generaciones del siglo».",
    (10, 4): "Y a Rafael le dijo: «Ata a Azael de pies y manos y échalo en las "
             "tinieblas; y abre el desierto que está en Dadúel, y échalo allí;",
    (10, 5): "y pon debajo de él piedras ásperas y agudas, y cúbrelo de "
             "tinieblas, y habite allí para siempre; y tápale el rostro, y que "
             "no vea la luz.",
    (10, 6): "Y en el gran día del juicio será llevado al incendio.",
    (10, 7): "Y sanará la tierra, la que los ángeles arruinaron; y revela la "
             "curación de la tierra, para que curen la plaga, para que no "
             "perezcan […]. Y tú lo sabes todo antes de que suceda, y los ves y "
             "los dejas y no dices nada. ¿Qué hay que hacer con ellos por esto? "
             "Entonces habló el Altísimo, y el Santo, el Grande, dijo, y envió a "
             "Uriel al hijo de Lamec, diciendo: «Ve a Noé y dile en mi nombre: "
             "Escóndete. Y revélale el fin que viene, porque toda la tierra "
             "perece. Y dile que va a haber un diluvio sobre toda la tierra, "
             "para destruirlo todo de sobre la faz de la tierra. Enseña al justo "
             "qué debe hacer, al hijo de Lamec; y él guardará su alma para vida "
             "y escapará por siempre, y de él será plantado un plantío que "
             "permanecerá por todas las generaciones del siglo». Y a Rafael le "
             "dijo: «Ve, Rafael, y ata a Azael de manos y pies, trábalo y échalo "
             "en las tinieblas; y abre el desierto que está en Dudael, y ve allí "
             "y échalo; y pon debajo de él piedras agudas y piedras ásperas, y "
             "cúbrelo de tinieblas, y habite allí para siempre; y tápale el "
             "rostro, y que no vea la luz. Y en el día del juicio será llevado "
             "al incendio del fuego. Y sana la tierra, la que los Vigilantes "
             "arruinaron; y revela la curación de la tierra, para que curen la "
             "tierra y no perezcan todos los hijos de los hombres por el "
             "misterio que dijeron los Vigilantes y enseñaron a sus hijos. Y "
             "quedó desolada toda la tierra por las obras de la enseñanza de "
             "Azael; y escribe sobre él todos los pecados». Y a Gabriel le dijo: "
             "«Ve, Gabriel, contra los gigantes, contra los bastardos, contra "
             "los hijos de la fornicación, y destruye a los hijos de los "
             "Vigilantes de entre los hijos de los hombres. Mándalos unos contra "
             "otros, de ellos contra ellos mismos, en guerra y en perdición. Y "
             "no habrá para ellos largura de días, y ninguna petición habrá para "
             "sus padres, aunque esperan vivir vida eterna y que cada uno de "
             "ellos viva quinientos años». Y a Miguel le dijo: «Ve, Miguel, ata "
             "a Semyaza y a los otros que están con él, los que se mezclaron con "
             "las hijas de los hombres […]».",
    (10, 8): "Y quedó desolada la tierra, arruinada por las obras de la "
             "enseñanza de Azael; y escribe sobre él todos los pecados.",
    (10, 9): "Y a Gabriel le dijo el Señor: «Ve contra los mazereos, contra los "
             "bastardos y los hijos de la fornicación, y destruye a los hijos de "
             "los Vigilantes de entre los hombres. Mándalos a una guerra de "
             "perdición, porque no hay para ellos largura de días.",
    (10, 10): "Y ninguna petición habrá para ellos ni acerca de ellos, aunque "
              "esperan vivir vida eterna y que cada uno de ellos viva quinientos "
              "años».",
    (10, 11): "Y dijo: «Miguel, ve y ata a Semyaza y a los demás que están con "
              "él, los que se unieron con las mujeres para mancharse con ellas "
              "en su inmundicia.",
    (10, 12): "Y cuando sean degollados sus hijos y vean la perdición de sus "
              "amados, átalos por setenta generaciones en los valles de la "
              "tierra, hasta el día de su juicio y de su consumación, hasta que "
              "se cumpla el juicio del siglo de los siglos.",
    (10, 13): "Entonces serán llevados al caos del fuego, y al tormento, y a la "
              "cárcel del encierro eterno.",
    (10, 14): "Y cualquiera que sea condenado y aniquilado, desde ahora será "
              "atado juntamente con ellos hasta el fin de su generación.",
    (10, 15): "Destruye todos los espíritus de los bastardos y a los hijos de "
              "los Vigilantes, porque hicieron injusticia a los hombres.",
    (10, 16): "Y destruye toda injusticia de sobre la tierra, y cese toda obra "
              "de maldad; y aparezca la planta de la justicia y de la verdad "
              "[…], y para siempre será plantada con gozo.",
    (10, 17): "Y ahora todos los justos escaparán y vivirán hasta engendrar "
              "millares, y cumplirán en paz todos los días de su juventud y sus "
              "sábados.",
    (10, 18): "[…] de los hombres, para mancharse con ellas en su inmundicia. Y "
              "cuando sean degollados sus hijos y vean la perdición de sus "
              "amados, átalos por setenta generaciones en los valles de la "
              "tierra, hasta el día de su juicio, hasta el día del cumplimiento "
              "final, hasta que se consume el juicio del siglo de los siglos. "
              "Entonces serán llevados al caos del fuego, y al tormento, y a la "
              "cárcel del encierro del siglo. Y cualquiera que sea condenado y "
              "aniquilado, desde ahora será atado juntamente con ellos hasta el "
              "fin de su generación.",
    (10, 19): "Y todos los árboles de la tierra se alegrarán, y plantarán viñas; "
              "y la vid que planten producirá mil cántaros de vino, y la semilla "
              "producirá por cada medida […]; el olivo producirá diez batos.",
    (10, 20): "Y tú limpia la tierra de toda inmundicia y de toda injusticia y "
              "de todo pecado e impiedad; y borra todas las inmundicias que se "
              "cometen sobre la tierra […]",
    (10, 21): "Y todos los pueblos me servirán y me bendecirán y me adorarán.",
    (10, 22): "Y toda la tierra quedará limpia de toda contaminación y de toda "
              "inmundicia, y de ira y de azote; y no volveré a enviarlos sobre "
              "ellos por todas las generaciones del siglo».",
    # --- 11. Los tesoros de bendición ---------------------------------------
    (11, 1): "Y entonces abriré los tesoros de bendición que hay en el cielo, y "
             "los haré bajar [sobre las obras,] sobre el trabajo de los hijos de "
             "los hombres.",
    (11, 2): "Y entonces la verdad y la paz irán juntas por todos los días del "
             "siglo y por todas las generaciones de los hombres.",

    # --- 12. Enoc, escriba de justicia, es enviado a los Vigilantes ---------
    (12, 1): "Antes de estas palabras fue arrebatado Enoc, y ninguno de los "
             "hombres supo dónde fue arrebatado, ni dónde está, ni qué fue de él.",
    (12, 2): "Y sus obras eran con los Vigilantes, y sus días con los santos.",
    (12, 3): "Y yo, Enoc, estaba de pie bendiciendo al Señor de la majestad, al "
             "Rey de los siglos; y he aquí que los Vigilantes del Santo, del "
             "Grande, me llamaban:",
    (12, 4): "«Enoc, escriba de justicia, ve y di a los Vigilantes del cielo "
             "—los que, abandonando el cielo alto, el santuario de la estación "
             "del siglo, se mancharon con las mujeres y, como hacen los hijos de "
             "la tierra, así hicieron ellos y tomaron para sí mujeres—: Habéis "
             "arruinado la tierra con gran ruina,",
    (12, 5): "y no habrá para vosotros paz ni perdón».",

    # --- 13. La sentencia a Azael y el memorial de los Vigilantes ----------
    (13, 1): "Y Enoc dijo a Azael: «Ve; no habrá paz para ti. Sentencia grande "
             "ha salido contra ti, para atarte;",
    (13, 2): "y no habrá para ti tregua ni petición, por las injusticias que "
             "mostraste y por todas las obras de impiedad y de injusticia y de "
             "pecado que enseñaste a los hombres».",
    (13, 3): "Entonces fui y se lo dije a todos ellos, y todos ellos temieron, y "
             "se apoderó de ellos temblor y temor.",
    (13, 4): "Y pidieron que les escribiera un memorial de súplica, para que les "
             "fuese dado perdón [y largura de días], y para que yo leyera ese "
             "memorial de súplica delante del Señor del cielo.",
    (13, 5): "Porque ellos ya no pueden hablar ni levantar sus ojos al cielo, de "
             "vergüenza por aquello en que habían pecado y por lo que fueron "
             "condenados.",
    (13, 6): "Entonces escribí el memorial de su súplica y las peticiones acerca "
             "de sus espíritus y de lo que piden, para que les fuese dado perdón "
             "y largura de días.",
    (13, 7): "Y fui y me senté junto a las aguas de Dan, en la tierra de Dan, "
             "que está a la derecha, al occidente de Hermoniim; y leía el "
             "memorial de sus peticiones hasta que me dormí.",
    (13, 8): "Y he aquí que vinieron sobre mí sueños, y cayeron sobre mí "
             "visiones, y vi visiones de ira; y vino una voz que decía: «Habla a "
             "los hijos del cielo para reprenderlos».",
    (13, 9): "Y al despertar fui a ellos, y estaban todos reunidos, sentados y "
             "llorando, en Ebelsata, que está entre el Líbano y Senesel, con el "
             "rostro cubierto.",
    (13, 10): "[…] delante de ellos, y les conté todas las visiones que había "
              "visto en sueños, y comencé a hablar las palabras de justicia, "
              "reprendiendo a los Vigilantes del cielo.",

    # --- 14. El libro de la reprensión, y la visión del trono --------------
    (14, 1): "Libro de las palabras de justicia y de la reprensión de los "
             "Vigilantes que son desde el siglo, conforme al mandamiento del "
             "Santo, del Grande, en esta visión.",
    (14, 2): "Yo vi en mis sueños lo que ahora digo con lengua de carne, con el "
             "aliento de mi boca, que el Grande dio a los hombres para hablar "
             "con ella y entender con el corazón.",
    (14, 4): "Yo escribí vuestra súplica [la de los ángeles], y en mi visión se "
             "me mostró esto: que vuestra súplica no fue aceptada […]",
    (14, 5): "para que ya no subáis al cielo por todos los siglos; y se ha dicho "
             "que seáis atados con las ataduras de la tierra por todas las "
             "generaciones del siglo.",
    (14, 6): "Y que antes de eso veáis la perdición de vuestros hijos amados, y "
             "que no os servirán de nada, sino que caerán delante de vosotros a "
             "espada.",
    (14, 7): "Y no habrá súplica por ellos ni por vosotros; y vosotros, llorando "
             "y suplicando, no diréis una sola palabra del escrito que yo "
             "escribí.",
    (14, 8): "Y a mí, en visión, se me mostró así: he aquí que en la visión me "
             "llamaban nubes y me gritaban nieblas; y carreras de estrellas y "
             "relámpagos me apremiaban y me alborotaban; y vientos, en la "
             "visión, me hicieron volar y me levantaron a lo alto y me "
             "introdujeron en el cielo.",
    (14, 9): "Y entré hasta acercarme a un muro edificado con piedras de "
             "granizo, y lenguas de fuego alrededor de él; y comenzaron a "
             "espantarme.",
    (14, 10): "Y entré en las lenguas de fuego y me acerqué a una casa grande, "
              "edificada con piedras de granizo; y las paredes de la casa eran "
              "como losas de piedra, y todas eran de nieve, y el suelo de nieve.",
    (14, 11): "Y los techos eran como carreras de estrellas y relámpagos, y en "
              "medio de ellos querubines de fuego, y su cielo era agua;",
    (14, 12): "y fuego ardiendo alrededor de las paredes, y puertas que ardían "
              "en fuego.",
    (14, 13): "Entré en aquella casa, caliente como fuego y fría como nieve, y "
              "no había en ella deleite alguno de vida. Temor me cubrió y "
              "temblor se apoderó de mí,",
    (14, 14): "y yo estaba sacudido y temblando, y caí sobre mi rostro y miraba "
              "en mi visión.",
    (14, 15): "Y he aquí otra puerta abierta delante de mí, y una casa mayor que "
              "aquélla, toda edificada con lenguas de fuego.",
    (14, 17): "Su suelo era de fuego, y lo más alto de ella eran relámpagos y "
              "carreras de estrellas, y su techo era fuego ardiente.",
    (14, 18): "Y miraba, y vi un trono alto, y su aspecto era como de cristal; y "
              "una rueda como de sol resplandeciente, y un monte de querubines.",
    (14, 19): "Y por debajo del trono salían ríos de fuego ardiente, y yo no "
              "podía mirar.",
    (14, 20): "Y la Gloria grande estaba sentada sobre él; su vestidura era más "
              "brillante que el sol y más blanca que toda nieve.",
    (14, 21): "Y ningún ángel podía entrar en esta casa ni ver su rostro, por lo "
              "honorable y glorioso que es; y ninguna carne podía ver",
    (14, 22): "el fuego que ardía alrededor. Y un gran fuego estaba delante de "
              "él, y nadie se le acerca alrededor; miríadas de miríadas están "
              "delante de él, y toda palabra suya es obra.",
    (14, 23): "Y los santos de los ángeles que se le acercan no se apartan de "
              "noche ni se alejan de él.",
    (14, 24): "Y yo estuve hasta entonces echado sobre mi rostro y temblando. Y "
              "el Señor me llamó con su boca y me dijo: «Acércate acá, Enoc, y "
              "escucha mi palabra».",
    (14, 25): "Y viniendo a mí uno de los santos, me levantó y me puso en pie y "
              "me llevó hasta la puerta; y yo inclinaba mi rostro hacia abajo.",
    # --- 15. Por qué no hay perdón para los Vigilantes ---------------------
    (15, 1): "Y respondiendo me dijo [el hombre verdadero de la verdad, el "
             "escriba], y oí su voz: «No temas, Enoc, hombre verdadero y escriba "
             "de la verdad; acércate acá y escucha mi voz.",
    (15, 2): "Ve y di a los que te enviaron […]: a vosotros os tocaba interceder "
             "por los hombres, y no a los hombres por vosotros.",
    (15, 3): "¿Por qué abandonasteis el cielo alto, el santo del siglo, y os "
             "acostasteis con las mujeres, y os manchasteis con las hijas de los "
             "hombres, y tomasteis para vosotros mujeres, e hicisteis como hacen "
             "los hijos de la tierra, y engendrasteis para vosotros hijos "
             "gigantes?",
    (15, 5): "Por eso les di a ellos hembras, para que sembraran en ellas y "
             "engendraran hijos en ellas, para que no les faltase obra alguna "
             "sobre la tierra.",
    (15, 6): "Pero vosotros erais espíritus vivientes, eternos, que no mueren "
             "por todas las generaciones del siglo.",
    (15, 7): "Y por eso no hice hembras entre vosotros: los del cielo, en el "
             "cielo tienen su morada.",
    (15, 8): "Y ahora, los gigantes, nacidos de los espíritus y de la carne, "
             "serán llamados espíritus malignos sobre la tierra, y en ella "
             "estará su morada.",
    (15, 9): "Espíritus malignos salieron de su cuerpo, porque de los de arriba "
             "nacieron, y de los santos Vigilantes es el principio de su "
             "creación y el principio de su fundamento. Espíritus malignos serán "
             "llamados.",
    (15, 10): "Los del cielo, en el cielo será su morada; y los espíritus "
              "nacidos sobre la tierra, en la tierra será su morada.",
    (15, 11): "Y los espíritus de los gigantes, los nefilim, que hacen "
              "injusticia, que arruinan y asaltan y luchan y derriban sobre la "
              "tierra [espíritus duros de gigantes], y que hacen […] y nada "
              "comen, sino que ayunan y tienen sed y hacen tropezar.",
    (15, 12): "Y estos espíritus se levantarán contra los hijos de los hombres y "
              "de las mujeres, porque de ellos salieron. Y ahora, los gigantes "
              "nacidos de espíritus y de carne: espíritus malignos los llamarán "
              "sobre la tierra, porque su morada estará sobre la tierra. "
              "Espíritus malignos serán los espíritus salidos del cuerpo de su "
              "carne, porque de los hombres nacieron y de los santos Vigilantes "
              "es el principio de su creación y el principio de su fundamento. "
              "Espíritus malignos serán sobre la tierra. Los espíritus de los "
              "gigantes, que se apacientan, que hacen injusticia, que arruinan, "
              "que asaltan y luchan y derriban sobre la tierra, y hacen "
              "carreras, y no comen sino que ayunan, y hacen apariciones, y "
              "tienen sed y hacen tropezar. Y se levantarán estos espíritus "
              "contra los hijos de los hombres y de las mujeres, porque de ellos "
              "salieron. Y desde el día de la matanza y de la muerte de los "
              "gigantes nefilim, los fuertes de la tierra, los grandes de "
              "renombre […]",

    # --- 16. Ningún misterio os fue ocultado, y lo revelasteis -------------
    (16, 1): "Desde el día de la matanza y de la perdición y de la muerte de los "
             "nefilim, los espíritus que salen del alma de su carne arruinan sin "
             "juicio: así arruinarán hasta el día del gran juicio, en el que el "
             "siglo grande se cumplirá.",
    (16, 2): "Y ahora, a los Vigilantes que te enviaron a interceder por ellos, "
             "los que estaban en el cielo, diles:",
    (16, 3): "«Vosotros estabais en el cielo, y no había misterio que no os "
             "fuese revelado; y conocisteis el misterio venido de Dios, y lo "
             "revelasteis a las mujeres en vuestra dureza de corazón; y por ese "
             "misterio las hembras y los hombres multiplican los males sobre la "
             "tierra».",
    (16, 4): "Diles, pues: no hay paz.",

    # --- 17. El primer viaje: el fuego del occidente ----------------------
    (17, 1): "Y tomándome, me llevaron a cierto lugar donde los que allí están "
             "se vuelven como fuego ardiente y, cuando quieren, aparecen como "
             "hombres.",
    (17, 2): "Y me llevaron a un lugar tenebroso y a un monte cuya cima llegaba "
             "hasta el cielo.",
    (17, 3): "Y vi el lugar de las lumbreras y los tesoros de las estrellas y de "
             "los truenos, y las profundidades del aire, donde están el arco de "
             "fuego y las flechas y sus aljabas, y todos los relámpagos.",
    (17, 4): "Y me llevaron hasta las aguas vivas y hasta el fuego del "
             "occidente, que es el que provee todas las puestas del sol.",
    (17, 5): "Y llegamos hasta un río de fuego, en el cual el fuego corre como "
             "agua y desemboca en un gran mar del occidente.",
    (17, 6): "Vi los grandes […] Los espíritus que salen de su alma, como de la "
             "carne, arruinarán sin juicio. Así arruinarán hasta el día del "
             "cumplimiento, hasta el gran juicio, en el que el siglo grande se "
             "cumplirá, de una vez y todo junto. Y otra vez: acerca del monte en "
             "el que juraron y se comprometieron unos con otros bajo anatema, "
             "que jamás se apartará de él el frío y la nieve y la escarcha, y el "
             "rocío no descenderá sobre él sino para maldición, hasta el día del "
             "gran juicio. En aquel tiempo será quemado y abatido, y estará "
             "ardiendo y derritiéndose como cera ante el fuego; así será quemado "
             "por todas sus obras. Y ahora yo os digo a vosotros, hijos de los "
             "hombres: ira grande hay contra vosotros y contra vuestros hijos, y "
             "esta ira no cesará sobre vosotros hasta el tiempo de la matanza de "
             "vuestros hijos. Y perecerán vuestros amados y morirán vuestros "
             "honrados de toda la tierra, porque todos los días de su vida, "
             "desde ahora, no pasarán de ciento veinte años. Y no penséis vivir "
             "más años, porque no hay para ellos camino alguno de escape desde "
             "ahora, por la ira con que se airó contra vosotros el Rey de todos "
             "los siglos. No penséis que escaparéis de esto. Y esto es del "
             "primer libro de Enoc, acerca de los Vigilantes. […] ríos [y hasta "
             "el gran río], y llegué hasta las tinieblas y me fui adonde ninguna "
             "carne camina.",
    (17, 7): "Vi los vientos de las tinieblas, los del invierno, y el "
             "derramamiento del abismo de todas las aguas.",
    (17, 8): "Vi la boca de la tierra de todos los ríos y la boca del abismo.",

    # --- 18. Los tesoros de los vientos y la cárcel de las estrellas -------
    (18, 1): "Vi los tesoros de todos los vientos; vi que con ellos adornó todas "
             "las criaturas, y el fundamento de la tierra.",
    (18, 2): "Y vi la piedra angular de la tierra; vi los cuatro vientos que "
             "sostienen la tierra y el firmamento del cielo.",
    (18, 3): "Y ellos están entre la tierra y el cielo.",
    (18, 4): "Vi los vientos que hacen girar el cielo y dan vueltas a la rueda "
             "del sol y a todas las estrellas.",
    (18, 5): "Vi los vientos que sobre la tierra llevan la nube; vi […] los "
             "confines de la tierra, el sostén del cielo por encima.",
    (18, 6): "Pasé adelante y vi un lugar que arde de noche y de día, donde "
             "están los siete montes de piedras preciosas: tres hacia el oriente "
             "y tres hacia el sur.",
    (18, 7): "Y los que están hacia el oriente eran de piedra de color, y uno de "
             "perla, y otro de […]; y los del sur, de piedra roja.",
    (18, 8): "Y el de en medio de ellos llegaba al cielo, como el trono de Dios, "
             "de piedra […]; y la cima del trono, de piedra de zafiro.",
    (18, 9): "Y vi fuego ardiendo; y más allá de aquellos montes",
    (18, 10): "hay un lugar, el confín de la gran tierra. Allí se consumarán los "
              "cielos.",
    (18, 12): "Y más allá de aquel abismo vi un lugar donde no había firmamento "
              "de cielo por encima, ni tierra fundada debajo, ni agua debajo de "
              "él, ni ave alguna: era un lugar desierto y terrible.",
    (18, 13): "Allí vi siete estrellas como grandes montes ardiendo; y al "
              "preguntar yo por ellas,",
    (18, 14): "el ángel me dijo: «Éste es el lugar, el fin del cielo y de la "
              "tierra; ésta se hizo cárcel para los astros y para las potestades "
              "del cielo.",
    (18, 15): "Y las estrellas que ruedan en el fuego son las que traspasaron el "
              "mandato del Señor al comienzo de su salida, porque no salieron en "
              "sus tiempos.",
    (18, 16): "Y se airó contra ellas y las ató hasta el tiempo del cumplimiento "
              "de su pecado: diez mil años».",

    # --- 19. Las mujeres de los Vigilantes, y lo que Enoc vio solo ---------
    (19, 1): "Y me dijo Uriel: «Aquí estarán los ángeles que se mezclaron con "
             "las mujeres; y sus espíritus, hechos de muchas formas, dañan a los "
             "hombres y los extraviarán para que sacrifiquen a los demonios, "
             "hasta el gran juicio, en el que serán juzgados hasta el fin.",
    (19, 2): "Y las mujeres de aquellos ángeles que se extraviaron se "
             "convertirán en sirenas».",
    (19, 3): "Y yo, Enoc, vi los espectáculos, yo solo, los confines de todo; y "
             "ningún hombre los verá como yo los he visto.",

    # --- 20. Los siete arcángeles y su oficio ------------------------------
    (20, 1): "Ángeles de las potestades:",
    (20, 2): "Uriel, uno de los santos ángeles, el que está sobre el mundo y "
             "sobre el Tártaro.",
    (20, 3): "Rafael, uno de los santos, el que está sobre los espíritus de los "
             "hombres.",
    (20, 4): "Raguel, uno de los santos ángeles, el que toma venganza del mundo "
             "de las lumbreras.",
    (20, 5): "Miguel, uno de los santos ángeles, el puesto sobre los bienes del "
             "pueblo [y sobre el caos].",
    (20, 6): "Sariel, uno de los santos ángeles, el que está sobre los espíritus "
             "de los que pecan en el espíritu.",
    (20, 8): "Remiel, uno de los santos ángeles, a quien Dios puso sobre los que "
             "resucitan. Los nombres de los arcángeles: siete.",

    # --- 21. El lugar sin forma y las estrellas atadas ---------------------
    (21, 1): "Y recorrí hasta el lugar sin forma,",
    (21, 2): "y allí vi una obra terrible: no vi cielo fundado por encima, sino "
             "un lugar sin forma y terrible.",
    (21, 3): "Y allí contemplé siete de las estrellas del cielo, atadas y "
             "arrojadas en él, semejantes a grandes montes y ardiendo en fuego.",
    (21, 4): "Entonces dije: «¿Por qué causa fueron atadas? ¿Y por qué fueron "
             "arrojadas?».",
    (21, 5): "Entonces me dijo Uriel —uno de los santos, que estaba conmigo y "
             "los guiaba—: «Enoc, ¿por quién preguntas? ¿O acerca de qué buscas "
             "con afán la verdad?».",
    (21, 6): "«Éstas son las estrellas del cielo que traspasaron el mandato "
             "del Señor, y fueron atadas aquí hasta cumplir diez mil años, el "
             "tiempo de sus pecados».",
    (21, 7): "Y de allí recorrí hasta otro lugar más terrible que éste, y "
             "contemplé obras terribles: un gran fuego que allí ardía y "
             "llameaba; y el lugar tenía una hendidura hasta el abismo, llena de "
             "grandes columnas de fuego que caían. Ni su medida ni su anchura "
             "pude ver ni imaginar.",
    (21, 8): "Entonces dije: «¡Qué terrible es este lugar, y qué espantoso a la "
             "vista!».",
    (21, 9): "Entonces me respondió Uriel, uno de los santos ángeles que estaba "
             "conmigo, y me dijo: «Enoc, ¿así te asustaste y te espantaste?». Y "
             "respondí: «Por este lugar terrible y por su aspecto espantoso».",
    (21, 10): "Y dijo: «Este lugar es cárcel de ángeles. Aquí serán retenidos "
              "por el siglo de los siglos».",

    # --- 22. Los lugares huecos donde esperan las almas --------------------
    (22, 1): "Y de allí recorrí hasta otro lugar, y me mostró hacia el occidente "
             "otro monte grande y alto, de roca maciza.",
    (22, 3): "Entonces respondió Rafael, uno de los santos que estaba conmigo, y "
             "me dijo: «Éstos son los lugares huecos para que en ellos se "
             "recojan los espíritus de las almas de los muertos; para esto mismo "
             "fueron destinados, para que aquí se reúnan todas las almas de los "
             "hombres.",
    (22, 4): "Y estos lugares fueron hechos para retenerlos hasta su juicio y "
             "hasta el plazo en que será el gran juicio». En ellos",
    (22, 5): "contemplé el espíritu de un muerto que suplicaba, y su voz llegaba "
             "hasta el cielo y suplicaba.",
    (22, 6): "Y pregunté a Rafael, el ángel que estaba conmigo, y le dije: «Este "
             "espíritu que suplica, ¿de quién es, para que así su voz llegue y "
             "suplique hasta el cielo?».",
    (22, 7): "Y me respondió diciendo: «Éste es el espíritu que salió de Abel, a "
             "quien mató Caín su hermano. Y Abel suplica contra él, para que su "
             "descendencia sea destruida de la faz de la tierra y su simiente "
             "desaparezca de entre la simiente de los hombres».",
    (22, 8): "Entonces pregunté acerca de todas las cavidades: «¿Por qué fueron "
             "separadas una de otra?».",
    (22, 9): "Y me respondió diciendo: «Éstas son para separar los espíritus de "
             "los muertos. Y ésta fue apartada para los espíritus de los justos, "
             "donde está la fuente de agua;",
    (22, 10): "y ésta fue creada para los pecadores, cuando mueren y son "
              "sepultados en la tierra y no hubo juicio sobre ellos en vida.",
    (22, 12): "Y ésta fue apartada para los espíritus de los que suplican, los "
              "que declaran acerca de su perdición, cuando fueron asesinados en "
              "los días de los pecadores.",
    (22, 13): "Y ésta fue creada para los espíritus de los hombres que no serán "
              "justos, sino pecadores e impíos, y estarán con los inicuos. Y sus "
              "espíritus —porque los que aquí fueron afligidos son castigados "
              "menos— no serán castigados en el día del juicio, ni serán "
              "llevados de aquí».",
    (22, 14): "Entonces bendije al Señor de la gloria y dije: «Bendito eres, "
              "Señor, el que gobierna la justicia del […]».",

    # --- 23. El fuego que persigue a las lumbreras -------------------------
    (23, 1): "Y de allí recorrí hasta otro lugar, hacia los confines de la "
             "tierra.",
    (23, 2): "Y contemplé un fuego que corría y no descansaba ni cesaba de su "
             "carrera, ni de día ni de noche, sino que seguía igual.",
    (23, 3): "Y pregunté diciendo: «¿Qué es esto, que no tiene descanso?».",
    (23, 4): "Entonces me respondió Raguel, uno de los santos ángeles que estaba "
             "conmigo: «Esta carrera del fuego, el fuego que va hacia el "
             "occidente, es el que persigue a todas las lumbreras del cielo».",

    # --- 24. Los siete montes y el árbol de la fragancia -------------------
    (24, 1): "Y me mostró montes de fuego que arden […] de noche.",
    (24, 2): "Y pasé más allá de ellos y contemplé siete montes, todos distintos "
             "uno de otro, cuyas piedras eran de hermosura, y todos honrosos y "
             "gloriosos y de buen aspecto: tres hacia el oriente, afirmados uno "
             "sobre otro, y tres hacia el sur, uno sobre otro; y valles hondos y "
             "ásperos, que no se tocan entre sí.",
    (24, 3): "Y había un séptimo monte en medio de éstos, y sobrepasaba en "
             "altura, como el asiento de un trono; y lo rodeaban árboles "
             "olorosos.",
    (24, 4): "Y había entre ellos un árbol como nunca he olido, ni ningún otro, "
             "y nada hay semejante a él: tenía un olor más fragante que los "
             "aromas, y lo mismo sus hojas y su flor; y el árbol no se marchita "
             "jamás. Y sus frutos eran como racimos de palmera.",
    (24, 6): "Entonces respondió Miguel, uno de los santos ángeles, que iba "
             "conmigo guiándome.",

    # --- 25. El trono de Dios y el fruto reservado a los justos -----------
    (25, 1): "Y me dijo: «Enoc, ¿qué preguntas? ¿Y de qué te maravillaste en el "
             "olor del árbol, y por qué quieres aprender la verdad?».",
    (25, 2): "Entonces le respondí: «De todo quiero saber, pero sobre todo, y "
             "muchísimo, acerca de este árbol».",
    (25, 3): "Y respondió diciendo: «Este monte alto, cuya cima es semejante a "
             "un trono, es el asiento de Dios, donde el gran Señor, el Santo de "
             "la gloria, el Rey del siglo, se sentará cuando descienda a visitar "
             "la tierra para bien.",
    (25, 4): "Y este árbol de fragancia: ninguna carne tiene potestad de tocarlo "
             "hasta el juicio, en el que habrá venganza de todos y consumación "
             "para siempre. Entonces será dado a los justos y a los santos",
    (25, 5): "su fruto, a los escogidos, para vida, por alimento; y será "
             "trasplantado a un lugar santo, junto a la casa de Dios, Rey del "
             "siglo.",
    (25, 6): "Entonces se alegrarán con gozo y se regocijarán y entrarán en el "
             "santuario. Su fragancia estará en sus huesos, y vivirán sobre la "
             "tierra una vida más larga que la que vivieron tus padres; y en sus "
             "días, penas y tormentos y plagas y azotes no los tocarán».",
    (25, 7): "Entonces bendije al Dios de la gloria, al Rey del siglo, que "
             "preparó tales cosas para los hombres justos, y las creó, y dijo "
             "que se les diesen.",

    # --- 26. El centro de la tierra y el valle --------------------------
    (26, 1): "Y de allí recorrí hasta el centro de la tierra, y vi un lugar "
             "bendito en el que había árboles con retoños que permanecen y "
             "brotan del árbol cortado.",
    (26, 2): "Y allí contemplé un monte santo; debajo del monte, agua que venía "
             "del oriente y cuyo curso iba hacia el sur.",
    (26, 3): "Y vi hacia el oriente otro monte más alto que éste, y entre ellos "
             "un valle hondo que no tenía anchura; y por él corre el agua, por "
             "debajo del monte.",
    (26, 5): "Y todos los valles son hondos, de roca maciza, y no se plantaba "
             "árbol en ellos.",
    (26, 6): "Y me maravillé del valle, y me maravillé mucho.",

    # --- 27. El valle maldito, y la bendición de los piadosos -------------
    (27, 1): "Y dije: «¿Por qué esta tierra es bendita y toda llena de árboles, "
             "y este valle en cambio está maldito?» […]",
    (27, 2): "[…] tierra maldita para los malditos es, para siempre. Aquí se "
             "reunirán todos los que digan con su boca palabra indecorosa contra "
             "el Señor y hablen cosas duras acerca de su gloria. Aquí se "
             "reunirán, y aquí estará su morada",
    (27, 3): "en los últimos siglos [en los días del juicio verdadero], delante "
             "de los justos, por todo el tiempo. Aquí bendecirán los piadosos al "
             "Señor de la gloria, al Rey del siglo,",
    (27, 4): "en los días de su juicio lo bendecirán, por la misericordia con "
             "que les repartió.",
    (27, 5): "Entonces bendije al Señor de la gloria, y declaré su gloria, y lo "
             "alabé magníficamente.",
    # --- 28 a 31. El viaje hacia el oriente, por los montes de los aromas ---
    (28, 1): "Y de allí fui hacia el centro de Mandóbara, y lo vi desierto y "
             "solitario, lleno de árboles;",
    (28, 2): "y de las semillas, agua sin lluvia que venía desde arriba,",
    (28, 3): "como un acueducto abundante: hacia el norte y hacia el occidente, "
             "por todas partes hace subir agua y rocío.",
    (29, 1): "Y de allí fui a otro lugar, en el Bábdera; y me dirigí hacia el "
             "oriente de aquel monte,",
    (30, 1): "y más allá de éstos me fui lejos hacia el oriente, y vi otro lugar "
             "grande, un valle de agua,",
    (30, 2): "en el que había un árbol con el verdor de aromas semejantes al "
             "lentisco;",
    (30, 3): "y junto a las orillas de éstos vi el aroma del cinamomo. Y más "
             "allá de éstos, hacia el oriente.",
    (31, 1): "Y vi otros montes, y en ellos bosques de árboles, y salía de ellos "
             "el néctar llamado sarrán, y el gálbano.",
    (31, 2): "Y más allá de estos montes vi otro monte hacia el oriente de los "
             "confines de la tierra, y todos los árboles llenos […] a semejanza "
             "de almendros,",
    (31, 3): "cuando se restriegan; y por eso su aroma es más fragante.",

    # --- 32. El paraíso de la justicia y el árbol de la prudencia ----------
    (32, 1): "[…] hacia el norte, al oriente, contemplé siete montes llenos de "
             "nardo fino y de lentisco y de cinamomo y de pimienta.",
    (32, 2): "Y de allí recorrí hasta Tasarcas, muy lejos de todos éstos, hacia "
             "el oriente de la tierra; y pasé por encima del mar Rojo y me fui a "
             "Acrón, y de allí pasé por encima de Zotiel.",
    (32, 3): "Y llegué al paraíso de la justicia, y vi de lejos, más allá de "
             "aquellos árboles, árboles más numerosos y grandes que crecían "
             "allí, muy hermosos y gloriosos y magníficos; y el árbol de la "
             "prudencia, del cual comen [los santos] […] y conocen gran "
             "prudencia.",
    (32, 4): "Aquel árbol era semejante al pino en su altura, y sus hojas "
             "semejantes a las del algarrobo; su fruto, como racimos de vid, muy "
             "alegres; y su olor llegaba lejos desde el árbol.",
    (32, 5): "Entonces dije: «¡Qué hermoso es este árbol, y qué grato a la "
             "vista!».",
    (32, 6): "Entonces respondió Rafael, el santo ángel que estaba conmigo: "
             "«Éste es el árbol de la prudencia, del cual comió tu padre […]».",
}
