"""Baruc en español, traducido del griego.

Baruc es el secretario de Jeremías —el que escribió al dictado el rollo que el
rey Joacim quemó, en Jeremías 36—, y este libro se le atribuye. Para las
Asambleas de Dios no es canon; se ofrece para estudio, y tiene tres partes que
no se parecen entre sí:

- 1 y 2, la confesión de los desterrados: «del Señor nuestro Dios es la
  justicia; y de nosotros, la vergüenza del rostro». Es el mismo molde de la
  oración de Daniel 9, y compararlas enseña cómo oraba Israel en el destierro.
- 3:9 a 4:4, el poema de la sabiduría: dónde se encuentra, quién la halló, y la
  respuesta —«es el libro de los mandamientos de Dios»—.
- 4:5 a 5:9, Jerusalén hablando a sus hijos como una madre, y el consuelo.

El griego trae calcos del hebreo que suenan raro en cualquier idioma («hombre
de Judá» por «cada uno de Judá»); se conservan cuando no estorban, porque son
la huella del original perdido y en exégesis se discuten.
"""

from __future__ import annotations

BARUC_ES: dict[tuple[int, int], str] = {
    # --- 1. La carta desde Babilonia ---------------------------------------
    (1, 1): "Y éstas son las palabras del libro que escribió Baruc, hijo de "
            "Nerías, hijo de Maasías, hijo de Sedequías, hijo de Asadías, hijo "
            "de Jelcías, en Babilonia,",
    (1, 2): "el año quinto, a siete del mes, en el tiempo en que los caldeos "
            "tomaron Jerusalén y la incendiaron.",
    (1, 3): "Y leyó Baruc las palabras de este libro a oídos de Jeconías, hijo "
            "de Joacim, rey de Judá, y a oídos de todo el pueblo que venía a oír "
            "el libro,",
    (1, 4): "y a oídos de los poderosos y de los hijos de los reyes, y a oídos "
            "de los ancianos, y a oídos de todo el pueblo, desde el menor hasta "
            "el mayor, de todos los que habitaban en Babilonia junto al río Sud.",
    (1, 5): "Y lloraban y ayunaban y oraban delante del Señor;",
    (1, 6): "y recogieron plata, según lo que la mano de cada uno podía.",
    (1, 7): "Y la enviaron a Jerusalén, a Joacim, hijo de Jelcías, hijo de "
            "Salom, el sacerdote, y a los sacerdotes y a todo el pueblo que se "
            "hallaba con él en Jerusalén,",
    (1, 8): "cuando él tomó los utensilios de la casa del Señor, los que habían "
            "sido sacados del templo, para devolverlos a la tierra de Judá, el "
            "día diez de siván: utensilios de plata que había hecho Sedequías, "
            "hijo de Josías, rey de Judá,",
    (1, 9): "después que Nabucodonosor, rey de Babilonia, deportó de Jerusalén a "
            "Jeconías y a los príncipes y a los prisioneros y a los poderosos y "
            "al pueblo de la tierra, y lo llevó a Babilonia.",
    (1, 10): "Y dijeron: «He aquí que os hemos enviado plata; comprad con ella "
             "holocaustos y ofrendas por el pecado e incienso, y preparad "
             "ofrenda de flor de harina y ofrecedla sobre el altar del Señor "
             "nuestro Dios;",
    (1, 11): "y orad por la vida de Nabucodonosor, rey de Babilonia, y por la "
             "vida de Baltasar su hijo, para que sus días sean como los días del "
             "cielo sobre la tierra.",
    (1, 12): "Y el Señor nos dará fuerza y alumbrará nuestros ojos, y viviremos "
             "bajo la sombra de Nabucodonosor, rey de Babilonia, y bajo la "
             "sombra de Baltasar su hijo, y les serviremos muchos días […]",
    (1, 13): "Y orad por nosotros al Señor nuestro Dios, porque hemos pecado "
             "contra el Señor nuestro Dios, y no se ha apartado de nosotros el "
             "furor del Señor ni su ira hasta el día de hoy.",
    (1, 14): "Y leeréis este libro que os hemos enviado, para hacer confesión en "
             "la casa del Señor, en día de fiesta y en los días señalados;",
    (1, 15): "y diréis: «Del Señor nuestro Dios es la justicia; y de nosotros, "
             "la vergüenza del rostro, como en este día: de cada hombre de Judá "
             "y de los habitantes de Jerusalén,",
    (1, 16): "y de nuestros reyes y de nuestros príncipes y de nuestros "
             "sacerdotes y de nuestros profetas y de nuestros padres,",
    (1, 17): "porque pecamos delante del Señor",
    (1, 18): "y le desobedecimos, y no escuchamos la voz del Señor nuestro Dios "
             "para andar en los mandatos del Señor que puso delante de nosotros.",
    (1, 19): "Desde el día en que el Señor sacó a nuestros padres de la tierra "
             "de Egipto hasta el día de hoy hemos sido desobedientes al Señor "
             "nuestro Dios, y nos desentendíamos de escuchar su voz.",
    (1, 20): "Y se nos pegaron los males y la maldición que el Señor ordenó a "
             "Moisés su siervo el día en que sacó a nuestros padres para darnos "
             "una tierra que mana leche y miel, como en este día.",
    (1, 21): "Y no escuchamos la voz del Señor nuestro Dios conforme a todas las "
             "palabras de los profetas que nos envió,",
    (1, 22): "sino que se fue cada uno tras el designio de su corazón malvado, a "
             "servir a otros dioses, a hacer lo malo ante los ojos del Señor "
             "nuestro Dios».",

    # --- 2. La confesión y la oración de los desterrados -------------------
    (2, 1): "Y cumplió el Señor su palabra, la que habló contra nosotros y "
            "contra nuestros jueces que juzgaron a Israel, y contra nuestros "
            "reyes y contra nuestros príncipes y contra cada hombre de Israel y "
            "de Judá.",
    (2, 2): "No se ha hecho debajo de todo el cielo lo que hizo en Jerusalén, "
            "conforme a lo escrito en la ley de Moisés:",
    (2, 3): "que comeríamos, un hombre las carnes de su hijo y un hombre las "
            "carnes de su hija.",
    (2, 4): "Y los entregó sujetos a todos los reinos de alrededor, para oprobio "
            "[…] allí donde el Señor los esparció.",
    (2, 5): "Y quedaron abajo y no arriba, porque pecamos contra el Señor "
            "nuestro Dios, no escuchando su voz.",
    (2, 6): "Del Señor nuestro Dios es la justicia; y de nosotros y de nuestros "
            "padres, la vergüenza del rostro, como en este día.",
    (2, 7): "Todos estos males que el Señor habló contra nosotros han venido "
            "sobre nosotros.",
    (2, 8): "Y no suplicamos el rostro del Señor para que cada uno se volviese "
            "de los pensamientos de su corazón malvado.",
    (2, 9): "Y el Señor estuvo vigilante sobre los males, y el Señor los trajo "
            "sobre nosotros; porque justo es el Señor en todas sus obras, las "
            "que nos mandó.",
    (2, 10): "Y no escuchamos su voz para andar en los mandatos del Señor que "
             "puso delante de nosotros.",
    (2, 11): "Y ahora, Señor, Dios de Israel, que sacaste a tu pueblo de la "
             "tierra de Egipto con mano fuerte, con señales y con prodigios y "
             "con gran poder y con brazo levantado, y te hiciste un nombre como "
             "en este día:",
    (2, 12): "hemos pecado, hemos sido impíos, hemos obrado injustamente, Señor "
             "Dios nuestro, contra todos tus preceptos.",
    (2, 13): "Apártese de nosotros tu furor, porque hemos quedado pocos entre "
             "las naciones donde nos dispersaste.",
    (2, 14): "Escucha, Señor, nuestra oración y nuestra súplica, y líbranos por "
             "amor de ti, y danos gracia delante de los que nos deportaron,",
    (2, 15): "para que toda la tierra sepa que tú eres el Señor nuestro Dios, "
             "porque tu nombre ha sido invocado sobre Israel y sobre su linaje.",
    (2, 16): "Señor, mira desde tu casa santa y acuérdate de nosotros; inclina, "
             "Señor, tu oído y escucha.",
    (2, 17): "Abre tus ojos y mira: que no son los muertos en el Hades, cuyo "
             "espíritu fue quitado de sus entrañas, los que darán gloria y "
             "reconocerán la justicia del Señor;",
    (2, 18): "sino el alma afligida por la grandeza del castigo, la que anda "
             "encorvada y débil, y los ojos que desfallecen y el alma "
             "hambrienta: ésos te darán gloria y justicia, Señor.",
    (2, 19): "Porque no es por la justicia de nuestros padres ni de nuestros "
             "reyes por lo que presentamos nuestra súplica delante de ti, Señor "
             "Dios nuestro;",
    (2, 20): "porque enviaste tu furor y tu ira sobre nosotros, tal como "
             "hablaste por medio de tus siervos los profetas, diciendo:",
    (2, 21): "«Así dijo el Señor: Inclinad vuestro hombro y servid al rey de "
             "Babilonia, y quedaos en la tierra que di a vuestros padres;",
    (2, 22): "y si no escucháis la voz del Señor para servir al rey de "
             "Babilonia,",
    (2, 23): "haré cesar de las ciudades de Judá y de fuera de Jerusalén la voz "
             "de alegría y la voz de gozo, la voz del esposo y la voz de la "
             "esposa; y toda la tierra quedará desierta, sin habitantes».",
    (2, 24): "Y no escuchamos tu voz para servir al rey de Babilonia; y "
             "cumpliste tus palabras, las que hablaste por medio de tus siervos "
             "los profetas: que serían sacados los huesos de nuestros reyes y "
             "los huesos de nuestros padres.",
    (2, 25): "Y he aquí que están arrojados al calor del día y a la helada de la "
             "noche; y murieron entre dolores atroces, de hambre y de espada y "
             "de peste.",
    (2, 26): "Y pusiste la casa sobre la cual fue invocado tu nombre como está "
             "en este día, por la maldad de la casa de Israel y de la casa de "
             "Judá.",
    (2, 27): "Y has obrado con nosotros, Señor Dios nuestro, conforme a toda tu "
             "clemencia y conforme a toda tu gran misericordia,",
    (2, 28): "según hablaste por medio de tu siervo Moisés, el día en que le "
             "mandaste escribir tu ley delante de los hijos de Israel, diciendo:",
    (2, 29): "«Si no escucháis mi voz, ciertamente este gran zumbido, esta "
             "muchedumbre, quedará reducida a poca cosa entre las naciones donde "
             "yo los dispersaré.",
    (2, 30): "Porque sé que no me escucharán, porque es un pueblo de dura "
             "cerviz; pero volverán en sí en la tierra de su destierro,",
    (2, 31): "y conocerán que yo soy el Señor su Dios. Y les daré corazón y "
             "oídos que oigan,",
    (2, 32): "y me alabarán en la tierra de su destierro, y se acordarán de mi "
             "nombre;",
    (2, 33): "y se volverán de su dura cerviz y de sus obras malvadas, porque se "
             "acordarán del camino de sus padres, los que pecaron delante del "
             "Señor.",
    (2, 34): "Y los haré volver a la tierra que juré a sus padres, a Abraham y a "
             "Isaac y a Jacob, y se adueñarán de ella; y los multiplicaré, y no "
             "disminuirán.",
    (2, 35): "Y estableceré con ellos un pacto eterno: que yo seré su Dios y "
             "ellos serán mi pueblo; y no volveré a mover a mi pueblo Israel de "
             "la tierra que les di».",
    # --- 3. La oración, y el poema de la sabiduría -------------------------
    (3, 1): "Señor Todopoderoso, Dios de Israel: un alma en angustia y un "
            "espíritu abatido clama a ti.",
    (3, 2): "Escucha, Señor, y ten misericordia, porque hemos pecado delante de "
            "ti;",
    (3, 3): "porque tú permaneces sentado para siempre, y nosotros perecemos "
            "para siempre.",
    (3, 4): "Señor Todopoderoso, Dios de Israel: escucha la oración de los "
            "muertos de Israel y de los hijos de los que pecaron delante de ti, "
            "los que no escucharon la voz del Señor su Dios, y se nos pegaron "
            "los males.",
    (3, 5): "No te acuerdes de las injusticias de nuestros padres, sino "
            "acuérdate de tu mano y de tu nombre en este tiempo;",
    (3, 6): "porque tú eres el Señor nuestro Dios, y te alabaremos, Señor.",
    (3, 7): "Porque para esto pusiste tu temor en nuestro corazón, y que "
            "invocáramos tu nombre; y te alabaremos en nuestro destierro, porque "
            "hemos apartado de nuestro corazón toda la injusticia de nuestros "
            "padres, los que pecaron delante de ti.",
    (3, 8): "He aquí que hoy estamos en nuestro destierro, donde nos "
            "dispersaste, para oprobio y para maldición y para castigo, conforme "
            "a todas las injusticias de nuestros padres, que se apartaron del "
            "Señor nuestro Dios.",
    (3, 9): "Escucha, Israel, los mandamientos de vida; prestad oído para "
            "conocer la prudencia.",
    (3, 10): "¿Qué es esto, Israel? ¿Por qué estás en tierra de enemigos? Has "
             "envejecido en tierra extraña, te has contaminado con los muertos,",
    (3, 11): "has sido contado con los que bajan al Hades,",
    (3, 12): "has abandonado la fuente de la sabiduría.",
    (3, 13): "Si hubieras andado por el camino de Dios, habitarías en paz para "
             "siempre.",
    (3, 14): "Aprende dónde está la prudencia, dónde está la fuerza, dónde está "
             "el entendimiento; y sabrás a la vez dónde está la larga vida y la "
             "vida, dónde está la luz de los ojos y la paz.",
    (3, 15): "¿Quién halló su lugar, y quién entró en sus tesoros?",
    (3, 16): "¿Dónde están los príncipes de las naciones y los que dominan las "
             "fieras de la tierra?",
    (3, 17): "Los que juegan con las aves del cielo, y atesoran la plata y el "
             "oro en que confiaron los hombres, y no hay fin de sus posesiones.",
    (3, 18): "Los que labran la plata y se afanan, y no hay quien descubra sus "
             "obras.",
    (3, 19): "Desaparecieron y bajaron al Hades, y otros se levantaron en su "
             "lugar.",
    (3, 20): "Jóvenes vieron la luz y habitaron sobre la tierra, pero el camino "
             "del conocimiento no lo conocieron",
    (3, 21): "ni entendieron sus sendas ni se asieron de ella; y sus hijos se "
             "alejaron de su camino.",
    (3, 22): "No se oyó de ella en Canaán ni se vio en Temán.",
    (3, 23): "Ni los hijos de Agar, que buscan la inteligencia sobre la tierra; "
             "ni los mercaderes de Merrán y de Temán, ni los fabuladores ni los "
             "que buscan la inteligencia: el camino de la sabiduría no lo "
             "conocieron ni se acordaron de sus sendas.",
    (3, 24): "Oh Israel, ¡qué grande es la casa de Dios, y qué extenso el lugar "
             "de su posesión!",
    (3, 25): "Grande, y no tiene fin; alto, e inconmensurable.",
    (3, 26): "Allí nacieron los gigantes, los famosos desde el principio, de "
             "gran estatura, diestros en la guerra.",
    (3, 27): "No a éstos escogió Dios, ni les dio el camino del conocimiento;",
    (3, 28): "y perecieron por no tener prudencia, perecieron por su falta de "
             "consejo.",
    (3, 29): "¿Quién subió al cielo y la tomó, y la hizo bajar de las nubes?",
    (3, 30): "¿Quién pasó al otro lado del mar y la halló, y la traerá a cambio "
             "de oro escogido?",
    (3, 31): "No hay quien conozca su camino, ni quien piense en su senda.",
    (3, 32): "Pero el que sabe todas las cosas la conoce, y la descubrió con su "
             "entendimiento: el que preparó la tierra para siempre y la llenó de "
             "animales de cuatro patas;",
    (3, 33): "el que envía la luz, y ella va; la llamó, y le obedeció temblando.",
    (3, 34): "Y las estrellas brillaron en sus puestos de guardia y se "
             "alegraron;",
    (3, 35): "las llamó, y dijeron: «Aquí estamos»; y brillaron con alegría para "
             "el que las hizo.",
    (3, 36): "Éste es nuestro Dios; ningún otro será contado junto a él.",
    (3, 37): "Descubrió todo camino de conocimiento, y se lo dio a Jacob su "
             "siervo y a Israel su amado.",
    (3, 38): "Después de esto apareció sobre la tierra, y convivió entre los "
             "hombres.",

    # --- 4. Jerusalén habla a sus hijos ------------------------------------
    (4, 1): "Éste es el libro de los mandamientos de Dios, y la ley que "
            "permanece para siempre: todos los que se aferran a ella, para vida; "
            "pero los que la abandonan morirán.",
    (4, 2): "Vuélvete, Jacob, y ásete de ella; camina hacia el resplandor, "
            "delante de su luz.",
    (4, 3): "No des a otro tu gloria, ni lo que te aprovecha a una nación "
            "extraña.",
    (4, 4): "Bienaventurados somos, Israel, porque lo que agrada a Dios nos es "
            "conocido.",
    (4, 5): "Ten ánimo, pueblo mío, memorial de Israel.",
    (4, 6): "Fuisteis vendidos a las naciones, no para perdición, sino que por "
            "haber irritado a Dios fuisteis entregados a los adversarios.",
    (4, 7): "Porque exasperasteis al que os hizo, sacrificando a los demonios y "
            "no a Dios;",
    (4, 8): "os olvidasteis del Dios eterno que os crió, y afligisteis también a "
            "Jerusalén, que os alimentó.",
    (4, 9): "Porque ella vio la ira que os venía de Dios, y dijo: «Escuchad, "
            "vecinas de Sion: Dios me ha traído gran duelo.",
    (4, 10): "Porque vi el cautiverio de mis hijos y de mis hijas, el que les "
             "trajo el Eterno.",
    (4, 11): "Porque los crié con alegría, pero los despedí con llanto y duelo.",
    (4, 12): "Nadie se alegre de mí, viuda y abandonada de muchos; quedé "
             "desolada por los pecados de mis hijos, porque se apartaron de la "
             "ley de Dios,",
    (4, 13): "y no conocieron sus preceptos, ni anduvieron por los caminos de "
             "los mandamientos de Dios, ni pisaron las sendas de la instrucción "
             "en su justicia.",
    (4, 14): "Vengan las vecinas de Sion, y acordaos del cautiverio de mis hijos "
             "y de mis hijas, el que les trajo el Eterno.",
    (4, 15): "Porque trajo contra ellos una nación de lejos, nación "
             "desvergonzada y de lengua extraña, que no respetó al anciano ni "
             "tuvo compasión del niño;",
    (4, 16): "y se llevaron a los amados de la viuda, y a la que estaba sola "
             "entre las hijas la dejaron desolada.",
    (4, 17): "Y yo, ¿en qué puedo ayudaros?",
    (4, 18): "Porque el que trajo los males os librará de la mano de vuestros "
             "enemigos.",
    (4, 19): "Andad, hijos, andad; que yo he quedado desolada.",
    (4, 20): "Me despojé de la túnica de la paz y me vestí el saco de mi "
             "súplica; clamaré al Eterno en mis días.",
    (4, 21): "Tened ánimo, hijos, clamad a Dios, y él os librará del poder, de "
             "la mano de los enemigos.",
    (4, 22): "Porque yo esperé del Eterno vuestra salvación, y me vino gozo de "
             "parte del Santo por la misericordia que os llegará pronto de "
             "vuestro eterno Salvador.",
    (4, 23): "Porque os envié con duelo y llanto, pero Dios os devolverá a mí "
             "con gozo y alegría para siempre.",
    (4, 24): "Porque así como ahora han visto las vecinas de Sion vuestro "
             "cautiverio, así verán pronto la salvación que os viene de vuestro "
             "Dios, la cual vendrá sobre vosotros con gran gloria y con el "
             "resplandor del Eterno.",
    (4, 25): "Hijos, soportad con paciencia la ira que os ha venido de Dios; te "
             "persiguió el enemigo, pero verás pronto su perdición, y pisarás "
             "sobre sus cuellos.",
    (4, 26): "Mis delicados anduvieron por caminos ásperos; fueron llevados como "
             "rebaño arrebatado por enemigos.",
    (4, 27): "Tened ánimo, hijos, y clamad a Dios, porque habrá memoria de "
             "vosotros de parte del que os trajo esto.",
    (4, 28): "Porque así como vuestro pensamiento se desvió de Dios, "
             "decuplicadlo al volveros a buscarlo.",
    (4, 29): "Porque el que os trajo los males os traerá la alegría eterna con "
             "vuestra salvación.",
    (4, 30): "Ten ánimo, Jerusalén: te consolará el que te dio nombre.",
    (4, 31): "Desdichados los que te maltrataron y se alegraron de tu caída;",
    (4, 32): "desdichadas las ciudades a las que sirvieron tus hijos; desdichada "
             "la que recibió a tus hijos.",
    (4, 33): "Porque así como se alegró de tu caída y se gozó de tu ruina, así "
             "se afligirá por su propia desolación.",
    (4, 34): "Y le quitaré el regocijo de su mucha gente, y su arrogancia se "
             "volverá duelo.",
    (4, 35): "Porque vendrá sobre ella fuego del Eterno por largos días, y será "
             "habitada por demonios la mayor parte del tiempo.",
    (4, 36): "Mira hacia el oriente, Jerusalén, y ve la alegría que te viene de "
             "Dios.",
    (4, 37): "He aquí que vienen tus hijos, los que despediste; vienen reunidos "
             "desde el oriente hasta el occidente, por la palabra del Santo, "
             "gozándose en la gloria de Dios.",

    # --- 5. El consuelo de Jerusalén ---------------------------------------
    (5, 1): "Despójate, Jerusalén, de la túnica de tu duelo y de tu aflicción, y "
            "vístete para siempre la hermosura de la gloria que viene de Dios.",
    (5, 2): "Envuélvete en el manto de la justicia que viene de Dios; ponte "
            "sobre la cabeza la mitra de la gloria del Eterno.",
    (5, 3): "Porque Dios mostrará tu resplandor a toda la tierra debajo del "
            "cielo.",
    (5, 4): "Porque tu nombre será llamado por Dios para siempre: «Paz de la "
            "justicia y gloria de la piedad».",
    (5, 5): "Levántate, Jerusalén, y ponte en lo alto, y mira hacia el oriente, "
            "y ve a tus hijos reunidos desde el poniente hasta el oriente, por "
            "la palabra del Santo, gozándose en el recuerdo de Dios.",
    (5, 6): "Porque salieron de ti a pie, llevados por enemigos; pero Dios te "
            "los trae, levantados con gloria como trono de reino.",
    (5, 7): "Porque Dios ha ordenado que se abaje todo monte alto y las dunas "
            "perpetuas, y que se llenen los barrancos, para allanar la tierra, a "
            "fin de que Israel camine seguro en la gloria de Dios.",
    (5, 8): "Y dieron sombra también los bosques y todo árbol oloroso a Israel, "
            "por mandato de Dios.",
    (5, 9): "Porque Dios guiará a Israel con alegría, a la luz de su gloria, con "
            "la misericordia y la justicia que vienen de él.",
}
