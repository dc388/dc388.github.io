"""2 Macabeos en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio.

No es la segunda parte de 1 Macabeos. Es otro libro, de otro autor, escrito
directamente en griego y con otro propósito. El propio autor lo dice en 2:23:
es el resumen en un solo volumen de una obra de cinco tomos de un tal Jasón de
Cirene, que se perdió. Cubre menos años que 1 Macabeos —de Seleuco IV a la
derrota de Nicanor— y se solapa con sus siete primeros capítulos, pero cuenta
los mismos hechos de otra manera: con discursos, milagros, jinetes celestiales
y una retórica que 1 Macabeos no tiene. Donde aquél es una crónica seca, éste
predica.

Y predica cosas que importan. Aquí aparece, por primera vez con esta claridad
en toda la Biblia griega, la resurrección del cuerpo: los siete hermanos del
capítulo 7 mueren uno tras otro diciéndolo a la cara del rey (7:9, 7:11, 7:14,
7:23, 7:29). Hebreos 11:35 —«otros fueron atormentados, no aceptando el
rescate, a fin de obtener mejor resurrección»— está señalando a este capítulo;
no hay otro pasaje al que pueda referirse. Y en 7:28 la madre le dice al hijo
menor que Dios hizo el cielo y la tierra «de lo que no existía», que es la
formulación más antigua que se conserva de la creación de la nada.

Hay que decir también lo otro, sin rodeos, porque es la razón de que este libro
no esté en la Biblia protestante: en 12:43-45 Judas manda dinero a Jerusalén
para que se ofrezca sacrificio por los soldados muertos, y el texto alaba el
gesto. De ahí sale la doctrina católica del purgatorio, y en ese pasaje se
apoyó Roma en Trento. Lutero lo señaló, y por eso el libro quedó fuera. La
traducción no lo suaviza ni lo esconde: dice lo que dice el griego, y el lector
decide. Lo mismo con 15:12-16, donde Onías y Jeremías, ya muertos, oran por el
pueblo.

A diferencia de 1 Macabeos, este autor nombra a Dios sin reparos: «el Señor»,
«el Todopoderoso», «el que todo lo ve». Se ha traducido tal cual.

El libro arranca con dos cartas de los judíos de Jerusalén a los de Egipto
(1:1-9 y 1:10—2:18) que alguien antepuso al resumen; no son de Jasón ni del
epitomista. Y termina con el autor pidiendo disculpas por su estilo (15:37-39),
que es de las páginas más humanas de toda la Septuaginta.

Defectos de esta edición griega que no se han corregido:

- En 1:36 el nombre se repite igual las dos veces (Νεφθάρ ... Νεφθάρ), donde el
  texto corriente trae Νεφθαΐ la segunda. Se traduce como está.
- En el capítulo 7 la numeración se descuadra: el versículo 36 va metido dentro
  del 35 con un ³⁶ volado, y lo que sigue, rotulado 36, es en realidad el 37.
  De ahí que el capítulo salte del 36 al 38 y no tenga 37. No se ha tocado; la
  traducción va donde la pone el griego, con el mismo ³⁶, para que las dos
  columnas cuadren.
- Lo mismo en 11:29: el versículo 30 va dentro del 29 con un ³⁰ volado, y el
  capítulo pasa del 29 al 31. Se traduce donde está.
"""

from __future__ import annotations

