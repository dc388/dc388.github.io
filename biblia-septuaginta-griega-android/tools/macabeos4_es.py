"""4 Macabeos en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Tampoco éste es
una crónica: es un discurso filosófico, y el único libro de esta biblioteca que
está construido como una demostración. La tesis se enuncia en la primera línea
y se repite como un martillo: «la razón piadosa es dueña absoluta de las
pasiones».

Para probarlo toma el relato que ya está en 2 Macabeos 6-7 —el anciano Eleazar
y los siete hermanos con su madre, torturados por Antíoco por no comer carne de
cerdo— y lo convierte en el argumento: si estos hombres y esta mujer aguantaron
eso, entonces la razón educada por la ley de Dios puede con el miedo, con el
dolor y hasta con el amor de una madre por sus hijos. Es filosofía estoica
hablada en judío: el autor usa las cuatro virtudes de los griegos —prudencia,
justicia, fortaleza, templanza— pero dice que la escuela donde se aprenden es
la Torá.

Conviene leerlo sabiendo dos cosas. La primera es que las escenas de tortura
son largas y detalladas, porque el género lo pedía; no es morbo, es la prueba
de la tesis, pero avisa. La segunda es que aquí aparece por primera vez, con
todas sus letras, la idea de que la muerte del justo es un rescate: «que mi
sangre sea su purificación, y toma mi vida en lugar de la suya» (6:29), y «por
la sangre de aquellos piadosos... la patria fue purificada» (17:21-22). Esa
manera de hablar estaba en el aire cuando se escribió el Nuevo Testamento, y
por eso vale la pena verla en su sitio.

Los términos técnicos se traducen siempre igual para que el argumento se pueda
seguir: λογισμός es «la razón», πάθη son «las pasiones», σωφροσύνη es
«templanza», φρόνησις «prudencia», ἀνδρεία «valor» y δικαιοσύνη «justicia».
"""

from __future__ import annotations

