"""Limpiar el inglés que quedó pegado en las definiciones del léxico.

Por qué hace falta
------------------
Las definiciones de Strong salieron en su día de la King James, y al pasarlas
al español quedaron tres cosas a medias. Mientras el diccionario vivía dentro
del lector se veían poco; ahora que cada palabra tiene su página, se leen.

  1. El posesivo inglés sin dar la vuelta: «Moses' esposa», «Saul's hija»,
     «Isaiah's hijo». 35 casos.
  2. El adjetivo delante del sustantivo, que es orden inglés: «un asirio rey»,
     «el babilonio nombre», «un simbólico nombre». 149 casos, y con ellos se
     arrastra la concordancia: «un filisteo ciudad» por «una ciudad filistea».
  3. Nombres propios en la forma inglesa antigua: «Messias» por «Mesías»,
     «Solomon» por «Salomón», «Achaz» por «Acaz». 47 casos.

Cómo se corrige
---------------
Con tablas escritas a mano, no con reglas que adivinen. Cada entrada de estas
tablas se ha mirado antes en su contexto y contra el inglés original, porque
en esto las reglas listas se equivocan de una forma que además parece
correcta. Tres ejemplos de por qué:

  * «la propia mano» y «la propia miseria» NO están mal: «propio» delante del
    sustantivo es español correcto («de su propia mano»). Una regla que diera
    la vuelta a todo adjetivo las habría estropeado. «un propio nombre» sí
    está mal, porque ahí es «nombre propio». Por eso «propio» no entra en la
    regla general y ese caso va suelto.
  * «Zacharias (es decir, Zechariah)»: el primero es la forma griega y el
    segundo la hebrea. Se corrige el de fuera y se deja el de dentro del
    paréntesis, que es una transliteración y tiene que seguir siéndolo, como
    «Mashiach» o «Korach».
  * Abraham, Jacob, David, Daniel, Isaac, Job, Amós y Joel se escriben igual
    en inglés y en español. No se tocan.

Lo que se deja como está
------------------------
«como el sagrado lleno uno», del inglés «as the sacred full one» (el siete
como número de la plenitud). El inglés de Strong ya es oscuro ahí y cualquier
arreglo sería interpretar por él, así que se queda.

Esto trabaja sobre el léxico ya exportado a la web, que es donde vive el dato:
la base de datos de la que salió no está en este repositorio.
"""

from __future__ import annotations

import json
import pathlib
import re
import sys

# 1. El posesivo inglés. Cada uno mirado en su contexto: el orden en español
#    no sale de una regla, porque «Joseph's Egyptian name» es «el nombre
#    egipcio de José» y no «el egipcio nombre de José».
POSESIVOS = {
    "Abraham's el mayor hijo": "el hijo mayor de Abraham",
    "Abraham's esposa": "la esposa de Abraham",
    "Abraham's sobrino": "el sobrino de Abraham",
    "Adam's hogar": "el hogar de Adán",
    "Christ's espíritu": "el espíritu de Cristo",
    "Daniel's compañeros": "los compañeros de Daniel",
    "David's padre": "el padre de David",
    "David's sucesor": "el sucesor de David",
    "Haman's esposa": "la esposa de Amán",
    "Hezekiah's madre": "la madre de Ezequías",
    "Isaiah's hijos": "los hijos de Isaías",
    "Isaiah's hijo": "el hijo de Isaías",
    "Jacob's hijos": "los hijos de Jacob",
    "Job's amigos": "los amigos de Job",
    "Job's hijas": "las hijas de Job",
    "Joseph's egipcio nombre": "el nombre egipcio de José",
    "Mars' colina": "la colina de Marte",
    "Moses' esposa": "la esposa de Moisés",
    "Moses' suegro": "el suegro de Moisés",
    "Nebuchadnezzar's jefe eunuco": "el jefe de los eunucos de Nabucodonosor",
    "Saul's hija": "la hija de Saúl",
    "'Solomon's de los siervos": "los siervos de Salomón",
    "Zerubbabel's persa nombre": "el nombre persa de Zorobabel",
}

