"""Bel y el Dragón en español, traducido del griego, en sus dos versiones.

Es el capítulo 14 de Daniel en la Vulgata, y tampoco está en el hebreo: para
las Asambleas de Dios no es canon y aquí se ofrece para estudio. Son dos
relatos cortos contra la idolatría, y lo que los hace valiosos es el método:
Daniel no discute si el ídolo es dios, sino que espolvorea ceniza en el suelo
del templo y va a mirar las huellas por la mañana. La sátira es antigua y sigue
mordiendo.

Las dos versiones griegas no son la misma obra:

- La de los Setenta (BEL) abre atribuyendo el relato a una profecía de Habacuc,
  y su Daniel es sacerdote. Es la versión más antigua y más áspera.
- La de Teodoción (BET) es la que pasó a la Vulgata: empieza con la muerte de
  Astiages y el reinado de Ciro, y el diálogo está más pulido.

Las medidas se dejan como están —artabas, metretas, minas— porque convertirlas
a kilos y litros sería inventar precisión que el texto no tiene; quien estudia
prefiere el nombre antiguo, que es además el que discuten los comentarios.
"""

from __future__ import annotations

# --- Bel y el Dragón, versión de los Setenta -------------------------------
BEL_ES: dict[tuple[int, int], str] = {
    (1, 1): "De la profecía de Habacuc, hijo de Jesús, de la tribu de Leví.",
    (1, 2): "Había un hombre, sacerdote, cuyo nombre era Daniel, hijo de Abal, "
            "compañero del rey de Babilonia.",
    (1, 3): "Y había un ídolo, Bel, al que veneraban los babilonios; y se "
            "gastaban en él cada día doce artabas de flor de harina, cuatro "
            "ovejas y seis metretas de aceite.",
    (1, 4): "Y el rey lo veneraba, e iba cada día a postrarse ante él; pero "
            "Daniel oraba al Señor. Y dijo el rey a Daniel: «¿Por qué no te "
            "postras ante Bel?».",
    (1, 5): "Y dijo Daniel al rey: «Yo no venero a nadie sino al Señor, el Dios "
            "que creó el cielo y la tierra y que tiene señorío sobre toda "
            "carne».",
    (1, 6): "Y le dijo el rey: «¿Éste, pues, no es dios? ¿No ves cuánto se gasta "
            "en él cada día?».",
    (1, 7): "Y le dijo Daniel: «De ninguna manera; que nadie te engañe. Porque "
            "éste por dentro es de barro y por fuera de bronce, y te juro por el "
            "Señor, el Dios de los dioses, que jamás ha comido nada».",
    (1, 8): "Y airado el rey, llamó a los encargados del templo y les dijo: "
            "«Mostradme quién come lo que se prepara para Bel; y si no, "
            "moriréis,",
    (1, 9): "o morirá Daniel, que afirma que él no lo come». Y ellos dijeron: "
            "«Bel mismo es el que lo devora». Y dijo Daniel al rey: «Que así "
            "sea: si no demuestro que no es Bel quien devora esto, moriré yo y "
            "todos los míos».",
    (1, 10): "Y eran los sacerdotes de Bel setenta, sin contar mujeres y niños. "
             "Y llevaron al rey al templo del ídolo.",
    (1, 11): "Y pusieron los manjares delante del rey y de Daniel, y se trajo "
             "vino mezclado y se le puso a Bel. Y dijo Daniel: «Tú mismo ves "
             "que estas cosas están puestas, oh rey; sella tú, pues, las llaves "
             "del templo cuando quede cerrado». Y al rey le agradó la palabra.",
    (1, 14): "Y Daniel mandó a los suyos que, echando a todos fuera del templo, "
             "cubrieran de ceniza todo el templo, sin que ninguno de los de "
             "fuera lo supiera. Y entonces, cerrado el templo, mandó sellarlo "
             "con el anillo del rey y con los anillos de algunos sacerdotes "
             "ilustres.",
    (1, 15): "[15-17] Y sucedió que al día siguiente llegaron al lugar; pero los "
             "sacerdotes de Bel, entrando por puertas falsas, se habían comido "
             "todo lo que estaba puesto delante de Bel y habían bebido el vino. "
             "Y dijo Daniel: «Mirad vuestros sellos, si siguen intactos, varones "
             "sacerdotes; y tú también, oh rey […]».",
    (1, 18): "Y abriendo las puertas, vieron consumido todo lo que se había "
             "puesto, y las mesas vacías. Y se alegró el rey y dijo a Daniel: "
             "«Grande es Bel, y no hay en él engaño».",
    (1, 19): "Y Daniel se rió mucho, y dijo al rey: «Ven, mira el engaño de los "
             "sacerdotes». Y dijo Daniel: «Oh rey, estas huellas, ¿de quién "
             "son?».",
    (1, 20): "Y dijo el rey: «De hombres y de mujeres y de niños».",
    (1, 21): "Y fue a la casa donde vivían los sacerdotes, y halló los manjares "
             "de Bel y el vino; y mostró Daniel al rey las puertas falsas por "
             "las que entraban los sacerdotes y consumían lo que se ponía "
             "delante de Bel.",
    (1, 22): "Y los sacó el rey del templo de Bel y los entregó a Daniel; y el "
             "gasto que se hacía en él se lo dio a Daniel, y a Bel lo derribó.",
    (1, 23): "Y había un dragón en aquel mismo lugar, y los babilonios lo "
             "veneraban.",
    (1, 24): "Y dijo el rey a Daniel: «¿Acaso también de éste dirás que es de "
             "bronce? He aquí que vive y come y bebe: póstrate ante él».",
    (1, 26): "Y dijo Daniel: «Oh rey, dame autoridad y mataré al dragón sin "
             "hierro ni palo». Y se lo concedió el rey y le dijo: «Te es dado».",
    (1, 27): "Y tomando Daniel treinta minas de pez, y sebo, y pelos, lo coció "
             "todo junto e hizo una torta, y la echó en la boca del dragón; y en "
             "comiéndola, reventó. Y lo mostró al rey, diciendo: «¿No es esto lo "
             "que veneráis, oh rey?».",
    (1, 28): "Y se juntaron todos los del país contra Daniel y dijeron: «Judío "
             "se ha vuelto el rey: derribó a Bel y mató al dragón».",
    (1, 30): "Y viendo el rey que la multitud del país se juntaba contra él, "
             "llamó a sus consejeros y dijo: «Entrego a Daniel a la muerte».",
    (1, 31): "[31-32] Y había un foso en el que se criaban siete leones, a los "
             "cuales se entregaba a los conspiradores del rey, y se les daba "
             "cada día dos cuerpos de condenados a muerte. Y las multitudes "
             "echaron a Daniel en aquel foso, para que fuera devorado y ni "
             "siquiera tuviera sepultura.",
    (1, 33): "Y sucedió, al sexto día, que Habacuc llevaba panes desmigados en "
             "una cesta, en un guisado, y una jarra de vino mezclado, e iba al "
             "campo hacia los segadores.",
    (1, 34): "Y habló el ángel del Señor a Habacuc, diciendo: «Así te dice el "
             "Señor Dios: Lleva la comida que tienes a Daniel, al foso de los "
             "leones, en Babilonia».",
    (1, 35): "Y dijo Habacuc: «Señor Dios, yo no he visto Babilonia, ni sé dónde "
             "está el foso».",
    (1, 36): "Y el ángel del Señor tomó a Habacuc por los cabellos de su cabeza "
             "y lo puso encima del foso que está en Babilonia.",
    (1, 37): "Y dijo Habacuc a Daniel: «Levántate y come la comida que te ha "
             "enviado el Señor Dios».",
    (1, 38): "Y dijo Daniel: «Se acordó, pues, de mí el Señor Dios, que no "
             "abandona a los que lo aman».",
    (1, 39): "Y comió Daniel; y el ángel del Señor devolvió a Habacuc al lugar "
             "de donde lo había tomado, el mismo día. Y el Señor Dios se acordó "
             "de Daniel.",
    (1, 40): "Y salió el rey después de esto, haciendo duelo por Daniel; y "
             "asomándose al foso, lo ve sentado.",
    (1, 41): "Y clamando, dijo el rey: «Grande es el Señor Dios, y no hay otro "
             "fuera de él».",
    (1, 42): "Y sacó el rey a Daniel del foso; y a los culpables de su perdición "
             "los echó en el foso delante de Daniel, y fueron devorados.",
}

