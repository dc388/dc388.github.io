"""Susana en español, traducida del griego, en sus dos versiones.

Susana es el capítulo 13 de Daniel en la Vulgata y no está en el hebreo: para
las Asambleas de Dios no es canon, y aquí se ofrece para estudio. Merece la
pena leerla por lo que es: el primer relato de detectives de la literatura
occidental, y una defensa de que un juicio sin interrogatorio no es un juicio.

Viene en dos versiones griegas que no son la misma obra, y las dos están en la
aplicación porque compararlas es el ejercicio:

- La de los Setenta (SUS) es más corta y más dura. Daniel interroga y sentencia
  en primera persona, y el relato termina con una moraleja sobre los jóvenes.
- La de Teodoción (SUT) es la que pasó a la Vulgata y la que se conoce. Cuenta
  el baño en el huerto, la escena que los ancianos espían, y a Susana clamando
  en voz alta; es más narrativa y menos sentenciosa.

El juego de palabras del interrogatorio no se puede traducir y sostener a la
vez, así que se sostiene: el anciano dice «debajo de un lentisco» (σχῖνον) y
Daniel responde que el ángel lo «partirá» (σχίσει); el otro dice «debajo de una
encina» (πρῖνον) y el ángel lo «aserrará» (πρίσαι). En español se conservan los
verbos partir y aserrar para que el eco se vea aunque el nombre del árbol ya no
rime, que es lo que hacen todas las traducciones serias.

Los versículos partidos llevan su letra: la versión de los Setenta tiene dos 35
y tres 62, y sin la letra los tres se quedarían con el mismo texto.
"""

from __future__ import annotations

