"""Traducción al español de la etimología del Diccionario Strong.

El campo `derivation` de Strong dice de dónde viene cada palabra, y en una app
en español aparecía tal cual: «from H1234 and H5678», «a primitive root», «of
uncertain derivation». No es prosa libre: es un formulario con un vocabulario
pequeño y muy repetido, así que se puede traducir por sustitución sin inventar
nada, igual que ya se hace con los códigos morfológicos.

El criterio es el mismo de todo el proyecto: se traduce lo que se entiende del
todo y se calla lo que no. `traducir()` devuelve None cuando queda una sola
palabra inglesa sin equivalente conocido; el constructor de la base cuenta
cuántas quedan fuera y la aplicación no muestra el campo en esos casos, en vez
de enseñar media frase en inglés.

Los números Strong, el texto griego y hebreo entre paréntesis y las citas
bíblicas se copian sin tocar.
"""

from __future__ import annotations

import re

# Fórmulas completas. Se prueban antes que las palabras sueltas y de más larga a
# más corta, porque «from the same as» no es «from» + «the same as».
FRASES: dict[str, str] = {
    "a primitive root": "raíz primitiva",
    "an unused root": "raíz no usada",
    "a primary verb": "verbo primario",
    "a primary word": "palabra primaria",
    "a primary preposition": "preposición primaria",
    "a primary particle": "partícula primaria",
    "a primary pronoun": "pronombre primario",
    "a primary number": "número primario",
    "of uncertain derivation": "de origen incierto",
    "of foreign derivation": "de origen extranjero",
    "of Hebrew derivation": "de origen hebreo",
    "of Aramaic derivation": "de origen arameo",
    "of Egyptian derivation": "de origen egipcio",
    "of Persian derivation": "de origen persa",
    "of Latin derivation": "de origen latino",
    "of Greek derivation": "de origen griego",
    "of Chaldee derivation": "de origen caldeo",
    "probably of foreign derivation": "probablemente de origen extranjero",
    "of doubtful derivation": "de origen dudoso",
    "of doubtful origin": "de origen dudoso",
    "of uncertain affinity": "de parentesco incierto",
    "of uncertain origin": "de origen incierto",
    "of foreign origin": "de origen extranjero",
    "of Hebrew origin": "de origen hebreo",
    "of Aramaic origin": "de origen arameo",
    "of Latin origin": "de origen latino",
    "of Persian origin": "de origen persa",
    "of Egyptian origin": "de origen egipcio",
    "of Chaldee origin": "de origen caldeo",
    "of Greek origin": "de origen griego",
    "of Hebrew or Aramaic origin": "de origen hebreo o arameo",
    "from the same as": "de la misma raíz que",
    "from the base of": "de la raíz de",
    "the same as": "lo mismo que",
    "the base of": "la raíz de",
    "corresponding to": "correspondiente a",
    "a derivative of": "un derivado de",
    "a compound of": "un compuesto de",
    "a collateral form of": "una forma paralela de",
    "an alternate form of": "una forma alternativa de",
    "a variation of": "una variante de",
    "a variation for": "una variante de",
    "a variation from": "una variante de",
    "a prolonged form of": "una forma alargada de",
    "a shortened form of": "una forma abreviada de",
    "a strengthened form of": "una forma reforzada de",
    "a reduplicated form of": "una forma reduplicada de",
    "a contracted form of": "una forma contraída de",
    "patronymically from": "patronímico de",
    "denominative from": "denominativo de",
    "by implication": "por extensión",
    "in the sense of": "en el sentido de",
    "in its original sense": "en su sentido original",
    "in the original sense": "en el sentido original",
    "through the idea of": "por la idea de",
    "with the idea of": "con la idea de",
    "akin to": "emparentado con",
    "apparently a primary word": "al parecer palabra primaria",
    "probably of foreign origin": "probablemente de origen extranjero",
    "compare": "compárese",
    "see": "véase",
    "i.e.": "es decir,",
    "e.g.": "por ejemplo,",
    "properly": "propiamente",
    "figuratively": "en sentido figurado",
    "literally": "literalmente",
    "middle voice": "voz media",
    "passive voice": "voz pasiva",
    "active voice": "voz activa",
    "middle voice of": "voz media de",
    "passive of": "pasiva de",
    "orthographical variation": "variante ortográfica",
    "lemma corrected to": "lema corregido a",
    "xlit corrected to": "transliteración corregida a",
    "missing vowel": "falta la vocal",
    "another form of": "otra forma de",
}