MACABEOS2_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "A los hermanos judíos que están en Egipto, salud: los hermanos "
            "judíos que están en Jerusalén y los que están en la región de "
            "Judea les desean paz cumplida.",
    (1, 2): "Y que Dios os haga bien, y se acuerde de su alianza con Abrahán y "
            "con Isaac y con Jacob, sus siervos fieles.",
    (1, 3): "Y os dé a todos corazón para adorarle y hacer su voluntad con "
            "ánimo grande y con alma dispuesta;",
    (1, 4): "y os abra el corazón a su ley y a sus mandamientos, y haga paz;",
    (1, 5): "y escuche vuestras súplicas, y se reconcilie con vosotros, y no os "
            "abandone en tiempo malo.",
    (1, 6): "Y ahora, aquí estamos orando por vosotros.",
    (1, 7): "Bajo el reinado de Demetrio, el año ciento sesenta y nueve, "
            "nosotros los judíos os escribimos en la tribulación y en el "
            "trance que nos sobrevino en estos años, desde que Jasón y los "
            "suyos se apartaron de la tierra santa y del reino;",
    (1, 8): "e incendiaron el pórtico y derramaron sangre inocente. Y rogamos "
            "al Señor y fuimos oídos; ofrecimos sacrificio y flor de harina, y "
            "encendimos las lámparas, y pusimos los panes.",
    (1, 9): "Y ahora, celebrad los días de las tiendas del mes de Quisleu.",
    (1, 10): "Año ciento ochenta y ocho, en Jerusalén. Los de Judea y el "
             "consejo de ancianos y Judas, a Aristóbulo, maestro del rey "
             "Tolomeo, y de la familia de los sacerdotes ungidos, y a los "
             "judíos de Egipto: salud y salud cumplida.",
    (1, 11): "Salvados por Dios de grandes peligros, le damos grandes gracias, "
             "como quien se ha puesto en pie de guerra contra un rey.",
    (1, 12): "Porque él mismo arrojó a Persia a los que se habían puesto en "
             "batalla contra la ciudad santa.",
    (1, 13): "Pues, llegado el caudillo, y con él el ejército que parecía "
             "irresistible, fueron acuchillados en el templo de Nanea, por una "
             "estratagema de que se valieron los sacerdotes de Nanea.",
    (1, 14): "Porque, con el pretexto de desposarse con ella, se presentó "
             "Antíoco en aquel lugar con los amigos que lo acompañaban, para "
             "llevarse mucho dinero a título de dote;",
    (1, 15): "y habiéndolo presentado los sacerdotes del templo de Nanea, y "
             "habiendo entrado él con unos pocos en el recinto del santuario, "
             "cerraron el templo en cuanto entró Antíoco;",
    (1, 16): "y abriendo la trampilla oculta del artesonado, lo fulminaron a "
             "pedradas al caudillo, y lo descuartizaron, y arrojaron las "
             "cabezas a los que estaban fuera.",
    (1, 17): "Por todo sea bendito nuestro Dios, que entregó a los impíos.",
    (1, 18): "Puesto que vamos a celebrar el veinticinco de Quisleu la "
             "purificación del templo, hemos creído deber informaros, para que "
             "también vosotros celebréis los días de las tiendas y del fuego, "
             "el fuego de cuando Nehemías, el que edificó entonces el templo y "
             "el altar, ofreció sacrificios.",
    (1, 19): "Porque, cuando nuestros padres fueron llevados a Persia, los "
             "sacerdotes piadosos tomaron a escondidas del fuego del altar y "
             "lo escondieron en la cavidad de un pozo seco, y allí lo pusieron "
             "a salvo, de modo que el lugar quedó desconocido para todos.",
    (1, 20): "Y pasados bastantes años, cuando plugo a Dios, Nehemías, enviado "
             "por el rey de Persia, mandó en busca del fuego a los "
             "descendientes de los sacerdotes que lo habían escondido.",
    (1, 21): "Y como nos informaran que no habían hallado fuego, sino un agua "
             "espesa, les mandó que sacaran de ella y la trajesen. Y cuando "
             "estuvo dispuesto lo del sacrificio, mandó Nehemías a los "
             "sacerdotes rociar con aquella agua la leña y lo que estaba "
             "encima.",
    (1, 22): "Y cuando esto se hizo y pasó un rato, y brilló el sol que estaba "
             "cubierto de nubes, se encendió una gran hoguera, de modo que "
             "todos se maravillaron.",
    (1, 23): "Y mientras se consumía el sacrificio, hicieron oración los "
             "sacerdotes, los sacerdotes y todos, comenzando Jonatán y "
             "respondiendo los demás, como Nehemías.",
    (1, 24): "Y la oración era de esta manera: «Señor, Dios, creador de todas "
             "las cosas, terrible y fuerte y justo y misericordioso, único rey "
             "y bueno,",
    (1, 25): "único dispensador, único justo y todopoderoso y eterno, el que "
             "libra a Israel de todo mal, el que hizo escogidos a los padres y "
             "los santificó:",
    (1, 26): "recibe el sacrificio por todo tu pueblo Israel, y guarda tu parte "
             "y conságrala.",
    (1, 27): "Reúne nuestra dispersión, libera a los que son esclavos entre las "
             "naciones, mira a los despreciados y aborrecidos, y sepan las "
             "naciones que tú eres nuestro Dios.",
    (1, 28): "Atormenta a los que nos oprimen y nos ultrajan con soberbia.",
    (1, 29): "Planta a tu pueblo en tu lugar santo, como dijo Moisés.»",
    (1, 30): "Y los sacerdotes entonaban los himnos.",
    (1, 31): "Y cuando se consumió lo del sacrificio, mandó Nehemías derramar "
             "el agua que sobraba sobre unas piedras grandes.",
    (1, 32): "Y hecho esto, se encendió una llama; pero se consumió con la luz "
             "que resplandeció desde el altar.",
    (1, 33): "Y cuando el hecho se hizo público, y se anunció al rey de los "
             "persas que en el lugar donde los sacerdotes deportados habían "
             "escondido el fuego había aparecido el agua con que los de "
             "Nehemías purificaron los sacrificios,",
    (1, 34): "el rey, después de comprobar el hecho, lo cercó y lo declaró "
             "sagrado;",
    (1, 35): "y de los que el rey recibía muchos y variados regalos, él "
             "repartía.",
    (1, 36): "Y los de Nehemías llamaron a esto Neftar, que se interpreta "
             "«purificación»; pero la mayoría lo llama Neftar.",

    # Capítulo 2
    (2, 1): "Se halla en los registros que Jeremías el profeta mandó a los "
            "deportados tomar del fuego, como queda dicho;",
    (2, 2): "y cómo el profeta encargó a los deportados, dándoles la ley, que "
            "no se olvidaran de los mandamientos del Señor, y que no se "
            "extraviaran en sus pensamientos al ver estatuas de oro y de plata "
            "y el adorno que las rodea.",
    (2, 3): "Y diciendo otras cosas semejantes, los exhortaba a que la ley no "
            "se apartara de su corazón.",
    (2, 4): "Estaba también en el escrito cómo el profeta, habiendo recibido un "
            "oráculo, mandó que la tienda y el arca lo siguieran, y cómo salió "
            "al monte al que subió Moisés y contempló la heredad de Dios.",
    (2, 5): "Y llegando Jeremías encontró una cueva a modo de casa, y metió "
            "allí la tienda y el arca y el altar del incienso, y tapió la "
            "entrada.",
    (2, 6): "Y algunos de los que lo acompañaban se acercaron para señalar el "
            "camino, y no pudieron dar con él.",
    (2, 7): "Y cuando Jeremías lo supo, los reprendió y dijo: «El lugar quedará "
            "desconocido hasta que Dios reúna la congregación de su pueblo y "
            "se muestre misericordioso.",
    (2, 8): "Y entonces el Señor mostrará estas cosas, y se verá la gloria del "
            "Señor y la nube, como se manifestaba en tiempos de Moisés, y como "
            "lo pidió Salomón, para que el lugar fuese consagrado "
            "grandemente.»",
    (2, 9): "Se declaraba también cómo, teniendo sabiduría, ofreció el "
            "sacrificio de la dedicación y del acabamiento del templo.",
    (2, 10): "Así como Moisés oró al Señor, y descendió fuego del cielo y "
             "consumió lo del sacrificio, así también Salomón oró al Señor, y "
             "el fuego, al descender, consumió los holocaustos.",
    (2, 11): "Y dijo Moisés: «Por no haberse comido lo del pecado, fue "
             "consumido.»",
    (2, 12): "Igualmente también Salomón celebró los ocho días.",
    (2, 13): "Se contaban también estas mismas cosas en los registros y en las "
             "memorias del tiempo de Nehemías, y cómo, al fundar una "
             "biblioteca, reunió los libros de los reyes y de los profetas, y "
             "los de David, y cartas de reyes acerca de las ofrendas.",
    (2, 14): "De igual modo también Judas reunió todos los libros que se habían "
             "perdido por la guerra que hemos tenido, y están en nuestro "
             "poder.",
    (2, 15): "Si, pues, tenéis necesidad de ellos, enviad quienes os los "
             "lleven.",
    (2, 16): "Estando, pues, a punto de celebrar la purificación, os hemos "
             "escrito; haréis bien, pues, en celebrar estos días.",
    (2, 17): "Y Dios, el que salvó a todo su pueblo y devolvió a todos la "
             "heredad y el reino y el sacerdocio y la santificación,",
    (2, 18): "como lo prometió por medio de la ley —pues esperamos en Dios que "
             "pronto tendrá misericordia de nosotros y nos reunirá de debajo "
             "del cielo en el lugar santo, porque nos libró de grandes males y "
             "purificó el lugar.",
    (2, 19): "Lo tocante a Judas Macabeo y a sus hermanos, y la purificación "
             "del templo grandísimo, y la dedicación del altar,",
    (2, 20): "y además las guerras contra Antíoco Epífanes y contra su hijo "
             "Eupátor,",
    (2, 21): "y las manifestaciones venidas del cielo a los que con celo "
             "pelearon varonilmente por el judaísmo, de modo que, siendo "
             "pocos, saquearon todo el país y persiguieron a las multitudes "
             "bárbaras,",
    (2, 22): "y recobraron el templo famoso en toda la tierra, y liberaron la "
             "ciudad, y restablecieron las leyes que estaban a punto de ser "
             "abolidas, habiéndoseles mostrado el Señor propicio con toda "
             "benignidad:",
    (2, 23): "todo esto, expuesto por Jasón de Cirene en cinco libros, "
             "intentaremos compendiarlo en un solo volumen.",
    (2, 24): "Porque, viendo la marea de números y la dificultad que hay para "
             "los que quieren meterse en los relatos de la historia por la "
             "abundancia de la materia,",
    (2, 25): "hemos procurado dar a los que quieren leer un deleite; a los "
             "estudiosos, facilidad para retenerlo de memoria; y a todos los "
             "que lo tomen en las manos, provecho.",
    (2, 26): "Y para nosotros, que nos hemos echado encima el trabajo de este "
             "compendio, no es cosa fácil, sino asunto de sudor y de desvelo;",
    (2, 27): "como no le es cómodo al que prepara un banquete y busca el "
             "provecho de otros. Aun así, por la gratitud de los muchos, "
             "soportaremos de buen grado la fatiga,",
    (2, 28): "dejando al historiador la exactitud en cada punto, y esforzándonos "
             "nosotros por seguir los trazos del compendio.",
    (2, 29): "Porque, así como al arquitecto de una casa nueva le toca "
             "preocuparse de toda la estructura, y al que se encarga de "
             "decorarla y pintarla le toca examinar lo apropiado para el "
             "adorno, así me parece que es también con nosotros.",
    (2, 30): "Penetrar en la materia y hacer recorridos con el discurso y "
             "detenerse en los pormenores, corresponde al que emprende la "
             "historia;",
    (2, 31): "pero buscar la brevedad en la expresión y renunciar al desarrollo "
             "del asunto, hay que concedérselo al que hace el resumen.",
    (2, 32): "Comencemos, pues, desde aquí el relato, sin añadir a lo dicho más "
             "que esto: porque es necedad alargarse en lo que va antes de la "
             "historia y luego abreviar la historia.",

    # Capítulo 3
    (3, 1): "Habitándose la ciudad santa en toda paz, y guardándose las leyes "
            "de la mejor manera, por la piedad del sumo sacerdote Onías y su "
            "aborrecimiento del mal,",
    (3, 2): "sucedía que hasta los mismos reyes honraban aquel lugar y "
            "glorificaban el templo con los mejores presentes,",
    (3, 3): "de modo que hasta Seleuco, el rey de Asia, costeaba de sus propias "
            "rentas todos los gastos que corresponden al servicio de los "
            "sacrificios.",
    (3, 4): "Pero un tal Simón, de la tribu de Benjamín, nombrado administrador "
            "del templo, tuvo un altercado con el sumo sacerdote acerca de la "
            "inspección del mercado de la ciudad.",
    (3, 5): "Y no pudiendo vencer a Onías, se fue a Apolonio hijo de Traseo, "
            "que por aquel tiempo era gobernador de Celesiria y Fenicia,",
    (3, 6): "y le denunció que el tesoro de Jerusalén estaba lleno de riquezas "
            "incalculables, de modo que la cantidad de dinero era innumerable, "
            "y que no correspondía a la cuenta de los sacrificios, y que era "
            "posible que todo aquello cayera bajo la autoridad del rey.",
    (3, 7): "Y Apolonio, en una entrevista con el rey, le informó del dinero "
            "que se le había denunciado. Y él designó a Heliodoro, el "
            "encargado de los negocios, y lo envió con órdenes de llevar a "
            "cabo la recaudación del dinero dicho.",
    (3, 8): "Y al punto emprendió Heliodoro el viaje, en apariencia para "
            "inspeccionar las ciudades de Celesiria y Fenicia, pero en "
            "realidad para cumplir el propósito del rey.",
    (3, 9): "Y llegado a Jerusalén, y recibido con benevolencia por el sumo "
            "sacerdote de la ciudad, le expuso la denuncia recibida y le "
            "declaró a qué había venido; y preguntaba si en verdad las cosas "
            "eran así.",
    (3, 10): "Y el sumo sacerdote le mostró que aquello eran depósitos de "
             "viudas y de huérfanos,",
    (3, 11): "y una parte de Hircano hijo de Tobías, hombre de posición muy "
             "elevada —y no como calumniaba el impío Simón—, y que el total "
             "eran cuatrocientos talentos de plata y doscientos de oro;",
    (3, 12): "y que era del todo imposible hacer agravio a los que se habían "
             "fiado de la santidad del lugar y de la majestad e inviolabilidad "
             "del templo venerado en todo el mundo.",
    (3, 13): "Pero el otro, por las órdenes reales que tenía, decía que aquello "
             "había de pasar de todos modos al tesoro del rey.",
    (3, 14): "Y fijado el día, entró a disponer la inspección de aquello; y no "
             "era pequeña la angustia por toda la ciudad.",
    (3, 15): "Y los sacerdotes, arrojándose delante del altar con sus vestiduras "
             "sacerdotales, invocaban al cielo, al que dio la ley sobre los "
             "depósitos, para que guardase intacto aquello a los que lo habían "
             "depositado.",
    (3, 16): "Y al ver el semblante del sumo sacerdote se le hería a uno el "
             "alma, porque su rostro y su color demudado manifestaban la "
             "angustia de su alma;",
    (3, 17): "pues se había derramado sobre aquel hombre un temor y un "
             "estremecimiento del cuerpo, por los cuales se hacía evidente a "
             "los que lo miraban el dolor que tenía en el corazón.",
    (3, 18): "Y los de las casas salían en tropel a una súplica general, porque "
             "el lugar estaba a punto de caer en desprecio.",
    (3, 19): "Y las mujeres, ceñidas de saco bajo los pechos, llenaban las "
             "calles; y de las doncellas recluidas, unas corrían a los "
             "pórticos, otras a las murallas, y algunas se asomaban por las "
             "ventanas.",
    (3, 20): "Y todas, tendiendo las manos al cielo, hacían su plegaria.",
    (3, 21): "Y daba lástima la postración confusa de la multitud y la "
             "expectación del sumo sacerdote en su gran angustia.",
    (3, 22): "Ellos, pues, invocaban al Señor todopoderoso que guardase intacto "
             "con toda seguridad lo confiado a los que lo habían recibido en "
             "depósito.",
    (3, 23): "Y Heliodoro llevaba a cabo lo resuelto.",
    (3, 24): "Y estando ya allí mismo con sus guardias junto al tesoro, el "
             "Soberano de los espíritus y de toda potestad hizo una gran "
             "manifestación, de modo que todos los que se habían atrevido a "
             "entrar, aterrados por el poder de Dios, cayeron en desfallecimiento "
             "y en pavor.",
    (3, 25): "Porque se les apareció un caballo con un jinete terrible, "
             "adornado con hermosísimos jaeces; y lanzándose con ímpetu, "
             "sacudió a Heliodoro con los cascos delanteros. Y el que lo "
             "montaba parecía llevar armadura de oro.",
    (3, 26): "Y se le aparecieron también otros dos jóvenes, notables por su "
             "vigor, hermosísimos de palabra, espléndidos de vestidura; los "
             "cuales, poniéndose uno a cada lado, lo azotaban sin parar, "
             "descargando sobre él muchos golpes.",
    (3, 27): "Y como cayera de repente a tierra y lo envolviera una gran "
             "oscuridad, lo levantaron y lo pusieron en una camilla;",
    (3, 28): "y al que poco antes había entrado en el tesoro dicho con gran "
             "séquito y con toda su guardia, lo llevaban ahora sin que nada "
             "pudiera valerle, reconociendo abiertamente la soberanía de Dios.",
    (3, 29): "Y él, por obra divina, yacía mudo y privado de toda esperanza y "
             "de salvación;",
    (3, 30): "y ellos bendecían al Señor, que glorificaba maravillosamente su "
             "propio lugar; y el templo, que poco antes estaba lleno de temor y "
             "de turbación, al manifestarse el Señor todopoderoso quedó lleno "
             "de gozo y de alegría.",
    (3, 31): "Y pronto algunos de los allegados de Heliodoro rogaron a Onías "
             "que invocara al Altísimo y concediera la vida al que yacía "
             "dando ya el último aliento.",
    (3, 32): "Y el sumo sacerdote, sospechando que el rey pudiera concebir la "
             "idea de que los judíos habían cometido algún crimen contra "
             "Heliodoro, ofreció un sacrificio por la salud de aquel hombre.",
    (3, 33): "Y mientras el sumo sacerdote hacía la expiación, los mismos "
             "jóvenes se aparecieron otra vez a Heliodoro, vestidos con las "
             "mismas ropas, y puestos en pie dijeron: «Da muchas gracias al "
             "sumo sacerdote Onías, porque por él te ha concedido el Señor la "
             "vida.",
    (3, 34): "Y tú, azotado desde el cielo, anuncia a todos la grandeza del "
             "poder de Dios.» Y dicho esto, desaparecieron.",
    (3, 35): "Y Heliodoro, ofreciendo sacrificio a Dios y haciendo grandísimos "
             "votos al que le había conservado la vida, y despidiéndose de "
             "Onías, volvió con su ejército al rey;",
    (3, 36): "y daba testimonio ante todos de las obras del Dios altísimo que "
             "había visto con sus propios ojos.",
    (3, 37): "Y preguntando el rey a Heliodoro quién sería el hombre adecuado "
             "para ser enviado otra vez a Jerusalén, respondió:",
    (3, 38): "«Si tienes algún enemigo o conspirador contra el Estado, mándalo "
             "allá, y lo recibirás azotado, si es que escapa con vida; porque "
             "en torno a aquel lugar hay verdaderamente algún poder de Dios.",
    (3, 39): "Porque el que tiene su morada en el cielo vigila aquel lugar y lo "
             "socorre, y a los que llegan para hacerle daño los hiere y los "
             "destruye.»",
    (3, 40): "Y lo tocante a Heliodoro y a la custodia del tesoro pasó así.",

    # Capítulo 4
    (4, 1): "Y el ya mencionado Simón, el que había sido delator del dinero y "
            "de la patria, hablaba mal de Onías, como si hubiera sido él quien "
            "azuzó a Heliodoro y el causante de aquellos males;",
    (4, 2): "y se atrevía a llamar conspirador contra el Estado al bienhechor "
            "de la ciudad, al protector de sus compatriotas y al celoso de las "
            "leyes.",
    (4, 3): "Y llegando la enemistad a tal punto que hasta se cometían "
            "asesinatos por uno de los hombres de confianza de Simón,",
    (4, 4): "viendo Onías lo grave de la contienda, y que Apolonio hijo de "
            "Menesteo, gobernador de Celesiria y Fenicia, agravaba la malicia "
            "de Simón,",
    (4, 5): "se dirigió al rey, no como acusador de sus conciudadanos, sino "
            "mirando el bien común y particular de todo el pueblo;",
    (4, 6): "porque veía que sin la intervención del rey era imposible alcanzar "
            "la paz en los asuntos, y que Simón no iba a cesar en su locura.",
    (4, 7): "Pero habiendo muerto Seleuco, y tomando el reino Antíoco, el "
            "llamado Epífanes, Jasón, el hermano de Onías, usurpó con malas "
            "artes el sumo sacerdocio,",
    (4, 8): "prometiendo al rey, en una entrevista, trescientos sesenta "
            "talentos de plata, y de otra renta ochenta talentos.",
    (4, 9): "Y además de esto se comprometía a pagar otros ciento cincuenta, si "
            "se le autorizaba a fundar por su propia cuenta un gimnasio y una "
            "efebía, y a inscribir como antioquenos a los de Jerusalén.",
    (4, 10): "Y accediendo el rey, y habiéndose apoderado del cargo, en seguida "
             "pasó a sus compatriotas al modo de vivir griego.",
    (4, 11): "Y anulando los privilegios reales concedidos a los judíos por "
             "medio de Juan, el padre de Eupólemo, el que fue de embajador "
             "para la amistad y alianza con los romanos, y derogando las "
             "instituciones legítimas, introdujo costumbres contrarias a la "
             "ley.",
    (4, 12): "Porque de buena gana estableció un gimnasio al pie mismo de la "
             "ciudadela, y sometiendo a los mejores de los jóvenes los puso "
             "bajo el sombrero griego.",
    (4, 13): "Y hubo tal auge del helenismo y tal avance de la extranjerización, "
             "por la desmedida impureza de Jasón, impío y no sumo sacerdote,",
    (4, 14): "que ya los sacerdotes no ponían empeño en los servicios del "
             "altar, sino que, despreciando el templo y descuidando los "
             "sacrificios, corrían a participar en la palestra en aquel "
             "espectáculo contrario a la ley, en cuanto sonaba la llamada del "
             "disco;",
    (4, 15): "y teniendo en nada los honores patrios, tenían por hermosísimas "
             "las glorias griegas.",
    (4, 16): "Por lo cual les alcanzó una dura situación, y a aquellos mismos "
             "cuyas costumbres envidiaban y a quienes en todo querían "
             "parecerse, los tuvieron por enemigos y verdugos.",
    (4, 17): "Porque no es cosa leve cometer impiedad contra las leyes divinas; "
             "pero esto lo mostrará el tiempo que sigue.",
    (4, 18): "Y celebrándose en Tiro los juegos quinquenales, estando presente "
             "el rey,",
    (4, 19): "envió el abominable Jasón delegados, como antioquenos de "
             "Jerusalén, llevando trescientas dracmas de plata para el "
             "sacrificio de Heracles; y los mismos que las llevaban pidieron "
             "que no se emplearan en el sacrificio,",
    (4, 20): "sino que, dadas las circunstancias, se destinaran a la "
             "construcción de trirremes.",
    (4, 21): "Y enviado a Egipto Apolonio hijo de Menesteo con motivo de la "
             "entronización del rey Filométor, Antíoco, al enterarse de que "
             "aquél se había hecho ajeno a sus intereses, se preocupó de su "
             "propia seguridad; por lo cual, llegando a Jope, pasó a "
             "Jerusalén.",
    (4, 22): "Y recibido con magnificencia por Jasón y por la ciudad, entró con "
             "antorchas y aclamaciones; y luego marchó con su ejército a "
             "Fenicia.",
    (4, 23): "Y al cabo de tres años envió Jasón a Menelao, el hermano del ya "
             "mencionado Simón, para llevar el dinero al rey y para gestionar "
             "las memorias sobre asuntos urgentes.",
    (4, 24): "Pero él, presentado al rey y habiéndolo halagado con apariencia "
             "de autoridad, desvió hacia sí el sumo sacerdocio, pujando "
             "trescientos talentos de plata por encima de Jasón.",
    (4, 25): "Y recibiendo las órdenes reales, se presentó sin traer nada digno "
             "del sumo sacerdocio, sino teniendo furias de tirano cruel e iras "
             "de fiera bárbara.",
    (4, 26): "Y Jasón, el que había suplantado con engaño a su propio hermano, "
             "suplantado a su vez por otro, fue expulsado y huyó al país de "
             "los amonitas.",
    (4, 27): "Y Menelao se hizo con el cargo, pero del dinero prometido al rey "
             "no pagaba nada con regularidad;",
    (4, 28): "y al hacer la reclamación Sóstrato, el comandante de la "
             "ciudadela —pues a él le correspondía el cobro de los tributos—, "
             "por esta causa fueron llamados los dos por el rey.",
    (4, 29): "Y Menelao dejó como sustituto en el sumo sacerdocio a Lisímaco, "
             "su propio hermano, y Sóstrato a Crates, el jefe de los chipriotas.",
    (4, 30): "Y estando así las cosas, sucedió que los de Tarso y los de Malos "
             "se sublevaron, porque habían sido dados como regalo a Antióquide, "
             "la concubina del rey.",
    (4, 31): "Fue, pues, el rey a toda prisa a sofocar los disturbios, dejando "
             "como sustituto a Andrónico, uno de los de alto rango.",
    (4, 32): "Y creyendo Menelao que había encontrado una ocasión propicia, "
             "sustrajo algunos objetos de oro del templo y se los regaló a "
             "Andrónico, y otros los había vendido en Tiro y en las ciudades de "
             "alrededor.",
    (4, 33): "Y habiéndolo averiguado con certeza Onías, lo denunció, "
             "retirado ya en un lugar de asilo, en Dafne, junto a Antioquía.",
    (4, 34): "Por lo cual Menelao, tomando aparte a Andrónico, le rogaba que "
             "diera muerte a Onías. Y él, llegándose a Onías y persuadido a la "
             "traición, le dio la mano derecha con juramentos; y aunque "
             "estaba bajo sospecha, lo convenció de salir del asilo; y al "
             "punto lo mató, sin respeto alguno a la justicia.",
    (4, 35): "Por lo cual no sólo los judíos, sino también muchos de las otras "
             "naciones, se indignaron y llevaron a mal el asesinato injusto de "
             "aquel hombre.",
    (4, 36): "Y cuando el rey volvió de las regiones de Cilicia, le salieron al "
             "paso los judíos de la ciudad, aborreciendo también los griegos "
             "aquella maldad, por haber sido muerto Onías sin razón.",
    (4, 37): "Y Antíoco, apenado en el alma y movido a compasión, y llorando "
             "por la templanza y la gran moderación del difunto,",
    (4, 38): "y encendido de ira, al instante despojó a Andrónico de la púrpura "
             "y le desgarró las túnicas, y llevándolo por toda la ciudad hasta "
             "el mismo lugar donde había cometido la impiedad contra Onías, "
             "allí quitó de en medio al asesino, dándole el Señor el castigo "
             "que merecía.",
    (4, 39): "Y habiéndose cometido muchos sacrilegios en la ciudad por "
             "Lisímaco con el consentimiento de Menelao, y habiéndose "
             "divulgado fuera la noticia, se juntó la multitud contra "
             "Lisímaco, cuando ya se habían sacado muchos objetos de oro.",
    (4, 40): "Y alborotándose las turbas y llenándose de ira, armó Lisímaco a "
             "unos tres mil hombres y empezó a usar de violencia, poniendo al "
             "frente a un tal Aurano, avanzado en años y no menos en necedad.",
    (4, 41): "Y dándose cuenta del ataque de Lisímaco, unos agarraron piedras, "
             "otros garrotes gruesos, y algunos, cogiendo puñados de la ceniza "
             "que allí había, lo arrojaban todo revuelto contra los de "
             "Lisímaco.",
    (4, 42): "Por lo cual hirieron a muchos de ellos, y a algunos los derribaron, "
             "y a todos los pusieron en fuga; y al mismo sacrílego lo mataron "
             "junto al tesoro.",
    (4, 43): "Y sobre esto se entabló proceso contra Menelao.",
    (4, 44): "Y llegado el rey a Tiro, presentaron ante él la acusación los "
             "tres hombres enviados por el consejo de ancianos.",
    (4, 45): "Y viéndose ya perdido Menelao, prometió mucho dinero a Tolomeo "
             "hijo de Dorimeno, para que persuadiera al rey.",
    (4, 46): "Por lo cual Tolomeo, llevando aparte al rey a un peristilo como "
             "para tomar el aire, le hizo cambiar de parecer.",
    (4, 47): "Y al causante de toda la maldad, a Menelao, lo absolvió de las "
             "acusaciones; y a aquellos desdichados, que aun si hubieran "
             "alegado ante escitas habrían salido absueltos, a ésos los "
             "condenó a muerte.",
    (4, 48): "Así que pronto sufrieron la pena injusta los que habían hablado "
             "en defensa de la ciudad y del pueblo y de los vasos sagrados.",
    (4, 49): "Por lo cual también los de Tiro, aborreciendo aquella maldad, "
             "costearon con magnificencia sus funerales.",
    (4, 50): "Y Menelao, por la codicia de los que mandaban, seguía en el "
             "cargo, creciendo en maldad, convertido en el gran enemigo de sus "
             "conciudadanos.",

    # Capítulo 5
    (5, 1): "Por aquel tiempo emprendió Antíoco su segunda expedición a Egipto.",
    (5, 2): "Y sucedió que por casi toda la ciudad, durante cuarenta días, se "
            "veían correr por los aires jinetes con vestiduras recamadas de "
            "oro, armados de lanzas y formados en escuadrones,",
    (5, 3): "y desenvainar de espadas, y escuadrones de caballos en orden, y "
            "ataques y cargas de unos y otros, y movimiento de escudos, y "
            "multitud de picas, y disparos de proyectiles, y destellos de "
            "arreos de oro, y corazas de toda clase.",
    (5, 4): "Por lo cual todos pedían que aquella aparición fuera para bien.",
    (5, 5): "Y habiéndose corrido el falso rumor de que Antíoco había muerto, "
            "Jasón, tomando no menos de mil hombres, dio de improviso un "
            "asalto a la ciudad; y rechazados los de la muralla, y tomada ya "
            "por fin la ciudad, Menelao huyó a la ciudadela.",
    (5, 6): "Y Jasón hacía matanza de sus propios conciudadanos sin piedad, sin "
            "darse cuenta de que el éxito contra los parientes es la mayor de "
            "las desgracias, y creyendo levantar trofeos sobre enemigos y no "
            "sobre compatriotas.",
    (5, 7): "Del poder no se apoderó, y al fin, cubierto de vergüenza por su "
            "intriga, huyó otra vez al país de los amonitas.",
    (5, 8): "Tuvo, pues, un final desastroso: encerrado ante Aretas, el tirano "
            "de los árabes, huyendo de ciudad en ciudad, perseguido por todos, "
            "odiado como apóstata de las leyes y aborrecido como verdugo de su "
            "patria y de sus conciudadanos, fue arrojado a Egipto.",
    (5, 9): "Y el que a tantos había desterrado de su patria, pereció en tierra "
            "extraña, habiéndose embarcado hacia los lacedemonios con la "
            "esperanza de hallar amparo por el parentesco;",
    (5, 10): "y el que había arrojado a muchos sin sepultura, quedó él sin "
             "duelo, y no tuvo funeral alguno ni parte en la sepultura de sus "
             "padres.",
    (5, 11): "Y llegando al rey noticia de lo sucedido, pensó que Judea se "
             "sublevaba; por lo cual, partiendo de Egipto enfurecido en su "
             "alma, tomó la ciudad por las armas,",
    (5, 12): "y mandó a los soldados matar sin piedad a los que encontraran, y "
             "degollar a los que subieran a las casas.",
    (5, 13): "Y hubo exterminio de jóvenes y de ancianos, destrucción de "
             "muchachos y de mujeres y de niños, degüello de doncellas y de "
             "criaturas.",
    (5, 14): "Ochenta mil perecieron en aquellos tres días: cuarenta mil a mano "
             "armada, y no menos que los degollados fueron vendidos.",
    (5, 15): "Y no contento con esto, se atrevió a entrar en el templo más "
             "santo de toda la tierra, teniendo por guía a Menelao, el que se "
             "había hecho traidor a las leyes y a la patria;",
    (5, 16): "y tomando con sus manos impuras los vasos sagrados, y barriendo "
             "con sus manos profanas lo que muchos reyes habían ofrendado para "
             "realce y gloria y honra de aquel lugar.",
    (5, 17): "Y se engreía Antíoco en su pensamiento, sin ver que el Señor se "
             "había airado por poco tiempo a causa de los pecados de los "
             "habitantes de la ciudad, y que por eso había apartado la vista "
             "de aquel lugar.",
    (5, 18): "Porque, si no hubiera sucedido que estaban enredados en muchos "
             "pecados, también a él, como a Heliodoro, el enviado por el rey "
             "Seleuco a inspeccionar el tesoro, apenas hubiera entrado lo "
             "habrían azotado y apartado de su osadía.",
    (5, 19): "Pero el Señor no escogió al pueblo por causa del lugar, sino el "
             "lugar por causa del pueblo.",
    (5, 20): "Por eso también el lugar mismo, después de haber compartido las "
             "desgracias del pueblo, participó luego de sus bienes; y el que "
             "fue abandonado en la ira del Todopoderoso, fue restablecido con "
             "toda gloria en la reconciliación del gran Señor.",
    (5, 21): "Antíoco, pues, habiendo sacado del templo mil ochocientos "
             "talentos, se marchó a toda prisa a Antioquía, creyendo en su "
             "soberbia poder hacer navegable la tierra y transitable el mar, "
             "por la altivez de su corazón.",
    (5, 22): "Y dejó gobernadores para maltratar al pueblo: en Jerusalén a "
             "Filipo, de raza frigio, de carácter más bárbaro que el que lo "
             "nombró;",
    (5, 23): "y en Guerizín a Andrónico. Y además de éstos, Menelao, que se "
             "alzaba sobre los demás en maldad contra sus conciudadanos, "
             "teniendo una disposición hostil hacia los ciudadanos judíos.",
    (5, 24): "Y envió al abominable Apolonio con un ejército de veintidós mil "
             "hombres, mandándole degollar a todos los que estuvieran en edad "
             "adulta y vender a las mujeres y a los más jóvenes.",
    (5, 25): "Y éste, llegado a Jerusalén y fingiéndose pacífico, esperó hasta "
             "el día santo del sábado; y tomando ociosos a los judíos, mandó a "
             "los suyos ponerse en armas,",
    (5, 26): "y traspasó con la lanza a todos los que habían salido al "
             "espectáculo, y entrando de carrera en la ciudad con los armados, "
             "derribó a mucha gente.",
    (5, 27): "Y Judas, el llamado Macabeo, retirándose con unos diez, vivía en "
             "los montes a la manera de las fieras con los suyos; y seguían "
             "alimentándose de hierba, para no contraer la contaminación.",
    # Capítulo 6
    (6, 1): "Y no mucho después envió el rey a un anciano ateniense a obligar a "
            "los judíos a apartarse de las leyes patrias y a no vivir según "
            "las leyes de Dios;",
    (6, 2): "y a profanar también el templo de Jerusalén y darle el nombre de "
            "Zeus Olímpico, y el de Guerizín, conforme eran los que habitaban "
            "aquel lugar, el de Zeus Hospitalario.",
    (6, 3): "Y era dura y del todo insoportable la irrupción de aquella "
            "maldad.",
    (6, 4): "Porque el templo se llenaba de disolución y de orgías por obra de "
            "las naciones, que se solazaban con meretrices y se juntaban con "
            "mujeres en los recintos sagrados, y además metían dentro cosas "
            "indebidas.",
    (6, 5): "Y el altar estaba lleno de cosas ilícitas, prohibidas por las "
            "leyes.",
    (6, 6): "Y no era posible guardar el sábado, ni observar las fiestas "
            "patrias, ni siquiera confesarse judío.",
    (6, 7): "Y eran llevados por amarga fuerza, cada mes, en el día del "
            "cumpleaños del rey, al sacrificio; y llegada la fiesta de "
            "Dioniso, eran obligados a ir en procesión en honor de Dioniso "
            "coronados de hiedra.",
    (6, 8): "Y se promulgó un decreto en las ciudades griegas vecinas, a "
            "instancia de Tolomeo, para que se siguiera el mismo "
            "procedimiento contra los judíos y se los obligara a sacrificar,",
    (6, 9): "y a los que no quisieran pasarse a las costumbres griegas, "
            "degollarlos. Podía, pues, verse la miseria presente.",
    (6, 10): "Porque dos mujeres fueron llevadas por haber circuncidado a sus "
             "hijos; y colgándoles las criaturas de los pechos, y paseándolas "
             "públicamente por la ciudad, las despeñaron desde la muralla.",
    (6, 11): "Y otros, que habían corrido juntos a las cuevas cercanas para "
             "guardar en secreto el día séptimo, denunciados a Filipo, fueron "
             "quemados vivos, porque tenían escrúpulo de defenderse a sí "
             "mismos por respeto a aquel día venerabilísimo.",
    (6, 12): "Ruego, pues, a los que lean este libro que no se desalienten por "
             "estas desgracias, sino que consideren que los castigos no son "
             "para destrucción, sino para corrección de nuestro linaje.",
    (6, 13): "Porque el que a los impíos no se les deje mucho tiempo, sino que "
             "caigan en seguida en el castigo, es señal de gran beneficio.",
    (6, 14): "Pues no ha juzgado el Señor obrar con nosotros como con las demás "
             "naciones, a las que aguarda con paciencia hasta castigarlas "
             "cuando hayan llegado a la medida de sus pecados;",
    (6, 15): "para no tener que castigarnos después, cuando nuestros pecados "
             "hubieran llegado al colmo.",
    (6, 16): "Por eso jamás aparta de nosotros su misericordia; y aunque "
             "corrige con la desgracia, no abandona a su pueblo.",
    (6, 17): "Pero quede dicho esto sólo a modo de recordatorio; volvamos en "
             "pocas palabras al relato.",
    (6, 18): "Un tal Eleazar, de los escribas principales, hombre ya avanzado en "
             "años y de aspecto muy noble, era obligado a comer carne de "
             "cerdo, abriéndole la boca a la fuerza.",
    (6, 19): "Pero él, prefiriendo la muerte con honor a la vida con "
             "abominación, avanzaba por su propia voluntad hacia el potro,",
    (6, 20): "después de escupir la carne, como deben acercarse los que tienen "
             "el valor de rechazar lo que no es lícito probar ni por amor a la "
             "vida.",
    (6, 21): "Y los encargados de aquel banquete contrario a la ley, por la "
             "antigua amistad que tenían con aquel hombre, lo tomaron aparte y "
             "le rogaban que trajera carne que le fuera lícito comer, "
             "preparada por él mismo, y que fingiera comer de la carne del "
             "sacrificio ordenada por el rey;",
    (6, 22): "para que, haciendo esto, se librara de la muerte, y por la antigua "
             "amistad con ellos alcanzara clemencia.",
    (6, 23): "Pero él, tomando una resolución noble, digna de su edad y de la "
             "eminencia de su vejez y de sus canas adquiridas con honor y de "
             "su conducta intachable desde niño, y sobre todo conforme a la "
             "legislación santa dada por Dios, respondió sin tardanza, "
             "diciéndoles que lo enviaran pronto al Hades:",
    (6, 24): "«Porque no es propio de nuestra edad fingir, no sea que muchos de "
             "los jóvenes crean que Eleazar, a los noventa años, se ha pasado "
             "a las costumbres extranjeras,",
    (6, 25): "y también ellos, por mi fingimiento y por un poco de vida "
             "insignificante, se extravíen por mi causa, y yo adquiera "
             "abominación y mancha para mi vejez.",
    (6, 26): "Porque, aunque de momento me librara del castigo de los hombres, "
             "de las manos del Todopoderoso no escaparé ni vivo ni muerto.",
    (6, 27): "Por eso, dejando ahora la vida con valentía, me mostraré digno de "
             "mi vejez,",
    (6, 28): "y dejaré a los jóvenes un ejemplo noble de cómo morir de buena "
             "gana y con nobleza por las leyes venerables y santas.» Y dicho "
             "esto, fue en seguida al potro,",
    (6, 29): "habiéndose trocado en hostilidad la benevolencia que poco antes "
             "le tenían, porque tomaron aquellas palabras, según ellos "
             "creían, por locura.",
    (6, 30): "Y estando a punto de morir por los golpes, dijo gimiendo: «Al "
             "Señor, que tiene el conocimiento santo, le consta que, pudiendo "
             "librarme de la muerte, soporto en el cuerpo dolores atroces bajo "
             "los azotes, pero en el alma los sufro con gusto por su temor.»",
    (6, 31): "Y así murió éste, dejando su muerte no sólo a los jóvenes, sino "
             "también a la mayor parte de la nación, como ejemplo de nobleza y "
             "memorial de virtud.",

    # Capítulo 7
    (7, 1): "Y sucedió también que siete hermanos, apresados con su madre, "
            "eran obligados por el rey a probar la carne de cerdo, prohibida "
            "por la ley, siendo atormentados con azotes y con nervios de buey.",
    (7, 2): "Y uno de ellos, tomando la palabra en nombre de todos, dijo: «¿Qué "
            "pretendes preguntarnos y averiguar de nosotros? Porque estamos "
            "dispuestos a morir antes que quebrantar las leyes de nuestros "
            "padres.»",
    (7, 3): "Y enfurecido el rey, mandó poner al fuego sartenes y calderos.",
    (7, 4): "Y cuando estuvieron al rojo al instante, mandó cortar la lengua al "
            "que había hablado en nombre de todos, y, arrancándole el cuero "
            "cabelludo, cortarle las extremidades, a la vista de los demás "
            "hermanos y de la madre.",
    (7, 5): "Y cuando quedó del todo inútil, mandó acercarlo al fuego todavía "
            "respirando y freírlo en la sartén. Y mientras el vaho de la "
            "sartén se esparcía largamente, se exhortaban unos a otros, junto "
            "con la madre, a morir con nobleza, diciendo así:",
    (7, 6): "«El Señor Dios lo está viendo, y en verdad se compadece de "
            "nosotros, como lo declaró Moisés en el cántico que da testimonio "
            "cara a cara, diciendo: “Y se compadecerá de sus siervos.”»",
    (7, 7): "Y muerto el primero de esta manera, llevaron al segundo al "
            "escarnio; y arrancándole el cuero de la cabeza con los cabellos, "
            "le preguntaban: «¿Comerás, antes de que se te castigue el cuerpo "
            "miembro a miembro?»",
    (7, 8): "Y él, respondiendo en la lengua de sus padres, dijo: «No.» Por lo "
            "cual también éste sufrió el mismo tormento que el primero.",
    (7, 9): "Y al dar el último aliento dijo: «Tú, malvado, nos quitas la vida "
            "presente; pero el Rey del mundo, a nosotros que morimos por sus "
            "leyes, nos resucitará para una vida eterna.»",
    (7, 10): "Y después de éste, era escarnecido el tercero; y pedida la "
             "lengua, la sacó al punto, y tendió las manos con valor,",
    (7, 11): "y dijo con nobleza: «Del cielo he recibido estos miembros, y por "
             "sus leyes los desprecio, y de él espero recibirlos otra vez»;",
    (7, 12): "de modo que el rey mismo y los que estaban con él quedaron "
             "asombrados del ánimo de aquel joven, de cómo tenía en nada los "
             "dolores.",
    (7, 13): "Y muerto también éste, atormentaban del mismo modo al cuarto, "
             "maltratándolo.",
    (7, 14): "Y estando a punto de morir, dijo así: «Es preferible morir a "
             "manos de los hombres y aguardar las esperanzas puestas en Dios "
             "de ser resucitado otra vez por él; porque para ti no habrá "
             "resurrección para la vida.»",
    (7, 15): "Y en seguida, trayendo al quinto, lo maltrataban.",
    (7, 16): "Y él, mirando al rey, dijo: «Teniendo poder entre los hombres, "
             "haces lo que quieres, aunque eres corruptible; pero no creas que "
             "nuestro linaje ha sido abandonado por Dios.",
    (7, 17): "Tú aguarda, y verás su gran poder, cómo te atormentará a ti y a "
             "tu descendencia.»",
    (7, 18): "Y después de éste llevaron al sexto, y al ir a morir dijo: «No te "
             "engañes en vano; porque nosotros padecemos esto por nuestra "
             "propia culpa, por haber pecado contra nuestro Dios; por eso nos "
             "han sobrevenido cosas asombrosas.",
    (7, 19): "Pero tú no pienses que quedarás impune, habiéndote atrevido a "
             "luchar contra Dios.»",
    (7, 20): "Y sobre todo la madre fue admirable y digna de gloriosa memoria, "
             "pues viendo morir a siete hijos en el espacio de un solo día, lo "
             "soportó con entereza por las esperanzas puestas en el Señor.",
    (7, 21): "Y exhortaba a cada uno de ellos en la lengua de sus padres, llena "
             "de noble sentimiento y despertando con ánimo varonil su "
             "razonamiento de mujer, diciéndoles:",
    (7, 22): "«Yo no sé cómo aparecisteis en mis entrañas, ni fui yo quien os "
             "dio el espíritu y la vida, ni fui yo quien ordenó los elementos "
             "de cada uno.",
    (7, 23): "Por tanto, el Creador del mundo, el que formó la generación del "
             "hombre y dispuso el origen de todas las cosas, os devolverá "
             "también, con misericordia, el espíritu y la vida, ya que ahora "
             "os despreciáis a vosotros mismos por sus leyes.»",
    (7, 24): "Y Antíoco, creyéndose despreciado y receloso de aquella voz que "
             "lo injuriaba, viviendo todavía el más joven, no sólo lo exhortaba "
             "con palabras, sino que le aseguraba con juramentos que a la vez "
             "lo haría rico y dichoso si abandonaba las costumbres de sus "
             "padres, y que lo tendría por amigo y le confiaría cargos.",
    (7, 25): "Y como el joven no le hiciera el menor caso, el rey llamó a la "
             "madre y la exhortó a que aconsejara al muchacho para su salud.",
    (7, 26): "Y después de mucho exhortarla, ella accedió a persuadir a su "
             "hijo.",
    (7, 27): "Pero inclinándose hacia él, burlando al cruel tirano, habló así "
             "en la lengua de sus padres: «Hijo, ten compasión de mí, que te "
             "llevé nueve meses en el vientre, y te amamanté tres años, y te "
             "crié y te llevé hasta esta edad, y te alimenté.",
    (7, 28): "Te ruego, hijo, que mires al cielo y a la tierra, y que, viendo "
             "todo lo que hay en ellos, reconozcas que Dios los hizo de lo que "
             "no existía, y que así también nace el linaje de los hombres.",
    (7, 29): "No temas a este verdugo, sino que, mostrándote digno de tus "
             "hermanos, acepta la muerte, para que en la misericordia te "
             "recobre junto con tus hermanos.»",
    (7, 30): "Y apenas acababa ella de hablar, dijo el joven: «¿A qué esperáis? "
             "No obedezco la orden del rey; la orden que obedezco es la de la "
             "ley que fue dada a nuestros padres por medio de Moisés.",
    (7, 31): "Y tú, que has sido el inventor de toda maldad contra los hebreos, "
             "no escaparás de las manos de Dios.",
    (7, 32): "Porque nosotros padecemos por nuestros propios pecados;",
    (7, 33): "y si por castigo y corrección se ha airado un poco contra "
             "nosotros el Señor viviente, otra vez se reconciliará con sus "
             "siervos.",
    (7, 34): "Pero tú, impío y el más abominable de todos los hombres, no te "
             "engrías en vano, hinchado con esperanzas inciertas, levantando "
             "la mano contra los hijos del cielo;",
    (7, 35): "porque todavía no has escapado del juicio de Dios todopoderoso, "
             "que todo lo ve. \u00b3\u2076Porque nuestros hermanos, después de "
             "soportar un breve dolor, han caído bajo la alianza de Dios para "
             "una vida perenne; pero tú, por el juicio de Dios, llevarás el "
             "justo castigo de tu soberbia.",
    (7, 36): "Y yo, como mis hermanos, entrego el cuerpo y la vida por las "
             "leyes de nuestros padres, invocando a Dios para que pronto se "
             "muestre propicio a la nación, y para que tú, entre pruebas y "
             "azotes, confieses que sólo él es Dios;",
    (7, 38): "y para que en mí y en mis hermanos se detenga la ira del "
             "Todopoderoso, justamente descargada sobre todo nuestro linaje.»",
    (7, 39): "Y enfurecido el rey, lo trató a éste peor que a los otros, "
             "llevando a mal la burla.",
    (7, 40): "Y así murió también éste, puro, confiando del todo en el Señor.",
    (7, 41): "Y la última, después de los hijos, murió la madre.",
    (7, 42): "Baste, pues, con lo dicho acerca de los sacrificios y de los "
             "tormentos desmedidos.",

    # Capítulo 8
    (8, 1): "Y Judas, el llamado Macabeo, y los suyos, entrando a escondidas en "
            "las aldeas, llamaban a sus parientes, y allegando a los que "
            "habían permanecido en el judaísmo, reunieron hasta seis mil.",
    (8, 2): "E invocaban al Señor que mirase al pueblo pisoteado por todos, y "
            "que tuviera compasión del templo profanado por hombres impíos;",
    (8, 3): "y que se apiadara de la ciudad arruinada y a punto de quedar "
            "arrasada, y que escuchara la sangre que clamaba a él;",
    (8, 4): "y que se acordara también de la muerte inicua de los niños "
            "inocentes, y de las blasfemias proferidas contra su nombre, y que "
            "aborreciera la maldad.",
    (8, 5): "Y el Macabeo, una vez organizado, ya se hizo irresistible para las "
            "naciones, porque la ira del Señor se había vuelto misericordia.",
    (8, 6): "Y cayendo de improviso sobre ciudades y aldeas, las incendiaba; y "
            "ocupando las posiciones favorables, ponía en fuga a no pocos de "
            "los enemigos;",
    (8, 7): "sobre todo tomaba las noches por aliadas para tales golpes; y la "
            "fama de su valor se difundía por todas partes.",
    (8, 8): "Y viendo Filipo que aquel hombre iba ganando terreno poco a poco, "
            "y que avanzaba cada vez más en sus éxitos, escribió a Tolomeo, "
            "gobernador de Celesiria y Fenicia, que acudiera en auxilio de los "
            "asuntos del rey.",
    (8, 9): "Y él, designando en seguida a Nicanor hijo de Patroclo, uno de los "
            "primeros amigos, lo envió poniendo a sus órdenes no menos de "
            "veinte mil hombres de toda raza, para exterminar a toda la nación "
            "de Judea. Y le agregaron también a Gorgias, hombre militar y con "
            "buena experiencia en los asuntos de la guerra.",
    (8, 10): "Y se propuso Nicanor completar con el producto del cautiverio de "
             "los judíos el tributo debido por el rey a los romanos, que era "
             "de dos mil talentos.",
    (8, 11): "Y en seguida envió a las ciudades de la costa invitando a comprar "
             "esclavos judíos, y prometiendo entregar noventa cuerpos por un "
             "talento; sin esperar el castigo que del Todopoderoso había de "
             "seguirle.",
    (8, 12): "Y llegó a Judas la noticia de la expedición de Nicanor; y cuando "
             "comunicó a los suyos la llegada del ejército,",
    (8, 13): "los cobardes y los que no creían en la justicia de Dios se "
             "escabullían y huían del lugar;",
    (8, 14): "y los otros vendían todo lo que les quedaba, y a una rogaban al "
             "Señor que librase a los que el impío Nicanor había vendido antes "
             "siquiera de encontrarlos;",
    (8, 15): "y si no por ellos, al menos por las alianzas con sus padres, y "
             "por haber sido invocado sobre ellos su nombre venerable y "
             "magnífico.",
    (8, 16): "Y reuniendo el Macabeo a los suyos, en número de seis mil, los "
             "exhortaba a no dejarse aterrar por los enemigos ni temer la gran "
             "muchedumbre de las naciones que injustamente venían contra "
             "ellos, sino a pelear con nobleza,",
    (8, 17): "teniendo ante los ojos el ultraje que ellos habían cometido "
             "contra el lugar santo, y el atropello de la ciudad escarnecida, "
             "y además la abolición de las instituciones de sus antepasados.",
    (8, 18): "«Porque ellos —dijo— confían en las armas y a la vez en su "
             "audacia; pero nosotros confiamos en el Dios todopoderoso, que "
             "puede derribar con una sola señal a los que vienen contra "
             "nosotros y al mundo entero.»",
    (8, 19): "Y les recordó además los socorros habidos en tiempos de sus "
             "antepasados, y el de Senaquerib, cómo perecieron ciento ochenta "
             "y cinco mil;",
    (8, 20): "y la batalla que hubo en Babilonia contra los gálatas, cómo, "
             "habiendo entrado en combate ocho mil en total con cuatro mil "
             "macedonios, y estando los macedonios en apuros, aquellos seis "
             "mil destruyeron a ciento veinte mil por el auxilio que les vino "
             "del cielo, y tomaron mucho botín.",
    (8, 21): "Y habiéndolos con esto animado y dispuesto a morir por las leyes "
             "y por la patria, dividió el ejército en cuatro cuerpos,",
    (8, 22): "poniendo a sus hermanos al frente de cada cuerpo, a Simón y a "
             "José y a Jonatán, dándole a cada uno mil quinientos hombres,",
    (8, 23): "y además a Eleazar. Y habiendo leído el libro santo, y dado por "
             "santo y seña «Auxilio de Dios», tomando él mismo el mando de la "
             "primera compañía, trabó batalla con Nicanor.",
    (8, 24): "Y siendo el Todopoderoso su aliado, degollaron a más de nueve mil "
             "de los enemigos, e hirieron y mutilaron a la mayor parte del "
             "ejército de Nicanor, y a todos los obligaron a huir.",
    (8, 25): "Y tomaron el dinero de los que habían venido a comprarlos. Y "
             "después de perseguirlos largo trecho, se volvieron, apremiados "
             "por la hora;",
    (8, 26): "porque era la víspera del sábado, y por esa causa no alargaron la "
             "persecución.",
    (8, 27): "Y recogiendo sus armas y despojando a los enemigos, se ocuparon "
             "del sábado, bendiciendo con abundancia y dando gracias al Señor, "
             "que los había salvado hasta aquel día, señalándoles el comienzo "
             "de su misericordia.",
    (8, 28): "Y después del sábado, repartiendo del botín a los maltratados y a "
             "las viudas y a los huérfanos, se distribuyeron el resto entre "
             "ellos y sus hijos.",
    (8, 29): "Y hecho esto, e hiciendo una súplica en común, rogaban al Señor "
             "misericordioso que se reconciliara del todo con sus siervos.",
    (8, 30): "Y trabando combate con los de Timoteo y Baquides, mataron a más "
             "de veinte mil de ellos, y se apoderaron de fortalezas muy altas, "
             "y repartieron mucho botín, haciendo partes iguales para sí y "
             "para los maltratados y los huérfanos y las viudas, y además para "
             "los ancianos.",
    (8, 31): "Y recogiendo cuidadosamente sus armas, las guardaron todas en los "
             "lugares apropiados, y el resto de los despojos lo llevaron a "
             "Jerusalén.",
    (8, 32): "Y mataron al jefe de la tropa de Timoteo, hombre malvadísimo y "
             "que mucho había afligido a los judíos.",
    (8, 33): "Y celebrando la victoria en la patria, quemaron a los que habían "
             "incendiado los pórticos sagrados, y a Calístenes, que se había "
             "refugiado en una casa; y recibió el salario que merecía su "
             "impiedad.",
    (8, 34): "Y el tres veces criminal Nicanor, el que había traído a mil "
             "mercaderes para la venta de los judíos,",
    (8, 35): "humillado por el auxilio del Señor por medio de aquellos a "
             "quienes él tenía por los más insignificantes, despojándose de la "
             "vestidura de gala, y atravesando el interior del país como un "
             "fugitivo, solo, llegó a Antioquía, teniendo por única fortuna la "
             "destrucción de su ejército.",
    (8, 36): "Y el que se había comprometido a saldar el tributo de los romanos "
             "con el cautiverio de los de Jerusalén, iba proclamando que los "
             "judíos tenían un defensor, y que por esa razón los judíos eran "
             "invulnerables, porque seguían las leyes prescritas por él.",
    # Capítulo 9
    (9, 1): "Por aquel tiempo sucedió que Antíoco se había retirado sin orden "
            "de las regiones de Persia.",
    (9, 2): "Porque había entrado en la llamada Persépolis, e intentó saquear "
            "el templo y dominar la ciudad; por lo cual, alzándose las "
            "multitudes, recurrieron a las armas; y sucedió que Antíoco, "
            "puesto en fuga por los del país, tuvo que emprender una retirada "
            "vergonzosa.",
    (9, 3): "Y estando en Ecbátana, le llegó la noticia de lo sucedido a "
            "Nicanor y a los de Timoteo.",
    (9, 4): "Y arrebatado por la ira, pensaba descargar también sobre los "
            "judíos la maldad de los que lo habían puesto en fuga; por lo cual "
            "mandó al auriga que condujera sin parar hasta acabar el viaje, "
            "estando ya sobre él el juicio del cielo; pues así había dicho con "
            "soberbia: «Haré de Jerusalén un cementerio de judíos, en cuanto "
            "llegue allí.»",
    (9, 5): "Pero el Señor que todo lo ve, el Dios de Israel, lo hirió con una "
            "llaga incurable e invisible. Y apenas hubo acabado de hablar, se "
            "apoderó de él un dolor irremediable de entrañas y agudos tormentos "
            "internos;",
    (9, 6): "con toda justicia, pues había atormentado las entrañas de otros "
            "con muchos e inauditos suplicios.",
    (9, 7): "Pero él no cesaba en modo alguno de su arrogancia, sino que "
            "todavía se llenaba más de soberbia, respirando fuego de ira "
            "contra los judíos y mandando acelerar la marcha. Y sucedió que "
            "cayó del carro que corría a toda velocidad, y con la violenta "
            "caída se le descoyuntaron todos los miembros del cuerpo.",
    (9, 8): "Y el que poco antes creía, con soberbia sobrehumana, mandar en las "
            "olas del mar y pesar en la balanza las alturas de los montes, "
            "puesto en tierra era llevado en unas andas, mostrando a todos con "
            "evidencia el poder de Dios;",
    (9, 9): "de modo que del cuerpo del impío hervían gusanos, y viviendo aún, "
            "entre dolores y tormentos, se le desprendían las carnes, y por su "
            "hedor todo el ejército no soportaba aquella podredumbre.",
    (9, 10): "Y al que poco antes creía tocar los astros del cielo, nadie podía "
             "llevarlo, por la insoportable pesadez de su hedor.",
    (9, 11): "Entonces, pues, quebrantado, empezó a ceder mucho de su soberbia, "
             "y a llegar al conocimiento bajo el azote divino, acometido a cada "
             "instante por los dolores.",
    (9, 12): "Y no pudiendo soportar ni su propio hedor, dijo esto: «Es justo "
             "someterse a Dios, y que el que es mortal no piense cosas "
             "soberbias.»",
    (9, 13): "Y oraba el abominable al Señor, que ya no había de tener "
             "misericordia de él, diciendo así:",
    (9, 14): "que declararía libre la ciudad santa, a la que iba a toda prisa "
             "para arrasarla y convertirla en cementerio;",
    (9, 15): "y que a los judíos, a quienes había resuelto no juzgar ni dignos "
             "de sepultura, sino aniquilarlos con sus niños como pasto de "
             "aves y de fieras, los haría a todos iguales a los atenienses;",
    (9, 16): "y que el templo santo, que antes había saqueado, lo adornaría con "
             "hermosísimas ofrendas, y devolvería multiplicados todos los "
             "vasos sagrados, y costearía de sus propias rentas los gastos "
             "correspondientes a los sacrificios;",
    (9, 17): "y además de esto, que él mismo se haría judío, y que recorrería "
             "todo lugar habitado proclamando el poder de Dios.",
    (9, 18): "Pero como los dolores no cesaban en modo alguno, pues había caído "
             "sobre él el justo juicio de Dios, desesperando de sí mismo "
             "escribió a los judíos la carta que sigue, en forma de súplica, "
             "que decía así:",
    (9, 19): "«A los buenos ciudadanos judíos, muchas saludes y salud y "
             "prosperidad, del rey y general Antíoco.",
    (9, 20): "Que estéis bien vosotros y vuestros hijos, y que vuestros asuntos "
             "vayan conforme a vuestro deseo. Teniendo puesta mi esperanza en "
             "el cielo,",
    (9, 21): "me acordaba con cariño de vuestra estima y de vuestra "
             "benevolencia. Al regresar de las regiones de Persia, y habiendo "
             "caído en una enfermedad grave, he juzgado necesario proveer a la "
             "seguridad común de todos vosotros;",
    (9, 22): "no porque desespere de mi estado, sino teniendo mucha esperanza "
             "de escapar de esta enfermedad.",
    (9, 23): "Pero considerando que también mi padre, en los tiempos en que "
             "hizo campaña en las regiones altas, designó sucesor,",
    (9, 24): "para que, si ocurría algo inesperado o llegaba alguna mala "
             "noticia, los del país, sabiendo a quién quedaba encomendado el "
             "gobierno, no se turbaran;",
    (9, 25): "y además de esto, observando que los soberanos vecinos y "
             "fronterizos del reino acechan los acontecimientos y esperan lo "
             "que ha de suceder, he designado rey a mi hijo Antíoco, a quien "
             "muchas veces, al subir a las satrapías de arriba, encomendaba y "
             "presentaba a la mayoría de vosotros. Y le he escrito lo que va "
             "abajo.",
    (9, 26): "Os ruego, pues, y os pido que, acordándoos de los beneficios "
             "recibidos en común y en particular, guardéis cada uno la "
             "benevolencia que tenéis hacia mí y hacia mi hijo;",
    (9, 27): "porque estoy convencido de que él, siguiendo con moderación y "
             "humanidad mi propósito, se conducirá con vosotros del mismo "
             "modo.»",
    (9, 28): "Así, pues, el homicida y blasfemo, padeciendo lo peor, como él "
             "había hecho padecer a otros, acabó su vida en tierra extraña, en "
             "los montes, con una muerte lastimosísima.",
    (9, 29): "Y trasladaba el cuerpo Filipo, su compañero de crianza; el cual, "
             "temiendo al hijo de Antíoco, se pasó a Egipto, a Tolomeo "
             "Filométor.",

    # Capítulo 10
    (10, 1): "Y el Macabeo y los suyos, guiándolos el Señor, recobraron el "
             "templo y la ciudad;",
    (10, 2): "y derribaron los altares levantados por los extranjeros en la "
             "plaza, y también los recintos sagrados.",
    (10, 3): "Y purificando el templo, hicieron otro altar; y sacando fuego de "
             "unas piedras que habían hecho arder, ofrecieron sacrificios "
             "después de dos años, e incienso y lámparas, y pusieron los panes "
             "de la proposición.",
    (10, 4): "Y hecho esto, postrados sobre el rostro, rogaban al Señor que no "
             "volvieran a caer en tales males, sino que, si alguna vez "
             "pecaban, fueran corregidos por él con benignidad, y no "
             "entregados a naciones blasfemas y bárbaras.",
    (10, 5): "Y en el mismo día en que el templo había sido profanado por los "
             "extranjeros, sucedió que se hizo la purificación del templo, el "
             "veinticinco de aquel mismo mes, que es Quisleu.",
    (10, 6): "Y celebraron con alegría ocho días a la manera de la fiesta de "
             "las tiendas, acordándose de cómo poco antes habían pasado la "
             "fiesta de las tiendas en los montes y en las cuevas, como "
             "fieras.",
    (10, 7): "Por eso, llevando tirsos y ramos hermosos, y también palmas, "
             "daban gracias al que les había concedido purificar su propio "
             "lugar.",
    (10, 8): "Y decretaron por edicto y voto común que toda la nación de los "
             "judíos celebrara cada año aquellos días.",
    (10, 9): "Y así fue lo tocante a la muerte de Antíoco, el llamado Epífanes.",
    (10, 10): "Y ahora expondremos lo tocante a Antíoco Eupátor, hijo del "
              "impío, resumiendo los males propios de las guerras.",
    (10, 11): "Porque éste, al tomar el reino, puso al frente de los asuntos a "
              "un tal Lisias, gobernador supremo de Celesiria y Fenicia.",
    (10, 12): "Porque Tolomeo, el llamado Macrón, procurando ante todo guardar "
              "la justicia con los judíos por la injusticia que se les había "
              "hecho, intentaba resolver pacíficamente los asuntos con ellos.",
    (10, 13): "Por lo cual, acusado por los amigos ante Eupátor, y oyéndose "
              "llamar traidor a cada paso, por haber abandonado Chipre, que le "
              "había confiado Filométor, y haberse pasado a Antíoco Epífanes, "
              "no honrando con nobleza un cargo noble, se envenenó y acabó con "
              "su vida.",
    (10, 14): "Y Gorgias, hecho gobernador de aquellas regiones, mantenía "
              "tropas mercenarias, y a cada paso alimentaba la guerra contra "
              "los judíos.",
    (10, 15): "Y juntamente con éstos, también los idumeos, dueños de "
              "fortalezas bien situadas, hostigaban a los judíos, y acogiendo "
              "a los desterrados de Jerusalén, intentaban mantener la guerra.",
    (10, 16): "Y los del Macabeo, haciendo rogativa y pidiendo a Dios que fuera "
              "su aliado, se lanzaron contra las fortalezas de los idumeos;",
    (10, 17): "y atacándolas con vigor, se apoderaron de aquellos puestos, y "
              "rechazaron a todos los que peleaban sobre la muralla, y "
              "degollaban a los que encontraban, y mataron no menos de veinte "
              "mil.",
    (10, 18): "Y habiéndose refugiado no menos de nueve mil en dos torres muy "
              "bien fortificadas, provistas de todo lo necesario para resistir "
              "un asedio,",
    (10, 19): "el Macabeo, dejando a Simón y a José, y además a Zaqueo y a los "
              "suyos, en número suficiente para el asedio de aquéllas, partió "
              "él mismo a lugares que urgían más.",
    (10, 20): "Pero los de Simón, dejándose llevar de la codicia, se dejaron "
              "sobornar con dinero por algunos de los que estaban en las "
              "torres; y recibiendo setenta mil dracmas, dejaron escapar a "
              "algunos.",
    (10, 21): "Y avisado el Macabeo de lo ocurrido, reunió a los jefes del "
              "pueblo y los acusó de haber vendido por dinero a sus hermanos, "
              "soltando contra ellos a sus enemigos.",
    (10, 22): "Y a éstos, por haberse hecho traidores, los mató; y al punto "
              "tomó las dos torres.",
    (10, 23): "Y prosperándole todo en las manos con las armas, destruyó en las "
              "dos fortalezas a más de veinte mil.",
    (10, 24): "Y Timoteo, el que antes había sido derrotado por los judíos, "
              "reuniendo un gran número de tropas extranjeras y juntando no "
              "pocos caballos de Asia, se presentó dispuesto a tomar Judea por "
              "las armas.",
    (10, 25): "Y los del Macabeo, al acercarse él, para suplicar a Dios se "
              "echaron tierra sobre la cabeza y se ciñeron los lomos de saco;",
    (10, 26): "y postrándose ante el basamento que hay delante del altar, "
              "pedían que, mostrándoseles propicio, fuera enemigo de sus "
              "enemigos y adversario de sus adversarios, como declara la ley.",
    (10, 27): "Y levantándose de la oración, tomando las armas, avanzaron desde "
              "la ciudad bastante lejos; y acercándose a los enemigos, se "
              "detuvieron.",
    (10, 28): "Y apenas se difundía la aurora, atacaron unos y otros: los unos "
              "teniendo como prenda de éxito y de victoria, además de su "
              "valor, el refugio en el Señor; los otros tomando por guía de "
              "los combates su propia furia.",
    (10, 29): "Y trabándose una dura batalla, se aparecieron a los adversarios "
              "desde el cielo cinco hombres magníficos sobre caballos de "
              "frenos de oro, que se pusieron al frente de los judíos;",
    (10, 30): "y tomando en medio al Macabeo y cubriéndolo con sus armaduras, "
              "lo guardaban ileso; y contra los enemigos lanzaban saetas y "
              "rayos, de modo que, confundidos por la ceguera, eran "
              "destrozados, llenos de espanto.",
    (10, 31): "Y fueron degollados veinte mil quinientos, y seiscientos "
              "jinetes.",
    (10, 32): "Y el mismo Timoteo huyó a la fortaleza llamada Gazara, plaza "
              "muy bien guarnecida, donde mandaba Quereas.",
    (10, 33): "Y los del Macabeo cercaron con ánimo la fortaleza durante "
              "cuarenta días.",
    (10, 34): "Y los de dentro, confiados en lo escarpado del lugar, "
              "blasfemaban desmedidamente y proferían palabras impías.",
    (10, 35): "Y al despuntar el día veinticinco, unos jóvenes de los del "
              "Macabeo, encendidos de ira por las blasfemias, asaltaron la "
              "muralla, y con ánimo viril y furia de fiera iban derribando al "
              "que encontraban.",
    (10, 36): "Y otros, subiendo igualmente mientras los de dentro estaban "
              "distraídos, incendiaban las torres, y encendiendo hogueras "
              "quemaban vivos a los blasfemos; y otros derribaban las puertas, "
              "y dando entrada al resto de la tropa, ocuparon la ciudad,",
    (10, 37): "y degollaron a Timoteo, que estaba escondido en una cisterna, y "
              "a Quereas su hermano, y a Apolófanes.",
    (10, 38): "Y hecho esto, con himnos y acción de gracias bendecían al Señor, "
              "que hace grandes beneficios a Israel y les da la victoria.",
    # Capítulo 11
    (11, 1): "Y muy poco tiempo después, Lisias, tutor del rey y pariente suyo "
             "y encargado de los asuntos, llevando muy a mal lo sucedido,",
    (11, 2): "reunió unos ochenta mil hombres y toda la caballería, y marchó "
             "contra los judíos, pensando hacer de la ciudad una residencia de "
             "griegos,",
    (11, 3): "y del templo una fuente de ingresos, como los demás recintos "
             "sagrados de las naciones, y poner en venta cada año el sumo "
             "sacerdocio;",
    (11, 4): "sin tener en cuenta en modo alguno el poder de Dios, envanecido "
             "por sus miríadas de infantes y sus millares de jinetes y sus "
             "ochenta elefantes.",
    (11, 5): "Y entrando en Judea y acercándose a Betsur, plaza fortificada "
             "distante de Jerusalén unos cinco esquenos, la apretaba.",
    (11, 6): "Y cuando los del Macabeo supieron que estaba asediando las "
             "fortalezas, con lamentos y lágrimas suplicaban con el pueblo al "
             "Señor que enviara un ángel bueno para salvación de Israel.",
    (11, 7): "Y el Macabeo mismo, tomando el primero las armas, exhortó a los "
             "demás a arrostrar el peligro con él para socorrer a sus "
             "hermanos; y todos a una se lanzaron con ardor.",
    (11, 8): "Y estando allí mismo, junto a Jerusalén, se apareció "
             "poniéndose al frente de ellos un jinete vestido de blanco, "
             "blandiendo armas de oro.",
    (11, 9): "Y todos a una bendijeron al Dios misericordioso, y cobraron "
             "fuerzas en sus almas, dispuestos a atravesar no sólo a hombres, "
             "sino a las fieras más salvajes y a murallas de hierro.",
    (11, 10): "Avanzaban en formación, teniendo por aliado al que venía del "
              "cielo, pues el Señor se había compadecido de ellos.",
    (11, 11): "Y lanzándose como leones contra los enemigos, tendieron por "
              "tierra a once mil de ellos y a mil seiscientos jinetes; y a "
              "todos los demás los obligaron a huir.",
    (11, 12): "Y la mayor parte de ellos se salvaron heridos y desarmados; y el "
              "mismo Lisias se salvó huyendo vergonzosamente.",
    (11, 13): "Pero, como no era hombre sin juicio, considerando la derrota que "
              "había sufrido, y comprendiendo que los hebreos eran invencibles "
              "porque el Dios poderoso combatía con ellos, envió mensajeros",
    (11, 14): "y los persuadió a llegar a un acuerdo en condiciones justas, y "
              "les prometió que persuadiría también al rey, obligándolo a "
              "hacerse amigo de ellos.",
    (11, 15): "Y el Macabeo accedió a todo cuanto proponía Lisias, mirando por "
              "el bien común; porque cuanto el Macabeo entregó por escrito a "
              "Lisias acerca de los judíos, lo concedió el rey.",
    (11, 16): "Porque las cartas escritas a los judíos por Lisias decían de "
              "esta manera: «Lisias, al pueblo de los judíos: salud.",
    (11, 17): "Juan y Absalón, los enviados por vosotros, al entregar el "
              "documento abajo escrito, pedían sobre las cosas en él "
              "indicadas.",
    (11, 18): "Cuanto convenía someter al rey, se lo he expuesto; y lo que era "
              "admisible, lo ha concedido.",
    (11, 19): "Si, pues, mantenéis vuestra buena disposición hacia los asuntos "
              "públicos, también en adelante procuraré ser causa de bienes "
              "para vosotros.",
    (11, 20): "Y sobre estos asuntos en detalle he encargado a éstos y a los "
              "míos que traten con vosotros.",
    (11, 21): "Que estéis bien. Año ciento cuarenta y ocho, el veinticuatro de "
              "Dióscoro.»",
    (11, 22): "Y la carta del rey decía así: «El rey Antíoco a su hermano "
              "Lisias: salud.",
    (11, 23): "Habiendo pasado nuestro padre a los dioses, queriendo nosotros "
              "que los del reino vivan sin turbación para atender a sus "
              "asuntos,",
    (11, 24): "y habiendo oído que los judíos no aprueban el cambio a las "
              "costumbres griegas dispuesto por nuestro padre, sino que "
              "prefieren su propio modo de vida y piden que se les permitan "
              "sus leyes;",
    (11, 25): "queriendo, pues, que también esta nación esté libre de "
              "turbación, decidimos que se les restituya el templo y que vivan "
              "conforme a las costumbres de sus antepasados.",
    (11, 26): "Harás, pues, bien en enviarles mensajeros y darles la mano, para "
              "que, conociendo nuestra voluntad, estén de buen ánimo y "
              "atiendan con gusto a sus propios asuntos.»",
    (11, 27): "Y la carta del rey a la nación era ésta: «El rey Antíoco al "
              "consejo de ancianos de los judíos y a los demás judíos: salud.",
    (11, 28): "Si estáis bien, es como queremos; también nosotros estamos "
              "bien.",
    (11, 29): "Nos ha manifestado Menelao que deseáis volver a vuestros "
              "asuntos. \u00b3\u2070A los que regresen hasta el treinta de "
              "Xántico se les dará la mano con la seguridad",
    (11, 31): "de que los judíos usarán de sus propios alimentos y leyes como "
              "antes, y ninguno de ellos será molestado en modo alguno por lo "
              "hecho por ignorancia.",
    (11, 32): "Y he enviado también a Menelao para tranquilizaros.",
    (11, 33): "Que estéis bien. Año ciento cuarenta y ocho, el quince de "
              "Xántico.»",
    (11, 34): "Y también los romanos les enviaron una carta que decía así: "
              "«Quinto Memio y Tito Manio, legados de los romanos, al pueblo "
              "de los judíos: salud.",
    (11, 35): "Cuanto os ha concedido Lisias, el pariente del rey, también "
              "nosotros lo aprobamos.",
    (11, 36): "Y en cuanto a lo que él juzgó que debía someterse al rey, "
              "enviad en seguida a alguien, después de examinarlo, para que "
              "podamos obrar como os conviene; porque nosotros vamos de "
              "camino a Antioquía.",
    (11, 37): "Por eso daos prisa y enviad a algunos, para que también nosotros "
              "sepamos cuál es vuestro parecer.",
    (11, 38): "Que tengáis salud. Año ciento cuarenta y ocho, el quince de "
              "Xántico.»",

    # Capítulo 12
    (12, 1): "Hechos estos acuerdos, Lisias se volvió al rey, y los judíos se "
             "dedicaron a la labranza.",
    (12, 2): "Pero los gobernadores de aquellas regiones, Timoteo y Apolonio "
             "hijo de Geneo, y además Jerónimo y Demofonte, y con ellos "
             "Nicanor, el gobernador de Chipre, no los dejaban vivir en paz ni "
             "estar tranquilos.",
    (12, 3): "Y los de Jope cometieron esta gran impiedad: invitaron a los "
             "judíos que vivían entre ellos a embarcarse con sus mujeres y sus "
             "hijos en unas barcas que ellos habían dispuesto, como si no "
             "hubiera ninguna enemistad contra ellos;",
    (12, 4): "y siendo esto por decisión común de la ciudad, y habiéndolo ellos "
             "aceptado, como quienes quieren la paz y no sospechan nada, los "
             "llevaron mar adentro y los hundieron, siendo no menos de "
             "doscientos.",
    (12, 5): "Y cuando supo Judas la crueldad cometida contra los de su pueblo, "
             "dio orden a los hombres que estaban con él,",
    (12, 6): "e invocando a Dios, el juez justo, fue contra los asesinos de sus "
             "hermanos: de noche incendió el puerto y quemó las barcas, y a los "
             "que allí se habían refugiado los pasó a cuchillo.",
    (12, 7): "Y como el recinto estaba cerrado, se retiró, con intención de "
             "volver y arrancar de raíz toda la comunidad de los de Jope.",
    (12, 8): "Y sabiendo que también los de Jamnia querían hacer lo mismo con "
             "los judíos que vivían entre ellos,",
    (12, 9): "cayó de noche sobre los de Jamnia e incendió el puerto con la "
             "flota, de modo que el resplandor del fuego se veía en Jerusalén, "
             "a doscientos cuarenta estadios de distancia.",
    (12, 10): "Y alejados de allí nueve estadios, mientras marchaban contra "
              "Timoteo, cayeron sobre él unos árabes, no menos de cinco mil "
              "hombres y quinientos jinetes.",
    (12, 11): "Y trabándose una dura batalla, y saliendo victoriosos los de "
              "Judas por el auxilio de Dios, los nómadas, derrotados, pidieron "
              "a Judas que les diera la mano, prometiéndole darle ganado y "
              "ayudarle en lo demás.",
    (12, 12): "Y Judas, comprendiendo que en verdad podían serle útiles en "
              "muchas cosas, accedió a hacer las paces con ellos; y recibida "
              "la mano, se retiraron a sus tiendas.",
    (12, 13): "Y atacó también cierta ciudad de sólidas fortificaciones, "
              "rodeada de murallas y habitada por gentes de todas las razas, "
              "llamada Caspín.",
    (12, 14): "Y los de dentro, confiados en la solidez de las murallas y en "
              "sus provisiones de víveres, trataban con insolencia a los de "
              "Judas, injuriándolos, y además blasfemando y diciendo lo que no "
              "es lícito.",
    (12, 15): "Pero los de Judas, invocando al gran Soberano del mundo, al que "
              "sin arietes ni máquinas de guerra derribó a Jericó en tiempos "
              "de Josué, se lanzaron como fieras contra la muralla;",
    (12, 16): "y tomando la ciudad por voluntad de Dios, hicieron una matanza "
              "indescriptible, de modo que el lago vecino, de dos estadios de "
              "ancho, parecía desbordar lleno de sangre.",
    (12, 17): "Y alejados de allí setecientos cincuenta estadios, llegaron a "
              "Járaca, donde los judíos llamados tubianos.",
    (12, 18): "Y a Timoteo no lo hallaron en aquellos lugares, pues se había "
              "retirado de allí sin haber hecho nada, aunque había dejado en "
              "cierto lugar una guarnición muy bien fortificada.",
    (12, 19): "Pero Dositeo y Sosípatro, jefes de los del Macabeo, saliendo, "
              "destruyeron a los que Timoteo había dejado en la fortaleza, más "
              "de diez mil hombres.",
    (12, 20): "Y el Macabeo, ordenando su ejército en compañías, los puso al "
              "frente de las compañías; y se lanzaron contra Timoteo, que "
              "tenía consigo ciento veinte mil infantes y nueve mil jinetes.",
    (12, 21): "Y al saber Timoteo la llegada de Judas, envió por delante a las "
              "mujeres y a la impedimenta al llamado Carnión; porque aquel "
              "lugar era difícil de asediar y de acceso difícil por lo "
              "estrecho de todos los pasos.",
    (12, 22): "Y al aparecer la primera compañía de Judas, y sobrecogidos de "
              "terror los enemigos, y viniendo sobre ellos el espanto por la "
              "manifestación del que todo lo ve, echaron a huir, cada uno por "
              "su lado, de modo que muchas veces eran heridos por los suyos y "
              "traspasados por el filo de sus propias espadas.",
    (12, 23): "Y Judas apretaba más la persecución, atravesando a aquellos "
              "criminales, y destruyó hasta treinta mil hombres.",
    (12, 24): "Y el mismo Timoteo, cayendo en manos de los de Dositeo y "
              "Sosípatro, les rogaba con mucha astucia que lo soltaran sano y "
              "salvo, porque tenía en su poder a los padres de muchos y a los "
              "hermanos de otros, y les iría mal si no.",
    (12, 25): "Y como asegurara con muchas palabras el compromiso de "
              "devolverlos ilesos, lo soltaron por la salvación de sus "
              "hermanos.",
    (12, 26): "Y saliendo contra Carnión y el templo de Atargatis, degolló a "
              "veinticinco mil personas.",
    (12, 27): "Y después de la derrota y destrucción de éstos, marchó también "
              "contra Efrón, ciudad fortificada, en la que había multitudes de "
              "todas las razas; y jóvenes robustos, apostados delante de las "
              "murallas, se defendían con vigor; y allí había gran cantidad de "
              "máquinas y de proyectiles.",
    (12, 28): "Pero invocando al Soberano que con su poder quebranta las "
              "fuerzas de los enemigos, tomaron la ciudad, y tendieron por "
              "tierra a veinticinco mil de los de dentro.",
    (12, 29): "Y partiendo de allí, se lanzaron contra la ciudad de los "
              "escitas, que dista de Jerusalén seiscientos estadios.",
    (12, 30): "Pero atestiguando los judíos allí establecidos la benevolencia "
              "que los de Escitópolis habían tenido con ellos, y el trato "
              "humano en los tiempos de la desgracia,",
    (12, 31): "les dieron las gracias y los exhortaron a seguir siendo "
              "benévolos con su pueblo, y llegaron a Jerusalén, estando ya "
              "cerca la fiesta de las semanas.",
    (12, 32): "Y después de la llamada Pentecostés, marcharon contra Gorgias, "
              "el gobernador de Idumea.",
    (12, 33): "Y él salió con tres mil infantes y cuatrocientos jinetes;",
    (12, 34): "y trabada la batalla, sucedió que cayeron unos pocos de los "
              "judíos.",
    (12, 35): "Y un tal Dositeo, de los de Bacenor, hombre de a caballo y "
              "fuerte, tenía agarrado a Gorgias, y asiéndolo de la clámide lo "
              "arrastraba con vigor; y queriendo coger vivo a aquel maldito, "
              "uno de los jinetes tracios cayó sobre él y le cortó el hombro, "
              "y Gorgias escapó a Marisa.",
    (12, 36): "Y como los de Esdrías llevaran mucho tiempo peleando y "
              "estuvieran agotados, invocó Judas al Señor para que se "
              "manifestara como su aliado y guía en la batalla;",
    (12, 37): "y entonando en la lengua de sus padres el grito de guerra con "
              "himnos, y cayendo de improviso sobre los de Gorgias, los puso "
              "en fuga.",
    (12, 38): "Y Judas, recogiendo su ejército, llegó a la ciudad de Odolam; y "
              "llegando el día séptimo, se purificaron según la costumbre y "
              "guardaron allí el sábado.",
    (12, 39): "Y al día siguiente fueron los de Judas, al tiempo en que ya era "
              "necesario hacerlo, a recoger los cuerpos de los caídos y a "
              "llevarlos, con sus parientes, a los sepulcros de sus padres.",
    (12, 40): "Y hallaron bajo las túnicas de cada uno de los muertos objetos "
              "consagrados de los ídolos de Jamnia, cosa que la ley prohíbe a "
              "los judíos; y fue claro para todos que por esta causa habían "
              "caído.",
    (12, 41): "Todos, pues, bendiciendo la obra del Señor, juez justo, que hace "
              "manifiesto lo oculto,",
    (12, 42): "se volvieron a la súplica, pidiendo que el pecado cometido fuera "
              "borrado del todo. Y el noble Judas exhortó a la multitud a "
              "guardarse de pecar, viendo con sus propios ojos lo que había "
              "sucedido por el pecado de los caídos.",
    (12, 43): "Y haciendo una colecta entre los hombres, hasta dos mil dracmas "
              "de plata, las envió a Jerusalén para que se ofreciera un "
              "sacrificio por el pecado, obrando muy bien y noblemente, "
              "pensando en la resurrección;",
    (12, 44): "porque, si no esperara que los caídos habían de resucitar, sería "
              "superfluo y ridículo orar por los muertos;",
    (12, 45): "y también porque miraba la hermosísima recompensa reservada a "
              "los que se duermen con piedad: pensamiento santo y piadoso. Por "
              "eso hizo la expiación por los muertos, para que quedaran "
              "libres del pecado.",

    # Capítulo 13
    (13, 1): "Y el año ciento cuarenta y nueve llegó a oídos de los de Judas "
             "que Antíoco Eupátor venía con grandes tropas contra Judea,",
    (13, 2): "y con él Lisias, su tutor y encargado de los asuntos, teniendo "
             "cada uno una fuerza griega de ciento diez mil infantes y cinco "
             "mil trescientos jinetes y veintidós elefantes y trescientos "
             "carros falcados.",
    (13, 3): "Y se les unió también Menelao, y exhortaba a Antíoco con mucha "
             "hipocresía, no por la salvación de la patria, sino creyendo que "
             "sería restablecido en el cargo.",
    (13, 4): "Pero el Rey de los reyes despertó la ira de Antíoco contra aquel "
             "criminal; y como Lisias le indicase que él era el causante de "
             "todos los males, mandó que lo llevaran a Berea y lo mataran "
             "allí, según la costumbre del lugar.",
    (13, 5): "Porque hay en aquel lugar una torre de cincuenta codos llena de "
             "ceniza, y tenía un artefacto giratorio que por todos lados caía "
             "a pico sobre la ceniza.",
    (13, 6): "Allí, al que es reo de sacrilegio o ha cometido algún otro crimen "
             "extraordinario, todos lo empujan a la muerte.",
    (13, 7): "De tal muerte le tocó morir al inicuo Menelao, sin alcanzar "
             "siquiera sepultura en la tierra;",
    (13, 8): "y con toda justicia, pues, ya que había cometido muchos pecados "
             "contra el altar, cuyo fuego y cuya ceniza eran santos, en ceniza "
             "recibió la muerte.",
    (13, 9): "Y el rey venía con el ánimo embravecido, dispuesto a mostrar a "
             "los judíos lo peor de lo que había ocurrido en tiempos de su "
             "padre.",
    (13, 10): "Y cuando Judas supo esto, mandó al pueblo invocar al Señor día y "
              "noche, para que, si alguna vez lo hizo, también ahora socorriera",
    (13, 11): "a los que estaban a punto de ser privados de la ley y de la "
              "patria y del templo santo, y no dejara que el pueblo, que "
              "apenas empezaba a respirar, cayera en manos de naciones "
              "blasfemas.",
    (13, 12): "Y habiéndolo hecho todos a una, y habiendo suplicado al Señor "
              "misericordioso con llanto y ayunos y postración durante tres "
              "días sin interrupción, Judas los animó y les mandó ponerse en "
              "marcha.",
    (13, 13): "Y a solas con los ancianos, resolvió salir y decidir la suerte "
              "de la guerra con el auxilio de Dios antes de que el ejército "
              "del rey entrara en Judea y se apoderara de la ciudad.",
    (13, 14): "Y encomendando la decisión al Señor del mundo, y exhortando a "
              "los suyos a pelear con nobleza hasta la muerte por las leyes, "
              "por el templo, por la ciudad, por la patria, por sus "
              "instituciones, acampó el ejército junto a Modín.",
    (13, 15): "Y dando a los suyos por santo y seña «Victoria de Dios», con los "
              "jóvenes más escogidos cayó de noche sobre el cuartel real, y "
              "mató en el campamento a unos dos mil hombres, y atravesó al "
              "principal de los elefantes con el que iba en su torre;",
    (13, 16): "y al final llenaron el campamento de espanto y de confusión, y "
              "se retiraron victoriosos.",
    (13, 17): "Y esto sucedió cuando ya despuntaba el día, por el amparo del "
              "Señor que lo asistía.",
    (13, 18): "Y el rey, habiendo probado la audacia de los judíos, intentó "
              "tomar aquellos lugares con estratagemas;",
    (13, 19): "y marchó contra Betsur, plaza fuerte de los judíos: atacaba, era "
              "rechazado, chocaba, quedaba menguado.",
    (13, 20): "Y Judas hacía llegar a los de dentro lo necesario.",
    (13, 21): "Pero Ródoco, de las filas judías, descubría los secretos a los "
              "enemigos; fue buscado y apresado y encerrado.",
    (13, 22): "Trató el rey por segunda vez con los de Betsur, dio la mano, "
              "recibió la suya, se retiró;",
    (13, 23): "atacó a los de Judas, fue derrotado; supo que Filipo, a quien "
              "había dejado al frente de los asuntos en Antioquía, se había "
              "rebelado; se turbó, llamó a los judíos, se sometió, y juró "
              "todas las condiciones justas; se reconcilió y ofreció "
              "sacrificio, honró el templo y el lugar, y se mostró benigno;",
    (13, 24): "y recibió bien al Macabeo, y dejó a Hegemónides por gobernador "
              "desde Tolemaida hasta el territorio de los gerrenos;",
    (13, 25): "llegó a Tolemaida. Los de Tolemaida llevaban a mal el tratado, "
              "porque se indignaban en extremo; querían anular lo pactado.",
    (13, 26): "Subió Lisias a la tribuna, hizo la defensa como pudo, los "
              "persuadió y los aplacó, los hizo benévolos, y volvió a "
              "Antioquía. Así pasó lo de la expedición y la retirada del rey.",
    # Capítulo 14
    (14, 1): "Y al cabo de tres años llegó a oídos de los de Judas que "
             "Demetrio hijo de Seleuco, entrando por el puerto de Trípoli con "
             "una fuerza poderosa y una flota,",
    (14, 2): "se había apoderado del país, después de quitar de en medio a "
             "Antíoco y a su tutor Lisias.",
    (14, 3): "Y un tal Alcimo, que había sido antes sumo sacerdote y se había "
             "contaminado voluntariamente en los tiempos de la mezcla con los "
             "gentiles, comprendiendo que de ningún modo tenía ya salvación ni "
             "acceso al altar santo,",
    (14, 4): "vino al rey Demetrio hacia el año ciento cincuenta y uno, "
             "llevándole una corona de oro y una palma, y además de esto los "
             "ramos de olivo que se acostumbra ofrecer del templo; y aquel día "
             "se estuvo quieto.",
    (14, 5): "Pero habiendo hallado ocasión propicia para su locura, llamado "
             "por Demetrio al consejo y preguntado en qué disposición y "
             "propósito estaban los judíos, respondió a esto:",
    (14, 6): "«Los judíos llamados asideos, a cuyo frente está Judas Macabeo, "
             "mantienen la guerra y promueven sediciones, sin dejar que el "
             "reino alcance la tranquilidad.",
    (14, 7): "Por eso, despojado yo de la gloria de mis antepasados —hablo del "
             "sumo sacerdocio—, he venido aquí por segunda vez:",
    (14, 8): "primero, mirando sinceramente por lo que toca al rey; y segundo, "
             "mirando también por mis propios conciudadanos; porque por la "
             "insensatez de los que he dicho, todo nuestro linaje sufre no "
             "poco.",
    (14, 9): "Y tú, oh rey, conocidas cada una de estas cosas, provee al país y "
             "a nuestro linaje acosado, conforme a la humanidad accesible que "
             "tienes con todos;",
    (14, 10): "porque, mientras viva Judas, es imposible que los asuntos "
              "alcancen la paz.»",
    (14, 11): "Y dicho esto por él, en seguida los demás amigos, que estaban "
              "mal dispuestos hacia Judas, encendieron más a Demetrio.",
    (14, 12): "Y designando al punto a Nicanor, el que había sido jefe de los "
              "elefantes, y nombrándolo gobernador de Judea, lo envió,",
    (14, 13): "dándole órdenes por escrito de quitar de en medio al mismo "
              "Judas, y dispersar a los suyos, y establecer a Alcimo como sumo "
              "sacerdote del templo grandísimo.",
    (14, 14): "Y los gentiles de Judea que habían huido de Judas se unían en "
              "tropel a Nicanor, pensando que las desdichas y desgracias de "
              "los judíos serían su propia prosperidad.",
    (14, 15): "Y oyendo la llegada de Nicanor y el ataque de las naciones, "
              "echándose tierra encima, suplicaban al que estableció a su "
              "pueblo para siempre y siempre ampara con manifestaciones "
              "visibles a su propia heredad.",
    (14, 16): "Y por orden de su jefe, partiendo de allí al instante, trabaron "
              "combate con ellos junto a la aldea de Lessaú.",
    (14, 17): "Y Simón, el hermano de Judas, había chocado con Nicanor, pero "
              "sufrió un revés por el desconcierto repentino ante los "
              "adversarios.",
    (14, 18): "Sin embargo, oyendo Nicanor el valor que tenían los de Judas y "
              "su entereza en los combates por la patria, recelaba decidir la "
              "cuestión por la sangre.",
    (14, 19): "Por eso envió a Posidonio y a Teódoto y a Matatías a dar y "
              "recibir la mano.",
    (14, 20): "Y después de mucho examinar estas cosas, y de haberlas "
              "comunicado el jefe a la tropa, y apareciendo el acuerdo "
              "unánime, aceptaron el tratado.",
    (14, 21): "Y fijaron el día en que se reunirían a solas en un mismo lugar; "
              "y se adelantó un carro de cada parte, y colocaron sillas.",
    (14, 22): "Dispuso Judas hombres armados listos en los puntos estratégicos, "
              "no fuera que de parte de los enemigos hubiera de repente alguna "
              "traición; y tuvieron la conversación conveniente.",
    (14, 23): "Y Nicanor se quedó en Jerusalén, y no hacía nada fuera de lugar; "
              "y despidió a las turbas que se habían reunido en tropel.",
    (14, 24): "Y tenía a Judas continuamente ante sus ojos, pues se había "
              "aficionado de corazón a aquel hombre.",
    (14, 25): "Y lo animó a casarse y a tener hijos; y se casó, y vivió "
              "tranquilo, y compartió la vida con él.",
    (14, 26): "Y Alcimo, viendo la mutua amistad entre ellos, y tomando el "
              "tratado que habían hecho, se fue a Demetrio y le dijo que "
              "Nicanor pensaba en contra de los intereses del reino, pues "
              "había designado sucesor a Judas, el conspirador contra su "
              "reino.",
    (14, 27): "Y el rey, enfurecido y exasperado por las calumnias de aquel "
              "malvado, escribió a Nicanor diciendo que llevaba muy a mal el "
              "tratado, y mandándole enviar cuanto antes al Macabeo preso a "
              "Antioquía.",
    (14, 28): "Y llegado esto a Nicanor, quedó turbado, y llevaba a mal anular "
              "lo pactado, no habiendo hecho aquel hombre ningún agravio.",
    (14, 29): "Pero como no era posible oponerse al rey, aguardaba una ocasión "
              "propicia para cumplirlo con alguna estratagema.",
    (14, 30): "Y el Macabeo, viendo que Nicanor se comportaba con él más "
              "ásperamente y que en el trato acostumbrado se había vuelto más "
              "rudo, comprendiendo que aquella aspereza no venía de nada "
              "bueno, reunió a no pocos de los suyos y se escondió de Nicanor.",
    (14, 31): "Y el otro, cuando comprendió que aquel hombre le había ganado "
              "con nobleza la partida, fue al templo grandísimo y santo, "
              "mientras los sacerdotes ofrecían los sacrificios prescritos, y "
              "les mandó entregar a aquel hombre.",
    (14, 32): "Y como ellos afirmasen con juramentos que no sabían dónde estaba "
              "el que buscaba,",
    (14, 33): "extendiendo la mano derecha hacia el templo, juró esto: «Si no "
              "me entregáis a Judas preso, arrasaré hasta el suelo este "
              "recinto de Dios, y derribaré el altar, y levantaré aquí un "
              "templo espléndido a Dioniso.»",
    (14, 34): "Y dicho esto, se fue. Y los sacerdotes, tendiendo las manos al "
              "cielo, invocaban al que siempre ha sido el defensor de nuestra "
              "nación, diciendo así:",
    (14, 35): "«Tú, Señor, que de nada tienes necesidad, quisiste que hubiera "
              "entre nosotros un templo de tu morada.",
    (14, 36): "Y ahora, Santo, Señor de toda santidad, guarda para siempre sin "
              "mancha esta casa recién purificada.»",
    (14, 37): "Y fue denunciado a Nicanor un tal Razís, de los ancianos de "
              "Jerusalén, hombre que amaba a sus conciudadanos y de muy buena "
              "fama, y al que por su benevolencia llamaban padre de los "
              "judíos.",
    (14, 38): "Porque en los tiempos anteriores, los de la mezcla con los "
              "gentiles, había sido acusado de judaísmo, y había expuesto "
              "cuerpo y alma por el judaísmo con todo empeño.",
    (14, 39): "Y queriendo Nicanor hacer patente la hostilidad que tenía contra "
              "los judíos, envió más de quinientos soldados a prenderlo;",
    (14, 40): "porque pensaba que, prendiéndolo a él, les causaría una "
              "desgracia.",
    (14, 41): "Y estando la tropa a punto de tomar la torre y forzando la "
              "puerta del patio y mandando traer fuego y prender las puertas, "
              "viéndose a punto de ser apresado, se echó sobre la espada,",
    (14, 42): "queriendo morir noblemente antes que caer en manos de aquellos "
              "criminales y ser ultrajado indignamente en su nobleza.",
    (14, 43): "Pero, no habiendo acertado el golpe por la prisa del trance, y "
              "entrando las turbas por las puertas, corrió con nobleza al muro "
              "y se arrojó con ánimo varonil sobre la multitud.",
    (14, 44): "Y retrocediendo aquéllos rápidamente, y quedando un espacio "
              "libre, cayó en medio del vacío.",
    (14, 45): "Y respirando todavía y encendido de ánimo, se levantó, "
              "brotándole la sangre a chorros, y con las heridas terribles "
              "atravesó corriendo por medio de la multitud, y puesto en pie "
              "sobre una roca escarpada,",
    (14, 46): "quedándose ya del todo sin sangre, se arrancó las entrañas y, "
              "tomándolas con ambas manos, las arrojó sobre la multitud; e "
              "invocando al que es dueño de la vida y del espíritu para que se "
              "las devolviera otra vez, murió de esta manera.",

    # Capítulo 15
    (15, 1): "Y Nicanor, sabiendo que los de Judas estaban en la región de "
             "Samaria, resolvió atacarlos con toda seguridad en el día del "
             "descanso.",
    (15, 2): "Y diciéndole los judíos que por fuerza lo acompañaban: «No los "
             "destruyas de manera tan salvaje y bárbara; honra el día que ha "
             "sido honrado de antemano con santidad por el que todo lo ve»,",
    (15, 3): "aquel tres veces criminal preguntó si hay en el cielo un soberano "
             "que haya mandado guardar el día del sábado.",
    (15, 4): "Y declarando ellos: «El Señor viviente, él mismo, es soberano en "
             "el cielo, y es el que mandó observar el día séptimo»,",
    (15, 5): "el otro dijo: «Y yo soy soberano sobre la tierra, y el que manda "
             "tomar las armas y cumplir el servicio del rey.» Sin embargo, no "
             "logró llevar a cabo su cruel propósito.",
    (15, 6): "Y Nicanor, engreído con toda arrogancia, había resuelto levantar "
             "un trofeo común con los despojos de los de Judas.",
    (15, 7): "Pero el Macabeo confiaba sin cesar, con toda esperanza, en "
             "alcanzar socorro de parte del Señor.",
    (15, 8): "Y exhortaba a los suyos a no temer el ataque de las naciones, "
             "sino a tener en la mente los auxilios que antes les habían "
             "venido del cielo, y a esperar también ahora la victoria que les "
             "vendría del Todopoderoso.",
    (15, 9): "Y animándolos con la ley y los profetas, y recordándoles además "
             "los combates que ya habían llevado a término, los dejó más "
             "animosos.",
    (15, 10): "Y despertando su ánimo, les dio las órdenes, mostrándoles a la "
              "vez la deslealtad de las naciones y su violación de los "
              "juramentos.",
    (15, 11): "Y armando a cada uno de ellos no tanto con la seguridad de los "
              "escudos y las lanzas como con el aliento de las buenas "
              "palabras, y contándoles además un sueño digno de crédito, los "
              "alegró sobremanera.",
    (15, 12): "Y la visión de aquel sueño era ésta: Onías, el que había sido "
              "sumo sacerdote, hombre noble y bueno, respetuoso en el trato, "
              "manso de carácter, comedido al hablar, y ejercitado desde niño "
              "en todo lo propio de la virtud, éste, tendidas las manos, "
              "oraba por toda la comunidad de los judíos;",
    (15, 13): "y que luego se aparecía de igual manera un hombre que destacaba "
              "por sus canas y por su gloria, y que había en torno a él una "
              "eminencia admirable y llena de majestad;",
    (15, 14): "y que Onías, tomando la palabra, decía: «Éste es el que ama a "
              "sus hermanos, el que ora mucho por el pueblo y por la ciudad "
              "santa: Jeremías, el profeta de Dios.»",
    (15, 15): "Y que Jeremías, extendiendo la mano derecha, entregaba a Judas "
              "una espada de oro, y al dársela decía estas palabras:",
    (15, 16): "«Toma la espada santa, don de Dios, con la cual quebrantarás a "
              "los adversarios.»",
    (15, 17): "Y animados por las palabras de Judas, hermosísimas y capaces de "
              "mover a la virtud y de hacer varoniles las almas de los "
              "jóvenes, resolvieron no acampar, sino lanzarse con nobleza, y "
              "trabando combate con todo valor decidir la cuestión, porque "
              "estaban en peligro la ciudad y las cosas santas y el templo.",
    (15, 18): "Porque la inquietud por las mujeres y los hijos, y además por "
              "los hermanos y los parientes, ocupaba en ellos un lugar "
              "secundario; el mayor y primer temor era el del templo "
              "consagrado.",
    (15, 19): "Y para los que habían quedado en la ciudad no era pequeña la "
              "angustia, turbados por el ataque en campo abierto.",
    (15, 20): "Y esperando ya todos la decisión inminente, y estando ya los "
              "enemigos a punto de chocar y el ejército formado, y los "
              "elefantes colocados en el lugar oportuno, y la caballería "
              "dispuesta en las alas,",
    (15, 21): "el Macabeo, viendo la presencia de aquellas multitudes y la "
              "variada provisión de armas y la ferocidad de los elefantes, "
              "levantando las manos al cielo, invocó al Señor que hace "
              "prodigios, sabiendo que no es por las armas, sino que, según él "
              "lo juzgue, otorga la victoria a los que son dignos.",
    (15, 22): "Y decía invocándolo de esta manera: «Tú, Señor, enviaste tu "
              "ángel en tiempos de Ezequías, rey de Judea, y mató del "
              "campamento de Senaquerib a ciento ochenta y cinco mil.",
    (15, 23): "Y ahora, Soberano de los cielos, envía un ángel bueno delante de "
              "nosotros, para espanto y temblor;",
    (15, 24): "por la grandeza de tu brazo sean aterrados los que con blasfemia "
              "vienen contra tu pueblo santo.» Y con esto terminó.",
    (15, 25): "Y los de Nicanor avanzaban con trompetas y cantos de guerra;",
    (15, 26): "y los de Judas trabaron combate con los enemigos entre "
              "invocaciones y oraciones.",
    (15, 27): "Y peleando con las manos y orando a Dios con el corazón, "
              "tendieron por tierra a no menos de treinta y cinco mil, muy "
              "alegres por la manifiesta ayuda de Dios.",
    (15, 28): "Y terminada la acción, y retirándose con alegría, reconocieron a "
              "Nicanor caído con su armadura.",
    (15, 29): "Y levantándose el clamor y el alboroto, bendecían al Soberano en "
              "la lengua de sus padres.",
    (15, 30): "Y el que en todo, con el cuerpo y con el alma, había sido el "
              "primer combatiente por sus conciudadanos, el que guardó para "
              "los de su pueblo el afecto de su juventud, mandó cortar la "
              "cabeza de Nicanor y la mano con el brazo, y llevarlas a "
              "Jerusalén.",
    (15, 31): "Y llegado allí, y convocando a los de su pueblo, y poniendo a "
              "los sacerdotes delante del altar, mandó llamar a los de la "
              "ciudadela.",
    (15, 32): "Y mostrándoles la cabeza del abominable Nicanor y la mano del "
              "blasfemo, la que había extendido con jactancia contra la casa "
              "santa del Todopoderoso,",
    (15, 33): "y cortando la lengua del impío Nicanor, dijo que la daría en "
              "trozos a las aves, y que el pago de su locura lo colgaran "
              "frente al templo.",
    (15, 34): "Y todos bendijeron hacia el cielo al Señor que se manifiesta, "
              "diciendo: «Bendito el que ha guardado sin mancha su propio "
              "lugar.»",
    (15, 35): "Y colgó la cabeza de Nicanor de la ciudadela, bien visible para "
              "todos, como señal manifiesta del auxilio del Señor.",
    (15, 36): "Y decretaron todos por voto común no dejar en modo alguno pasar "
              "sin marca aquel día, \u207d\u00b3\u2077\u207e sino señalar el "
              "trece del mes duodécimo —que en la lengua de este país se llama "
              "Adar—, el día anterior al día de Mardoqueo.",
    (15, 37): "Habiendo, pues, sucedido así lo de Nicanor, y estando desde "
              "aquellos tiempos la ciudad en poder de los hebreos, también yo "
              "pondré aquí fin a mi relato.",
    (15, 38): "Y si ha quedado bien y con acierto en la composición, eso es lo "
              "que yo mismo quería; y si mediocre y del montón, era lo que "
              "estaba a mi alcance.",
    (15, 39): "Porque, así como beber vino solo es dañoso, e igualmente lo es "
              "el agua sola, pero el vino mezclado con agua resulta ya "
              "agradable y produce deleite, así también la composición del "
              "relato deleita los oídos de los que dan con esta obra. Y aquí "
              "estará el final.",
}
