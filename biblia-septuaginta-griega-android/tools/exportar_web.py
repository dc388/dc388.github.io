"""Saca de la base los datos que necesita la versión web.

La aplicación de Android lleva la base entera dentro y la consulta con SQLite.
En el navegador eso no vale: son 72 MB y nadie espera a que bajen para leer un
salmo. Aquí se parte en archivos pequeños —uno por capítulo— que el servidor
manda sueltos y el navegador guarda en su caché.

Se exporta solo lo que hace falta para leer. El interlineal, el léxico y la
búsqueda son otra pieza y llevan su propia forma de servirse.

    python3 tools/exportar_web.py ../biblia-web/datos
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "app/src/main/assets/biblia.db"


def exportar(destino: Path) -> None:
    con = sqlite3.connect(BASE)
    con.row_factory = sqlite3.Row
    destino.mkdir(parents=True, exist_ok=True)

    indice: list[dict] = []
    for col in con.execute(
        "SELECT id, name, short_name, edition, license, source_url, language, rtl"
        " FROM collections ORDER BY sort_order"
    ):
        libros = []
        for libro in con.execute(
            "SELECT id, code, name_es, name_orig, alt_name, source_note, chapter_list,"
            " verse_count FROM books WHERE collection_id = ? ORDER BY sort_order",
            (col["id"],),
        ):
            libros.append({
                "codigo": libro["code"],
                "nombre": libro["name_es"],
                "original": libro["name_orig"],
                "alterno": libro["alt_name"],
                "nota": libro["source_note"],
                "capitulos": [int(c) for c in libro["chapter_list"].split(",")],
                "versiculos": libro["verse_count"],
            })
            # La carpeta lleva la colección delante porque los códigos se
            # repiten: «GEN» es Génesis en hebreo y también en la Septuaginta,
            # y son textos distintos. Sin esto uno pisaba al otro.
            exportar_libro(
                con, destino, libro["id"], col["id"], libro["code"], libro["chapter_list"]
            )

        indice.append({
            "id": col["id"],
            "nombre": col["name"],
            "corto": col["short_name"],
            "edicion": col["edition"],
            "licencia": col["license"],
            "fuente": col["source_url"],
            "lengua": col["language"],
            "rtl": bool(col["rtl"]),
            "libros": libros,
        })

    escribir(destino / "indice.json", indice)
    total = sum(len(c["libros"]) for c in indice)
    print(f"{len(indice)} colecciones, {total} libros")


def exportar_libro(
    con: sqlite3.Connection,
    destino: Path,
    libro_id: int,
    coleccion: str,
    codigo: str,
    capitulos: str,
) -> None:
    carpeta = destino / coleccion / codigo
    carpeta.mkdir(parents=True, exist_ok=True)
    for numero in (int(c) for c in capitulos.split(",")):
        versiculos = []
        for fila in con.execute(
            "SELECT v.verse, v.suffix, v.text, t.text AS espanol"
            " FROM verses v"
            " LEFT JOIN translation t"
            "   ON t.book_id = v.book_id AND t.chapter = v.chapter AND t.verse = v.verse"
            " WHERE v.book_id = ? AND v.chapter = ?"
            " ORDER BY v.verse, v.suffix",
            (libro_id, numero),
        ):
            entrada = {"v": fila["verse"], "t": fila["text"]}
            if fila["suffix"]:
                entrada["s"] = fila["suffix"]
            # La Reina-Valera solo cubre el hebreo y el Nuevo Testamento; en el
            # resto la clave sencillamente no va, y así no pesa.
            if fila["espanol"]:
                entrada["es"] = fila["espanol"]
            versiculos.append(entrada)
        escribir(carpeta / f"{numero}.json", versiculos)


def escribir(ruta: Path, datos: object) -> None:
    # Sin espacios entre las claves: en 1 400 archivos, cada byte se nota.
    ruta.write_text(
        json.dumps(datos, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
    )


def main() -> int:
    destino = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("../biblia-web/datos")
    if not BASE.exists():
        print(f"Falta la base: {BASE}. Ejecuta antes tools/build_db.py")
        return 1
    exportar(destino.resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