# --- Susana, versión de los Setenta ----------------------------------------
SUSANA_ES: dict[tuple[int, int, str], str] = {
    (1, 1, ""): "Y había un hombre que vivía en Babilonia, y su nombre era "
                "Joaquín.",
    (1, 2, ""): "Y tomó por mujer a una cuyo nombre era Susana, hija de Jelcías, "
                "muy hermosa y temerosa del Señor;",
    (1, 3, ""): "y sus padres eran justos, y enseñaron a su hija conforme a la "
                "ley de Moisés.",
    (1, 4, ""): "Y Joaquín era muy rico, y tenía un huerto contiguo a su casa; y "
                "a él acudían los judíos, por ser él el más honorable de todos.",
    (1, 5, ""): "Y fueron nombrados aquel año dos ancianos del pueblo como "
                "jueces, de los cuales dijo el Soberano: «Salió iniquidad de "
                "Babilonia, de ancianos jueces que parecían gobernar al pueblo».",
    (1, 6, ""): "Y venían a ellos pleitos de otras ciudades.",
    (1, 7, ""): "Éstos, viendo a una mujer de hermosa figura —mujer de un hermano "
                "suyo de los hijos de Israel, de nombre Susana, hija de Jelcías, "
                "mujer de Joaquín—, que paseaba por el huerto de su marido al "
                "caer la tarde,",
    (1, 8, ""): "y habiéndola deseado,",
    (1, 9, ""): "pervirtieron su entendimiento y apartaron sus ojos para no "
                "mirar al cielo ni acordarse de los juicios justos.",
    (1, 10, ""): "Y ambos estaban heridos por ella, y ninguno confesaba al otro "
                 "el mal que los tenía por ella; ni la mujer supo de este asunto.",
    (1, 12, ""): "Y cuando llegaba el amanecer, venían escondiéndose el uno del "
                 "otro, compitiendo por ver quién se le mostraría primero y le "
                 "hablaría.",
    (1, 13, ""): "Y he aquí que ella paseaba según su costumbre, y uno de los "
                 "ancianos había llegado; y he aquí que llegó el otro, y el uno "
                 "interrogó al otro diciendo: «¿Por qué has salido tú tan de "
                 "madrugada sin llevarme contigo?».",
    (1, 14, ""): "Y se confesaron el uno al otro su tormento.",
    (1, 19, ""): "Y dijo el uno al otro: «Vayamos a ella». Y puestos de acuerdo, "
                 "se acercaron a ella y la forzaban.",
    (1, 22, ""): "Y les dijo la judía: «Sé que, si hago esto, es la muerte para "
                 "mí; y si no lo hago, no escaparé de vuestras manos.",
    (1, 23, ""): "Pero mejor me es caer en vuestras manos sin haberlo hecho, que "
                 "pecar delante del Señor».",
    (1, 28, ""): "Y aquellos hombres inicuos se volvieron amenazando entre sí y "
                 "acechando para darle muerte; y llegando a la sinagoga de la "
                 "ciudad donde residían, se sentaron en consejo todos los hijos "
                 "de Israel que allí estaban.",
    (1, 29, ""): "Y levantándose los dos ancianos y jueces, dijeron: «Enviad por "
                 "Susana, hija de Jelcías, que es mujer de Joaquín». Y ellos la "
                 "llamaron enseguida.",
    (1, 30, ""): "Y cuando llegó la mujer con su padre y su madre, llegaron "
                 "también sus criados y sus criadas, que eran quinientos en "
                 "número, y los cuatro hijos de Susana.",
    (1, 31, ""): "Y la mujer era muy delicada.",
    (1, 32, ""): "Y mandaron los inicuos que la descubrieran, para saciarse de "
                 "la hermosura que deseaban.",
    (1, 33, ""): "Y lloraban todos los suyos y todos cuantos la conocían.",
    (1, 34, ""): "Y levantándose los ancianos y jueces, pusieron sus manos sobre "
                 "su cabeza.",
    (1, 35, ""): "Pero su corazón confiaba en el Señor su Dios; y levantando el "
                 "rostro, lloró para sí, diciendo:",
    (1, 35, "a"): "«Señor, Dios eterno, el que conoce todas las cosas antes de "
                  "que existan: tú sabes que yo no he hecho lo que estos inicuos "
                  "maquinan contra mí». Y el Señor escuchó su súplica.",
    (1, 36, ""): "Y los dos ancianos dijeron: «Nosotros paseábamos por el huerto "
                 "de su marido,",
    (1, 37, ""): "y dando la vuelta al paseo, la vimos a ésta acostada con un "
                 "hombre; y quedándonos quietos, los mirábamos mientras se "
                 "abrazaban;",
    (1, 38, ""): "y ellos no sabían que estábamos allí. Entonces hablamos entre "
                 "nosotros, diciendo: Sepamos quiénes son éstos.",
    (1, 39, ""): "Y acercándonos, la reconocimos a ella; pero el joven huyó, "
                 "cubierto el rostro.",
    (1, 40, ""): "Y echando mano de ésta, le preguntábamos: ¿Quién era el "
                 "hombre?",
    (1, 41, ""): "Y no nos dijo quién era. Esto testificamos». Y les creyó toda "
                 "la asamblea, por ser ancianos y jueces del pueblo.",
    (1, 44, ""): "[44-45] Y he aquí que, mientras la llevaban a morir, un ángel "
                 "del Señor —y dio el ángel, conforme le había sido mandado, "
                 "espíritu de entendimiento a Daniel, que era muy joven—.",
    (1, 48, ""): "Y apartando Daniel a la multitud y poniéndose en medio de "
                 "ellos, dijo: «¿Tan necios sois, hijos de Israel? ¿Sin "
                 "interrogar ni averiguar lo cierto habéis condenado a muerte a "
                 "una hija de Israel?",
    (1, 51, ""): "Y ahora, apartádmelos lejos el uno del otro, para que yo los "
                 "examine».",
    (1, 51, "a"): "Y cuando fueron apartados, dijo Daniel a la asamblea: «Ahora "
                  "no miréis que éstos son ancianos, diciendo: No mentirán; sino "
                  "que yo los interrogaré conforme a lo que se me vaya "
                  "presentando».",
    (1, 52, ""): "Y llamó a uno de ellos, y acercaron al anciano ante el joven; "
                 "y le dijo Daniel: «Oye, oye, envejecido en días malos: ahora "
                 "te han alcanzado los pecados que hacías antes,",
    (1, 53, ""): "cuando se te confiaba oír y juzgar causas que llevan la "
                 "muerte; y al inocente condenabas y a los culpables soltabas, "
                 "diciendo el Señor: Al inocente y al justo no matarás.",
    (1, 54, ""): "Ahora pues, ¿debajo de qué árbol y en qué lugar del huerto los "
                 "viste estar juntos?». Y dijo el impío: «Debajo de un "
                 "lentisco».",
    (1, 55, ""): "Y dijo el joven: «Bien has mentido contra tu propia alma; "
                 "porque el ángel del Señor partirá hoy tu alma».",
    (1, 56, ""): "Y apartando a éste, mandó que le acercaran al otro; y a éste "
                 "le dijo: «¿Por qué es torcida tu simiente, como de Sidón y no "
                 "como de Judá? La hermosura te engañó, el deseo miserable.",
    (1, 57, ""): "Y así hacíais con las hijas de Israel, y ellas, por miedo, se "
                 "juntaban con vosotros; pero una hija de Judá no soportó "
                 "vuestra enfermedad, ni consintió en la iniquidad.",
    (1, 58, ""): "Ahora pues, dime: ¿debajo de qué árbol y en qué lugar del "
                 "huerto los sorprendiste juntos?». Y él dijo: «Debajo de una "
                 "encina».",
    (1, 59, ""): "Y dijo Daniel: «Pecador, ahora el ángel del Señor está en pie "
                 "con la espada, hasta que el pueblo os extermine, para "
                 "aserrarte».",
    (1, 60, ""): "[60-62] Y toda la asamblea clamó a favor del joven, porque por "
                 "su propia boca los había puesto a los dos como testigos falsos "
                 "convictos; y conforme manda la ley hicieron con ellos, según "
                 "habían maquinado contra su hermana. Y los amordazaron y, "
                 "sacándolos, los arrojaron a un barranco; entonces el ángel del "
                 "Señor arrojó fuego en medio de ellos. Y fue salvada sangre "
                 "inocente en aquel día.",
    (1, 62, "a"): "Por eso los jóvenes son los amados de Jacob, por su "
                  "sencillez.",
    (1, 62, "b"): "Y nosotros guardémonos para tener hijos fuertes y jóvenes; "
                  "porque los jóvenes serán piadosos, y habrá en ellos espíritu "
                  "de conocimiento y de entendimiento por el siglo de los siglos.",
}