# --- Bel y el Dragón, versión de Teodoción ----------------------------------
BEL_TEODOCION_ES: dict[tuple[int, int], str] = {
    (1, 1): "Y el rey Astiages fue reunido con sus padres, y Ciro el persa "
            "recibió su reino.",
    (1, 2): "Y Daniel era compañero del rey, y honrado más que todos sus amigos.",
    (1, 3): "Y tenían los babilonios un ídolo cuyo nombre era Bel, y se gastaban "
            "en él cada día doce artabas de flor de harina, cuarenta ovejas y "
            "seis metretas de vino.",
    (1, 4): "Y el rey lo veneraba, e iba cada día a postrarse ante él; pero "
            "Daniel se postraba ante su Dios. Y le dijo el rey: «¿Por qué no te "
            "postras ante Bel?».",
    (1, 5): "Y él dijo: «Porque yo no venero ídolos hechos por mano de hombre, "
            "sino al Dios vivo, el que creó el cielo y la tierra y tiene señorío "
            "sobre toda carne».",
    (1, 6): "Y le dijo el rey: «¿No te parece que Bel es un dios vivo? ¿O no ves "
            "cuánto come y bebe cada día?».",
    (1, 7): "Y dijo Daniel riéndose: «No te engañes, oh rey; porque éste por "
            "dentro es barro y por fuera bronce, y nunca ha comido nada».",
    (1, 8): "Y airado el rey, llamó a sus sacerdotes y les dijo: «Si no me "
            "decís quién come este gasto, moriréis;",
    (1, 9): "pero si demostráis que Bel lo come, morirá Daniel, porque ha "
            "blasfemado contra Bel». Y dijo Daniel al rey: «Sea conforme a tu "
            "palabra».",
    (1, 10): "Y eran los sacerdotes de Bel setenta, sin contar mujeres y niños. "
             "Y fue el rey con Daniel a la casa de Bel.",
    (1, 11): "Y dijeron los sacerdotes de Bel: «Mira, nosotros salimos fuera; y "
             "tú, oh rey, pon los manjares y el vino mezclado, y cierra la "
             "puerta y séllala con tu anillo.",
    (1, 12): "Y si al venir de mañana no lo hallas todo comido por Bel, "
             "moriremos nosotros; y si no, Daniel, que miente contra nosotros».",
    (1, 13): "Pero ellos estaban tranquilos, porque habían hecho debajo de la "
             "mesa una entrada escondida, y por ella entraban continuamente y lo "
             "consumían.",
    (1, 14): "Y sucedió que, en cuanto salieron ellos, el rey puso los manjares "
             "delante de Bel. Y mandó Daniel a sus criados, y trajeron ceniza, y "
             "espolvorearon todo el templo en presencia del rey solo; y "
             "saliendo, cerraron la puerta y la sellaron con el anillo del rey.",
    (1, 15): "Y los sacerdotes vinieron de noche, según su costumbre, con sus "
             "mujeres y sus hijos, y se lo comieron todo y lo bebieron.",
    (1, 16): "Y el rey madrugó de mañana, y Daniel con él.",
    (1, 17): "Y dijo: «¿Están intactos los sellos, Daniel?». Y él dijo: "
             "«Intactos, oh rey».",
    (1, 18): "Y sucedió que, al abrir las puertas, mirando el rey sobre la mesa, "
             "clamó a gran voz: «Grande eres, Bel, y no hay en ti engaño alguno».",
    (1, 19): "Y se rió Daniel, y detuvo al rey para que no entrara dentro, y "
             "dijo: «Mira el suelo y reconoce de quién son estas huellas».",
    (1, 20): "Y dijo el rey: «Veo huellas de hombres y de mujeres y de niños».",
    (1, 21): "Y airado el rey, prendió entonces a los sacerdotes y a sus mujeres "
             "y a sus hijos; y ellos le mostraron las puertas escondidas por las "
             "que entraban y consumían lo que había sobre la mesa.",
    (1, 22): "Y el rey los mató, y entregó a Bel a Daniel; y él lo derribó, y "
             "también su templo.",
    (1, 23): "Y había un gran dragón, y los babilonios lo veneraban.",
    (1, 24): "Y dijo el rey a Daniel: «No puedes decir que éste no es un dios "
             "vivo; póstrate, pues, ante él».",
    (1, 25): "Y dijo Daniel: «Al Señor mi Dios me postraré, porque éste es Dios "
             "vivo;",
    (1, 26): "y tú, oh rey, dame autoridad y mataré al dragón sin espada ni "
             "palo». Y dijo el rey: «Te la doy».",
    (1, 27): "Y tomó Daniel pez y sebo y pelos, y lo coció todo junto e hizo "
             "unas tortas, y las echó en la boca del dragón; y en comiéndolas, "
             "reventó el dragón. Y dijo: «Mirad lo que veneráis».",
    (1, 28): "Y sucedió que, cuando lo oyeron los babilonios, se indignaron y se "
             "amotinaron contra el rey y dijeron: «Judío se ha vuelto el rey: "
             "derribó a Bel y mató al dragón y degolló a los sacerdotes».",
    (1, 29): "Y viniendo al rey, dijeron: «Entréganos a Daniel; y si no, te "
             "mataremos a ti y a tu casa».",
    (1, 30): "Y vio el rey que lo apremiaban mucho, y obligado les entregó a "
             "Daniel.",
    (1, 31): "Y ellos lo echaron en el foso de los leones, y estuvo allí seis "
             "días.",
    (1, 32): "Y había en el foso siete leones, y se les daba cada día dos "
             "cuerpos y dos ovejas; pero entonces no se les dio nada, para que "
             "devorasen a Daniel.",
    (1, 33): "Y estaba Habacuc el profeta en Judea, y él había cocido un guisado "
             "y había desmigado panes en una cesta, e iba al campo a llevárselo "
             "a los segadores.",
    (1, 34): "Y dijo el ángel del Señor a Habacuc: «Lleva la comida que tienes a "
             "Babilonia, a Daniel, al foso de los leones».",
    (1, 35): "Y dijo Habacuc: «Señor, yo no he visto Babilonia, ni conozco el "
             "foso».",
    (1, 36): "Y lo tomó el ángel del Señor por la coronilla y, llevándolo por "
             "los cabellos de su cabeza, lo puso en Babilonia encima del foso, "
             "con el ímpetu de […]",
}
