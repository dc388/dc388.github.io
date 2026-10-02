"""Los Salmos de Salomón en español, traducidos del griego.

Para las Asambleas de Dios no son canon; se ofrecen para estudio. No los
escribió Salomón: son dieciocho salmos compuestos en Jerusalén hacia el año 60
antes de Cristo, por gente que acababa de ver a Pompeyo entrar en el templo. El
«dragón» del salmo 2, muerto a estocadas en la arena de Egipto y sin quien lo
entierre, es Pompeyo; ese detalle fecha el libro casi al año.

Su interés es que aquí está, con todas sus letras, la esperanza mesiánica judía
del siglo anterior a Jesús. El salmo 17 pide a Dios que levante «al hijo de
David» para reinar sobre Israel, y dice cómo será ese rey: sin caballos ni
jinetes ni arcos, sin acumular oro para la guerra; quebrará la soberbia con la
palabra de su boca, reunirá un pueblo santo, y las naciones vendrán a Jerusalén
a ver su gloria. Lo llama «Cristo Señor» —χριστὸς κύριος—, que es la primera
vez que esas dos palabras aparecen juntas fuera del Nuevo Testamento.

Leer eso y después leer a los discípulos preguntando «¿restaurarás en este
tiempo el reino a Israel?» explica muchas cosas: ésta era la expectativa con la
que Jesús se encontró, y con la que discutió.

Los salmos 1, 2 y 3 llevan en esta edición griega el epígrafe descolocado —el
título del salmo aparece metido dentro de un versículo o al final, numerado
como si fuera un versículo más (2:8, 3:41)—. Se traduce donde el texto lo pone
y se avisa aquí, en vez de recolocarlo en silencio.
"""

from __future__ import annotations