# Palabras sueltas.
PALABRAS: dict[str, str] = {
    "from": "de", "of": "de", "and": "y", "or": "o", "a": "", "an": "",
    "the": "el", "to": "a", "as": "como", "in": "en", "for": "por", "by": "por",
    "with": "con", "through": "por", "same": "misma", "root": "raíz",
    "primitive": "primitiva", "primary": "primaria", "unused": "no usada",
    "feminine": "femenino", "masculine": "masculino", "neuter": "neutro",
    "plural": "plural", "singular": "singular", "dual": "dual",
    "derivative": "derivado", "derivation": "origen", "base": "raíz",
    "compound": "compuesto", "form": "forma", "forms": "formas",
    "variation": "variante", "prolonged": "alargada", "shortened": "abreviada",
    "strengthened": "reforzada", "contracted": "contraída",
    "reduplicated": "reduplicada", "reduplication": "reduplicación",
    "alternate": "alternativa", "collateral": "paralela",
    "probably": "probablemente", "perhaps": "quizá", "apparently": "al parecer",
    "presumed": "supuesto", "uncertain": "incierto", "certain": "cierto",
    "corresponding": "correspondiente", "origin": "origen", "meaning": "que significa",
    "sense": "sentido", "idea": "idea", "participle": "participio",
    "particle": "partícula", "adverb": "adverbio", "verb": "verbo",
    "noun": "sustantivo", "article": "artículo", "pronoun": "pronombre",
    "preposition": "preposición", "prepositional": "preposicional",
    "prefix": "prefijo", "suffix": "sufijo", "enclitic": "enclítico",
    "negative": "negativa", "comparative": "comparativo",
    "superlative": "superlativo", "diminutive": "diminutivo",
    "intensive": "intensivo", "patronymic": "patronímico", "patrial": "gentilicio",
    "denominative": "denominativo", "ordinal": "ordinal",
    "genitive": "genitivo", "dative": "dativo", "accusative": "acusativo",
    "nominative": "nominativo", "case": "caso", "person": "persona",
    "tenses": "tiempos", "tense": "tiempo", "present": "presente",
    "middle": "media", "passive": "pasiva", "active": "activa", "voice": "voz",
    "irregular": "irregular", "obsolete": "en desuso", "identical": "idéntico",
    "equivalent": "equivalente", "original": "original", "word": "palabra",
    "lemma": "lema", "vowel": "vocal", "missing": "falta",
    "corrected": "corregido", "orthographical": "ortográfica",
    "transposition": "transposición", "permutation": "permutación",
    "contraction": "contracción", "prolongation": "alargamiento",
    "abbreviated": "abreviado", "shorter": "más corta", "another": "otra",
    "also": "también", "but": "pero", "only": "solo", "including": "incluido",
    "rather": "más bien", "like": "como", "thus": "así", "together": "juntos",
    "used": "usado", "inserted": "insertado", "interposed": "interpuesto",
    "formed": "formado", "being": "siendo", "its": "su", "his": "su",
    "which": "que", "that": "que", "not": "no", "if": "si", "some": "algún",
    "first": "primero", "second": "segundo", "one": "uno", "double": "doble",
    "multiple": "múltiple", "number": "número", "fully": "plenamente",
    "especially": "especialmente", "affinity": "parentesco", "akin": "emparentado",
    "properly": "propiamente", "implication": "extensión", "part": "parte",
    "compare": "compárese", "see": "véase", "aramaic": "arameo",
    "hebrew": "hebreo", "greek": "griego", "latin": "latín", "persian": "persa",
    "egyptian": "egipcio", "chaldee": "caldeo", "foreign": "extranjero",
    "inseparable": "inseparable", "primarily": "primariamente",
    "figuratively": "en sentido figurado", "literally": "literalmente",
    "otherwise": "por lo demás", "out": "fuera", "up": "arriba", "off": "lejos",
    "is": "es", "be": "ser", "has": "tiene", "will": "futuro", "go": "ir",
    "he": "él", "it": "ello", "my": "mi", "people": "pueblo", "place": "lugar",
    "pronominal": "pronominal", "possessor": "poseedor", "suffixed": "con sufijo",
}

# Se copian tal cual: números Strong, texto no latino y citas bíblicas.
_INTACTO = re.compile(r"[HG]\d+|[^\W\dA-Za-z_]+|\d+:\d+")
_PALABRA = re.compile(r"[A-Za-z][A-Za-z'\-]*")
_CODIGO = re.compile(r"[HG]\d+")


def _frases_ordenadas() -> list[tuple[re.Pattern[str], str]]:
    orden = sorted(FRASES.items(), key=lambda kv: -len(kv[0]))
    return [
        (re.compile(r"\b" + re.escape(k) + r"\b", re.IGNORECASE), v) for k, v in orden
    ]


_FRASES = _frases_ordenadas()
_MARCA = "\x00"


