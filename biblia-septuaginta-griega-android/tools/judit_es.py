"""Judit en español, traducida del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Es una novela
de resistencia: un rey pagano que se hace llamar dios, un general que arrasa
todo lo que encuentra, una aldea de montaña que se queda sin agua y se rinde a
plazo fijo, y una viuda que sale de noche del pueblo y vuelve con una cabeza
en un zurrón.

Vale la pena leerla por dos cosas. La primera es que el libro se burla de la
historia a propósito: llama a Nabucodonosor «rey de los asirios» y lo pone en
Nínive, que para entonces ya había caído, y hace volver del destierro a un
pueblo que todavía no había salido. No es ignorancia, es el modo de decir «esto
pasa siempre», como quien cuenta una parábola. La segunda es el discurso de
Judit a los ancianos en el capítulo 8: que poner plazo a Dios —«si en cinco
días no nos socorre, nos entregamos»— es tentarlo, y que la fidelidad no se
mide por lo que Dios haga sino por quién es.

Lo que hace es un engaño y un asesinato, y el libro no lo disimula: ella misma
pide fuerza «para el engaño de mis labios» (9:13). Conviene leerlo como lo que
es, un relato, y no como una regla de conducta.

El texto griego de esta edición trae en 1:1 una transposición evidente —las
palabras «en los días» están metidas dentro del verbo «reinó»—; aquí se traduce
la lectura que el propio texto deja ver, sin corregir nada más. Los capítulos
saltan del 3:1 al 3:3 porque el editor griego cose el versículo 2 dentro del 1.
"""

from __future__ import annotations