SALMOS_SALOMON_ES: dict[tuple[int, int], str] = {
    (1, 1): "Clamé al Señor cuando me vi del todo afligido, a Dios cuando los "
            "pecadores se echaron encima.",
    (1, 2): "De repente se oyó delante de mí un clamor de guerra. Me "
            "escuchará, porque yo estaba lleno de justicia.",
    (1, 3): "Pensé en mi corazón que estaba lleno de justicia, porque me iba "
            "bien y era rico en hijos.",
    (1, 4): "Su riqueza se extendió por toda la tierra, y su gloria hasta el "
            "extremo de la tierra.",
    (1, 5): "Se encumbraron hasta las estrellas; dijeron: «No caeremos»;",
    (1, 6): "y se insolentaron con sus bienes, y no lo soportaron.",
    (1, 7): "Sus pecados estaban en lo escondido, y yo no lo sabía;",
    (1, 8): "sus iniquidades pasaron a las de las naciones anteriores a ellos; "
            "profanaron sin reparo el santuario del Señor.",

    (2, 1): "Cuando el pecador se ensoberbeció, derribó con el ariete las "
            "murallas fuertes, y tú no lo impediste.",
    (2, 2): "Subieron naciones extranjeras a tu altar y lo pisotearon con sus "
            "sandalias, llenos de soberbia,",
    (2, 3): "porque los hijos de Jerusalén habían manchado el santuario del "
            "Señor y habían profanado con iniquidades las ofrendas de Dios.",
    (2, 4): "Por eso dijo: «Apartadlas lejos de mí»; no le agradó a él la "
            "hermosura de la gloria de ellos.",
    (2, 5): "Fue tenida en nada delante de Dios, fue deshonrada del todo.",
    (2, 6): "Hijos e hijas en cautiverio duro, marcado a hierro el cuello, "
            "señalados entre las naciones.",
    (2, 7): "Conforme a sus pecados hizo con ellos, porque los abandonó en "
            "manos de los que prevalecían.",
    (2, 8): "Salmo de Salomón, sobre Jerusalén. Porque apartó su rostro de "
            "tener misericordia de ellos: del joven y del anciano y de sus "
            "hijos, de una vez;",
    (2, 9): "porque hicieron el mal de una vez, sin querer oír.",
    (2, 10): "Y el cielo se llenó de indignación, y la tierra los aborreció,",
    (2, 11): "porque ningún hombre había hecho sobre ella lo que ellos "
             "hicieron.",
    (2, 12): "Y conocerá la tierra todos tus juicios, que son justos, oh Dios.",
    (2, 13): "Pusieron a los hijos de Jerusalén por escarnio, a cambio de las "
             "prostitutas que había en ella; todo el que pasaba entraba a "
             "plena luz del sol; se burlaban de sus iniquidades.",
    (2, 14): "Como ellos mismos hacían, así a la luz del sol quedaron "
             "expuestas sus injusticias. Y las hijas de Jerusalén quedaron "
             "profanadas conforme a tu juicio,",
    (2, 15): "porque ellas mismas se mancharon en el revoltijo de sus uniones. "
             "Me duelen por esto las entrañas y las tripas.",
    (2, 16): "Yo te doy la razón, oh Dios, con rectitud de corazón; porque en "
             "tus juicios está tu justicia, oh Dios.",
    (2, 17): "Porque pagaste a los pecadores conforme a sus obras, y conforme "
             "a sus pecados, que fueron muy malos.",
    (2, 18): "Descubriste sus pecados para que se viera tu juicio;",
    (2, 19): "borraste su memoria de la tierra. Dios es juez justo, y no hace "
             "acepción de personas.",
    (2, 20): "Porque las naciones afrentaron a Jerusalén pisoteándola; arrancó "
             "su hermosura del trono de gloria.",
    (2, 21): "Se ciñó cilicio en vez de vestido de gala, una soga en la cabeza "
             "en vez de corona.",
    (2, 22): "Se quitó la diadema de gloria que Dios le había puesto.",
    (2, 23): "Con deshonra fue arrojada por tierra su hermosura.",
    (2, 24): "Y yo lo vi, y supliqué ante el rostro del Señor, y dije: "
             "«Basta ya, Señor, de que tu mano pese sobre Israel con la "
             "invasión de las naciones;",
    (2, 25): "porque se burlaron y no perdonaron, con ira y furor y con "
             "rencor;",
    (2, 26): "y acabarán con ellos si tú, Señor, no los reprendes con tu ira.",
    (2, 27): "Porque no lo hicieron por celo, sino por el apetito de su alma,",
    (2, 28): "para derramar su ira sobre nosotros en el saqueo. Y no tardes, "
             "oh Dios, en devolvérselo sobre sus cabezas,",
    (2, 29): "para poner en deshonra la soberbia del dragón».",
    (2, 30): "Y no tardó, hasta que Dios me mostró su insolencia: atravesado a "
             "estocadas en los montes de Egipto, tenido en menos que lo más "
             "insignificante en la tierra y en el mar;",
    (2, 31): "su cuerpo llevado de acá para allá sobre las olas, con gran "
             "ultraje, y no había quien lo enterrase,",
    (2, 32): "porque Dios lo había humillado con deshonra. No consideró que "
             "era un hombre, ni pensó en el final.",
    (2, 33): "Dijo: «Yo seré señor de la tierra y del mar»; y no reconoció que "
             "Dios es grande, poderoso en su gran fuerza.",
    (2, 34): "Él es rey sobre los cielos, y juzga a reyes y a autoridades;",
    (2, 35): "él es quien me levanta a mí para gloria, y quien hace dormir a "
             "los soberbios en perdición eterna con deshonra, porque no lo "
             "conocieron.",
    (2, 36): "Y ahora ved, magnates de la tierra, el juicio del Señor, porque "
             "es un rey grande y justo, que juzga lo que hay bajo el cielo.",
    (2, 37): "Bendecid a Dios los que teméis al Señor con inteligencia, porque "
             "la misericordia del Señor está sobre los que le temen, junto con "
             "el juicio,",
    (2, 38): "para distinguir entre el justo y el pecador, y pagar a los "
             "pecadores para siempre conforme a sus obras,",
    (2, 39): "y compadecerse del justo librándolo de la humillación del "
             "pecador, y pagar al pecador por lo que hizo al justo.",
    (2, 40): "Porque el Señor es bueno con los que lo invocan con paciencia, "
             "para tratar según su misericordia a sus santos, de modo que "
             "estén siempre en pie delante de él con fortaleza.",
    (2, 41): "Bendito sea el Señor para siempre delante de sus siervos.",

    (3, 1): "¿Por qué duermes, alma mía, y no bendices al Señor?",
    (3, 2): "Cantad himno y alabanza a Dios, que es digno de alabanza. Canta y "
            "está en vela, atenta a su vigilancia; porque un salmo brotado de "
            "un corazón bueno es cosa buena para Dios.",
    (3, 3): "Los justos se acuerdan siempre del Señor, confesándolo y "
            "reconociendo justos los juicios del Señor.",
    (3, 4): "El justo no desprecia la corrección del Señor; su voluntad está "
            "siempre delante del Señor.",
    (3, 5): "Tropezó el justo, y dio la razón al Señor; cayó, y mira qué hará "
            "Dios con él;",
    (3, 6): "está atento a ver de dónde le vendrá la salvación.",
    (3, 7): "La verdad de los justos viene de Dios, su salvador; no se hospeda "
            "en la casa del justo pecado sobre pecado.",
    (3, 8): "El justo revisa continuamente su casa, para quitar la injusticia "
            "que haya en su falta.",
    (3, 9): "Expía sus faltas involuntarias con ayuno y humillando su alma,",
    (3, 10): "y el Señor purifica a todo hombre santo y a su casa.",
    (3, 11): "Tropezó el pecador, y maldice su vida, el día de su nacimiento y "
             "los dolores de su madre;",
    (3, 12): "añadió pecados a los pecados de su vida;",
    (3, 13): "cayó, porque su caída fue grave, y no se levantará. La perdición "
             "del pecador es para siempre,",
    (3, 14): "y no habrá memoria de él cuando Dios visite a los justos.",
    (3, 15): "Ésta es la suerte de los pecadores para siempre.",
    (3, 16): "Pero los que temen al Señor resucitarán para vida eterna, y su "
             "vida, en la luz del Señor, no acabará jamás.",
    (3, 41): "Salmo de Salomón, sobre los justos.",

    (4, 1): "¿Por qué tú, profano, te sientas en el consejo de los santos, "
            "estando tu corazón lejos del Señor, provocando con tus "
            "transgresiones al Dios de Israel?",
    (4, 2): "Desmedido en palabras, desmedido en aspavientos más que nadie; el "
            "duro de palabra para condenar a los pecadores en el juicio.",
    (4, 3): "Y su mano es la primera que cae sobre el acusado, como movida por "
            "celo, siendo él mismo culpable de toda clase de pecados y de "
            "desenfrenos.",
    (4, 4): "Sus ojos están sobre toda mujer sin distinción; su lengua miente "
            "en los tratos con juramento.",
    (4, 5): "De noche y a escondidas peca, como si no lo vieran; con los ojos "
            "le habla a cualquier mujer concertando la maldad.",
    (4, 6): "Rápido para entrar en cualquier casa con buena cara, como si no "
            "tuviera malicia.",
    (4, 7): "Quite Dios de en medio a los que viven con hipocresía entre los "
            "santos, con la ruina de su carne y con la pobreza de su vida;",
    (4, 8): "descubra Dios las obras de los hombres que buscan agradar a los "
            "hombres, con risa y burla de sus obras.",
    (4, 9): "Y den los santos por justo el juicio de su Dios, cuando sean "
            "quitados los pecadores de la presencia del justo,",
    (4, 10): "el adulador que sólo habla con engaño.",
    (4, 11): "Y sus ojos están sobre la casa de un hombre que vive tranquilo, "
             "como una serpiente, para deshacer la sensatez que hay entre "
             "ellos con palabras de transgresores.",
    (4, 12): "Sus palabras son sofismas, para llevar a cabo el deseo de los "
             "injustos.",
    (4, 13): "No paró hasta que logró dispersarlos como huérfanos, y dejó "
             "desierta una casa por un deseo ilícito.",
    (4, 14): "Engañó con palabras diciendo que no hay quien vea y juzgue;",
    (4, 15): "se hartó de transgresión con aquélla; y sus ojos van a otra "
             "casa, a destruirla con palabras que levantan el vuelo. Su alma "
             "no se sacia, como el Hades, con todo esto.",
    (4, 16): "Disertación de Salomón contra los que buscan agradar a los "
             "hombres. Sea, Señor, su suerte la deshonra delante de ti; su "
             "salida, entre gemidos, y su entrada, bajo maldición;",
    (4, 17): "sea su vida, Señor, en dolores y pobreza y estrechez; su sueño, "
             "entre penas, y su despertar, entre apuros;",
    (4, 18): "quítesele el sueño de las sienes por la noche; fracasen todas "
             "las obras de sus manos;",
    (4, 19): "quede su casa falta de todo aquello con que sacie su apetito;",
    (4, 20): "sea su vejez la soledad de no tener hijos, hasta que se lo "
             "lleven.",
    (4, 21): "Sean dispersadas por las fieras las carnes de los que buscan "
             "agradar a los hombres, y los huesos de los transgresores queden "
             "a la luz del sol con deshonra.",
    (4, 22): "Sáquenles los ojos los cuervos a los hipócritas,",
    (4, 23): "porque dejó desiertas muchas casas de hombres con deshonra, y "
             "las dispersó por su codicia;",
    (4, 24): "y no se acordaron de Dios, ni temieron a Dios en todo esto;",
    (4, 25): "y provocaron a Dios y lo irritaron hasta querer quitarlos de la "
             "tierra, porque engañaban con falacias a las almas sencillas.",
    (4, 26): "Dichosos los que temen al Señor en su sencillez;",
    (4, 27): "el Señor los librará de hombres taimados y pecadores; y nos "
             "librará de todo tropiezo del transgresor.",
    (4, 28): "Quite Dios de en medio a los que con soberbia cometen toda "
             "injusticia, porque el Señor nuestro Dios es un juez grande y "
             "poderoso en justicia.",
    (4, 29): "Sea, Señor, tu misericordia sobre todos los que te aman.",

    (5, 1): "Señor Dios, alabaré tu nombre con júbilo, en medio de los que "
            "conocen tus juicios justos.",
    (5, 2): "Porque tú eres el refugio bueno y misericordioso del pobre.",
    (5, 3): "Cuando yo clame a ti, no te calles ante mí,",
    (5, 4): "porque nadie toma botín de un hombre fuerte;",
    (5, 5): "y ¿quién tomará algo de todo lo que tú hiciste, si tú no se lo "
            "das?",
    (5, 6): "Porque el hombre y su suerte están ante ti en la balanza; no "
            "podrá añadir nada más de lo que decida tu juicio, oh Dios.",
    (5, 7): "Cuando estamos afligidos te invocamos pidiendo ayuda, y tú no "
            "rechazas nuestra súplica, porque tú eres nuestro Dios.",
    (5, 8): "No dejes caer pesada tu mano sobre nosotros, para que no pequemos "
            "por necesidad.",
    (5, 9): "Y aunque no nos hagas volver, no nos apartaremos, sino que "
            "acudiremos a ti;",
    (5, 10): "porque si tengo hambre, a ti clamaré, oh Dios, y tú me darás.",
    (5, 11): "Tú alimentas a las aves y a los peces, cuando das lluvia a los "
             "desiertos para que brote la hierba, preparando pasto en el "
             "desierto para todo ser vivo;",
    (5, 12): "y si tienen hambre, a ti levantan su rostro.",
    (5, 13): "A los reyes y a los príncipes y a los pueblos tú los alimentas, "
             "oh Dios; y del pobre y del indigente, ¿cuál es la esperanza sino "
             "tú, Señor?",
    (5, 14): "Y tú escucharás; porque ¿quién es bueno y benigno sino tú, que "
             "alegras el alma del humilde abriendo tu mano con misericordia?",
    (5, 15): "La bondad del hombre va con tacañería, y si repite el favor, es "
             "a regañadientes; y si lo hiciera sin refunfuñar, hasta eso sería "
             "de admirar.",
    (5, 16): "Pero tu don es abundante y generoso y rico, y aquel cuya "
             "esperanza está en ti no será escatimado en el don.",
    (5, 17): "Sobre toda la tierra está tu misericordia, Señor, con bondad.",
    (5, 18): "Dichoso aquel de quien Dios se acuerda dándole lo justo para "
             "bastarse;",
    (5, 19): "si el hombre tiene de sobra, peca;",
    (5, 20): "basta lo moderado con justicia, y en eso está la bendición del "
             "Señor, que da hartura con justicia.",
    (5, 21): "Se alegraron con bienes los que temen al Señor, y tu bondad está "
             "sobre Israel en tu reino.",
    (5, 22): "Bendita sea la gloria del Señor, porque él es nuestro rey.",
    (5, 29): "Salmo de Salomón.",

    (6, 1): "Dichoso el hombre cuyo corazón está dispuesto a invocar el nombre "
            "del Señor;",
    (6, 2): "cuando se acuerde del nombre del Señor, será salvado.",
    (6, 3): "Sus caminos son enderezados por el Señor, y las obras de sus "
            "manos, guardadas por el Señor su Dios.",
    (6, 4): "No se turbará por la visión de sus malos sueños;",
    (6, 5): "su alma no se espantará al cruzar ríos ni en el vaivén de los "
            "mares.",
    (6, 6): "Se levantó de su sueño y bendijo el nombre del Señor;",
    (6, 7): "con el corazón sereno cantó himnos al nombre de Dios, y suplicó "
            "ante el rostro del Señor por toda su casa.",
    (6, 8): "Y el Señor escuchó la oración de todo el que teme a Dios, y toda "
            "petición del alma que espera en él la cumple el Señor.",
    (6, 9): "Bendito sea el Señor, que hace misericordia con los que lo aman "
            "de verdad.",
    (6, 22): "De Salomón, sobre la esperanza.",

    (7, 1): "No te alejes de nosotros, oh Dios, para que no se echen sobre "
            "nosotros los que nos aborrecieron sin causa.",
    (7, 2): "Porque tú los rechazaste, oh Dios; que su pie no pise la heredad "
            "de tu santuario.",
    (7, 3): "Corrígenos tú conforme a tu voluntad, y no nos entregues a las "
            "naciones.",
    (7, 4): "Porque, si envías la muerte, tú le darás órdenes acerca de "
            "nosotros; porque tú eres misericordioso y no te airarás hasta "
            "acabar con nosotros.",
    (7, 5): "Mientras tu nombre habite en medio de nosotros, alcanzaremos "
            "misericordia.",
    (7, 6): "Y ninguna nación podrá contra nosotros, porque tú eres nuestro "
            "escudo.",
    (7, 7): "Y nosotros te invocaremos, y tú nos escucharás;",
    (7, 8): "porque tú te compadecerás del linaje de Israel para siempre, y no "
            "lo rechazarás; y nosotros estaremos bajo tu yugo para siempre, y "
            "bajo el azote de tu corrección.",
    (7, 9): "De Salomón, sobre la vuelta. Nos enderezarás en el tiempo de tu "
            "auxilio, para tener misericordia de la casa de Jacob en el día en "
            "que se lo prometiste.",

    (8, 1): "Aflicción y ruido de guerra oyó mi oído: sonido de trompeta que "
            "anuncia matanza y ruina;",
    (8, 2): "clamor de un pueblo numeroso como de un viento muy fuerte, como "
            "una tormenta de fuego arrastrada por el desierto.",
    (8, 3): "Y dije en mi corazón: «¿Dónde va a juzgarlo Dios?».",
    (8, 4): "Oí una voz hacia Jerusalén, ciudad del santuario;",
    (8, 5): "se me quebraron los riñones al oírlo, se me aflojaron las "
            "rodillas;",
    (8, 6): "se asustó mi corazón, se me estremecieron los huesos como lino.",
    (8, 7): "Dije: «Enderezan sus caminos con justicia». Repasé los juicios de "
            "Dios desde la creación del cielo y de la tierra; y di por justo a "
            "Dios en sus juicios de siempre.",
    (8, 8): "Descubrió Dios sus pecados a la luz del sol; conoció toda la "
            "tierra los juicios justos de Dios.",
    (8, 9): "De Salomón, para la victoria. En sótanos escondidos estaban sus "
            "transgresiones, que provocaban la ira;",
    (8, 10): "el hijo con la madre y el padre con la hija se revolcaban;",
    (8, 11): "cometían adulterio cada uno con la mujer de su prójimo, y "
             "hacían entre sí pactos con juramento sobre esto.",
    (8, 12): "Saqueaban las cosas santas de Dios, como si no hubiera heredero "
             "que las rescatase.",
    (8, 13): "Pisaban el altar del Señor con toda clase de impureza, y con "
             "flujo de sangre mancharon los sacrificios, como si fueran carnes "
             "profanas.",
    (8, 14): "No dejaron pecado que no cometiesen, más que las naciones.",
    (8, 15): "Por eso les mezcló Dios un espíritu de extravío, les dio a beber "
             "una copa de vino puro hasta la embriaguez.",
    (8, 16): "Trajo al que venía del extremo de la tierra, al que golpea con "
             "fuerza;",
    (8, 17): "decretó la guerra contra Jerusalén y contra su tierra.",
    (8, 18): "Salieron a su encuentro los príncipes de la tierra con alegría; "
             "le dijeron: «Bienvenido sea tu camino; venid, entrad en paz».",
    (8, 19): "Allanaron los caminos ásperos para su entrada, abrieron las "
             "puertas de Jerusalén, coronaron sus murallas.",
    (8, 20): "Entró como un padre en la casa de sus hijos, en paz; asentó sus "
             "pies con toda seguridad.",
    (8, 21): "Tomó sus torres fortificadas y la muralla de Jerusalén,",
    (8, 22): "porque Dios lo trajo seguro en medio del extravío de ellos.",
    (8, 23): "Destruyó a sus príncipes y a todo sabio en el consejo, derramó "
             "la sangre de los habitantes de Jerusalén como agua sucia.",
    (8, 24): "Se llevó a sus hijos y a sus hijas, los que habían engendrado en "
             "profanación.",
    (8, 25): "Habían obrado conforme a sus impurezas, igual que sus padres;",
    (8, 26): "profanaron Jerusalén y las cosas consagradas al nombre de Dios.",
    (8, 27): "Quedó justificado Dios en sus juicios ante las naciones de la "
             "tierra;",
    (8, 28): "y los santos de Dios, como corderos en su inocencia, en medio de "
             "ellos.",
    (8, 29): "Digno de alabanza es el Señor, que juzga a toda la tierra con su "
             "justicia.",
    (8, 30): "Mira, oh Dios: nos mostraste tu juicio en tu justicia.",
    (8, 31): "Vieron nuestros ojos tus juicios, oh Dios; reconocimos justo tu "
             "nombre venerable por los siglos,",
    (8, 32): "porque tú eres el Dios de la justicia, que juzga a Israel "
             "corrigiéndolo.",
    (8, 33): "Vuelve, oh Dios, tu misericordia sobre nosotros, y compadécete "
             "de nosotros;",
    (8, 34): "reúne la dispersión de Israel con misericordia y bondad.",
    (8, 35): "Porque tu fidelidad está con nosotros, y nosotros endurecimos "
             "nuestra cerviz; y tú eres el que nos corrige.",
    (8, 36): "No nos desprecies, Dios nuestro, para que no nos devoren las "
             "naciones como si no hubiera quien nos rescatase.",
    (8, 37): "Y tú eres nuestro Dios desde el principio, y en ti está nuestra "
             "esperanza, Señor;",
    (8, 38): "y nosotros no nos apartaremos de ti, porque tus juicios sobre "
             "nosotros son buenos.",
    (8, 39): "Para nosotros y para nuestros hijos es tu favor para siempre; "
             "Señor salvador nuestro, no volveremos a ser sacudidos por los "
             "siglos.",
    (8, 40): "Digno de alabanza es el Señor en sus juicios, en boca de los "
             "santos; y bendito sea Israel por el Señor para siempre.",

    (9, 1): "Cuando Israel fue llevado en destierro a tierra extranjera, por "
            "haberse apartado del Señor que los había rescatado,",
    (9, 2): "fueron arrojados de la heredad que el Señor les había dado; entre "
            "todas las naciones está la dispersión de Israel, conforme a la "
            "palabra de Dios;",
    (9, 3): "para que quedes justificado, oh Dios, en tu justicia, en medio de "
            "nuestras iniquidades;",
    (9, 4): "porque tú eres juez justo sobre todos los pueblos de la tierra.",
    (9, 5): "Porque no se esconderá de tu conocimiento nadie que obre "
            "injusticias;",
    (9, 6): "y las obras justas de tus santos están delante de ti, Señor. ¿Y "
            "dónde se esconderá el hombre de tu conocimiento, oh Dios?",
    (9, 7): "Nuestras obras están en la elección y en la potestad de nuestra "
            "alma: hacer justicia o injusticia con las obras de nuestras "
            "manos.",
    (9, 8): "Y en tu justicia visitas a los hijos de los hombres:",
    (9, 9): "el que hace justicia atesora vida para sí ante el Señor, y el que "
            "hace injusticia es él mismo el culpable de la perdición de su "
            "alma;",
    (9, 10): "porque los juicios del Señor son con justicia, hombre por hombre "
             "y casa por casa.",
    (9, 11): "¿Con quién serás bueno, oh Dios, sino con los que invocan al "
             "Señor?",
    (9, 12): "Purificará del pecado al alma que se confiesa y lo declara "
             "abiertamente;",
    (9, 13): "porque la vergüenza es para nosotros y para nuestros rostros por "
             "todo ello.",
    (9, 14): "¿Y a quién perdonará los pecados sino a los que han pecado?",
    (9, 15): "Bendecirás a los justos y no los llamarás a cuentas por lo que "
             "pecaron; y tu bondad está sobre los que pecan y se arrepienten.",
    (9, 16): "Y ahora, tú eres Dios y nosotros el pueblo que amaste; mira y "
             "compadécete, Dios de Israel, porque somos tuyos; y no apartes tu "
             "misericordia de nosotros, para que no se echen sobre nosotros.",
    (9, 17): "Porque tú escogiste la descendencia de Abrahán entre todas las "
             "naciones,",
    (9, 18): "y pusiste tu nombre sobre nosotros, Señor; y no cesarás jamás.",
    (9, 19): "Hiciste alianza con nuestros padres acerca de nosotros, y "
             "nosotros esperaremos en ti con el alma vuelta a ti.",
    (9, 20): "Del Señor es la misericordia sobre la casa de Israel para "
             "siempre y para siempre jamás.",
    (9, 40): "De Salomón, sobre la reprensión.",

    (10, 1): "Dichoso el hombre de quien el Señor se acuerda con reprensión, y "
             "a quien aparta del mal camino con el azote, para que quede "
             "limpio de pecado y no lo multiplique.",
    (10, 2): "El que prepara la espalda para los azotes quedará limpio, porque "
             "el Señor es bueno con los que soportan la corrección.",
    (10, 3): "Porque enderezará los caminos de los justos, y no los torcerá "
             "con la corrección.",
    (10, 4): "Y la misericordia del Señor está sobre los que lo aman de "
             "verdad; y el Señor se acordará de sus siervos con misericordia.",
    (10, 5): "Porque el testimonio está en la ley de la alianza eterna, el "
             "testimonio del Señor sobre los caminos de los hombres cuando los "
             "visita.",
    (10, 6): "Justo y santo es nuestro Señor en sus juicios para siempre, e "
             "Israel alabará el nombre del Señor con alegría.",
    (10, 7): "Y los santos lo confesarán en la asamblea del pueblo, y Dios se "
             "compadecerá de los pobres para alegría de Israel;",
    (10, 8): "porque Dios es bueno y misericordioso para siempre, y las "
             "asambleas de Israel glorificarán el nombre del Señor.",
    (10, 9): "Del Señor es la salvación sobre la casa de Israel, para gozo "
             "eterno.",
    (10, 20): "De Salomón, en himnos.",

    (11, 1): "Tocad la trompeta en Sión, la trompeta que convoca a los santos;",
    (11, 2): "pregonad en Jerusalén la voz del que anuncia la buena noticia: "
             "que Dios ha tenido misericordia de Israel al visitarlos.",
    (11, 3): "Ponte en pie, Jerusalén, en lo alto, y mira a tus hijos "
             "reunidos de una vez, de oriente y de occidente, por el Señor.",
    (11, 4): "Del norte vienen con la alegría de su Dios; de islas lejanas los "
             "reunió Dios.",
    (11, 5): "Rebajó los montes altos hasta allanarlos para ellos;",
    (11, 6): "las colinas huyeron ante su llegada, los bosques les dieron "
             "sombra a su paso.",
    (11, 7): "Todo árbol de buen olor hizo Dios brotar para ellos, para que "
             "pasase Israel en la visita de la gloria de su Dios.",
    (11, 8): "Vístete, Jerusalén, los vestidos de tu gloria; prepara la "
             "vestidura de tu santidad, porque Dios ha prometido bienes a "
             "Israel para siempre y para siempre jamás.",
    (11, 9): "De Salomón, sobre la esperanza. Cumpla el Señor lo que ha "
             "prometido sobre Israel y sobre Jerusalén; levante el Señor a "
             "Israel en el nombre de su gloria. Del Señor es la misericordia "
             "sobre Israel para siempre y para siempre jamás.",

    (12, 1): "Señor, libra mi alma del hombre inicuo y malvado, de la lengua "
             "inicua y chismosa que dice mentiras y engaños.",
    (12, 2): "Con toda clase de retorcimientos son las palabras de la lengua "
             "del hombre malo, como el fuego que prende en la era y quema su "
             "hermosura.",
    (12, 3): "Su estancia es para llenar las casas con una lengua mentirosa, "
             "para cortar los árboles de la alegría con la llama que abrasa a "
             "los inicuos,",
    (12, 4): "para enredar a las casas en guerra con labios chismosos. Aleje "
             "Dios de los sencillos los labios de los inicuos, dejándolos "
             "perplejos, y sean dispersados los huesos de los chismosos lejos "
             "de los que temen al Señor.",
    (12, 5): "Perezca en llamas de fuego la lengua chismosa, lejos de los "
             "santos.",
    (12, 6): "Guarde el Señor el alma pacífica que aborrece a los injustos, y "
             "enderece el Señor al hombre que hace la paz en su casa.",
    (12, 7): "Del Señor es la salvación sobre Israel su siervo para siempre;",
    (12, 8): "y perezcan los pecadores de la presencia del Señor de una vez, y "
             "hereden los santos del Señor las promesas.",
    (12, 9): "De Salomón, sobre la lengua de los inicuos.",

    (13, 1): "La diestra del Señor me cubrió, la diestra del Señor nos "
             "perdonó.",
    (13, 2): "El brazo del Señor nos salvó de la espada que pasaba, del hambre "
             "y de la muerte de los pecadores.",
    (13, 3): "Fieras dañinas se les echaron encima; con sus dientes les "
             "arrancaban las carnes, y con sus muelas les trituraban los "
             "huesos; y de todo esto nos libró el Señor.",
    (13, 4): "Se turbó el impío por sus faltas, no fuera a ser arrastrado "
             "junto con los pecadores;",
    (13, 5): "porque es terrible la ruina del pecador, y nada de todo esto "
             "toca al justo.",
    (13, 6): "Porque no es lo mismo la corrección de los justos por sus faltas "
             "involuntarias que la ruina del pecador:",
    (13, 7): "al justo se le corrige con discreción, para que el pecador no se "
             "alegre a costa del justo.",
    (13, 8): "Salmo de Salomón: consuelo de los justos. Porque amonestará al "
             "justo como a un hijo amado, y su corrección será como la de un "
             "primogénito.",
    (13, 9): "Porque el Señor perdonará a sus santos, y borrará sus faltas con "
             "la corrección; porque la vida de los justos es para siempre.",
    (13, 10): "Pero los pecadores serán arrebatados a la perdición, y no "
              "quedará memoria de ellos;",
    (13, 11): "y sobre los santos está la misericordia del Señor, y sobre los "
              "que lo temen, su misericordia.",

    (14, 1): "Fiel es el Señor con los que lo aman de verdad, con los que "
             "soportan su corrección, con los que caminan en la justicia de "
             "sus preceptos, en la ley que nos mandó para nuestra vida.",
    (14, 2): "Los santos del Señor vivirán por ella para siempre; el paraíso "
             "del Señor, los árboles de la vida, son sus santos.",
    (14, 3): "Su plantación está enraizada para siempre; no serán arrancados "
             "en todos los días del cielo, porque la porción y la heredad de "
             "Dios es Israel.",
    (14, 4): "Pero no así los pecadores y los inicuos, que amaron un día "
             "pasado en la complicidad de su pecado; su deseo está en la "
             "pequeñez de lo que se pudre,",
    (14, 5): "y no se acordaron de Dios. Porque los caminos de los hombres "
             "están siempre a la vista delante de él, y conoce las cámaras del "
             "corazón antes de que existan.",
    (14, 6): "Por eso su herencia es el Hades y las tinieblas y la perdición, "
             "y no serán hallados en el día de la misericordia de los justos; "
             "pero los santos del Señor heredarán la vida con alegría.",
    (14, 11): "Himno de Salomón.",

    (15, 1): "Cuando me vi afligido invoqué el nombre del Señor, esperé en el "
             "auxilio del Dios de Jacob, y fui salvado;",
    (15, 2): "porque tú, oh Dios, eres la esperanza y el refugio de los "
             "pobres.",
    (15, 3): "Porque ¿quién es fuerte, oh Dios, sino para confesarte de "
             "verdad?",
    (15, 4): "¿Y para qué es capaz el hombre, sino para confesar tu nombre?",
    (15, 5): "Un salmo nuevo con cántico, con alegría de corazón, fruto de los "
             "labios con el instrumento afinado de la lengua, primicia de los "
             "labios salida de un corazón santo y justo.",
    (15, 6): "Salmo de Salomón, con cántico. El que hace esto no será sacudido "
             "jamás por el mal; la llama del fuego y la ira de los injustos no "
             "lo tocarán,",
    (15, 7): "cuando salgan de la presencia del Señor contra los pecadores "
             "para destruir toda la existencia de los pecadores.",
    (15, 8): "Porque la señal de Dios está sobre los justos para salvación: el "
             "hambre y la espada y la muerte están lejos de los justos.",
    (15, 9): "Porque huirán de los santos como perseguidos en la guerra; pero "
             "perseguirán a los pecadores y los alcanzarán, y los que cometen "
             "iniquidad no escaparán del juicio del Señor: serán alcanzados "
             "como por enemigos expertos.",
    (15, 10): "Porque la señal de la perdición está sobre su frente,",
    (15, 11): "y la herencia de los pecadores es la perdición y las tinieblas, "
              "y sus iniquidades los perseguirán hasta lo hondo del Hades.",
    (15, 12): "Su herencia no se hallará para sus hijos,",
    (15, 13): "porque los pecados dejarán desiertas las casas de los "
              "pecadores; y los pecadores perecerán para siempre en el día del "
              "juicio del Señor,",
    (15, 14): "cuando Dios visite la tierra con su juicio.",
    (15, 15): "Pero los que temen al Señor hallarán misericordia en aquel día, "
              "y vivirán por la misericordia de su Dios; y los pecadores "
              "perecerán para siempre.",

    (16, 1): "Cuando mi alma se adormeció lejos del Señor, por poco me deslicé "
             "en la modorra del sueño.",
    (16, 2): "Estando lejos de Dios, por poco se derramó mi alma en la muerte, "
             "cerca de las puertas del Hades junto con el pecador,",
    (16, 3): "al apartarse mi alma del Señor Dios de Israel, si el Señor no me "
             "hubiese socorrido con su misericordia eterna.",
    (16, 4): "Me picó como el aguijón al caballo, para que estuviese despierto "
             "ante él; mi salvador y mi socorro me salvó en todo momento.",
    (16, 5): "Te daré gracias, oh Dios, porque me socorriste para salvación y "
             "no me contaste entre los pecadores para la perdición.",
    (16, 6): "No apartes de mí tu misericordia, oh Dios, ni el recuerdo de ti "
             "de mi corazón hasta la muerte.",
    (16, 7): "Domíname, oh Dios, apartándome del pecado malo y de toda mujer "
             "mala que hace caer al insensato.",
    (16, 8): "Y no me engañe la hermosura de una mujer sin ley, ni nada de lo "
             "que se somete a un pecado que no aprovecha.",
    (16, 9): "Endereza las obras de mis manos en tu presencia, y guarda mis "
             "pasos en tu recuerdo.",
    (16, 10): "Cuida mi lengua y mis labios con palabras de verdad; aparta "
              "lejos de mí la ira y el furor sin razón.",
    (16, 11): "Aparta de mí la murmuración y el desaliento en la aflicción, si "
              "peco cuando tú me corriges para hacerme volver.",
    (16, 12): "Afianza mi alma con benevolencia y alegría; cuando tú fortalezcas "
              "mi alma, me bastará lo que se me dé.",
    (16, 13): "Porque, si tú no fortaleces, ¿quién aguantará la corrección en "
              "la pobreza,",
    (16, 14): "cuando el alma es probada por medio de la carne que se corrompe? "
              "Tu prueba está en su carne y en la aflicción de la pobreza.",
    (16, 15): "Himno de Salomón, sobre el auxilio a los santos. Si el justo "
              "soporta estas cosas, alcanzará misericordia del Señor.",

    (17, 1): "Señor, tú eres nuestro rey para siempre y para siempre jamás, "
             "porque en ti, Dios nuestro, se gloriará nuestra alma.",
    (17, 2): "¿Y cuánto es el tiempo de la vida del hombre sobre la tierra? "
             "Según su tiempo, así es su esperanza.",
    (17, 3): "Pero nosotros esperaremos en Dios, nuestro salvador, porque el "
             "poder de nuestro Dios es para siempre, con misericordia,",
    (17, 4): "y el reino de nuestro Dios es para siempre sobre las naciones.",
    (17, 5): "Tú, Señor, escogiste a David como rey sobre Israel, y tú le "
             "juraste acerca de su descendencia para siempre, que no faltaría "
             "delante de ti su reinado.",
    (17, 6): "Pero por nuestros pecados se levantaron contra nosotros los "
             "pecadores; se echaron sobre nosotros y nos expulsaron; lo que no "
             "les habías prometido, lo tomaron por la fuerza,",
    (17, 7): "y no glorificaron tu nombre venerable; con pompa establecieron "
             "un reino en lugar de su propia grandeza;",
    (17, 8): "dejaron desierto el trono de David con la soberbia de una "
             "usurpación. Pero tú, oh Dios, los derribarás, y quitarás su "
             "descendencia de la tierra,",
    (17, 9): "levantando contra ellos a un hombre ajeno a nuestro linaje.",
    (17, 10): "Conforme a sus pecados les pagarás, oh Dios, para que reciban "
              "conforme a sus obras.",
    (17, 11): "No tendrá Dios misericordia de ellos; rastreó su descendencia y "
              "no dejó de ellos ni a uno.",
    (17, 12): "Fiel es el Señor en todos los juicios que hace sobre la tierra.",
    (17, 13): "Dejó el inicuo desierta nuestra tierra, sin habitantes; "
              "aniquilaron a jóvenes y a ancianos y a sus niños a la vez.",
    (17, 14): "En el furor de su hermosura los envió hasta el occidente, y a "
              "los príncipes de la tierra los puso en escarnio; y no "
              "perdonó.",
    (17, 15): "Salmo de Salomón, con cántico; al rey. Como un extraño obró el "
              "enemigo, con soberbia; y su corazón era ajeno a nuestro Dios.",
    (17, 16): "E hizo en Jerusalén todo lo que hacen las naciones en sus "
              "ciudades con sus dioses.",
    (17, 17): "Y los hijos de la alianza, en medio de naciones mezcladas, se "
              "impusieron sobre ellos; no había entre ellos, en Jerusalén, "
              "quien obrase misericordia y verdad.",
    (17, 18): "Huyeron de ellos los que amaban las asambleas de los santos; "
              "como pájaros salieron volando de su nido.",
    (17, 19): "Andaban errantes por los desiertos, para salvar su vida del "
              "mal; y era cosa preciosa a los ojos de los desterrados un alma "
              "salvada de ellos.",
    (17, 20): "Por toda la tierra fue su dispersión a manos de los inicuos, "
              "porque el cielo se retuvo y no destiló lluvia sobre la tierra;",
    (17, 21): "las fuentes eternas se cerraron en los abismos y en los montes "
              "altos, porque no había entre ellos quien hiciese justicia y "
              "juicio: desde su príncipe hasta el más pequeño del pueblo, "
              "todos en pecado.",
    (17, 22): "El rey en la transgresión, y el juez en la desobediencia, y el "
              "pueblo en el pecado.",
    (17, 23): "Mira, Señor, y levántales a su rey, hijo de David, en el tiempo "
              "que tú, oh Dios, has señalado, para que reine sobre Israel tu "
              "siervo;",
    (17, 24): "y cíñelo de fuerza para quebrantar a los príncipes injustos.",
    (17, 25): "Limpia a Jerusalén de las naciones que la pisotean para "
              "destruirla, con sabiduría y con justicia;",
    (17, 26): "para echar a los pecadores de la heredad, para triturar la "
              "soberbia del pecador como vasija de alfarero, para quebrar con "
              "vara de hierro toda su consistencia;",
    (17, 27): "para destruir a las naciones sin ley con la palabra de su boca; "
              "para que, ante su amenaza, huyan las naciones de su presencia; "
              "y para dejar en evidencia a los pecadores con la palabra de su "
              "corazón.",
    (17, 28): "Y reunirá un pueblo santo al que guiará con justicia, y juzgará "
              "a las tribus del pueblo santificado por el Señor su Dios.",
    (17, 29): "Y no dejará que la injusticia se hospede más entre ellos, ni "
              "habitará con ellos hombre alguno que conozca la maldad;",
    (17, 30): "porque los conocerá, y sabrá que todos son hijos de su Dios, y "
              "los repartirá según sus tribus sobre la tierra.",
    (17, 31): "Y no morará ya entre ellos forastero ni extranjero; juzgará a "
              "los pueblos y a las naciones con la sabiduría de su justicia. "
              "Pausa.",
    (17, 32): "Y tendrá a pueblos de naciones sirviéndole bajo su yugo, y "
              "glorificará al Señor a la vista de toda la tierra.",
    (17, 33): "Y limpiará a Jerusalén en santidad, como lo era desde el "
              "principio,",
    (17, 34): "de modo que vengan las naciones desde el extremo de la tierra a "
              "ver su gloria, trayendo como dones a los hijos de ella que "
              "estaban agotados,",
    (17, 35): "y a ver la gloria del Señor, con la que Dios la glorificó. Y él "
              "será un rey justo, enseñado por Dios, sobre ellos;",
    (17, 36): "y no habrá injusticia en sus días en medio de ellos, porque "
              "todos serán santos, y su rey será el Cristo Señor.",
    (17, 37): "Porque no pondrá su esperanza en el caballo ni en el jinete ni "
              "en el arco, ni acumulará oro ni plata para la guerra; ni "
              "reunirá esperanzas en una multitud para el día de la batalla.",
    (17, 38): "El Señor mismo es su rey; la esperanza del fuerte está en la "
              "esperanza de Dios; y tendrá misericordia de todas las naciones "
              "que estén delante de él con temor.",
    (17, 39): "Porque someterá la tierra con la palabra de su boca para "
              "siempre;",
    (17, 40): "bendecirá al pueblo del Señor con sabiduría y con alegría.",
    (17, 41): "Y él mismo estará limpio de pecado, para gobernar a pueblos "
              "grandes, para reprender a los príncipes y para quitar a los "
              "pecadores con la fuerza de su palabra.",
    (17, 42): "Y no desfallecerá en sus días apoyado en su Dios, porque Dios "
              "lo hizo fuerte en el espíritu santo, y sabio en el consejo de "
              "la inteligencia, con fortaleza y justicia.",
    (17, 43): "Y la bendición del Señor está con él, con poder;",
    (17, 44): "y no desfallecerá su esperanza en el Señor. Y ¿quién podrá "
              "contra él, fuerte en sus obras y poderoso en el temor de Dios,",
    (17, 45): "apacentando el rebaño del Señor con fe y con justicia, sin "
              "dejar que ninguno de ellos desfallezca en su pasto?",
    (17, 46): "A todos los llevará con equidad, y no habrá entre ellos "
              "soberbia que oprima a ninguno.",
    (17, 47): "Ésta es la hermosura del rey de Israel, la que conoció Dios "
              "cuando decidió levantarlo sobre la casa de Israel para "
              "corregirla.",
    (17, 48): "Sus palabras están acrisoladas más que el oro más fino; en las "
              "asambleas juzgará a las tribus del pueblo santificado;",
    (17, 49): "sus palabras son como palabras de santos en medio de pueblos "
              "santificados.",
    (17, 50): "Dichosos los que vivan en aquellos días y vean los bienes de "
              "Israel en la reunión de las tribus. Que Dios lo cumpla.",
    (17, 51): "Apresure Dios su misericordia sobre Israel; nos librará de la "
              "impureza de enemigos profanos. El Señor mismo es nuestro rey "
              "para siempre y para siempre jamás.",

    (18, 1): "Señor, tu misericordia está sobre las obras de tus manos para "
             "siempre;",
    (18, 2): "tu bondad, con don abundante, está sobre Israel; tus ojos velan "
             "sobre ellos, y no faltará nada de lo suyo;",
    (18, 3): "tus oídos escuchan la súplica esperanzada del pobre; tus juicios "
             "están sobre toda la tierra con misericordia,",
    (18, 4): "y tu amor sobre la descendencia de Abrahán, los hijos de Israel. "
             "Tu corrección está sobre nosotros como sobre un hijo "
             "primogénito y único,",
    (18, 5): "para apartar del desatino al alma dócil que yerra por "
             "ignorancia.",
    (18, 6): "Purifique Dios a Israel para el día de la misericordia con "
             "bendición, para el día de la elección, cuando levante a su "
             "Cristo.",
    (18, 7): "Dichosos los que vivan en aquellos días y vean los bienes del "
             "Señor, los que hará para la generación que ha de venir,",
    (18, 8): "bajo la vara de corrección del Cristo del Señor, en el temor de "
             "su Dios, con la sabiduría del espíritu y de la justicia y de la "
             "fortaleza,",
    (18, 9): "para enderezar a los hombres en obras de justicia con el temor "
             "de Dios, y para ponerlos a todos delante del Señor.",
    (18, 10): "Generación buena, en el temor de Dios, en los días de la "
              "misericordia. Pausa.",
    (18, 11): "Grande es nuestro Dios y glorioso, y habita en las alturas;",
    (18, 12): "él es quien dispuso en su curso las lumbreras para marcar las "
              "estaciones de día en día; y no se apartaron del camino que les "
              "mandaste.",
    (18, 13): "En el temor de Dios va su camino cada día, desde el día en que "
              "Dios los creó y para siempre.",
    (18, 14): "Y no se extraviaron desde el día en que los creó; desde las "
              "generaciones antiguas no se apartaron de sus caminos, si no es "
              "cuando Dios se lo mandó por orden de sus siervos.",
    (18, 51): "Salmo de Salomón, todavía sobre el Cristo del Señor.",
}