def traducir(derivation: str | None) -> str | None:
    """Etimología en español, o None si queda alguna palabra sin traducir."""
    if not derivation or not derivation.strip():
        return None

    texto = derivation.strip()

    # Primero las fórmulas completas; lo ya traducido se marca para que las
    # palabras sueltas no lo vuelvan a tocar. Los números Strong se marcan
    # igual, porque si no la «H» de «H959» pasaría por palabra suelta.
    for patron, español in _FRASES:
        texto = patron.sub(lambda _m, e=español: _MARCA + e + _MARCA, texto)
    texto = _CODIGO.sub(lambda m: _MARCA + m.group(0) + _MARCA, texto)

    partes = texto.split(_MARCA)
    salida: list[str] = []
    for i, parte in enumerate(partes):
        if i % 2 == 1:  # ya traducido
            salida.append(parte)
            continue
        resto = parte
        for palabra in set(_PALABRA.findall(parte)):
            español = PALABRAS.get(palabra.lower())
            if español is None:
                return None  # una sola palabra desconocida y no se muestra nada
            resto = re.sub(r"\b" + re.escape(palabra) + r"\b", español, resto)
        salida.append(resto)

    limpio = "".join(salida)
    limpio = re.sub(r"\s+", " ", limpio).strip(" ;,")
    limpio = re.sub(r"\s+([,;:.\)])", r"\1", limpio)
    limpio = re.sub(r"\(\s+", "(", limpio)
    return limpio or None

# Segundo lote: el vocabulario que aparece al explicar qué significan los
# nombres propios («de H1 (padre) y H4428 (rey)») y las abreviaturas de las
# citas. Sale del recuento de lo que quedaba sin traducir, de más a menos
# frecuente.
PALABRAS.update({
    "god": "Dios", "jah": "Jah", "jehovah": "YHVH", "lord": "señor",
    "house": "casa", "name": "nombre", "father": "padre", "brother": "hermano",
    "son": "hijo", "man": "hombre", "king": "rey", "servant": "siervo",
    "judge": "juez", "city": "ciudad", "village": "aldea", "fountain": "fuente",
    "water": "agua", "waters": "aguas", "springs": "manantiales", "well": "pozo",
    "rock": "roca", "stone": "piedra", "mountain": "monte", "heights": "alturas",
    "height": "altura", "high": "alto", "lofty": "elevado", "hollow": "hueco",
    "heap": "montón", "meadow": "pradera", "fortress": "fortaleza",
    "dwelling": "morada", "portion": "porción", "source": "origen",
    "strength": "fuerza", "force": "fuerza", "strong": "fuerte", "firm": "firme",
    "help": "ayuda", "favor": "favor", "gift": "regalo", "pleasure": "placer",
    "light": "luz", "sun": "sol", "flame": "llama", "fire": "fuego",
    "fruit": "fruto", "hand": "mano", "eyes": "ojos", "burden": "carga",
    "whiteness": "blancura", "fragrant": "fragante", "red": "rojo",
    "good": "bueno", "great": "grande", "clear": "claro", "hidden": "oculto",
    "conspicuous": "conspicuo", "liberal": "generoso", "knowing": "conocedor",
    "cutting": "corte", "covering": "cubierta", "piercing": "perforación",
    "bending": "curvatura", "union": "unión", "distinction": "distinción",
    "flowing": "que fluye", "built": "construido", "made": "hecho",
    "given": "dado", "break": "romper", "cover": "cubrir", "cut": "cortar",
    "open": "abrir", "pour": "derramar", "stretch": "extender", "hide": "ocultar",
    "pierce": "traspasar", "prick": "punzar", "gather": "reunir",
    "hold": "sostener", "have": "tener", "make": "hacer", "bend": "doblar",
    "turn": "volver", "shine": "brillar", "glisten": "resplandecer",
    "mean": "significar", "denoting": "que indica", "signification": "significado",
    "implied": "implícito", "denominatively": "denominativamente",
    "indicative": "indicativo", "imperative": "imperativo",
    "adjective": "adjetivo", "numeral": "numeral", "demonstrative": "demostrativo",
    "directive": "direccional", "transcription": "transcripción",
    "simpler": "más simple", "similar": "similar", "congener": "afín",
    "error": "error", "erroneous": "erróneo", "unknown": "desconocido",
    "dagesh": "daguesh", "ayin": "ayin",
    # Libros bíblicos, que aparecen en las citas.
    "jeremiah": "Jeremías", "ezekiel": "Ezequiel", "isaiah": "Isaías",
    "samuel": "Samuel", "kings": "Reyes", "chronicles": "Crónicas",
    "psalm": "Salmo", "psalms": "Salmos", "job": "Job", "daniel": "Daniel",
    "ezra": "Esdras", "nehemiah": "Nehemías", "joshua": "Josué",
    "palestine": "Palestina", "baal": "Baal",
    # Palabras de relación y gramática que quedaban sueltas.
    "usually": "normalmente", "sometimes": "a veces", "often": "a menudo",
    "rarely": "rara vez", "respectively": "respectivamente", "hence": "de ahí",
    "else": "si no", "both": "ambos", "all": "todo", "other": "otro",
    "who": "que", "so": "así", "more": "más", "over": "sobre", "on": "en",
    "at": "en", "into": "en", "down": "abajo", "forth": "adelante",
    "away": "lejos", "round": "alrededor", "past": "pasado", "time": "tiempo",
    "third": "tercero", "two": "dos", "pieces": "piezas", "motion": "movimiento",
    "remotely": "remotamente", "patronymically": "patronímicamente",
})
