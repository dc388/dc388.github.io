#!/usr/bin/env python3
"""Material para escribir una entrada del versículo del día.

Cada reflexión del versículo del día tiene que decir algo de UNA palabra del
original que la traducción no alcanza a decir, y tiene que poder sostenerse con
lo que la propia aplicación trae dentro: el texto, el análisis morfológico y el
léxico. Escribirlas de memoria es como se cuela un matiz inventado —ya pasó una
vez, con Isaías 41:10— así que esto junta el material antes de escribir nada.

    python3 tools/versiculo_del_dia.py at SAL 27 14
    python3 tools/versiculo_del_dia.py nt JUA 1 1

Imprime el texto original, la traducción publicada, y para cada palabra su
número Strong, su análisis morfológico desplegado y la definición del léxico.
No decide nada: la reflexión la escribe una persona mirando esto.
"""

import json
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent.parent / "biblia" / "datos"

# La misma tabla que muestra la aplicación, ya en español: el griego de
# Robinson y el hebreo de OSHB en el mismo diccionario.
MORFOLOGIA = json.load((RAIZ / "morfologia.json").open())


def entrada_lexico(strong):
    """El artículo del léxico. Los archivos van de mil en mil: G25 está en G0."""
    if not strong or not strong[1:].isdigit():
        return None
    archivo = RAIZ / "lexico" / f"{strong[0]}{int(strong[1:]) // 1000}.json"
    if not archivo.exists():
        return None
    return json.load(archivo.open()).get(strong)


def main(coleccion, codigo, capitulo, versiculo):
    texto = json.load((RAIZ / coleccion / codigo / f"{capitulo}.json").open())
    fila = next((x for x in texto if x["v"] == versiculo), None)
    if fila is None:
        sys.exit(f"{codigo} {capitulo}:{versiculo} no existe en {coleccion}")

    print(f"=== {codigo} {capitulo}:{versiculo} ({coleccion}) ===")
    print("ORIGINAL:", fila["t"])
    print("ESPAÑOL :", fila.get("es") or "(esta colección no lleva traducción)")

    analisis = RAIZ / coleccion / codigo / f"{capitulo}.palabras.json"
    if not analisis.exists():
        print("\n(texto sin análisis morfológico)")
        return
    palabras = json.load(analisis.open()).get(str(versiculo), [])
    print()
    for forma, strong, homonimo, morf in palabras:
        e = entrada_lexico(strong) or {}
        lema = e.get("lema", "?")
        definicion = e.get("definicion_es") or e.get("definicion") or ""
        print(f"{forma}  [{strong}{homonimo}]  {morf}")
        print(f"    {lema} — {MORFOLOGIA.get(morf, '(sin descripción)')}")
        if definicion:
            print(f"    {definicion[:160]}")
        articulo = (e.get("articulos") or {}).get(homonimo) or {}
        bdb = articulo.get("texto_es") or articulo.get("texto")
        if bdb:
            print("    BDB:", bdb.replace("\n", " / ")[:220])
        print()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
