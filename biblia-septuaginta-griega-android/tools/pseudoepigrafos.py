"""Pseudoepígrafos: los libros de fuera del canon, en su griego conservado.

Empieza por el Libro de Enoc, que es el que más se busca: lo cita Judas 14-15,
lo leyeron los de Qumrán y entra en el canon de la Iglesia etíope, pero no en el
hebreo ni en el de ninguna de las iglesias occidentales.

Del griego solo sobrevive una parte. El Códice Panopolitano, encontrado en
Ajmim en 1886, trae los capítulos 1 a 32 —el Libro de los Vigilantes, que es la
sección que cita Judas— y ahí se acaba. El resto del libro únicamente existe
completo en etíope, que no se incluye porque no hay edición redistribuible ni
la aplicación sabe presentar esa escritura.

La edición es la de Johannes Flemming (Das Buch Henoch, GCS, Leipzig 1901), en
First1KGreek, con licencia CC BY-SA 4.0.
"""

from __future__ import annotations

from pathlib import Path

import tei

# (código, nombre en español, título griego, nombre alterno, archivo TEI, parte)
PSEUDOEPIGRAFOS = [
    ("ENOC", "Enoc", "Ἀποκάλυψις Ἑνώχ", "1 Enoc, Libro de los Vigilantes",
     "tlg1463.tlg001.1st1K-grc2.xml", None),
]

NOTA_ENOC = (
    "Capítulos 1 a 32, que son los que sobreviven en griego en el Códice "
    "Panopolitano. El resto del libro solo se conserva completo en etíope."
)

NOTAS = {"ENOC": NOTA_ENOC}


def descargar(destino: Path) -> None:
    tei.descargar(destino, [p[4] for p in PSEUDOEPIGRAFOS])


def leer(ruta: Path, parte: int | None = None) -> list[tuple[int, int, str, str]]:
    """Lee descartando lo que no esté en griego.

    La edición de Flemming imprime el griego conservado junto a su traducción
    alemana del etíope, y el TEI no distingue una de otra. Sin filtrar, la
    mitad del libro entraría en alemán.
    """
    return tei.leer(ruta, parte, solo_griego=True)
