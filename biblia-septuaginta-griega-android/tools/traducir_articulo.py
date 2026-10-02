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
import unicodedata

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

    # Latín editorial de las dos obras. Cada una se ha mirado en todas sus
    # apariciones antes de ponerla aquí, y en las diez son lo mismo.
    #
    # «ut» va siempre en «ut supr.» y «ut infr.», y como «supr.» ya dice
    # «arriba» e «infr.» dice «abajo», con poner «como» la fórmula queda
    # entera: «como arriba».
    # Va junta y suelta: «interr.adv. Where?» es una sola sigla, y partida
    # salía «interrogativo. adverbio.», con el orden del inglés.
    "interr.adv.": "adverbio interrogativo",
    # «shining one, epith. of king of Babylon» y «v. conject. in Di».
    "epith.": "epíteto", "conject.": "conjetura",
    "appell.": "apelativo", "orthogr.": "ortografía",
    # «by metapl. for τὰ ὁρκωμόσια»: metaplasmo, el cambio de declinación.
    "metapl.": "metaplasmo",
    # Más abreviaturas de Brown-Driver-Briggs.
    "app.": "aparentemente",      # «app. a descendant of Judah»
    "del.": "suprímase",          # «but del. 𝔊 Co»: bórrese, según esos testigos
    "theoph.": "teofanía",        # «quake of earth at theoph.»
    "kg.": "rey",                 # «honour, majesty, of kg.»
    "odorif.": "odorífero",       # «odorif. tree, aloe»
    "tr.": "traducido",           # «AV, tr. as = ῥυπάω»
    "improb.": "improbable", "sacrif.": "sacrificó",
    "cop.": "copulativo", "subjunc.": "subjuntivo",
    "altern.": "alternativa", "etymol.": "etimología",
    "suff.": "sufijo", "subscr.": "suscripción",
    "inscr.": "inscripción", "metath.": "metátesis",
    "ed.": "edición", "ins.": "insértese", "insignif.": "insignificante",
    "format.": "formación", "individ.": "individuo",
    "abst.": "abstracto", "cuneif.": "cuneiforme", "fam.": "familia",
    "punct.": "puntuación", "syncop.": "sincopado", "transl.": "traducido",
    "transpos.": "transposición", "cpd.": "compuesto", "abbr.": "abreviado",
    "instrum.": "instrumento", "urb.": "ciudad",
    "uncontr.": "sin contraer",
    "pregn.": "pregnante",      # «constr. pregn.»: construcción pregnante
    "elsew.": "en otros lugares", "ap.": "apud",
    "dei": "de dios",            # «as design. dei»: designación de la deidad
    "Trans.": "transitivo", "Intrans.": "intransitivo", "Neut.": "neutro",
    # «n.pr.flum.» es flumen, el río: la misma sigla que n.pr.fl. pero entera.
    "n.pr.flum.": "nombre propio de río",
    # «van d. H» es van der Hooght, el editor. En minúscula no lo coge la regla
    # de los nombres propios, que mira la mayúscula inicial.
    "van": "van",
    "interr.": "interrogativo",
    "ut": "como",
    # «v. sub ענה» = véase bajo esa raíz. Cinco veces, siempre igual.
    "sub": "bajo",
    # «si vera l.» = si vera lectio, «si la lectura es correcta». Es una
    # fórmula que el filólogo reconoce de un vistazo y que traducida pierde
    # más de lo que gana, así que se deja en latín: las dos palabras se
    # devuelven a sí mismas para que no tumben el artículo.
    "si": "si", "vera": "vera",
    # Siglas de bibliografía: «DB, ext., 367» es el volumen suplementario del
    # Dictionary of the Bible, y «WH, br.» son los corchetes de Westcott-Hort.
    # No se traducen, se dejan: son el nombre de la obra.
    "ext.": "ext.", "br.": "br.",
    # En minúscula es «mount», el accidente geográfico, no el evangelio. Las
    # diecisiete veces. «Mt» con mayúscula sigue siendo Mateo, que para eso
    # esta tabla distingue mayúsculas.
    "mt.": "monte", "mont.": "monte",
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


