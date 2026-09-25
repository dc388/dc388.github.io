"""Ignacio de Antioquía a los Esmirniotas, traducida del griego.

Escrita desde Tróade. En el capítulo 8 aparece por primera vez en un texto la
expresión «la iglesia católica», es decir, universal. Se traduce literalmente.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_ESMIRNIOTAS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la iglesia de Dios Padre y "
            "del amado Jesucristo, que ha alcanzado misericordia en todo don, "
            "llena de fe y de amor, a la que no le falta ningún don, "
            "dignísima de Dios y portadora de santidad, la que está en "
            "Esmirna de Asia: en espíritu irreprensible y en la palabra de "
            "Dios, abundante salud.",
    (1, 1): "Glorifico a Jesucristo, el Dios que así os ha hecho sabios; "
            "porque he comprendido que estáis perfeccionados en una fe "
            "inconmovible, como clavados en la cruz del Señor Jesucristo en "
            "la carne y en el espíritu, y afianzados en el amor en la sangre "
            "de Cristo, plenamente convencidos acerca de nuestro Señor, que "
            "es verdaderamente del linaje de David según la carne, Hijo de "
            "Dios según la voluntad y el poder de Dios, nacido verdaderamente "
            "de una virgen, bautizado por Juan para que se cumpliese por él "
            "toda justicia;",
    (1, 2): "verdaderamente clavado por nosotros en la carne bajo Poncio "
            "Pilato y Herodes el tetrarca —de cuyo fruto somos nosotros, de "
            "su pasión bienaventurada por Dios—, para alzar un estandarte "
            "para los siglos por medio de la resurrección, para sus santos y "
            "fieles, sean de entre los judíos o de entre los gentiles, en el "
            "único cuerpo de su iglesia.",

    # Capítulo 2
    (2, 1): "Porque todas estas cosas padeció por nosotros, para que fuésemos "
            "salvos; y verdaderamente padeció, así como también "
            "verdaderamente se resucitó a sí mismo; no como dicen algunos "
            "incrédulos, que padeció en apariencia, siendo ellos mismos "
            "apariencia; y según piensan, así también les acontecerá, siendo "
            "incorpóreos y semejantes a demonios.",

    # Capítulo 3
    (3, 1): "Porque yo sé y creo que aun después de la resurrección estaba en "
            "la carne.",
    (3, 2): "Y cuando vino a los que estaban con Pedro, les dijo: «Tomad, "
            "palpadme y ved que no soy un demonio incorpóreo». Y al punto le "
            "tocaron y creyeron, unidos estrechamente a su carne y a su "
            "espíritu. Por esto también despreciaron la muerte, y fueron "
            "hallados por encima de la muerte.",
    (3, 3): "Y después de la resurrección comió y bebió con ellos como un ser "
            "de carne, aunque espiritualmente estaba unido al Padre.",

    # Capítulo 4
    (4, 1): "Os exhorto a estas cosas, amados, sabiendo que también vosotros "
            "pensáis así. Pero os prevengo contra las fieras con forma de "
            "hombre, a las cuales no sólo no debéis recibir, sino, si es "
            "posible, ni siquiera salirles al encuentro; sólo orad por ellos, "
            "por si de algún modo se arrepienten, lo cual es difícil; mas de "
            "esto tiene potestad Jesucristo, nuestra verdadera vida. ² Porque "
            "si estas cosas fueron hechas por nuestro Señor en apariencia, "
            "también yo estoy encadenado en apariencia. ¿Y por qué me he "
            "entregado yo mismo a la muerte, al fuego, a la espada, a las "
            "fieras? Pero cerca de la espada, cerca de Dios; entre las "
            "fieras, entre Dios; Sólo en el nombre de Jesucristo, para "
            "padecer juntamente con él, lo soporto todo, fortaleciéndome él, "
            "el hombre perfecto.",

    # Capítulo 5
    (5, 1): "Al cual algunos, por ignorancia, niegan, o más bien fueron "
            "negados por él, siendo abogados de la muerte más que de la "
            "verdad; a los cuales no persuadieron las profecías, ni la ley de "
            "Moisés, ni hasta ahora el evangelio, ni los padecimientos de "
            "cada uno de nosotros.",
    (5, 2): "Porque también acerca de nosotros piensan lo mismo. Porque ¿de "
            "qué me sirve que alguno me alabe a mí, si blasfema de mi Señor, "
            "no confesando que es portador de carne? Y el que esto dice le ha "
            "negado por completo, siendo portador de un cadáver.",
    (5, 3): "Y sus nombres, que son de incrédulos, no me ha parecido bien "
            "escribirlos. Antes, ni siquiera me acontezca acordarme de ellos, "
            "hasta que se arrepientan volviendo a la pasión, que es nuestra "
            "resurrección.",

    # Capítulo 6
    (6, 1): "Nadie se engañe: aun los seres celestiales, y la gloria de los "
            "ángeles, y los príncipes visibles e invisibles, si no creen en "
            "la sangre de Cristo, también para ellos hay juicio. El que pueda "
            "recibir esto, que lo reciba. Que el puesto no envanezca a nadie; "
            "porque el todo es la fe y el amor, a los cuales nada se "
            "antepone.",
    (6, 2): "Mas considerad a los que tienen opiniones ajenas acerca de la "
            "gracia de Jesucristo que vino a nosotros, cuán contrarios son al "
            "sentir de Dios. No les importa el amor, ni la viuda, ni el "
            "huérfano, ni el atribulado, ni el preso o el liberado, ni el "
            "hambriento o el sediento.",

    # Capítulo 7
    (7, 1): "Se apartan de la eucaristía y de la oración, porque no confiesan "
            "que la eucaristía es la carne de nuestro Salvador Jesucristo, la "
            "que padeció por nuestros pecados, la que el Padre, en su bondad, "
            "resucitó. Así pues, los que contradicen el don de Dios mueren en "
            "sus disputas. Mejor les fuera amar, para que también "
            "resucitasen.",
    (7, 2): "Conviene apartarse de los tales y no hablar de ellos ni en "
            "privado ni en público, sino atender a los profetas, y "
            "especialmente al evangelio, en el cual se nos ha manifestado la "
            "pasión y se ha consumado la resurrección. Y huid de las "
            "divisiones como principio de males.",

    # Capítulo 8
    (8, 1): "Seguid todos al obispo, como Jesucristo al Padre, y al "
            "presbiterio como a los apóstoles; y a los diáconos "
            "reverenciadlos como al mandamiento de Dios. Nadie haga sin el "
            "obispo nada de lo que concierne a la iglesia. Téngase por "
            "eucaristía válida la que se celebra bajo el obispo o bajo aquel "
            "a quien él la encomiende.",
    (8, 2): "Dondequiera que aparezca el obispo, allí esté la multitud; así "
            "como dondequiera que esté Jesucristo, allí está la iglesia "
            "católica. No es lícito sin el obispo ni bautizar ni celebrar el "
            "ágape; sino que lo que él apruebe, eso es también agradable a "
            "Dios, para que todo lo que hagáis sea seguro y firme.",

    # Capítulo 9
    (9, 1): "Es razonable, por lo demás, que volvamos a la sobriedad, "
            "mientras aún tenemos tiempo de arrepentirnos para con Dios. "
            "Bueno es conocer a Dios y al obispo. El que honra al obispo es "
            "honrado por Dios; el que hace algo a escondidas del obispo sirve "
            "al diablo.",
    (9, 2): "Abunde, pues, todo en vosotros en gracia, porque sois dignos. En "
            "todo me habéis confortado, y a vosotros Jesucristo. Ausente y "
            "presente me habéis amado. Vuestra recompensa es Dios, y "
            "soportándolo todo por él, le alcanzaréis.",

    # Capítulo 10
    (10, 1): "A Filón y a Reo Agatópode, que me siguieron por la palabra de "
             "Dios, hicisteis bien en recibirlos como a diáconos de Dios; los "
             "cuales también dan gracias al Señor por vosotros, porque los "
             "confortasteis de todas las maneras. Nada de ello se os perderá.",
    (10, 2): "Mi espíritu es rescate por el vuestro, y también mis cadenas, "
             "que no desdeñasteis ni os avergonzasteis de ellas. Tampoco se "
             "avergonzará de vosotros la esperanza perfecta, Jesucristo.",

    # Capítulo 11
    (11, 1): "Vuestra oración ha llegado a la iglesia que está en Antioquía "
             "de Siria, de donde vengo encadenado con cadenas dignísimas de "
             "Dios, y saludo a todos; no siendo digno de ser de allí, pues "
             "soy el último de ellos; mas por voluntad de Dios he sido tenido "
             "por digno, no por mi conciencia, sino por la gracia de Dios, la "
             "cual ruego que me sea dada perfecta, para que por vuestra "
             "oración alcance a Dios.",
    (11, 2): "Así pues, para que vuestra obra sea perfecta así en la tierra "
             "como en el cielo, conviene que vuestra iglesia elija a mano "
             "alzada, para honra de Dios, un embajador de Dios, que vaya "
             "hasta Siria a congratularse con ellos porque tienen paz y han "
             "recobrado su propia grandeza y les ha sido restituido su propio "
             "cuerpo.",
    (11, 3): "Me ha parecido, pues, cosa digna de Dios que enviéis a alguno "
             "de los vuestros con una carta, para que glorifique con ellos la "
             "bonanza que según Dios les ha sobrevenido, y que ya por vuestra "
             "oración habían alcanzado el puerto. Siendo perfectos, pensad "
             "también cosas perfectas; porque si queréis obrar bien, Dios "
             "está pronto a concedéroslo.",

    # Capítulo 12
    (12, 1): "Os saluda el amor de los hermanos que están en Tróade, desde "
             "donde también os escribo por medio de Burro, a quien enviasteis "
             "conmigo juntamente con los efesios, vuestros hermanos, el cual "
             "me ha confortado en todo. ¡Y ojalá todos le imitasen, pues es "
             "un ejemplar del ministerio de Dios! La gracia le recompensará "
             "en todo.",
    (12, 2): "Saludo al obispo, digno de Dios, y al presbiterio, digno de "
             "Dios, y a los diáconos, mis consiervos, y a todos, a cada uno "
             "en particular y en común, en el nombre de Jesucristo, y en su "
             "carne y en su sangre, en su pasión y resurrección, así carnal "
             "como espiritual, en la unidad de Dios y vuestra. Gracia a "
             "vosotros, misericordia, paz, paciencia en todo tiempo.",

    # Capítulo 13
    (13, 1): "Saludo a las casas de mis hermanos con sus mujeres e hijos, y a "
             "las vírgenes llamadas viudas. Estad bien en el poder del Padre. "
             "Os saluda Filón, que está conmigo.",
    (13, 2): "Saludo a la casa de Tavia, la cual ruego que esté afianzada en "
             "la fe y en el amor, así carnal como espiritual. Saludo a Alce, "
             "nombre que me es querido, y a Dafno el incomparable, y a "
             "Eutecno, y a todos por su nombre. Estad bien en la gracia de "
             "Dios.",
}
