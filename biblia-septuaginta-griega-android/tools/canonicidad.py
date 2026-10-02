"""Qué es canon y qué no, y por qué está aquí lo que no lo es.

La aplicación trae 138 libros. Mezclarlos en una sola lista sin decir cuál es
cuál sería el peor servicio que se le puede hacer a quien estudia: hay que poder
ver de un golpe si lo que se está leyendo es Escritura o es literatura del mismo
período que ayuda a entenderla.

El criterio es el de las Asambleas de Dios, que es el que pidió quien encarga
esto: su Declaración de Verdades Fundamentales abre afirmando «las Escrituras
inspiradas» del Antiguo y el Nuevo Testamento, y con eso recibe el canon
protestante de 66 libros. Todo lo demás de esta biblioteca —los
deuterocanónicos, el resto de la Septuaginta, los pseudoepígrafos y los Padres
Apostólicos— se ofrece como literatura de estudio, no como Escritura, y la
aplicación lo dice donde se ve.

Las cuatro clases, y por qué se distinguen en vez de llamarlo todo «apócrifo»:

- CANON: los 66. En la Septuaginta son los mismos libros en griego, no otros.
- DEUTEROCANONICO: los que Roma y las iglesias orientales sí reciben —Tobías,
  Judit, Sabiduría, Eclesiástico, Baruc, Macabeos, las adiciones a Ester y a
  Daniel—. Para las Asambleas de Dios no son canon, pero no es lo mismo que el
  resto: hay una tradición eclesial detrás y conviene saberlo.
- SEPTUAGINTA: los que no recibe nadie como canon pero vienen en los códices
  griegos: 1 Esdras, 3 y 4 Macabeos, las Odas.
- PSEUDOEPIGRAFO: atribuidos a un autor que no los escribió. Enoc, los Salmos
  de Salomón.
- PADRES: los Padres Apostólicos. No son apócrifos y llamarlos así sería un
  error: son cartas y manuales cristianos del siglo I y II, y nunca se
  presentaron como Escritura. La Didaché y 1 Clemente son de la generación de
  los apóstoles.

Ester y Daniel son canónicos, pero su texto griego lleva dentro adiciones que no
lo son —la oración de Azarías, Susana, Bel—. Aquí Susana y Bel van aparte,
porque así vienen en la edición griega que se usa, y la nota lo explica.
"""

from __future__ import annotations

CANON = "canon"
DEUTEROCANONICO = "deuterocanonico"
SEPTUAGINTA = "septuaginta"
PSEUDOEPIGRAFO = "pseudoepigrafo"
PADRES = "padres"

# Cómo se llama cada clase donde la ve quien lee, y qué se le dice.
CLASES: dict[str, tuple[str, str]] = {
    CANON: (
        "Canon",
        "Los 66 libros que las Asambleas de Dios reciben como Escritura "
        "inspirada.",
    ),
    DEUTEROCANONICO: (
        "Deuterocanónicos",
        "Recibidos como canon por la Iglesia católica y las orientales, no por "
        "las Asambleas de Dios. Se ofrecen para estudio.",
    ),
    SEPTUAGINTA: (
        "Otros libros de la Septuaginta",
        "Vienen en los códices griegos y ninguna iglesia los recibe como canon.",
    ),
    PSEUDOEPIGRAFO: (
        "Pseudoepígrafos",
        "Atribuidos a un autor que no los escribió. Se citan en el Nuevo "
        "Testamento —Judas 14 cita a Enoc— y por eso se estudian.",
    ),
    PADRES: (
        "Padres Apostólicos",
        "Cartas y manuales cristianos del siglo I y II. No son apócrifos: nunca "
        "se presentaron como Escritura.",
    ),
}

# Los libros de la Septuaginta que NO son del canon de 66. Todo lo que no esté
# aquí es canónico: es más seguro enumerar la excepción que el canon, porque una
# edición griega nueva trae libros raros, no libros canónicos nuevos.
_FUERA_DEL_CANON: dict[str, str] = {
    "TOB": DEUTEROCANONICO,   # Tobías
    "JDT": DEUTEROCANONICO,   # Judit
    "SAB": DEUTEROCANONICO,   # Sabiduría de Salomón
    "SIR": DEUTEROCANONICO,   # Eclesiástico (Sirácida)
    "BAR": DEUTEROCANONICO,   # Baruc
    "CJE": DEUTEROCANONICO,   # Carta de Jeremías (Baruc 6 en la Vulgata)
    "1MA": DEUTEROCANONICO,   # 1 Macabeos
    "2MA": DEUTEROCANONICO,   # 2 Macabeos
    "SUS": DEUTEROCANONICO,   # Susana, adición a Daniel
    "SUT": DEUTEROCANONICO,
    "BEL": DEUTEROCANONICO,   # Bel y el Dragón, adición a Daniel
    "BET": DEUTEROCANONICO,
    "1ES": SEPTUAGINTA,       # 1 Esdras, el «Esdras griego»
    "3MA": SEPTUAGINTA,
    "4MA": SEPTUAGINTA,
    "ODA": SEPTUAGINTA,       # Odas, con la oración de Manasés
    "SSA": PSEUDOEPIGRAFO,    # Salmos de Salomón
}

# El orden en que se enseñan los que no son canon: primero lo que alguna iglesia
# recibe, y dentro de eso el orden de la Vulgata, que es como se citan.
ORDEN = (
    "TOB", "JDT", "SAB", "SIR", "BAR", "CJE", "1MA", "2MA",
    "SUS", "SUT", "BEL", "BET",
    "1ES", "3MA", "4MA", "ODA",
    "SSA", "ENOC",
)


def clase(coleccion: str, codigo: str) -> str:
    """La clase de un libro, por su colección y su código."""
    if coleccion == "padres":
        return PADRES
    if coleccion == "pseudo":
        return PSEUDOEPIGRAFO
    if coleccion == "lxx":
        return _FUERA_DEL_CANON.get(codigo, CANON)
    return CANON                          # el hebreo y el Nuevo Testamento


def orden(codigo: str) -> int:
    """Dónde va este libro dentro de su clase. Los que no están, al final."""
    return ORDEN.index(codigo) if codigo in ORDEN else len(ORDEN)
