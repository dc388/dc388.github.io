"""Traductor de los artículos de Brown-Driver-Briggs y Abbott-Smith.

Son las dos obras de referencia de la ficha, y estaban enteras en inglés. No son
prosa corrida: son entradas de léxico técnico, donde conviven cuatro cosas
distintas —el lema en hebreo o griego, el aparato de referencias (Jb 8:12, LXX,
WH), las abreviaturas gramaticales (n.m., cstr., Hiph.) y, entre medias, la
prosa inglesa que dice lo que significa la palabra—. Sólo esa última hace falta
traducirla; las otras tres se pasan intactas, porque una referencia bíblica y un
código de conjugación no están en ningún idioma.

La mitad de los artículos de BDB son listas cortas de acepciones —la mediana son
48 caracteres— y ésas salen enteras. Los densos, los que van llenos de aparato
crítico y discusión filológica, no salen, y se quedan en inglés: rige la misma
regla que en traducir_strong.py, y por el mismo motivo. Si un solo tramo de
prosa no se resuelve, el artículo entero se queda como estaba. Media entrada en
español y media en inglés no se lee, y peor aún, no se sabe de cuál fiarse.

Las abreviaturas sí se abren: «n.pr.m.» dice «nombre propio de varón» y «cstr.»
dice «constructo», porque son justo lo que deja fuera al lector que no ha
estudiado con estas obras. Los nombres de las conjugaciones hebreas —Qal, Piel,
Hifil— se quedan como están: se usan igual en español.
"""

from __future__ import annotations

import re

from traducir_strong import PALABRAS, desconocidas, traducir

# Abreviaturas de las dos obras. Se abren enteras: son la barrera de entrada
# para quien no se crió leyendo léxicos ingleses.
SIGLAS: dict[str, str] = {
    "vb.": "verbo", "vb": "verbo",
    "n.m.": "sustantivo masculino", "n.f.": "sustantivo femenino",
    "n.[m.]": "sustantivo [masculino]", "n.[f.]": "sustantivo [femenino]",
    "n.pr.m.": "nombre propio de varón", "n.pr.f.": "nombre propio de mujer",
    "n.pr.loc.": "nombre propio de lugar", "n.pr.": "nombre propio",
    "n.pr.mont.": "nombre propio de monte", "n.pr.fl.": "nombre propio de río",
    "n.pr.gent.": "nombre propio gentilicio", "n.pr.dei": "nombre propio de dios",
    "n.pr.terr.": "nombre propio de territorio", "n.pr.pers.": "nombre propio de persona",
    "adj.": "adjetivo", "adj.gent.": "adjetivo gentilicio", "adv.": "adverbio",
    "prep.": "preposición", "conj.": "conjunción", "interj.": "interjección",
    "pron.": "pronombre", "subst.": "sustantivo", "part.": "partícula",
    "ptcp.": "participio", "inf.": "infinitivo", "impf.": "imperfecto",
    "pf.": "perfecto", "imv.": "imperativo", "juss.": "yusivo",
    "sf.": "sufijo", "sfs.": "sufijos", "cstr.": "constructo",
    "absol.": "absoluto", "abs.": "absoluto", "acc.": "acusativo",
    "gen.": "genitivo", "dat.": "dativo", "nom.": "nominativo",
    "voc.": "vocativo", "pl.": "plural", "sg.": "singular", "du.": "dual",
    "coll.": "colectivo", "pers.": "persona", "c.": "con",
    "fig.": "figuradamente", "metaph.": "metafóricamente",
    "lit.": "literalmente", "esp.": "sobre todo", "freq.": "frecuente",
    "rare": "raro", "usu.": "por lo común", "prob.": "probablemente",
    "perh.": "quizá", "opp.": "opuesto a", "seq.": "seguido de",
    "id.": "ídem", "ib.": "ibídem", "sim.": "semejante",
    "cf.": "compárese", "v.": "véase", "v.s.": "véase arriba",
    "q.v.": "véase", "s.v.": "s. v.", "al.": "y otros", "al.;": "y otros;",
    "al.)": "y otros)", "al.):": "y otros):", "al.,": "y otros,",
    "etc.": "etc.", "etc.;": "etc.;", "i.e.": "es decir", "e.g.": "por ejemplo",
    "denom.": "denominativo", "cl.": "en griego clásico",
    "pass.": "en pasiva", "pass.,": "en pasiva,", "act.": "en activa",
    "mid.": "en media", "intrans.": "intransitivo", "trans.": "transitivo",
    "rel.": "relativo", "interrog.": "interrogativo", "neg.": "negativo",
    "dimin.": "diminutivo", "onomatop.": "onomatopéyico",
    "SYN.:": "SINÓNIMOS:", "Metaph.,": "Metafóricamente,",
    "rei,": "de la cosa,", "rei": "de la cosa",
}