# 2. Adjetivo y sustantivo, al revés. La tabla dice el género de cada
#    sustantivo, porque de ahí sale el artículo y la terminación.
GENERO = {
    "caudillo": "m", "centinela": "m", "ciudad": "f", "cristiano": "m",
    "deidad": "f", "emperador": "m", "epíteto": "m", "eunuco": "m",
    "general": "m", "heroína": "f", "imperio": "m", "juez": "m",
    "legislador": "m", "lengua": "f", "lugar": "m", "mes": "m", "mujer": "f",
    "nombre": "m", "ocasión": "f", "oficial": "m", "patriarca": "m",
    "persona": "f", "príncipe": "m", "profeta": "m", "pueblo": "m",
    "reina": "f", "rey": "m", "sentido": "m", "sátrapa": "m", "templo": "m",
    "tribu": "f", "título": "m", "visir": "m", "ídolo": "m",
}

# La forma masculina y femenina de cada adjetivo. Los invariables se repiten.
ADJETIVOS = {
    "adoptado": ("adoptado", "adoptada"),
    "asirio": ("asirio", "asiria"),
    "babilonio": ("babilonio", "babilonia"),
    "colectivo": ("colectivo", "colectiva"),
    "dado": ("dado", "dada"),
    "egipcio": ("egipcio", "egipcia"),
    "elevado": ("elevado", "elevada"),
    "figurado": ("figurado", "figurada"),
    "filisteo": ("filisteo", "filistea"),
    "fortificado": ("fortificado", "fortificada"),
    "israelita": ("israelita", "israelita"),
    "judío": ("judío", "judía"),
    "persa": ("persa", "persa"),
    "romano": ("romano", "romana"),
    "simbólico": ("simbólico", "simbólica"),
    "sirio": ("sirio", "siria"),
    "señalado": ("señalado", "señalada"),
    "árabe": ("árabe", "árabe"),
}

ARTICULOS = {
    "un": {"m": "un", "f": "una"},
    "una": {"m": "un", "f": "una"},
    "el": {"m": "el", "f": "la"},
    "la": {"m": "el", "f": "la"},
    "los": {"m": "los", "f": "las"},
    "las": {"m": "los", "f": "las"},
}

_ORDEN = re.compile(
    r"\b(un|una|el|la|los|las)\s+(" + "|".join(ADJETIVOS) + r")\s+("
    + "|".join(GENERO) + r")\b"
)

# Casos que la regla no coge porque llevan dos palabras detrás o porque el
# adjetivo queda fuera de la tabla a propósito.
ORDEN_SUELTOS = {
    "un israelita sumo sacerdote": "un sumo sacerdote israelita",
    "un propio nombre": "un nombre propio",
    "un tipo nombre": "un nombre simbólico",
    "la mayoría lugar santo": "el lugar santísimo",
    "la personas pueblo (joven)": "las personas (gente joven)",
    "un enfrente tribu": "una tribu contraria",
}

# 3. Nombres propios en la forma inglesa antigua. Solo los que en español se
#    escriben distinto: Abraham, Jacob, David, Daniel, Isaac, Job, Amós y Joel
#    no están aquí porque se escriben igual.
NOMBRES = {
    "Achaz": "Acaz", "Chanaan": "Canaán", "Core": "Coré", "Elijah": "Elías",
    "Elisha": "Eliseo", "Ezekias": "Ezequías", "Hosea": "Oseas",
    "Isaiah": "Isaías", "Joatham": "Joatam", "Jonah": "Jonás",
    "Jonas": "Jonás", "Josias": "Josías", "Messias": "Mesías",
    "Micah": "Miqueas", "Moses": "Moisés", "Naasson": "Naasón",
    "Ozias": "Ozías", "Rachab": "Rahab", "Ruth": "Rut", "Salathiel": "Salatiel",
    "Salmon": "Salmón", "Saul": "Saúl", "Solomon": "Salomón",
    "Zabulon": "Zabulón", "Zacharias": "Zacarías",
    # Forma griega de Elías, como la escribe la King James.
    "Helias": "Elías",
}

# Citas bíblicas con el libro en inglés: «(Isaiah 41:9)». Van aparte de los
# nombres propios porque están dentro de un paréntesis, y ahí la regla de los
# nombres no entra a propósito, para no estropear las transliteraciones.
LIBROS_CITADOS = {
    "Isaiah": "Isaías", "Jeremiah": "Jeremías", "Ezekiel": "Ezequiel",
    "Hosea": "Oseas", "Joel": "Joel", "Amos": "Amós", "Obadiah": "Abdías",
    "Jonah": "Jonás", "Micah": "Miqueas", "Nahum": "Nahúm",
    "Habakkuk": "Habacuc", "Zephaniah": "Sofonías", "Haggai": "Ageo",
    "Zechariah": "Zacarías", "Malachi": "Malaquías", "Psalms": "Salmos",
    "Proverbs": "Proverbios", "Genesis": "Génesis", "Exodus": "Éxodo",
    "Leviticus": "Levítico", "Numbers": "Números",
    "Deuteronomy": "Deuteronomio", "Joshua": "Josué", "Judges": "Jueces",
    "Ruth": "Rut", "Samuel": "Samuel", "Kings": "Reyes",
    "Chronicles": "Crónicas", "Ezra": "Esdras", "Nehemiah": "Nehemías",
    "Esther": "Ester", "Job": "Job", "Daniel": "Daniel",
}


