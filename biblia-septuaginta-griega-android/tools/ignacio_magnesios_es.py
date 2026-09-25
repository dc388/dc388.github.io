"""Ignacio de Antioquía a los Magnesios, traducida del griego.

Escrita desde Esmirna, camino del martirio. Insiste en la unidad con el obispo
y advierte contra quienes siguen viviendo «según el judaísmo».

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_MAGNESIOS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la bendecida en la gracia de "
            "Dios Padre en Cristo Jesús, nuestro Salvador, en quien saludo a "
            "la iglesia que está en Magnesia junto al Meandro, y le deseo en "
            "Dios Padre y en Jesucristo salud abundantísima.",
    (1, 1): "Habiendo conocido el gran buen orden de vuestro amor según Dios, "
            "me he determinado con alegría a hablaros en la fe de Jesucristo.",
    (1, 2): "Porque, tenido por digno de un nombre divinísimo, en las cadenas "
            "que llevo canto a las iglesias, y les deseo unión con la carne y "
            "el espíritu de Jesucristo, nuestra vida para siempre; unión de "
            "fe y de amor, al cual nada se prefiere; y, lo que es más "
            "principal, unión con Jesús y con el Padre; en quien, soportando "
            "todo el ultraje del príncipe de este siglo y escapando de él, "
            "alcanzaremos a Dios.",

    # Capítulo 2
    (2, 1): "Ya que, pues, he sido tenido por digno de veros por medio de "
            "Damas, vuestro obispo digno de Dios, y de los dignos presbíteros "
            "Baso y Apolonio, y de mi consiervo el diácono Zotión, de quien "
            "ojalá pueda yo gozar, porque está sometido al obispo como a la "
            "gracia de Dios, y al presbiterio como a la ley de Jesucristo.",

    # Capítulo 3
    (3, 1): "Y a vosotros os conviene no abusar de la edad de vuestro obispo, "
            "sino tributarle toda reverencia según el poder de Dios Padre, "
            "como he sabido que también los santos presbíteros no se "
            "aprovechan de su aparente juventud, sino que, como prudentes en "
            "Dios, le ceden el paso; y no a él, sino al Padre de Jesucristo, "
            "el obispo de todos.",
    (3, 2): "Así pues, para honra de Aquel que nos ha querido, conviene "
            "obedecer sin hipocresía alguna; porque no es que uno engañe a "
            "este obispo que se ve, sino que trata de burlar al invisible. Y "
            "en tal caso la cuenta no es con la carne, sino con Dios, que "
            "conoce las cosas ocultas.",

    # Capítulo 4
    (4, 1): "Conviene, pues, no sólo llamarse cristianos, sino también serlo; "
            "así como hay algunos que llaman obispo a alguien, pero todo lo "
            "hacen sin él. Los tales no me parecen tener buena conciencia, "
            "porque no se reúnen firmemente conforme al mandamiento.",

    # Capítulo 5
    (5, 1): "Puesto que, pues, las cosas tienen un fin, y dos cosas se nos "
            "proponen a la vez, la muerte y la vida, y cada uno ha de ir a su "
            "propio lugar;",
    (5, 2): "porque así como hay dos monedas, una de Dios y otra del mundo, y "
            "cada una lleva impreso su propio cuño, así los incrédulos llevan "
            "el de este mundo, y los fieles, en amor, el cuño de Dios Padre "
            "por medio de Jesucristo; y si no estamos dispuestos por él a "
            "morir de buen grado para participar en su pasión, su vida no "
            "está en nosotros.",

    # Capítulo 6
    (6, 1): "Puesto que, pues, en las personas antes mencionadas he "
            "contemplado en fe a toda vuestra muchedumbre, y la he amado, os "
            "exhorto: procurad hacerlo todo en la concordia de Dios, "
            "presidiendo el obispo en lugar de Dios, y los presbíteros en "
            "lugar del senado de los apóstoles, y los diáconos, dulcísimos "
            "para mí, a quienes se ha confiado el ministerio de Jesucristo, "
            "el cual antes de los siglos estaba junto al Padre y al fin se "
            "manifestó.",
    (6, 2): "Todos, pues, habiendo recibido la conformidad de costumbres de "
            "Dios, reverenciaos unos a otros, y nadie mire a su prójimo según "
            "la carne, sino amaos siempre unos a otros en Jesucristo. Nada "
            "haya entre vosotros que pueda dividiros, sino uníos al obispo y "
            "a los que presiden, para figura y enseñanza de incorrupción.",

    # Capítulo 7
    (7, 1): "Así pues, como el Señor nada hizo sin el Padre, estando unido a "
            "él, ni por sí mismo ni por medio de los apóstoles, así tampoco "
            "vosotros hagáis nada sin el obispo y los presbíteros; ni "
            "intentéis que parezca razonable algo hecho a solas por vuestra "
            "cuenta, sino que en común haya una sola oración, una sola "
            "súplica, una sola mente, una sola esperanza en el amor, en el "
            "gozo irreprochable, que es Jesucristo, mejor que el cual no hay "
            "nada.",
    (7, 2): "Corred todos a una como a un solo templo de Dios, como a un solo "
            "altar, a un solo Jesucristo, que procedió de un solo Padre, y "
            "está con el Único, y a él volvió.",

    # Capítulo 8
    (8, 1): "No os dejéis engañar por doctrinas extrañas ni por fábulas "
            "antiguas que no aprovechan. Porque si hasta ahora vivimos según "
            "el judaísmo, confesamos que no hemos recibido la gracia.",
    (8, 2): "Porque los divinísimos profetas vivieron según Cristo Jesús. Por "
            "eso también fueron perseguidos, inspirados por su gracia, para "
            "que los desobedientes fuesen plenamente convencidos de que hay "
            "un solo Dios, que se manifestó a sí mismo por medio de "
            "Jesucristo su Hijo, que es su Verbo salido del silencio, el cual "
            "en todo agradó al que le envió.",

    # Capítulo 9
    (9, 1): "Si, pues, los que se habían criado en el orden antiguo de las "
            "cosas vinieron a la novedad de la esperanza, no guardando ya el "
            "sábado, sino viviendo según el día del Señor, en el cual también "
            "amaneció nuestra vida por medio de él y de su muerte, que "
            "algunos niegan; misterio por el cual recibimos el creer, y por "
            "el cual perseveramos, para ser hallados discípulos de "
            "Jesucristo, nuestro único Maestro;",
    (9, 2): "¿cómo podremos nosotros vivir sin aquel a quien también los "
            "profetas, siendo sus discípulos en el espíritu, esperaban como a "
            "su Maestro? Y por eso aquel a quien justamente aguardaban, al "
            "venir, los resucitó de entre los muertos.",

    # Capítulo 10
    (10, 1): "No seamos, pues, insensibles a su bondad. Porque si él nos "
             "imitara según lo que nosotros hacemos, ya no existiríamos. Por "
             "tanto, hechos discípulos suyos, aprendamos a vivir según el "
             "cristianismo. Porque el que se llama con otro nombre fuera de "
             "éste, no es de Dios.",
    (10, 2): "Echad fuera, pues, la mala levadura, envejecida y agriada, y "
             "transformaos en la nueva levadura, que es Jesucristo. Salaos en "
             "él, para que nadie entre vosotros se corrompa, porque por el "
             "olor seréis descubiertos.",
    (10, 3): "Absurdo es hablar de Jesucristo y judaizar. Porque el "
             "cristianismo no creyó en el judaísmo, sino el judaísmo en el "
             "cristianismo, en el cual se ha congregado toda lengua que ha "
             "creído en Dios.",

    # Capítulo 11
    (11, 1): "Y esto, amados míos, no porque haya sabido que algunos de "
             "vosotros estén así, sino que, como el menor de vosotros, quiero "
             "preveniros para que no caigáis en los anzuelos de la "
             "vanagloria, sino que estéis plenamente convencidos del "
             "nacimiento, de la pasión y de la resurrección acontecida en el "
             "tiempo del gobierno de Poncio Pilato; cosas hechas verdadera y "
             "firmemente por Jesucristo, nuestra esperanza, de la cual "
             "ninguno de vosotros sea jamás apartado.",

    # Capítulo 12
    (12, 1): "Que pueda yo gozar de vosotros en todo, si es que soy digno. "
             "Porque, aunque estoy atado, no soy comparable a uno solo de "
             "vosotros que estáis libres. Sé que no os envanecéis, porque "
             "tenéis a Jesucristo en vosotros; y más aún, cuando os alabo, sé "
             "que os avergonzáis, como está escrito: El justo es acusador de "
             "sí mismo.",

    # Capítulo 13
    (13, 1): "Procurad, pues, afirmaros en las enseñanzas del Señor y de los "
             "apóstoles, para que prosperéis en todo lo que hagáis, en la "
             "carne y en el espíritu, en la fe y en el amor, en el Hijo y en "
             "el Padre y en el Espíritu, en el principio y en el fin, "
             "juntamente con vuestro dignísimo obispo, y con la bien tejida "
             "corona espiritual de vuestro presbiterio, y con los diáconos "
             "según Dios.",
    (13, 2): "Someteos al obispo y los unos a los otros, como Jesucristo al "
             "Padre, y los apóstoles a Cristo y al Padre, para que haya unión "
             "carnal y espiritual.",

    # Capítulo 14
    (14, 1): "Sabiendo que estáis llenos de Dios, os he exhortado brevemente. "
             "Acordaos de mí en vuestras oraciones, para que alcance a Dios, "
             "y de la iglesia que está en Siria, de la cual no soy digno de "
             "llamarme miembro; porque necesito de vuestra oración unida en "
             "Dios y de vuestro amor, para que la iglesia que está en Siria "
             "sea tenida por digna de ser rociada por medio de vuestra "
             "iglesia.",

    # Capítulo 15
    (15, 1): "Os saludan los efesios desde Esmirna, desde donde también os "
             "escribo, presentes aquí para gloria de Dios, como también "
             "vosotros, los cuales me han confortado en todo, juntamente con "
             "Policarpo, obispo de los esmirniotas. Y también las demás "
             "iglesias os saludan en honra de Jesucristo. Pasadlo bien en la "
             "concordia de Dios, poseyendo un espíritu inseparable, que es "
             "Jesucristo.",
}