# Más abreviaturas, las que faltaban al medir: las dos obras las usan a cientos.
SIGLAS.update({
    "SYN.": "SINÓNIMOS", "syn.": "sinónimo", "Metaph.": "Metafóricamente",
    "rei": "de la cosa", "pers.": "de la persona", "loc.": "de lugar",
    "temp.": "de tiempo", "constr.": "construcción", "consec.": "consecutivo",
    "conjc.": "conjetura", "prec.": "precedente", "foll.": "siguiente",
    "pred.": "predicado", "poss.": "posesivo", "artic.": "con artículo",
    "anarth.": "sin artículo", "demonstr.": "demostrativo",
    "prepositive": "prepositivo", "aor.": "aoristo", "praes.": "presente",
    "pres.": "presente", "fut.": "futuro", "impf.": "imperfecto",
    "subj.": "subjuntivo", "subjc.": "subjuntivo", "optat.": "optativo",
    "imperat.": "imperativo", "indic.": "indicativo", "irreg.": "irregular",
    "partit.": "partitivo", "appos.": "aposición", "apodosis": "apódosis",
    "protasis": "prótasis", "cogn.": "cognado", "spec.": "en especial",
    "specif.": "específicamente", "gent.": "gentilicio", "concr.": "en concreto",
    "abstr.": "en abstracto", "indef.": "indefinido", "def.": "definido",
    "masc.": "masculino", "fem.": "femenino", "neut.": "neutro",
    "sq.": "seguido de", "seq.": "seguido de", "oft.": "a menudo",
    "sts.": "a veces", "supr.": "arriba", "infr.": "abajo",
    "appar.": "al parecer", "qual.": "cualitativo", "contr.": "contracto",
    "conjug.": "conjugación", "frequentat.": "frecuentativo",
    "et": "y", "ff.": "y siguientes", "ff": "y siguientes",
    "mult.": "múltiple", "om.": "omite", "txt.": "texto", "mg.": "margen",
    "ref.": "referencia", "dub.": "dudoso", "orat.": "oración",
    "dir.": "directo", "fin.": "final", "phr.": "frase", "ph.": "frase",
    "exc.": "excepto", "estc.": "et cetera", "eb.": "hebreo",
    "Heb.": "hebreo", "Aram.": "arameo", "Syr.": "siríaco", "Ar.": "árabe",
    "Pers.": "persa", "Egypt.": "egipcio", "Phoen.": "fenicio",
    "Sab.": "sabeo", "Eth.": "etiópico", "Arab.": "árabe", "Assyr.": "asirio",
    "st": "º", "nd": "º", "rd": "º", "th": "º",
    "ff.": "y ss.", "vv.": "vv.", "ps": "Sal", "ll.": "ll.",
    "relat.": "relativo", "obj.": "objeto", "preps.": "preposiciones",
    "sc.": "a saber", "bef.": "antes de", "pr.": "propio",
    "accus.": "acusativo", "instr.": "instrumental", "demonstr.": "demostrativo",
    "abl.": "ablativo", "dupl.": "duplicado", "recipr.": "recíproco",
    "imper.": "imperativo", "seld.": "raras veces", "vbs.": "verbos",
    "intens.": "intensivo", "vir.": "varón", "ex.": "ejemplo",
    "comp.": "comparativo", "fr.": "de", "loc.": "de lugar",
    "superl.": "superlativo", "comm.": "común", "plpf.": "pluscuamperfecto",
    "wh.": "que", "sch.": "escolio", "disting.": "distinguido de",
    "incl.": "incluido", "indecl.": "indeclinable", "delib.": "deliberativo",
    "reff.": "referencias", "mng.": "significado", "mngs.": "significados",
    "terr.": "territorio", "exx.": "ejemplos", "etym.": "etimología",
    "infin.": "infinitivo", "num.": "numeral", "ans.": "respuesta",
    "personif.": "personificado", "impers.": "impersonal",
    "interrog.": "interrogativo", "indir.": "indirecto",
    "hypoth.": "hipotético", "praegn.": "en sentido pregnante",
    "praegnans": "pregnante", "praeg.": "pregnante", "constructio": "construcción",
    "refl.": "reflexivo", "combin.": "combinación", "ellips.": "elipsis",
    "pt.": "participio", "pts.": "participios", "periphr.": "perifrástico",
    "eccl.": "eclesiástico", "genl.": "general", "colloq.": "coloquial",
    "circumst.": "circunstancia", "depon.": "deponente", "predic.": "predicativo",
    "vocat.": "vocativo", "cit.": "citado", "op.": "obra",
    "implic.": "por implicación", "commod.": "de provecho", "opt.": "optativo",
    "rhet.": "retórico", "intr.": "intransitivo", "techn.": "técnico",
    "correlat.": "correlativo", "imp.": "imperativo", "vol.": "volumen",
    "attrib.": "atributivo", "alw.": "siempre", "coll.": "colectivo",
    "durat.": "durativo", "cstr.": "constructo", "collat.": "colateral",
    "ind.": "indicativo", "proph.": "profético", "var.": "variante",
    "vernac.": "lengua vernácula", "trop.": "en sentido figurado",
    "post-positive": "pospositivo", "phem.": "eufemismo",
    "expl.": "explicación", "diff.": "distinto", "ordin.": "ordinal",
    "equiv.": "equivalente", "causat.": "causativo", "correl.": "correlativo",
    "copul.": "copulativo", "asynd.": "asíndeton", "epexeg.": "epexegético",
    "pleonast.": "pleonástico", "topogr.": "topográfico",
    "contemp.": "contemporáneo", "fpl.": "femenino plural",
    "identif.": "identificado", "propr.": "propio", "trib.": "tribu",
    "gentilic.": "gentilicio", "elsewh.": "en otro lugar", "betw.": "entre",
    "init.": "al principio", "der.": "derivado", "aft.": "después",
    "sthg.": "algo", "cent.": "siglo", "pp.": "págs.", "ms.": "manuscrito",
    "bks.": "libros", "nn.": "notas", "ell.": "elipsis", "indep.": "independiente",
    "f.": "femenino", "m.": "masculino", "art.": "artículo",
    "poet.": "poético", "exclam.": "exclamación", "onomat.": "onomatopéyico", "prob": "probablemente",
    "adj.": "adjetivo", "num.": "numeral", "ord.": "ordinal",
    "card.": "cardinal", "distrib.": "distributivo", "emph.": "enfático",
    "abbrev.": "abreviado", "corrupt.": "corrupción", "txt": "texto",
    "As.": "asirio", "Gk.": "griego", "Lat.": "latín", "Vg.": "Vulgata",
    "Qal": "Qal", "Niph.": "Nifal", "Pi.": "Piel", "Pu.": "Pual",
    "Hiph.": "Hifil", "Hoph.": "Hofal", "Hithp.": "Hitpael",
    "Ithp.": "Itpael", "Ithpa.": "Itpaal", "Aph.": "Afel", "Pe.": "Peal",
    "Pilp.": "Pilpel", "Po.": "Poel", "Polel": "Polel", "Hithpo.": "Hitpolel",
    "Kt": "Ketib", "Qr": "Qeré", "LXX": "LXX", "NT": "NT", "AV": "AV",
    "EV": "versiones inglesas", "RV": "RV", "WH": "WH", "MT": "texto masorético",
})