# Los troncos verbales hebreos en la forma corta de Abbott-Smith.
#
# BDB los escribe largos y con mayúscula —«Niph.», «Hiph.»— y ya estaban. Pero
# Abbott-Smith, cuando cita la Septuaginta, los abrevia en minúscula detrás de
# la raíz hebrea: «[in LXX for צדק hi.]», «[for גָּלָה ni., pi.]». Como la
# búsqueda respeta las mayúsculas a propósito —sin eso «Mt», el evangelio, se
# leía como «MT», el texto masorético—, esas formas cortas no casaban con nada
# y bloqueaban el artículo entero. Solo «hi.», «pi.» y «ni.» cerraban el paso a
# 572 artículos.
SIGLAS.update({
    "qal": "qal",
    "ni.": "nifal",
    "niph.": "nifal",
    "pi.": "piel",
    "pu.": "pual",
    "hi.": "hifil",
    "hiph.": "hifil",
    "ho.": "hofal",
    "hoph.": "hofal",
    "hith.": "hitpael",
    "hithp.": "hitpael",
    "po.": "poel",
    "Po.": "Poel",
    "pil.": "pilel",
    "pilp.": "pilpel",
})

# Otras abreviaturas de los dos léxicos, comprobadas una a una en su contexto.
# Abreviaturas de libro que son además palabras inglesas corrientes. Las demás
# —Mk, Lk, Ro, Ga, Phl…— pasan intactas solas, porque no significan nada en
# inglés; éstas no, y se traducían. «He 11:21», la carta a los Hebreos, salía
# «él 11:21»: 593 veces en 416 artículos. «Is 40:4», Isaías, salía «es 40:4».
#
# Se mapean a sí mismas, que es lo que hace el resto de abreviaturas de libro en
# esta obra. Comprobado antes de tocarlas: de las 1353 apariciones de «He» y las
# 667 de «Is» en los dos léxicos, ni una sola es la palabra inglesa; hasta los
# «Westc., He., 297» son el comentario de Westcott a Hebreos.
SIGLAS.update({
    "He": "He",
    "Is": "Is",
    # Dos más del mismo tipo, y las dos las rompí yo en este mismo trabajo al
    # meter «am» («I am», traduciendo ἐγώ εἰμι) y «de» (el latín de «Plut., de
    # Puer. Educ.») en la tabla de palabras, que no distingue mayúsculas.
    #
    # «Am 5:2», Amós, salía «soy 5:2». «De 25:4», Deuteronomio, salía «de
    # 25:4». Comprobadas igual que «He» e «Is» antes de ponerlas aquí: de las
    # 70 apariciones de «Am» y las 188 de «De» en los dos léxicos, ninguna es
    # la palabra inglesa ni la preposición latina. Son Amós y Deuteronomio en
    # las citas, y Delitzsch y Driver en las referencias de Brown-Driver-Briggs
    # —«Driver, De., 98 f.», «Thes MV De»—.
    #
    # En minúscula siguen traduciéndose, que para eso esta tabla distingue
    # mayúsculas: «I am» es «soy» y «de Puer. Educ.» se queda en latín.
    "Am": "Am",
    "De": "De",

    # Nombres de autor y de obra que son además palabras inglesas corrientes,
    # y que por eso se estaban traduciendo. Comprobadas todas sus apariciones:
    #
    #   «Field, Notes, 134» es F. Field y sus «Notes on the Translation of the
    #   New Testament». 186 veces «Field», que salía «campo», y 284 «Notes»,
    #   que salía «notas». Las 284 son el título de esa obra.
    #
    #   «Dalman, Words, 21» es «The Words of Jesus», de Gustaf Dalman. 83
    #   veces, todas el título.
    "Field": "Field",
    "Notes": "Notes",
    "Words": "Words",

    # Las mismas abreviaturas gramaticales que ya están en minúscula, pero a
    # principio de frase. «Pass. struck back» salía «pasar struck back» —el
    # verbo inglés— en vez de «en pasiva», 88 veces; «Fig., of Christians»
    # salía «higo, de cristianos», 15 veces. Y «Compar., ἀκριβέστερον» es el
    # comparativo, no «compárese».
    "Pass.": "en pasiva",
    "Fig.": "figuradamente",
    "Compar.": "comparativo",
    "compar.": "comparativo",

    # Y las demás del mismo tipo, buscadas de una vez en lugar de ir
    # tropezando con ellas: abreviaturas gramaticales que ya estaban en
    # minúscula y que a principio de frase se quedaban en inglés.
    "Act.": "en activa",      # «Act., to destroy utterly» — y además caía en
                              # PALABRAS["act"] y salía «acto»
    "Mid.": "en media",       # 84 veces, la voz media
    "Pt.": "participio",      # 63
    "Cf.": "compárese",       # 25
    "V.": "véase",            # 24
    "Impf.": "imperfecto",    # 38
    "Inf.": "infinitivo",     # 26
    "Pf.": "perfecto",        # 23
    "Imv.": "imperativo",     # 5
    "Superl.": "superlativo", # 4
    "Esp.": "sobre todo",     # 9
    "C.": "con",              # «C. acc. rei», «C. dat. pers.»: 75 de las 76
                              # llevan detrás un caso o un modo

    # Y aquí, al comprobar la lista anterior, salió otra cosa: _sigla tiene una
    # tercera regla —si la pieza lleva mayúscula y punto, se reintenta en
    # minúscula, para que «Interrog.» valga lo mismo que «interrog.»— y esa
    # regla se come también las que NO son abreviaturas gramaticales.
    #
    # Son nombres de obra, y en las dos obras no significan otra cosa:
    #
    #   «Pr.»  son las Prolegomena de Moulton: «M, Pr., 46».
    #   «Tr.»  es el Synonyms of the NT de Trench: «Tr., Syn., §xxv».
    #   «Syn.» es esa misma obra: «Tr., Syn.».
    #   «App.» es el apéndice de Westcott-Hort: «WH, App., 145».
    #   «Al.»  es Áquila, la versión griega: «[in Al.: Ps 48 (49):9]».
    #   «Cl.»  es la Classical Review: «v. Cl. Rev., i, 7».
    #   «Ap.»  es el comentario de Swete al Apocalipsis: «Swete, Ap., 5».
    #   «Fr.»  es una inicial, no la preposición.
    #
    # Casi siempre se salvaban por la coma que llevan detrás —«Pr.,» no es
    # «Pr.»— y por eso sólo había nueve artículos mal; pero salvarse por la
    # puntuación no es salvarse. Van en _NUNCA_EN_MINUSCULA, más abajo.
    #
    # «Mt.», «Intr.», «Pl.» y «Eccl.» se quedan como están: salen en los dos
    # sentidos, mitad y mitad, y protegerlas dejaría en inglés tantas como
    # arregla.
    # «St. Paul» se leía como el sufijo ordinal inglés de «1st» y salía
    # «º Pablo». Como sigla se reconoce antes de llegar a esa regla.
    "St.": "S.",
    # «sing.» caía en PALABRAS["sing"] y salía «cantar»: «3rd pers. sing.» daba
    # «3º de la persona cantar». Son 27 pasajes.
    "sing.": "singular",
    # BDB escribe «3rd ps. sing.», donde «ps.» es «persona». Sin el punto, «ps»
    # es la sigla de los Salmos, así que salía «3º Sal singular».
    "ps.": "persona",
    # «Th.» con punto caía en el sufijo ordinal de «4th» y salía «º». Se mapea a
    # sí misma, como el resto de abreviaturas de libro: son 88 citas de
    # Tesalonicenses y una «Th. NT», la teología del NT de Stevens.
    "Th.": "Th.",
    # Más abreviaturas de los dos léxicos, comprobadas en su contexto.
    "fs.": "femenino singular",
    "ms.": "masculino singular",
    "bet.": "entre",
    "erron.": "erróneamente",
    "assoc.": "asociado",
    "superlat.": "superlativo",
    "comparat.": "comparativo",
    "tabern.": "tabernáculo",
    "crasis": "crasis",
    "law-term": "término jurídico",
    # Códice Alejandrino-Vaticano: sigla de manuscrito, no se traduce.
    "AB": "AB",
    # «prop.» es «properly», no un puntal. Caía en PALABRAS["prop"], que es el
    # sustantivo, y 96 pasajes ya traducidos decían «puntal» donde el léxico
    # dice «propiamente». Sale 263 veces, y hasta las 11 que van sin punto son
    # «properly» con coma («prop, a vagabond») salvo una.
    "prop.": "propiamente",
    # Con mayúscula cuando encabeza una acepción: «I. Prop., intrans.».
    "Prop.": "Propiamente",
    # «Pal.» es Palestina, no el tronco Palel. Comprobado en contexto: «on S.
    # border of Pal.», «n.pr.font. in SW. Pal.».
    "Pal.": "Palestina",
    # Variantes de tronco que BDB escribe con punto y sin la marca de ayin.
    "Hithpa.": "hitpael",
    "Hithpe.": "hitpeel",
    "Hithpo.": "hitpoel",
    "hithpo.": "hitpoel",
    "Hithpol.": "hitpolel",
    "Hithpōl.": "hitpolel",
    "Piel": "Piel",
    "Pual": "Pual",
    "symb.": "simbólicamente",
    "hyperb.": "hipérbole",
    "interpr.": "interpretación",
    "conjunct.": "conjuntivo",
    "quadril.": "cuadrilítero",
    "aorist": "aoristo",
    "tit.": "título",
})

