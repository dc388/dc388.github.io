"""Rellena la definición en español del léxico ya exportado para la web.

build_db.py es quien manda: al construir la base pone definition_es con la
traducción a mano de definiciones.py y, donde no la hay, con la de
traducir_strong.py. exportar_web.py se limita a copiarla.

Esto hace lo mismo sobre una exportación que ya existe, sin reconstruir la base
—que tarda y requiere volver a clonar los corpus— para cuando lo único que
cambia son las tablas del traductor. El resultado es idéntico por construcción:
es la misma función sobre los mismos datos.

    python3 tools/rellenar_definiciones.py biblia/datos
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from definiciones import DEFINICIONES  # noqa: E402
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
        archivo.write_text(
            json.dumps(entradas, ensure_ascii=False, separators=(",", ":")),
            encoding="utf-8",
        )
    return mano, automaticas, sin_traducir


if __name__ == "__main__":
    destino = Path(sys.argv[1] if len(sys.argv) > 1 else "biblia/datos")
    mano, automaticas, sin_traducir = rellenar(destino)
    print(f"a mano {mano}  automáticas {automaticas}  sin traducir {sin_traducir}")
