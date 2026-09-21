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