SIGLAS.update({
    "post-ex.": "postexílico",
    "post-exil.": "postexílico",
    "post-exilic": "postexílico",
    "pret.": "pretérito",
    "mpl.": "masculino plural",
    "fpl.": "femenino plural",
    "mod.": "moderno",
    # Latín de aparato crítico, que las dos obras usan sin traducir.
    "vel": "o",
    "aliter": "de otro modo",
    "foreg.": "anterior",
    "deriv.": "derivación",
    "prol.": "prólogo",
    "dim.": "diminutivo",
    "qu.": "pregunta",
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


# Siglas cuya forma sin punto es una palabra inglesa corriente y no una
# abreviatura. Solo «As» lo es de verdad: BDB escribe «As.», con punto, cuando
# quiere decir asirio, y un «As» suelto a principio de frase es la conjunción
# inglesa. Sin esta excepción, «As opposed to a woman» salía «asirio opuesto a
# una mujer», y «As a demonstrative pronoun» —en ὁ, la palabra más frecuente
# del Nuevo Testamento— salía «asirio demostrativo pronombre». Eran 70 pasajes
# en 53 entradas.
#
# Las otras quince siglas que chocan («adj», «pron», «gen», «part»…) se quedan
# como están: en un artículo de léxico esas formas son abreviaturas, no
# sustantivos, y la lectura de sigla es la correcta.
# Siglas que sólo valen con el punto puesto. «As» sin punto es la palabra
# inglesa, no «asirio».
#
# «C» y «V» se añaden aquí porque al meter «C.» («C. acc. rei» = cum) y «V.»
# («V. Milligan» = see) quedaron reconocidas también sin punto, y entonces
# «B.C. 681-668» —que el trozador parte en «B», «.», «C», «.»— salía «B. con.
# 681-668». La fecha de Esarhadón no lleva preposición.
_NUNCA_SIN_PUNTO = {"As", "C", "V"}

# Las mismas siglas sin el punto final: las dos obras lo ponen o no según les
# viene («pl.» y «pl»). La búsqueda respeta las mayúsculas a propósito: sin eso,
# «Mt» —el evangelio— se leía como «MT», el texto masorético.
_SIN_PUNTO = {
    k.rstrip("."): v
    for k, v in SIGLAS.items()
    if k.rstrip(".") not in _NUNCA_SIN_PUNTO
}

_ABRE = "([{«\u201c"
_CIERRA = ")]}»\u201d,;:.!?"
_PALABRA_ASCII = re.compile(r"[A-Za-z][A-Za-z'-]*|[^A-Za-z]+")

# Una palabra con letra latina que no es ASCII: «Kühner», «Ægean», «poët.»,
# «Pō», «Ēl», «Hithpō», «quæst.», «Nabû».
#
# El trozador de arriba solo ve A-Za-z, así que partía estas palabras en la
# letra rara y dejaba los cachos sueltos como si fueran inglés: «Kühner» salía
# «K» + «ü» + «hner», y «hner» tumbaba el artículo entero. Nueve artículos por
# Kühner, seis por Ægean, y 230 en total.
#
# Se protegen enteras en vez de intentar traducirlas, porque en estas dos obras
# una palabra con macrón, diéresis, circunflejo o ligadura es casi siempre una
# de tres cosas, y ninguna se traduce: una transliteración del hebreo (Pō, Ēl,
# Hithpō, ‛Anathôth), el apellido de un filólogo alemán (Kühner, Köhler,
# Schürer) o una abreviatura latina (quæst., poët.). Y quitarles el acento
# tampoco vale: el macrón de Pō y de Ēl distingue la vocal larga de la breve,
# que es justo el dato que la transliteración viene a dar.
_PALABRA_ACENTUADA = re.compile(r"[A-Za-z\u00C0-\u024F]*[\u00C0-\u024F][A-Za-z\u00C0-\u024F]*")
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


# Siglas con mayúscula que NO valen lo mismo que su forma en minúscula, porque
# con mayúscula son el nombre de una obra. Ver la explicación larga arriba.
_NUNCA_EN_MINUSCULA = {"Pr.", "Tr.", "Syn.", "App.", "Al.", "Cl.", "Ap.", "Fr."}


def _sigla(pieza: str) -> str | None:
    hallada = SIGLAS.get(pieza) or _SIN_PUNTO.get(pieza.rstrip("."))
    if (hallada is None and pieza.endswith(".") and pieza[:1].isupper()
            and pieza not in _NUNCA_EN_MINUSCULA):
        # «Interrog.» al principio de una acepción es la misma sigla que
        # «interrog.»; sólo vale si lleva punto, para no confundir «Mt» con «MT».
        hallada = _SIN_PUNTO.get(pieza[:1].lower() + pieza[1:].rstrip("."))
    return hallada


# «[a.di.ab]», «[h.da.ac]»: los identificadores con que Open Scriptures
# numeró las entradas de BDB. Van siempre entre corchetes, así que se
# reconocen sin confundirlos con una cadena de abreviaturas.
# Los troncos verbales que BDB escribe con la marca de ayin (U+201B) y con
# macrones y circunflejos: «Pō‛lēl», «Hithpō‛l», «Pe‛îl». Esa marca no es una
# letra, así que el trozador partía «Po‛el» en «Po» y «el» y dejaba las dos
# mitades como palabras inglesas sin resolver. Bloqueaban 53 formas distintas.
#
# Se cotejan por su raíz —sin diacríticos, sin la marca y en minúscula—, que es
# la única manera de que las seis grafías de «Polel» se traten como una.
TRONCOS_AYIN = {
    "po": "poel", "poel": "poel", "pol": "poel",
    "polel": "polel", "polal": "polal", "poal": "poal",
    "pilel": "pilel", "palel": "palel", "pal": "palel",
    "pul": "pual", "peil": "peil", "pᵉil": "peil", "pealal": "pealal",
    "hithpo": "hitpoel", "hithpol": "hitpoel", "hithpoel": "hitpoel",
    "hithpolel": "hitpolel", "hithpalel": "hitpalel", "ethpol": "etpoel",
}


def _raiz_ayin(pieza: str) -> str:
    """La pieza sin la marca de ayin, sin diacríticos y en minúscula."""
    limpia = pieza.strip(".,;:()[]").replace("\u201b", "").replace("\u2018", "")
    descompuesta = unicodedata.normalize("NFD", limpia)
    return "".join(c for c in descompuesta if not unicodedata.combining(c)).lower()


_CITA = re.compile(r"\d+[:.]\d+")

_CODIGO_BDB = re.compile(r"\[[a-z]{1,4}(?:\.[a-z]{1,4}){1,4}\][^\w\s]*$")


def _piezas(linea: str) -> list[tuple[str, str]]:
    """Parte una línea en piezas etiquetadas: sigla, protegido o prosa.

    Es el único sitio donde se decide qué es cada cosa, para que el traductor y
    el informe de lo que falta vean exactamente lo mismo.
    """
    salida: list[tuple[str, str]] = []
    trozos_linea = linea.split(" ")
    for n, pieza in enumerate(trozos_linea):
        # La marca de ayin: o es un tronco verbal, o es un nombre propio
        # transliterado («‛Anathôth», «Sē‛ir»). Los nombres pasan enteros; lo
        # que no se hace es partirlos y traducir las mitades por separado.
        if "\u201b" in pieza:
            tronco = TRONCOS_AYIN.get(_raiz_ayin(pieza))
            salida.append(("sigla", tronco) if tronco else ("protegido", pieza))
            continue
        # «To» es Tobías cuando le sigue una cita —«To 5:2»— y la preposición
        # inglesa cuando encabeza una acepción —«2. To slander, defame»—. Es la
        # única de las tres abreviaturas que de verdad se usa en los dos
        # sentidos: 93 veces libro, 12 veces preposición. Aquí se mira lo que
        # viene detrás, que es lo único que las distingue.
        if (pieza.strip("([{«").rstrip(")]}»,;") == "To"
                and n + 1 < len(trozos_linea)
                and _CITA.match(trozos_linea[n + 1].lstrip("([{«"))):
            salida.append(("protegido", pieza))
            continue
        # «f.» detrás de un número es «y siguiente», no «femenino».
        #
        # «Cremer, 611 f.» quiere decir la página 611 y la que sigue, igual que
        # «ff.» quiere decir «y siguientes». Pero «f.» también es la
        # abreviatura de femenino —«n.pr.m. & f.»—, y la tabla de siglas, que
        # no mira el contexto, las daba todas por femenino: 650 apariciones, de
        # las cuales 442 van justo detrás de un número.
        #
        # Se mira lo que viene delante, que es lo único que las separa. Quedan
        # mal las dos o tres de las enumeraciones tipo «I, 2, f., g.», donde
        # delante hay un número pero «f.» es una letra de orden; a cambio se
        # arreglan más de cuatrocientas.
        if (pieza.rstrip(")]},;:") == "f." and n
                and trozos_linea[n - 1].rstrip(")]},;:").rstrip(",")[-1:].isdigit()):
            cola = pieza[len("f."):]
            salida.append(("sigla", "y siguiente" + cola))
            continue
        # Identificador interno de la digitalización de BDB: «[a.di.ab]». No es
        # prosa del léxico ni significa nada para quien lee, pero al partirse en
        # «a», «di» y «ab» dejaba esas sílabas como palabras inglesas sin
        # resolver y tumbaba el artículo entero. Bloqueaba 179.
        if _CODIGO_BDB.match(pieza):
            salida.append(("protegido", pieza))
            continue
        # primero la pieza tal cual, con su punto: «Interrog.» sólo se reconoce
        # como sigla mientras lo lleve, porque «Ex» sin punto es el Éxodo
        espanol = _sigla(pieza)
        abre = cierra = ""
        if espanol is None:
            abre, desnuda, cierra = _desnudar(pieza)
            # «(c)» es la tercera acepción, no la abreviatura latina «c.».
            #
            # Esta segunda consulta mira la pieza ya sin paréntesis, y ahí «c»
            # cae en la tabla de siglas sin punto y sale «con»: 48 veces, en 43
            # artículos, ya publicados. Lo mismo con «(f)», que salía
            # «(femenino)».
            #
            # Lo que las distingue es el punto, que es lo que marca que algo
            # está abreviado: «(v. MM)» lleva punto y es «véase», «(c)» no lo
            # lleva y es una letra de enumeración. Con el punto puesto, la
            # consulta de más arriba —sobre la pieza entera— ya las coge.
            if (abre or cierra) and len(desnuda) == 1 and desnuda.isalpha():
                salida.append(("protegido", pieza))
                continue
            espanol = _sigla(desnuda)
        if espanol is not None:
            salida.append(("sigla", abre + espanol + cierra))
            continue
        if _PALABRA_ACENTUADA.search(pieza):
            salida.append(("protegido", pieza))
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


# Guion blando (U+00AD). Es invisible y no significa nada: lo dejó la
# digitalización donde el original partía la palabra a final de renglón. Pero
# para el trozador «con­taining» son dos palabras inglesas que no existen, y
# tumbaba el artículo entero. Bloqueaba 43.
_BLANDO = "\u00ad"

# El identificador de BDB puede venir pegado a lo que sigue —«[c.cd.ab];—only»—,
# y entonces no basta con reconocer la pieza entera: hay que sacarlo de en medio
# para que el resto se traduzca. Se sustituye por un carácter de uso privado,
# que no lleva letras y por tanto pasa protegido, y se devuelve al final.
_CUALQUIER_CODIGO = re.compile(r"\[[a-z]{1,4}(?:\.[a-z]{1,4}){1,4}\]")
_MARCA_CODIGO = "\ue001"


def _apartar_codigos(texto: str) -> tuple[str, list[str]]:
    guardados: list[str] = []

    def cambia(m):
        guardados.append(m.group(0))
        return _MARCA_CODIGO

    return _CUALQUIER_CODIGO.sub(cambia, texto), guardados


def _devolver_codigos(texto: str, guardados: list[str]) -> str:
    for codigo in guardados:
        texto = texto.replace(_MARCA_CODIGO, codigo, 1)
    return texto


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


# Preposición repetida, otra vez. traducir() ya la colapsa dentro de cada
# tramo, pero las siglas se desarrollan después de eso, al montar la línea:
# «in cl.» da «en» y luego «en griego clásico», y el doblete aparece ya fuera
# del alcance de aquella limpieza. Aquí se repasa el artículo entero.
_REPETIDA = re.compile(r"\b(a|de|en|con) \1\b")


def traducir_articulo(texto: str | None) -> str | None:
    """El artículo en español, o None si hay una sola palabra que no se entiende."""
    if not texto or not texto.strip():
        return None
    texto = texto.replace(_BLANDO, "")
    texto, codigos = _apartar_codigos(texto)
    lineas = _recorrer(texto, traducir)
    if lineas is None:
        return None
    return _devolver_codigos(_REPETIDA.sub(r"\1", "\n".join(lineas)), codigos)


def desconocidas_articulo(texto: str | None) -> list[str]:
    """Las palabras que impiden traducir este artículo. Para afinar las tablas."""
    if not texto or not texto.strip():
        return []
    texto = texto.replace(_BLANDO, "")
    texto, _ = _apartar_codigos(texto)
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