JUDIT_ES: dict[tuple[int, int], str] = {
    (1, 1): "El año duodécimo del reinado de Nabucodonosor, que reinó sobre "
            "los asirios en Nínive, la gran ciudad, en los días de Arfaxad, "
            "que reinó sobre los medos en Ecbátana",
    (1, 2): "—y edificó sobre Ecbátana, y alrededor, murallas de piedras "
            "labradas, de tres codos de ancho y seis codos de largo, e hizo la "
            "altura de la muralla de setenta codos y su anchura de cincuenta "
            "codos;",
    (1, 3): "y sus torres las levantó sobre las puertas de ella, de cien "
            "codos, y su anchura la cimentó en sesenta codos;",
    (1, 4): "e hizo sus puertas, puertas que se alzaban hasta una altura de "
            "setenta codos, y su anchura de cuarenta codos, para las salidas "
            "del ejército de sus valientes y las formaciones de su "
            "infantería—,",
    (1, 5): "en aquellos días hizo guerra el rey Nabucodonosor contra el rey "
            "Arfaxad en la gran llanura, que es la que está en los términos de "
            "Ragau.",
    (1, 6): "Y se juntaron con él todos los que habitaban la montaña, y todos "
            "los que habitaban junto al Éufrates y al Tigris y al Hidaspes, y "
            "en la llanura Arioc, rey de los elamitas; y se reunieron muchas "
            "naciones para la batalla de los hijos de Queleul.",
    (1, 7): "Y envió Nabucodonosor, rey de los asirios, a todos los que "
            "habitaban Persia y a todos los que habitaban hacia el occidente, "
            "a los que habitaban Cilicia y Damasco, el Líbano y el "
            "Antilíbano, y a todos los que habitaban frente a la costa,",
    (1, 8): "y a los que estaban entre las naciones del Carmelo y de Galaad y "
            "a la alta Galilea y a la gran llanura de Esdrelón,",
    (1, 9): "y a todos los que estaban en Samaria y en sus ciudades, y al otro "
            "lado del Jordán hasta Jerusalén y Betane y Quelús y Cades y el "
            "río de Egipto, y Tafnas y Ramsés y toda la tierra de Gesén,",
    (1, 10): "hasta llegar más arriba de Tanis y de Menfis, y a todos los que "
             "habitaban Egipto hasta llegar a los términos de Etiopía.",
    (1, 11): "Y todos los que habitaban toda aquella tierra tuvieron en nada "
             "la palabra de Nabucodonosor, rey de los asirios, y no se le "
             "unieron para la guerra, porque no le temieron, sino que estaba "
             "delante de ellos como un hombre igual a cualquiera; y "
             "despidieron a sus mensajeros con las manos vacías y con "
             "deshonra.",
    (1, 12): "Y se enfureció Nabucodonosor sobremanera contra toda aquella "
             "tierra, y juró por su trono y por su reino que se vengaría de "
             "todos los términos de Cilicia y de Damasco y de Siria, y que "
             "mataría a espada a todos los que habitaban en Moab y a los hijos "
             "de Amón y a toda Idumea y a todos los de Egipto, hasta llegar a "
             "los confines de los dos mares.",
    (1, 13): "Y se puso en orden de batalla con su ejército contra el rey "
             "Arfaxad el año diecisiete, y prevaleció en la guerra, y puso en "
             "fuga a todo el ejército de Arfaxad y a toda su caballería y "
             "todos sus carros,",
    (1, 14): "y se enseñoreó de sus ciudades; y llegó hasta Ecbátana, y tomó "
             "las torres y saqueó sus plazas, y convirtió su hermosura en "
             "afrenta suya.",
    (1, 15): "Y prendió a Arfaxad en los montes de Ragau, y lo atravesó con "
             "sus venablos, y acabó con él hasta aquel día.",
    (1, 16): "Y volvió con ellos, él y su ejército, y estuvieron de holganza y "
             "banquete, él y su ejército, ciento veinte días.",

    (2, 1): "Y el año dieciocho, el día veintidós del mes primero, hubo "
            "consejo en la casa de Nabucodonosor, rey de los asirios, para "
            "tomar venganza de toda la tierra, como había dicho.",
    (2, 2): "Y convocó a todos sus siervos y a todos sus magnates, y puso ante "
            "ellos el secreto de su designio, y con su propia boca dio por "
            "consumada toda la maldad de la tierra;",
    (2, 3): "y ellos determinaron destruir a todo el que no hubiese seguido la "
            "palabra de su boca.",
    (2, 4): "Y cuando acabó de tomar su acuerdo, llamó Nabucodonosor, rey de "
            "los asirios, a Holofernes, general en jefe de su ejército, que "
            "era el segundo después de él, y le dijo:",
    (2, 5): "«Así dice el gran rey, el señor de toda la tierra: He aquí, tú "
            "saldrás de mi presencia y tomarás contigo hombres seguros de su "
            "fuerza, ciento veinte mil de a pie y una multitud de caballos con "
            "sus jinetes, doce mil.",
    (2, 6): "Y saldrás al encuentro de toda la tierra del occidente, porque "
            "desobedecieron la palabra de mi boca;",
    (2, 7): "y les mandarás preparar tierra y agua, porque saldré con mi furor "
            "contra ellos y cubriré toda la faz de la tierra con los pies de "
            "mi ejército, y los entregaré a ellos como botín.",
    (2, 8): "Y sus heridos llenarán sus barrancos y sus torrentes, y el río se "
            "desbordará lleno de sus muertos;",
    (2, 9): "y llevaré cautivos a los suyos hasta los extremos de toda la "
            "tierra.",
    (2, 10): "Tú, pues, sal y tómame de antemano todo su territorio; y los que "
             "se te entreguen, guárdamelos para el día de su castigo.",
    (2, 11): "Pero con los rebeldes no perdone tu ojo: entrégalos a la muerte "
             "y al saqueo por toda tu tierra.",
    (2, 12): "Porque, vivo yo y por el poder de mi reino, lo he dicho y lo "
             "haré con mi mano.",
    (2, 13): "Y tú no traspases ni una sola de las palabras de tu señor, sino "
             "cúmplelas del todo, tal como te lo he mandado, y no tardes en "
             "hacerlas».",
    (2, 14): "Y salió Holofernes de la presencia de su señor, y llamó a todos "
             "los príncipes y a los generales y a los jefes del ejército de "
             "Asur,",
    (2, 15): "y contó hombres escogidos para la batalla, como se lo había "
             "mandado su señor, ciento veinte mil, y doce mil arqueros de a "
             "caballo,",
    (2, 16): "y los ordenó del modo en que se forma una multitud para la "
             "guerra.",
    (2, 17): "Y tomó camellos y asnos y mulos para su impedimenta, una "
             "muchedumbre grandísima, y ovejas y bueyes y cabras para su "
             "abastecimiento, sin número,",
    (2, 18): "y provisiones en abundancia para cada hombre, y oro y plata de "
             "la casa del rey, muchísimo.",
    (2, 19): "Y salió él y todo su ejército en marcha, para ir delante del rey "
             "Nabucodonosor y cubrir toda la faz de la tierra hacia el "
             "occidente con carros y jinetes y sus soldados de a pie "
             "escogidos.",
    (2, 20): "Y salió con ellos una gran mezcolanza de gente, como langosta y "
             "como la arena de la tierra, porque no había número por la "
             "multitud de ellos.",
    (2, 21): "Y salieron de Nínive camino de tres días hacia la llanura de "
             "Bectileth, y acamparon desde Bectileth cerca del monte que está "
             "a la izquierda de la alta Cilicia.",
    (2, 22): "Y tomó todo su ejército, los de a pie y los jinetes y sus "
             "carros, y se fue de allí a la montaña.",
    (2, 23): "Y destrozó a Fud y a Lud, y saquearon a todos los hijos de Raséis "
             "y a los hijos de Ismael, los que están frente al desierto, al sur "
             "de la tierra de los caldeos.",
    (2, 24): "Y pasó el Éufrates y atravesó la Mesopotamia, y derribó todas "
             "las ciudades altas que están sobre el torrente Abroná, hasta "
             "llegar al mar.",
    (2, 25): "Y ocupó los términos de Cilicia, y destrozó a todos los que se "
             "le opusieron, y llegó hasta los términos de Jafet, los del sur, "
             "frente a Arabia.",
    (2, 26): "Y rodeó a todos los hijos de Madián, y quemó sus tiendas y "
             "saqueó sus apriscos.",
    (2, 27): "Y bajó a la llanura de Damasco en los días de la siega del "
             "trigo, y quemó todos sus campos, y entregó al exterminio los "
             "rebaños y las vacadas, y despojó sus ciudades y arrasó sus "
             "llanuras, e hirió a todos sus jóvenes a filo de espada.",
    (2, 28): "Y cayó el miedo y el temblor de él sobre los que habitaban la "
             "costa, los que estaban en Sidón y en Tiro, y sobre los que "
             "habitaban Sur y Ocina, y sobre todos los que habitaban Jamnia; y "
             "los que habitaban en Azoto y en Ascalón le temieron sobremanera.",

    (3, 1): "Y le enviaron mensajeros con palabras de paz, diciendo: «He aquí "
            "que nosotros, los siervos de Nabucodonosor el gran rey, estamos "
            "postrados delante de ti; haz con nosotros como bien te parezca.",
    (3, 3): "He aquí nuestras granjas y toda nuestra llanura de trigo y los "
            "rebaños y las vacadas y todos los apriscos de nuestras tiendas "
            "están delante de ti; sírvete de ello como te agrade.",
    (3, 4): "He aquí también nuestras ciudades y los que habitan en ellas son "
            "siervos tuyos; ven y trátalas como bien te parezca».",
    (3, 5): "Y llegaron los hombres ante Holofernes y le refirieron estas "
            "palabras.",
    (3, 6): "Y bajó él y su ejército a la costa, y puso guarniciones en las "
            "ciudades altas, y tomó de ellas hombres escogidos como tropas "
            "auxiliares.",
    (3, 7): "Y lo recibieron ellos y toda su comarca con coronas y danzas y "
            "panderos.",
    (3, 8): "Y él arrasó todos sus términos y taló sus bosques sagrados; "
            "porque se le había dado el encargo de exterminar a todos los "
            "dioses de la tierra, para que a él solo, a Nabucodonosor, "
            "sirvieran todas las naciones, y todas las lenguas y todas sus "
            "tribus lo invocasen como dios.",
    (3, 9): "Y llegó frente a Esdrelón, cerca de Dotea, que está enfrente del "
            "gran desfiladero de Judea,",
    (3, 10): "y acamparon entre Gabaa y la ciudad de los escitas; y estuvo "
             "allí un mes de días, para reunir toda la impedimenta de su "
             "ejército.",

    (4, 1): "Y oyeron los hijos de Israel que habitaban en Judea todo cuanto "
            "había hecho a las naciones Holofernes, el general en jefe de "
            "Nabucodonosor, rey de los asirios, y de qué modo había despojado "
            "todos sus templos y los había entregado al exterminio;",
    (4, 2): "y temieron en gran manera delante de él, y se turbaron por "
            "Jerusalén y por el templo del Señor su Dios,",
    (4, 3): "porque hacía poco que habían subido del cautiverio, y de poco "
            "tiempo atrás se había vuelto a reunir todo el pueblo de Judea, y "
            "los utensilios y el altar y la Casa habían sido consagrados "
            "después de la profanación.",
    (4, 4): "Y enviaron avisos a todo el territorio de Samaria, y a Coná y "
            "Bet-Horón y Belmén y Jericó, y a Cobá y Esorá y al valle de "
            "Salem,",
    (4, 5): "y ocuparon de antemano todas las cumbres de los montes altos, y "
            "fortificaron con muros las aldeas que hay en ellos, y almacenaron "
            "víveres como preparativo de guerra, porque hacía poco que sus "
            "campos habían sido segados.",
    (4, 6): "Y escribió Joacim, el sumo sacerdote, que estaba en aquellos días "
            "en Jerusalén, a los que habitaban Betulia y Betomestáim, que está "
            "enfrente de Esdrelón, frente a la llanura que está cerca de "
            "Dotán,",
    (4, 7): "diciéndoles que guardasen las subidas de la montaña, porque por "
            "ellas era la entrada a Judea; y era fácil detener a los que "
            "subían, por ser estrecho el paso, sólo para dos hombres a lo "
            "sumo.",
    (4, 8): "Y los hijos de Israel hicieron como les mandó Joacim el sumo "
            "sacerdote y el consejo de ancianos de todo el pueblo de Israel, "
            "que residía en Jerusalén.",
    (4, 9): "Y clamó todo hombre de Israel a Dios con gran insistencia, y "
            "humillaron sus almas con gran insistencia,",
    (4, 10): "ellos y sus mujeres y sus niños y sus ganados; y todo forastero "
             "y jornalero y esclavo comprado por dinero se ciñeron cilicio a "
             "los lomos.",
    (4, 11): "Y todo hombre de Israel, y las mujeres y los niños que habitaban "
             "en Jerusalén, cayeron rostro a tierra delante del templo, y se "
             "echaron ceniza sobre la cabeza, y extendieron sus cilicios "
             "delante del Señor;",
    (4, 12): "y cubrieron de cilicio el altar, y clamaron al Dios de Israel "
             "todos a una con insistencia, para que no entregase al saqueo a "
             "sus niños ni a sus mujeres al botín, ni las ciudades de su "
             "heredad al exterminio, ni el santuario a la profanación y a la "
             "afrenta, irrisión de las naciones.",
    (4, 13): "Y el Señor escuchó su voz y miró su aflicción; y el pueblo estuvo "
             "ayunando muchos días en toda Judea y en Jerusalén, delante del "
             "santuario del Señor Todopoderoso.",
    (4, 14): "Y Joacim el sumo sacerdote y todos los que estaban delante del "
             "Señor, los sacerdotes y los que servían al Señor, ceñidos de "
             "cilicio los lomos, ofrecían el holocausto perpetuo y los votos y "
             "las ofrendas voluntarias del pueblo;",
    (4, 15): "y había ceniza sobre sus turbantes; y clamaban al Señor con "
             "todas sus fuerzas, para que visitase con bien a toda la casa de "
             "Israel.",

    (5, 1): "Y se le anunció a Holofernes, general en jefe del ejército de "
            "Asur, que los hijos de Israel se habían preparado para la guerra, "
            "y que habían cerrado los pasos de la montaña y amurallado toda "
            "cumbre de monte alto, y que habían puesto trampas en las "
            "llanuras.",
    (5, 2): "Y se airó con gran furor, y llamó a todos los príncipes de Moab y "
            "a los generales de Amón y a todos los sátrapas de la costa,",
    (5, 3): "y les dijo: «Decidme, hijos de Canaán: ¿quién es este pueblo que "
            "está asentado en la montaña, y cuáles son las ciudades que "
            "habitan, y cuál la multitud de su ejército, y en qué está su "
            "poder y su fuerza, y qué rey se ha levantado sobre ellos como "
            "caudillo de su ejército,",
    (5, 4): "y por qué han vuelto la espalda y no han venido a mi encuentro, a "
            "diferencia de todos los que habitan en el occidente?».",
    (5, 5): "Y le dijo Ajior, el caudillo de todos los hijos de Amón: «Oiga mi "
            "señor una palabra de boca de tu siervo, y te diré la verdad "
            "acerca del pueblo que habita esta montaña, cerca de donde tú "
            "estás; y no saldrá mentira de la boca de tu siervo.",
    (5, 6): "Este pueblo son descendientes de los caldeos;",
    (5, 7): "y habitaron antes como forasteros en Mesopotamia, porque no "
            "quisieron seguir a los dioses de sus padres, que estaban en "
            "tierra de los caldeos.",
    (5, 8): "Se apartaron del camino de sus progenitores y adoraron al Dios "
            "del cielo, al Dios a quien reconocieron; y los echaron de delante "
            "de sus dioses, y huyeron a Mesopotamia, y habitaron allí como "
            "forasteros muchos días.",
    (5, 9): "Y les dijo su Dios que saliesen del lugar donde habitaban como "
            "forasteros y que fuesen a la tierra de Canaán; y habitaron allí, "
            "y se llenaron de oro y de plata y de ganados en gran abundancia.",
    (5, 10): "Y bajaron a Egipto, porque el hambre cubrió la faz de la tierra "
             "de Canaán, y habitaron allí como forasteros mientras hubo con "
             "qué sustentarse; y llegaron a ser allí una gran multitud, y no "
             "había número para su linaje.",
    (5, 11): "Y se levantó contra ellos el rey de Egipto, y los explotaron con "
             "trabajos y con ladrillo, y los humillaron y los pusieron por "
             "esclavos.",
    (5, 12): "Y clamaron a su Dios, y él hirió toda la tierra de Egipto con "
             "plagas para las que no había remedio; y los egipcios los echaron "
             "de su presencia.",
    (5, 13): "Y Dios secó el mar Rojo delante de ellos,",
    (5, 14): "y los llevó por el camino del Sinaí y de Cades Barnea; y echaron "
             "a todos los que habitaban en el desierto,",
    (5, 15): "y habitaron en tierra de los amorreos, y a todos los hesebonitas "
             "los exterminaron con su fuerza; y pasando el Jordán, recibieron "
             "en heredad toda la montaña.",
    (5, 16): "Y echaron de delante de sí al cananeo y al ferezeo y al jebuseo "
             "y a Siquem y a todos los guergueseos, y habitaron allí muchos "
             "días.",
    (5, 17): "Y mientras no pecaron delante de su Dios, les fue bien, porque "
             "está con ellos un Dios que aborrece la injusticia;",
    (5, 18): "pero cuando se apartaron del camino que él les había señalado, "
             "fueron destruidos en muchas guerras, muchísimo, y fueron "
             "llevados cautivos a tierra ajena, y el templo de su Dios fue "
             "arrasado hasta el suelo, y sus ciudades fueron tomadas por sus "
             "enemigos.",
    (5, 19): "Y ahora, habiéndose vuelto a su Dios, han subido de la "
             "dispersión en que habían sido dispersados, y han ocupado "
             "Jerusalén, donde está su santuario, y se han asentado en la "
             "montaña, porque estaba desierta.",
    (5, 20): "Y ahora, soberano señor: si hay en este pueblo alguna falta y "
             "están pecando contra su Dios, y comprobamos que esa es la "
             "piedra de tropiezo que hay en ellos, subamos y hagámosles la "
             "guerra;",
    (5, 21): "pero si no hay iniquidad en su nación, pase de largo mi señor, "
             "no sea que su Señor y su Dios los escude, y quedemos por "
             "oprobio delante de toda la tierra».",
    (5, 22): "Y sucedió que, cuando Ajior acabó de decir estas palabras, murmuró "
             "todo el pueblo que rodeaba la tienda y estaba alrededor; y los "
             "magnates de Holofernes y todos los que habitaban la costa y Moab "
             "dijeron que lo hiciesen pedazos:",
    (5, 23): "«Porque no vamos a tener miedo de los hijos de Israel. Mira: es "
             "un pueblo en el que no hay ejército ni fuerza para una batalla "
             "reñida.",
    (5, 24): "Por eso subamos, y serán pasto de todo tu ejército, soberano "
             "Holofernes».",

    (6, 1): "Y cuando cesó el tumulto de los hombres que rodeaban el consejo, "
            "dijo Holofernes, general en jefe del ejército de Asur, a Ajior "
            "delante de todo aquel pueblo de extranjeros, y a todos los hijos "
            "de Moab:",
    (6, 2): "«¿Y quién eres tú, Ajior, y los mercenarios de Efraín, para "
            "profetizar entre nosotros como has hecho hoy, y decir que no "
            "hagamos guerra al linaje de Israel porque su Dios los escuda? ¿Y "
            "quién es Dios sino Nabucodonosor? Él enviará su poder y los "
            "exterminará de la faz de la tierra, y no los librará su Dios;",
    (6, 3): "sino que nosotros, sus siervos, los heriremos como a un solo "
            "hombre, y no resistirán el ímpetu de nuestros caballos.",
    (6, 4): "Porque los abrasaremos con ellos, y sus términos se embriagarán "
            "con su sangre, y sus llanuras se llenarán de sus muertos; y ni la "
            "huella de sus pies resistirá delante de nosotros, sino que "
            "perecerán del todo, dice el rey Nabucodonosor, señor de toda la "
            "tierra; porque dijo, y no quedará sin cumplirse ninguna de las "
            "palabras que ha dicho.",
    (6, 5): "Y tú, Ajior, mercenario de Amón, que has dicho estas palabras en "
            "el día de tu iniquidad, no volverás a ver mi rostro desde este "
            "día hasta que yo tome venganza del linaje de los que salieron de "
            "Egipto;",
    (6, 6): "y entonces el hierro de mi ejército y el pueblo de mis siervos te "
            "atravesarán los costados, y caerás entre sus heridos cuando yo "
            "vuelva.",
    (6, 7): "Y mis siervos te llevarán a la montaña y te dejarán en una de las "
            "ciudades de las subidas,",
    (6, 8): "y no morirás hasta que seas exterminado con ellos.",
    (6, 9): "Y si acaso esperas en tu corazón que no serán tomados, que no se "
            "te venga abajo el semblante. Lo he dicho, y no caerá en vano "
            "ninguna de mis palabras».",
    (6, 10): "Y mandó Holofernes a sus siervos, los que estaban de pie en su "
             "tienda, que prendiesen a Ajior y lo llevasen a Betulia y lo "
             "entregasen en manos de los hijos de Israel.",
    (6, 11): "Y lo prendieron sus siervos y lo sacaron fuera del campamento, a "
             "la llanura, y partieron de en medio del llano hacia la montaña, "
             "y llegaron a las fuentes que estaban debajo de Betulia.",
    (6, 12): "Y cuando los hombres de la ciudad los vieron en la cumbre del "
             "monte, tomaron sus armas y salieron fuera de la ciudad a la "
             "cumbre del monte; y todos los honderos les cerraron la subida y "
             "les tiraban piedras.",
    (6, 13): "Y ellos, poniéndose a cubierto al pie del monte, ataron a Ajior "
             "y lo dejaron tirado al pie del monte, y se volvieron a su señor.",
    (6, 14): "Y bajando los hijos de Israel de su ciudad, se acercaron a él, y "
             "desatándolo lo llevaron a Betulia, y lo presentaron a los "
             "príncipes de su ciudad,",
    (6, 15): "que eran en aquellos días Ozías hijo de Micá, de la tribu de "
             "Simeón, y Cabris hijo de Gotoniel, y Carmis hijo de Melquiel.",
    (6, 16): "Y convocaron a todos los ancianos de la ciudad, y acudieron "
             "corriendo todos sus jóvenes y las mujeres a la asamblea; y "
             "pusieron a Ajior en medio de todo el pueblo, y le preguntó Ozías "
             "qué había sucedido.",
    (6, 17): "Y él respondiendo les contó lo dicho en el consejo de Holofernes, "
             "y todas las palabras que él había dicho en medio de los "
             "príncipes de los hijos de Asur, y cuantas arrogancias había "
             "proferido Holofernes contra la casa de Israel.",
    (6, 18): "Y postrándose el pueblo adoró a Dios, y clamaron diciendo:",
    (6, 19): "«Señor, Dios del cielo, mira su soberbia, y ten compasión de la "
             "humillación de nuestro linaje, y vuelve tu rostro hacia los que "
             "te han sido consagrados en este día».",
    (6, 20): "Y consolaron a Ajior, y lo alabaron mucho.",
    (6, 21): "Y Ozías lo llevó consigo desde la asamblea a su casa, e hizo un "
             "banquete a los ancianos; e invocaron al Dios de Israel pidiendo "
             "auxilio toda aquella noche.",

    (7, 1): "Al día siguiente mandó Holofernes a todo su ejército y a todo el "
            "pueblo que había venido en su ayuda que levantasen el campamento "
            "hacia Betulia, y que tomasen de antemano las subidas de la "
            "montaña y diesen guerra a los hijos de Israel.",
    (7, 2): "Y levantó el campamento aquel día todo hombre valiente de ellos; "
            "y su ejército era de hombres de guerra: ciento setenta mil de a "
            "pie y doce mil de a caballo, sin contar la impedimenta y los "
            "hombres que iban a pie con ella, muchedumbre grandísima.",
    (7, 3): "Y acamparon en el valle cerca de Betulia, junto a la fuente, y se "
            "extendieron a lo ancho desde Dotán hasta Belbáim, y a lo largo "
            "desde Betulia hasta Ciamón, que está enfrente de Esdrelón.",
    (7, 4): "Y los hijos de Israel, cuando vieron su multitud, se turbaron en "
            "gran manera, y se decían unos a otros: «Ahora éstos van a lamer "
            "la faz de toda la tierra, y ni los montes altos ni los barrancos "
            "ni las colinas resistirán su peso».",
    (7, 5): "Y tomando cada uno sus armas de guerra, y encendiendo hogueras en "
            "sus torres, estuvieron en guardia toda aquella noche.",
    (7, 6): "Y al día segundo sacó Holofernes toda su caballería a la vista de "
            "los hijos de Israel que estaban en Betulia,",
    (7, 7): "y reconoció las subidas de su ciudad, y recorrió las fuentes de "
            "las aguas y las tomó de antemano, y puso en ellas destacamentos "
            "de hombres de guerra; y él se volvió a su gente.",
    (7, 8): "Y acercándose a él todos los príncipes de los hijos de Esaú y "
            "todos los caudillos del pueblo de Moab y los generales de la "
            "costa, dijeron:",
    (7, 9): "«Escuche nuestro soberano una palabra, para que no haya quebranto "
            "en tu ejército.",
    (7, 10): "Porque este pueblo de los hijos de Israel no confía en sus "
             "lanzas, sino en la altura de sus montes, en los que ellos "
             "habitan; y no es fácil subir a las cumbres de sus montes.",
    (7, 11): "Y ahora, soberano, no les hagas guerra como se hace una guerra "
             "en campo abierto, y no caerá ni un solo hombre de tu pueblo.",
    (7, 12): "Quédate en tu campamento, guardando a todo hombre de tu "
             "ejército, y apodérense tus siervos de la fuente de agua que sale "
             "al pie del monte,",
    (7, 13): "porque de allí sacan agua todos los que habitan Betulia; y los "
             "matará la sed, y entregarán su ciudad. Y nosotros y nuestra "
             "gente subiremos a las cumbres de los montes cercanos y "
             "acamparemos en ellas como avanzada, para que no salga de la "
             "ciudad ni un solo hombre.",
    (7, 14): "Y se consumirán de hambre ellos y sus mujeres y sus hijos, y "
             "antes que venga sobre ellos la espada quedarán tendidos en las "
             "plazas donde viven;",
    (7, 15): "y les darás el pago que merecen por haberse rebelado y no haber "
             "salido en paz al encuentro de tu persona».",
    (7, 16): "Y agradaron sus palabras a Holofernes y a todos sus siervos, y "
             "mandó hacer como habían dicho.",
    (7, 17): "Y partió el destacamento de los hijos de Amón, y con ellos cinco "
             "mil de los hijos de Asur, y acamparon en el valle y se "
             "apoderaron de las aguas y de las fuentes de las aguas de los "
             "hijos de Israel.",
    (7, 18): "Y subieron los hijos de Esaú y los hijos de Amón, y acamparon en "
             "la montaña enfrente de Dotán; y enviaron de entre ellos hacia el "
             "sur y hacia el oriente, enfrente de Egrebel, que está cerca de "
             "Cus, que está sobre el torrente Mocmur. Y el resto del ejército "
             "de los asirios acampó en la llanura y cubrió toda la faz de la "
             "tierra, y sus tiendas y su impedimenta se extendieron en gran "
             "muchedumbre, y eran una multitud grandísima.",
    (7, 19): "Y los hijos de Israel clamaron al Señor su Dios, porque se les "
             "acobardó el ánimo, pues los habían cercado todos sus enemigos y "
             "no había modo de escapar de entre ellos.",
    (7, 20): "Y permaneció alrededor de ellos todo el campamento de Asur —los "
             "de a pie y los carros y sus jinetes— treinta y cuatro días; y a "
             "todos los que habitaban Betulia se les acabó el agua de todas "
             "sus vasijas,",
    (7, 21): "y las cisternas se vaciaban, y no tenían agua para beber hasta "
             "saciarse ni un solo día, porque se la daban a beber por medida.",
    (7, 22): "Y desfallecieron sus niños, y las mujeres y los jóvenes "
             "desmayaban de sed, y caían por las plazas de la ciudad y por los "
             "pasos de las puertas, y ya no había fuerza en ellos.",
    (7, 23): "Y se juntó todo el pueblo contra Ozías y contra los príncipes de "
             "la ciudad, los jóvenes y las mujeres y los niños, y clamaron a "
             "gran voz y dijeron delante de los ancianos:",
    (7, 24): "«Juzgue Dios entre vosotros y nosotros, porque habéis cometido "
             "con nosotros una gran injusticia al no tratar de paz con los "
             "hijos de Asur.",
    (7, 25): "Y ahora no hay quien nos socorra, sino que Dios nos ha vendido "
             "en sus manos para que caigamos delante de ellos de sed y de "
             "muerte espantosa.",
    (7, 26): "Y ahora llamadlos y entregad toda la ciudad como botín a la "
             "gente de Holofernes y a todo su ejército;",
    (7, 27): "porque más nos vale caer en sus manos como presa: seremos "
             "esclavos, pero viviremos, y no veremos con nuestros ojos la "
             "muerte de nuestros niños, ni a nuestras mujeres y a nuestros "
             "hijos exhalar el alma.",
    (7, 28): "Os ponemos por testigos el cielo y la tierra, y a nuestro Dios y "
             "Señor de nuestros padres, que nos castiga conforme a nuestros "
             "pecados y conforme a los pecados de nuestros padres, para que no "
             "haga hoy como estas palabras dicen».",
    (7, 29): "Y hubo un gran llanto en medio de la asamblea, todos a una, y "
             "clamaron al Señor Dios a gran voz.",
    (7, 30): "Y les dijo Ozías: «Tened ánimo, hermanos; aguantemos todavía "
             "cinco días, en los cuales el Señor nuestro Dios volverá a "
             "nosotros su misericordia, porque no nos abandonará del todo.",
    (7, 31): "Y si pasan y no nos viene socorro, haré conforme a vuestras "
             "palabras».",
    (7, 32): "Y dispersó al pueblo, cada uno a su puesto, y fueron a los muros "
             "y a las torres de su ciudad; y a las mujeres y a los niños los "
             "mandó a sus casas. Y estaban en la ciudad muy abatidos.",

    (8, 1): "Y oyó en aquellos días Judit, hija de Merarí, hijo de Ox, hijo de "
            "José, hijo de Oziel, hijo de Elcías, hijo de Elías, hijo de "
            "Jilquías, hijo de Eliab, hijo de Natanael, hijo de Salamiel, hijo "
            "de Sarasadai, hijo de Israel.",
    (8, 2): "Y su marido, Manasés, era de su misma tribu y de su misma "
            "familia; y murió en los días de la siega de la cebada,",
    (8, 3): "porque estaba de pie junto a los que ataban las gavillas en el "
            "campo, y le dio una insolación en la cabeza, y cayó en cama y "
            "murió en Betulia, su ciudad; y lo sepultaron con sus padres en el "
            "campo que está entre Dotán y Balamón.",
    (8, 4): "Y estaba Judit en su casa, viuda, hacía tres años y cuatro meses.",
    (8, 5): "Y se hizo una tienda sobre el terrado de su casa, y se ciñó "
            "cilicio a los lomos, y llevaba puestos los vestidos de su viudez.",
    (8, 6): "Y ayunaba todos los días de su viudez, salvo las vísperas de "
            "sábado y los sábados, y las vísperas de luna nueva y las lunas "
            "nuevas, y las fiestas y los días de alegría de la casa de Israel.",
    (8, 7): "Y era hermosa de aspecto y muy bella de rostro; y le había dejado "
            "Manasés, su marido, oro y plata y siervos y siervas y ganados y "
            "campos, y ella se quedó al frente de todo ello.",
    (8, 8): "Y no había quien dijese de ella una palabra mala, porque temía a "
            "Dios en gran manera.",
    (8, 9): "Y oyó las palabras airadas del pueblo contra el gobernador, "
            "porque se habían acobardado por la falta de agua; y oyó Judit "
            "todo lo que Ozías les había dicho, que les había jurado entregar "
            "la ciudad a los asirios al cabo de cinco días.",
    (8, 10): "Y enviando a su doncella, la que estaba al frente de todos sus "
             "bienes, llamó a Cabris y a Carmis, los ancianos de su ciudad.",
    (8, 11): "Y vinieron a ella, y les dijo: «Oídme, príncipes de los "
             "habitantes de Betulia: no es recto lo que habéis hablado hoy "
             "delante del pueblo, y habéis puesto un juramento —el que "
             "pronunciasteis entre Dios y vosotros— diciendo que entregaréis "
             "la ciudad a nuestros enemigos si en esos días el Señor no os "
             "envía socorro.",
    (8, 12): "Y ahora, ¿quiénes sois vosotros para haber tentado hoy a Dios y "
             "para poneros en lugar de Dios en medio de los hijos de los "
             "hombres?",
    (8, 13): "Ahora estáis poniendo a prueba al Señor Todopoderoso, y jamás "
             "entenderéis nada.",
    (8, 14): "Porque no alcanzáis el fondo del corazón de un hombre, ni "
             "penetráis los razonamientos de su mente; ¿y cómo vais a escudriñar "
             "a Dios, que hizo todas estas cosas, y a conocer su pensamiento y "
             "a comprender su designio? De ninguna manera, hermanos: no "
             "provoquéis la ira del Señor nuestro Dios.",
    (8, 15): "Porque si él no quiere socorrernos dentro de esos cinco días, "
             "tiene poder para protegernos los días que quiera, o también para "
             "destruirnos delante de nuestros enemigos.",
    (8, 16): "Pero vosotros no toméis en prenda los designios del Señor "
             "nuestro Dios, porque Dios no es como un hombre, a quien se "
             "amenaza, ni como un hijo de hombre, a quien se le pone pleito.",
    (8, 17): "Por eso, esperando la salvación que viene de él, invoquémoslo en "
             "nuestra ayuda, y escuchará nuestra voz si le place.",
    (8, 18): "Porque no ha habido en nuestras generaciones, ni hay en el día "
             "de hoy, ni tribu ni familia ni pueblo ni ciudad entre nosotros "
             "que adore a dioses hechos por mano de hombre, como sucedió en "
             "los días de antes,",
    (8, 19): "por lo cual nuestros padres fueron entregados a la espada y al "
             "saqueo, y cayeron en gran ruina delante de nuestros enemigos.",
    (8, 20): "Pero nosotros no reconocemos otro Dios fuera de él; por eso "
             "esperamos que no nos mirará con desdén, ni a ninguno de los "
             "nuestros.",
    (8, 21): "Porque si nos toman, así quedará también toda Judea, y nuestro "
             "santuario será saqueado, y Dios pedirá cuenta de su profanación "
             "a costa de nuestra sangre,",
    (8, 22): "y la matanza de nuestros hermanos y el cautiverio de la tierra y "
             "la desolación de nuestra heredad las hará recaer sobre nuestra "
             "cabeza entre las naciones dondequiera que seamos esclavos; y "
             "seremos motivo de tropiezo y de oprobio delante de los que nos "
             "posean.",
    (8, 23): "Porque nuestra esclavitud no será para bien, sino que el Señor "
             "nuestro Dios la convertirá en deshonra.",
    (8, 24): "Y ahora, hermanos, demos ejemplo a nuestros hermanos, porque de "
             "nosotros pende su vida, y el santuario y la Casa y el altar "
             "descansan sobre nosotros.",
    (8, 25): "Por todo esto, demos gracias al Señor nuestro Dios, que nos "
             "prueba como también probó a nuestros padres.",
    (8, 26): "Acordaos de cuanto hizo con Abrahán, y de cómo probó a Isaac, y "
             "de lo que le sucedió a Jacob en Mesopotamia de Siria, cuando "
             "apacentaba las ovejas de Labán, hermano de su madre.",
    (8, 27): "Porque no nos ha metido en el fuego como a ellos, para escudriñar "
             "su corazón, ni ha tomado venganza de nosotros; sino que para "
             "corregirlos azota el Señor a los que se le acercan».",
    (8, 28): "Y le dijo Ozías: «Todo lo que has dicho lo has hablado con buen "
             "corazón, y no hay quien pueda contradecir tus palabras.",
    (8, 29): "Porque no es de hoy tu sabiduría manifiesta, sino que desde el "
             "principio de tus días todo el pueblo conoce tu inteligencia, "
             "porque es bueno lo que tu corazón ha forjado.",
    (8, 30): "Pero el pueblo tenía una sed terrible, y nos obligaron a hacer "
             "como les dijimos y a echar sobre nosotros un juramento que no "
             "quebrantaremos.",
    (8, 31): "Y ahora, ruega por nosotros, porque eres mujer piadosa, y "
             "enviará el Señor la lluvia para llenar nuestras cisternas, y ya "
             "no desfalleceremos».",
    (8, 32): "Y les dijo Judit: «Escuchadme, y haré una cosa que llegará a los "
             "hijos de nuestro linaje de generación en generación.",
    (8, 33): "Vosotros estaréis esta noche junto a la puerta, y saldré yo con "
             "mi doncella; y dentro de los días después de los cuales dijisteis "
             "que entregaríais la ciudad a nuestros enemigos, el Señor visitará "
             "a Israel por mi mano.",
    (8, 34): "Pero vosotros no indaguéis lo que voy a hacer, porque no os lo "
             "diré hasta que esté cumplido».",
    (8, 35): "Y le dijeron Ozías y los príncipes: «Vete en paz, y el Señor Dios "
             "vaya delante de ti para tomar venganza de nuestros enemigos».",
    (8, 36): "Y saliendo de la tienda, se fueron a sus puestos.",

    (9, 1): "Y Judit se postró rostro en tierra, y se echó ceniza sobre la "
            "cabeza, y descubrió el cilicio que llevaba puesto. Y era la hora "
            "en que se ofrecía en Jerusalén, en la casa de Dios, el incienso "
            "de aquella tarde; y clamó Judit a gran voz al Señor, y dijo:",
    (9, 2): "«Señor, Dios de mi padre Simeón, a quien pusiste en la mano una "
            "espada para tomar venganza de los extranjeros que desataron el "
            "seno de una virgen para mancharla, y descubrieron su muslo para "
            "su vergüenza, y profanaron su seno para su afrenta —porque tú "
            "dijiste: “No será así”, y ellos lo hicieron—:",
    (9, 3): "por eso entregaste a sus príncipes a la muerte, y su lecho, que "
            "se avergonzó de su engaño, fue engañado hasta la sangre; e "
            "heriste a los siervos junto con los poderosos, y a los poderosos "
            "sobre sus tronos;",
    (9, 4): "y entregaste sus mujeres al botín y sus hijas al cautiverio, y "
            "todos sus despojos al reparto de los hijos amados por ti, que "
            "ardieron con tu mismo celo y aborrecieron la mancha de su sangre "
            "y te invocaron como auxiliador. Oh Dios, Dios mío, escúchame "
            "también a mí, que soy viuda.",
    (9, 5): "Porque tú hiciste lo que a aquello precedió, y aquello mismo, y "
            "lo que vino después, y lo de ahora, y lo que ha de venir; y "
            "sucedió lo que tú pensaste,",
    (9, 6): "y se presentaron las cosas que habías determinado y dijeron: "
            "«Aquí estamos»; porque todos tus caminos están dispuestos, y tu "
            "juicio se hace con previo conocimiento.",
    (9, 7): "Porque mira: los asirios se han crecido con su ejército, se han "
            "engreído con el caballo y el jinete, se han jactado de la fuerza "
            "de su infantería, han puesto su esperanza en el escudo y en la "
            "jabalina y en el arco y en la honda, y no han conocido que tú "
            "eres el Señor que quebranta las guerras.",
    (9, 8): "«Señor» es tu nombre. Rompe tú su fuerza con tu poder, y abate su "
            "vigor con tu furor; porque han determinado profanar tu santuario, "
            "manchar la morada donde reposa el nombre de tu gloria, y derribar "
            "con el hierro el cuerno de tu altar.",
    (9, 9): "Mira su soberbia, envía tu ira sobre sus cabezas, pon en mi mano, "
            "de viuda, la fuerza que he pensado.",
    (9, 10): "Hiere al siervo por los labios de mi engaño junto con el "
             "príncipe, y al príncipe junto con su criado; quiebra su "
             "arrogancia por mano de una mujer.",
    (9, 11): "Porque tu poder no está en el número, ni tu señorío en los "
             "fuertes; sino que eres Dios de los humildes, auxiliador de los "
             "pequeños, amparo de los débiles, refugio de los desamparados, "
             "salvador de los desesperados.",
    (9, 12): "Sí, sí: Dios de mi padre y Dios de la heredad de Israel, "
             "soberano de los cielos y de la tierra, creador de las aguas, rey "
             "de toda tu creación, escucha tú mi súplica,",
    (9, 13): "y haz que mi palabra y mi engaño sean herida y azote para los "
             "que han tramado cosas duras contra tu alianza y contra tu casa "
             "consagrada y contra la cumbre de Sión y contra la casa que tus "
             "hijos poseen.",
    (9, 19): "Y haz que toda tu nación y toda tribu reconozcan y sepan que tú "
             "eres el Dios de todo poder y de toda fuerza, y que no hay otro "
             "que escude al linaje de Israel sino tú».",

    (10, 1): "Y sucedió que, cuando dejó de clamar al Dios de Israel y acabó "
             "todas estas palabras,",
    (10, 2): "se levantó de donde estaba postrada, y llamó a su doncella, y "
             "bajó a la sala en que solía estar los días de sábado y en sus "
             "fiestas;",
    (10, 3): "y se quitó el cilicio que llevaba puesto y se despojó de los "
             "vestidos de su viudez; y se lavó el cuerpo con agua y se ungió "
             "con perfume espeso, y se arregló los cabellos de la cabeza y se "
             "puso una diadema, y se vistió sus vestidos de fiesta, con los "
             "que se engalanaba en los días de la vida de Manasés su marido;",
    (10, 4): "y se calzó sandalias en los pies, y se puso las ajorcas y los "
             "brazaletes y los anillos y los pendientes y todas sus joyas; y "
             "se hermoseó en gran manera, para atraer los ojos de cuantos "
             "hombres la viesen.",
    (10, 5): "Y dio a su doncella un odre de vino y una alcuza de aceite, y "
             "llenó una alforja de harina tostada y de tortas de higos y de "
             "panes puros; y envolvió todas sus vasijas y se las puso encima.",
    (10, 6): "Y salieron hacia la puerta de la ciudad de Betulia, y hallaron "
             "de pie junto a ella a Ozías y a los ancianos de la ciudad, "
             "Cabris y Carmis.",
    (10, 7): "Y cuando la vieron —y estaba cambiado su rostro y mudado su "
             "vestido—, se maravillaron de su hermosura en gran manera, y le "
             "dijeron:",
    (10, 8): "«El Dios de nuestros padres te conceda gracia y lleve a término "
             "lo que te propones, para orgullo de los hijos de Israel y honra "
             "de Jerusalén». Y ella adoró a Dios,",
    (10, 9): "y les dijo: «Mandad que me abran la puerta de la ciudad, y "
             "saldré a cumplir las cosas de que habéis hablado conmigo». Y "
             "mandaron a los jóvenes que se la abriesen, como ella había "
             "dicho.",
    (10, 10): "Y lo hicieron así. Y salió Judit, ella y su criada con ella; y "
              "los hombres de la ciudad la siguieron con la vista mientras "
              "bajaba el monte, hasta que atravesó el valle y ya no la vieron "
              "más.",
    (10, 11): "E iban derechas por el valle, y les salió al encuentro una "
              "avanzada de los asirios,",
    (10, 12): "y la prendieron y le preguntaron: «¿De quién eres, y de dónde "
              "vienes, y adónde vas?». Y ella dijo: «Soy hija de los hebreos, "
              "y huyo de ellos, porque están a punto de seros entregados para "
              "que los devoréis;",
    (10, 13): "y yo voy a presentarme a Holofernes, general en jefe de "
              "vuestro ejército, para anunciarle palabras de verdad; y le "
              "mostraré un camino por el que puede ir y dominar toda la "
              "montaña sin que se le pierda ni uno solo de sus hombres, ni "
              "carne ni aliento de vida».",
    (10, 14): "Y cuando los hombres oyeron sus palabras y le miraron el "
              "rostro, les pareció maravillosa en su hermosura, y le dijeron:",
    (10, 15): "«Has salvado tu vida al darte prisa en bajar a la presencia de "
              "nuestro señor. Ve, pues, ahora a su tienda, y algunos de los "
              "nuestros te escoltarán hasta ponerte en sus manos.",
    (10, 16): "Y cuando estés delante de él, no temas en tu corazón, sino "
              "anúnciale lo que has dicho, y él te tratará bien».",
    (10, 17): "Y escogieron de entre ellos cien hombres, y los pusieron de "
              "escolta a ella y a su doncella, y las llevaron a la tienda de "
              "Holofernes.",
    (10, 18): "Y hubo gran concurrencia en el campamento, porque su llegada "
              "corrió de tienda en tienda; y viniendo, la rodeaban mientras "
              "estaba fuera de la tienda de Holofernes, hasta que le dieron "
              "aviso de ella.",
    (10, 19): "Y se maravillaban de su hermosura, y por ella se maravillaban "
              "de los hijos de Israel; y se decían unos a otros: «¿Quién ha de "
              "despreciar a este pueblo, que tiene consigo mujeres así? "
              "Porque no está bien dejar con vida ni a uno solo de ellos: los "
              "que quedaran serían capaces de engañar a toda la tierra».",
    (10, 20): "Y salieron los de la guardia de Holofernes y todos sus "
              "servidores, y la metieron en la tienda.",
    (10, 21): "Y estaba Holofernes reposando sobre su lecho, bajo el "
              "mosquitero, que era de púrpura y oro y esmeralda y piedras "
              "preciosas entretejidas.",
    (10, 22): "Y le hablaron de ella, y él salió al vestíbulo de la tienda, y "
              "delante de él iban lámparas de plata.",
    (10, 23): "Y cuando Judit llegó ante él y ante sus servidores, todos se "
              "maravillaron de la hermosura de su rostro; y ella, postrándose "
              "rostro en tierra, se inclinó ante él, y sus siervos la "
              "levantaron.",

    (11, 1): "Y le dijo Holofernes: «Ten ánimo, mujer; no temas en tu corazón, "
             "porque yo no he hecho mal a nadie que haya querido servir a "
             "Nabucodonosor, rey de toda la tierra.",
    (11, 2): "Y ahora, tu pueblo, el que habita la montaña: si no me hubieran "
             "tenido en nada, no habría levantado mi lanza contra ellos; ellos "
             "mismos se lo han hecho.",
    (11, 3): "Y ahora, dime por qué has huido de ellos y has venido a "
             "nosotros; porque has venido a salvarte. Ten ánimo: esta noche "
             "vivirás, y en adelante también;",
    (11, 4): "porque no hay quien te haga daño, sino que te tratarán bien, "
             "como se hace con los siervos de mi señor el rey Nabucodonosor».",
    (11, 5): "Y le dijo Judit: «Recibe las palabras de tu sierva, y hable tu "
             "criada delante de ti; y no diré mentira a mi señor esta noche.",
    (11, 6): "Y si sigues las palabras de tu criada, Dios llevará a cabo "
             "contigo la empresa, y mi señor no fracasará en sus designios.",
    (11, 7): "Porque vive Nabucodonosor, rey de toda la tierra, y vive su "
             "poder, el que te envió a poner en orden a toda alma viviente: "
             "que no sólo los hombres le sirven por ti, sino que también las "
             "fieras del campo y los ganados y las aves del cielo vivirán, por "
             "tu fuerza, para Nabucodonosor y para toda su casa.",
    (11, 8): "Porque hemos oído de tu sabiduría y de la habilidad de tu "
             "espíritu, y se ha anunciado por toda la tierra que tú eres el "
             "único capaz en todo el reino, poderoso en saber y admirable en "
             "las campañas de guerra.",
    (11, 9): "Y ahora, en cuanto a lo que dijo Ajior en tu consejo: hemos oído "
             "sus palabras, porque los hombres de Betulia le perdonaron la "
             "vida y él les contó todo cuanto había dicho ante ti.",
    (11, 10): "Por eso, soberano señor, no pases por alto su palabra, sino "
              "guárdala en tu corazón, porque es verdadera: nuestro linaje no "
              "es castigado, ni prevalece la espada contra ellos, si no pecan "
              "contra su Dios.",
    (11, 11): "Y ahora, para que mi señor no fracase ni se quede sin hacer "
              "nada, va a caer la muerte sobre ellos: los ha alcanzado un "
              "pecado con el que provocarán la ira de su Dios, en cuanto "
              "cometan esa acción indebida.",
    (11, 12): "Porque, como se les han acabado los alimentos y toda el agua "
              "escasea, han determinado echar mano de sus ganados, y han "
              "resuelto consumir todo aquello que Dios les prohibió comer en "
              "sus leyes.",
    (11, 13): "Y hasta las primicias del trigo y los diezmos del vino y del "
              "aceite, que habían reservado consagrándolos a los sacerdotes "
              "que están en Jerusalén delante de nuestro Dios, han decidido "
              "gastarlos, cosas que a nadie del pueblo le está permitido tocar "
              "ni con las manos.",
    (11, 14): "Y han enviado a Jerusalén —porque también los que allí habitan "
              "han hecho lo mismo— gente que les traiga del consejo de "
              "ancianos la dispensa.",
    (11, 15): "Y sucederá que, en cuanto se lo comuniquen y ellos lo hagan, "
              "aquel mismo día te serán entregados para su ruina.",
    (11, 16): "Por eso yo, tu sierva, al saber todo esto, huí de ellos; y me "
              "ha enviado Dios a hacer contigo cosas de las que se pasmará "
              "toda la tierra, cuantos las oigan.",
    (11, 17): "Porque tu sierva es temerosa de Dios y sirve noche y día al "
              "Dios del cielo. Y ahora me quedaré contigo, señor mío, y tu "
              "sierva saldrá de noche al barranco, y oraré a Dios, y él me "
              "dirá cuándo hayan cometido sus pecados;",
    (11, 18): "y vendré a comunicártelo, y saldrás tú con todo tu ejército, y "
              "no habrá entre ellos quien te resista.",
    (11, 19): "Y te llevaré por medio de Judea hasta llegar frente a "
              "Jerusalén, y pondré tu trono en medio de ella; y los llevarás "
              "como ovejas que no tienen pastor, y ni un perro ladrará con su "
              "lengua delante de ti. Porque esto se me ha dicho por "
              "revelación y se me ha anunciado, y he sido enviada a "
              "comunicártelo».",
    (11, 20): "Y agradaron sus palabras a Holofernes y a todos sus servidores, "
              "y se maravillaron de su sabiduría y dijeron:",
    (11, 21): "«No hay mujer como ésta de un extremo a otro de la tierra, por "
              "la belleza de su rostro y por la sensatez de sus palabras».",
    (11, 22): "Y le dijo Holofernes: «Bien ha hecho Dios en enviarte delante "
              "de tu pueblo, para que el poder esté en nuestras manos y la "
              "perdición en los que despreciaron a mi señor.",
    (11, 23): "Y ahora, hermosa eres de figura y buena en tus palabras; "
              "porque, si haces como has dicho, tu Dios será mi Dios, y tú te "
              "sentarás en la casa del rey Nabucodonosor y serás nombrada por "
              "toda la tierra».",

    (12, 1): "Y mandó que la llevasen adonde estaba guardada su vajilla de "
             "plata, y ordenó que le sirviesen de sus propios manjares y que "
             "bebiese de su vino.",
    (12, 2): "Y dijo Judit: «No comeré de ello, para que no haya ocasión de "
             "tropiezo, sino que se me proveerá de lo que he traído conmigo».",
    (12, 3): "Y le dijo Holofernes: «Y si se acaba lo que traes contigo, ¿de "
             "dónde vamos a sacar para darte otro tanto? Porque no hay entre "
             "nosotros nadie de tu nación».",
    (12, 4): "Y le dijo Judit: «Vive tu alma, señor mío, que tu sierva no "
             "gastará lo que trae consigo antes de que el Señor haga por mi "
             "mano lo que tiene determinado».",
    (12, 5): "Y la llevaron los servidores de Holofernes a la tienda, y "
             "durmió hasta la medianoche; y se levantó a la vigilia del alba,",
    (12, 6): "y mandó decir a Holofernes: «Mande mi señor que dejen a tu "
             "sierva salir a orar».",
    (12, 7): "Y ordenó Holofernes a sus guardias que no se lo impidiesen. Y "
             "permaneció en el campamento tres días; y salía de noche al "
             "barranco de Betulia, y se lavaba en el campamento, en la fuente "
             "del agua.",
    (12, 8): "Y al subir, rogaba al Señor Dios de Israel que enderezase su "
             "camino para levantar a los hijos de su pueblo.",
    (12, 9): "Y volviendo pura, se quedaba en la tienda hasta que tomaba su "
             "alimento hacia la tarde.",
    (12, 10): "Y sucedió que al cuarto día hizo Holofernes un banquete sólo "
              "para sus servidores, y no invitó a ninguno de los encargados "
              "del servicio.",
    (12, 11): "Y dijo a Bagoas, el eunuco que estaba al frente de todo lo "
              "suyo: «Ve y convence a esa mujer hebrea que está contigo de que "
              "venga a nosotros y coma y beba con nosotros.",
    (12, 12): "Porque sería una vergüenza para nosotros dejar marchar a una "
              "mujer así sin haber gozado de ella; que si no la atraemos, se "
              "reirá de nosotros».",
    (12, 13): "Y salió Bagoas de la presencia de Holofernes, y entró a ella y "
              "le dijo: «No tenga reparo esta hermosa joven en venir a mi "
              "señor, para ser honrada en su presencia, y beber con nosotros "
              "vino con alegría, y ser hoy como una de las hijas de los hijos "
              "de Asur que están en la casa de Nabucodonosor».",
    (12, 14): "Y le dijo Judit: «¿Y quién soy yo para contradecir a mi señor? "
              "Todo lo que sea grato a sus ojos me apresuraré a hacerlo, y "
              "esto será para mí motivo de gozo hasta el día de mi muerte».",
    (12, 15): "Y levantándose, se engalanó con sus vestidos y con todo el "
              "adorno de mujer; y su criada fue delante y le tendió en el "
              "suelo, frente a Holofernes, las pieles que había recibido de "
              "Bagoas para su uso diario, para comer recostada sobre ellas.",
    (12, 16): "Y entrando Judit, se recostó; y el corazón de Holofernes se "
              "salió de sí por ella, y se le estremeció el alma; y estaba "
              "ardiendo en deseo de estar con ella, y andaba buscando ocasión "
              "de seducirla desde el día en que la vio.",
    (12, 17): "Y le dijo Holofernes: «Bebe, pues, y alégrate con nosotros».",
    (12, 18): "Y dijo Judit: «Beberé, señor, porque mi vida se ha engrandecido "
              "hoy en mí más que en todos los días de mi existencia».",
    (12, 19): "Y tomando de lo que su criada le había preparado, comió y bebió "
              "delante de él.",
    (12, 20): "Y se alegró Holofernes con ella, y bebió muchísimo vino, cuanto "
              "no había bebido jamás en un solo día desde que nació.",

    (13, 1): "Y cuando se hizo tarde, se dieron prisa sus servidores en "
             "retirarse; y Bagoas cerró la tienda por fuera, y despidió a los "
             "que estaban en presencia de su señor, y se fueron a sus lechos, "
             "porque todos estaban rendidos por lo mucho que había durado el "
             "banquete.",
    (13, 2): "Y quedó Judit sola en la tienda, y Holofernes caído sobre su "
             "lecho, porque el vino lo tenía anegado.",
    (13, 3): "Y había dicho Judit a su criada que se quedase fuera de la "
             "alcoba y aguardase su salida, como cada día, pues dijo que "
             "saldría a su oración; y a Bagoas le había hablado en estos "
             "mismos términos.",
    (13, 4): "Y se marcharon todos de su presencia, y nadie quedó en la "
             "alcoba, ni pequeño ni grande. Y Judit, puesta en pie junto a su "
             "lecho, dijo en su corazón: «Señor, Dios de todo poder, mira en "
             "esta hora la obra de mis manos, para honra de Jerusalén;",
    (13, 5): "porque ahora es el momento de socorrer tu heredad y de hacer que "
             "mi empresa sea el quebranto de los enemigos que se han levantado "
             "contra nosotros».",
    (13, 6): "Y acercándose al barrote del lecho que estaba a la cabecera de "
             "Holofernes, descolgó de allí su alfanje,",
    (13, 7): "y llegándose al lecho, lo agarró por la cabellera de la cabeza y "
             "dijo: «Dame fuerza, Dios de Israel, en este día».",
    (13, 8): "Y le dio en el cuello dos golpes con toda su fuerza, y le quitó "
             "la cabeza,",
    (13, 9): "e hizo rodar su cuerpo de la cama, y descolgó el mosquitero de "
             "las columnas; y poco después salió y entregó a su doncella la "
             "cabeza de Holofernes,",
    (13, 10): "y ella la metió en la alforja de sus provisiones. Y salieron "
              "las dos juntas, según su costumbre; y atravesando el "
              "campamento, dieron la vuelta a aquel barranco y subieron al "
              "monte de Betulia, y llegaron a sus puertas.",
    (13, 11): "Y dijo Judit desde lejos a los que guardaban las puertas: "
              "«¡Abrid, abrid la puerta! Con nosotras está Dios, nuestro Dios, "
              "para mostrar todavía su fuerza en Israel y su poder contra "
              "nuestros enemigos, como lo ha hecho hoy».",
    (13, 12): "Y sucedió que, cuando los hombres de su ciudad oyeron su voz, "
              "se dieron prisa en bajar a la puerta de su ciudad, y convocaron "
              "a los ancianos de la ciudad.",
    (13, 13): "Y acudieron corriendo todos, desde el menor hasta el mayor, "
              "porque les parecía increíble que hubiese vuelto; y abrieron la "
              "puerta y las recibieron, y encendiendo fuego para alumbrar, las "
              "rodearon.",
    (13, 14): "Y ella les dijo a gran voz: «¡Alabad a Dios, alabadlo! Alabad a "
              "Dios, que no ha apartado su misericordia de la casa de Israel, "
              "sino que ha quebrantado a nuestros enemigos por mi mano esta "
              "noche».",
    (13, 15): "Y sacando la cabeza de la alforja, se la mostró y les dijo: "
              "«Aquí tenéis la cabeza de Holofernes, general en jefe del "
              "ejército de Asur, y aquí el mosquitero bajo el cual yacía en su "
              "embriaguez. Y el Señor lo ha herido por mano de una mujer.",
    (13, 16): "Y vive el Señor, que me ha guardado en el camino por donde fui, "
              "que mi rostro lo sedujo para su perdición, y no cometió conmigo "
              "pecado que me manchara ni me avergonzara».",
    (13, 17): "Y todo el pueblo quedó atónito, y inclinándose adoraron a Dios "
              "y dijeron a una: «Bendito seas, Dios nuestro, que has reducido "
              "a nada en este día a los enemigos de tu pueblo».",
    (13, 18): "Y le dijo Ozías: «Bendita eres tú, hija, del Dios Altísimo, más "
              "que todas las mujeres de la tierra; y bendito el Señor Dios que "
              "creó los cielos y la tierra, el que te ha guiado para herir la "
              "cabeza del jefe de nuestros enemigos.",
    (13, 19): "Porque no se apartará la confianza que has inspirado del "
              "corazón de los hombres que recuerden la fuerza de Dios para "
              "siempre.",
    (13, 20): "Y que Dios te lo tenga en cuenta para gloria eterna, y te "
              "visite con bienes, porque no miraste por tu propia vida ante la "
              "humillación de nuestro linaje, sino que saliste al paso de "
              "nuestra ruina caminando derechamente delante de nuestro Dios». "
              "Y dijo todo el pueblo: «Amén, amén».",

    (14, 1): "Y les dijo Judit: «Escuchadme, hermanos: tomad esta cabeza y "
             "colgadla de las almenas de vuestra muralla.",
    (14, 2): "Y sucederá que, en cuanto despunte el alba y salga el sol sobre "
             "la tierra, tomaréis cada uno vuestras armas de guerra, y saldrá "
             "todo hombre fuerte fuera de la ciudad, y pondréis al frente de "
             "ellos un capitán, como si bajaseis a la llanura contra la "
             "avanzada de los hijos de Asur; pero no bajaréis.",
    (14, 3): "Y ellos, tomando sus armaduras, irán a su campamento y "
             "despertarán a los generales del ejército de Asur; y correrán "
             "juntos a la tienda de Holofernes y no lo hallarán; y caerá sobre "
             "ellos el pánico, y huirán delante de vosotros.",
    (14, 4): "Y persiguiéndolos vosotros y todos los que habitan todo el "
             "territorio de Israel, los iréis derribando por sus caminos.",
    (14, 5): "Pero antes de hacer esto, llamadme a Ajior el amonita, para que "
             "vea y reconozca al que despreció a la casa de Israel y lo envió "
             "a nosotros como a la muerte».",
    (14, 6): "Y llamaron a Ajior de la casa de Ozías; y cuando llegó y vio la "
             "cabeza de Holofernes en la mano de uno de los hombres, en la "
             "asamblea del pueblo, cayó de bruces y se le fue el aliento.",
    (14, 7): "Y cuando lo levantaron, se echó a los pies de Judit y se inclinó "
             "ante ella y dijo: «Bendita seas tú en toda tienda de Judá y en "
             "toda nación: los que oigan tu nombre se estremecerán.",
    (14, 8): "Y ahora cuéntame todo lo que has hecho en estos días». Y Judit "
             "le contó, en medio del pueblo, todo cuanto había hecho desde el "
             "día en que salió hasta aquel momento en que les hablaba.",
    (14, 9): "Y cuando acabó de hablar, prorrumpió el pueblo en un gran "
             "clamor, y llenó su ciudad de voces de alegría.",
    (14, 10): "Y viendo Ajior todo lo que había hecho el Dios de Israel, creyó "
              "en Dios firmemente, y se circuncidó la carne de su prepucio, y "
              "fue agregado a la casa de Israel hasta el día de hoy.",
    (14, 11): "Y cuando subió el alba, colgaron la cabeza de Holofernes de la "
              "muralla, y tomó cada hombre de Israel sus armas, y salieron por "
              "escuadrones hacia las subidas.",
    (14, 12): "Y cuando los hijos de Asur los vieron, mandaron aviso a sus "
              "jefes, y éstos fueron a los generales y a los jefes de mil y a "
              "todos sus capitanes.",
    (14, 13): "Y llegaron a la tienda de Holofernes, y dijeron al que estaba "
              "al frente de todo lo suyo: «Despierta a nuestro señor, porque "
              "esos esclavos se han atrevido a bajar contra nosotros a la "
              "guerra, para acabar de ser exterminados».",
    (14, 14): "Y entró Bagoas y golpeó la cortina de la tienda, porque "
              "suponía que estaba durmiendo con Judit.",
    (14, 15): "Y como nadie le respondió, descorrió la cortina y entró en la "
              "alcoba, y lo halló tirado muerto sobre el escabel, y su cabeza "
              "le había sido quitada.",
    (14, 16): "Y gritó a gran voz con llanto y gemido y clamor fuerte, y "
              "rasgó sus vestidos.",
    (14, 17): "Y entró en la tienda donde Judit se alojaba, y no la halló; y "
              "salió de un salto hacia la tropa gritando:",
    (14, 18): "«¡Los esclavos nos han traicionado! ¡Una sola mujer de los "
              "hebreos ha cubierto de vergüenza la casa del rey "
              "Nabucodonosor! Mirad: Holofernes por el suelo, y su cabeza no "
              "está sobre él».",
    (14, 19): "Y cuando los príncipes del ejército de Asur oyeron estas "
              "palabras, rasgaron sus túnicas, y se turbó su ánimo "
              "sobremanera, y se levantó entre ellos un griterío y un clamor "
              "grandísimo en medio del campamento.",

    (15, 1): "Y cuando los que estaban en las tiendas lo oyeron, quedaron "
             "atónitos por lo sucedido,",
    (15, 2): "y cayó sobre ellos temblor y espanto, y ya no hubo hombre que se "
             "quedase al lado de su compañero, sino que, desbandándose todos a "
             "una, huían por todos los caminos de la llanura y de la montaña.",
    (15, 3): "Y también los que acampaban en la montaña alrededor de Betulia "
             "se dieron a la fuga. Y entonces los hijos de Israel, todo hombre "
             "de guerra de entre ellos, se lanzaron sobre ellos.",
    (15, 4): "Y envió Ozías a Betomastáim y a Cobá y a Colá y a todo el "
             "territorio de Israel mensajeros que anunciasen lo ocurrido, para "
             "que todos se lanzasen sobre los enemigos y acabasen con ellos.",
    (15, 5): "Y cuando los hijos de Israel lo oyeron, cayeron todos a una "
             "sobre ellos y los fueron destrozando hasta Cobá. Y del mismo "
             "modo acudieron los de Jerusalén y los de toda la montaña, porque "
             "les habían anunciado lo sucedido en el campamento de sus "
             "enemigos; y los de Galaad y los de Galilea los envolvieron por "
             "los flancos con gran matanza, hasta que pasaron Damasco y sus "
             "términos.",
    (15, 6): "Y los demás, los que habitaban Betulia, cayeron sobre el "
             "campamento de Asur y lo saquearon, y se enriquecieron "
             "sobremanera.",
    (15, 7): "Y los hijos de Israel, volviendo de la matanza, se apoderaron de "
             "lo que quedaba; y las aldeas y las granjas de la montaña y del "
             "llano cogieron muchos despojos, porque eran una cantidad "
             "grandísima.",
    (15, 8): "Y Joacim el sumo sacerdote y el consejo de ancianos de los hijos "
             "de Israel que habitaban en Jerusalén vinieron a ver los bienes "
             "que el Señor había hecho a Israel, y a ver a Judit y saludarla.",
    (15, 9): "Y cuando entraron a ella, la bendijeron todos a una y le "
             "dijeron: «Tú eres la honra de Jerusalén, tú el gran orgullo de "
             "Israel, tú la gran gloria de nuestro linaje.",
    (15, 10): "Todo esto lo has hecho con tu mano, has hecho el bien a Israel, "
              "y Dios se ha complacido en ello. Bendita seas del Señor "
              "Todopoderoso por los siglos». Y dijo todo el pueblo: «Amén».",
    (15, 11): "Y todo el pueblo saqueó el campamento durante treinta días; y "
              "dieron a Judit la tienda de Holofernes y toda su vajilla de "
              "plata y los lechos y las vasijas y todos sus enseres; y ella lo "
              "tomó y lo cargó sobre su mula, y unció sus carros y lo amontonó "
              "encima.",
    (15, 12): "Y acudieron corriendo todas las mujeres de Israel a verla, y la "
              "bendijeron, y organizaron en su honor una danza; y ella tomó "
              "ramos en las manos y los dio a las mujeres que estaban con "
              "ella,",
    (15, 13): "y se coronaron de olivo, ella y las que iban con ella; y salió "
              "delante de todo el pueblo, guiando la danza de todas las "
              "mujeres, y la seguía todo hombre de Israel, armados y con "
              "coronas y con himnos en la boca.",
    (15, 14): "Y entonó Judit este cántico de acción de gracias ante todo "
              "Israel, y todo el pueblo respondía a voz en grito a esta "
              "alabanza.",

    (16, 1): "Y dijo Judit: «Entonad a mi Dios con panderos, cantad al Señor "
             "con címbalos, componedle salmo y alabanza, exaltad e invocad su "
             "nombre.",
    (16, 2): "Porque el Señor es un Dios que quebranta las guerras: porque en "
             "sus campamentos, en medio del pueblo, me libró de la mano de los "
             "que me perseguían.",
    (16, 3): "Vino Asur de los montes, del norte; vino con las miríadas de su "
             "ejército, cuya multitud cegó los torrentes y cuya caballería "
             "cubrió las colinas.",
    (16, 4): "Dijo que quemaría mis montes y que mataría a espada a mis "
             "jóvenes, y que arrojaría por tierra a mis niños de pecho, y que "
             "entregaría al saqueo a mis pequeños, y que se llevaría como "
             "botín a mis vírgenes.",
    (16, 5): "El Señor Todopoderoso los frustró por mano de una mujer.",
    (16, 6): "Porque su valiente no cayó a manos de jóvenes, ni lo hirieron "
             "hijos de Titanes, ni gigantes de alta talla se echaron sobre "
             "él, sino que Judit, hija de Merarí, lo desarmó con la belleza de "
             "su rostro.",
    (16, 7): "Porque se despojó del vestido de su viudez para levantar a los "
             "afligidos de Israel; ungió su rostro con perfume,",
    (16, 8): "y se ató los cabellos con una diadema, y tomó un vestido de "
             "lino para engañarlo.",
    (16, 9): "Su sandalia le arrebató el ojo, y su hermosura le cautivó el "
             "alma; el alfanje le atravesó el cuello.",
    (16, 10): "Se estremecieron los persas ante su audacia, y los medos "
              "quedaron desconcertados ante su arrojo.",
    (16, 11): "Entonces prorrumpieron en gritos mis humildes, y mis débiles "
              "—que estaban temerosos y espantados— levantaron su voz, y "
              "aquéllos fueron puestos en fuga.",
    (16, 12): "Hijos de muchachas los acribillaron, y los herían como a "
              "chiquillos de desertores; perecieron en la batalla de mi Señor.",
    (16, 13): "Cantaré a mi Dios un cántico nuevo: Señor, grande eres y "
              "glorioso, admirable en fortaleza, insuperable.",
    (16, 14): "Sírvate toda tu creación, porque tú dijiste y fueron hechas; "
              "enviaste tu espíritu y las edificó, y no hay quien resista a tu "
              "voz.",
    (16, 15): "Porque los montes serán sacudidos desde sus cimientos junto con "
              "las aguas, y las peñas se derretirán delante de ti como cera; "
              "pero con los que te temen tú eres propicio.",
    (16, 16): "Porque poca cosa es todo sacrificio en olor de suavidad, y muy "
              "poco todo […] para holocausto tuyo; pero el que teme al […] es "
              "grande para siempre.",
    (16, 17): "¡Ay de las naciones […] contra mi linaje! El Señor Todopoderoso "
              "les dará su merecido en el día del juicio: enviará fuego y "
              "gusanos a sus carnes, y llorarán de dolor eternamente».",
    (16, 18): "Y cuando llegaron a Jerusalén, adoraron a Dios; y una vez que "
              "el pueblo se purificó, ofrecieron sus holocaustos y sus "
              "ofrendas voluntarias y sus dones.",
    (16, 19): "Y Judit consagró todos los objetos de Holofernes que el pueblo "
              "le había dado, y el mosquitero que ella misma había tomado de "
              "su alcoba lo entregó como ofrenda votiva a Dios.",
    (16, 20): "Y el pueblo estuvo de fiesta en Jerusalén, delante del "
              "santuario, por tres meses, y Judit se quedó con ellos.",
    (16, 21): "Y pasados aquellos días, volvió cada uno a su heredad, y Judit "
              "se fue a Betulia y se quedó al frente de su hacienda; y fue en "
              "su tiempo famosa en toda la tierra.",
    (16, 22): "Y muchos la desearon, y ningún hombre la conoció en todos los "
              "días de su vida, desde el día en que murió Manasés su marido y "
              "fue reunido con su pueblo.",
    (16, 23): "Y llegó a muy avanzada edad, y envejeció en la casa de su "
              "marido hasta los ciento cinco años; y dejó libre a su doncella. "
              "Y murió en Betulia, y la sepultaron en la gruta de Manasés su "
              "marido.",
    (16, 24): "Y la casa de Israel la lloró siete días. Y antes de morir "
              "repartió sus bienes entre todos los parientes más próximos de "
              "Manasés su marido y los parientes más próximos de su propio "
              "linaje.",
    (16, 25): "Y no hubo ya quien atemorizase a los hijos de Israel en los "
              "días de Judit, ni muchos días después de su muerte. Amén.",
}