# --- Susana, versión de Teodoción -------------------------------------------
SUSANA_TEODOCION_ES: dict[tuple[int, int, str], str] = {
    (1, 1, ""): "Y había un hombre que vivía en Babilonia, y su nombre era "
                "Joaquín.",
    (1, 2, ""): "Y tomó por mujer a una cuyo nombre era Susana, hija de Jelcías, "
                "muy hermosa y temerosa del Señor.",
    (1, 3, ""): "Y sus padres eran justos, y enseñaron a su hija conforme a la "
                "ley de Moisés.",
    (1, 4, ""): "Y Joaquín era muy rico, y tenía un huerto contiguo a su casa; y "
                "a él acudían los judíos, por ser él el más honorable de todos.",
    (1, 5, ""): "Y fueron nombrados aquel año dos ancianos del pueblo como "
                "jueces, de los cuales dijo el Soberano: «Salió iniquidad de "
                "Babilonia, de ancianos jueces que parecían gobernar al pueblo».",
    (1, 6, ""): "Éstos frecuentaban la casa de Joaquín, y acudían a ellos todos "
                "los que tenían pleito.",
    (1, 7, ""): "Y sucedía que, cuando el pueblo se retiraba a mediodía, entraba "
                "Susana y paseaba por el huerto de su marido.",
    (1, 8, ""): "Y los dos ancianos la veían entrar y pasear cada día, y "
                "ardieron en deseo de ella.",
    (1, 9, ""): "Y pervirtieron su propio entendimiento, y apartaron sus ojos "
                "para no mirar al cielo ni acordarse de los juicios justos.",
    (1, 10, ""): "Y ambos estaban heridos por ella, y no se declararon el uno al "
                 "otro su tormento,",
    (1, 11, ""): "porque se avergonzaban de declarar su deseo, que era unirse "
                 "con ella.",
    (1, 12, ""): "Y acechaban con empeño, cada día, para verla.",
    (1, 13, ""): "Y se dijeron el uno al otro: «Vayámonos a casa, que es hora de "
                 "comer». Y saliendo, se apartaron el uno del otro.",
    (1, 14, ""): "Pero volviéndose atrás, llegaron al mismo sitio; y "
                 "preguntándose el uno al otro la causa, confesaron su deseo. Y "
                 "entonces acordaron juntos un momento en que pudieran hallarla "
                 "sola.",
    (1, 15, ""): "Y sucedió que, mientras acechaban un día propicio, entró ella "
                 "una vez como ayer y anteayer, sólo con dos criadas, y quiso "
                 "bañarse en el huerto, porque hacía calor.",
    (1, 16, ""): "Y no había allí nadie, salvo los dos ancianos, escondidos y "
                 "acechándola.",
    (1, 17, ""): "Y dijo a las criadas: «Traedme aceite y ungüentos, y cerrad "
                 "las puertas del huerto, para que me bañe».",
    (1, 18, ""): "Y ellas hicieron como dijo: cerraron las puertas del huerto y "
                 "salieron por las puertas laterales a traer lo que se les había "
                 "mandado; y no vieron a los ancianos, porque estaban "
                 "escondidos.",
    (1, 19, ""): "Y sucedió que, en cuanto salieron las criadas, se levantaron "
                 "los dos ancianos y corrieron hacia ella,",
    (1, 20, ""): "y dijeron: «Mira, las puertas del huerto están cerradas y "
                 "nadie nos ve, y estamos ardiendo por ti. Consiente, pues, y "
                 "acuéstate con nosotros.",
    (1, 21, ""): "Y si no, testificaremos contra ti que estaba contigo un joven, "
                 "y que por eso despediste a las criadas».",
    (1, 22, ""): "Y gimió Susana y dijo: «Estoy en aprieto por todos lados: "
                 "porque si hago esto, es la muerte para mí; y si no lo hago, no "
                 "escaparé de vuestras manos.",
    (1, 23, ""): "Mejor me es caer en vuestras manos sin haberlo hecho, que "
                 "pecar delante del Señor».",
    (1, 24, ""): "Y clamó Susana a gran voz; y clamaron también los dos "
                 "ancianos contra ella.",
    (1, 25, ""): "Y corriendo uno de ellos, abrió las puertas del huerto.",
    (1, 26, ""): "Y cuando los de la casa oyeron el grito en el huerto, entraron "
                 "de golpe por la puerta lateral para ver qué le había pasado.",
    (1, 27, ""): "Y cuando los ancianos dijeron sus palabras, los siervos se "
                 "avergonzaron mucho, porque jamás se había dicho tal cosa de "
                 "Susana.",
    (1, 28, ""): "Y sucedió que al día siguiente, cuando el pueblo se reunió en "
                 "casa de su marido Joaquín, llegaron los dos ancianos llenos de "
                 "su designio inicuo contra Susana, para darle muerte, y dijeron "
                 "delante del pueblo:",
    (1, 29, ""): "«Enviad por Susana, hija de Jelcías, que es mujer de Joaquín». "
                 "Y ellos enviaron.",
    (1, 30, ""): "Y vino ella, y sus padres y sus hijos y todos sus parientes.",
    (1, 31, ""): "Y Susana era muy delicada y hermosa de figura.",
    (1, 32, ""): "Y los inicuos mandaron que la descubrieran —porque estaba "
                 "cubierta con el velo—, para saciarse de su hermosura.",
    (1, 33, ""): "Y lloraban los suyos y todos los que la veían.",
    (1, 34, ""): "Y levantándose los dos ancianos en medio del pueblo, pusieron "
                 "sus manos sobre su cabeza.",
    (1, 35, ""): "Y ella, llorando, levantó los ojos al cielo, porque su corazón "
                 "confiaba en el Señor.",
    (1, 36, ""): "Y dijeron los ancianos: «Paseando nosotros solos por el "
                 "huerto, entró ésta con dos criadas, y cerró las puertas del "
                 "huerto y despidió a las criadas.",
    (1, 37, ""): "Y vino a ella un joven, que estaba escondido, y se acostó con "
                 "ella.",
    (1, 38, ""): "Y nosotros, que estábamos en un rincón del huerto, al ver la "
                 "iniquidad corrimos hacia ellos;",
    (1, 39, ""): "y viéndolos juntos, a él no pudimos sujetarlo, porque era más "
                 "fuerte que nosotros y, abriendo las puertas, saltó fuera;",
    (1, 40, ""): "pero echando mano de ésta, le preguntábamos quién era el "
                 "joven,",
    (1, 41, ""): "y no quiso decírnoslo. Esto testificamos». Y les creyó la "
                 "asamblea, por ser ancianos del pueblo y jueces, y la "
                 "condenaron a morir.",
    (1, 42, ""): "Y clamó Susana a gran voz y dijo: «Dios eterno, conocedor de "
                 "lo escondido, el que sabe todas las cosas antes de que existan:",
    (1, 43, ""): "tú sabes que testificaron mentira contra mí. Y he aquí que "
                 "muero sin haber hecho nada de lo que éstos han maquinado "
                 "contra mí».",
    (1, 44, ""): "Y el Señor escuchó su voz.",
    (1, 45, ""): "Y mientras la llevaban a morir, despertó Dios el espíritu "
                 "santo de un muchacho muy joven, de nombre Daniel.",
    (1, 46, ""): "Y clamó a gran voz: «¡Inocente soy yo de la sangre de ésta!».",
    (1, 47, ""): "Y todo el pueblo se volvió hacia él y dijeron: «¿Qué palabra "
                 "es ésta que has dicho?».",
    (1, 48, ""): "Y él, puesto en medio de ellos, dijo: «¿Tan necios sois, hijos "
                 "de Israel? ¿Sin interrogar ni averiguar lo cierto habéis "
                 "condenado a una hija de Israel?",
    (1, 49, ""): "Volved al tribunal, porque éstos han testificado mentira "
                 "contra ella».",
    (1, 50, ""): "Y todo el pueblo volvió a toda prisa. Y le dijeron los "
                 "ancianos: «Ven, siéntate en medio de nosotros y decláranoslo, "
                 "porque Dios te ha dado la dignidad de anciano».",
    (1, 51, ""): "Y les dijo Daniel: «Apartadlos lejos el uno del otro, y yo los "
                 "interrogaré».",
    (1, 52, ""): "Y cuando fueron apartados el uno del otro, llamó a uno de "
                 "ellos y le dijo: «Envejecido en días malos: ahora te han "
                 "alcanzado los pecados que hacías antes,",
    (1, 53, ""): "juzgando juicios injustos, condenando a los inocentes y "
                 "soltando a los culpables, diciendo el Señor: Al inocente y al "
                 "justo no matarás.",
    (1, 54, ""): "Ahora pues, si de veras la viste, di: ¿debajo de qué árbol los "
                 "viste juntos?». Y él dijo: «Debajo de un lentisco».",
    (1, 55, ""): "Y dijo Daniel: «Bien has mentido contra tu propia cabeza; "
                 "porque ya el ángel de Dios, recibida de Dios la sentencia, te "
                 "partirá por medio».",
    (1, 56, ""): "Y apartándolo, mandó que acercaran al otro; y le dijo: "
                 "«Simiente de Canaán y no de Judá: la hermosura te engañó y el "
                 "deseo pervirtió tu corazón.",
    (1, 57, ""): "Así hacíais con las hijas de Israel, y ellas, por miedo, se "
                 "juntaban con vosotros; pero una hija de Judá no soportó "
                 "vuestra iniquidad.",
    (1, 58, ""): "Ahora pues, dime: ¿debajo de qué árbol los sorprendiste "
                 "juntos?». Y él dijo: «Debajo de una encina».",
    (1, 59, ""): "Y le dijo Daniel: «Bien has mentido también tú contra tu "
                 "propia cabeza; porque el ángel de Dios está esperando con la "
                 "espada para aserrarte por medio, y así exterminaros».",
    (1, 60, ""): "Y toda la asamblea clamó a gran voz, y bendijeron a Dios, que "
                 "salva a los que esperan en él.",
    (1, 61, ""): "Y se levantaron contra los dos ancianos, porque Daniel los "
                 "había convencido, por su propia boca, de ser testigos falsos; "
                 "e hicieron con ellos como ellos habían maquinado contra su "
                 "prójimo,",
    (1, 62, ""): "obrando conforme a la ley de Moisés, y los mataron. Y fue "
                 "salvada sangre inocente en aquel día.",
    (1, 63, ""): "Y Jelcías y su mujer alabaron a Dios por su hija, junto con "
                 "Joaquín su marido y todos los parientes, porque no se halló en "
                 "ella cosa indecorosa.",
    (1, 64, ""): "Y Daniel llegó a ser grande delante del pueblo desde aquel día "
                 "en adelante.",
}