# Lo que no está en ningún idioma y pasa tal cual: hebreo, griego, cifras,
# referencias bíblicas y las siglas de los críticos (WH, MM, Cremer).


_ABRE = "([{«\u201c"
_CIERRA = ")]}»\u201d,;:.!?"


def _desnudar(pieza: str) -> tuple[str, str, str]:
    """Aparta los paréntesis y comas pegados, que escondían «(cf.» y «pl.,»."""
    abre = ""
    while pieza and pieza[0] in _ABRE:
        abre += pieza[0]
        pieza = pieza[1:]
    cierra = ""
    while pieza and pieza[-1] in _CIERRA and pieza not in SIGLAS and len(pieza) > 1:
        cierra = pieza[-1] + cierra
        pieza = pieza[:-1]
    return abre, pieza, cierra


# Las mismas siglas sin el punto final: las dos obras lo ponen o no según les
# viene («pl.» y «pl»). La búsqueda respeta las mayúsculas a propósito: sin eso,
# «Mt» —el evangelio— se leía como «MT», el texto masorético.
_SIN_PUNTO = {k.rstrip("."): v for k, v in SIGLAS.items()}

_ABRE = "([{«\u201c"
_CIERRA = ")]}»\u201d,;:.!?"
_PALABRA_ASCII = re.compile(r"[A-Za-z][A-Za-z'-]*|[^A-Za-z]+")
# Puntuación que no rompe la prosa: la traduce el mismo motor de palabras.
_NEUTRO = re.compile(r"^[\s,;:.()\[\]'\"!?&/-]*$")
# Los números romanos, uno por uno y no por sus letras: «did», «mix» e «ill»
# están hechos de letras romanas y se colaban en inglés sin que nadie lo notara.
_ROMANO_ESTRICTO = re.compile(
    r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")

ROMANOS = {
    "i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii",
    "xiii", "xiv", "xv", "xvi", "xvii", "xviii", "xix", "xx", "xxi", "xxii",
    "xxiii", "xxiv", "xxv", "xxx", "xl", "l", "lx", "c", "cc", "d", "m",
}
_PALABRA_INGLESA = re.compile(r"^[A-Za-z][A-Za-z'-]*$")


def _desnudar(pieza: str) -> tuple[str, str, str]:
    """Aparta los paréntesis y comas pegados, que escondían «(cf.» y «pl.,»."""
    abre = ""
    while pieza and pieza[0] in _ABRE:
        abre += pieza[0]
        pieza = pieza[1:]
    cierra = ""
    while pieza and pieza[-1] in _CIERRA and pieza not in SIGLAS and len(pieza) > 1:
        cierra = pieza[-1] + cierra
        pieza = pieza[:-1]
    return abre, pieza, cierra


def _sigla(pieza: str) -> str | None:
    hallada = SIGLAS.get(pieza) or _SIN_PUNTO.get(pieza.rstrip("."))
    if hallada is None and pieza.endswith(".") and pieza[:1].isupper():
        # «Interrog.» al principio de una acepción es la misma sigla que
        # «interrog.»; sólo vale si lleva punto, para no confundir «Mt» con «MT».
        hallada = _SIN_PUNTO.get(pieza[:1].lower() + pieza[1:].rstrip("."))
    return hallada


def _piezas(linea: str) -> list[tuple[str, str]]:
    """Parte una línea en piezas etiquetadas: sigla, protegido o prosa.

    Es el único sitio donde se decide qué es cada cosa, para que el traductor y
    el informe de lo que falta vean exactamente lo mismo.
    """
    salida: list[tuple[str, str]] = []
    for pieza in linea.split(" "):
        # primero la pieza tal cual, con su punto: «Interrog.» sólo se reconoce
        # como sigla mientras lo lleve, porque «Ex» sin punto es el Éxodo
        espanol = _sigla(pieza)
        abre = cierra = ""
        if espanol is None:
            abre, desnuda, cierra = _desnudar(pieza)
            espanol = _sigla(desnuda)
        if espanol is not None:
            salida.append(("sigla", abre + espanol + cierra))
            continue
        trozos = _PALABRA_ASCII.findall(pieza)
        if trozos and all(
            _NEUTRO.match(x)
            or (_PALABRA_INGLESA.match(x) and _sigla(x) is None
                and not _protegido_suelto(x, abre, cierra))
            for x in trozos
        ):
            salida.append(("prosa", pieza))     # entera, con su puntuación
            continue
        # La pieza lleva pegadas cosas de las dos clases:
        # «palm-tree;—only» es prosa, raya, prosa.
        for trozo in trozos:
            suelta = _sigla(trozo) if _PALABRA_INGLESA.match(trozo) else None
            if suelta is not None:
                salida.append(("sigla", suelta))
            elif _PALABRA_INGLESA.match(trozo):
                clase = "protegido" if _protegido_suelto(trozo, abre, cierra) else "prosa"
                salida.append((clase, trozo))
            elif _NEUTRO.match(trozo) and salida:
                salida[-1] = (salida[-1][0], salida[-1][1] + trozo)
            else:
                salida.append(("protegido", trozo))
    return salida


def _recorrer(texto: str, traduce):
    """Recorre el artículo llamando a «traduce» con cada tramo de prosa inglesa.

    Devuelve las líneas ya armadas, o None en cuanto un tramo no se resuelve.
    """
    lineas: list[str] = []
    for linea in texto.replace("\xa0", " ").split("\n"):
        sangria = linea[: len(linea) - len(linea.lstrip(" "))]
        armada: list[str] = []
        prosa: list[str] = []
        for clase, trozo in _piezas(linea) + [("fin", "")]:
            if clase == "prosa":
                prosa.append(trozo)
                continue
            if prosa:
                espanol = traduce(" ".join(prosa))
                if espanol is None:
                    return None
                armada.append(espanol)
                prosa = []
            if clase != "fin":
                armada.append(trozo)
        lineas.append(sangria + " ".join(p for p in armada if p != ""))
    return lineas


def traducir_articulo(texto: str | None) -> str | None:
    """El artículo en español, o None si hay una sola palabra que no se entiende."""
    if not texto or not texto.strip():
        return None
    lineas = _recorrer(texto, traducir)
    return None if lineas is None else "\n".join(lineas)


def desconocidas_articulo(texto: str | None) -> list[str]:
    """Las palabras que impiden traducir este artículo. Para afinar las tablas."""
    if not texto or not texto.strip():
        return []
    faltan: list[str] = []

    def mirar(tramo: str) -> str:
        faltan.extend(desconocidas(tramo))
        return ""                        # sigue recorriendo: queremos todas

    _recorrer(texto, mirar)
    return faltan


def _protegido_suelto(trozo: str, abre: str, cierra: str) -> bool:
    """Una letra suelta o un número romano: es una enumeración o una sigla,
    no una palabra. Salvo el artículo «a», que sí lo es."""
    if len(trozo) == 1:
        return trozo not in "aA" or bool(abre or cierra)
    if _ROMANO_ESTRICTO.match(trozo.upper()) and trozo.lower() not in PALABRAS:
        return trozo != "I" and (trozo.isupper() or trozo.islower() and len(trozo) > 1)
    return trozo.lower() in ROMANOS and trozo != "I" and (
        trozo.isupper() or trozo.islower() and len(trozo) > 1)
