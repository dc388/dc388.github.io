"""La definición del Diccionario Strong, en español.

El interlineal ya daba la glosa corta traducida y el análisis morfológico
explicado en español. Pero al abrir la ficha de una palabra, la definición
seguía apareciendo tal cual la escribió James Strong en 1890: en inglés. Para
quien no lee inglés eso deja la herramienta a medias justo donde más falta
hace, que es al hacer exégesis.

Aquí están traducidas a mano. No es traducción automática: el inglés de Strong
es lexicográfico y abreviado, y una máquina lo destroza de una forma que
además parece correcta, que es lo peor que le puede pasar a quien estudia.

Se traduce por orden de frecuencia en el texto, que es lo que rinde: los 200
lemas más frecuentes cubren el 58 % de las 439 705 palabras, y los 2 000 el
88 %. El resto sigue mostrando la definición inglesa hasta que le toque.

Criterios:

- Se traduce la definición, no se resume ni se mejora: si Strong dice «in a
  great variety of applications», eso se dice, porque avisa al lector de que
  la palabra es elástica y no debe forzarse en un solo sentido.

- Se conservan sus marcas de registro —«propiamente», «por implicación»,
  «figuradamente»— porque no son adorno: distinguen el sentido primario del
  derivado, y en exégesis esa distinción es justamente lo que se discute.

- Donde el campo inglés de la base llegó truncado o ilegible, se da la entrada
  completa de Strong en español en vez de arrastrar el defecto.

- Las referencias a otros números Strong se dejan como están: son enlaces a
  otra entrada, no texto que traducir.
"""

from __future__ import annotations

# Griego ---------------------------------------------------------------------

GRIEGO: dict[str, str] = {
    "G2424": "Jesús (es decir, Yehoshúa), el nombre de nuestro Señor y de otros dos o tres israelitas",
    "G1537": "preposición primaria que denota origen, el punto del que procede el movimiento o la acción: de, desde, fuera de; de lugar, de tiempo o de causa; literal o figurado, directo o remoto",
    "G1909": "propiamente, superposición —de tiempo, de lugar, de orden, etc.—; con genitivo indica distribución: sobre, encima de; con dativo, reposo: en, sobre; con acusativo, movimiento hacia: sobre, a",
    "G2962": "supremo en autoridad, es decir, como sustantivo, el que manda; por implicación, Señor, como título de respeto",
    "G2192": "tener, sostener; se usa con aplicaciones muy variadas, literales o figuradas, directas o remotas: posesión, capacidad, continuidad, relación o condición",
    "G4314": "preposición de dirección: hacia adelante, es decir, hacia; con genitivo, del lado de, o sea, perteneciente a; con dativo, al lado de, o sea, cerca de; normalmente con acusativo, el lugar, el tiempo o la ocasión hacia la que algo se dirige",
    "G1096": "hacer que algo llegue a ser, es decir, en reflexivo, llegar a ser, venir a existir; se usa con gran amplitud: literal, figurada, intensiva, etc.",
    "G1223": "a través de, por medio de, en aplicaciones muy amplias: de lugar, de causa o de ocasión",
    "G2443": "para que, indicando el propósito o el resultado",
    "G3708": "propiamente, mirar fijamente, es decir, por implicación, discernir con claridad; por extensión, atender a; por hebraísmo, experimentar; en pasiva, aparecer",
    "G575": "«fuera», es decir, lejos de algo cercano, en varios sentidos: de lugar, de tiempo o de relación; literal o figurado",
    "G2064": "venir o ir (con una gran variedad de aplicaciones, literales y figuradas)",
    "G235": "propiamente, «otras cosas»; es decir, como adverbio, al contrario, por el contrario; en muchas relaciones",
    "G4160": "hacer o realizar, en una aplicación muy amplia, más o menos directa",
    "G5101": "pronombre interrogativo: quién, cuál o qué, en preguntas directas o indirectas",
    "G5547": "ungido, es decir, el Mesías; epíteto de Jesús",
    "G444": "de rostro de hombre, es decir, un ser humano",
    "G5100": "alguna persona o alguna cosa; alguien, algo",
    "G3588": "el, la, lo (a veces hay que suplirlo y a veces se omite, según lo pida el castellano)",
    "G2532": "y, también, aun, así pues, además, etc.; a menudo se usa unido a otras partículas o palabras breves",
    "G846": "el pronombre reflexivo «mismo», usado (solo o en comparación con G1438 (ἑαυτοῦ)) para la tercera persona, y (con el pronombre personal correspondiente) para las demás",
    "G4771": "tú",
    "G1161": "pero, y, etc.",
    "G1722": "en, dentro de, sobre, junto a, por, etc.",
    "G1473": "yo",
    "G1510": "yo soy, yo existo (solo se usa cuando es enfático)",
    "G3004": "propiamente, «poner» delante, es decir, (figuradamente) relatar de palabra; normalmente en discurso ordenado o formal, mientras que G2036 (ἔπω) y G5346 (φημί) suelen referirse al habla suelta",
    "G1519": "a, hacia o dentro de (señalando el punto al que se llega o en el que se entra), sea de lugar, de tiempo o (figuradamente) de finalidad o resultado; también en locuciones adverbiales",
    "G3756": "el adverbio de negación absoluta (compárese con G3361 (μή)); no",
    "G3739": "el pronombre relativo, y a veces demostrativo: que, quien, el cual, lo que",
    "G3778": "este, esta, esto; es decir, este o aquel (a menudo repitiendo el artículo)",
    "G2316": "una deidad, especialmente la Divinidad suprema; figuradamente, un magistrado; por hebraísmo, sumamente",
    "G3754": "como demostrativo, que (a veces redundante); como causal, porque",
    "G3956": "todo, cualquiera, cada uno, el conjunto entero",
    "G1063": "propiamente, introduce la razón de lo dicho; se usa al argumentar, al explicar o al reforzar, y a menudo acompañado de otras partículas",
    "G3361": "como adverbio, no; como conjunción, no sea que; también en pregunta que espera respuesta negativa, mientras que G3756 (οὐ) espera una afirmativa",
}

