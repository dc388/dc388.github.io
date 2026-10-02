"""Los Padres Apostólicos, en la edición griega de Kirsopp Lake.

Son los escritos cristianos más antiguos fuera del Nuevo Testamento —algunos
anteriores a varios libros del canon— y los que más se citan en el estudio del
cristianismo del siglo I y II. Van en su propia colección, no mezclados con el
Nuevo Testamento, porque no son canónicos.

La fuente es First1KGreek, que publica la edición de Lake (Loeb, 1912–1917) en
TEI y con licencia CC BY-SA 4.0, la misma que ya usa la Septuaginta de Swete.

El texto no viene analizado, igual que la Septuaginta, así que se apoya en el
mismo puente de formas del Nuevo Testamento: al tocar una palabra se muestra
lo que esa misma forma significa donde sí está etiquetada.
"""

from __future__ import annotations

from pathlib import Path

import tei


PADRES = [
    ("1CLE", "1 Clemente", "Πρὸς Κορινθίους Α", "Primera carta de Clemente de Roma",
     "tlg1271.tlg001.1st1K-grc1.xml", None),
    ("2CLE", "2 Clemente", "Πρὸς Κορινθίους Β", "Segunda carta de Clemente",
     "tlg1271.tlg002.1st1K-grc1.xml", None),
    # Las siete cartas auténticas de Ignacio se editan como una sola obra
    # («Epistulae vii genuinae»), así que salen del mismo archivo: cada una es
    # una de sus divisiones, en el orden de la edición.
    ("IGEF", "Ignacio a los Efesios", "Πρὸς Ἐφεσίους", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 1),
    ("IGMA", "Ignacio a los Magnesios", "Πρὸς Μαγνησιεῖς", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 2),
    ("IGTR", "Ignacio a los Tralianos", "Πρὸς Τραλλιανούς", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 3),
    ("IGRO", "Ignacio a los Romanos", "Πρὸς Ῥωμαίους", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 4),
    ("IGFI", "Ignacio a los Filadelfios", "Πρὸς Φιλαδελφεῖς", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 5),
    ("IGES", "Ignacio a los Esmirniotas", "Πρὸς Σμυρναίους", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 6),
    ("IGPO", "Ignacio a Policarpo", "Πρὸς Πολύκαρπον", None,
     "tlg1443.tlg001.1st1K-grc1.xml", 7),
    ("POFI", "Policarpo a los Filipenses", "Πρὸς Φιλιππησίους", None,
     "tlg1622.tlg001.1st1K-grc1.xml", None),
    ("MAPO", "Martirio de Policarpo", "Μαρτύριον τοῦ Πολυκάρπου", None,
     "tlg1484.tlg001.1st1K-grc1.xml", None),
    ("DIDA", "Didaché", "Διδαχὴ τῶν δώδεκα ἀποστόλων",
     "Enseñanza de los doce apóstoles", "tlg1311.tlg001.1st1K-grc1.xml", None),
    ("BERN", "Bernabé", "Βαρνάβα ἐπιστολή", "Carta de Bernabé",
     "tlg1216.tlg001.opp-grc1.xml", None),
    ("HERM", "Pastor de Hermas", "Ποιμὴν τοῦ Ἑρμᾶ", None,
     "tlg1419.tlg001.1st1K-grc1.xml", None),
    ("DIOG", "A Diogneto", "Πρὸς Διόγνητον", "Carta a Diogneto",
     "tlg0646.tlg004.1st1K-grc1.xml", None),
]

# El Pastor de Hermas se edita en tres partes (Visiones, Mandatos, Semejanzas)
# con su propia numeración cada una. La fuente respeta esa estructura, pero la
# base guarda capítulos como números sueltos, así que se numeran de corrido:
# es la numeración continua de 1 a 114 que usan las ediciones modernas.
NOTA_HERMAS = (
    "Las Visiones, los Mandatos y las Semejanzas van seguidos en un solo "
    "recuento de capítulos, no numerados por partes."
)




def descargar(destino: Path) -> None:
    tei.descargar(destino, [p[4] for p in PADRES])


leer = tei.leer
