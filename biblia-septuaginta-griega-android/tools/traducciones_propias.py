"""Las traducciones al español hechas a mano para esta aplicación.

La Reina-Valera cubre los 66 libros del canon y nada más. Todo lo demás de esta
biblioteca —los apócrifos, los pseudoepígrafos y los Padres Apostólicos— no
tiene traducción española libre que copiar: lo comprobé contra las cuatro
Biblias en dominio público que existen en español (Reina-Valera 1909, Biblia en
Español Sencillo, Palabra de Dios para Ti, Versión Biblia Libre) y las cuatro
traen los 66 y ninguno más.

Así que se traducen aquí, a mano y del griego, libro por libro. Este módulo es
el único sitio donde se registran: build_db.py y rellenar_web.py recorren esta
tabla y no saben nada de cada libro en particular, así que añadir uno nuevo es
escribir su módulo y añadir una línea aquí.

Cada libro va en su propio archivo porque son miles de versículos y un archivo
de todos sería inmanejable. El criterio de traducción es el mismo en todos y
está escrito en la cabecera de cada uno: se traduce del griego que está en la
aplicación y no de una traducción inglesa; las lagunas se marcan con […] en vez
de coserlas en silencio; los corchetes del editor griego se conservan.
"""

from __future__ import annotations

from baruc_es import BARUC_ES
from bel_es import BEL_ES, BEL_TEODOCION_ES
from carta_jeremias_es import CARTA_JEREMIAS_ES
from enoc_es import ENOC_ES
from susana_es import SUSANA_ES, SUSANA_TEODOCION_ES

def _con_sufijo(libro: dict) -> dict[tuple[int, int, str], str]:
    """Admite claves de dos elementos y las completa con el sufijo vacío.

    La clave es (capítulo, versículo, sufijo). El sufijo es la letra de los
    versículos partidos —Susana tiene dos «35» y tres «62»—, y en los libros que
    no los tienen se puede omitir.
    """
    return {
        clave if len(clave) == 3 else (clave[0], clave[1], ""): texto
        for clave, texto in libro.items()
    }


# {(colección, código de libro): {(capítulo, versículo, sufijo): texto}}
PROPIAS: dict[tuple[str, str], dict[tuple[int, int, str], str]] = {
    ("pseudo", "ENOC"): _con_sufijo(ENOC_ES),
    ("lxx", "SUS"): _con_sufijo(SUSANA_ES),
    ("lxx", "SUT"): _con_sufijo(SUSANA_TEODOCION_ES),
    ("lxx", "BEL"): _con_sufijo(BEL_ES),
    ("lxx", "BET"): _con_sufijo(BEL_TEODOCION_ES),
    ("lxx", "CJE"): _con_sufijo(CARTA_JEREMIAS_ES),
    ("lxx", "BAR"): _con_sufijo(BARUC_ES),
}


def versiculos() -> int:
    """Cuántos versículos hay traducidos, para poder decirlo sin estimarlo."""
    return sum(len(libro) for libro in PROPIAS.values())