# Hebreo ---------------------------------------------------------------------

HEBREO: dict[str, str] = {
    "H259": "propiamente, unido, es decir, uno; o, como ordinal, primero",
    "H3947": "tomar (con la más amplia variedad de aplicaciones)",
    "H3045": "conocer (propiamente, averiguar por la vista); se usa en una gran variedad de sentidos —figurado, literal, eufemístico y por inferencia— e incluye observar, cuidar y reconocer",
    "H5927": "subir; como intransitivo, estar en alto, y como activo, ascender; se usa en gran variedad de sentidos, primarios y secundarios, literales y figurados",
    "H854": "propiamente, cercanía (solo se usa como preposición o adverbio), cerca de; de ahí, en general, con, junto a, en, entre, etc.",
    "H5869": "un ojo (literal o figuradamente); por analogía, una fuente, como el ojo del paisaje",
    "H8141": "un año (como una vuelta completa del tiempo)",
    "H589": "yo",
    "H8034": "un nombre, como marca o recuerdo de lo que uno es; por implicación, honra, autoridad, carácter",
    "H7971": "enviar: despedir, mandar a buscar o echar fuera, en una gran variedad de aplicaciones",
    "H2009": "¡he aquí!, ¡mira!",
    "H4191": "morir (literal o figuradamente); en causativo, matar",
    "H8033": "allí; trasladado al tiempo, entonces; a menudo, hacia allá o desde allá",
    "H3063": "Judá, nombre de cinco israelitas; también de la tribu descendiente del primero y de su territorio",
    "H398": "comer (literal o figuradamente)",
    "H5650": "un siervo",
    "H369": "una nada, lo que no existe; se usa por lo general como partícula negativa",
    "H802": "una mujer",
    "H3651": "propiamente, puesto derecho; de ahí, como adjetivo figurado, justo; pero normalmente, como adverbio o conjunción, rectamente o así, en aplicaciones varias de modo, tiempo y relación, a menudo acompañado de otras partículas",
    "H1571": "propiamente, reunión; solo se usa adverbialmente: también, aun, sí; a menudo repetido en correlación: tanto… como",
    "H8147": "dos; también, como ordinal, doble",
    "H4872": "Moisés, el legislador de Israel",
    "H5315": "propiamente, una criatura que respira, es decir, un ser animado o, en abstracto, la vitalidad; se usa con enorme amplitud en sentido literal, adaptado o figurado, sea corporal o mental",
    "H3548": "literalmente, el que oficia: un sacerdote; también, por deferencia, quien ejerce como tal aunque sea laico",
    "H4100": "propiamente, interrogativo: ¿qué? (incluye ¿cómo?, ¿por qué?, ¿cuándo?); también exclamativo: ¡qué! (incluye ¡cómo!); y de forma indefinida, lo que (incluye cualquier cosa, y aun como relativo, aquello que)",
    "H428": "estos o esos",
    "H7121": "llamar a alguien; propiamente, dirigirse a él por su nombre, pero se usa en una gran variedad de aplicaciones",
    "H408": "no (la negación matizada, usada para desaconsejar); una vez, en Job 24:25, como sustantivo: nada",
    "H1870": "un camino (por ser lo que se pisa); figuradamente, un modo de vivir o de obrar; a menudo con valor adverbial",
    "H7451": "malo; o, como sustantivo, el mal, sea natural o moral",
    "H5375": "levantar, alzar, llevar; en una gran variedad de aplicaciones, literales y figuradas, absolutas y relativas",
    "H3389": "Jerusalén, la ciudad capital de Palestina",
    "H4714": "Egipto, es decir, el Alto y el Bajo Egipto",
    "H251": "un hermano, en el sentido más amplio: el parentesco literal y también la afinidad o el parecido metafóricos, igual que ocurre con «padre»",
    "H6965": "levantarse, ponerse en pie; en aplicaciones varias: literal, figurada, intensiva y causativa",
    "H2063": "esta; a menudo con valor adverbial",
    "H7218": "la cabeza (por ser lo que más fácilmente se mueve), sea literal o figuradamente, en muchas aplicaciones de lugar, tiempo y rango",
    "H3820": "el corazón; también se usa figuradamente, con muchísima amplitud, para los sentimientos, la voluntad y aun el entendimiento; asimismo para el centro de cualquier cosa",
    "H1323": "una hija, usada en el mismo sentido amplio que los demás términos de parentesco, literal y figuradamente",
    "H7760": "poner, colocar; se usa en una gran variedad de aplicaciones: literal, figurada, por inferencia y de forma elíptica",
    "H4325": "agua; figuradamente, jugo; por eufemismo, orina o semen",
    "H3967": "cien; también como multiplicativo y como fracción",
    "H3541": "propiamente, como esto; de ahí, por implicación, de este modo o así; también, de lugar, aquí o hacia aquí; o, de tiempo, ahora",
    "H2896": "bueno, como adjetivo, en el sentido más amplio; se usa igualmente como sustantivo, en masculino y femenino, singular y plural: lo bueno, un bien, un hombre o una mujer de bien",
    "H1992": "ellos (solo se usa cuando es enfático)",
    "H1471": "una nación extranjera; de ahí, un gentil; también, figuradamente, una manada de animales o una nube de langostas",
    "H5674": "cruzar, pasar al otro lado; se usa con mucha amplitud para cualquier tránsito, literal o figurado, transitivo, intransitivo, intensivo o causativo",
    "H120": "rojizo, es decir, un ser humano: el individuo, la especie, la humanidad, etc.",
    "H2022": "un monte o una cadena de montes (a veces en sentido figurado)",
    "H1419": "grande, en cualquier sentido; de ahí, mayor en edad; también, insolente",
    "H5975": "estar de pie, permanecer; en relaciones varias, literales y figuradas, intransitivas y transitivas",
    "H853": "propiamente, «el mismo»; pero por lo general sirve para señalar con más precisión el complemento de un verbo o de una preposición: a saber, es decir",
    "H3068": "Jehová, el nombre nacional del Dios de Israel",
    "H5921": "encima, sobre, por encima de, o contra (en este último sentido siempre con idea de caer desde arriba), en una gran variedad de aplicaciones",
    "H413": "cerca de, con o entre; y en general, a, hacia",
    "H834": "que, el cual, lo que, quien; también (como adverbio y como conjunción) cuando, donde, cómo, porque, para que, etc.",
    "H3605": "propiamente, la totalidad; de ahí, todo, cualquiera o cada uno (en singular, aunque muchas veces con sentido plural)",
    "H559": "decir (con muchísima amplitud de uso)",
    "H3808": "no (la negación simple o absoluta); por implicación, ninguno; con frecuencia acompañado de otras partículas",
    "H1121": "un hijo (como el que edifica el nombre de la familia), en el sentido más amplio, literal y figurado: incluye nieto, súbdito, pueblo, y también la cualidad o condición de algo",
    "H3588": "por implicación, se usa con enorme amplitud como conjunción o adverbio de relación, y otras partículas añadidas le modifican mucho el sentido",
    "H1961": "existir, es decir, ser o llegar a ser, suceder (siempre con fuerza propia; nunca es una mera cópula ni un auxiliar)",
    "H6213": "hacer o fabricar, en el sentido más amplio y con la aplicación más extensa",
    "H430": "dioses en el sentido corriente; pero específicamente (en este plural, sobre todo con el artículo) el Dios supremo; ocasionalmente se aplica por deferencia a magistrados",
    "H935": "ir o venir (con una gran variedad de aplicaciones)",
    "H4428": "un rey",
    "H3478": "Israel, nombre simbólico de Jacob; y también, como tipo, de su descendencia",
    "H776": "la tierra (en su conjunto, o una parte de ella: un país)",
    "H3117": "un día (como las horas de calor), sea en sentido literal —de la salida a la puesta del sol, o de una puesta a la siguiente— o figurado: un espacio de tiempo definido por lo que ocurre en él",
    "H376": "un hombre, como individuo o como varón; se usa a menudo junto a un término más preciso, y en esos casos con frecuencia no se traduce",
    "H6440": "el rostro (como la parte que se vuelve); se usa con gran variedad de aplicaciones, literales y figuradas, y también, con prefijo, como preposición: delante de",
    "H1004": "una casa (con la mayor variedad de aplicaciones, en especial la familia)",
    "H5414": "dar, con la mayor amplitud de aplicación: poner, hacer, etc.",
    "H1931": "él (ella o ello); solo se expresa cuando es enfático o cuando falta el verbo; también, con fuerza intensiva, «mismo», o (sobre todo con el artículo) «el mismo»; a veces con valor demostrativo",
    "H5971": "un pueblo (como unidad congregada); específicamente, una tribu, como las de Israel; de ahí, colectivamente, tropas o servidores; figuradamente, un rebaño",
    "H3027": "una mano (la mano abierta, que indica poder, medio, dirección, etc.)",
    "H1697": "una palabra; por implicación, un asunto (aquello de lo que se habla) o una cosa; adverbialmente, una causa",
    "H7200": "ver, en sentido literal o figurado, con numerosas aplicaciones, directas e implícitas, transitivas, intransitivas y causativas",
    "H5704": "hasta (tan lejos, tan largo o tanto como), sea de espacio (hasta), de tiempo (durante, mientras, hasta que) o de grado (igual que)",
    "H4480": "propiamente, una parte de; de ahí, como preposición, de o desde, en muchos sentidos",
    "H1": "padre, en sentido literal e inmediato, o figurado y remoto",
    "H2088": "el pronombre demostrativo masculino: este o ese",
    "H8085": "oír con entendimiento (a menudo con la idea de prestar atención y de obedecer; en causativo, hacer saber)",
    "H1696": "quizá propiamente, ordenar; pero usado figuradamente, hablando de palabras, hablar; raras veces, en sentido destructivo, someter",
    "H5892": "una ciudad (un lugar guardado por vigilancia o por una guardia) en el sentido más amplio, hasta de un simple campamento o puesto",
    "H859": "tú y a ti; o, en plural, vosotros y a vosotros",
    "H3427": "propiamente, sentarse (en concreto, como juez, al acecho o en reposo); por implicación, habitar, permanecer; en causativo, establecerse, casarse",
    "H1732": "David, el hijo menor de Isaí",
    "H518": "de uso muy amplio: como demostrativo, ¡mira!; como interrogativo, ¿acaso?; como condicional, si, aunque; también ¡ojalá!, cuando; y de ahí, como negación, no",
    "H3318": "salir (en causativo, sacar), con una gran variedad de aplicaciones, literales y figuradas, directas y aproximadas",
    "H7725": "volver atrás (y de ahí, apartarse), transitiva o intransitivamente, en sentido literal o figurado; no implica necesariamente regreso al punto de partida",
    "H5973": "adverbio o preposición: con (es decir, en compañía de), en aplicaciones variadas; en concreto, igual que; a menudo con prefijo preposicional",
    "H3212": "andar (literal o figuradamente); en causativo, llevar, en varios sentidos",
}

DEFINICIONES: dict[str, str] = {**GRIEGO, **HEBREO}
