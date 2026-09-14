"""Los 66 libros protestantes, y cómo los llama cada formato.

Las digitalizaciones libres vienen en tres formatos —USFX, OSIS y Zefania— y
ninguno nombra los libros igual: USFX dice `JDG`, OSIS dice `Judg` y Zefania no
los nombra, los numera. Esta tabla es el único sitio donde se cruzan, para que
un error de correspondencia se arregle en una línea y no en tres lectores.

El orden es el protestante, que es el que usa la numeración de Zefania: no es
el orden en que la aplicación enseña los libros (el Antiguo Testamento hebreo
va en orden del Tanaj), y los dos no deben confundirse.
"""

from __future__ import annotations

from typing import NamedTuple


class Libro(NamedTuple):
    app: str      # el código de esta aplicación
    usfx: str     # <book id="...">
    osis: str     # osisID='...'
    zefania: int  # <BIBLEBOOK bnumber="...">


CANON: tuple[Libro, ...] = (
    Libro("GEN", "GEN", "Gen", 1),
    Libro("EXO", "EXO", "Exod", 2),
    Libro("LEV", "LEV", "Lev", 3),
    Libro("NUM", "NUM", "Num", 4),
    Libro("DEU", "DEU", "Deut", 5),
    Libro("JOS", "JOS", "Josh", 6),
    Libro("JUE", "JDG", "Judg", 7),
    Libro("RUT", "RUT", "Ruth", 8),
    Libro("1SA", "1SA", "1Sam", 9),
    Libro("2SA", "2SA", "2Sam", 10),
    Libro("1RY", "1KI", "1Kgs", 11),
    Libro("2RY", "2KI", "2Kgs", 12),
    Libro("1CR", "1CH", "1Chr", 13),
    Libro("2CR", "2CH", "2Chr", 14),
    Libro("ESD", "EZR", "Ezra", 15),
    Libro("NEH", "NEH", "Neh", 16),
    Libro("EST", "EST", "Esth", 17),
    Libro("JOB", "JOB", "Job", 18),
    Libro("SAL", "PSA", "Ps", 19),
    Libro("PRO", "PRO", "Prov", 20),
    Libro("ECL", "ECC", "Eccl", 21),
    Libro("CNT", "SNG", "Song", 22),
    Libro("ISA", "ISA", "Isa", 23),
    Libro("JER", "JER", "Jer", 24),
    Libro("LAM", "LAM", "Lam", 25),
    Libro("EZE", "EZK", "Ezek", 26),
    Libro("DAN", "DAN", "Dan", 27),
    Libro("OSE", "HOS", "Hos", 28),
    Libro("JOE", "JOL", "Joel", 29),
    Libro("AMO", "AMO", "Amos", 30),
    Libro("ABD", "OBA", "Obad", 31),
    Libro("JON", "JON", "Jonah", 32),
    Libro("MIQ", "MIC", "Mic", 33),
    Libro("NAH", "NAM", "Nah", 34),
    Libro("HAB", "HAB", "Hab", 35),
    Libro("SOF", "ZEP", "Zeph", 36),
    Libro("AGE", "HAG", "Hag", 37),
    Libro("ZAC", "ZEC", "Zech", 38),
    Libro("MAL", "MAL", "Mal", 39),
    Libro("MAT", "MAT", "Matt", 40),
    Libro("MAR", "MRK", "Mark", 41),
    Libro("LUC", "LUK", "Luke", 42),
    Libro("JUA", "JHN", "John", 43),
    Libro("HEC", "ACT", "Acts", 44),
    Libro("ROM", "ROM", "Rom", 45),
    Libro("1CO", "1CO", "1Cor", 46),
    Libro("2CO", "2CO", "2Cor", 47),
    Libro("GAL", "GAL", "Gal", 48),
    Libro("EFE", "EPH", "Eph", 49),
    Libro("FIL", "PHP", "Phil", 50),
    Libro("COL", "COL", "Col", 51),
    Libro("1TE", "1TH", "1Thess", 52),
    Libro("2TE", "2TH", "2Thess", 53),
    Libro("1TI", "1TI", "1Tim", 54),
    Libro("2TI", "2TI", "2Tim", 55),
    Libro("TIT", "TIT", "Titus", 56),
    Libro("FLM", "PHM", "Phlm", 57),
    Libro("HEB", "HEB", "Heb", 58),
    Libro("SAN", "JAS", "Jas", 59),
    Libro("1PE", "1PE", "1Pet", 60),
    Libro("2PE", "2PE", "2Pet", 61),
    Libro("1JN", "1JN", "1John", 62),
    Libro("2JN", "2JN", "2John", 63),
    Libro("3JN", "3JN", "3John", 64),
    Libro("JUD", "JUD", "Jude", 65),
    Libro("APO", "REV", "Rev", 66),
)

# Variantes que se encuentran en digitalizaciones reales. OSIS tiene un estándar
# y no todo el mundo lo sigue: algunas usan la forma corta, otras la larga.
ALIAS_OSIS = {
    "exo": "Exod", "deu": "Deut", "jos": "Josh", "jdg": "Judg", "rth": "Ruth",
    "1sa": "1Sam", "2sa": "2Sam", "1ki": "1Kgs", "2ki": "2Kgs",
    "1ch": "1Chr", "2ch": "2Chr", "ezr": "Ezra", "est": "Esth",
    "psa": "Ps", "psalms": "Ps", "pro": "Prov", "ecc": "Eccl",
    "sng": "Song", "canticles": "Song", "songofsolomon": "Song",
    "ezk": "Ezek", "jol": "Joel", "amo": "Amos", "oba": "Obad",
    "jon": "Jonah", "mic": "Mic", "nam": "Nah", "zep": "Zeph",
    "hag": "Hag", "zec": "Zech", "mat": "Matt", "mrk": "Mark",
    "luk": "Luke", "jhn": "John", "act": "Acts", "1co": "1Cor",
    "2co": "2Cor", "eph": "Eph", "php": "Phil", "1th": "1Thess",
    "2th": "2Thess", "1ti": "1Tim", "2ti": "2Tim", "tit": "Titus",
    "phm": "Phlm", "jas": "Jas", "1pe": "1Pet", "2pe": "2Pet",
    "1jn": "1John", "2jn": "2John", "3jn": "3John", "jud": "Jude",
    "rev": "Rev",
}

POR_USFX = {l.usfx: l.app for l in CANON}
POR_OSIS = {l.osis.lower(): l.app for l in CANON}
POR_ZEFANIA = {l.zefania: l.app for l in CANON}


def desde_osis(codigo: str) -> str | None:
    """Código de libro OSIS -> código de la aplicación, tolerando variantes."""
    clave = codigo.strip().lower()
    if clave in POR_OSIS:
        return POR_OSIS[clave]
    canonico = ALIAS_OSIS.get(clave)
    return POR_OSIS.get(canonico.lower()) if canonico else None
