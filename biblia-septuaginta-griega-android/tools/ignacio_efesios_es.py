"""Ignacio de Antioquía a los Efesios, traducida del griego.

Ignacio, obispo de Antioquía, escribió siete cartas camino de Roma, donde iba
a morir en la arena hacia el año 110. Ésta la escribió desde Esmirna. Las siete
son el primer testimonio de una iglesia gobernada por un solo obispo con su
presbiterio y sus diáconos, y el griego de Ignacio es apretado y ardiente: se
ha procurado no alisarlo.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_EFESIOS_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a la bendecida en grandeza por "
            "la plenitud de Dios Padre, a la predestinada antes de los siglos "
            "a ser para siempre, para gloria permanente e inmutable, unida y "
            "escogida en la verdadera pasión, por voluntad del Padre y de "
            "Jesucristo, nuestro Dios; a la iglesia dignísima de ser llamada "
            "bienaventurada, que está en Éfeso de Asia: salud abundantísima "
            "en Jesucristo y en gozo irreprochable.",
    (1, 1): "Habiendo recibido en Dios vuestro nombre tan amado, que habéis "
            "adquirido por naturaleza justa, según la fe y el amor en Cristo "
            "Jesús, nuestro Salvador: siendo imitadores de Dios, reavivados "
            "en la sangre de Dios, habéis llevado a perfecto cumplimiento la "
            "obra que os es connatural.",
    (1, 2): "Porque al oír que venía yo atado desde Siria por el nombre y la "
            "esperanza comunes, esperando por vuestra oración alcanzar a "
            "luchar con las fieras en Roma, para que, alcanzándolo, pueda ser "
            "discípulo, os apresurasteis a verme.",
    (1, 3): "Puesto que, pues, he recibido en el nombre de Dios a toda "
            "vuestra muchedumbre en Onésimo, varón de amor inefable y vuestro "
            "obispo, al cual ruego que améis según Jesucristo, y que todos "
            "vosotros le seáis semejantes. Bendito sea el que os concedió, "
            "siendo dignos, poseer tal obispo.",

    # Capítulo 2
    (2, 1): "En cuanto a mi consiervo Burro, vuestro diácono según Dios, "
            "bendecido en todo, ruego que permanezca para honra vuestra y del "
            "obispo. Y también Croco, digno de Dios y de vosotros, a quien "
            "recibí como ejemplar de vuestro amor, me ha confortado en todo; "
            "así lo refrigere también a él el Padre de Jesucristo, juntamente "
            "con Onésimo, Burro, Euplo y Frontón, por medio de los cuales os "
            "he visto a todos vosotros en amor.",
    (2, 2): "Que pueda yo gozar de vosotros siempre, si es que soy digno. "
            "Conviene, pues, glorificar de todas maneras a Jesucristo, que os "
            "ha glorificado, para que, perfeccionados en una misma sumisión, "
            "sometidos al obispo y al presbiterio, seáis santificados en "
            "todo.",

    # Capítulo 3
    (3, 1): "No os doy órdenes como si fuera alguien. Porque, aunque estoy "
            "atado por el Nombre, aún no he sido perfeccionado en Jesucristo; "
            "ahora, en efecto, comienzo a ser discípulo, y os hablo como a "
            "condiscípulos míos. Pues era yo quien debía ser ungido por "
            "vosotros con fe, amonestación, paciencia y longanimidad.",
    (3, 2): "Pero ya que el amor no me permite callar acerca de vosotros, por "
            "eso me he adelantado a exhortaros a que corráis a una con el "
            "sentir de Dios. Porque también Jesucristo, nuestra vida "
            "inseparable, es el sentir del Padre, así como los obispos, "
            "establecidos hasta los confines de la tierra, están en el sentir "
            "de Jesucristo.",

    # Capítulo 4
    (4, 1): "Por lo cual os conviene correr a una con el sentir del obispo, "
            "como ya lo hacéis. Porque vuestro presbiterio, digno de su "
            "renombre y digno de Dios, está así concertado con el obispo como "
            "las cuerdas a la cítara. Por eso en vuestra concordia y en "
            "vuestro amor sinfónico se canta a Jesucristo.",
    (4, 2): "Y vosotros, uno por uno, formad un coro, para que, siendo "
            "concordes en la unanimidad, tomando en la unidad el tono de "
            "Dios, cantéis a una voz por medio de Jesucristo al Padre, para "
            "que os oiga y os reconozca, por vuestras buenas obras, como "
            "miembros de su Hijo. Os es provechoso, pues, estar en unidad "
            "irreprochable, para que también participéis siempre de Dios.",

    # Capítulo 5
    (5, 1): "Porque si yo en poco tiempo tuve tal familiaridad con vuestro "
            "obispo, que no era humana sino espiritual, ¿cuánto más os tengo "
            "por bienaventurados a vosotros, que estáis unidos a él como la "
            "iglesia a Jesucristo, y como Jesucristo al Padre, para que todas "
            "las cosas sean concordes en la unidad?",
    (5, 2): "Nadie se engañe: si alguno no está dentro del altar, se priva "
            "del pan de Dios. Porque si la oración de uno o dos tiene tanta "
            "fuerza, ¿cuánto más la del obispo y la de toda la iglesia?",
    (5, 3): "Así pues, el que no acude a la asamblea, ése ya se ensoberbece y "
            "a sí mismo se ha juzgado. Porque escrito está: Dios resiste a "
            "los soberbios. Procuremos, pues, no resistir al obispo, para que "
            "estemos sometidos a Dios.",

    # Capítulo 6
    (6, 1): "Y cuanto más vea uno callar al obispo, tanto más le tema; porque "
            "a todo aquel que el amo de casa envía para la administración de "
            "su casa, así debemos recibirlo como al mismo que lo envió. Es "
            "claro, pues, que debemos mirar al obispo como al Señor mismo.",
    (6, 2): "Y el mismo Onésimo alaba sobremanera vuestro buen orden en Dios, "
            "porque todos vivís según la verdad y porque entre vosotros no "
            "habita herejía alguna; antes bien, no escucháis a nadie más que "
            "al que os habla de Jesucristo en verdad.",

    # Capítulo 7
    (7, 1): "Porque algunos acostumbran llevar de acá para allá el Nombre con "
            "dolo perverso, mientras hacen otras cosas indignas de Dios; a "
            "éstos debéis evitarlos como a fieras, porque son perros rabiosos "
            "que muerden a traición; de ellos debéis guardaros, pues son "
            "difíciles de curar.",
    (7, 2): "Un solo médico hay, carnal y espiritual, engendrado e "
            "inengendrado, Dios en el hombre, en la muerte vida verdadera, "
            "nacido de María y de Dios, primero pasible y luego impasible: "
            "Jesucristo nuestro Señor.",

    # Capítulo 8
    (8, 1): "Que nadie, pues, os engañe, como tampoco os dejáis engañar, "
            "siendo enteramente de Dios. Porque cuando no se ha asentado "
            "entre vosotros ninguna contienda que pueda atormentaros, "
            "entonces vivís según Dios. Soy vuestro desecho, y me ofrezco en "
            "expiación por vosotros, efesios, iglesia célebre por los siglos.",
    (8, 2): "Los carnales no pueden hacer las cosas espirituales, ni los "
            "espirituales las carnales, así como tampoco la fe las de la "
            "incredulidad, ni la incredulidad las de la fe. Pero aun lo que "
            "hacéis según la carne, eso es espiritual, porque todo lo hacéis "
            "en Jesucristo.",

    # Capítulo 9
    (9, 1): "Pero he sabido que pasaron por ahí algunos venidos de allá con "
            "mala doctrina, a quienes no permitisteis sembrar entre vosotros, "
            "tapándoos los oídos para no recibir lo que ellos sembraban, como "
            "piedras que sois del templo del Padre, preparadas para el "
            "edificio de Dios Padre, elevadas a lo alto por la grúa de "
            "Jesucristo, que es la cruz, usando como cuerda al Espíritu "
            "Santo; y vuestra fe es la que os eleva, y el amor es el camino "
            "que conduce a Dios.",
    (9, 2): "Sois, pues, todos compañeros de camino, portadores de Dios y "
            "portadores del templo, portadores de Cristo, portadores de lo "
            "santo, adornados en todo con los mandamientos de Jesucristo. Con "
            "vosotros también yo, regocijándome, he sido tenido por digno de "
            "conversar por medio de lo que os escribo, y de alegrarme con "
            "vosotros, porque, en cuanto a la vida humana, no amáis nada sino "
            "sólo a Dios.",

    # Capítulo 10
    (10, 1): "Y orad también sin cesar por los demás hombres, porque hay en "
             "ellos esperanza de arrepentimiento, para que alcancen a Dios. "
             "Permitidles, pues, que por lo menos por vuestras obras sean "
             "hechos discípulos.",
    (10, 2): "Frente a sus iras, vosotros mansos; frente a sus jactancias, "
             "vosotros humildes; frente a sus blasfemias, vosotros las "
             "oraciones; frente a su extravío, vosotros firmes en la fe; "
             "frente a su fiereza, vosotros apacibles, sin procurar imitarlos "
             "a vuestra vez.",
    (10, 3): "Hallémonos hermanos suyos por la mansedumbre; y procuremos ser "
             "imitadores del Señor: a ver quién es más agraviado, quién más "
             "despojado, quién más menospreciado, para que no se halle entre "
             "vosotros hierba alguna del diablo, sino que con toda pureza y "
             "templanza permanezcáis en Jesucristo en la carne y en el "
             "espíritu.",

    # Capítulo 11
    (11, 1): "Éstos son los últimos tiempos. En adelante, pues, "
             "avergoncémonos, temamos la longanimidad de Dios, no sea que se "
             "nos vuelva condenación. Porque, o temamos la ira venidera, o "
             "amemos la gracia presente: una de las dos; con tal sólo de ser "
             "hallados en Cristo Jesús para la vida verdadera.",
    (11, 2): "Fuera de él, nada os parezca digno; en él llevo estas cadenas, "
             "las perlas espirituales, en las cuales ojalá resucite yo por "
             "vuestra oración, de la cual ojalá sea siempre partícipe, para "
             "que sea hallado en la heredad de los cristianos de Éfeso, que "
             "siempre estuvieron de acuerdo con los apóstoles en el poder de "
             "Jesucristo.",

    # Capítulo 12
    (12, 1): "Sé quién soy y a quiénes escribo. Yo, un condenado; vosotros, "
             "objeto de misericordia. Yo, bajo peligro; vosotros, afianzados.",
    (12, 2): "Sois lugar de paso de los que son llevados a la muerte para ir "
             "a Dios, coiniciados en los misterios con Pablo, el santificado, "
             "el que recibió testimonio, digno de ser llamado bienaventurado, "
             "en cuyas huellas ojalá sea yo hallado cuando alcance a Dios; "
             "él, que en toda su carta hace memoria de vosotros en Cristo "
             "Jesús.",

    # Capítulo 13
    (13, 1): "Procurad, pues, reuniros con más frecuencia para la eucaristía "
             "de Dios y para su gloria. Porque cuando os juntáis con "
             "frecuencia en un mismo lugar, son derribados los poderes de "
             "Satanás, y su ruina se deshace en la concordia de vuestra fe.",
    (13, 2): "Nada hay mejor que la paz, en la cual se acaba toda guerra de "
             "los celestiales y de los terrenales.",

    # Capítulo 14
    (14, 1): "Nada de esto se os oculta, si tenéis perfectamente la fe y el "
             "amor hacia Jesucristo, que son principio y fin de la vida: el "
             "principio es la fe, el fin es el amor. Y las dos, hechas una, "
             "son Dios; y todo lo demás que atañe a la hombría de bien se "
             "sigue de ellas.",
    (14, 2): "Nadie que profesa la fe peca, ni nadie que posee el amor "
             "aborrece. Por su fruto se conoce el árbol; así, los que "
             "profesan ser de Cristo se darán a conocer por lo que hacen. "
             "Porque la obra no es ahora cosa de profesión, sino de que uno "
             "sea hallado en el poder de la fe hasta el fin.",

    # Capítulo 15
    (15, 1): "Mejor es callar y ser, que hablar y no ser. Bueno es enseñar, "
             "si el que habla hace. Uno solo es, pues, el Maestro, que dijo, "
             "y fue hecho; y aun lo que hizo callando es digno del Padre.",
    (15, 2): "El que posee de verdad la palabra de Jesús puede oír también su "
             "silencio, para ser perfecto, para que obre por lo que habla y "
             "sea conocido por lo que calla.",
    (15, 3): "Nada se le oculta al Señor, sino que aun nuestros secretos "
             "están cerca de él. Hagámoslo, pues, todo como quien habita en "
             "nosotros, para que seamos templos suyos y él sea en nosotros "
             "nuestro Dios; como lo es en verdad, y se manifestará ante "
             "nuestro rostro, por lo cual con justicia le amamos.",

    # Capítulo 16
    (16, 1): "No os engañéis, hermanos míos: los que corrompen las familias "
             "no heredarán el reino de Dios.",
    (16, 2): "Si, pues, los que hacían esto según la carne murieron, ¿cuánto "
             "más si alguno corrompe con mala doctrina la fe de Dios, por la "
             "cual Jesucristo fue crucificado? Tal hombre, hecho inmundo, irá "
             "al fuego inextinguible, y lo mismo el que le escucha.",

    # Capítulo 17
    (17, 1): "Por esto recibió el Señor ungüento sobre su cabeza: para "
             "exhalar incorrupción sobre la iglesia. No os unjáis con el mal "
             "olor de la doctrina del príncipe de este siglo, no sea que os "
             "lleve cautivos lejos de la vida que tenéis delante.",
    (17, 2): "¿Y por qué no somos todos prudentes, habiendo recibido el "
             "conocimiento de Dios, que es Jesucristo? ¿Por qué perecemos "
             "neciamente, ignorando el don que el Señor en verdad ha enviado?",

    # Capítulo 18
    (18, 1): "Mi espíritu es desecho de la cruz, la cual es escándalo para "
             "los incrédulos, mas para nosotros salvación y vida eterna. "
             "¿Dónde está el sabio? ¿Dónde el disputador? ¿Dónde la jactancia "
             "de los que se llaman entendidos?",
    (18, 2): "Porque nuestro Dios, Jesús el Cristo, fue llevado en el seno "
             "por María, según la economía de Dios, del linaje de David, sí, "
             "pero del Espíritu Santo; el cual nació y fue bautizado, para "
             "purificar el agua con su pasión.",

    # Capítulo 19
    (19, 1): "Y quedaron ocultos al príncipe de este siglo la virginidad de "
             "María y su parto, así como también la muerte del Señor: tres "
             "misterios clamorosos, que fueron obrados en el silencio de "
             "Dios.",
    (19, 2): "¿Cómo, pues, fueron manifestados a los siglos? Una estrella "
             "brilló en el cielo por encima de todas las estrellas, y su luz "
             "era indecible, y su novedad causaba asombro; y todos los demás "
             "astros, junto con el sol y la luna, se hicieron coro en torno a "
             "la estrella, y ella sobrepujaba con su luz a todos; y había "
             "turbación: ¿de dónde vendría aquella novedad tan distinta de "
             "ellos?",
    (19, 3): "Desde entonces se deshacía toda magia y desaparecía toda "
             "atadura de maldad; la ignorancia era destruida, el antiguo "
             "reino se arruinaba, al manifestarse Dios en forma humana para "
             "novedad de vida eterna; y tomaba principio lo que en Dios "
             "estaba ya dispuesto. De ahí que todo se conmoviera, porque se "
             "preparaba la destrucción de la muerte.",

    # Capítulo 20
    (20, 1): "Si Jesucristo me tiene por digno, por vuestra oración, y es su "
             "voluntad, en el segundo librito que he de escribiros os "
             "explicaré más la economía que he comenzado a tratar acerca del "
             "hombre nuevo Jesucristo, en su fe y en su amor, en su pasión y "
             "resurrección;",
    (20, 2): "sobre todo si el Señor me revela que todos vosotros, uno por "
             "uno y en común, por la gracia que viene del Nombre, os reunís "
             "en una sola fe y en Jesucristo, el cual según la carne es del "
             "linaje de David, Hijo del hombre e Hijo de Dios, para obedecer "
             "al obispo y al presbiterio con mente no distraída, partiendo un "
             "mismo pan, que es medicina de inmortalidad, antídoto para no "
             "morir, sino vivir en Jesucristo para siempre.",

    # Capítulo 21
    (21, 1): "Yo soy rescate por vosotros y por aquellos que, para honra de "
             "Dios, enviasteis a Esmirna, desde donde también os escribo, "
             "dando gracias al Señor y amando a Policarpo como también a "
             "vosotros. Acordaos de mí, como también Jesucristo de vosotros.",
    (21, 2): "Orad por la iglesia que está en Siria, de donde soy llevado "
             "atado a Roma, siendo el último de los fieles de allí, así como "
             "he sido tenido por digno de ser hallado para honra de Dios. "
             "Pasadlo bien en Dios Padre y en Jesucristo, nuestra común "
             "esperanza.",
}
