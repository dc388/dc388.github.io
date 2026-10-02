"""Genera un archivo por idioma, listo para publicar y descargar.

Cada traducción sale como una base SQLite pequeña, `traduccion-<código>.db`, con
una sola tabla. La aplicación la descarga y la enchufa con ATTACH a la base
principal; por eso los nombres de tabla y columnas son los mismos que ya usa.

Se genera además `index.json`, que es lo que la aplicación consulta para saber
qué idiomas hay, cuánto pesa cada uno, qué cubre y con qué firma comprobarlo.

La cobertura se mide, no se promete: varias digitalizaciones libres están
incompletas —la danesa no trae Abdías ni Judas, la letona y la suajili son solo
Nuevo Testamento— y eso tiene que salir escrito donde el usuario lo vea antes
de descargar, no después.

    python3 tools/build_traducciones.py <carpeta de open-bibles> [<salida>]
"""

from __future__ import annotations

import gzip
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from canon import CANON
from traducciones import DISPONIBLES, leer

LIBROS_AT = [l.app for l in CANON[:39]]
LIBROS_NT = [l.app for l in CANON[39:]]

ESQUEMA = """
CREATE TABLE translation (
    book_code TEXT NOT NULL,
    chapter   INTEGER NOT NULL,
    verse     INTEGER NOT NULL,
    text      TEXT NOT NULL,
    PRIMARY KEY (book_code, chapter, verse)
) WITHOUT ROWID;
"""


def escribir(destino: Path, versiculos: dict) -> None:
    if destino.exists():
        destino.unlink()
    db = sqlite3.connect(destino)
    db.executescript(ESQUEMA)
    db.executemany(
        "INSERT INTO translation (book_code, chapter, verse, text) VALUES (?,?,?,?)",
        ((b, c, v, t) for (b, c, v), t in sorted(versiculos.items())),
    )
    db.commit()
    db.execute("VACUUM")
    db.close()


def cobertura(versiculos: dict) -> dict:
    hay = {k[0] for k in versiculos}
    at = sum(1 for b in LIBROS_AT if b in hay)
    nt = sum(1 for b in LIBROS_NT if b in hay)
    if at == 39 and nt == 27:
        resumen = "completa"
    elif at == 0:
        resumen = "solo Nuevo Testamento"
    else:
        faltan = 66 - at - nt
        resumen = "falta 1 libro" if faltan == 1 else f"faltan {faltan} libros"
    return {
        "libros_at": at,
        "libros_nt": nt,
        "versiculos": len(versiculos),
        "resumen": resumen,
        "faltan": [b for b in LIBROS_AT + LIBROS_NT if b not in hay],
    }


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    carpeta = Path(sys.argv[1])
    salida = Path(sys.argv[2] if len(sys.argv) > 2 else "build/traducciones")
    salida.mkdir(parents=True, exist_ok=True)

    indice = []
    total_comprimido = 0
    print(f"{'cód':<6}{'idioma':<14}{'versículos':>11}{'archivo':>10}{'descarga':>10}  cobertura")
    print("-" * 82)

    for t in DISPONIBLES:
        versiculos = leer(carpeta, t)
        if not versiculos:
            print(f"{t.codigo:<6}{t.idioma:<14}  SIN VERSÍCULOS — se omite")
            continue

        destino = salida / f"traduccion-{t.codigo}.db"
        escribir(destino, versiculos)
        crudo = destino.read_bytes()
        comprimido = gzip.compress(crudo, 9)
        (salida / f"traduccion-{t.codigo}.db.gz").write_bytes(comprimido)
        total_comprimido += len(comprimido)

        cob = cobertura(versiculos)
        indice.append({
            "codigo": t.codigo,
            "idioma": t.idioma,
            "version": t.version,
            "licencia": t.licencia,
            "archivo": f"traduccion-{t.codigo}.db.gz",
            "bytes_descarga": len(comprimido),
            "bytes_instalado": len(crudo),
            "sha256": hashlib.sha256(comprimido).hexdigest(),
            **cob,
        })
        print(f"{t.codigo:<6}{t.idioma:<14}{len(versiculos):>11}"
              f"{len(crudo)/1e6:>9.1f}M{len(comprimido)/1e6:>9.1f}M  {cob['resumen']}")

    indice.sort(key=lambda x: x["idioma"])
    (salida / "index.json").write_text(
        json.dumps({"version": 1, "traducciones": indice}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print("-" * 82)
    completas = sum(1 for i in indice if i["resumen"] == "completa")
    print(f"{len(indice)} idiomas · {completas} con los 66 libros · "
          f"{total_comprimido/1e6:.0f} MB en total para descargar")
    print(f"en {salida}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
