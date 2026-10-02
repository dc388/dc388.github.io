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
from tobias_es import TOBIAS_ES
from enoc_es import ENOC_ES
from judit_es import JUDIT_ES
from eclesiastico_es import ECLESIASTICO_ES
from esdras1_es import ESDRAS1_ES
from sabiduria_es import SABIDURIA_ES
from macabeos1_es import MACABEOS1_ES
from macabeos2_es import MACABEOS2_ES
from macabeos3_es import MACABEOS3_ES
from macabeos4_es import MACABEOS4_ES
from odas_es import ODAS_ES
from salmos_salomon_es import SALMOS_SALOMON_ES
from susana_es import SUSANA_ES, SUSANA_TEODOCION_ES

# Los Padres Apostólicos, una obra por módulo.
from clemente1_es import CLEMENTE1_ES
from clemente2_es import CLEMENTE2_ES
from ignacio_efesios_es import IGNACIO_EFESIOS_ES
from ignacio_magnesios_es import IGNACIO_MAGNESIOS_ES
from ignacio_tralianos_es import IGNACIO_TRALIANOS_ES
from ignacio_romanos_es import IGNACIO_ROMANOS_ES
from ignacio_filadelfios_es import IGNACIO_FILADELFIOS_ES
from ignacio_esmirniotas_es import IGNACIO_ESMIRNIOTAS_ES
from ignacio_policarpo_es import IGNACIO_POLICARPO_ES
from policarpo_filipenses_es import POLICARPO_FILIPENSES_ES
from martirio_policarpo_es import MARTIRIO_POLICARPO_ES
from didache_es import DIDACHE_ES
from bernabe_es import BERNABE_ES
from hermas_es import HERMAS_ES
from diogneto_es import DIOGNETO_ES

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
    ("lxx", "TOB"): _con_sufijo(TOBIAS_ES),
    ("lxx", "JDT"): _con_sufijo(JUDIT_ES),
    ("lxx", "SAB"): _con_sufijo(SABIDURIA_ES),
    ("lxx", "SIR"): _con_sufijo(ECLESIASTICO_ES),
    ("lxx", "1ES"): _con_sufijo(ESDRAS1_ES),
    ("lxx", "SSA"): _con_sufijo(SALMOS_SALOMON_ES),
    ("lxx", "1MA"): _con_sufijo(MACABEOS1_ES),
    ("lxx", "2MA"): _con_sufijo(MACABEOS2_ES),
    ("lxx", "3MA"): _con_sufijo(MACABEOS3_ES),
    ("lxx", "4MA"): _con_sufijo(MACABEOS4_ES),
    ("lxx", "ODA"): _con_sufijo(ODAS_ES),
    ("padres", "1CLE"): _con_sufijo(CLEMENTE1_ES),
    ("padres", "2CLE"): _con_sufijo(CLEMENTE2_ES),
    ("padres", "IGEF"): _con_sufijo(IGNACIO_EFESIOS_ES),
    ("padres", "IGMA"): _con_sufijo(IGNACIO_MAGNESIOS_ES),
    ("padres", "IGTR"): _con_sufijo(IGNACIO_TRALIANOS_ES),
    ("padres", "IGRO"): _con_sufijo(IGNACIO_ROMANOS_ES),
    ("padres", "IGFI"): _con_sufijo(IGNACIO_FILADELFIOS_ES),
    ("padres", "IGES"): _con_sufijo(IGNACIO_ESMIRNIOTAS_ES),
    ("padres", "IGPO"): _con_sufijo(IGNACIO_POLICARPO_ES),
    ("padres", "POFI"): _con_sufijo(POLICARPO_FILIPENSES_ES),
    ("padres", "MAPO"): _con_sufijo(MARTIRIO_POLICARPO_ES),
    ("padres", "DIDA"): _con_sufijo(DIDACHE_ES),
    ("padres", "BERN"): _con_sufijo(BERNABE_ES),
    ("padres", "HERM"): _con_sufijo(HERMAS_ES),
    ("padres", "DIOG"): _con_sufijo(DIOGNETO_ES),
}


def versiculos() -> int:
    """Cuántos versículos hay traducidos, para poder decirlo sin estimarlo."""
    return sum(len(libro) for libro in PROPIAS.values())
