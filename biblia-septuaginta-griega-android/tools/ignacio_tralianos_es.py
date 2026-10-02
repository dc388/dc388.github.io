"""Ignacio de Antioquía a los Tralianos, traducida del griego.

Escrita desde Esmirna. Va contra los docetas, que decían que Cristo sólo
pareció sufrir: Ignacio repite que «verdaderamente» nació, comió, padeció y
resucitó.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_TRALIANOS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la amada de Dios, Padre de "
            "Jesucristo, a la iglesia santa que está en Trales de Asia, "
            "escogida y digna de Dios, que tiene paz en la carne y en el "
            "espíritu por la pasión de Jesucristo, nuestra esperanza por la "
            "resurrección hacia él; a la cual también saludo en la plenitud, "
            "a la manera apostólica, y le deseo salud abundantísima.",
    (1, 1): "He sabido que tenéis una mente irreprochable e indivisa en la "
            "paciencia, no por costumbre sino por naturaleza, según me lo "
            "manifestó Polibio, vuestro obispo, que por voluntad de Dios y de "
            "Jesucristo se presentó en Esmirna, y tanto se alegró conmigo, "
            "atado en Cristo Jesús, que en él contemplé a toda vuestra "
            "muchedumbre.",
    (1, 2): "Habiendo recibido, pues, por medio de él vuestra benevolencia "
            "según Dios, di gloria al hallaros, según supe, imitadores de "
            "Dios.",

    # Capítulo 2
    (2, 1): "Porque cuando os sometéis al obispo como a Jesucristo, me "
            "parecéis vivir no según los hombres, sino según Jesucristo, que "
            "por nosotros murió, para que, creyendo en su muerte, escapéis de "
            "morir.",
    (2, 2): "Es necesario, pues, como ya lo hacéis, que no hagáis nada sin el "
            "obispo, sino que os sometáis también al presbiterio como a los "
            "apóstoles de Jesucristo, nuestra esperanza, en quien, si "
            "vivimos, seremos hallados.",
    (2, 3): "Es preciso también que los diáconos, que lo son de los misterios "
            "de Jesucristo, agraden a todos de todas maneras. Porque no son "
            "diáconos de comidas y bebidas, sino servidores de la iglesia de "
            "Dios. Conviene, pues, que se guarden de las acusaciones como del "
            "fuego.",

    # Capítulo 3
    (3, 1): "Asimismo, que todos reverencien a los diáconos como a "
            "Jesucristo, como también al obispo, que es figura del Padre, y a "
            "los presbíteros como al senado de Dios y como al colegio de los "
            "apóstoles. Sin éstos no se llama iglesia.",
    (3, 2): "Acerca de esto estoy persuadido de que así lo tenéis. Porque he "
            "recibido el ejemplar de vuestro amor, y lo tengo conmigo en "
            "vuestro obispo, cuyo solo porte es una gran enseñanza, y su "
            "mansedumbre, un poder; creo que aun los ateos le reverencian.",
    (3, 3): "Porque os amo, me contengo, pudiendo escribir con más dureza "
            "sobre esto. No he llegado a pensar que, siendo yo un condenado, "
            "os dé órdenes como un apóstol.",

    # Capítulo 4
    (4, 1): "Muchas cosas entiendo en Dios, pero me mido a mí mismo, para no "
            "perecer por la jactancia. Porque ahora debo temer más y no "
            "prestar atención a los que me envanecen; porque los que me "
            "alaban me azotan.",
    (4, 2): "Amo, en efecto, el padecer, pero no sé si soy digno. Porque la "
            "envidia no la ven muchos, pero a mí me hace más guerra. "
            "Necesito, pues, mansedumbre, por la cual es destruido el "
            "príncipe de este siglo.",

    # Capítulo 5
    (5, 1): "¿Acaso no puedo escribiros las cosas celestiales? Pero temo "
            "causaros daño, siendo como sois niños; y perdonadme, no sea que, "
            "no pudiendo recibirlas, os ahoguéis.",
    (5, 2): "Porque también yo, no por estar atado y poder entender las cosas "
            "celestiales, y las jerarquías de los ángeles, y las formaciones "
            "de los principados, las cosas visibles e invisibles, por eso ya "
            "soy discípulo. Porque mucho nos falta, para que no nos falte "
            "Dios.",

    # Capítulo 6
    (6, 1): "Os exhorto, pues, no yo, sino el amor de Jesucristo: usad sólo "
            "del alimento cristiano, y absteneos de la hierba extraña, que es "
            "la herejía.",
    (6, 2): "Éstos entretejen consigo a Jesucristo, haciéndose pasar por "
            "dignos de fe, como quienes dan un veneno mortal mezclado con "
            "vino y miel, que el ignorante toma con gusto, y con un placer "
            "funesto recibe la muerte.",

    # Capítulo 7
    (7, 1): "Guardaos, pues, de los tales. Y esto lo lograréis no "
            "envaneciéndoos y permaneciendo inseparables de Dios, Jesucristo, "
            "y del obispo, y de las ordenanzas de los apóstoles.",
    (7, 2): "El que está dentro del altar es puro; pero el que está fuera del "
            "altar no es puro; es decir, el que hace algo sin el obispo, el "
            "presbiterio y los diáconos, ése no es puro en su conciencia.",

    # Capítulo 8
    (8, 1): "No porque haya sabido de algo semejante entre vosotros, sino que "
            "os prevengo, porque sois mis amados, previendo las asechanzas "
            "del diablo. Vosotros, pues, revistiéndoos de mansedumbre, "
            "recreaos en la fe, que es la carne del Señor, y en el amor, que "
            "es la sangre de Jesucristo.",
    (8, 2): "Ninguno de vosotros tenga nada contra su prójimo. No deis "
            "ocasión a los gentiles, para que por unos pocos insensatos no "
            "sea blasfemada la muchedumbre que está en Dios. Porque: ¡Ay de "
            "aquel por quien mi nombre es vanamente blasfemado entre algunos!",

    # Capítulo 9
    (9, 1): "Haceos, pues, sordos cuando alguno os hable sin Jesucristo, el "
            "que es del linaje de David, el que es de María; el cual "
            "verdaderamente nació, comió y bebió; verdaderamente fue "
            "perseguido bajo Poncio Pilato; verdaderamente fue crucificado y "
            "murió, a la vista de los celestiales, de los terrenales y de los "
            "infernales;",
    (9, 2): "el cual también verdaderamente resucitó de entre los muertos, "
            "resucitándole su Padre; y a semejanza suya, así también a "
            "nosotros, los que creemos en él, nos resucitará su Padre en "
            "Cristo Jesús, sin el cual no tenemos la vida verdadera.",

    # Capítulo 10
    (10, 1): "Y si, como dicen algunos que son ateos, es decir, incrédulos, "
             "él sólo en apariencia padeció —siendo ellos mismos pura "
             "apariencia—, ¿por qué estoy yo atado? ¿Por qué deseo también "
             "luchar con las fieras? En vano, pues, muero. Luego miento "
             "contra el Señor.",

    # Capítulo 11
    (11, 1): "Huid, pues, de los malos retoños que engendran fruto mortífero, "
             "del cual si alguno gusta, al instante muere. Porque éstos no "
             "son plantío del Padre. ² Porque si lo fuesen, aparecerían como "
             "ramas de la cruz, y su fruto sería incorruptible; por medio de "
             "ella, en su pasión, él os llama a vosotros, que sois sus "
             "miembros. No puede, pues, la cabeza nacer sola sin los "
             "miembros, prometiéndonos Dios la unión, que es él mismo.",

    # Capítulo 12
    (12, 1): "Os saludo desde Esmirna, juntamente con las iglesias de Dios "
             "que están aquí conmigo, las cuales me han confortado en todo, "
             "en la carne y en el espíritu.",
    (12, 2): "Os exhortan mis cadenas, que llevo por Jesucristo, pidiendo "
             "alcanzar a Dios: perseverad en vuestra concordia y en la "
             "oración de unos con otros. Porque os conviene a cada uno, y "
             "especialmente a los presbíteros, confortar al obispo para honra "
             "del Padre, de Jesucristo y de los apóstoles.",
    (12, 3): "Ruego que me escuchéis en amor, para que no sea yo, por haberos "
             "escrito, testimonio contra vosotros. Y orad también por mí, que "
             "necesito de vuestro amor en la misericordia de Dios, para que "
             "sea tenido por digno de la suerte que estoy a punto de "
             "alcanzar, a fin de no ser hallado reprobado.",

    # Capítulo 13
    (13, 1): "Os saluda el amor de los esmirniotas y de los efesios. Acordaos "
             "en vuestras oraciones de la iglesia que está en Siria, de la "
             "cual no soy digno de ser llamado miembro, siendo el último de "
             "ellos.",
    (13, 2): "Pasadlo bien en Jesucristo, sometidos al obispo como al "
             "mandamiento, y asimismo al presbiterio. Y amaos uno por uno los "
             "unos a los otros con corazón indiviso.",
    (13, 3): "Mi espíritu se ofrece en expiación por vosotros, no sólo ahora, "
             "sino también cuando alcance a Dios. Porque aún estoy bajo "
             "peligro; pero fiel es el Padre en Jesucristo para cumplir mi "
             "petición y la vuestra; en él seáis hallados irreprochables.",
}
