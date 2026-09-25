"""Ignacio de Antioquía a los Romanos, traducida del griego.

La más famosa de las siete. Ignacio ruega a los cristianos de Roma que no hagan
nada por librarlo de la muerte: «Trigo soy de Dios, y por los dientes de las
fieras he de ser molido, para ser hallado pan puro de Cristo» (4).

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_ROMANOS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la que ha alcanzado "
            "misericordia en la magnificencia del Padre altísimo y de "
            "Jesucristo, su único Hijo; a la iglesia amada e iluminada por la "
            "voluntad de Aquel que ha querido todas las cosas que existen, "
            "según el amor de Jesucristo, nuestro Dios; la cual también "
            "preside en el lugar de la región de los romanos, digna de Dios, "
            "digna de honra, digna de ser llamada bienaventurada, digna de "
            "alabanza, digna de alcanzar su deseo, digna en pureza, y que "
            "preside en el amor, que lleva el nombre de Cristo, que lleva el "
            "nombre del Padre; a la cual también saludo en el nombre de "
            "Jesucristo, Hijo del Padre; a los que según la carne y el "
            "espíritu están unidos a todo mandamiento suyo, llenos de la "
            "gracia de Dios sin división, y purificados de todo color "
            "extraño: salud abundantísima e irreprochable en Jesucristo, "
            "nuestro Dios.",
    (1, 1): "Puesto que, por mis ruegos a Dios, he alcanzado ver vuestros "
            "rostros dignos de Dios, como aun pedía obtener más —porque atado "
            "en Cristo Jesús espero saludaros, si es voluntad que yo sea "
            "tenido por digno de llegar hasta el fin—;",
    (1, 2): "porque el principio está bien dispuesto, si es que alcanzo la "
            "gracia de recibir sin estorbo mi herencia. Porque temo vuestro "
            "amor, no sea que él mismo me haga daño. Porque a vosotros os es "
            "fácil hacer lo que queráis; pero a mí me es difícil alcanzar a "
            "Dios, si vosotros no me perdonáis.",

    # Capítulo 2
    (2, 1): "Porque no quiero que agradéis a los hombres, sino que agradéis a "
            "Dios, como ya le agradáis. Porque ni yo tendré jamás ocasión "
            "semejante de alcanzar a Dios, ni vosotros, si calláis, podréis "
            "firmar con vuestro nombre obra mejor. Porque si calláis acerca "
            "de mí, yo seré palabra de Dios; pero si amáis mi carne, otra vez "
            "seré una voz.",
    (2, 2): "No me procuréis otra cosa que ser derramado en libación a Dios, "
            "mientras todavía hay un altar preparado, para que, hechos un "
            "coro en el amor, cantéis al Padre en Cristo Jesús, porque Dios "
            "se ha dignado que el obispo de Siria fuese hallado en el "
            "poniente, habiéndolo hecho venir desde el oriente. Hermoso es "
            "ponerse del mundo hacia Dios, para en él amanecer.",

    # Capítulo 3
    (3, 1): "Nunca envidiasteis a nadie; a otros enseñasteis. Y yo quiero que "
            "también sean firmes aquellas cosas que mandáis cuando instruís a "
            "los discípulos.",
    (3, 2): "Pedid solamente para mí fuerza interior y exterior, para que no "
            "sólo hable, sino también quiera; para que no sólo me llame "
            "cristiano, sino que también sea hallado tal. Porque si soy "
            "hallado tal, también podré ser llamado así, y entonces ser fiel, "
            "cuando ya no aparezca al mundo.",
    (3, 3): "Nada de lo que se ve es bueno; porque nuestro Dios Jesucristo, "
            "estando en el Padre, se manifiesta más. No es obra de "
            "persuasión, sino de grandeza, el cristianismo, cuando es "
            "aborrecido por el mundo.",

    # Capítulo 4
    (4, 1): "Yo escribo a todas las iglesias, y a todas encargo que yo muero "
            "de buen grado por Dios, si vosotros no lo impedís. Os ruego que "
            "no tengáis para conmigo una benevolencia inoportuna. Dejadme ser "
            "pasto de las fieras, por medio de las cuales me es dado alcanzar "
            "a Dios. Trigo soy de Dios, y por los dientes de las fieras he de "
            "ser molido, para ser hallado pan puro de Cristo.",
    (4, 2): "Antes bien, halagad a las fieras, para que se me vuelvan "
            "sepulcro y no dejen nada de mi cuerpo, para que, una vez "
            "dormido, no sea gravoso a nadie. Entonces seré verdaderamente "
            "discípulo de Jesucristo, cuando el mundo no vea ni siquiera mi "
            "cuerpo. Suplicad a Cristo por mí, para que por medio de estos "
            "instrumentos sea hallado sacrificio.",
    (4, 3): "No os mando como Pedro y Pablo. Ellos eran apóstoles; yo, un "
            "condenado. Ellos, libres; yo, hasta ahora, esclavo. Pero si "
            "padezco, seré liberto de Jesucristo, y resucitaré en él libre. "
            "Ahora aprendo, atado, a no desear nada.",

    # Capítulo 5
    (5, 1): "Desde Siria hasta Roma lucho con las fieras, por tierra y por "
            "mar, de noche y de día, atado a diez leopardos, que son una "
            "escuadra de soldados; los cuales, aun cuando se les hace bien, "
            "se vuelven peores. Pero con sus injurias soy más discípulo; mas "
            "no por eso estoy justificado.",
    (5, 2): "¡Ojalá goce yo de las fieras que me están preparadas! Y ruego "
            "que se muestren prontas conmigo; y aun las halagaré para que me "
            "devoren prontamente, no como a algunos a quienes, por miedo, no "
            "tocaron. Y si ellas de mala gana no quisieren, yo las forzaré.",
    (5, 3): "Perdonadme: lo que me conviene, yo lo sé. Ahora comienzo a ser "
            "discípulo. Que nada de lo visible ni de lo invisible me envidie, "
            "para que alcance a Jesucristo. Fuego y cruz, manadas de fieras, "
            "desgarramientos, descoyuntamientos, dispersión de huesos, "
            "mutilación de miembros, trituración de todo el cuerpo, los "
            "tormentos malvados del diablo vengan sobre mí, con tal que "
            "alcance a Jesucristo.",

    # Capítulo 6
    (6, 1): "De nada me aprovecharán los confines del mundo ni los reinos de "
            "este siglo. Mejor es para mí morir en Cristo Jesús que reinar "
            "sobre los confines de la tierra. A aquél busco, al que murió por "
            "nosotros; a aquél quiero, al que por nosotros resucitó. Mi parto "
            "está inminente.",
    (6, 2): "Perdonadme, hermanos: no me impidáis vivir, no queráis que yo "
            "muera; al que quiere ser de Dios no lo entreguéis al mundo, ni "
            "lo seduzcáis con la materia. Dejadme recibir la luz pura; "
            "llegado allí, seré hombre.",
    (6, 3): "Permitidme ser imitador de la pasión de mi Dios. Si alguno le "
            "tiene en sí mismo, comprenda lo que quiero, y compadézcase de "
            "mí, sabiendo lo que me apremia.",

    # Capítulo 7
    (7, 1): "El príncipe de este siglo quiere arrebatarme y corromper mi "
            "propósito dirigido a Dios. Que ninguno, pues, de los que estáis "
            "ahí le ayude; antes bien, sed de mi parte, es decir, de la de "
            "Dios. No habléis de Jesucristo mientras deseáis el mundo.",
    (7, 2): "Que la envidia no habite entre vosotros. Aunque yo mismo, "
            "estando presente, os suplique, no me hagáis caso; creed más bien "
            "a esto que os escribo. Porque vivo os escribo, enamorado de "
            "morir. Mi amor está crucificado, y no hay en mí fuego que ame la "
            "materia, sino agua viva que habla dentro de mí y me dice desde "
            "lo íntimo: Ven al Padre.",
    (7, 3): "No me deleito en el alimento corruptible ni en los placeres de "
            "esta vida. Pan de Dios quiero, que es la carne de Jesucristo, el "
            "del linaje de David; y por bebida quiero su sangre, que es amor "
            "incorruptible.",

    # Capítulo 8
    (8, 1): "Ya no quiero vivir según los hombres. Y esto será, si vosotros "
            "lo queréis. Quered, para que también vosotros seáis queridos.",
    (8, 2): "Con pocas letras os lo ruego: creedme. Y Jesucristo os "
            "manifestará estas cosas, que digo la verdad; él, la boca sin "
            "mentira, por la cual el Padre ha hablado en verdad.",
    (8, 3): "Pedid por mí, para que lo alcance. No os he escrito según la "
            "carne, sino según el sentir de Dios. Si padezco, me habréis "
            "querido; si soy rechazado, me habréis aborrecido.",

    # Capítulo 9
    (9, 1): "Acordaos en vuestra oración de la iglesia que está en Siria, la "
            "cual, en lugar de mí, tiene a Dios por pastor. Sólo Jesucristo "
            "será su obispo, y vuestro amor.",
    (9, 2): "Pero yo me avergüenzo de ser contado entre ellos, porque no soy "
            "digno, siendo el último de ellos y un abortivo; mas he alcanzado "
            "misericordia para ser alguien, si alcanzo a Dios.",
    (9, 3): "Os saluda mi espíritu y el amor de las iglesias que me "
            "recibieron en el nombre de Jesucristo, no como a un transeúnte. "
            "Porque aun las que no estaban en mi camino según la carne me "
            "precedían de ciudad en ciudad.",

    # Capítulo 10
    (10, 1): "Os escribo esto desde Esmirna, por medio de los efesios, dignos "
             "de ser llamados bienaventurados. Está también conmigo, con "
             "otros muchos, Croco, nombre muy querido para mí.",
    (10, 2): "En cuanto a los que me precedieron desde Siria a Roma para "
             "gloria de Dios, creo que ya los conocéis; hacedles saber que "
             "estoy cerca. Porque todos son dignos de Dios y de vosotros; y "
             "os conviene confortarlos en todo.",
    (10, 3): "Os escribí esto el día noveno antes de las calendas de "
             "septiembre. Pasadlo bien hasta el fin en la paciencia de "
             "Jesucristo.",
}
