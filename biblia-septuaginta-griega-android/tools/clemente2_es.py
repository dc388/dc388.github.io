"""La llamada Segunda carta de Clemente, traducida del griego.

No es una carta ni es de Clemente: es una homilía, la más antigua que se
conserva entera, predicada hacia mediados del siglo II. Se transmitió junto a
la Primera y de ahí le viene el nombre. Exhorta al arrepentimiento y cita
dichos de Jesús que no están en los evangelios canónicos.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

CLEMENTE2_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "Hermanos, así debemos pensar de Jesucristo, como de Dios, como "
            "del juez de vivos y muertos; y no debemos pensar poca cosa de "
            "nuestra salvación.",
    (1, 2): "Porque si pensamos poca cosa de él, poca cosa esperamos también "
            "recibir; y los que oyen como si se tratara de cosas pequeñas "
            "pecan, y nosotros pecamos no sabiendo de dónde fuimos llamados, "
            "y por quién, y a qué lugar, y cuántas cosas soportó Jesucristo "
            "padecer por causa de nosotros.",
    (1, 3): "¿Qué recompensa, pues, le daremos nosotros, o qué fruto digno de "
            "lo que él mismo nos dio? ¿Y cuántos deberes santos le debemos?",
    (1, 4): "Porque él nos concedió la luz; como padre nos llamó hijos; "
            "cuando perecíamos, nos salvó.",
    (1, 5): "¿Qué alabanza, pues, le daremos, o qué pago en recompensa de lo "
            "que hemos recibido?",
    (1, 6): "Estábamos ciegos en el entendimiento, adorando piedras y leños, "
            "y oro y plata y bronce, obras de hombres; y toda nuestra vida no "
            "era otra cosa sino muerte. Envueltos, pues, en oscuridad, y "
            "llenos de tal niebla en la vista, recobramos la vista, "
            "deponiendo por su voluntad aquella nube que nos envolvía.",
    (1, 7): "Porque tuvo misericordia de nosotros, y movido a compasión nos "
            "salvó, habiendo visto en nosotros mucho error y perdición, y que "
            "no teníamos ninguna esperanza de salvación, sino la que viene de "
            "él.",
    (1, 8): "Porque nos llamó cuando no éramos, y quiso que de lo que no era "
            "llegásemos a ser.",

    # Capítulo 2
    (2, 1): "Alégrate, estéril, la que no daba a luz; prorrumpe y clama, la "
            "que no estaba de parto; porque más son los hijos de la "
            "desamparada que los de la que tiene marido. Lo que dijo: "
            "Alégrate, estéril, la que no daba a luz, por nosotros lo dijo; "
            "porque estéril era nuestra iglesia antes que le fuesen dados "
            "hijos.",
    (2, 2): "Y lo que dijo: Clama, la que no estaba de parto, esto quiere "
            "decir: que elevemos nuestras oraciones con sencillez a Dios, y "
            "que no desfallezcamos como las que están de parto.",
    (2, 3): "Y lo que dijo: Porque más son los hijos de la desamparada que "
            "los de la que tiene marido, es porque nuestro pueblo parecía "
            "estar desamparado de Dios; mas ahora, habiendo creído, hemos "
            "llegado a ser más que los que parecían tener a Dios.",
    (2, 4): "Y otra Escritura dice también: No he venido a llamar a justos, "
            "sino a pecadores.",
    (2, 5): "Esto quiere decir que es menester salvar a los que se pierden.",
    (2, 6): "Porque lo grande y admirable es esto: no afirmar lo que está en "
            "pie, sino lo que cae.",
    (2, 7): "Así también Cristo quiso salvar lo que se perdía, y salvó a "
            "muchos, viniendo y llamándonos a nosotros, que ya nos perdíamos.",

    # Capítulo 3
    (3, 1): "Habiendo, pues, usado él de tanta misericordia para con "
            "nosotros, primeramente, que nosotros los vivos no sacrificamos a "
            "los dioses muertos ni los adoramos, sino que por él hemos "
            "conocido al Padre de la verdad, ¿cuál es el conocimiento que se "
            "tiene de él, sino no negar a aquel por quien lo hemos conocido?",
    (3, 2): "Y él mismo dice también: Al que me confesare delante de los "
            "hombres, yo también le confesaré delante de mi Padre.",
    (3, 3): "Esta es, pues, nuestra recompensa, si confesamos a aquel por "
            "quien fuimos salvos.",
    (3, 4): "¿Y en qué le confesamos? En hacer lo que dice, y en no desoír "
            "sus mandamientos, y en no honrarle solamente con los labios, "
            "sino de todo corazón y de toda la mente.",
    (3, 5): "Y dice también en Isaías: Este pueblo con los labios me honra, "
            "mas su corazón lejos está de mí.",

    # Capítulo 4
    (4, 1): "No le llamemos, pues, solamente Señor, porque esto no nos "
            "salvará.",
    (4, 2): "Porque dice: No todo el que me dice: Señor, Señor, será salvo, "
            "sino el que hace la justicia.",
    (4, 3): "Así que, hermanos, confesémosle en las obras, en amarnos los "
            "unos a los otros, en no adulterar, ni murmurar unos de otros, ni "
            "tener envidia, sino en ser continentes, misericordiosos, buenos; "
            "y debemos compadecernos los unos de los otros, y no ser avaros. "
            "En estas obras confesémosle, y no en las contrarias.",
    (4, 4): "Y no debemos temer más a los hombres, sino a Dios.",
    (4, 5): "Por esto, si hacéis estas cosas, dijo el Señor: Aunque "
            "estuvieseis reunidos conmigo en mi seno, si no hacéis mis "
            "mandamientos, os echaré fuera y os diré: Apartaos de mí, no sé "
            "de dónde sois, obradores de iniquidad.",

    # Capítulo 5
    (5, 1): "Por tanto, hermanos, dejando nuestra peregrinación en este "
            "mundo, hagamos la voluntad del que nos llamó, y no temamos salir "
            "de este mundo.",
    (5, 2): "Porque dice el Señor: Seréis como corderos en medio de lobos.",
    (5, 3): "Y respondiendo Pedro, le dice: ¿Y si los lobos despedazan a los "
            "corderos?",
    (5, 4): "Dijo Jesús a Pedro: No teman los corderos a los lobos después de "
            "muertos; y vosotros no temáis a los que os matan y nada más "
            "pueden haceros, sino temed a aquel que, después que hayáis "
            "muerto, tiene poder sobre el alma y el cuerpo para echarlos en "
            "la gehena de fuego.",
    (5, 5): "Y sabed, hermanos, que la estancia de esta carne en este mundo "
            "es pequeña y de poco tiempo, mas la promesa de Cristo es grande "
            "y admirable, y es el reposo del reino venidero y de la vida "
            "eterna.",
    (5, 6): "¿Qué hemos, pues, de hacer para alcanzar estas cosas, sino "
            "conducirnos santa y justamente, y tener estas cosas del mundo "
            "por ajenas, y no codiciarlas?",
    (5, 7): "Porque al codiciar adquirir estas cosas, caemos del camino de la "
            "justicia.",

    # Capítulo 6
    (6, 1): "Y dice el Señor: Ningún siervo puede servir a dos señores. Si "
            "nosotros queremos servir a Dios y a Mamón, no nos es provechoso.",
    (6, 2): "Porque ¿qué aprovecha si alguno gana todo el mundo, y pierde su "
            "alma?",
    (6, 3): "Y este siglo y el venidero son dos enemigos.",
    (6, 4): "Este predica adulterio y corrupción, y avaricia y engaño; aquel "
            "renuncia a estas cosas.",
    (6, 5): "No podemos, pues, ser amigos de los dos; mas debemos, "
            "renunciando a este, tener trato con aquel.",
    (6, 6): "Pensamos que es mejor aborrecer las cosas de aquí, porque son "
            "pequeñas, y de poco tiempo, y corruptibles, y amar aquellas, los "
            "bienes incorruptibles.",
    (6, 7): "Porque haciendo la voluntad de Cristo hallaremos reposo; pero si "
            "no, nada nos librará del castigo eterno, si desoímos sus "
            "mandamientos.",
    (6, 8): "Y dice también la Escritura en Ezequiel que, aunque se levanten "
            "Noé, y Job, y Daniel, no librarán a sus hijos en la cautividad.",
    (6, 9): "Y si aun tales justos no pueden con sus justicias librar a sus "
            "hijos, nosotros, si no guardamos el bautismo puro y sin mancha, "
            "¿con qué confianza entraremos en el reino de Dios? ¿O quién será "
            "nuestro abogado, si no somos hallados teniendo obras santas y "
            "justas?",

    # Capítulo 7
    (7, 1): "Así que, hermanos míos, luchemos, sabiendo que la lucha está a "
            "la mano, y que a las luchas corruptibles acuden muchos "
            "navegando, pero no todos son coronados, sino los que mucho han "
            "trabajado y bien han luchado.",
    (7, 2): "Luchemos, pues, nosotros, para que todos seamos coronados.",
    (7, 3): "Así que corramos por el camino recto, la lucha incorruptible, y "
            "acudamos muchos a ella navegando, y luchemos, para que también "
            "seamos coronados; y si no podemos todos ser coronados, lleguemos "
            "al menos cerca de la corona.",
    (7, 4): "Debemos saber que el que lucha en la lucha corruptible, si es "
            "hallado haciendo trampa, es azotado, levantado y echado fuera "
            "del estadio.",
    (7, 5): "¿Qué os parece? El que corrompe la lucha de la incorrupción, "
            "¿qué padecerá?",
    (7, 6): "Porque de los que no guardaron el sello, dice: Su gusano no "
            "morirá, y su fuego nunca se apagará, y serán espectáculo para "
            "toda carne.",

    # Capítulo 8
    (8, 1): "Mientras estamos, pues, en la tierra, arrepintámonos.",
    (8, 2): "Porque somos barro en la mano del artífice; pues de la manera "
            "que el alfarero, si hace una vasija y se le tuerce o se le "
            "quiebra en las manos, vuelve a formarla de nuevo, pero si se ha "
            "adelantado a echarla en el horno de fuego, ya no podrá "
            "remediarla, así también nosotros, mientras estamos en este "
            "mundo, arrepintámonos de todo corazón de las maldades que hemos "
            "hecho en la carne, para que seamos salvos por el Señor mientras "
            "tenemos tiempo de arrepentimiento.",
    (8, 3): "Porque después que hayamos salido del mundo, ya no podremos allí "
            "confesarnos ni arrepentirnos más.",
    (8, 4): "Así que, hermanos, haciendo la voluntad del Padre, y guardando "
            "pura la carne, y observando los mandamientos del Señor, "
            "recibiremos la vida eterna.",
    (8, 5): "Porque dice el Señor en el evangelio: Si lo pequeño no "
            "guardasteis, ¿quién os dará lo grande? Porque os digo que el que "
            "es fiel en lo muy poco, también en lo mucho es fiel.",
    (8, 6): "Esto, pues, quiere decir: Guardad pura la carne, y sin mancha el "
            "sello, para que recibamos la vida eterna.",

    # Capítulo 9
    (9, 1): "Y ninguno de vosotros diga que esta carne no es juzgada ni "
            "resucita.",
    (9, 2): "Sabed: ¿en qué fuisteis salvos, en qué recobrasteis la vista, "
            "sino estando en esta carne?",
    (9, 3): "Debemos, pues, guardar la carne como templo de Dios.",
    (9, 4): "Porque de la manera que en la carne fuisteis llamados, también "
            "en la carne vendréis.",
    (9, 5): "Si Cristo, el Señor que nos salvó, siendo primero espíritu, se "
            "hizo carne, y así nos llamó, así también nosotros en esta carne "
            "recibiremos la recompensa.",
    (9, 6): "Amémonos, pues, los unos a los otros, para que todos lleguemos "
            "al reino de Dios.",
    (9, 7): "Mientras tenemos tiempo de ser sanados, entreguémonos a Dios que "
            "nos sana, dándole recompensa.",
    (9, 8): "¿Cuál? El arrepentirnos de corazón sincero.",
    (9, 9): "Porque él conoce de antemano todas las cosas, y sabe lo que hay "
            "en nuestro corazón.",
    (9, 10): "Démosle, pues, alabanza, no solo con la boca, sino también con "
             "el corazón, para que nos reciba como a hijos.",
    (9, 11): "Porque también dijo el Señor: Mis hermanos son estos que hacen "
             "la voluntad de mi Padre.",

    # Capítulo 10
    (10, 1): "Así que, hermanos míos, hagamos la voluntad del Padre que nos "
             "llamó, para que vivamos; y sigamos más bien la virtud, y "
             "dejemos la maldad como precursora de nuestros pecados, y "
             "huyamos de la impiedad, no sea que nos alcancen los males.",
    (10, 2): "Porque si procuramos hacer el bien, la paz nos seguirá.",
    (10, 3): "Porque por esta causa no es posible que el hombre la halle: "
             "porque hay quienes introducen temores humanos, prefiriendo el "
             "deleite de aquí antes que la promesa venidera.",
    (10, 4): "Porque no saben cuán gran tormento trae el deleite de aquí, y "
             "qué delicias trae la promesa venidera.",
    (10, 5): "Y si ellos solos hicieran estas cosas, sería tolerable; mas "
             "ahora perseveran en enseñar el mal a las almas inocentes, no "
             "sabiendo que tendrán doble condenación, así ellos como los que "
             "los oyen.",

    # Capítulo 11
    (11, 1): "Sirvamos, pues, nosotros a Dios con corazón limpio, y seremos "
             "justos; pero si no le servimos, por no creer a la promesa de "
             "Dios, seremos miserables.",
    (11, 2): "Porque dice también la palabra profética: Miserables son los de "
             "doble ánimo, los que dudan en su corazón, los que dicen: Estas "
             "cosas ya las oímos antiguamente, y en tiempo de nuestros "
             "padres, y nosotros, esperando día tras día, nada de esto hemos "
             "visto.",
    (11, 3): "¡Insensatos! Comparaos a un árbol; tomad la vid: primero pierde "
             "la hoja, luego nace el brote, después el agraz, y luego el "
             "racimo maduro.",
    (11, 4): "Así también mi pueblo tuvo desórdenes y aflicciones; después "
             "recibirá los bienes.",
    (11, 5): "Así que, hermanos míos, no seamos de doble ánimo, sino "
             "esperando perseveremos, para que recibamos también la "
             "recompensa.",
    (11, 6): "Porque fiel es el que prometió dar a cada uno la recompensa de "
             "sus obras.",
    (11, 7): "Si hacemos, pues, la justicia delante de Dios, entraremos en su "
             "reino y recibiremos las promesas, que oído no oyó, ni ojo vio, "
             "ni han subido en corazón de hombre.",

    # Capítulo 12
    (12, 1): "Esperemos, pues, a cada hora el reino de Dios en amor y "
             "justicia, ya que no sabemos el día de la manifestación de Dios.",
    (12, 2): "Porque habiéndole preguntado alguno al Señor mismo cuándo "
             "vendría su reino, dijo: Cuando los dos sean uno, y lo de fuera "
             "como lo de dentro, y el varón con la mujer, ni varón ni mujer.",
    (12, 3): "Y los dos son uno cuando nos hablamos verdad unos a otros, y en "
             "dos cuerpos hay sin fingimiento una sola alma.",
    (12, 4): "Y lo de fuera como lo de dentro quiere decir esto: lo de dentro "
             "llama al alma, y lo de fuera llama al cuerpo. De la manera, "
             "pues, que tu cuerpo se ve, así también sea tu alma manifiesta "
             "en las buenas obras.",
    (12, 5): "Y el varón con la mujer, ni varón ni mujer, quiere decir esto: "
             "que el hermano, al ver a una hermana, no piense de ella nada "
             "femenino, ni ella piense nada masculino de él.",
    (12, 6): "Si hacéis estas cosas, dice, vendrá el reino de mi Padre.",

    # Capítulo 13
    (13, 1): "Hermanos, pues, arrepintámonos ya de una vez; seamos sobrios "
             "para el bien, porque estamos llenos de mucha necedad y maldad. "
             "Borremos de nosotros los pecados pasados, y arrepintiéndonos de "
             "alma seamos salvos; y no seamos complacedores de los hombres, "
             "ni queramos agradarnos solamente a nosotros mismos, sino "
             "también a los hombres de fuera por la justicia, para que el "
             "nombre no sea blasfemado por causa de nosotros.",
    (13, 2): "Porque dice el Señor: Continuamente es blasfemado mi nombre "
             "entre todas las gentes; y otra vez: ¡Ay de aquel por cuya causa "
             "es blasfemado mi nombre! ¿En qué es blasfemado? En que no "
             "hacéis lo que yo quiero.",
    (13, 3): "Porque las gentes, oyendo de nuestra boca los oráculos de Dios, "
             "se maravillan de ellos como hermosos y grandes; luego, cuando "
             "conocen nuestras obras, que no son dignas de las palabras que "
             "decimos, se vuelven de ahí a la blasfemia, diciendo que es "
             "alguna fábula y engaño.",
    (13, 4): "Porque cuando oyen de nosotros que dice Dios: No tenéis mérito "
             "si amáis a los que os aman, sino que tenéis mérito si amáis a "
             "los enemigos y a los que os aborrecen; cuando oyen estas cosas, "
             "se maravillan de la excelencia de la bondad; mas cuando ven que "
             "no solo no amamos a los que aborrecen, sino que ni aun a los "
             "que aman, se burlan de nosotros, y es blasfemado el nombre.",

    # Capítulo 14
    (14, 1): "Así que, hermanos, haciendo la voluntad de nuestro Padre Dios, "
             "seremos de la iglesia primera, la espiritual, la que fue creada "
             "antes del sol y de la luna; pero si no hacemos la voluntad del "
             "Señor, seremos de aquellos de quienes habla la Escritura que "
             "dice: Mi casa ha sido hecha cueva de ladrones. Así que "
             "escojamos, pues, ser de la iglesia de la vida, para que seamos "
             "salvos.",
    (14, 2): "Y no creo que ignoréis que la iglesia viva es el cuerpo de "
             "Cristo; porque dice la Escritura: Hizo Dios al hombre varón y "
             "hembra; el varón es Cristo, la hembra es la iglesia; y además "
             "los libros y los apóstoles dicen que la iglesia no es de ahora, "
             "sino desde el principio. Porque era espiritual, como también "
             "nuestro Jesús, pero se manifestó en los postreros días para "
             "salvarnos.",
    (14, 3): "Y la iglesia, siendo espiritual, se manifestó en la carne de "
             "Cristo, mostrándonos que si alguno de nosotros la guarda en la "
             "carne y no la corrompe, la recibirá en el Espíritu Santo; "
             "porque esta carne es copia del espíritu; ninguno, pues, que "
             "haya corrompido la copia participará del original. Esto, pues, "
             "quiere decir, hermanos: Guardad la carne, para que participéis "
             "del espíritu.",
    (14, 4): "Y si decimos que la carne es la iglesia y el espíritu es "
             "Cristo, entonces el que ha ultrajado la carne ha ultrajado la "
             "iglesia. Este tal, pues, no participará del espíritu, que es "
             "Cristo.",
    (14, 5): "Tan grande vida e incorrupción puede recibir esta carne, "
             "estando unido a ella el Espíritu Santo, que nadie puede "
             "declarar ni decir lo que el Señor ha preparado para sus "
             "escogidos.",

    # Capítulo 15
    (15, 1): "Y no creo haber dado un consejo pequeño acerca de la "
             "continencia; el que lo siga no se arrepentirá, sino que se "
             "salvará a sí mismo y a mí, que le aconsejé. Porque no es "
             "pequeña recompensa hacer volver para salvación a un alma que "
             "anda errada y se pierde.",
    (15, 2): "Porque esta es la recompensa que podemos dar a Dios que nos "
             "creó: que el que habla y el que oye hable y oiga con fe y amor.",
    (15, 3): "Permanezcamos, pues, justos y santos en lo que hemos creído, "
             "para que con confianza pidamos a Dios, que dice: Aún estando tú "
             "hablando, diré: Heme aquí.",
    (15, 4): "Porque esta palabra es señal de una gran promesa; porque dice "
             "el Señor que él está más pronto a dar que el que pide a pedir.",
    (15, 5): "Participando, pues, de tan grande bondad, no nos neguemos a "
             "nosotros mismos el alcanzar tantos bienes. Porque cuanto placer "
             "traen estas palabras a los que las cumplen, tanta condenación "
             "traen a los que las desoyen.",

    # Capítulo 16
    (16, 1): "Así que, hermanos, habiendo recibido no pequeña ocasión para "
             "arrepentirnos, mientras tenemos tiempo, convirtámonos a Dios "
             "que nos llamó, mientras todavía tenemos a quien nos recibe.",
    (16, 2): "Porque si renunciamos a estos deleites, y vencemos a nuestra "
             "alma no haciendo sus malos deseos, participaremos de la "
             "misericordia de Jesús.",
    (16, 3): "Mas sabed que ya viene el día del juicio como horno encendido, "
             "y algunos de los cielos se derretirán, y toda la tierra como "
             "plomo que se derrite en el fuego; y entonces se manifestarán "
             "las obras ocultas y las manifiestas de los hombres.",
    (16, 4): "Buena es, pues, la limosna, como arrepentimiento del pecado; "
             "mejor es el ayuno que la oración, y la limosna que ambos; y el "
             "amor cubre multitud de pecados, y la oración de buena "
             "conciencia libra de la muerte. Bienaventurado todo aquel que es "
             "hallado lleno de estas cosas, porque la limosna viene a ser "
             "alivio del pecado.",

    # Capítulo 17
    (17, 1): "Arrepintámonos, pues, de todo corazón, para que ninguno de "
             "nosotros perezca. Porque si tenemos mandamientos de hacer "
             "también esto, de apartar a los hombres de los ídolos y de "
             "instruirlos, ¡cuánto más no debe perecer un alma que ya conoce "
             "a Dios!",
    (17, 2): "Ayudémonos, pues, unos a otros a conducir también a los débiles "
             "hacia el bien, para que todos seamos salvos, y convirtámonos y "
             "amonestémonos los unos a los otros.",
    (17, 3): "Y no parezca solamente ahora que creemos y atendemos, mientras "
             "somos amonestados por los presbíteros, sino que también, cuando "
             "nos hayamos retirado a casa, acordémonos de los mandamientos "
             "del Señor, y no nos dejemos arrastrar en sentido contrario por "
             "los deseos mundanos, sino que, acudiendo con más frecuencia, "
             "procuremos adelantar en los mandamientos del Señor, para que "
             "todos, sintiendo lo mismo, estemos reunidos para la vida.",
    (17, 4): "Porque dijo el Señor: Vengo a reunir a todas las gentes, tribus "
             "y lenguas. Y esto lo dice del día de su manifestación, cuando "
             "viniendo nos redimirá, a cada uno conforme a sus obras.",
    (17, 5): "Y verán su gloria y su poder los incrédulos, y se asombrarán al "
             "ver el reino del mundo en Jesús, diciendo: ¡Ay de nosotros, "
             "porque tú eras, y no lo sabíamos, y no creíamos, y no "
             "obedecíamos a los presbíteros que nos anunciaban acerca de "
             "nuestra salvación! Y su gusano no morirá, y su fuego nunca se "
             "apagará, y serán espectáculo para toda carne.",
    (17, 6): "Habla de aquel día del juicio, cuando verán a los que entre "
             "nosotros vivieron impíamente y tuvieron en poco los "
             "mandamientos de Jesucristo.",
    (17, 7): "Pero los justos que obraron bien, y soportaron los tormentos, y "
             "aborrecieron los deleites del alma, cuando contemplen a los que "
             "se desviaron y negaron a Jesús con palabras o con obras, cómo "
             "son castigados con terribles tormentos en fuego inextinguible, "
             "darán gloria a su Dios, diciendo: Habrá esperanza para el que "
             "ha servido a Dios de todo corazón.",

    # Capítulo 18
    (18, 1): "Seamos, pues, también nosotros de los que dan gracias, de los "
             "que han servido a Dios, y no de los impíos que son juzgados.",
    (18, 2): "Porque yo también, siendo del todo pecador, y no habiendo huido "
             "aún de la tentación, sino estando todavía en medio de los "
             "instrumentos del diablo, procuro seguir la justicia, para que "
             "pueda llegar siquiera cerca de ella, temiendo el juicio "
             "venidero.",

    # Capítulo 19
    (19, 1): "Así que, hermanos y hermanas, después del Dios de la verdad, os "
             "leo una exhortación para que atendáis a lo que está escrito, a "
             "fin de que os salvéis a vosotros mismos y al que lee entre "
             "vosotros. Porque os pido como recompensa que os arrepintáis de "
             "todo corazón, dándoos a vosotros mismos salvación y vida. "
             "Porque haciendo esto pondremos una meta a todos los jóvenes que "
             "quieren esforzarse en la piedad y en la bondad de Dios.",
    (19, 2): "Y no nos disgustemos ni nos indignemos, como necios, cuando "
             "alguno nos amonesta y nos convierte de la injusticia a la "
             "justicia. Porque a veces, haciendo el mal, no lo conocemos, a "
             "causa del doble ánimo y de la incredulidad que hay en nuestros "
             "pechos, y tenemos entenebrecido el entendimiento por los deseos "
             "vanos.",
    (19, 3): "Practiquemos, pues, la justicia, para que seamos salvos hasta "
             "el fin. Bienaventurados los que obedecen estos preceptos; "
             "aunque por poco tiempo padezcan males en este mundo, recogerán "
             "el fruto inmortal de la resurrección.",
    (19, 4): "No se entristezca, pues, el piadoso si en los tiempos presentes "
             "padece miseria; un tiempo bienaventurado le espera. Aquel, "
             "habiendo vuelto a vivir arriba con los padres, se regocijará en "
             "el siglo sin tristeza.",

    # Capítulo 20
    (20, 1): "Pero tampoco turbe vuestro entendimiento aquello de que vemos a "
             "los injustos enriquecerse, y a los siervos de Dios en "
             "estrechez.",
    (20, 2): "Creamos, pues, hermanos y hermanas: combatimos en la prueba del "
             "Dios vivo, y nos ejercitamos en la vida presente, para ser "
             "coronados en la venidera.",
    (20, 3): "Ninguno de los justos recibió pronto su fruto, sino que lo "
             "espera.",
    (20, 4): "Porque si Dios diese en breve a los justos su recompensa, al "
             "punto estaríamos ejercitándonos en el comercio y no en la "
             "piedad; porque pareceríamos ser justos, persiguiendo no lo "
             "piadoso, sino lo lucrativo. Y por esto el juicio divino castigó "
             "al espíritu que no era justo, y lo cargó de cadenas.",
    (20, 5): "Al único Dios invisible, Padre de la verdad, que nos envió al "
             "Salvador y Príncipe de la incorrupción, por medio del cual "
             "también nos manifestó la verdad y la vida celestial, a él sea "
             "la gloria por los siglos de los siglos. Amén. Epístola segunda "
             "de Clemente a los Corintios.",
}