# Gentilicios femeninos en inglés, que el traductor dejó enteros.
GENTILICIOS = {
    "Canaanitess": "cananea", "Edomitess": "edomita", "Hebrewess": "hebrea",
    "Jezreelitess": "jezreelita", "Jisreelitess": "jezreelita",
    "Karmelitess": "carmelita", "Midianitess": "madianita",
    "Ishmaelitess": "ismaelita", "Moabitess": "moabita",
    "Samaritess": "samaritana",
    "Shunammitess": "sunamita",
}


def da_la_vuelta(m: re.Match) -> str:
    articulo, adjetivo, sustantivo = m.group(1), m.group(2), m.group(3)
    genero = GENERO[sustantivo]
    art = ARTICULOS[articulo][genero]
    adj = ADJETIVOS[adjetivo][0 if genero == "m" else 1]
    return f"{art} {sustantivo} {adj}"


def corrige(texto: str) -> str:
    """Las tres pasadas, en este orden y no en otro.

    Los posesivos van primero porque llevan dentro nombres ingleses («Moses'
    suegro») y hay que quitarlos antes de que la pasada de nombres los toque
    a medias. Los sueltos del orden van antes que la regla general por la
    misma razón: son más largos y la regla se comería su principio.
    """
    for viejo, nuevo in POSESIVOS.items():
        texto = texto.replace(viejo, nuevo)
    for viejo, nuevo in ORDEN_SUELTOS.items():
        texto = texto.replace(viejo, nuevo)
    texto = _ORDEN.sub(da_la_vuelta, texto)
    for viejo, nuevo in GENTILICIOS.items():
        # El artículo se arregla aquí, pegado a la forma inglesa, y no después
        # sobre la palabra española ya puesta.
        #
        # Haberlo hecho después costó 39 errores: los gentilicios en -ess son
        # femeninos («Rachab, a Canaanitess» pide «una cananea»), pero
        # «edomita», «moabita» o «madianita» sin más son masculinos la mayoría
        # de las veces, y la pasada de después convirtió en mujeres a Esaú,
        # Balac, Doeg y otros treinta y seis. Pegado a la forma inglesa no
        # puede pasar: solo toca donde de verdad había un -ess.
        texto = re.sub(rf"\bun\s+{viejo}\b", f"una {nuevo}", texto)
        texto = re.sub(rf"\b{viejo}\b", nuevo, texto)
    for viejo, nuevo in NOMBRES.items():
        # Fuera de los paréntesis nada más: «Zacharias (es decir, Zechariah)»
        # lleva dentro la forma hebrea, que es una transliteración y se queda.
        texto = re.sub(rf"\b{viejo}\b(?![^()]*\))", nuevo, texto)
    for viejo, nuevo in LIBROS_CITADOS.items():
        texto = re.sub(rf"\b{viejo}(?=\s+\d)", nuevo, texto)
    # «de el hijo» -> «del hijo», que lo deja la vuelta del posesivo.
    texto = re.sub(r"\bde el\b", "del", texto)
    texto = re.sub(r"\buno de las\b", "una de las", texto)
    return texto


def main(carpeta: pathlib.Path) -> None:
    tocadas = archivos = 0
    for ruta in sorted((carpeta / "datos" / "lexico").glob("*.json")):
        d = json.loads(ruta.read_text(encoding="utf-8"))
        cambiado = False
        for entrada in d.values():
            vieja = entrada.get("definicion_es")
            if not vieja:
                continue
            nueva = corrige(vieja)
            if nueva != vieja:
                entrada["definicion_es"] = nueva
                tocadas += 1
                cambiado = True
        if cambiado:
            ruta.write_text(
                json.dumps(d, ensure_ascii=False, separators=(",", ":")),
                encoding="utf-8")
            archivos += 1
    print(f"definiciones corregidas: {tocadas}   archivos reescritos: {archivos}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("uso: corregir_glosas.py <carpeta biblia/>")
    main(pathlib.Path(sys.argv[1]).resolve())
