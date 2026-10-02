"""1 Esdras en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Es el libro más
raro de esta colección: cuenta otra vez, en griego y con otro orden, lo que ya
está en 2 Crónicas 35-36, en Esdras entero y en Nehemías 8. No es una
traducción del hebreo que conocemos, sino una obra aparte, y por eso vale la
pena tenerla: donde difiere del texto masorético, la diferencia es el dato.

Lo que sólo está aquí es el capítulo 3 y buena parte del 4: el certamen de los
tres jóvenes de la guardia de Darío sobre qué es lo más fuerte del mundo. Uno
dice que el vino, otro que el rey, y el tercero —Zorobabel— que las mujeres,
«pero por encima de todo vence la verdad». De ahí sale la frase que acabó en
tantas paredes: «Grande es la verdad, y prevalece». Ese pasaje no tiene
paralelo hebreo en ninguna parte.

El otro interés es que aquí Esdras lee la ley al pueblo (capítulo 9) como en
Nehemías 8, pero encajado en otro sitio de la historia: los dos relatos juntos
muestran que la memoria del regreso del destierro se contaba de más de una
manera.

Sobre los nombres: el griego llama Ἰωακείμ tanto al rey puesto por Egipto como
a su hijo, que reinó tres meses y diez días. Aquí se distinguen como Joacim
(el padre) y Joaquín (el hijo), porque si no no se sabe quién es quién; y el
hijo de Josías a quien el griego llama Ἰεχονίας es el que en Reyes se llama
Joacaz. Se conserva la forma griega y se avisa aquí, en vez de corregir el
texto por dentro. Por lo mismo se deja el 5:145 donde el texto lo pone: es el
versículo 47, mal numerado en esta edición griega.
"""

from __future__ import annotations

