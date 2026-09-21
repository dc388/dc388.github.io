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

Faltan los capítulos que el Panopolitano no conserva —el 4 no está— y el libro
entero pasado el 32: eso solo sobrevive completo en etíope, y es otro trabajo.
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

}
