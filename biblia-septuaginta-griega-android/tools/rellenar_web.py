"""Completa una exportación web ya hecha, sin reconstruir la base.

build_db.py es quien manda: al construir la base pone definition_es con la
traducción a mano de definiciones.py y, donde no la hay, con la de
traducir_strong.py. exportar_web.py se limita a copiarla.

Esto hace lo mismo sobre una exportación que ya existe, sin reconstruir la base
—que tarda y requiere volver a clonar los corpus— para cuando lo único que
cambia son las tablas del traductor. El resultado es idéntico por construcción:
es la misma función sobre los mismos datos.

    python3 tools/rellenar_web.py biblia/datos
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import canonicidad  # noqa: E402
from traducciones_propias import PROPIAS  # noqa: E402
from definiciones import DEFINICIONES  # noqa: E402
from traducir_articulo import traducir_articulo  # noqa: E402
from traducir_strong import traducir  # noqa: E402


def rellenar(destino: Path) -> tuple[int, int, int]:
    mano = automaticas = sin_traducir = 0
    for archivo in sorted((destino / "lexico").glob("*.json")):
        entradas = json.loads(archivo.read_text(encoding="utf-8"))
        for strong, entrada in entradas.items():
            espanol = DEFINICIONES.get(strong)
            if espanol:
                mano += 1
            else:
                espanol = traducir(entrada.get("definicion"))
                if espanol:
                    automaticas += 1
                elif entrada.get("definicion"):
                    sin_traducir += 1
            entrada["definicion_es"] = espanol
            for articulo in (entrada.get("articulos") or {}).values():
                articulo["texto_es"] = traducir_articulo(articulo.get("texto"))
        archivo.write_text(
            json.dumps(entradas, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
    return mano, automaticas, sin_traducir


def traducir_a_mano(destino: Path) -> tuple[int, int]:
    """Pone las traducciones hechas a mano en los libros que no tienen otra.

    Lo mismo que hace build_db.py al construir la base. Recorre el registro de
    traducciones_propias.py, así que un libro nuevo no necesita tocar esto.
    """
    puestos = total = 0
    for (coleccion, codigo), libro in PROPIAS.items():
        carpeta = destino / coleccion / codigo
        if not carpeta.is_dir():
            continue
        for archivo in carpeta.glob("*.json"):
            capitulo = int(archivo.stem)
            versiculos = json.loads(archivo.read_text(encoding="utf-8"))
            for entrada in versiculos:
                total += 1
                espanol = libro.get((capitulo, entrada["v"], entrada.get("s", "")))
                if espanol:
                    entrada["es"] = espanol
                    puestos += 1
                else:
                    entrada.pop("es", None)
            archivo.write_text(
                json.dumps(versiculos, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8",
            )
    return puestos, total


def clasificar(destino: Path) -> int:
    """Marca cada libro del índice con su clase: canon, deuterocanónico, etc.

    Lo mismo que hace exportar_web.py al exportar; aquí se aplica sobre el
    índice que ya está publicado.
    """
    ruta = destino / "indice.json"
    indice = json.loads(ruta.read_text(encoding="utf-8"))
    for coleccion in indice:
        for libro in coleccion["libros"]:
            libro["canon"] = canonicidad.clase(coleccion["id"], libro["codigo"])
    ruta.write_text(
        json.dumps(indice, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )
    return sum(len(c["libros"]) for c in indice)


if __name__ == "__main__":
    destino = Path(sys.argv[1] if len(sys.argv) > 1 else "biblia/datos")
    mano, automaticas, sin_traducir = rellenar(destino)
    print(f"a mano {mano}  automáticas {automaticas}  sin traducir {sin_traducir}")
    print(f"{clasificar(destino)} libros clasificados por canonicidad")
    puestos, total = traducir_a_mano(destino)
    print(f"traducción propia: {puestos} de {total} versículos")