ESDRAS1_ES: dict[tuple[int, int], str] = {
    (1, 1): "Y celebró Josías la pascua en Jerusalén a su Señor, e "
            "inmolaron la pascua el día catorce del mes primero,",
    (1, 2): "después de poner a los sacerdotes por turnos, revestidos, en el "
            "templo del Señor.",
    (1, 3): "Y dijo a los levitas, servidores del templo de Israel, que se "
            "santificasen al Señor para colocar el arca santa del Señor en la "
            "casa que edificó el rey Salomón, hijo de David:",
    (1, 4): "«Ya no tendréis que llevarla a hombros. Y ahora servid al Señor "
            "vuestro Dios y atended a su pueblo Israel, y preparaos por "
            "familias y por tribus, conforme a lo escrito por David rey de "
            "Israel y conforme a la magnificencia de Salomón su hijo;",
    (1, 5): "y, puestos en el santuario según la división por familias de "
            "vosotros los levitas, que estáis delante de vuestros hermanos los "
            "hijos de Israel,",
    (1, 6): "por orden, inmolad la pascua y preparad los sacrificios para "
            "vuestros hermanos, y celebrad la pascua conforme al mandato del "
            "Señor que se dio a Moisés».",
    (1, 7): "Y regaló Josías al pueblo que allí se encontraba treinta mil "
            "corderos y cabritos y tres mil terneros; esto se dio al pueblo y "
            "a los sacerdotes y a los levitas de los bienes del rey, según lo "
            "prometido.",
    (1, 8): "Y dieron Jelcías y Zacarías y Esielo, los encargados del templo, "
            "a los sacerdotes, para la pascua, dos mil seiscientas ovejas y "
            "trescientos terneros.",
    (1, 9): "Y Jeconías y Semeías y Natanael su hermano, y Sabías y Oquielo y "
            "Joram, jefes de mil, dieron a los levitas, para la pascua, mil "
            "ovejas y setecientos terneros.",
    (1, 10): "Y así ocurrieron las cosas: se pusieron en orden los sacerdotes "
             "y los levitas, con los panes ázimos, por tribus y por divisiones "
             "de familias, delante del pueblo, para presentar la ofrenda al "
             "Señor conforme a lo escrito en el libro de Moisés; y así se hizo "
             "por la mañana.",
    (1, 11): "Y asaron la pascua al fuego como está mandado, y cocieron los "
             "sacrificios en calderos y ollas con buen olor, y los repartieron "
             "a toda la gente del pueblo.",
    (1, 12): "Y después de esto prepararon para sí mismos y para sus hermanos "
             "los sacerdotes, hijos de Aarón;",
    (1, 13): "porque los sacerdotes estuvieron ofreciendo las grasas hasta "
             "entrada la noche, y los levitas prepararon para sí mismos y para "
             "sus hermanos los sacerdotes, hijos de Aarón.",
    (1, 14): "Y los cantores sagrados, hijos de Asaf, estaban en su puesto "
             "según lo dispuesto por David: Asaf y Zacarías y Edinús, los del "
             "rey.",
    (1, 15): "Y los porteros, cada uno en su puerta; ninguno tenía que dejar "
             "su turno, porque sus hermanos los levitas prepararon para "
             "ellos.",
    (1, 16): "Y se cumplió todo lo del sacrificio del Señor en aquel día, "
             "celebrándose la pascua y ofreciéndose los sacrificios sobre el "
             "altar del Señor, conforme al mandato del rey Josías.",
    (1, 17): "Y los hijos de Israel que allí se encontraban celebraron la "
             "pascua y la fiesta de los ázimos siete días.",
    (1, 18): "Y no se celebró en Israel una pascua como ésta desde los tiempos "
             "del profeta Samuel;",
    (1, 19): "y ninguno de los reyes de Israel celebró una pascua como la que "
             "celebró Josías con los sacerdotes y los levitas y los judíos y "
             "todo Israel que se hallaba residiendo en Jerusalén.",
    (1, 20): "El año dieciocho del reinado de Josías se celebró esta pascua.",
    (1, 21): "Y las obras de Josías fueron rectas delante de su Señor, con un "
             "corazón lleno de piedad.",
    (1, 22): "Y lo que a él se refiere está escrito en los tiempos pasados, "
             "acerca de los que pecaron y obraron impíamente contra el Señor "
             "más que ninguna otra nación y reino, y de lo que le causó "
             "dolor; y las palabras del Señor se alzaron contra Israel.",
    (1, 23): "Y después de toda esta obra de Josías, sucedió que el faraón, "
             "rey de Egipto, vino a promover guerra en Carquemis, junto al "
             "Éufrates; y Josías salió a su encuentro.",
    (1, 24): "Y le mandó decir el rey de Egipto: «¿Qué tengo yo contigo, rey "
             "de Judea?",
    (1, 25): "No he sido enviado contra ti por el Señor Dios, porque mi guerra "
             "es junto al Éufrates. Y ahora el Señor está conmigo, y el Señor "
             "me apremia: apártate y no te opongas al Señor».",
    (1, 26): "Pero Josías no se volvió a su carro, sino que se empeñó en "
             "pelear contra él, sin atender a las palabras del profeta "
             "Jeremías dichas de parte del Señor;",
    (1, 27): "sino que le presentó batalla en la llanura de Meguido, y "
             "bajaron los jefes contra el rey Josías.",
    (1, 28): "Y dijo el rey a sus siervos: «Sacadme de la batalla, porque "
             "estoy muy mal herido». Y al punto lo sacaron sus siervos de la "
             "línea de combate,",
    (1, 29): "y subió a su segundo carro; y devuelto a Jerusalén, cambió esta "
             "vida por la otra, y fue sepultado en el sepulcro de sus padres.",
    (1, 30): "Y en toda Judea hicieron duelo por Josías; y lo lloró el profeta "
             "Jeremías, y los principales, con sus mujeres, lo han llorado "
             "hasta el día de hoy; y se estableció que esto se hiciera siempre "
             "en todo el linaje de Israel.",
    (1, 31): "Y esto está escrito en el libro de las historias de los reyes de "
             "Judea; y cada uno de los hechos de Josías, y su gloria, y su "
             "inteligencia en la ley del Señor, y lo que hizo, y lo que ahora "
             "se ha contado, está registrado en el libro de los reyes de "
             "Israel y de Judá.",
    (1, 32): "Y los del pueblo tomaron a Jeconías, hijo de Josías, y lo "
             "proclamaron rey en lugar de Josías su padre, cuando tenía "
             "veintitrés años.",
    (1, 33): "Y reinó en Israel y en Jerusalén tres meses; y lo depuso el rey "
             "de Egipto para que no reinase en Jerusalén,",
    (1, 34): "e impuso a la nación una multa de cien talentos de plata y un "
             "talento de oro.",
    (1, 35): "Y el rey de Egipto proclamó rey de Judea y de Jerusalén a Joacim "
             "su hermano.",
    (1, 36): "Y Joacim encadenó a los magnates; y a Zarío, su hermano, lo "
             "prendió y lo hizo subir desde Egipto.",
    (1, 37): "Tenía veinticinco años Joacim cuando empezó a reinar sobre Judea "
             "y Jerusalén, e hizo lo malo delante del Señor.",
    (1, 38): "Y contra él subió Nabucodonosor, rey de Babilonia, y lo ató con "
             "cadenas de bronce y lo llevó a Babilonia.",
    (1, 39): "Y Nabucodonosor tomó de los vasos sagrados del Señor y, "
             "lleván­doselos, los depositó en su templo en Babilonia.",
    (1, 40): "Y lo que se cuenta de él, y de su impureza y de su impiedad, "
             "está escrito en el libro de las crónicas de los reyes.",
    (1, 41): "Y reinó en su lugar Joaquín su hijo; porque, cuando fue "
             "proclamado, tenía ocho años.",
    (1, 42): "Y reinó tres meses y diez días en Jerusalén, e hizo lo malo "
             "delante del Señor.",
    (1, 43): "Y al cabo de un año, Nabucodonosor mandó llevarlo a Babilonia "
             "junto con los vasos sagrados del Señor,",
    (1, 44): "y proclamó rey de Judea y de Jerusalén a Sedecías, que tenía "
             "veintiún años; y reinó once años.",
    (1, 45): "E hizo lo malo delante del Señor, y no se dejó conmover por las "
             "palabras dichas por el profeta Jeremías de parte del Señor.",
    (1, 46): "Y habiéndole tomado juramento el rey Nabucodonosor por el nombre "
             "del Señor, perjuró y se rebeló; y endureciendo su cerviz y su "
             "corazón, traspasó las leyes del Señor Dios de Israel.",
    (1, 47): "Y también los jefes del pueblo y de los sacerdotes cometieron "
             "muchas impiedades e iniquidades, más que todas las impurezas de "
             "todas las naciones, y profanaron el templo del Señor, el "
             "santificado en Jerusalén.",
    (1, 48): "Y el Dios de sus padres envió por medio de su mensajero a "
             "llamarlos, porque tenía compasión de ellos y de su morada.",
    (1, 49): "Pero ellos se burlaron de sus mensajeros, y el día en que habló "
             "el Señor se reían de sus profetas, hasta que él, airado contra "
             "su nación por aquellas impiedades, mandó que subieran contra "
             "ellos los reyes de los caldeos.",
    (1, 50): "Éstos mataron a sus jóvenes a espada en torno al santo templo, y "
             "no perdonaron a joven ni a doncella ni a anciano ni a muchacho, "
             "sino que a todos los entregó en sus manos,",
    (1, 51): "y tomaron todos los vasos sagrados del Señor, grandes y "
             "pequeños, y las arcas del Señor y los tesoros reales, y se los "
             "llevaron a Babilonia.",
    (1, 52): "Y quemaron la casa del Señor, y derribaron las murallas de "
             "Jerusalén, y prendieron fuego a sus torres,",
    (1, 53): "y acabaron de arruinar todo lo que en ella era glorioso; y a los "
             "que quedaron se los llevó a Babilonia a punta de espada.",
    (1, 54): "Y fueron sus esclavos, de él y de sus hijos, hasta que reinaron "
             "los persas, para que se cumpliese la palabra del Señor dicha por "
             "boca de Jeremías:",
    (1, 55): "«Hasta que la tierra haya disfrutado de sus sábados, reposará "
             "todo el tiempo de su desolación, hasta cumplirse setenta años».",

    (2, 1): "En el año primero del reinado de Ciro, rey de los persas, para "
            "que se cumpliese la palabra del Señor dicha por boca de "
            "Jeremías,",
    (2, 2): "despertó el Señor el espíritu de Ciro, rey de los persas, y éste "
            "proclamó en todo su reino, y también por escrito, lo siguiente:",
    (2, 3): "«Así dice Ciro, rey de los persas: A mí me ha proclamado rey de "
            "la tierra habitada el Señor de Israel, el Señor Altísimo,",
    (2, 4): "y me ha encargado que le edifique una casa en Jerusalén, la que "
            "está en Judea.",
    (2, 5): "Si hay, pues, alguno de vosotros que sea de su pueblo, sea su "
            "Señor con él, y suba a Jerusalén, la que está en Judea, y "
            "edifique la casa del Señor de Israel; él es el Señor que habita "
            "en Jerusalén.",
    (2, 6): "Y cuantos residen en aquellos lugares, ayúdenle los de su lugar "
            "con oro y con plata y con donativos, con caballos y con ganados, "
            "junto con las demás cosas ofrecidas por voto para el templo del "
            "Señor que está en Jerusalén».",
    (2, 7): "Y se pusieron en pie los jefes de familia de la tribu de Judá y "
            "de Benjamín, y los sacerdotes y los levitas, y todos aquellos "
            "cuyo espíritu despertó el Señor para subir a edificar al Señor la "
            "casa que está en Jerusalén;",
    (2, 8): "y los que vivían alrededor de ellos los ayudaron en todo: con "
            "plata y oro, caballos, ganados y ofrendas votivas en gran "
            "abundancia, muchos cuyo ánimo fue movido.",
    (2, 9): "Y el rey Ciro sacó los vasos sagrados del Señor, los que "
            "Nabucodonosor se había llevado de Jerusalén y había depositado en "
            "el templo de su ídolo.",
    (2, 10): "Y sacándolos, Ciro rey de los persas los entregó a Mitrídates, "
             "su tesorero;",
    (2, 11): "y por medio de éste fueron entregados a Sanabasar, gobernador de "
             "Judea.",
    (2, 12): "Y el número de ellos era: copas de oro para libaciones, mil; "
             "copas de plata para libaciones, mil; incensarios de plata, "
             "veintinueve; tazas de oro, treinta; de plata, dos mil "
             "cuatrocientas diez; y otros vasos, mil.",
    (2, 13): "Y todos los vasos que se llevaron, de oro y de plata, fueron "
             "cinco mil cuatrocientos sesenta y nueve;",
    (2, 14): "y fueron subidos por Sanabasar junto con los que volvían del "
             "cautiverio, de Babilonia a Jerusalén.",
    (2, 15): "Pero en los tiempos de Artajerjes, rey de los persas, "
             "escribieron contra los que habitaban en Judea y en Jerusalén "
             "—Bélemo y Mitrídates y Tabelio y Rátimo y Beeltetmo y Samelio "
             "el escriba, y los demás que con ellos se concertaban, "
             "habitantes de Samaria y de otros lugares— la carta que sigue:",
    (2, 16): "«Al rey Artajerjes, nuestro señor: tus siervos Rátimo, encargado "
             "de los asuntos corrientes, y Samelio el escriba, y los demás de "
             "su consejo, y los de Celesiria y Fenicia.",
    (2, 17): "Sepa ahora el rey nuestro señor que los judíos que subieron de "
             "vuestra tierra hasta nosotros, llegados a Jerusalén, están "
             "habitando aquella ciudad rebelde y perversa, y están reparando "
             "sus plazas y sus murallas, y echando los cimientos de un "
             "templo.",
    (2, 18): "Y si esa ciudad se edifica y se acaban sus murallas, no "
             "soportarán pagar tributo, sino que hasta se opondrán a los "
             "reyes; y como ya se trabaja en lo del templo, nos parece bien no "
             "desatender un asunto así, sino avisar al rey nuestro señor para "
             "que, si te parece, se busque en los libros de tus padres.",
    (2, 19): "Y hallarás en las crónicas lo que está escrito acerca de esto, y "
             "sabrás que aquella ciudad fue rebelde e inquietó a reyes y a "
             "ciudades, y que los judíos son rebeldes y desde antiguo han "
             "organizado en ella asedios; y por esa causa fue arrasada aquella "
             "ciudad.",
    (2, 20): "Ahora, pues, te advertimos, señor rey, que, si esa ciudad se "
             "edifica y se levantan sus murallas, ya no tendrás paso hacia "
             "Celesiria y Fenicia».",
    (2, 21): "Entonces el rey respondió por escrito a Rátimo, el encargado de "
             "los asuntos corrientes, y a Beeltetmo y a Samelio el escriba y a "
             "los demás que con ellos se concertaban y habitaban en Samaria y "
             "en Siria y en Fenicia, lo siguiente:",
    (2, 22): "«He leído la carta que me habéis enviado. Mandé, pues, que se "
             "hiciera una averiguación; y se halló que aquella ciudad desde "
             "antiguo se ha enfrentado a los reyes,",
    (2, 23): "y que aquellos hombres promueven en ella rebeliones y guerras, y "
             "que hubo en Jerusalén reyes fuertes y duros que dominaron y "
             "cobraron tributo en Celesiria y Fenicia.",
    (2, 24): "Ahora, pues, he mandado impedir a aquellos hombres que edifiquen "
             "la ciudad, y que se tenga cuidado de que no se haga nada más en "
             "ese sentido, y de que ese mal no vaya a más hasta llegar a "
             "inquietar a los reyes».",
    (2, 25): "Entonces, leído lo escrito por el rey Artajerjes, Rátimo y "
             "Samelio el escriba y los que con ellos se concertaban partieron "
             "a toda prisa hacia Jerusalén con caballería y con una tropa "
             "formada, y empezaron a impedir a los que edificaban. Y la "
             "construcción del templo que está en Jerusalén quedó parada hasta "
             "el año segundo del reinado de Darío, rey de los persas.",

    (3, 1): "Y el rey Darío dio un gran banquete a todos sus súbditos, y a "
            "todos los nacidos en su casa, y a todos los magnates de Media y "
            "de Persia,",
    (3, 2): "y a todos los sátrapas y generales y gobernadores que estaban "
            "bajo su mando, desde la India hasta Etiopía, en las ciento "
            "veintisiete satrapías.",
    (3, 3): "Y comieron y bebieron, y una vez saciados se retiraron; y el rey "
            "Darío se retiró a su alcoba y se acostó, y se despertó.",
    (3, 4): "Entonces los tres jóvenes de la guardia, los que custodiaban la "
            "persona del rey, se dijeron unos a otros:",
    (3, 5): "«Diga cada uno de nosotros una frase sobre lo que es más fuerte; "
            "y a aquel cuya palabra parezca más sabia que la de los otros, el "
            "rey Darío le dará grandes regalos y grandes premios de victoria:",
    (3, 6): "vestirse de púrpura, y beber en vajilla de oro, y dormir sobre "
            "oro, y un carro con frenos de oro, y un turbante de lino fino y "
            "un collar al cuello;",
    (3, 7): "y se sentará como segundo después de Darío por su sabiduría, y "
            "será llamado pariente de Darío».",
    (3, 8): "Y entonces, escribiendo cada uno su frase, la sellaron y la "
            "pusieron bajo la almohada del rey Darío, y dijeron:",
    (3, 9): "«Cuando el rey se levante, le entregarán el escrito; y aquel de "
            "quien el rey y los tres magnates de Persia juzguen que su palabra "
            "es la más sabia, a ése se le dará la victoria, conforme está "
            "escrito».",
    (3, 10): "El uno escribió: «Lo más fuerte es el vino».",
    (3, 11): "El otro escribió: «Lo más fuerte es el rey».",
    (3, 12): "El tercero escribió: «Lo más fuerte son las mujeres; pero por "
             "encima de todo vence la verdad».",
    (3, 13): "Y cuando el rey despertó, tomaron el escrito y se lo dieron, y "
             "lo leyó.",
    (3, 14): "Y enviando recado, llamó a todos los magnates de Persia y de "
             "Media, y a los sátrapas y generales y gobernadores y cónsules; y "
             "se sentó en la sala del consejo, y se leyó el escrito delante de "
             "ellos.",
    (3, 15): "Y dijo: «Llamad a los jóvenes, y que ellos expliquen sus "
             "palabras». Y los llamaron, y entraron.",
    (3, 16): "Y les dijeron: «Explicadnos lo que habéis escrito». Y empezó el "
             "primero, el que había hablado de la fuerza del vino, y dijo "
             "así:",
    (3, 17): "«Señores, ¡qué fuerte es el vino! A todos los hombres que lo "
             "beben les trastorna el juicio:",
    (3, 18): "hace del rey y del huérfano un mismo juicio, y del esclavo y del "
             "libre, y del pobre y del rico;",
    (3, 19): "y todo pensamiento lo vuelve en fiesta y alegría, y ya no se "
             "acuerda uno de ninguna tristeza ni de ninguna deuda;",
    (3, 20): "y hace ricos a todos los corazones, y ya no se acuerda uno del "
             "rey ni del sátrapa, y hace que todos hablen por talentos;",
    (3, 21): "y, cuando beben, no se acuerdan de guardar amistad con los "
             "amigos ni con los hermanos, y al poco desenvainan las espadas;",
    (3, 22): "y cuando se les pasa el vino, no se acuerdan de lo que "
             "hicieron.",
    (3, 23): "Señores, ¿no es el vino lo más fuerte, si de tal manera obliga a "
             "obrar?». Y habiendo hablado así, calló.",

    (4, 1): "Y empezó a hablar el segundo, el que había hablado de la fuerza "
            "del rey:",
    (4, 2): "«Señores, ¿no son lo más fuerte los hombres, que dominan la "
            "tierra y el mar y todo lo que hay en ellos?",
    (4, 3): "Pues el rey es más fuerte todavía, y los manda y los domina, y "
            "todo cuanto les dice lo obedecen.",
    (4, 4): "Si les dice que se hagan la guerra unos a otros, la hacen; y si "
            "los envía contra los enemigos, van y arrasan montes y murallas y "
            "torres.",
    (4, 5): "Matan y mueren, y no traspasan la palabra del rey; y si vencen, "
            "todo se lo llevan al rey, tanto el botín como todo lo demás.",
    (4, 6): "Y cuantos no van al ejército ni pelean, sino que labran la "
            "tierra, otra vez, cuando siembran y siegan, llevan la cosecha al "
            "rey; y forzándose unos a otros, le llevan los tributos al rey.",
    (4, 7): "Y él, siendo uno solo, si dice «matad», matan; si dice «soltad», "
            "sueltan;",
    (4, 8): "si dice «herid», golpean; si dice «arrasad», arrasan; si dice "
            "«edificad», edifican;",
    (4, 9): "si dice «talad», talan; si dice «plantad», plantan;",
    (4, 10): "y todo su pueblo y sus ejércitos obedecen. Y con todo esto, él "
             "está recostado, come y bebe y duerme;",
    (4, 11): "y ellos hacen guardia alrededor de él, y ninguno puede irse a "
             "hacer sus propias tareas, ni le desobedecen.",
    (4, 12): "Señores, ¿cómo no va a ser el rey lo más fuerte, si de tal modo "
             "es obedecido?». Y calló.",
    (4, 13): "Y el tercero, el que había hablado de las mujeres y de la verdad "
             "—éste es Zorobabel—, empezó a hablar:",
    (4, 14): "«Señores: ¿no es grande el rey, y muchos los hombres, y fuerte "
             "el vino? ¿Quién es, pues, el que los domina, o quién el que los "
             "gobierna? ¿No son las mujeres?",
    (4, 15): "Las mujeres dieron a luz al rey y a todo el pueblo que domina el "
             "mar y la tierra;",
    (4, 16): "de ellas nacieron, y ellas criaron a los que plantaron las viñas "
             "de donde sale el vino;",
    (4, 17): "y ellas hacen los vestidos de los hombres, y ellas les dan honra "
             "a los hombres, y los hombres no pueden existir sin las mujeres.",
    (4, 18): "Y si juntan oro y plata y toda cosa hermosa, y ven a una sola "
             "mujer bella de figura y de rostro, dejándolo todo se quedan "
             "boquiabiertos ante ella, y con la boca abierta se la quedan "
             "mirando, y todos la prefieren a ella antes que al oro y a la "
             "plata y a cualquier cosa hermosa.",
    (4, 20): "Un hombre abandona a su propio padre, que lo crió, y a su propia "
             "tierra, y se une a su mujer;",
    (4, 21): "y con la mujer entrega la vida, y no se acuerda ni del padre ni "
             "de la madre ni de la tierra.",
    (4, 22): "Y de aquí tenéis que concluir que las mujeres os dominan: ¿no os "
             "afanáis y os fatigáis, y todo se lo dais y se lo lleváis a las "
             "mujeres?",
    (4, 23): "Y toma un hombre su espada y sale a echarse al camino y a robar "
             "y a hurtar, y a navegar por el mar y por los ríos;",
    (4, 24): "y ve al león, y anda en la oscuridad; y cuando ha robado y "
             "saqueado y desvalijado, se lo lleva a la que ama.",
    (4, 25): "Y ama el hombre a su mujer más que al padre y a la madre.",
    (4, 26): "Y muchos perdieron el juicio por causa de las mujeres, y se "
             "hicieron esclavos por ellas;",
    (4, 27): "y muchos perecieron y tropezaron y pecaron por causa de las "
             "mujeres.",
    (4, 28): "¿Y ahora no me creéis? ¿No es grande el rey en su poder? ¿No "
             "temen todas las provincias tocarlo?",
    (4, 29): "Pues yo lo vi a él y a Apame, la hija del admirable Bártaco, la "
             "concubina del rey, sentada a la derecha del rey,",
    (4, 30): "y quitándole la diadema de la cabeza al rey y poniéndosela ella; "
             "y le daba bofetadas al rey con la mano izquierda.",
    (4, 31): "Y con todo esto el rey se la quedaba mirando con la boca "
             "abierta; y si ella le sonreía, él reía; y si se enfadaba con él, "
             "él la halagaba para que se reconciliase con él.",
    (4, 32): "Señores, ¿cómo no van a ser fuertes las mujeres, si así se "
             "comportan?».",
    (4, 33): "Y entonces el rey y los magnates se miraban unos a otros. Y él "
             "empezó a hablar de la verdad:",
    (4, 34): "«Señores: ¿no son fuertes las mujeres? Grande es la tierra, y "
             "alto el cielo, y veloz en su carrera el sol, que da la vuelta "
             "por el círculo del cielo y vuelve corriendo a su propio lugar en "
             "un solo día.",
    (4, 35): "¿No es grande el que hace estas cosas? Pues también la verdad es "
             "grande, y más fuerte que todas las cosas.",
    (4, 36): "Toda la tierra invoca a la verdad, y el cielo la bendice, y "
             "todas las obras se estremecen y tiemblan, y no hay en ella nada "
             "injusto.",
    (4, 37): "Injusto es el vino, injusto el rey, injustas las mujeres, "
             "injustos todos los hijos de los hombres e injustas todas sus "
             "obras, todas las cosas de esa clase; y no hay en ellas verdad, y "
             "en su injusticia perecerán.",
    (4, 38): "Pero la verdad permanece y tiene fuerza para siempre, y vive y "
             "reina por los siglos de los siglos.",
    (4, 39): "Y en ella no hay acepción de personas ni diferencias, sino que "
             "hace lo justo apartándose de todos los injustos y malvados; y "
             "todos aprueban sus obras,",
    (4, 40): "y no hay en su juicio nada injusto. Y de ella es la fuerza y el "
             "reino y el poder y la majestad de todos los siglos. ¡Bendito sea "
             "el Dios de la verdad!».",
    (4, 41): "Y dejó de hablar; y entonces todo el pueblo clamó y dijo: "
             "«¡Grande es la verdad, y es lo más fuerte!».",
    (4, 42): "Entonces el rey le dijo: «Pide lo que quieras, más de lo "
             "escrito, y te lo daremos, ya que has sido hallado el más sabio; "
             "y te sentarás a mi lado, y serás llamado pariente mío».",
    (4, 43): "Entonces él dijo al rey: «Acuérdate del voto que hiciste de "
             "edificar Jerusalén el día en que recibiste tu reino,",
    (4, 44): "y de enviar allá todos los vasos que fueron tomados de Jerusalén "
             "y que Ciro apartó cuando hizo voto de arrasar Babilonia, y que "
             "prometió enviar allá.",
    (4, 45): "Y tú hiciste voto de reedificar el templo que quemaron los "
             "idumeos cuando Judea fue asolada por los caldeos.",
    (4, 46): "Y ahora esto es lo que pido, señor rey, y esto es lo que te "
             "solicito, y ésta es la magnanimidad que espero de ti: te ruego, "
             "pues, que cumplas el voto que con tu propia boca hiciste al Rey "
             "del cielo».",
    (4, 47): "Entonces el rey Darío se levantó y lo besó, y le escribió cartas "
             "para todos los administradores y gobernadores y generales y "
             "sátrapas, para que lo escoltasen a él y a todos los que con él "
             "subían a edificar Jerusalén.",
    (4, 48): "Y escribió cartas a todos los gobernadores de Celesiria y "
             "Fenicia y a los del Líbano, para que transportasen madera de "
             "cedro desde el Líbano hasta Jerusalén, y para que edificasen con "
             "él la ciudad.",
    (4, 49): "Y escribió, a favor de la libertad de todos los judíos que "
             "subiesen del reino a Judea, que ningún poderoso ni sátrapa ni "
             "gobernador ni administrador se presentase a sus puertas,",
    (4, 50): "y que toda la tierra que ocupasen quedase para ellos libre de "
             "tributo; y que los idumeos dejasen las aldeas de los judíos que "
             "tenían tomadas;",
    (4, 51): "y que para la construcción del templo se diesen cada año veinte "
             "talentos, hasta que estuviera edificado;",
    (4, 52): "y para el altar, holocaustos que se ofreciesen cada día, según "
             "el mandamiento que tienen de ofrecer diecisiete, otros diez "
             "talentos al año;",
    (4, 53): "y que todos los que subiesen de Babilonia a levantar la ciudad "
             "tuviesen libertad, ellos y sus hijos, y todos los sacerdotes que "
             "subieran.",
    (4, 54): "Y escribió también sobre el suministro y sobre la vestidura "
             "sacerdotal con que celebran el culto.",
    (4, 55): "Y escribió que se diera a los levitas el suministro hasta el día "
             "en que se acabase la casa y se edificase Jerusalén.",
    (4, 56): "Y escribió que se diesen a todos los que guardasen la ciudad "
             "lotes de tierra y sueldos.",
    (4, 57): "Y envió todos los vasos que Ciro había apartado de Babilonia; y "
             "todo cuanto Ciro había mandado hacer, también él mandó que se "
             "hiciese y que se enviase a Jerusalén.",
    (4, 58): "Y cuando salió el joven, alzó el rostro al cielo, hacia "
             "Jerusalén, y bendijo al Rey del cielo diciendo:",
    (4, 59): "«De ti viene la victoria, y de ti la sabiduría, y tuya es la "
             "gloria, y yo soy siervo tuyo.",
    (4, 60): "Bendito seas tú, que me diste sabiduría; y a ti te doy gracias, "
             "Señor de los padres».",
    (4, 61): "Y tomó las cartas y salió hacia Babilonia, y se lo contó todo a "
             "sus hermanos.",
    (4, 62): "Y bendijeron al Dios de sus padres, porque les había dado alivio "
             "y licencia",
    (4, 63): "para subir y edificar Jerusalén y el templo sobre el que ha sido "
             "invocado su nombre; y celebraron con música y alegría durante "
             "siete días.",

    (5, 1): "Y después de esto fueron elegidos para subir los jefes de casas "
            "paternas según sus tribus, con sus mujeres y sus hijos y sus "
            "hijas y sus criados, y sus criadas y sus ganados.",
    (5, 2): "Y Darío envió con ellos mil jinetes, hasta devolverlos a "
            "Jerusalén en paz y con música, con panderos y flautas;",
    (5, 3): "y todos sus hermanos iban festejando; y él hizo que subiesen "
            "juntamente con aquéllos.",
    (5, 4): "Y éstos son los nombres de los hombres que subieron, por familias "
            "según sus tribus, conforme a su división:",
    (5, 5): "los sacerdotes, hijos de Fineés, hijos de Aarón: Jesús hijo de "
            "Josedec, hijo de Saraías, y Joacim hijo de Zorobabel, hijo de "
            "Salatiel, de la casa de David, del linaje de Farés, de la tribu "
            "de Judá,",
    (5, 6): "el que pronunció ante Darío, rey de los persas, palabras sabias, "
            "en el año segundo de su reinado, en el mes de Nisán, que es el "
            "mes primero.",
    (5, 7): "Y éstos son los de Judea que subieron del cautiverio del "
            "destierro, a los que Nabucodonosor, rey de Babilonia, había "
            "deportado a Babilonia,",
    (5, 8): "y volvieron a Jerusalén y al resto de Judea, cada uno a su propia "
            "ciudad, los que vinieron con Zorobabel y Jesús, Nehemías, "
            "Zaraías, Resaías, Enenio, Mardoqueo, Beelsaro, Asfáraso, "
            "Borolio, Roimo y Baana, sus guías.",
    (5, 9): "Número de los del pueblo, con sus guías: hijos de Foros, dos mil "
            "ciento setenta y dos;",
    (5, 10): "hijos de Ares, setecientos cincuenta y seis;",
    (5, 11): "hijos de Fatalimoab, de los hijos de Jesús y de Roboab, dos mil "
             "ochocientos doce;",
    (5, 12): "hijos de Jolamo, mil doscientos cincuenta y cuatro; hijos de "
             "Zatón, novecientos setenta; hijos de Corbe, setecientos cinco; "
             "hijos de Baní, seiscientos cuarenta y ocho;",
    (5, 13): "hijos de Bebai, seiscientos treinta y tres; hijos de Argai, mil "
             "trescientos veintidós;",
    (5, 14): "hijos de Adonicam, seiscientos treinta y siete; hijos de Bosai, "
             "dos mil seiscientos seis; hijos de Adelio, cuatrocientos "
             "cincuenta y cuatro;",
    (5, 15): "hijos de Azer, de Ezequías; hijos de Cilán y de Azetas, sesenta "
             "y siete; hijos de Azaro, cuatrocientos treinta y dos;",
    (5, 16): "hijos de Anís, ciento uno; hijos de Arom; hijos de Basai, "
             "trescientos veintitrés; hijos de Arsifurit, ciento dos;",
    (5, 17): "hijos de Beteros, tres mil cinco; los de Ragetlomón, ciento "
             "veintitrés;",
    (5, 18): "los de Netebas, cincuenta y cinco; los de Enato, ciento cincuenta "
             "y ocho; los de Betasmón, cuarenta y dos;",
    (5, 19): "los de Cariatiarim, veinticinco; los de Pira y Berog, "
             "setecientos;",
    (5, 20): "los cadiaseos y los amidios, cuatrocientos veintidós; los de "
             "Cirama y Gabes, seiscientos veintiuno;",
    (5, 21): "los de Macalón, ciento veintidós; los de Betolio, cincuenta y "
             "dos; los hijos de Nifís, ciento cincuenta y seis;",
    (5, 22): "hijos de Calamólalo y de Onús, setecientos veinticinco; hijos de "
             "Jericó, doscientos cuarenta y cinco;",
    (5, 23): "hijos de Sanás, tres mil trescientos uno.",
    (5, 24): "Los sacerdotes: los hijos de Jedú, hijo de Jesús, entre los "
             "hijos de Sanabís, ochocientos setenta y dos; hijos de Ermero, "
             "doscientos cincuenta y dos;",
    (5, 25): "hijos de Fasoro, mil doscientos cuarenta y siete; hijos de "
             "Carme, doscientos diecisiete.",
    (5, 26): "Los levitas: hijos de Jesúe, de Cadmiel y de Bano y de Sudías, "
             "setenta y cuatro.",
    (5, 27): "Los cantores sagrados, hijos de Asaf, ciento veintiocho.",
    (5, 28): "Los porteros: hijos de Salum, hijos de Atar, hijos de Tolmán, "
             "hijos de Dacobi, hijos de Tetí, hijos de Samí, en total ciento "
             "treinta y nueve.",
    (5, 29): "Los servidores del templo: hijos de Esaú, hijos de Gasifá, hijos "
             "de Gabaot, hijos de Queras, hijos de Suá, hijos de Faleo, hijos "
             "de Labaná,",
    (5, 30): "hijos de Acud, hijos de Utá, hijos de Quetab, hijos de Acabá, "
             "hijos de Subai, hijos de Anán, hijos de Cuá, hijos de Cedur,",
    (5, 31): "hijos de Jairo, hijos de Daisán, hijos de Noebá, hijos de "
             "Casebá, hijos de Cazerá, hijos de Ozías, hijos de Finoe, hijos "
             "de Asará, hijos de Bastai, hijos de Asana, hijos de Maní, hijos "
             "de Nafisí, hijos de Acuf, hijos de Aquibá, hijos de Asur, hijos "
             "de Faracem, hijos de Basalem,",
    (5, 32): "hijos de Dedá, hijos de Bacús, hijos de Serar, hijos de Tomtei, "
             "hijos de Nasí, hijos de Atefá.",
    (5, 33): "Hijos de los siervos de Salomón: hijos de Asafiot, hijos de "
             "Faridá, hijos de Jeelí, hijos de Lozón, hijos de Isdael, hijos "
             "de Safuí,",
    (5, 34): "hijos de Aguiá, hijos de Facaret Sabié, hijos de Sarotí, hijos "
             "de Misaías, hijos de Gas, hijos de Adús, hijos de Subás, hijos "
             "de Aferrá, hijos de Barodís, hijos de Safag, hijos de Alón.",
    (5, 35): "Todos los servidores del templo y los hijos de los siervos de "
             "Salomón: trescientos setenta y dos.",
    (5, 36): "Éstos son los que subieron de Termelet y de Telersás; su jefe "
             "era Caratalán, y Alar.",
    (5, 37): "Y no pudieron declarar sus familias ni su linaje, ni si eran de "
             "Israel: hijos de Asán, hijo de Baenán, hijos de Necodán, "
             "seiscientos cincuenta y dos.",
    (5, 38): "Y de los sacerdotes, los que se atribuían el sacerdocio y no "
             "fueron hallados: los hijos de Obías, los hijos de Acos, los "
             "hijos de Jadús, el que tomó por mujer a Augia, de las hijas de "
             "Faezeldeo, y fue llamado con el nombre de éste.",
    (5, 39): "Y buscándose el registro genealógico de éstos en el censo, y no "
             "hallándose, quedaron excluidos del sacerdocio.",
    (5, 40): "Y les dijo Nehemías y Atarías que no participasen de las cosas "
             "santas hasta que se alzase un sacerdote revestido de la "
             "declaración y la verdad.",
    (5, 41): "Y todos los de Israel, de doce años para arriba, sin contar "
             "criados y criadas, eran cuarenta y dos mil trescientos sesenta. "
             "Sus criados y criadas: siete mil trescientos treinta y siete; "
             "cantores y cantoras, doscientos cuarenta y cinco.",
    (5, 42): "Camellos, cuatrocientos treinta y cinco; caballos, siete mil "
             "treinta y seis; mulos, doscientos cuarenta y cinco; bestias de "
             "carga, cinco mil quinientas veinticinco.",
    (5, 43): "Y algunos de los jefes de familias, al llegar al templo de Dios "
             "que está en Jerusalén, hicieron voto de levantar la casa en su "
             "lugar según sus posibilidades,",
    (5, 44): "y de dar para el tesoro sagrado de las obras mil minas de oro y "
             "cinco mil minas de plata y cien vestiduras sacerdotales.",
    (5, 45): "Y se establecieron los sacerdotes y los levitas y los del pueblo "
             "en Jerusalén y en la región; y los cantores sagrados y los "
             "porteros y todo Israel, en sus aldeas.",
    (5, 46): "Y llegado el mes séptimo, estando ya los hijos de Israel cada "
             "uno en lo suyo, se reunieron todos a una en la plaza de la "
             "primera puerta, la del oriente.",
    (5, 145): "Y presentándose Jesús hijo de Josedec y sus hermanos los "
              "sacerdotes, y Zorobabel hijo de Salatiel y sus hermanos, "
              "prepararon el altar del Dios de Israel,",
    (5, 48): "para ofrecer sobre él holocaustos, conforme a lo prescrito en el "
             "libro de Moisés, el hombre de Dios.",
    (5, 49): "Y se les juntaron algunos de las otras naciones de la tierra; y "
             "erigieron el altar en su sitio, porque estaban en enemistad con "
             "ellos y los dominaban todas las naciones de la tierra; y "
             "ofrecían sacrificios en su tiempo, y holocaustos al Señor por la "
             "mañana y por la tarde.",
    (5, 50): "Y celebraron la fiesta de las tiendas como está mandado en la "
             "ley, y los sacrificios de cada día, como correspondía;",
    (5, 51): "y después de esto las ofrendas perpetuas, y los sacrificios de "
             "los sábados y de las lunas nuevas y de todas las fiestas "
             "consagradas.",
    (5, 52): "Y cuantos habían hecho voto a Dios, desde la luna nueva del mes "
             "primero empezaron a ofrecer sacrificios a Dios, aunque el templo "
             "de Dios no estaba todavía edificado.",
    (5, 53): "Y dieron dinero a los canteros y a los carpinteros, y bebida y "
             "comida y provisiones a los sidonios y a los tirios, para que "
             "trajesen del Líbano maderas de cedro y las llevasen en balsas al "
             "puerto de Jope, conforme al mandato que les había dado por "
             "escrito Ciro, rey de los persas.",
    (5, 54): "Y en el año segundo, llegados al templo de Dios en Jerusalén, en "
             "el mes segundo, comenzaron Zorobabel hijo de Salatiel y Jesús "
             "hijo de Josedec y sus hermanos y los sacerdotes y los levitas y "
             "todos los que habían venido del cautiverio a Jerusalén,",
    (5, 55): "y echaron los cimientos del templo de Dios en la luna nueva del "
             "mes segundo del año segundo desde su llegada a Judea y a "
             "Jerusalén.",
    (5, 56): "Y pusieron a los levitas de veinte años para arriba al frente de "
             "las obras del Señor; y se presentaron Jesús con sus hijos y sus "
             "hermanos, y Cadmiel su hermano, y los hijos de Jesús Emadabún, y "
             "los hijos de Judá hijo de Iliadún, con sus hijos y sus hermanos: "
             "todos los levitas, a una, como capataces, trabajando en las "
             "obras de la casa del Señor. Y los constructores edificaron el "
             "templo del Señor.",
    (5, 57): "Y se pusieron los sacerdotes revestidos, con instrumentos y "
             "trompetas, y los levitas hijos de Asaf con los címbalos, "
             "cantando himnos al Señor y bendiciéndolo conforme a David, rey "
             "de Israel;",
    (5, 58): "y clamaron con himnos bendiciendo al Señor, porque su bondad y "
             "su gloria son para siempre sobre todo Israel.",
    (5, 59): "Y todo el pueblo tocó las trompetas y gritó a gran voz, cantando "
             "himnos al Señor por el levantamiento de la casa del Señor.",
    (5, 60): "Y vinieron algunos de los sacerdotes y de los levitas y de los "
             "jefes de familias, los ancianos que habían visto la casa "
             "anterior, a ver la construcción de ésta, con clamor y gran "
             "llanto;",
    (5, 61): "y muchos, con trompetas y con gran alegría en la voz,",
    (5, 62): "de modo que el pueblo no podía oír las trompetas por el llanto "
             "del pueblo; porque la muchedumbre tocaba con tal fuerza que se "
             "oía desde lejos.",
    (5, 63): "Y al oírlo, los enemigos de la tribu de Judá y de Benjamín "
             "vinieron a enterarse de qué era aquel son de trompetas,",
    (5, 64): "y se enteraron de que los que habían vuelto del cautiverio "
             "estaban edificando el templo al Señor Dios de Israel.",
    (5, 65): "Y acercándose a Zorobabel y a Jesús y a los jefes de familias, "
             "les dicen: «Edificaremos con vosotros;",
    (5, 66): "porque igual que vosotros obedecemos a vuestro Señor, y a él le "
             "ofrecemos sacrificios desde los días de Asbacafat, rey de los "
             "asirios, que nos trajo aquí».",
    (5, 67): "Y les dijeron Zorobabel y Jesús y los jefes de familias de "
             "Israel: «No os toca a vosotros edificar la casa al Señor nuestro "
             "Dios;",
    (5, 68): "porque nosotros solos edificaremos al Señor de Israel, conforme "
             "a lo que nos mandó Ciro, rey de los persas».",
    (5, 69): "Pero las naciones de la tierra se echaron encima de los de Judea "
             "y, asediándolos, les impedían edificar;",
    (5, 70): "y con intrigas y arengas populares y conjuras impidieron que se "
             "acabase la construcción todo el tiempo que vivió el rey Ciro; y "
             "quedaron detenidos en la obra dos años, hasta el reinado de "
             "Darío.",

    (6, 1): "Y en el año segundo del reinado de Darío profetizaron Ageo y "
            "Zacarías hijo de Adó, los profetas, a los judíos que estaban en "
            "Judea y en Jerusalén, en el nombre del Señor Dios de Israel, "
            "sobre ellos.",
    (6, 2): "Entonces se levantaron Zorobabel hijo de Salatiel y Jesús hijo de "
            "Josedec, y empezaron a edificar la casa del Señor que está en "
            "Jerusalén, estando con ellos los profetas del Señor, que los "
            "ayudaban.",
    (6, 3): "En aquel mismo tiempo se presentó ante ellos Sisinnes, gobernador "
            "de Siria y Fenicia, y Satrabuzanes y sus colegas, y les dijo:",
    (6, 4): "«¿Por orden de quién estáis edificando esta casa y acabando este "
            "techado y todo lo demás? ¿Y quiénes son los constructores que lo "
            "están haciendo?».",
    (6, 5): "Pero los ancianos de los judíos hallaron gracia, porque el Señor "
            "había puesto sus ojos en los que volvían del cautiverio,",
    (6, 6): "y no se les impidió la obra hasta que se informase a Darío acerca "
            "de ellos y se recibiese respuesta.",
    (6, 7): "Copia de la carta que escribieron y enviaron a Darío Sisinnes, "
            "gobernador de Siria y Fenicia, y Satrabuzanes y sus colegas, los "
            "gobernadores de Siria y Fenicia: «Al rey Darío, salud.",
    (6, 8): "Sepa todo nuestro señor el rey que, llegados a la región de Judea "
            "y a la ciudad de Jerusalén, encontramos a los ancianos de los "
            "judíos, los del cautiverio, en la ciudad de Jerusalén, edificando "
            "al Señor una casa grande y nueva, con piedras labradas y "
            "costosas, colocando maderas en los muros;",
    (6, 9): "y aquellas obras se hacen con diligencia, y el trabajo prospera "
            "en sus manos, y se lleva a cabo con toda magnificencia y "
            "esmero.",
    (6, 10): "Entonces preguntamos a aquellos ancianos, diciendo: «¿Por orden "
             "de quién edificáis esta casa y echáis los cimientos de estas "
             "obras?».",
    (6, 11): "Se lo preguntamos, pues, para poder informarte y escribirte los "
             "nombres de los hombres que están al frente, y les pedimos la "
             "lista de sus jefes.",
    (6, 12): "Y ellos nos respondieron diciendo: «Somos siervos del Señor, que "
             "creó el cielo y la tierra.",
    (6, 13): "Y esta casa fue edificada hace muchos años por un rey de Israel "
             "grande y fuerte, y fue terminada.",
    (6, 14): "Y como nuestros padres lo irritaron y pecaron contra el Señor de "
             "Israel, el del cielo, él los entregó en manos de Nabucodonosor, "
             "rey de Babilonia, rey de los caldeos;",
    (6, 15): "y derribando la casa, la quemaron, y llevaron cautivo al pueblo "
             "a Babilonia.",
    (6, 16): "Pero en el año primero del reinado de Ciro sobre el país de "
             "Babilonia, el rey Ciro ordenó por escrito que se edificase esta "
             "casa,",
    (6, 17): "y los vasos sagrados de oro y de plata que Nabucodonosor había "
             "sacado de la casa que está en Jerusalén y había depositado en su "
             "propio templo, los volvió a sacar el rey Ciro del templo que "
             "está en Babilonia, y fueron entregados a Zorobabel y a "
             "Sanabasar el gobernador,",
    (6, 18): "y se le ordenó a éste que llevase todos aquellos vasos y los "
             "depositase en el templo de Jerusalén, y que el templo del Señor "
             "fuese edificado en su sitio.",
    (6, 19): "Entonces aquel Sanabasar, al llegar, echó los cimientos de la "
             "casa del Señor que está en Jerusalén; y desde entonces hasta "
             "ahora se está edificando, y no ha llegado a su término».",
    (6, 20): "Ahora, pues, decide tú, rey: búsquese en los archivos reales del "
             "rey nuestro señor, los que están en Babilonia,",
    (6, 21): "y si se halla que la construcción de la casa del Señor que está "
             "en Jerusalén se hizo con la aprobación del rey Ciro, y le parece "
             "bien al rey nuestro señor, mándenos aviso sobre esto».",
    (6, 22): "Entonces el rey Darío mandó que se buscase en los archivos que "
             "están en Babilonia; y se halló en Ecbátana, la fortaleza que "
             "está en la región de Media, un rollo en el que estaba anotado "
             "esto:",
    (6, 23): "«Año primero del reinado de Ciro. El rey Ciro mandó edificar la "
             "casa del Señor que está en Jerusalén, donde ofrecen sacrificios "
             "con fuego perpetuo;",
    (6, 24): "su altura, sesenta codos, y su anchura, sesenta codos, con tres "
             "hiladas de piedras labradas y una hilada de madera nueva del "
             "país; y que el gasto se dé de la casa del rey Ciro.",
    (6, 25): "Y los vasos sagrados de la casa del Señor, los de oro y los de "
             "plata, que Nabucodonosor sacó de la casa que está en Jerusalén y "
             "se llevó a Babilonia, que sean devueltos a la casa que está en "
             "Jerusalén, donde estaban, para que se pongan allí».",
    (6, 26): "Y mandó que Sisinnes, gobernador de Siria y Fenicia, y "
             "Satrabuzanes y sus colegas, y los gobernadores designados en "
             "Siria y Fenicia, tuvieran cuidado de no acercarse a aquel lugar, "
             "sino de dejar que el siervo del Señor, Zorobabel, gobernador de "
             "Judea, y los ancianos de los judíos edificasen aquella casa del "
             "Señor en su sitio.",
    (6, 27): "«Y yo también he mandado que se edifique por entero, y que se "
             "ponga atención en cooperar con los que han vuelto del "
             "cautiverio de Judea hasta que se termine la casa del Señor;",
    (6, 28): "y que de los tributos de Celesiria y Fenicia se dé puntualmente "
             "una asignación a aquellos hombres para los sacrificios al Señor, "
             "a Zorobabel el gobernador, para toros y carneros y corderos;",
    (6, 29): "e igualmente trigo y sal y vino y aceite, sin falta, año tras "
             "año, según lo que los sacerdotes de Jerusalén indiquen que se "
             "gasta cada día, sin discusión,",
    (6, 30): "para que se ofrezcan libaciones al Dios Altísimo por el rey y "
             "por sus hijos, y oren por la vida de ellos.",
    (6, 31): "Y he mandado que a todo el que traspase algo de lo escrito o lo "
             "anule, se tome un madero de sus propios bienes y sea colgado en "
             "él, y que sus bienes pasen a ser del rey.",
    (6, 32): "Por lo cual, también el Señor, cuyo nombre allí se invoca, "
             "destruya a todo rey y a toda nación que extienda su mano para "
             "impedir o dañar aquella casa del Señor que está en Jerusalén.",
    (6, 33): "Yo, el rey Darío, he decretado que se cumpla esto con esmero».",

    (7, 1): "Entonces Sisinnes, gobernador de Celesiria y Fenicia, y "
            "Satrabuzanes y sus colegas, siguiendo lo mandado por el rey "
            "Darío,",
    (7, 2): "supervisaban las obras sagradas con el mayor esmero, cooperando "
            "con los ancianos de los judíos y con los jefes del templo.",
    (7, 3): "Y las obras sagradas iban prosperando, mientras profetizaban Ageo "
            "y Zacarías, los profetas;",
    (7, 4): "y las terminaron por mandato del Señor Dios de Israel y con la "
            "aprobación de Ciro y de Darío y de Artajerjes, reyes de los "
            "persas.",
    (7, 5): "Quedó terminada la casa el día veintitrés del mes de Adar, el año "
            "sexto del rey Darío.",
    (7, 6): "Y los hijos de Israel y los sacerdotes y los levitas y los demás "
            "que habían vuelto del cautiverio y se les habían agregado "
            "hicieron conforme a lo que está en el libro de Moisés.",
    (7, 7): "Y ofrecieron para la dedicación del templo del Señor cien toros, "
            "doscientos carneros y cuatrocientos corderos,",
    (7, 8): "y doce machos cabríos por el pecado de todo Israel, según el "
            "número de los jefes de las doce tribus de Israel.",
    (7, 9): "Y se pusieron los sacerdotes y los levitas revestidos, por "
            "clases, al frente de las obras del Señor Dios de Israel, conforme "
            "al libro de Moisés; y los porteros, cada uno en su puerta.",
    (7, 10): "Y los hijos de Israel que habían vuelto del cautiverio "
             "celebraron la pascua el día catorce del mes primero, cuando los "
             "sacerdotes y los levitas se purificaron a la vez,",
    (7, 11): "y todos los hijos del cautiverio, porque se purificaron, ya que "
             "los levitas se purificaron todos a la vez;",
    (7, 12): "e inmolaron la pascua para todos los hijos del cautiverio y para "
             "sus hermanos los sacerdotes y para sí mismos.",
    (7, 13): "Y comieron los hijos de Israel que habían vuelto del cautiverio, "
             "todos los que se habían apartado de las abominaciones de las "
             "naciones de la tierra buscando al Señor.",
    (7, 14): "Y celebraron la fiesta de los ázimos siete días, con alegría "
             "delante del Señor,",
    (7, 15): "porque él había cambiado en favor de ellos el ánimo del rey de "
             "los asirios, para fortalecer sus manos en las obras del Señor "
             "Dios de Israel.",

    (8, 1): "Y después de esto, reinando Artajerjes, rey de los persas, subió "
            "Esdras, hijo de Azarías, hijo de Zecrías, hijo de Jilquías, hijo "
            "de Salumo,",
    (8, 2): "hijo de Sadoc, hijo de Ajitob, hijo de Amarías, hijo de Ozías, "
            "hijo de Boccas, hijo de Abisúe, hijo de Fineés, hijo de Eleazar, "
            "hijo de Aarón, el primer sacerdote.",
    (8, 3): "Este Esdras subió de Babilonia como escriba experto en la ley de "
            "Moisés, dada por el Dios de Israel;",
    (8, 4): "y el rey lo honró, porque halló gracia delante de él en todas sus "
            "peticiones.",
    (8, 5): "Y subieron con él a Jerusalén algunos de los hijos de Israel y de "
            "los sacerdotes y de los levitas y de los cantores sagrados y de "
            "los porteros y de los servidores del templo,",
    (8, 6): "el año séptimo del reinado de Artajerjes, en el mes quinto —éste "
            "es el año segundo del rey—; porque, habiendo salido de Babilonia "
            "en la luna nueva del mes primero, llegaron a Jerusalén gracias al "
            "buen viaje que el Señor les concedió por él.",
    (8, 7): "Porque Esdras poseía gran ciencia, de modo que no omitía nada de "
            "la ley del Señor ni de los mandamientos, sino que enseñaba a todo "
            "Israel los preceptos y los juicios.",
    (8, 8): "Llegó de parte del rey Artajerjes a Esdras, el sacerdote y lector "
            "de la ley del Señor, un escrito cuya copia es la siguiente:",
    (8, 9): "«El rey Artajerjes a Esdras, sacerdote y lector de la ley del "
            "Señor, salud.",
    (8, 10): "Habiendo decidido obrar con benevolencia, he ordenado que los "
             "del pueblo de los judíos que lo deseen, y los sacerdotes y los "
             "levitas que lo elijan, y los que están en nuestro reino, vayan "
             "contigo a Jerusalén.",
    (8, 11): "Cuantos, pues, lo tengan resuelto, pónganse en camino contigo, "
             "según lo hemos decidido yo y mis siete amigos consejeros,",
    (8, 12): "para que inspeccionen lo de Judea y lo de Jerusalén conforme a "
             "la ley del Señor que él tiene,",
    (8, 13): "y para llevar a Jerusalén los dones que hemos ofrecido al Señor "
             "yo y mis amigos, y todo el oro y la plata que se encuentre en la "
             "región de Babilonia para el Señor, a Jerusalén, junto con lo "
             "donado por el pueblo para el templo de su Señor que está en "
             "Jerusalén;",
    (8, 14): "que se recaude el oro y la plata para toros y carneros y "
             "corderos y lo que va con ellos,",
    (8, 15): "de modo que se ofrezcan sacrificios sobre el altar de su Señor "
             "que está en Jerusalén.",
    (8, 16): "Y todo lo que quieras hacer con tus hermanos con el oro y la "
             "plata, hazlo conforme a la voluntad de tu Dios;",
    (8, 17): "y lo mismo con los vasos sagrados que se te dan para el servicio "
             "del templo de tu Dios que está en Jerusalén. Y lo demás que "
             "necesites para el servicio del templo de tu Dios,",
    (8, 18): "lo darás del tesoro real.",
    (8, 19): "Y yo, el rey Artajerjes, he mandado a los tesoreros de Siria y "
             "Fenicia que den puntualmente a Esdras, el sacerdote y lector de "
             "la ley del Dios Altísimo, cuanto pida, hasta cien talentos de "
             "plata,",
    (8, 20): "e igualmente hasta cien coros de trigo y cien medidas de vino.",
    (8, 21): "Cúmplase conforme a la ley de Dios para el Dios Altísimo, para "
             "que no venga la ira sobre el reino del rey y de sus hijos.",
    (8, 22): "Y se os manda también que a todos los sacerdotes y a los levitas "
             "y a los cantores sagrados y a los porteros y a los servidores "
             "del templo y a los administradores de este templo no se les "
             "imponga tributo alguno ni ninguna otra carga, y que nadie tenga "
             "facultad de imponérsela.",
    (8, 23): "Y tú, Esdras, conforme a la sabiduría de Dios, nombra jueces y "
             "magistrados para que juzguen en toda Siria y Fenicia a todos los "
             "que conocen la ley de tu Dios; y a los que no la conocen, "
             "enséñasela.",
    (8, 24): "Y todos cuantos traspasen la ley de tu Dios y la del rey serán "
             "castigados con rigor, sea con la muerte, sea con otro suplicio, "
             "sea con multa en dinero o con destierro».",
    (8, 25): "Bendito sea el Señor, el único, que puso esto en el corazón del "
             "rey: glorificar su casa que está en Jerusalén;",
    (8, 26): "y que me honró a mí delante de los reyes y de todos sus amigos y "
             "magnates.",
    (8, 27): "Y yo cobré ánimo con el auxilio del Señor mi Dios, y reuní de "
             "Israel hombres para que subiesen conmigo.",
    (8, 28): "Y éstos son los jefes, según sus familias y sus divisiones, que "
             "subieron conmigo de Babilonia en el reinado del rey Artajerjes:",
    (8, 29): "de los hijos de Fineés, Gersón; de los hijos de Itamar, Gamael; "
             "de los hijos de David,",
    (8, 30): "Atús hijo de Sequenías; de los hijos de Farés, Zacarías, y con "
             "él, según el registro, ciento cincuenta hombres;",
    (8, 31): "de los hijos de Fahat-Moab, Elionías hijo de Zaraías, y con él "
             "doscientos hombres;",
    (8, 32): "de los hijos de Zatoe, Sequenías hijo de Jezelo, y con él "
             "trescientos hombres; de los hijos de Adín, Obet hijo de Jonatán, "
             "y con él doscientos cincuenta hombres;",
    (8, 33): "de los hijos de Elam, Jesías hijo de Gotolías, y con él setenta "
             "hombres;",
    (8, 34): "de los hijos de Safatías, Zaraías hijo de Micael, y con él "
             "setenta hombres;",
    (8, 35): "de los hijos de Joab, Abadías hijo de Jezelo, y con él doscientos "
             "doce hombres;",
    (8, 36): "de los hijos de Banías, Salimot hijo de Josafías, y con él ciento "
             "sesenta hombres;",
    (8, 37): "de los hijos de Bebai, Zacarías hijo de Bebai, y con él "
             "veintiocho hombres;",
    (8, 38): "de los hijos de Astat, Juan hijo de Acatán, y con él ciento diez "
             "hombres;",
    (8, 39): "de los hijos de Adonicam, los últimos, y éstos son sus nombres: "
             "Elifala hijo de Geuel, y Samaías, y con ellos setenta hombres;",
    (8, 40): "de los hijos de Bagoi, Utai hijo de Istacalco, y con él setenta "
             "hombres.",
    (8, 41): "Y los reuní junto al río llamado Teras, y acampamos allí tres "
             "días, y pasé revista a los que había.",
    (8, 42): "Y no habiendo hallado allí a ninguno de los sacerdotes ni de los "
             "levitas,",
    (8, 43): "envié a Eleazar y a Iduelo y a Maasmán y a Enaatán y a Samaías y "
             "a Jorib, a Natán, Enatán, Zacarías y Mosolamón, que eran jefes y "
             "hombres entendidos,",
    (8, 44): "y les dije que fuesen a Ladeo, el jefe que está en el lugar del "
             "tesoro,",
    (8, 45): "encargándoles que hablasen con Ladeo y con sus hermanos y con "
             "los tesoreros de aquel lugar, para que nos enviasen hombres que "
             "pudiesen ejercer el sacerdocio en la casa de nuestro Señor.",
    (8, 46): "Y nos trajeron, por la mano poderosa de nuestro Señor, a un "
             "hombre entendido de los hijos de Moolí, hijo de Leví, hijo de "
             "Israel: a Asebebías, y a sus hijos y a sus hermanos, dieciocho;",
    (8, 47): "y a Asebías y a Anuno y a Osaías su hermano, de los hijos de "
             "Cananeo, y a sus hijos, veinte hombres;",
    (8, 48): "y de los servidores del templo que dio David, y los jefes para "
             "el servicio de los levitas, doscientos veinte servidores del "
             "templo; de todos se registró la lista de los nombres.",
    (8, 49): "Y proclamé allí un ayuno para los jóvenes delante de nuestro "
             "Señor,",
    (8, 50): "para pedirle un buen viaje para nosotros y para nuestros hijos y "
             "nuestros ganados.",

    (8, 51): "Porque me dio vergüenza pedir al rey jinetes y soldados de a pie "
             "como escolta para protegernos de nuestros adversarios;",
    (8, 52): "pues le habíamos dicho al rey: «La fuerza de nuestro Señor estará "
             "con los que lo buscan, para todo bien».",
    (8, 53): "Y de nuevo suplicamos a nuestro Señor todas estas cosas, y lo "
             "hallamos propicio.",
    (8, 54): "Y aparté a doce de los jefes de los sacerdotes, y a Eserebías y "
             "a Asamías, y con ellos a diez de sus hermanos;",
    (8, 55): "y les pesé la plata y el oro y los vasos sagrados de la casa de "
             "nuestro Señor, lo que habían donado el rey y sus consejeros y "
             "los magnates y todo Israel.",
    (8, 56): "Y se lo entregué pesado: seiscientos cincuenta talentos de plata, "
             "y vasos de plata por valor de cien talentos, y cien talentos de "
             "oro, y veinte objetos de oro, y diez vasos de bronce, de bronce "
             "fino y reluciente.",
    (8, 57): "Y les dije: «También vosotros estáis consagrados al Señor, y los "
             "vasos son santos, y la plata y el oro son una ofrenda votiva al "
             "Señor, al Señor de nuestros padres.",
    (8, 58): "Velad y guardadlo hasta que lo entreguéis a los jefes de los "
             "sacerdotes y de los levitas y a los jefes de las familias de "
             "Israel, en Jerusalén, en las cámaras de la casa de nuestro "
             "Señor».",
    (8, 59): "Y los sacerdotes y los levitas que recibieron la plata y el oro "
             "y los vasos los llevaron al templo del Señor en Jerusalén.",
    (8, 60): "Y partiendo del lugar del río Teras el día doce del mes primero, "
             "llegaron a Jerusalén bajo la mano poderosa de nuestro Señor, que "
             "estaba sobre nosotros; y nos libró desde la salida de todo "
             "enemigo; y llegamos a Jerusalén.",
    (8, 61): "Y pasados allí tres días, se pesó la plata y el oro y se entregó "
             "en la casa del Señor a Marmotí, sacerdote hijo de Urías,",
    (8, 62): "y con él a Eleazar hijo de Fineés; y estaban con ellos Josabdo "
             "hijo de Jesús y Moet hijo de Sabanno, los levitas; todo por "
             "número y por peso, y todo el peso quedó registrado en aquella "
             "misma hora.",
    (8, 63): "Y los que habían vuelto del cautiverio ofrecieron sacrificios al "
             "Señor, Dios de Israel: doce toros por todo Israel, noventa y "
             "seis carneros, setenta y seis corderos, doce machos cabríos como "
             "sacrificio de salvación; todo en sacrificio al Señor.",
    (8, 64): "Y entregaron las órdenes del rey a los administradores reales y "
             "a los gobernadores de Siria y Fenicia, y éstos honraron a la "
             "nación y al templo del Señor.",
    (8, 65): "Y terminado esto, se acercaron a mí los jefes y me dijeron:",
    (8, 66): "«No se han separado el pueblo de Israel ni los príncipes ni los "
             "sacerdotes ni los levitas de las naciones extranjeras de la "
             "tierra ni de sus impurezas: de los cananeos y heteos y ferezeos "
             "y jebuseos y moabitas y egipcios e idumeos;",
    (8, 67): "porque han tomado por mujeres a algunas de sus hijas, ellos y "
             "sus hijos, y se ha mezclado la simiente santa con las naciones "
             "extranjeras de la tierra; y los jefes y los magnates han tenido "
             "parte en esta iniquidad desde el principio del asunto».",
    (8, 68): "Y en cuanto oí esto, rasgué mis vestidos y la vestidura sagrada, "
             "y me arranqué el pelo de la cabeza y de la barba, y me senté "
             "preocupado y muy afligido.",
    (8, 69): "Y se reunieron junto a mí cuantos se conmovían ante la palabra "
             "del Señor de Israel, mientras yo hacía duelo por aquella "
             "iniquidad; y estuve sentado, muy afligido, hasta el sacrificio "
             "de la tarde.",
    (8, 70): "Y levantándome del ayuno, con los vestidos y la vestidura "
             "sagrada rasgados, doblando las rodillas y extendiendo las manos "
             "al Señor, dije:",
    (8, 71): "«Señor, estoy avergonzado, confundido delante de tu rostro.",
    (8, 72): "Porque nuestros pecados se han multiplicado por encima de "
             "nuestras cabezas, y nuestras faltas se han levantado hasta el "
             "cielo",
    (8, 73): "desde los tiempos de nuestros padres, y estamos en gran pecado "
             "hasta el día de hoy.",
    (8, 74): "Y por nuestros pecados y los de nuestros padres fuimos "
             "entregados, con nuestros hermanos y con nuestros reyes y con "
             "nuestros sacerdotes, a los reyes de la tierra, a la espada y al "
             "cautiverio y al saqueo, con vergüenza, hasta el día de hoy.",
    (8, 75): "Y ahora, ¡cuánta misericordia hemos recibido de ti, Señor, "
             "Señor!: que nos quede una raíz y un nombre en este lugar de tu "
             "santuario,",
    (8, 76): "y que se nos descubra una lumbrera en la casa de nuestro Señor, "
             "y se nos dé sustento en el tiempo de nuestra servidumbre; y en "
             "nuestra servidumbre no fuimos abandonados por nuestro Señor,",
    (8, 77): "sino que nos hizo hallar gracia delante de los reyes de los "
             "persas, para darnos sustento",
    (8, 78): "y para glorificar nuestro templo y levantar la desolada Sión, "
             "dándonos un apoyo firme en Judea y en Jerusalén.",
    (8, 79): "Y ahora, ¿qué diremos, Señor, teniendo todo esto? Porque hemos "
             "traspasado tus mandamientos, los que diste por mano de tus "
             "siervos los profetas, diciendo:",
    (8, 80): "«La tierra en la que entráis para tomarla en posesión es una "
             "tierra manchada con la mancha de los extranjeros de la tierra, y "
             "la han llenado de su impureza;",
    (8, 81): "y ahora, no caséis a vuestras hijas con sus hijos, ni toméis a "
             "sus hijas para vuestros hijos,",
    (8, 82): "ni procuréis nunca hacer las paces con ellos, para que, "
             "fortalecidos, comáis los bienes de la tierra y se la dejéis en "
             "herencia a vuestros hijos para siempre».",
    (8, 83): "Y todo lo que nos sucede nos viene por nuestras malas obras y "
             "por nuestros grandes pecados. Porque tú, Señor, que aliviaste "
             "nuestros pecados,",
    (8, 84): "nos diste una raíz como ésta; y otra vez hemos vuelto a "
             "traspasar tu ley, mezclándonos con la impureza de las naciones "
             "de la tierra.",
    (8, 85): "¿No te irritaste contra nosotros hasta querer destruirnos sin "
             "dejar raíz ni semilla ni nombre nuestro?",
    (8, 86): "Señor de Israel, tú eres veraz: pues hemos quedado como una raíz "
             "en el día de hoy.",
    (8, 87): "Aquí estamos delante de ti con nuestras iniquidades; porque ya "
             "no es posible seguir en pie delante de ti por causa de esto».",
    (8, 88): "Y mientras Esdras oraba y se confesaba llorando, postrado en "
             "tierra delante del templo, se reunió junto a él, desde "
             "Jerusalén, una muchedumbre grandísima: hombres y mujeres y "
             "jóvenes; porque había un gran llanto en la multitud.",
    (8, 89): "Y alzando la voz Jeconías hijo de Jehiel, de los hijos de "
             "Israel, dijo a Esdras: «Nosotros hemos pecado contra el Señor, y "
             "hemos tomado mujeres extranjeras de las naciones de la tierra; y "
             "ahora todo Israel está por encima de esto.",
    (8, 90): "Hagamos por esto un juramento al Señor: echar a todas nuestras "
             "mujeres extranjeras con sus hijos, como te ha parecido bien a "
             "ti y a cuantos obedecen la ley del Señor.",
    (8, 91): "Levántate y cúmplelo; porque a ti te toca el asunto, y nosotros "
             "estamos contigo para darte fuerza».",
    (8, 92): "Y levantándose Esdras, hizo jurar a los jefes de los sacerdotes "
             "y de los levitas de todo Israel que harían conforme a esto; y lo "
             "juraron.",

    (9, 1): "Y levantándose Esdras del atrio del templo, fue a la cámara de "
            "Jonatán hijo de Nasibo,",
    (9, 2): "y pasando allí la noche, no probó pan ni bebió agua, haciendo "
            "duelo por las grandes iniquidades de la multitud.",
    (9, 3): "Y se hizo un pregón en toda Judea y en Jerusalén, para que todos "
            "los que habían vuelto del cautiverio se reuniesen en Jerusalén;",
    (9, 4): "y que a cuantos no acudiesen en dos o tres días, conforme al "
            "juicio de los ancianos que presidían, se les confiscasen sus "
            "ganados y quedasen ellos excluidos de la asamblea de los que "
            "habían vuelto del cautiverio.",
    (9, 5): "Y se reunieron en Jerusalén, en tres días, los de la tribu de "
            "Judá y de Benjamín: era el mes noveno, el día veinte del mes.",
    (9, 6): "Y se sentó toda la multitud en la plaza del templo, temblando por "
            "el mal tiempo que hacía.",
    (9, 7): "Y levantándose Esdras, les dijo: «Vosotros habéis obrado "
            "inicuamente y habéis tomado mujeres extranjeras, añadiendo pecado "
            "a Israel.",
    (9, 8): "Y ahora, dad gloria confesándoos al Señor Dios de nuestros "
            "padres,",
    (9, 9): "y haced su voluntad, y separaos de las naciones de la tierra y de "
            "las mujeres extranjeras».",
    (9, 10): "Y toda la multitud clamó y dijo a gran voz: «Así lo haremos, "
             "como has dicho.",
    (9, 11): "Pero la multitud es grande y es tiempo de invierno, y no podemos "
             "estar a la intemperie; y no es cosa de un día ni de dos, porque "
             "hemos pecado mucho en esto.",
    (9, 12): "Quédense los jefes de la multitud, y vayan viniendo, cuando les "
             "toque, todos los de nuestras poblaciones que tengan mujeres "
             "extranjeras,",
    (9, 13): "con los ancianos y los jueces de cada lugar, hasta que se aparte "
             "de nosotros la ira del Señor por este asunto».",
    (9, 14): "Jonatán hijo de Azael y Ezequías hijo de Tocano se encargaron de "
             "esto, y Mosolamo y Leví y Sabateo cooperaron con ellos.",
    (9, 15): "Y los que habían vuelto del cautiverio hicieron conforme a todo "
             "esto.",
    (9, 16): "Y Esdras el sacerdote se escogió hombres, jefes de sus familias, "
             "todos por su nombre; y se reunieron a puerta cerrada en la luna "
             "nueva del mes décimo para examinar el asunto.",
    (9, 17): "Y se llevó a término lo referente a los hombres que tenían "
             "mujeres extranjeras, hasta la luna nueva del mes primero.",
    (9, 18): "Y de los sacerdotes se halló que tenían mujeres extranjeras los "
             "siguientes:",
    (9, 19): "de los hijos de Jesús hijo de Josedec y de sus hermanos: Maasías "
             "y Eleazar y Jorib y Jodán;",
    (9, 20): "y se comprometieron a echar a sus mujeres, y a ofrecer carneros "
             "en expiación por su falta;",
    (9, 21): "y de los hijos de Emer: Ananías y Zabdeo y Manes y Sameo y "
             "Jereel y Azarías;",
    (9, 22): "y de los hijos de Fasur: Elioneo, Masías, Ismael y Natanael y "
             "Ocáiledo y Saltas;",
    (9, 23): "y de los levitas: Jozabdo y Semeí y Colio —éste es Calitas— y "
             "Pateo, y Judas y Jonás;",
    (9, 24): "de los cantores sagrados: Eliasib y Bacuro;",
    (9, 25): "de los porteros: Salumo y Tolbanes;",
    (9, 26): "de Israel: de los hijos de Foros: Jerma y Jezías y Melquías y "
             "Miamino y Eleazar y Asebías y Bannas;",
    (9, 27): "de los hijos de Ela: Matán y Zacarías, Jezriel y Oabdio y "
             "Jeremot y Aedías;",
    (9, 28): "y de los hijos de Zamot: Eliadas, Eliasimo, Otonías, Jarimot y "
             "Sabato y Zeralías;",
    (9, 29): "y de los hijos de Bebai: Juan y Ananías y Zabdo y Ematís;",
    (9, 30): "y de los hijos de Maní: Olamo, Mamuco, Jedeo, Jasubo y Asael y "
             "Jeremot;",
    (9, 31): "y de los hijos de Adín: Lato y Mosías, Lacuno y Naído, y "
             "Bescaspasmo y Sestel y Balnúo y Manasías;",
    (9, 32): "y de los hijos de Anán: Eliodas y Asaías y Melquías y Sabeas y "
             "Simón Cosameo;",
    (9, 33): "y de los hijos de Asom: Maltaneo y Matatías y Sabaneo y Elifalat "
             "y Manasés y Semeí;",
    (9, 34): "y de los hijos de Baní: Jeremías, Momdeo, Maero, Juna, Mamdai y "
             "Pedías y Anos, Carabasión y Enasibo y Mamtaneo, Eliasís, Bannús, "
             "Edialís, Someís, Selemías, Natanías; y de los hijos de Ezorá: "
             "Sesís, Ezril, Azael, Samato, Zambrí, Josefo;",
    (9, 35): "de los hijos de Noomá: Zitías, Zabadeas, Edos, Uel, Banaías.",
    (9, 36): "Todos éstos habían tomado mujeres extranjeras, y las despidieron "
             "con sus hijos.",
    (9, 37): "Y los sacerdotes y los levitas y los de Israel se establecieron "
             "en Jerusalén y en la región, en la luna nueva del mes séptimo; y "
             "los hijos de Israel, en sus poblaciones.",
    (9, 38): "Y se reunió toda la multitud a una en la plaza de la puerta "
             "oriental del templo,",
    (9, 39): "y dijeron a Esdras, el sacerdote y lector, que trajese la ley de "
             "Moisés, la entregada por el Dios de Israel.",
    (9, 40): "Y Esdras el sumo sacerdote trajo la ley a toda la multitud, "
             "desde los hombres hasta las mujeres, y a todos los sacerdotes, "
             "para que oyeran la ley, en la luna nueva del mes séptimo;",
    (9, 41): "y la leyó en la plaza que está delante de la puerta del templo, "
             "desde el amanecer hasta el mediodía, delante de los hombres y de "
             "las mujeres; y todos pusieron toda su atención en la ley.",
    (9, 42): "Y se puso en pie Esdras, el sacerdote y lector de la ley, sobre "
             "el estrado de madera que se había preparado;",
    (9, 43): "y se pusieron junto a él, a la derecha, Matatías, Samo, Ananías, "
             "Azarías, Urías, Ezequías y Baalsamo;",
    (9, 44): "y a la izquierda, Faladeo, Misael, Melquías, Lotasubo, Nabarías "
             "y Zacarías.",
    (9, 45): "Y tomando Esdras el libro delante de la multitud —porque estaba "
             "sentado en un sitio de honor a la vista de todos—,",
    (9, 46): "al abrir la ley se pusieron todos en pie; y bendijo Esdras al "
             "Señor Dios Altísimo, Todopoderoso;",
    (9, 47): "y toda la multitud respondió: «Amén, amén»; y alzando las manos "
             "en alto y postrándose en tierra, adoraron a Dios.",
    (9, 48): "Jesús y Anniut y Sarabías, Jadino, Jacubo, Sabateo, Auteas, "
             "Maiannas y Calitas, Azarías, Jozabdo, Ananías y Falías, los "
             "levitas, enseñaban la ley del Señor, y leían a la multitud la "
             "ley del Señor, dándole sentido al mismo tiempo que la leían.",
    (9, 49): "Y dijo Atarates a Esdras, el sumo sacerdote y lector, y a los "
             "levitas que enseñaban a la multitud, ante todos:",
    (9, 50): "«Este día es santo para el Señor». Y todos lloraban al oír la "
             "ley.",
    (9, 51): "«Id, pues, y comed manjares sabrosos, y enviad porciones a los "
             "que no tienen;",
    (9, 52): "porque el día es santo para el Señor, y no os entristezcáis, "
             "porque el Señor os dará gloria».",
    (9, 53): "Y los levitas iban dando órdenes a todo el pueblo diciendo: "
             "«Este día es santo; no os entristezcáis».",
    (9, 54): "Y se fueron todos a comer y a beber y a alegrarse, y a dar "
             "porciones a los que no tenían, y a alegrarse mucho;",
    (9, 55): "porque habían quedado llenos de aliento con las palabras que se "
             "les habían enseñado. Y se reunieron.",
}
