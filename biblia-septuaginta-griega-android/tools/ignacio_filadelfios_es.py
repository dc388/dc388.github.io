"""Ignacio de Antioquía a los Filadelfios, traducida del griego.

Escrita desde Tróade. Vuelve sobre la unidad en torno a una sola eucaristía,
un solo altar y un solo obispo.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_FILADELFIOS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la iglesia de Dios Padre y "
            "del Señor Jesucristo que está en Filadelfia de Asia, que ha "
            "alcanzado misericordia y está afianzada en la concordia de Dios, "
            "y se regocija sin vacilar en la pasión de nuestro Señor, y está "
            "plenamente convencida de su resurrección en toda misericordia; a "
            "la cual saludo en la sangre de Jesucristo, que es gozo eterno y "
            "permanente, sobre todo si están unidos con el obispo y con los "
            "presbíteros y diáconos que están con él, designados según el "
            "sentir de Jesucristo, a los cuales, conforme a su propia "
            "voluntad, él afirmó con firmeza por su Santo Espíritu.",
    (1, 1): "De este obispo he sabido que no por sí mismo ni por medio de "
            "hombres obtuvo el ministerio que pertenece a la comunidad, ni "
            "por vanagloria, sino en el amor de Dios Padre y del Señor "
            "Jesucristo; y me ha dejado asombrado su mansedumbre, pues "
            "callando puede más que los que hablan cosas vanas.",
    (1, 2): "Porque está acorde con los mandamientos como la cítara con sus "
            "cuerdas. Por eso mi alma tiene por dichoso su sentir para con "
            "Dios, sabiendo que es virtuoso y perfecto, y su firmeza y su "
            "falta de ira en toda la mansedumbre del Dios vivo.",

    # Capítulo 2
    (2, 1): "Hijos, pues, de la luz de la verdad, huid de la división y de "
            "las malas doctrinas; y donde está el pastor, allí seguidle como "
            "ovejas.",
    (2, 2): "Porque muchos lobos que parecen dignos de crédito llevan "
            "cautivos con placer malo a los que corren la carrera de Dios; "
            "mas en vuestra unidad no tendrán lugar.",

    # Capítulo 3
    (3, 1): "Apartaos de las malas hierbas, que no cultiva Jesucristo, porque "
            "no son plantío del Padre. No que haya hallado división entre "
            "vosotros, sino depuración.",
    (3, 2): "Porque cuantos son de Dios y de Jesucristo, éstos están con el "
            "obispo. Y cuantos, arrepentidos, vengan a la unidad de la "
            "iglesia, también éstos serán de Dios, para que vivan conforme a "
            "Jesucristo.",
    (3, 3): "No os engañéis, hermanos míos: si alguno sigue al que hace "
            "cisma, no heredará el reino de Dios; si alguno anda en sentir "
            "ajeno, éste no se conforma con la pasión.",

    # Capítulo 4
    (4, 1): "Procurad, pues, usar de una sola eucaristía; porque una sola es "
            "la carne de nuestro Señor Jesucristo, y uno solo el cáliz para "
            "unirnos en su sangre, uno solo el altar, así como uno solo es el "
            "obispo, junto con el presbiterio y los diáconos, mis consiervos; "
            "para que todo lo que hagáis, lo hagáis según Dios.",

    # Capítulo 5
    (5, 1): "Hermanos míos, me derramo sobremanera en amor por vosotros, y "
            "lleno de gozo os pongo en guardia; mas no yo, sino Jesucristo, "
            "en quien, estando encadenado, temo más, como quien aún no está "
            "perfeccionado; pero vuestra oración a Dios me perfeccionará, "
            "para que alcance la suerte en que he alcanzado misericordia, "
            "acogiéndome al evangelio como a la carne de Jesús, y a los "
            "apóstoles como al presbiterio de la iglesia.",
    (5, 2): "Y amemos también a los profetas, porque también ellos anunciaron "
            "lo tocante al evangelio, y esperaron en él y le aguardaron; en "
            "quien también, habiendo creído, fueron salvos, estando en la "
            "unidad de Jesucristo, santos dignos de amor y dignos de "
            "admiración, que recibieron testimonio de Jesucristo y fueron "
            "contados en el evangelio de la esperanza común.",

    # Capítulo 6
    (6, 1): "Pero si alguno os interpreta el judaísmo, no le escuchéis. "
            "Porque mejor es oír el cristianismo de un hombre circuncidado "
            "que el judaísmo de un incircunciso. Mas si ni el uno ni el otro "
            "hablan de Jesucristo, éstos son para mí estelas y sepulcros de "
            "muertos, sobre los cuales sólo están escritos nombres de "
            "hombres.",
    (6, 2): "Huid, pues, de las malas artes y asechanzas del príncipe de este "
            "siglo, no sea que, oprimidos por su sentir, os debilitéis en el "
            "amor; antes bien, reuníos todos en uno con corazón indiviso.",
    (6, 3): "Y doy gracias a mi Dios de que tengo buena conciencia en cuanto "
            "a vosotros, y nadie puede gloriarse, ni en secreto ni en "
            "público, de que yo haya sido gravoso a alguno en poco o en "
            "mucho. Y a todos aquellos entre quienes hablé les deseo que no "
            "lo conviertan en testimonio contra sí.",

    # Capítulo 7
    (7, 1): "Porque, aunque algunos quisieron engañarme según la carne, el "
            "Espíritu, que es de Dios, no se engaña. Porque sabe de dónde "
            "viene y a dónde va, y redarguye lo oculto. Clamé estando entre "
            "vosotros, hablaba a gran voz, con voz de Dios: «Atended al "
            "obispo, y al presbiterio, y a los diáconos».",
    (7, 2): "Y hubo quienes sospecharon que yo decía esto porque sabía de "
            "antemano la división de algunos; pero me es testigo aquel por "
            "quien estoy encadenado de que no lo supe por carne humana. Mas "
            "el Espíritu predicaba, diciendo así: «Sin el obispo no hagáis "
            "nada; guardad vuestra carne como templo de Dios; amad la unión; "
            "huid de las divisiones; sed imitadores de Jesucristo, como "
            "también él lo es de su Padre».",

    # Capítulo 8
    (8, 1): "Yo, pues, hacía lo que me tocaba, como hombre dispuesto para la "
            "unión. Y donde hay división e ira, Dios no habita. A todos, "
            "pues, los que se arrepienten perdona el Señor, si se arrepienten "
            "volviendo a la unidad de Dios y al consejo del obispo. Confío en "
            "la gracia de Jesucristo, que desatará de vosotros toda atadura.",
    (8, 2): "Y os exhorto a no hacer nada por contienda, sino conforme a la "
            "enseñanza de Cristo. Porque oí a algunos que decían: «Si no lo "
            "hallo en los archivos, no lo creo en el evangelio»; y cuando yo "
            "les decía: «Está escrito», me respondían: «Eso es lo que está en "
            "cuestión». Mas para mí los archivos son Jesucristo; los archivos "
            "inviolables son su cruz, y su muerte, y su resurrección, y la fe "
            "que es por él; en las cuales quiero, por vuestra oración, ser "
            "justificado.",

    # Capítulo 9
    (9, 1): "Buenos son también los sacerdotes, pero mejor es el sumo "
            "sacerdote, a quien se ha confiado el lugar santísimo, el único a "
            "quien se han confiado las cosas ocultas de Dios; él es la puerta "
            "del Padre, por la cual entran Abraham, e Isaac, y Jacob, y los "
            "profetas, y los apóstoles, y la iglesia. Todo esto es para la "
            "unidad de Dios.",
    (9, 2): "Pero el evangelio tiene algo singular: la venida del Salvador, "
            "nuestro Señor Jesucristo, su pasión y la resurrección. Porque "
            "los amados profetas lo anunciaron a él; mas el evangelio es el "
            "cumplimiento de la incorrupción. Todas estas cosas juntas son "
            "buenas, si creéis en amor.",

    # Capítulo 10
    (10, 1): "Puesto que, conforme a vuestra oración y a las entrañas que "
             "tenéis en Cristo Jesús, se me ha anunciado que la iglesia que "
             "está en Antioquía de Siria tiene paz, os conviene, como iglesia "
             "de Dios, elegir a mano alzada un diácono para que vaya allá "
             "como embajador de Dios, para que se congratule con ellos, "
             "reunidos en uno, y glorifique el Nombre.",
    (10, 2): "Bienaventurado en Jesucristo el que sea tenido por digno de tal "
             "ministerio; y vosotros seréis glorificados. Y si queréis, no os "
             "es imposible hacerlo por el nombre de Dios, como también las "
             "iglesias más cercanas enviaron obispos, y otras, presbíteros y "
             "diáconos.",

    # Capítulo 11
    (11, 1): "En cuanto a Filón, el diácono de Cilicia, varón de buen "
             "testimonio, que también ahora me sirve en la palabra de Dios "
             "junto con Reo Agatópode, varón escogido, que me sigue desde "
             "Siria habiendo renunciado a esta vida, los cuales también dan "
             "testimonio de vosotros, yo también doy gracias a Dios por "
             "vosotros, porque los recibisteis como también el Señor os "
             "recibió a vosotros. Y los que los deshonraron, sean redimidos "
             "por la gracia de Jesucristo.",
    (11, 2): "Os saluda el amor de los hermanos que están en Tróade, desde "
             "donde también os escribo por medio de Burro, enviado conmigo "
             "por los efesios y los esmirniotas en señal de honra. Los "
             "honrará el Señor Jesucristo, en quien esperan en carne, alma, "
             "espíritu, fe, amor, concordia. Estad bien en Cristo Jesús, "
             "nuestra esperanza común.",
}