MACABEOS4_ES: dict[tuple[int, ...], str] = {
    (1, 1): "Al ir a exponer un asunto sumamente filosófico —si la razón "
            "piadosa es dueña absoluta de las pasiones—, os aconsejaría con "
            "razón que prestéis atención de buena gana a esta filosofía.",
    (1, 2): "Porque este razonamiento es necesario para el saber de "
            "cualquiera, y además encierra el elogio de la mayor de las "
            "virtudes, quiero decir, de la prudencia.",
    (1, 3): "Pues si se ve que la razón domina las pasiones que estorban la "
            "templanza —la glotonería y el deseo—,",
    (1, 4): "también queda claro que señorea las pasiones que estorban la "
            "justicia, como la malicia, y las que estorban el valor: la ira y "
            "el dolor y el miedo.",
    (1, 5): "¿Cómo es, pues —dirán quizá algunos—, que si la razón domina las "
            "pasiones, no manda sobre el olvido y la ignorancia? Es una "
            "objeción ridícula;",
    (1, 6): "porque la razón no domina sus propias pasiones, sino las "
            "contrarias a la justicia y al valor y a la templanza y a la "
            "prudencia; y a éstas no para suprimirlas, sino para no cederles.",
    (1, 7): "Podría demostraros por muchos caminos y de muchas maneras que la "
            "razón piadosa es soberana de las pasiones;",
    (1, 8): "pero lo demostraré mucho mejor por el valor de los que murieron "
            "por la virtud: Eleazar y los siete hermanos y la madre de "
            "éstos.",
    (1, 9): "Porque todos ellos, despreciando los tormentos hasta la muerte, "
            "demostraron que la razón vence a las pasiones.",
    (1, 10): "Por sus virtudes me toca alabar a estos hombres que en aquel "
             "tiempo murieron con su madre por la nobleza; y por sus honores "
             "los llamaría dichosos.",
    (1, 11): "Porque aquéllos, admirados no sólo por todos los hombres a causa "
             "de su valor y de su aguante, sino hasta por los que los "
             "torturaban, fueron la causa de que se acabase la tiranía sobre "
             "su pueblo, venciendo al tirano con su aguante, de modo que por "
             "ellos quedó purificada la patria.",
    (1, 12): "Pero de esto podré hablar en seguida, empezando por el asunto, "
             "como acostumbro a hacer, y luego pasaré al relato sobre ellos, "
             "dando gloria al Dios sapientísimo.",
    (1, 13): "Investigamos, pues, si la razón es soberana de las pasiones.",
    (1, 14): "Distingamos qué es la razón y qué la pasión, y cuántas clases "
             "hay de pasiones, y si la razón las domina todas.",
    (1, 15): "La razón es, pues, el entendimiento que, con una vida recta, "
             "prefiere el discurso de la sabiduría.",
    (1, 16): "Y la sabiduría es el conocimiento de las cosas divinas y humanas "
             "y de sus causas. Y ésta es la instrucción de la ley, por la que "
             "aprendemos las cosas divinas con reverencia y las humanas con "
             "provecho.",
    (1, 18): "Y las formas de la sabiduría son la prudencia y la justicia y el "
             "valor y la templanza;",
    (1, 19): "y la principal de todas es la prudencia, de la que la razón saca "
             "el dominio de las pasiones.",
    (1, 20): "Y las clases de pasiones más abarcadoras son dos: el placer y el "
             "dolor; y cada una de ellas está también, por naturaleza, en el "
             "alma.",
    (1, 21): "Y hay muchas pasiones que acompañan al placer y al dolor.",
    (1, 22): "Antes del placer está el deseo; después del placer, la alegría.",
    (1, 23): "Antes del dolor está el miedo; después del dolor, la tristeza.",
    (1, 24): "Y la ira es una pasión común al placer y al dolor, si uno se "
             "para a pensar cuándo le sobrevino.",
    (1, 25): "Y en el placer está también la disposición maliciosa, que es la "
             "más versátil de todas las pasiones:",
    (1, 26): "en el alma, la jactancia y la avaricia y la vanagloria y la "
             "porfía y la envidia;",
    (1, 27): "y en el cuerpo, comer de todo y la gula y el comer a solas.",
    (1, 28): "Y como el placer y el dolor son dos plantas del cuerpo y del "
             "alma, muchos son los brotes de estas pasiones;",
    (1, 29): "y a cada uno de ellos la razón, labrador universal, lo escarda y "
             "lo poda y lo ata y lo riega y lo trasiega de todas las maneras, "
             "y domestica así la maleza de los caracteres y de las pasiones.",
    (1, 30): "Porque la razón es guía de las virtudes y soberana de las "
             "pasiones. Fíjate, pues, primero en las obras que estorban la "
             "templanza, para ver que la razón es dueña de las pasiones.",
    (1, 31): "La templanza es, pues, el dominio de los deseos.",
    (1, 32): "Y de los deseos, unos son del alma y otros del cuerpo; y se ve "
             "que la razón domina ambos.",
    (1, 33): "Porque, si no, ¿por qué, sintiéndonos atraídos hacia alimentos "
             "prohibidos, renunciamos a los placeres que dan? ¿No es porque la "
             "razón puede dominar los apetitos? Yo, al menos, así lo creo.",
    (1, 34): "Por eso, aun deseando pescados y aves y cuadrúpedos y toda clase "
             "de manjares que la ley nos prohíbe, nos abstenemos por el "
             "dominio de la razón.",
    (1, 35): "Porque las pasiones del apetito quedan sujetas, refrenadas por "
             "el entendimiento templado; y todos los movimientos del cuerpo "
             "quedan bajo la disciplina de la razón.",

    (2, 1): "Y ¿qué tiene de extraño que los deseos del alma queden anulados "
            "ante la participación en la hermosura?",
    (2, 2): "Por eso se alaba a José el casto, porque con la razón, con la "
            "reflexión, dominó el placer.",
    (2, 3): "Porque, siendo joven y en la flor de la edad para el trato "
            "carnal, anuló con la razón el aguijón de las pasiones.",
    (2, 4): "Y se ve que la razón domina no sólo el aguijón del placer, sino "
            "todo deseo.",
    (2, 5): "Porque dice la ley: «No desearás la mujer de tu prójimo, ni nada "
            "de lo que es de tu prójimo».",
    (2, 6): "Y si la ley nos ha dicho que no deseemos, mucho más os "
            "convencería de que la razón puede dominar los deseos, igual que "
            "domina las pasiones que estorban la justicia.",
    (2, 7): "Porque ¿de qué modo se corrige uno que es de carácter comilón "
            "solitario y glotón y borracho, si no es porque es claro que la "
            "razón es dueña de las pasiones?",
    (2, 8): "Así, en cuanto uno se rige por la ley, aunque sea avaro, se hace "
            "violencia a su propia inclinación, y presta sin interés a los que "
            "lo necesitan, y cancela la deuda cuando llegan los años "
            "sabáticos.",
    (2, 9): "Y aunque uno sea tacaño, la ley lo domina por medio de la razón: "
            "no rebusca su cosecha ni vuelve a vendimiar sus viñas. Y en lo "
            "demás también se puede reconocer que la razón domina las "
            "pasiones.",
    (2, 10): "Porque la ley domina hasta el cariño a los padres, sin traicionar "
             "la virtud por ellos;",
    (2, 11): "y domina el amor a la esposa, censurándola cuando transgrede;",
    (2, 12): "y señorea el amor a los hijos, castigándolos por su maldad; y "
             "manda sobre el trato con los amigos, reprendiéndolos por su "
             "perversidad.",
    (2, 13): "Y no creáis que es cosa extraña que la razón pueda dominar hasta "
             "la enemistad por medio de la ley,",
    (2, 14): "cuando no se talan los árboles frutales de los enemigos, sino "
             "que se salva lo de los enemigos para los que lo han perdido, y "
             "se levanta lo caído.",
    (2, 15): "Y se ve que la razón domina también las pasiones más violentas: "
             "el ansia de mandar y la vanagloria y la jactancia y la soberbia "
             "y la envidia.",
    (2, 16): "Porque todas estas pasiones maliciosas las rechaza el "
             "entendimiento templado, lo mismo que la ira; porque también "
             "manda sobre ella.",
    (2, 17): "Así Moisés, aunque estaba airado contra Datán y Abirón, no hizo "
             "nada contra ellos movido por la ira, sino que gobernó su ira con "
             "la razón.",
    (2, 18): "Porque el entendimiento templado es capaz, como he dicho, de "
             "vencer a las pasiones, y de cambiar unas y de anular otras.",
    (2, 19): "Pues, si no, ¿por qué nuestro sapientísimo padre Jacob reprocha "
             "a Simeón y a Leví el haber degollado a toda la nación de los "
             "siquemitas sin razón, diciendo: «Maldita su ira»?",
    (2, 20): "Porque si la razón no pudiera dominar la ira, no habría hablado "
             "así.",
    (2, 21): "Porque cuando Dios formó al hombre, le plantó dentro sus "
             "pasiones y sus inclinaciones;",
    (2, 22): "y entonces mismo entronizó por encima de todo, por medio de los "
             "sentidos, al entendimiento como guía sagrado;",
    (2, 23): "y a éste le dio una ley, conforme a la cual, si se gobierna, "
             "reinará con un reinado templado y justo y bueno y valiente.",
    (2, 24): "¿Cómo es, pues —dirá alguien—, que si la razón domina las "
             "pasiones, no domina el olvido y la ignorancia?",

    (3, 1): "«Es un razonamiento del todo ridículo; porque no se ve que la "
            "razón domine sus propias pasiones, sino las del cuerpo».",
    (3, 2): "Por ejemplo: ninguno de vosotros puede arrancar de raíz el deseo, "
            "pero la razón sí puede hacer que uno no quede esclavo del "
            "deseo.",
    (3, 3): "Ninguno de vosotros puede arrancar la ira del alma, pero sí es "
            "posible hacer frente a la ira.",
    (3, 4): "Ninguno de vosotros puede arrancar la malicia, pero la razón "
            "puede ayudar a no doblegarse ante la malicia.",
    (3, 5): "Porque la razón no es la que arranca de cuajo las pasiones, sino "
            "la que lucha contra ellas.",
    (3, 6): "Y esto se puede entender con más claridad por la sed del rey "
            "David.",
    (3, 7): "Porque, habiendo atacado David a los extranjeros durante todo el "
            "día y matado a muchos de ellos con los soldados de su pueblo,",
    (3, 8): "al llegar la tarde, sudoroso y muy fatigado, vino a la tienda "
            "real, en torno a la cual estaba acampado todo el ejército de "
            "nuestros antepasados.",
    (3, 9): "Y todos los demás estaban cenando;",
    (3, 10): "pero el rey, muerto de sed, aunque tenía fuentes en abundancia, "
             "no podía con ellas curar su sed,",
    (3, 11): "sino que un deseo irracional del agua que estaba en poder de los "
             "enemigos lo abrasaba, creciendo, y lo consumía deshaciéndolo.",
    (3, 12): "Por lo cual, como los de su guardia se quejaban del capricho del "
             "rey, dos jóvenes soldados esforzados, avergonzados de que el rey "
             "lo deseara, se armaron de todas sus armas y, tomando un cántaro, "
             "saltaron las empalizadas de los enemigos;",
    (3, 13): "y burlando a los centinelas de las puertas, se abrieron paso "
             "buscando por todo el campamento enemigo.",
    (3, 14): "Y hallando con audacia la fuente, llenaron de ella la bebida "
             "para el rey.",
    (3, 15): "Pero él, aunque ardía de sed, pensó que era un peligro terrible "
             "para su alma, y consideró que aquella bebida equivalía a sangre.",
    (3, 16): "Por lo cual, oponiendo la razón al deseo, derramó aquella bebida "
             "como libación a Dios.",
    (3, 17): "Porque el entendimiento templado es capaz de vencer las "
             "violencias de las pasiones y de apagar los ardores de los "
             "aguijones,",
    (3, 18): "y de derribar los dolores del cuerpo por grandes que sean, y, "
             "por la nobleza de la razón, de escupir sobre todos los dominios "
             "de las pasiones.",
    (3, 19): "Y ya el momento nos llama a la demostración por medio de la "
             "historia de la razón templada.",
    (3, 20): "Porque, cuando nuestros padres gozaban de una paz profunda "
             "gracias al buen orden de sus leyes, y les iba bien, hasta el "
             "punto de que el rey de Asia, Seleuco Nicanor, les asignó dinero "
             "para el culto y reconoció su régimen,",
    (3, 21): "entonces algunos, alzándose contra la concordia común, "
             "provocaron desgracias de toda clase.",

    (4, 1): "Porque un tal Simón, que hacía oposición a Onías —el que entonces "
            "tenía el sumo sacerdocio de por vida, hombre noble y bueno—, como "
            "no logró perjudicarlo por más que lo calumnió de todos los modos "
            "en detrimento de su pueblo, se marchó al destierro con intención "
            "de traicionar a su patria.",
    (4, 2): "Por lo cual, presentándose a Apolonio, general de Siria y de "
            "Fenicia y de Cilicia, le dijo:",
    (4, 3): "«Vengo por lealtad a los intereses del rey, para denunciar que en "
            "los tesoros de Jerusalén hay acumuladas muchas decenas de miles "
            "de fondos privados que no pertenecen al templo, sino que le "
            "corresponden al rey Seleuco».",
    (4, 4): "Y enterado Apolonio de todo esto, alabó a Simón por su cuidado de "
            "los intereses del rey, y, subiendo ante Seleuco, le denunció "
            "aquel tesoro de dinero;",
    (4, 5): "y recibiendo autorización sobre ello, vino rápidamente a nuestra "
            "patria con el maldito Simón y con un ejército muy pesado,",
    (4, 6): "y, presentándose, dijo que venía por orden del rey, para hacerse "
            "con los fondos privados del tesoro.",
    (4, 7): "Y como el pueblo se indignó ante aquella palabra y le replicaba, "
            "pensando que sería terrible que los que habían confiado sus "
            "depósitos al tesoro sagrado se vieran despojados, lo impedían "
            "como podían.",
    (4, 8): "Pero Apolonio se dirigía al templo lanzando amenazas.",
    (4, 9): "Y mientras los sacerdotes, con las mujeres y los niños, suplicaban "
            "en el templo a Dios que escudase aquel lugar despreciado,",
    (4, 10): "y mientras subía Apolonio con su ejército armado a saquear el "
             "dinero, se aparecieron desde el cielo unos ángeles a caballo, "
             "relampagueando con sus armas, que les infundieron un gran miedo "
             "y temblor.",
    (4, 11): "Y Apolonio cayó medio muerto en el atrio del templo abierto a "
             "todos, y extendió las manos al cielo, y con lágrimas rogaba a "
             "los hebreos que orasen por él y aplacasen al ejército celestial.",
    (4, 12): "Porque decía que había pecado hasta merecer la muerte, y que, si "
             "se salvaba, cantaría ante todos los hombres la dicha de aquel "
             "lugar sagrado.",
    (4, 13): "Movido por estas palabras, Onías el sumo sacerdote, aunque por "
             "otra parte temía que el rey Seleuco pensara que Apolonio había "
             "sido eliminado por una conjura humana y no por castigo divino, "
             "oró por él.",
    (4, 14): "Y él, salvado contra toda esperanza, se marchó a dar cuenta al "
             "rey de lo que le había pasado.",
    (4, 15): "Y muerto el rey Seleuco, le sucede en el mando su hijo Antíoco "
             "Epífanes, hombre soberbio y terrible;",
    (4, 16): "el cual, deponiendo del sumo sacerdocio a Onías, puso como sumo "
             "sacerdote a su hermano Jasón,",
    (4, 17): "que se comprometió a dar, si le confiaba el cargo, tres mil "
             "seiscientos sesenta talentos al año.",
    (4, 18): "Y él le confió el sumo sacerdocio y el gobierno del pueblo;",
    (4, 19): "y aquél trastornó al pueblo y lo hizo vivir en toda clase de "
             "transgresiones,",
    (4, 20): "hasta el punto de construir un gimnasio en la misma ciudadela de "
             "nuestra patria y de acabar con el cuidado del templo.",
    (4, 21): "Por lo cual, indignada la justicia divina, le puso en guerra al "
             "propio Antíoco.",
    (4, 22): "Porque, estando él en guerra en Egipto contra Tolomeo, se enteró "
             "de que, al correr el rumor de que había muerto, los de Jerusalén "
             "se habían alegrado enormemente, y se volvió rápidamente contra "
             "ellos.",
    (4, 23): "Y después de saquearlos, dictó un decreto: que si alguno de "
             "ellos aparecía viviendo conforme a la ley de sus padres, "
             "muriese.",
    (4, 24): "Y como de ningún modo lograba deshacer con sus decretos la "
             "lealtad del pueblo, sino que veía anuladas todas sus amenazas y "
             "castigos",
    (4, 25): "—hasta el punto de que hubo mujeres que, por haber circuncidado "
             "a sus hijos, fueron despeñadas con sus criaturas, sabiendo de "
             "antemano que eso les iba a pasar—,",
    (4, 26): "como sus decretos eran despreciados por el pueblo, él mismo "
             "empezó a obligar con tormentos, uno por uno, a los de aquel "
             "pueblo, a que probasen comidas impuras y abjurasen del "
             "judaísmo.",

    (5, 1): "Así pues, sentándose el tirano Antíoco con su consejo en un lugar "
            "elevado, y estando sus tropas alrededor en armas,",
    (5, 2): "mandaba a sus lanceros que trajesen a rastras a los hebreos uno "
            "por uno y que los obligasen a probar carne de cerdo y lo "
            "sacrificado a los ídolos;",
    (5, 3): "y que a los que no quisiesen comer lo impuro se los matase en el "
            "potro.",
    (5, 4): "Y habiendo apresado a muchos, el primero de aquel grupo, un "
            "hebreo llamado Eleazar, sacerdote de nacimiento, versado en la "
            "ley, entrado en años y conocido de muchos de los del tirano por "
            "su edad, fue llevado a su presencia.",
    (5, 5): "Y viéndolo Antíoco, dijo:",
    (5, 6): "«Yo, antes de empezar los tormentos contra ti, anciano, te "
            "aconsejaría esto: que te salves probando la carne de cerdo; "
            "porque respeto tu edad y tus canas, que, teniéndolas después de "
            "tanto tiempo, no me parece que sean de un filósofo, si sigues la "
            "religión de los judíos.",
    (5, 7): "Porque ¿a qué aborreces la carne de este animal, que la "
            "naturaleza nos ha regalado como la más sabrosa?",
    (5, 8): "Porque es necio no gozar de lo agradable que no acarrea deshonra, "
            "e injusto rechazar los dones de la naturaleza.",
    (5, 9): "Y me parece que harás algo todavía más necio si, por una vana "
            "opinión acerca de la verdad,",
    (5, 10): "encima me desprecias a mí a costa de tu propio castigo. ¿No vas "
             "a despertar de esa charlatana filosofía vuestra,",
    (5, 11): "y a desechar ese razonamiento tuyo lleno de sandeces, y, "
             "recobrando un juicio digno de tu edad, a filosofar sobre la "
             "verdad de lo que conviene,",
    (5, 12): "y, aceptando mi consejo benévolo, a tener lástima de tu propia "
             "vejez?",
    (5, 13): "Porque piensa que, aunque haya alguna potencia vigilante en esa "
             "religión, te perdonará toda transgresión cometida por "
             "necesidad».",
    (5, 14): "Y mientras el tirano lo apremiaba de este modo a comer aquella "
             "carne ilícita, Eleazar pidió la palabra;",
    (5, 15): "y, obtenido el permiso para hablar, comenzó a razonar así ante "
             "todos:",
    (5, 16): "«Nosotros, Antíoco, persuadidos de vivir conforme a una ley "
             "divina, no creemos que haya necesidad más fuerte que la de "
             "obedecer a nuestra ley.",
    (5, 17): "Por eso en modo alguno consideramos lícito transgredirla.",
    (5, 18): "Y aunque, conforme a la verdad, nuestra ley no fuera divina, "
             "como tú supones, y nosotros sólo lo creyéramos, ni aun así nos "
             "sería lícito echar por tierra nuestra fama de piedad.",
    (5, 19): "No creas, pues, que sería un pecado pequeño comer lo impuro;",
    (5, 20): "porque transgredir en lo pequeño y en lo grande tiene la misma "
             "fuerza:",
    (5, 21): "por lo uno y por lo otro se desprecia igualmente la ley.",
    (5, 22): "Te burlas de nuestra filosofía como si no viviéramos en ella con "
             "buen juicio.",
    (5, 23): "Porque nos enseña a fondo la templanza, de modo que dominemos "
             "todos los placeres y deseos, y nos ejercita en el valor, de modo "
             "que soportemos voluntariamente todo dolor;",
    (5, 24): "y nos educa en la justicia, de modo que en todas nuestras "
             "costumbres seamos ecuánimes, y nos enseña la piedad, de modo que "
             "demos culto magníficamente sólo al Dios que es.",
    (5, 25): "Por eso no comemos lo impuro; porque, creyendo que la ley ha "
             "sido puesta por Dios, sabemos que el creador del mundo, al "
             "legislar, tiene consideración de nuestra naturaleza:",
    (5, 26): "lo que iba a convenir a nuestras almas, nos permitió comerlo; y "
             "lo que iba a sernos contrario, nos prohibió comerlo.",
    (5, 27): "Y es propio de un tirano que no sólo nos obligues a transgredir, "
             "sino a comer, para reírte encima de esta comida impura que tanto "
             "aborrecemos.",
    (5, 28): "Pero no te reirás de mí con esa risa;",
    (5, 29): "ni traicionaré los sagrados juramentos de mis antepasados de "
             "guardar la ley,",
    (5, 30): "ni aunque me saques los ojos y me deshagas las entrañas.",
    (5, 31): "No soy tan viejo ni tan cobarde como para que mi razón no sea "
             "joven por la piedad.",
    (5, 32): "Prepara para esto los potros y atiza el fuego con más fuerza.",
    (5, 33): "No tendré tanta lástima de mi vejez como para acabar yo mismo "
             "con la ley de mis padres.",
    (5, 34): "No te faltaré, ley que me educaste; no huiré de ti, querida "
             "templanza;",
    (5, 35): "no te avergonzaré, razón filosófica; no te negaré, sacerdocio "
             "venerable ni ciencia de la ley;",
    (5, 36): "ni mancharás tú la boca venerable de mi vejez, ni la edad de una "
             "vida vivida conforme a la ley.",
    (5, 37): "Puro me recibirán mis padres, por no haber temido tus violencias "
             "hasta la muerte.",
    (5, 38): "Podrás tiranizar a los impíos; pero de mis razonamientos acerca "
             "de la piedad no serás dueño, ni con palabras ni con obras».",

    (6, 1): "Y habiendo replicado de este modo a las exhortaciones del tirano, "
            "los lanceros se acercaron y arrastraron con saña a Eleazar hacia "
            "los instrumentos de tortura.",
    (6, 2): "Y primero desnudaron al anciano, que iba adornado con la decencia "
            "propia de su piedad.",
    (6, 3): "Después, atándole los brazos por los dos lados, lo destrozaban a "
            "latigazos,",
    (6, 4): "mientras un heraldo gritaba desde el otro lado: «¡Obedece las "
            "órdenes del rey!».",
    (6, 5): "Pero Eleazar, magnánimo y verdaderamente noble, torturado como si "
            "fuera en un sueño, no cambiaba de ningún modo.",
    (6, 6): "Sino que, alzando los ojos al cielo, el anciano se dejaba "
            "desgarrar las carnes con los látigos, y chorreaba sangre, y se le "
            "abrían los costados;",
    (6, 7): "y, cayendo al suelo porque el cuerpo no soportaba los dolores, "
            "mantenía la razón derecha y sin doblarse.",
    (6, 8): "Y hasta uno de aquellos crueles lanceros, saltando sobre él, le "
            "daba patadas en los costados para que se levantara al caer.",
    (6, 9): "Pero él aguantaba los dolores y despreciaba la violencia y "
            "resistía los malos tratos;",
    (6, 10): "y, como un atleta noble bajo los golpes, el anciano vencía a los "
             "que lo torturaban.",
    (6, 11): "Y, sudando el rostro y jadeando con fuerza, hasta los mismos "
             "verdugos lo admiraban por su fortaleza.",
    (6, 12): "Por lo cual, unos por compasión de su vejez,",
    (6, 13): "otros por el afecto del trato, y otros por admiración de su "
             "aguante, algunos de los del rey se le acercaron y le decían:",
    (6, 14): "«¿Por qué te pierdes sin razón con estos males, Eleazar?",
    (6, 15): "Nosotros te serviremos carne cocida; y tú, fingiendo que pruebas "
             "la de cerdo, sálvate».",
    (6, 16): "Y Eleazar, como herido más cruelmente por aquel consejo, gritó:",
    (6, 17): "«¡No pensemos tan mal los hijos de Abrahán, como para "
             "representar, con alma blanda, una comedia impropia de nosotros!",
    (6, 18): "Porque sería absurdo que, habiendo vivido hasta la vejez "
             "conforme a la verdad, y guardando conforme a la ley la fama que "
             "de ello nos viene, cambiásemos ahora,",
    (6, 19): "y nos convirtiéramos nosotros mismos en modelo de impiedad para "
             "los jóvenes, sirviéndoles de ejemplo para comer lo impuro.",
    (6, 20): "Porque sería vergonzoso sobrevivir un poco de tiempo, y ese poco "
             "siendo objeto de burla de todos por cobardía;",
    (6, 21): "y que el tirano nos despreciara como a gente sin hombría, y no "
             "defendiéramos hasta la muerte nuestra ley divina.",
    (6, 22): "Por eso vosotros, hijos de Abrahán, morid noblemente por la "
             "piedad.",
    (6, 23): "Y vosotros, lanceros del tirano, ¿a qué esperáis?».",
    (6, 24): "Y viéndolo tan magnánimo ante los tormentos, y sin que "
             "cambiase ni ante la compasión de ellos, lo llevaron al fuego;",
    (6, 25): "y allí, quemándolo con instrumentos de artera invención, lo "
             "arrojaban de un lado a otro y le echaban por las narices "
             "líquidos hediondos.",
    (6, 26): "Y él, quemado ya hasta los huesos y a punto de desfallecer, alzó "
             "los ojos a Dios y dijo:",
    (6, 27): "«Tú sabes, Dios, que, pudiendo salvarme, muero entre tormentos "
             "de fuego por la ley.",
    (6, 28): "Sé propicio a tu pueblo, contentándote con el castigo que "
            "nosotros sufrimos por ellos.",
    (6, 29): "Haz que mi sangre sea su purificación, y toma mi vida en lugar "
             "de la suya».",
    (6, 30): "Y diciendo esto, aquel hombre santo murió noblemente entre los "
             "tormentos, y hasta los tormentos de la muerte resistió con la "
             "razón por causa de la ley.",
    (6, 31): "Queda, pues, reconocido que la razón piadosa es dueña de las "
             "pasiones.",
    (6, 32): "Porque, si las pasiones hubieran dominado a la razón, a ellas "
             "les habría atribuido el testimonio del dominio.",
    (6, 33): "Pero, habiendo vencido la razón a las pasiones, le atribuimos a "
             "ella, como corresponde, la autoridad del mando.",
    (6, 34): "Y es justo que reconozcamos que el poder es de la razón, cuando "
             "domina hasta los dolores que le vienen de fuera;",
    (6, 35, "s"): "pues sería ridículo lo contrario. Y no sólo demuestro que la "
             "razón ha dominado los dolores, sino que domina también los "
             "placeres y no cede ante ellos.",

    (7, 1): "Porque, como un piloto excelente, la razón de nuestro padre "
            "Eleazar llevaba el timón de la nave de la piedad por el mar de "
            "las pasiones;",
    (7, 2): "y, aunque azotado por las amenazas del tirano y anegado por el "
            "oleaje de los tormentos,",
    (7, 3): "en modo alguno torció el gobernalle de la piedad, hasta que "
            "arribó al puerto de la victoria sobre la muerte.",
    (7, 4): "Jamás una ciudad sitiada resistió con tantas y tan variadas "
            "máquinas como aquel hombre santísimo, cuando, abrasada su alma "
            "sagrada con malos tratos y torturas, conmovió a los que lo "
            "asediaban, por la razón que escudaba su piedad.",
    (7, 5): "Porque el padre Eleazar, tendiendo su pensamiento como un "
            "promontorio escarpado, quebró las olas enfurecidas de las "
            "pasiones.",
    (7, 6): "¡Oh sacerdote digno del sacerdocio! No manchaste tus dientes "
            "sagrados, ni hiciste partícipe de comida impura a aquel vientre "
            "que no había tenido sitio más que para la piedad y la pureza.",
    (7, 7): "¡Oh tú, que concordabas con la ley y filosofabas con una vida "
            "divina!",
    (7, 8): "Así han de ser los que ponen la ley en práctica con su propia "
            "sangre y la defienden con un sudor noble en los sufrimientos "
            "hasta la muerte.",
    (7, 9): "Tú, padre, con tu aguante confirmaste para gloria nuestra el buen "
            "orden de la ley, y honraste con tus palabras la santidad sin "
            "traicionarla, y con tus obras diste crédito a las palabras de la "
            "filosofía.",
    (7, 10): "¡Oh anciano más fuerte que los tormentos, viejo más recio que el "
             "fuego, gran rey de las pasiones, Eleazar!",
    (7, 11): "Porque, como el padre Aarón, armado con el incensario, corriendo "
             "entre la muchedumbre del pueblo venció al ángel que traía el "
             "fuego,",
    (7, 12): "así el descendiente de Aarón, Eleazar, derretido por el fuego, "
             "no cambió su razón.",
    (7, 13): "Y lo más admirable: siendo viejo, y aflojadas ya las fuerzas de "
             "su cuerpo, y relajadas las carnes, y cansados los nervios, "
             "rejuveneció",
    (7, 14): "con el espíritu de la razón, y con la razón de un Isaac dejó sin "
             "efecto el potro de muchas cabezas.",
    (7, 15): "¡Oh vejez dichosa, y canas venerables, y vida conforme a la ley, "
             "que el sello fiel de la muerte llevó a su término!",
    (7, 16): "Si, pues, un anciano despreció por piedad los tormentos hasta la "
             "muerte, queda reconocido que la razón piadosa es la que gobierna "
             "las pasiones. Quizá dirían algunos que no todos dominan las "
             "pasiones, porque no todos tienen una razón prudente.",
    (7, 18): "Pero cuantos se ocupan de la piedad de todo corazón, sólo ésos "
             "pueden dominar las pasiones de la carne,",
    (7, 19): "los que creen que no mueren para Dios, como tampoco murieron "
             "nuestros patriarcas Abrahán, Isaac y Jacob, sino que viven para "
             "Dios.",
    (7, 20): "No hay, pues, nada contrario en el hecho de que algunos parezcan "
             "dominados por las pasiones, por tener una razón débil.",
    (7, 21): "Porque ¿quién, filosofando piadosamente conforme a toda la regla "
             "de la filosofía, y habiendo creído en Dios,",
    (7, 22): "y sabiendo que es dichoso soportar todo dolor por la virtud, no "
             "iba a dominar las pasiones por causa de la piedad?",
    (7, 23): "Porque sólo el sabio y templado es valiente y señor de las "
             "pasiones.",
    (7, 24): "Y por eso hasta unos muchachos, filosofando con la razón de la "
             "piedad, vencieron tormentos aún más crueles.",

    (8, 1): "Porque, habiendo sido vencido a la vista de todos el tirano en el "
            "primer intento, al no poder obligar a un anciano a comer lo "
            "impuro,",
    (8, 2): "entonces, lleno de rabia, mandó traer a otros de entre los "
            "hebreos jóvenes: y que, si comían lo impuro, los soltasen después "
            "de comer; y que, si se negaban, los torturasen con más saña.",
    (8, 3): "Dadas estas órdenes por el tirano, fueron traídos siete hermanos "
            "con su anciana madre, hermosos y recatados y nobles y agraciados "
            "en todo.",
    (8, 4): "Y viéndolos el tirano rodeando a su madre en medio como en un "
            "coro, se fijó en ellos y, asombrado de su buen aspecto y de su "
            "nobleza, les sonrió y, llamándolos cerca, dijo:",
    (8, 5): "«Jóvenes, con toda benevolencia admiro la hermosura de cada uno "
            "de vosotros; y teniendo en mucho a tantos hermanos juntos, no "
            "sólo os aconsejo que no cometáis la misma locura que el anciano "
            "que ha sido torturado antes,",
    (8, 6): "sino que os ruego que cedáis y disfrutéis de mi amistad; porque, "
            "así como puedo castigar a los que desobedecen mis órdenes, así "
            "también puedo hacer bien a los que me obedecen.",
    (8, 7): "Fiaos, pues, y recibiréis cargos de mando en mis asuntos, si "
            "renunciáis a la norma de vida de vuestros padres;",
    (8, 8): "y, adoptando el modo de vivir griego y cambiando de costumbres, "
            "gozad de vuestra juventud.",
    (8, 9): "Porque, si me irritáis con vuestra desobediencia, me obligaréis a "
            "destruiros uno por uno con castigos terribles entre tormentos.",
    (8, 10): "Tened, pues, lástima de vosotros mismos, de quienes hasta yo, "
             "que soy vuestro enemigo, me compadezco por vuestra edad y por "
             "vuestra buena figura.",
    (8, 11): "¿No vais a considerar que, si desobedecéis, no os espera otra "
             "cosa que morir entre torturas?».",
    (8, 12): "Y diciendo esto, mandó que pusieran delante los instrumentos de "
             "tortura, para convencerlos también por el miedo a comer lo "
             "impuro.",
    (8, 13): "Y cuando los lanceros pusieron delante los potros y los "
             "desmembradores y los aparatos de tortura y los tornos y las "
             "catapultas y las calderas y las sartenes y las tenazas para los "
             "dedos y las garfios de hierro y las cuñas y los fuelles del "
             "fuego, el tirano tomó la palabra y dijo:",
    (8, 14): "«Muchachos, temed; y la justicia a la que veneráis os será "
             "propicia por haber transgredido por necesidad».",
    (8, 15): "Pero ellos, al oír aquellas palabras seductoras y ver aquellas "
             "cosas terribles, no sólo no tuvieron miedo, sino que replicaron "
             "al tirano con filosofía, y con su buen razonamiento acabaron con "
             "su tiranía.",
    (8, 16): "Y pensemos: si hubiera habido entre ellos algunos cobardes y sin "
             "hombría, ¿qué palabras habrían empleado? ¿No serían éstas?",
    (8, 17): "«¡Ay de nosotros, desdichados y muy necios! Estando el rey "
             "llamándonos y convocándonos para hacernos bien, ¿no vamos a "
             "obedecerle?",
    (8, 18): "¿Por qué nos hacemos ilusiones con propósitos vacíos y nos "
             "atrevemos a una desobediencia que trae la muerte?",
    (8, 19): "¿No vamos a temer, hermanos, los instrumentos de tortura, y a "
             "considerar las amenazas de los tormentos, y a huir de esta "
             "vanagloria y de esta jactancia que acarrea la ruina?",
    (8, 20): "Tengamos lástima de nuestra edad y compadezcámonos de la vejez "
             "de nuestra madre;",
    (8, 21): "y pensemos que, si desobedecemos, moriremos.",
    (8, 22): "Y la justicia divina nos perdonará por haber temido al rey por "
             "necesidad.",
    (8, 23): "¿Por qué nos sacamos a nosotros mismos de esta vida tan dulce y "
             "nos privamos de este mundo tan grato?",
    (8, 24): "No forcemos la necesidad, ni busquemos vanagloria en nuestro "
             "propio suplicio.",
    (8, 25): "Ni la ley misma nos condena a muerte de buen grado por haber "
             "temido los instrumentos de tortura.",
    (8, 26): "¿De dónde se nos ha metido dentro tanta porfía, y por qué nos "
             "gusta esta terquedad que trae la muerte, pudiendo vivir "
             "tranquilos si obedecemos al rey?».",
    (8, 27): "Pero nada de esto pensaron ni se les ocurrió a aquellos jóvenes "
             "cuando iban a ser torturados,",
    (8, 28): "porque despreciaban las pasiones y eran dueños de los dolores;",
    (8, 29): "de modo que, en cuanto el tirano acabó de aconsejarles que "
             "comieran lo impuro, todos a una voz, como de una sola alma, "
             "dijeron:",

    (9, 1): "«¿A qué esperas, tirano? Porque estamos dispuestos a morir antes "
            "que a traspasar los mandamientos de nuestros padres.",
    (9, 2): "Porque con razón nos avergonzaríamos de nuestros antepasados si "
            "no tomásemos por consejera y por norma la obediencia a la ley.",
    (9, 3): "Tirano consejero de transgresiones: no nos tengas lástima más que "
            "nosotros mismos, tú que nos odias.",
    (9, 4): "Porque tenemos por más duro que la misma muerte tu compasión, si "
            "es a costa de salvarnos transgrediendo la ley.",
    (9, 5): "Nos intentas aterrar amenazándonos con la muerte entre tormentos, "
            "como si no hubieras aprendido nada hace un momento de Eleazar.",
    (9, 6): "Y si los ancianos de los hebreos murieron por la piedad después "
            "de soportar los tormentos, con más razón moriremos nosotros, los "
            "jóvenes, despreciando los tormentos de tus violencias, que hasta "
            "un anciano maestro venció.",
    (9, 7): "Prueba, pues, tirano; y si haces morir nuestras almas por la "
            "piedad, no creas que nos haces daño torturándonos.",
    (9, 8): "Porque nosotros, por este sufrimiento y por este aguante, "
            "recibiremos los premios de la virtud;",
    (9, 9): "pero tú, por nuestro asesinato impío, sufrirás de la justicia "
            "divina un tormento eterno por el fuego, como te mereces».",
    (9, 10): "Y al decir ellos esto, el tirano no sólo se irritó contra ellos "
             "como contra unos desobedientes, sino que se enfureció como "
             "contra unos desagradecidos.",
    (9, 11): "Por lo cual, a una orden suya, los verdugos trajeron al mayor de "
             "ellos y, rasgándole la túnica, le ataron las manos y los brazos "
             "con correas por los dos lados.",
    (9, 12): "Y cuando se cansaron de azotarlo con los látigos sin conseguir "
             "nada, lo echaron sobre el potro.",
    (9, 13): "Y, estirado en él, aquel joven noble se iba descoyuntando;",
    (9, 14): "y, roto miembro por miembro, los acusaba diciendo:",
    (9, 15): "«Tirano asquerosísimo, enemigo de la justicia del cielo, de "
             "corazón cruel: no me destrozas de este modo por haber matado a "
             "nadie ni por haber sido impío, sino por defender la ley divina».",
    (9, 16): "Y como los lanceros le decían: «Consiente en comer, para que te "
             "libres de los tormentos»,",
    (9, 17): "él respondió: «No es tan fuerte, servidores repugnantes, vuestro "
             "procedimiento como para arrastrar mi razón. Cortadme los "
             "miembros y quemadme las carnes y descoyuntadme las "
             "articulaciones;",
    (9, 18): "porque por todos vuestros tormentos os convenceré de que sólo "
             "los hijos de los hebreos son invencibles por la virtud».",
    (9, 19): "Mientras decía esto, le echaron encima fuego y, atizando el "
             "potro, lo estiraban todavía más.",
    (9, 20): "Y el potro se manchaba de sangre por todas partes, y el montón "
             "de brasas se apagaba con el goteo de la sangre, y las carnes se "
             "iban desprendiendo en torno a los ejes de la máquina.",
    (9, 21): "Y, teniendo ya deshecha la armazón de sus huesos, aquel joven "
             "magnánimo y digno de Abrahán no gimió,",
    (9, 22): "sino que, como transfigurándose en el fuego hacia la "
             "incorrupción, soportó noblemente las torturas, diciendo:",
    (9, 23): "«Imitadme, hermanos; no desertéis de mi puesto en la eternidad, "
             "ni reneguéis de la hermandad de mi valor. Combatid el sagrado y "
             "noble combate por la piedad,",
    (9, 24): "por el que nuestra providencia justa y paterna, hecha propicia a "
             "nuestro pueblo, castigue a este tirano maldito».",
    (9, 25): "Y diciendo esto, aquel joven digno de un sacerdote exhaló el "
             "alma.",
    (9, 26): "Y admirándose todos de su fortaleza, los lanceros trajeron al "
             "segundo en edad después del primero, y, ajustándose garfios de "
             "hierro con uñas afiladas, lo ataron a los instrumentos y a la "
             "catapulta.",
    (9, 27): "Y cuando le preguntaron si quería comer antes de ser torturado, "
             "y oyeron su noble respuesta,",
    (9, 28): "aquellas fieras de leopardo lo agarraron por los tendones con "
             "los garfios de hierro y le arrancaron toda la carne hasta la "
             "barbilla y la piel de la cabeza; y él, soportando aquel dolor "
             "atroz, decía:",
    (9, 29): "«¡Qué dulce es cualquier clase de muerte por la piedad de "
             "nuestros padres!». Y dijo al tirano:",
    (9, 30): "«¿No te parece, tirano el más cruel de todos, que ahora eres tú "
             "el más torturado que yo, al ver vencida la razón soberbia de tu "
             "tiranía por nuestro aguante en la piedad?",
    (9, 31): "Porque yo alivio mi dolor con los gozos que da la virtud;",
    (9, 32): "pero tú estás torturado por las amenazas de tu impiedad. Y no "
             "escaparás, tirano asquerosísimo, de los castigos de la ira "
             "divina».",

    (10, 1): "Y habiendo soportado éste una muerte memorable, trajeron al "
             "tercero, al que muchos exhortaban a que se salvase probando "
             "aquella comida.",
    (10, 2): "Pero él gritó y dijo: «¿Es que no sabéis que el mismo padre me "
             "engendró a mí que a los que han muerto, y la misma madre me dio "
             "a luz, y en las mismas creencias fui criado?",
    (10, 3): "No reniego del noble parentesco de esta hermandad.",
    (10, 4): "Ante esto, si tenéis algún instrumento de castigo, aplicadlo a "
             "mi cuerpo; porque mi alma, aunque queráis, no la tocaréis».",
    (10, 5): "Y ellos, llevando a mal la franqueza de aquel hombre, le "
             "descoyuntaron con los desmembradores las manos y los pies, y, "
             "haciendo palanca en las junturas, se los desencajaron;",
    (10, 6): "y le fueron arrancando los dedos y los brazos y las piernas y "
             "los codos.",
    (10, 7): "Y no pudiendo de ningún modo doblegarlo, le arrancaron la piel "
             "junto con las puntas de los dedos, y lo desollaron a la manera "
             "de los escitas, y en seguida lo llevaron al potro,",
    (10, 8): "donde, desencajándosele las vértebras, veía sus propias carnes "
             "hechas jirones y las gotas de sangre que le corrían de las "
             "entrañas.",
    (10, 9): "Y a punto de morir, dijo:",
    (10, 10): "«Nosotros, tirano asquerosísimo, padecemos esto por la "
              "instrucción y la virtud de Dios;",
    (10, 11): "pero tú, por tu impiedad y por tus asesinatos, soportarás "
              "tormentos que no se acaban».",
    (10, 12): "Y habiendo muerto éste como correspondía a sus hermanos, "
              "trajeron al cuarto, diciéndole:",
    (10, 13): "«No te vuelvas loco tú también con la misma locura que tus "
              "hermanos, sino obedece al rey y sálvate».",
    (10, 14): "Pero él les dijo: «No tenéis contra mí un fuego tan ardiente "
              "como para hacerme perder la hombría.",
    (10, 15): "Por la muerte dichosa de mis hermanos, y por la ruina eterna "
              "del tirano, y por la vida memorable de los piadosos, no negaré "
              "la noble hermandad.",
    (10, 16): "Inventa tormentos, tirano, para que también por ellos aprendas "
              "que soy hermano de los que has torturado antes».",
    (10, 17): "Al oír esto, aquel Antíoco sediento de sangre y asesino y del "
              "todo repugnante mandó que le cortasen la lengua.",
    (10, 18): "Pero él dijo: «Aunque me quites el órgano de la voz, Dios oye "
              "también a los que callan.",
    (10, 19): "Mira, ya tengo la lengua fuera: córtala; porque no por eso vas "
              "a cortar nuestra razón.",
    (10, 20): "De buena gana nos dejamos mutilar los miembros del cuerpo por "
              "Dios.",
    (10, 21): "Pero a ti te alcanzará Dios pronto, porque estás cortando una "
              "lengua que cantaba los himnos divinos».",

    (11, 1): "Y cuando también éste murió destrozado por los tormentos, se "
             "adelantó de un salto el quinto, diciendo:",
    (11, 2): "«No pienso, tirano, rehuir el tormento por la virtud;",
    (11, 3): "he venido yo mismo por mi propio pie, para que, matándome "
             "también a mí, debas a la justicia del cielo el castigo de más "
             "crímenes.",
    (11, 4): "¡Oh tú, que odias la virtud y odias a los hombres! ¿Qué hemos "
             "hecho para que nos destroces de este modo?",
    (11, 5): "¿Te parece mal que demos culto al creador de todas las cosas y "
             "que vivamos conforme a su ley virtuosa?",
    (11, 6): "Pero eso merece honores, no tormentos,",
    (11, 7): "si es que tuvieras sentimientos humanos y esperanza de salvación "
             "en Dios.",
    (11, 8): "Pero ahora, mira: como eres ajeno a Dios, haces la guerra a los "
             "que son piadosos con Dios».",
    (11, 9): "Mientras decía estas cosas, los lanceros lo ataron y lo "
             "arrastraron a la catapulta;",
    (11, 10): "y, atándolo a ella por las rodillas, y sujetándoselas con "
              "grilletes de hierro, le doblaron la espalda sobre la cuña de la "
              "rueda, y, doblado del todo hacia atrás sobre el potro a la "
              "manera de un escorpión, se le descoyuntaban los miembros.",
    (11, 11): "Y de este modo, con el aliento oprimido y el cuerpo "
              "estrangulado,",
    (11, 12): "decía: «Buenos favores nos haces sin querer, tirano; buenos, "
              "porque nos das ocasión de mostrar con dolores más nobles "
              "nuestra firmeza en la ley».",
    (11, 13): "Y muerto también éste, trajeron al sexto, un muchacho, al que "
              "el tirano preguntó si quería comer y quedar libre; y él dijo:",
    (11, 14): "«Yo soy más joven que mis hermanos en la edad, pero de su misma "
              "edad en el pensamiento;",
    (11, 15): "porque, habiendo nacido y sido criados para lo mismo, también "
              "debemos morir igualmente por lo mismo.",
    (11, 16): "Así que, si te parece bien torturar a los que no comen lo "
              "impuro, tortúrame».",
    (11, 17): "Y al decir esto, lo llevaron al potro,",
    (11, 18): "sobre el cual, estirado miembro a miembro y desencajadas las "
              "vértebras, lo quemaban por debajo.",
    (11, 19): "Y poniendo al rojo unos asadores agudos, se los aplicaban a la "
              "espalda; y, atravesándole los costados, le quemaban las "
              "entrañas.",
    (11, 20): "Y él, mientras lo torturaban, decía: «¡Oh combate digno de un "
              "sacerdote, para el que, por la piedad, hemos sido llamados "
              "tantos hermanos a la palestra de los dolores, y no hemos sido "
              "vencidos!",
    (11, 21): "Porque es invencible, tirano, la ciencia de la piedad.",
    (11, 22): "Armado de nobleza moriré también yo con mis hermanos,",
    (11, 23): "sumando yo mismo contra ti un gran vengador, inventor de "
              "tormentos y enemigo de los que son de verdad piadosos.",
    (11, 24): "Seis muchachos hemos acabado con tu tiranía.",
    (11, 25): "Porque el que no hayas podido hacernos cambiar de parecer ni "
              "forzarnos a comer lo impuro, ¿no es tu derrota?",
    (11, 26): "Tu fuego nos resulta frío, y no duelen tus catapultas, y tu "
              "violencia es impotente.",
    (11, 27): "Porque nuestros guardias no son los de un tirano, sino los de "
              "la ley divina; por eso tenemos invencible la razón».",

    (12, 1): "Y cuando también éste murió dichosamente, arrojado a una "
             "caldera, se presentó el séptimo, el más joven de todos.",
    (12, 2): "Y el tirano se compadeció de él, aunque había sido terriblemente "
             "insultado por sus hermanos;",
    (12, 3): "y, viéndolo ya con las ataduras puestas, lo mandó traer más "
             "cerca e intentaba persuadirlo diciendo:",
    (12, 4): "«Ya ves el final de la insensatez de tus hermanos: por su "
             "desobediencia han muerto entre torturas. Tú, si no te dejas "
             "convencer, morirás también, desdichado, torturado antes de "
             "tiempo;",
    (12, 5): "pero, si obedeces, serás mi amigo y estarás al frente de los "
             "asuntos del reino».",
    (12, 6): "Y con estas exhortaciones mandó traer a la madre del muchacho, "
             "para que, compadeciéndose de ella por haber perdido a tantos "
             "hijos, la moviese a persuadir al que quedaba de que se salvase.",
    (12, 7): "Pero él, después de que su madre lo exhortó en lengua hebrea "
             "—como diremos un poco más adelante—,",
    (12, 8): "dijo: «Soltadme; quiero hablar al rey y a todos los amigos que "
             "están con él».",
    (12, 9): "Y, alegrándose mucho por la promesa del muchacho, lo soltaron "
             "en seguida.",
    (12, 10): "Y él, corriendo hasta cerca de las sartenes, dijo:",
    (12, 11): "«Tirano impío y el más sacrílego de todos los malvados: ¿no te "
              "dio vergüenza, habiendo recibido de Dios los bienes y el reino, "
              "matar a sus servidores y torturar a los que se ejercitan en la "
              "piedad?",
    (12, 12): "Por eso la justicia divina te reserva un fuego más espeso y "
              "eterno, y tormentos que no te soltarán por toda la eternidad.",
    (12, 13): "¿No te dio vergüenza, siendo hombre, bestia ferocísima, cortar "
              "la lengua a los que sienten como tú y están hechos de los "
              "mismos elementos, y destrozarlos y torturarlos de este modo?",
    (12, 14): "Pero ellos, muriendo noblemente, han cumplido su piedad para "
              "con Dios;",
    (12, 15): "y tú gemirás amargamente por haber matado sin causa a los "
              "campeones de la virtud».",
    (12, 16): "Por lo cual, cuando él mismo iba a morir, dijo:",
    (12, 17): "«No deserto del testimonio de mis hermanos.",
    (12, 18): "E invoco al Dios de mis padres para que sea propicio a mi "
              "pueblo;",
    (12, 19): "y a ti te castigará en esta vida y después de muerto».",
    (12, 20): "Y después de hacer esta súplica, se arrojó a las sartenes; y "
              "así entregó el alma.",

    (13, 1): "Si, pues, los siete hermanos despreciaron los dolores hasta la "
             "muerte, queda reconocido por todas partes que la razón piadosa "
             "es dueña absoluta de las pasiones.",
    (13, 2): "Porque, si esclavizados por las pasiones hubieran comido lo "
             "impuro, diríamos que habían sido vencidos por ellas;",
    (13, 3): "pero no fue así, sino que con esa razón alabada ante Dios "
             "vencieron a las pasiones.",
    (13, 4): "Y no se puede pasar por alto el mando del pensamiento, porque "
             "dominó tanto la pasión como el dolor.",
    (13, 5): "¿Cómo, pues, no se ha de reconocer en éstos el dominio del buen "
             "razonamiento sobre las pasiones, si no se volvieron atrás ante "
             "los dolores del fuego?",
    (13, 6): "Porque, como las torres que se adelantan a la entrada de los "
             "puertos rompen las embestidas de las olas y ofrecen a los que "
             "entran un fondeadero en calma,",
    (13, 7): "así el buen razonamiento de aquellos jóvenes, con sus siete "
             "torres, fortificó el puerto de la piedad y venció el desenfreno "
             "de las pasiones.",
    (13, 8): "Porque, formando un coro sagrado de piedad, se animaban unos a "
             "otros diciendo:",
    (13, 9): "«Muramos como hermanos, hermanos, por la ley; imitemos a los "
             "tres jóvenes de Siria, que despreciaron un horno tan poderoso "
             "como esto.",
    (13, 10): "No perdamos la hombría ante la prueba de la piedad».",
    (13, 11): "Y uno decía: «Ánimo, hermano»; y otro: «Aguanta noblemente»;",
    (13, 12): "y otro decía: «Acordaos de dónde venís, y de por mano de qué "
              "padre soportó Isaac dejarse degollar por la piedad».",
    (13, 13): "Y cada uno, y todos a la vez mirándose unos a otros, alegres y "
              "llenos de valor, decían: «Consagrémonos a Dios de todo corazón, "
              "al que nos dio las almas, y empleemos los cuerpos en guardar la "
              "ley.",
    (13, 14): "No temamos al que cree que mata;",
    (13, 15): "porque grande es el combate del alma y grande el peligro de "
              "tormento eterno reservado a los que traspasan el mandamiento de "
              "Dios.",
    (13, 16): "Armémonos, pues, con el dominio de las pasiones que da la razón "
              "divina.",
    (13, 17): "Si padecemos así, Abrahán e Isaac y Jacob nos recibirán, y "
              "todos los padres nos alabarán».",
    (13, 18): "Y a cada uno de los hermanos que se llevaban a rastras, los que "
              "quedaban le decían: «No nos avergüences, hermano, ni faltes a "
              "los que han muerto antes».",
    (13, 19): "Y no ignoráis los lazos del cariño humano, que la providencia "
              "divina y sapientísima repartió a los que nacen por medio de los "
              "padres, y plantó en el vientre de la madre,",
    (13, 20): "en el que los hermanos habitaron el mismo tiempo, y fueron "
              "formados en el mismo tiempo, y crecieron con la misma sangre, y "
              "llegaron a término por la misma vida,",
    (13, 21): "y nacieron al cabo de los mismos meses, y mamaron de las mismas "
              "fuentes, de las que se crían, entre abrazos, unas almas que se "
              "quieren como hermanos;",
    (13, 22): "y ese cariño se hace más fuerte por criarse juntos y por el "
              "trato de cada día y por la demás educación, y, en nuestro caso, "
              "por el ejercicio en la ley de Dios.",
    (13, 23): "Siendo, pues, así de fuerte el cariño fraterno, los siete "
              "hermanos tuvieron entre sí una concordia todavía más "
              "entrañable;",
    (13, 24): "porque, educados en la misma ley, y ejercitados en las mismas "
              "virtudes, y criados juntos en una vida justa, se querían "
              "todavía más.",
    (13, 25): "Porque compartir el mismo celo por la nobleza acrecentaba su "
              "concordia mutua;",
    (13, 26): "porque, junto con la piedad, les hacía más deseable el cariño "
              "fraterno.",
    (13, 27): "Y sin embargo, aunque la naturaleza y la convivencia y las "
              "costumbres de la virtud acrecentaban entre ellos los lazos de "
              "la hermandad, los que quedaban soportaron, por la piedad, ver a "
              "sus hermanos destrozados y torturados hasta la muerte,",

    (14, 1): "y aún más: animándolos al suplicio, de modo que no sólo "
             "despreciaron los dolores, sino que dominaron las pasiones del "
             "cariño fraterno.",
    (14, 2): "¡Oh razones más regias que las de un rey, y más libres que las "
             "de los libres!",
    (14, 3): "¡Oh sagrada y bien concertada armonía de los siete hermanos "
             "acerca de la piedad!",
    (14, 4): "Ninguno de aquellos siete muchachos se acobardó ni retrocedió "
             "ante la muerte,",
    (14, 5): "sino que todos, como corriendo por el camino de la inmortalidad, "
             "se apresuraban a la muerte por los tormentos.",
    (14, 6): "Porque, como las manos y los pies se mueven al unísono según las "
             "órdenes del alma, así aquellos santos muchachos, como movidos "
             "por el alma inmortal de la piedad, concordaron en morir por "
             "ella.",
    (14, 7): "¡Oh semana santísima de hermanos concordes! Porque, como los "
             "siete días de la creación del mundo giran en torno a la "
             "piedad,",
    (14, 8): "así aquellos muchachos, danzando en torno a la semana, formaban "
             "corro deshaciendo el miedo a los tormentos.",
    (14, 9): "Ahora nosotros, al oír la aflicción de aquellos jóvenes, nos "
             "estremecemos; y ellos, no sólo viéndola, ni sólo oyendo la "
             "palabra de la amenaza en el momento, sino padeciéndola, "
             "aguantaron, y encima con dolores de fuego.",
    (14, 10): "Y ¿qué puede haber más doloroso? Porque la fuerza del fuego, "
              "aguda y rápida como es, deshacía pronto los cuerpos.",
    (14, 11): "Y no tengáis por asombroso que la razón dominara a aquellos "
              "hombres en los tormentos, cuando hasta el entendimiento de una "
              "mujer despreció dolores más variados.",
    (14, 12): "Porque la madre de aquellos siete jóvenes soportó los suplicios "
              "de cada uno de sus hijos.",
    (14, 13): "Y ved cuán enredado es el cariño de una madre por sus hijos, "
              "que lo arrastra todo hacia la compasión de las entrañas;",
    (14, 14): "cuando hasta los animales irracionales tienen hacia lo que "
              "engendran una compasión y un cariño parecidos a los de los "
              "hombres.",
    (14, 15): "Porque, entre las aves, las domésticas, que andan por los "
              "tejados de las casas, defienden a sus crías;",
    (14, 16): "y las que anidan en las cumbres de los montes y en las quiebras "
              "de los barrancos y en los huecos de los árboles y en sus copas, "
              "allí ponen sus huevos y estorban al que se acerca;",
    (14, 17): "y si no pueden estorbarlo, revolotean alrededor de ellos "
              "doliéndose de cariño, llamándolos con su propia voz, y ayudan a "
              "sus crías como pueden.",
    (14, 18): "¿Y qué falta hace demostrar por los animales irracionales la "
              "compasión hacia los hijos,",
    (14, 19): "cuando hasta las abejas, por el tiempo en que hacen los "
              "panales, se defienden de los que se acercan, y como con un "
              "hierro pican con el aguijón a los que se acercan a su colmena, "
              "y se defienden hasta la muerte?",
    (14, 20): "Pues a la madre de aquellos jóvenes, que tenía el alma de "
              "Abrahán, no la hizo cambiar la compasión por sus hijos.",

    (15, 1): "¡Oh razón, tirana de las pasiones por los hijos! ¡Oh piedad, más "
             "deseable para una madre que sus hijos! Puestas delante de la "
             "madre dos cosas —la piedad y la salvación pasajera de sus siete "
             "hijos conforme a la promesa del tirano—,",
    (15, 3): "amó más la piedad, la que salva para la vida eterna según "
             "Dios.",
    (15, 4): "¿De qué modo podría describir los sentimientos de los padres "
             "hacia sus hijos, esa semejanza de alma y de figura que queda "
             "sellada de un modo admirable en el pequeño carácter del niño, y "
             "sobre todo porque las madres son más compasivas que los padres "
             "con los que han engendrado?",
    (15, 5): "Porque cuanto más débiles de ánimo y más fecundas son las "
             "madres, tanto más quieren a sus hijos.",
    (15, 6): "Y de todas las madres, la de aquellos siete fue la que más quiso "
             "a sus hijos, ella que con siete embarazos había arraigado en "
             "ellos su cariño;",
    (15, 7): "y que, por los muchos dolores de parto de cada uno de ellos, "
             "estaba obligada a sentir compasión por ellos;",
    (15, 8): "pero por el temor de Dios despreció la salvación pasajera de sus "
             "hijos.",
    (15, 9): "Y no sólo eso, sino que por la nobleza de sus hijos y por su "
             "obediencia a la ley, todavía tenía en ellos mayor cariño;",
    (15, 10): "porque eran justos y templados y valientes y magnánimos y "
              "amantes de sus hermanos, y tan amantes de su madre que, "
              "guardando las leyes hasta la muerte, le obedecían.",
    (15, 11): "Pero, con todo, aunque eran tantas las cosas que arrastraban a "
              "la madre a la compasión por sus hijos, en ninguno de ellos "
              "lograron las torturas más variadas hacer cambiar su razón;",
    (15, 12): "sino que, hijo por hijo y a todos a la vez, la madre los "
              "animaba a morir por la piedad.",
    (15, 13): "¡Oh naturaleza sagrada, y lazos de los padres, y cariño hacia "
              "los padres, y crianza, y pasiones indomables de las madres!",
    (15, 14): "Viendo la madre a cada uno torturado y quemado, no cambió, por "
              "la piedad.",
    (15, 15): "Veía las carnes de sus hijos derretirse en el fuego, y los "
              "dedos de los pies y de las manos temblando por el suelo, y las "
              "carnes de las cabezas arrancadas hasta la barbilla, tendidas "
              "como máscaras.",
    (15, 16): "¡Oh madre, que probaste entonces dolores más amargos que los "
              "de dar a luz a aquéllos!",
    (15, 17): "¡Oh única mujer que dio a luz la piedad entera!",
    (15, 18): "No te hizo cambiar el primogénito al expirar, ni el segundo al "
              "mirarte lastimeramente entre los tormentos, ni el tercero al "
              "morir.",
    (15, 19): "Ni al ver los ojos de cada uno, que miraban con fiereza en los "
              "tormentos el mismo suplicio, y las narices que anunciaban ya su "
              "muerte, lloraste.",
    (15, 20): "Viendo sobre las carnes de unos hijos las carnes cortadas de "
              "otros, y sobre unas manos otras manos amputadas, y sobre unas "
              "cabezas otras cabezas degolladas, y sobre unos muertos otros "
              "muertos que caían, y viendo aquel lugar convertido por los "
              "tormentos en cementerio de tus hijos, no derramaste una "
              "lágrima.",
    (15, 21): "Ni las melodías de las sirenas ni los cantos de los cisnes "
              "atraen así los oídos de los que escuchan, como aquellas voces "
              "de hijos que, entre tormentos, llamaban a su madre.",
    (15, 22): "¡Con qué grandes y con cuántos tormentos era entonces torturada "
              "la madre, mientras sus hijos lo eran con potros y con hierros "
              "al rojo!",
    (15, 23): "Pero la razón piadosa, dando valor a sus entrañas en medio de "
              "aquellas pasiones, le dio fuerza para despreciar el amor "
              "pasajero a sus hijos.",
    (15, 24): "Y aunque veía la destrucción de siete hijos y la enredada "
              "variedad de las torturas, aquella madre valerosa lo dejó todo "
              "atrás por su fe en Dios.",
    (15, 25): "Porque, como en una sala de consejo, viendo en su propia alma a "
              "unos consejeros terribles —la naturaleza y el parentesco y el "
              "amor a los hijos y el suplicio de los hijos—,",
    (15, 26): "teniendo en la mano dos votos, el de la muerte y el de la "
              "salvación de sus hijos,",
    (15, 27): "no escogió la salvación que iba a conservar a siete hijos por "
              "poco tiempo,",
    (15, 28): "sino que, como hija de Abrahán, se acordó de su firmeza "
              "piadosa.",
    (15, 29): "¡Oh madre de un pueblo, vengadora de la ley, y escudo de la "
              "piedad, y vencedora en el combate de las entrañas!",
    (15, 30): "¡Oh más noble que los varones en la firmeza, y más valiente que "
              "los hombres en el aguante!",
    (15, 31): "Porque, como el arca de Noé, que llevaba al mundo entero en el "
              "diluvio que cubrió el mundo, soportó las olas violentas,",
    (15, 32): "así tú, guardiana de la ley, anegada por todas partes en el "
              "diluvio de las pasiones y azotada por los vientos violentos de "
              "los tormentos de tus hijos, aguantaste noblemente las "
              "tempestades de la piedad.",

    (16, 1): "Si, pues, una mujer, y anciana, y madre de siete hijos, soportó "
             "ver a sus hijos torturados hasta la muerte, queda reconocido que "
             "la razón piadosa es soberana de las pasiones.",
    (16, 2): "He demostrado, pues, que no sólo unos hombres dominaron las "
             "pasiones, sino que hasta una mujer despreció los mayores "
             "tormentos.",
    (16, 3): "Y no eran tan feroces los leones que rodeaban a Daniel, ni el "
             "horno encendido con fuego violentísimo para Misael, como "
             "abrasaba a aquélla la naturaleza del amor a los hijos, viendo "
             "torturados a sus siete hijos.",
    (16, 4): "Pero con la razón de la piedad apagó la madre unas pasiones tan "
             "numerosas y tan grandes.",
    (16, 5): "Y hay que considerar esto: que si aquella mujer hubiera sido "
             "cobarde de ánimo, siendo como era madre, habría gemido por "
             "ellos, y quizá habría hablado así:",
    (16, 6): "«¡Ay de mí, desdichada y muchas veces tres veces desgraciada, "
             "que, habiendo dado a luz siete hijos, no he llegado a ser madre "
             "de ninguno!",
    (16, 7): "¡Oh siete embarazos inútiles, y siete gestaciones de diez meses "
             "sin provecho, y crianzas estériles, y lactancias miserables!",
    (16, 8): "En vano soporté por vosotros, hijos, muchos dolores de parto y "
             "los desvelos más duros de la crianza.",
    (16, 9): "¡Ay de mis hijos, unos sin casar, y los casados sin provecho! No "
             "veré a vuestros hijos, ni seré llamada abuela ni tenida por "
             "dichosa.",
    (16, 10): "¡Ay de mí, que tuve muchos hijos y hermosos, y soy ahora mujer "
              "viuda y sola y llena de llanto!",
    (16, 11): "Y cuando muera, no tendré a ninguno de mis hijos para "
              "enterrarme». Pero con ese lamento la madre santa y piadosa no "
              "lloró por ninguno,",
    (16, 12): "ni apartó a ninguno de ellos para que no muriera, ni se "
              "entristeció porque morían;",
    (16, 13): "sino que, como si tuviera un entendimiento de acero, y como si "
              "diera a luz de nuevo a sus hijos para la inmortalidad, más bien "
              "los animaba y les suplicaba que fueran a la muerte por la "
              "piedad.",
    (16, 14): "¡Oh madre, soldado de Dios por la piedad! Anciana y mujer, "
              "venciste con tu firmeza hasta a un tirano, y en obras y en "
              "palabras resultaste más fuerte que un hombre.",
    (16, 15): "Porque, cuando fuiste apresada con tus hijos, estabas en pie "
              "viendo torturar a Eleazar, y decías a tus hijos en lengua "
              "hebrea:",
    (16, 16): "«Hijos, noble es el combate al que habéis sido llamados para "
              "dar testimonio por nuestro pueblo: luchad con ánimo por la ley "
              "de nuestros padres.",
    (16, 17): "Porque sería vergonzoso que este anciano soportase los dolores "
              "por la piedad, y que vosotros, los jóvenes, os asustaseis de "
              "los tormentos.",
    (16, 18): "Acordaos de que por Dios habéis tenido parte en el mundo y "
              "habéis gozado de la vida;",
    (16, 19): "y por eso debéis soportar todo dolor por Dios.",
    (16, 20): "Por él también nuestro padre Abrahán se apresuró a inmolar a "
              "Isaac, el padre de nuestro pueblo; y, viendo caer sobre él la "
              "mano paterna con el cuchillo, no se acobardó.",
    (16, 21): "Y Daniel el justo fue arrojado a los leones; y Ananías y "
              "Azarías y Misael fueron lanzados a un horno de fuego, y "
              "aguantaron por Dios.",
    (16, 22): "Y vosotros, pues, teniendo la misma fe en Dios, no os "
              "irritéis;",
    (16, 23): "porque sería absurdo que, conociendo la piedad, no hicierais "
              "frente a los dolores».",
    (16, 24): "Con estas palabras, la madre de siete, exhortando a cada uno de "
              "sus hijos, los persuadió a morir antes que a traspasar el "
              "mandamiento de Dios;",
    (16, 25): "y además sabiendo esto: que los que mueren por Dios viven para "
              "Dios, como Abrahán e Isaac y Jacob y todos los patriarcas.",

    (17, 1): "Y decían algunos de los lanceros que, cuando también ella iba a "
             "ser prendida para morir, se arrojó a la pira para que nadie "
             "tocase su cuerpo.",
    (17, 2): "¡Oh madre que con siete hijos acabaste con la violencia del "
             "tirano y dejaste sin efecto sus malos designios, y mostraste la "
             "nobleza de la fe!",
    (17, 3): "Porque, como un techo noblemente asentado sobre la columna de "
             "tus hijos, soportaste sin doblarte el terremoto de los "
             "tormentos.",
    (17, 4): "Ten ánimo, pues, madre de alma santa, que tienes noblemente en "
             "Dios la esperanza de tu aguante.",
    (17, 5): "No está la luna en el cielo con las estrellas tan augusta como "
             "tú, que, alumbrando hacia la piedad a siete hijos iguales a "
             "estrellas, quedaste honrada ante Dios y fijada con ellos en el "
             "cielo.",
    (17, 6): "Porque tu descendencia venía de Abrahán, el siervo de Dios.",
    (17, 7): "Y si nos fuera posible pintar, como en un cuadro, la piedad de "
             "tu historia, ¿no se estremecerían los que vieran a una madre de "
             "siete hijos soportando por la piedad tormentos variados hasta la "
             "muerte?",
    (17, 8): "Porque sería justo grabar también en su epitafio, para memoria "
             "de los de nuestro pueblo, estas palabras:",
    (17, 9): "«Aquí están enterrados un sacerdote anciano y una mujer anciana "
             "y siete hijos, por la violencia de un tirano que quería acabar "
             "con el régimen de los hebreos.",
    (17, 10): "Ellos vengaron a su pueblo, mirando a Dios y soportando los "
              "tormentos hasta la muerte».",
    (17, 11): "Porque verdaderamente fue un combate divino el que se libró por "
              "medio de ellos.",
    (17, 12): "Porque entonces la virtud presidía los juegos, probando por el "
              "aguante; y el premio era la incorrupción en una vida sin fin.",
    (17, 13): "Eleazar fue el primero en el combate; y la madre de los siete "
              "hijos competía; y los hermanos luchaban;",
    (17, 14): "y el tirano combatía en contra; y el mundo y la vida de los "
              "hombres miraban;",
    (17, 15): "y venció la piedad, coronando a sus propios atletas.",
    (17, 16): "¿Quién no admiró a aquellos atletas de la ley de la verdad? "
              "¿Quién no quedó asombrado?",
    (17, 17): "El mismo tirano y todo su consejo se admiraron de su aguante,",
    (17, 18): "por el cual ahora están junto al trono divino y viven la "
              "eternidad dichosa.",
    (17, 19): "Porque dice Moisés: «Y todos los santificados están bajo tus "
              "manos».",
    (17, 20): "Y también éstos, santificados por Dios, han sido honrados; y no "
              "sólo con este honor, sino con que, gracias a ellos, los "
              "enemigos no dominaron a nuestro pueblo,",
    (17, 21): "y el tirano fue castigado y la patria quedó purificada,",
    (17, 22): "porque ellos vinieron a ser como un rescate por el pecado del "
              "pueblo; y por la sangre de aquellos piadosos y por su muerte "
              "propiciatoria, la providencia divina salvó a Israel, que antes "
              "había sido maltratado.",
    (17, 23): "Porque, viendo el tirano Antíoco la hombría de su virtud y su "
              "aguante en los tormentos, proclamó a sus soldados el aguante de "
              "aquéllos como ejemplo;",
    (17, 24): "y con eso los tuvo nobles y valientes para el combate a pie y "
              "para el asedio, y, saqueando, venció a todos sus enemigos.",

    (18, 1): "¡Oh hijos israelitas, descendientes de la simiente de Abrahán! "
             "Obedeced a esta ley y sed piadosos en todo,",
    (18, 2): "sabiendo que la razón piadosa es dueña de las pasiones, y no "
             "sólo de los dolores de dentro, sino también de los de fuera;",
    (18, 3): "por lo cual aquéllos, entregando sus cuerpos a los dolores por "
             "la piedad, no sólo fueron admirados por los hombres, sino que "
             "fueron considerados dignos de la porción divina.",
    (18, 4): "Y por ellos el pueblo tuvo paz; y renovando el buen orden de la "
             "ley en la patria, echó a los enemigos del asedio.",
    (18, 5): "Y el tirano Antíoco fue castigado en la tierra, y muerto sigue "
             "siendo castigado; porque, como no pudo de ningún modo obligar a "
             "los de Jerusalén a adoptar costumbres extranjeras y a apartarse "
             "de las de sus padres,",
    (18, 6): "entonces partió de Jerusalén y fue a acampar contra los persas. "
             "Y la madre de los siete hijos, aquella mujer justa, decía "
             "también esto a sus hijos:",
    (18, 7): "«Yo fui virgen pura y no salí de la casa de mi padre; y guardé "
             "la costilla de la que fui edificada.",
    (18, 8): "No me corrompió el seductor que arruina en el descampado, ni "
             "estropeó la pureza de mi virginidad la serpiente corruptora del "
             "engaño; y viví con mi marido el tiempo de mi juventud.",
    (18, 9): "Y cuando éstos llegaron a la edad, murió vuestro padre. Dichoso "
             "él: porque, habiendo vivido buscando una vida con buenos hijos, "
             "no tuvo que sufrir el momento de quedarse sin ellos.",
    (18, 10): "Él os enseñaba, mientras estaba con nosotros, la ley y los "
              "profetas;",
    (18, 11): "nos leía lo de Abel, muerto por Caín, y lo de Isaac ofrecido en "
              "holocausto, y lo de José en la cárcel;",
    (18, 12): "nos hablaba del celo de Fineés, y os enseñaba lo de Ananías y "
              "Azarías y Misael en el fuego;",
    (18, 13): "y glorificaba a Daniel en el foso de los leones, y lo llamaba "
              "dichoso;",
    (18, 14): "y os recordaba el pasaje de Isaías que dice: «Aunque pases por "
              "el fuego, la llama no te quemará».",
    (18, 15): "Nos cantaba al salmista David, que dice: «Muchas son las "
              "aflicciones de los justos».",
    (18, 16): "Nos citaba el proverbio de Salomón que dice: «Es árbol de vida "
              "para todos los que hacen su voluntad».",
    (18, 17): "Nos confirmaba lo de Ezequiel, que dice: «¿Vivirán estos huesos "
              "secos?».",
    (18, 18): "Y no olvidaba el cántico que enseñó Moisés, el que enseña: «Yo "
              "hago morir y hago vivir;",
    (18, 19): "ésta es vuestra vida y la duración de vuestros días»».",
    (18, 20): "¡Oh día amargo aquél, y no amargo, cuando el amargo tirano de "
              "los griegos, encendiendo fuego en calderas crueles y llevando "
              "con furor hirviente a la catapulta y otra vez a sus tormentos a "
              "los siete hijos de aquella hija de Abrahán,",
    (18, 21): "les cegó las pupilas de los ojos y les cortó las lenguas y los "
              "mató con tormentos variados!",
    (18, 22): "Por lo cual la justicia divina persiguió y seguirá persiguiendo "
              "a aquel maldito.",
    (18, 23): "Y los hijos de Abrahán, con su madre vencedora, se reúnen en la "
              "morada de los padres, habiendo recibido de Dios almas puras e "
              "inmortales;",
    (18, 24): "a él la gloria por los siglos de los siglos. Amén.",
}
