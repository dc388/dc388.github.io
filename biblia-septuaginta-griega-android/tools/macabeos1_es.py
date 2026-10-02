"""1 Macabeos en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Y es, con
diferencia, el más importante de los que aquí no lo son, porque cuenta lo que
pasó entre Malaquías y Mateo: los ciento cincuenta años de silencio del Antiguo
Testamento no fueron silencio, y éste es el documento.

Aquí está Antíoco IV entrando en el templo y llevándose el altar de oro; el
«abominación de la desolación» puesto sobre el altar el 15 de Quisleu (1:54),
que es la frase que Jesús repite en Mateo 24; el sacerdote Matatías negándose a
sacrificar y huyendo a los montes con sus cinco hijos; Judas Macabeo; la
purificación del templo tres años después, día por día (4:52-59), que es la
fiesta que en Juan 10:22 se llama «la dedicación» y que los judíos siguen
celebrando como Janucá. Sin este libro, esos versículos del Nuevo Testamento
son frases sueltas.

Es una crónica sobria, escrita primero en hebreo —el original se perdió— por
alguien cercano a la corte de los asmoneos. Y tiene una peculiaridad que no
conviene pasar por alto: no nombra a Dios ni una vez. Dice «el Cielo», dice «el
que ayuda», dice «él»; nunca «Dios» ni «Señor». No es que el autor no crea:
es la reverencia de su época, la misma que está detrás del «reino de los
cielos» de Mateo. Aquí se ha respetado: donde el griego dice οὐρανός, esta
traducción dice «el Cielo», con mayúscula, y no se ha rellenado con «Dios».

También conviene saber que el autor está del lado de los asmoneos y escribe
para justificar su dinastía. Eso no lo hace falso, pero sí interesado, y se
nota en cómo trata a los que no combatieron.

Las fechas van en la era seléucida, que es la que usa el libro: el año 1 es el
312 antes de Cristo. Se dejan como están, sin convertirlas dentro del texto.

Un detalle de esta edición griega: en 4:7 el versículo 8 no va aparte, sino
metido dentro del 7 con un ⁸ volado. No se ha corregido; la traducción hace lo
mismo, con el mismo ⁸, para que el español y el griego se puedan seguir
renglón por renglón.
"""

from __future__ import annotations

MACABEOS1_ES: dict[tuple[int, ...], str] = {
    (1, 1): "Y sucedió que, después de que Alejandro de Macedonia, hijo de "
            "Filipo, que salió de la tierra de Quitim, derrotó a Darío, rey de "
            "los persas y de los medos, y reinó en su lugar, habiendo reinado "
            "antes sobre Grecia,",
    (1, 2): "emprendió muchas guerras y se apoderó de plazas fuertes y degolló "
            "a reyes,",
    (1, 3): "y llegó hasta los confines de la tierra, y tomó los despojos de "
            "multitud de naciones; y la tierra quedó en silencio ante él, y se "
            "engrió y se le ensoberbeció el corazón.",
    (1, 4): "Y reunió un ejército muy poderoso, y dominó países y naciones y "
            "principados, y le pagaban tributo.",
    (1, 5): "Y después de esto cayó en cama y comprendió que se moría.",
    (1, 6): "Y llamó a sus servidores más ilustres, los que se habían criado "
            "con él desde joven, y les repartió su reino estando él todavía "
            "vivo.",
    (1, 7): "Y reinó Alejandro doce años, y murió.",
    (1, 8): "Y sus servidores se hicieron con el poder, cada uno en su "
            "territorio;",
    (1, 9): "y todos se ciñeron la diadema después de su muerte, y sus hijos "
            "después de ellos durante muchos años; y multiplicaron los males "
            "en la tierra.",
    (1, 10): "Y salió de ellos una raíz pecadora, Antíoco Epífanes, hijo del "
             "rey Antíoco, que había estado como rehén en Roma; y empezó a "
             "reinar el año ciento treinta y siete del reino de los griegos.",
    (1, 11): "En aquellos días salió de Israel una casta de hijos sin ley, y "
             "convencieron a muchos diciendo: «Vamos a hacer una alianza con "
             "las naciones que nos rodean; porque desde que nos apartamos de "
             "ellas nos han sobrevenido muchos males».",
    (1, 12): "Y aquella propuesta les pareció bien;",
    (1, 13): "y algunos del pueblo se ofrecieron con entusiasmo y fueron al "
             "rey; y él les dio permiso para adoptar las costumbres de las "
             "naciones.",
    (1, 14): "Y construyeron un gimnasio en Jerusalén conforme a los usos de "
             "las naciones,",
    (1, 15): "y se rehicieron el prepucio y se apartaron de la alianza santa, "
             "y se unieron a las naciones, y se vendieron para hacer el mal.",
    (1, 16): "Y una vez asentado el reino ante Antíoco, éste se propuso reinar "
             "sobre la tierra de Egipto, para reinar sobre los dos reinos.",
    (1, 17): "Y entró en Egipto con un ejército numeroso, con carros y "
             "elefantes y jinetes y una gran flota;",
    (1, 18): "y trabó batalla contra Tolomeo, rey de Egipto; y Tolomeo se "
             "replegó ante él y huyó, y cayeron muchos heridos.",
    (1, 19): "Y tomaron las plazas fuertes de la tierra de Egipto, y él se "
             "llevó los despojos de la tierra de Egipto.",
    (1, 20): "Y volvió Antíoco, después de haber derrotado a Egipto, el año "
             "ciento cuarenta y tres, y subió contra Israel y contra Jerusalén "
             "con un ejército numeroso;",
    (1, 21): "y entró con soberbia en el santuario, y se llevó el altar de "
             "oro, y el candelabro de la luz con todos sus utensilios,",
    (1, 22): "y la mesa de la proposición y las copas de las libaciones y las "
             "tazas y los incensarios de oro, y el velo y las coronas y el "
             "adorno de oro que había en la fachada del templo; y lo arrancó "
             "todo.",
    (1, 23): "Y se llevó la plata y el oro y los objetos preciosos; y se llevó "
             "los tesoros escondidos que encontró.",
    (1, 24): "Y tomándolo todo, se marchó a su tierra. E hicieron una matanza, "
             "y hablaron con gran soberbia.",
    (1, 25): "Y hubo un gran duelo en Israel por todos sus lugares; y gimieron "
             "los príncipes y los ancianos, las doncellas y los jóvenes "
             "desfallecieron, y la hermosura de las mujeres se mudó.",
    (1, 27): "Todo novio entonó un lamento; la que estaba sentada en la cámara "
             "nupcial quedó de luto.",
    (1, 28): "Y tembló la tierra por sus habitantes, y toda la casa de Jacob "
             "se vistió de vergüenza.",
    (1, 29): "Dos años después envió el rey a un recaudador de tributos a las "
             "ciudades de Judá; y llegó a Jerusalén con un ejército numeroso.",
    (1, 30): "Y les habló con palabras de paz, pero con engaño, y ellos le "
             "creyeron; y cayó de repente sobre la ciudad y la hirió con un "
             "gran golpe, e hizo perecer a mucha gente de Israel.",
    (1, 31): "Y tomó los despojos de la ciudad y le prendió fuego, y derribó "
             "sus casas y las murallas de alrededor,",
    (1, 32): "y llevó cautivas a las mujeres y a los niños; y se apoderaron de "
             "los ganados.",
    (1, 33): "Y fortificaron la ciudad de David con una muralla grande y "
             "sólida, con torres fuertes, y la convirtieron en su ciudadela.",
    (1, 34): "Y pusieron allí una gente pecadora, hombres sin ley, y se "
             "hicieron fuertes en ella.",
    (1, 35): "Y almacenaron armas y víveres, y, reuniendo los despojos de "
             "Jerusalén, los depositaron allí; y aquello vino a ser una gran "
             "trampa,",
    (1, 36): "y una emboscada contra el santuario, y un adversario perverso "
             "para Israel de continuo.",
    (1, 37): "Y derramaron sangre inocente alrededor del santuario, y "
             "mancharon el santuario.",
    (1, 38): "Y huyeron por su causa los habitantes de Jerusalén, y la ciudad "
             "se convirtió en morada de extraños; y fue extraña a los que en "
             "ella habían nacido, y sus propios hijos la abandonaron.",
    (1, 39): "Su santuario quedó desolado como un desierto; sus fiestas se "
             "volvieron duelo, sus sábados, afrenta; su honor, desprecio.",
    (1, 40): "A la medida de su gloria se multiplicó su deshonra, y su "
             "grandeza se volvió duelo.",
    (1, 41): "Y escribió el rey a todo su reino que todos fuesen un solo "
             "pueblo,",
    (1, 42): "y que cada uno abandonase sus propias costumbres; y todas las "
             "naciones aceptaron lo que el rey mandaba.",
    (1, 43): "Y muchos de Israel se avinieron a su culto, y sacrificaron a los "
             "ídolos y profanaron el sábado.",
    (1, 44): "Y envió el rey cartas por mano de mensajeros a Jerusalén y a las "
             "ciudades de Judá, ordenando que siguiesen costumbres extrañas al "
             "país,",
    (1, 45): "y que se prohibiesen en el santuario los holocaustos y los "
             "sacrificios y las libaciones, y que se profanasen los sábados y "
             "las fiestas,",
    (1, 46): "y que se manchasen el santuario y los santos;",
    (1, 47): "que se levantasen altares y recintos sagrados e ídolos, y que se "
             "sacrificasen cerdos y animales impuros,",
    (1, 48): "y que se dejase a los hijos sin circuncidar, y que se "
             "contaminasen a sí mismos con toda clase de impureza y "
             "profanación,",
    (1, 49): "de modo que olvidasen la ley y cambiasen todos sus preceptos.",
    (1, 50): "Y el que no obrase conforme a la palabra del rey, moriría.",
    (1, 51): "Conforme a todas estas palabras escribió a todo su reino, y "
             "nombró inspectores sobre todo el pueblo; y mandó a las ciudades "
             "de Judá que ofreciesen sacrificios, ciudad por ciudad.",
    (1, 52): "Y se les juntaron muchos del pueblo, todo el que abandonaba la "
             "ley; e hicieron el mal en la tierra,",
    (1, 53): "y obligaron a Israel a esconderse en toda clase de refugios.",
    (1, 54): "Y el día quince de Quisleu del año ciento cuarenta y cinco "
             "levantaron la abominación de la desolación sobre el altar; y en "
             "las ciudades de Judá, alrededor, levantaron altares,",
    (1, 55): "y quemaban incienso a las puertas de las casas y en las plazas.",
    (1, 56): "Y los libros de la ley que encontraban los rompían y los "
             "quemaban.",
    (1, 57): "Y a aquel en cuyo poder se hallaba un libro de la alianza, y al "
             "que se mostraba conforme con la ley, la sentencia del rey lo "
             "condenaba a muerte.",
    (1, 58): "Con su poder obraban así con Israel, con los que encontraban mes "
             "tras mes en las ciudades.",
    (1, 59): "Y el día veinticinco del mes ofrecían sacrificios sobre el ara "
             "que estaba encima del altar.",
    (1, 60): "Y a las mujeres que habían circuncidado a sus hijos las mataban "
             "conforme al decreto,",
    (1, 61): "y colgaban a las criaturas del cuello de sus madres; y también a "
             "sus familias y a los que los habían circuncidado.",
    (1, 62): "Y muchos en Israel se mantuvieron firmes y decidieron no comer "
             "nada impuro,",
    (1, 63): "y aceptaron morir antes que mancharse con aquellos alimentos y "
             "profanar la alianza santa; y murieron.",
    (1, 64): "Y cayó sobre Israel una ira muy grande.",

    (2, 1): "En aquellos días se levantó Matatías, hijo de Juan, hijo de "
            "Simeón, sacerdote de los hijos de Joarib, de Jerusalén, y se "
            "estableció en Modín.",
    (2, 2): "Y tenía cinco hijos: Juan, llamado Gadí;",
    (2, 3): "Simón, llamado Tasí;",
    (2, 4): "Judas, llamado Macabeo;",
    (2, 5): "Eleazar, llamado Auarán; y Jonatán, llamado Safús.",
    (2, 6): "Y vio las blasfemias que se cometían en Judá y en Jerusalén,",
    (2, 7): "y dijo: «¡Ay de mí! ¿Para qué he nacido, para ver la ruina de mi "
            "pueblo y la ruina de la ciudad santa, y para quedarme allí cuando "
            "es entregada en manos de enemigos, y el santuario en manos de "
            "extraños?",
    (2, 8): "Su templo ha quedado como un hombre sin honra;",
    (2, 9): "los objetos de su gloria han sido llevados cautivos; sus niños "
            "han sido asesinados en sus plazas, y sus jóvenes por la espada "
            "del enemigo.",
    (2, 10): "¿Qué nación no ha heredado su realeza y no se ha apoderado de "
             "sus despojos?",
    (2, 11): "Todo su adorno le ha sido arrancado; de libre ha pasado a "
             "esclava.",
    (2, 12): "Y he aquí que nuestro santuario y nuestra hermosura y nuestra "
             "gloria han quedado desolados, y las naciones los han profanado.",
    (2, 13): "¿Para qué seguimos viviendo?».",
    (2, 14): "Y Matatías y sus hijos rasgaron sus vestidos y se vistieron de "
             "cilicio, e hicieron gran duelo.",
    (2, 15): "Y llegaron a la ciudad de Modín los enviados del rey, los que "
             "forzaban a la apostasía, para que ofreciesen sacrificios.",
    (2, 16): "Y muchos de Israel se acercaron a ellos; y Matatías y sus hijos "
             "también se juntaron.",
    (2, 17): "Y tomaron la palabra los enviados del rey y dijeron a Matatías: "
             "«Tú eres príncipe e ilustre y grande en esta ciudad, y estás "
             "respaldado por hijos y hermanos.",
    (2, 18): "Acércate, pues, el primero y cumple el mandato del rey, como lo "
             "han hecho todas las naciones y los príncipes de Judá y los que "
             "han quedado en Jerusalén; y serás tú y tu casa de los amigos del "
             "rey, y tú y tus hijos seréis honrados con plata y con oro y con "
             "muchos regalos».",
    (2, 19): "Y respondió Matatías y dijo a gran voz: «Aunque todas las "
             "naciones que hay en los dominios del reino del rey le obedezcan, "
             "apartándose cada una del culto de sus padres, y hayan escogido "
             "cumplir sus mandatos,",
    (2, 20): "yo y mis hijos y mis hermanos caminaremos en la alianza de "
             "nuestros padres.",
    (2, 21): "Líbrenos el Cielo de abandonar la ley y los preceptos.",
    (2, 22): "No obedeceremos las palabras del rey apartándonos de nuestro "
             "culto ni a derecha ni a izquierda».",
    (2, 23): "Y cuando acabó de decir estas palabras, se acercó un judío a la "
             "vista de todos para ofrecer sacrificio sobre el ara de Modín, "
             "conforme al mandato del rey.",
    (2, 24): "Y lo vio Matatías, y ardió en celo, y se le estremecieron las "
             "entrañas, y dejó subir su furor conforme a la ley; y corriendo, "
             "lo degolló sobre el ara.",
    (2, 25): "Y al enviado del rey que forzaba a sacrificar lo mató en aquel "
             "mismo momento, y derribó el ara;",
    (2, 26): "y ardió en celo por la ley, como hizo Fineés con Zambrí, hijo de "
             "Salú.",
    (2, 27): "Y gritó Matatías por la ciudad a gran voz, diciendo: «¡Todo el "
             "que arda en celo por la ley y mantenga la alianza, que salga "
             "detrás de mí!».",
    (2, 28): "Y huyeron él y sus hijos a los montes, y dejaron cuanto tenían "
             "en la ciudad.",
    (2, 29): "Entonces bajaron muchos al desierto, buscando la justicia y el "
             "derecho, para establecerse allí:",
    (2, 30): "ellos y sus hijos y sus mujeres y sus ganados, porque los males "
             "se habían endurecido sobre ellos.",
    (2, 31): "Y se les comunicó a los hombres del rey y a las tropas que "
             "estaban en Jerusalén, en la ciudad de David, que unos hombres "
             "que habían desatendido el mandato del rey habían bajado a los "
             "escondrijos del desierto.",
    (2, 32): "Y corrieron muchos tras ellos y, alcanzándolos, acamparon frente "
             "a ellos y se dispusieron a atacarlos en día de sábado.",
    (2, 33): "Y les dijeron: «¡Basta ya! Salid y haced conforme a la palabra "
             "del rey, y viviréis».",
    (2, 34): "Y ellos dijeron: «No saldremos, ni cumpliremos la palabra del "
             "rey profanando el día del sábado».",
    (2, 35): "Y se apresuraron a atacarlos.",
    (2, 36): "Y ellos no les respondieron, ni les arrojaron una piedra, ni "
             "taponaron los escondrijos,",
    (2, 37): "diciendo: «Muramos todos en nuestra inocencia; el Cielo y la "
             "tierra son testigos de que nos hacéis perecer sin juicio».",
    (2, 38): "Y los atacaron en combate en sábado; y murieron ellos y sus "
             "mujeres y sus hijos y sus ganados, hasta mil personas.",
    (2, 39): "Y lo supo Matatías y los suyos, e hicieron por ellos un duelo "
             "grandísimo.",
    (2, 40): "Y se dijeron unos a otros: «Si todos hacemos como han hecho "
             "nuestros hermanos y no peleamos contra las naciones por nuestra "
             "vida y por nuestros preceptos, nos exterminarán muy pronto de la "
             "tierra».",
    (2, 41): "Y aquel día tomaron esta decisión, diciendo: «A todo hombre que "
             "venga a atacarnos en día de sábado, le haremos frente, y no "
             "moriremos todos como murieron nuestros hermanos en los "
             "escondrijos».",
    (2, 42): "Entonces se les unió la asamblea de los asideos, gente valiente "
             "de Israel, todos los que se entregaban de buen grado a la ley.",
    (2, 43): "Y todos los que huían de aquellos males se les agregaron, y "
             "fueron para ellos un refuerzo.",
    (2, 44): "Y formaron un ejército, e hirieron a los pecadores en su ira y a "
             "los hombres sin ley en su furor; y los demás huyeron a las "
             "naciones para salvarse.",
    (2, 45): "Y Matatías y los suyos recorrieron el país y derribaron las "
             "aras,",
    (2, 46): "y circuncidaron por la fuerza a cuantos niños sin circuncidar "
             "hallaron en los términos de Israel.",
    (2, 47): "Y persiguieron a los hijos de la soberbia, y la obra prosperó en "
             "sus manos.",
    (2, 48): "Y defendieron la ley de la mano de las naciones y de la mano de "
             "los reyes, y no dejaron levantar cabeza al pecador.",
    (2, 49): "Y se acercaron los días en que Matatías había de morir, y dijo a "
             "sus hijos: «Ahora se ha afianzado la soberbia y el escarmiento, "
             "y es tiempo de ruina y de ira ardiente.",
    (2, 50): "Y ahora, hijos, arded en celo por la ley y dad vuestra vida por "
             "la alianza de nuestros padres.",
    (2, 51): "Acordaos de las obras que nuestros padres hicieron en sus "
             "generaciones, y alcanzaréis gran gloria y nombre eterno.",
    (2, 52): "¿No fue hallado fiel Abrahán en la prueba, y le fue contado como "
             "justicia?",
    (2, 53): "José, en el tiempo de su angustia, guardó el mandamiento, y "
             "llegó a ser señor de Egipto.",
    (2, 54): "Fineés, nuestro padre, por haber ardido en celo, recibió la "
             "alianza de un sacerdocio eterno.",
    (2, 55): "Josué, por cumplir la palabra, llegó a ser juez en Israel.",
    (2, 56): "Caleb, por dar testimonio ante la asamblea, recibió una tierra "
             "en herencia.",
    (2, 57): "David, por su piedad, heredó un trono de reino eterno.",
    (2, 58): "Elías, por arder en celo por la ley, fue arrebatado como al "
             "cielo.",
    (2, 59): "Ananías, Azarías y Misael, por creer, fueron salvados de la "
             "llama.",
    (2, 60): "Daniel, por su inocencia, fue librado de la boca de los "
             "leones.",
    (2, 61): "Y así, entended, generación tras generación, que ninguno de los "
             "que esperan en él desfallecerá.",
    (2, 62): "Y no temáis las palabras de un hombre pecador, porque su gloria "
             "acaba en estiércol y en gusanos.",
    (2, 63): "Hoy se ensalza, y mañana no se lo encuentra, porque ha vuelto a "
             "su polvo y sus planes se han deshecho.",
    (2, 64): "Y vosotros, hijos, sed fuertes y portaos como hombres en "
             "vuestra ley, porque por ella seréis glorificados.",
    (2, 65): "Y aquí está Simeón, vuestro hermano: sé que es hombre de "
             "consejo; escuchadlo siempre, y él será para vosotros un padre.",
    (2, 66): "Y Judas Macabeo, fuerte y valiente desde su juventud: él será "
             "vuestro jefe de ejército, y llevará la guerra contra los "
             "pueblos.",
    (2, 67): "Y vosotros atraeos a todos los que cumplen la ley, y vengad a "
             "vuestro pueblo.",
    (2, 68): "Dad a las naciones su merecido, y atended a los mandatos de la "
             "ley».",
    (2, 69): "Y los bendijo, y fue reunido con sus padres.",
    (2, 70): "Y murió el año ciento cuarenta y seis; y lo sepultaron sus hijos "
             "en los sepulcros de sus padres, en Modín; y todo Israel hizo por "
             "él gran duelo.",

    (3, 1): "Y se levantó en su lugar su hijo Judas, llamado Macabeo.",
    (3, 2): "Y lo ayudaban todos sus hermanos y todos los que se habían unido "
            "a su padre, y peleaban con alegría la guerra de Israel.",
    (3, 3): "Y él extendió la gloria de su pueblo; se vistió la coraza como un "
            "gigante y se ciñó sus armas de guerra; trabó combates, protegiendo "
            "el campamento con su espada.",
    (3, 4): "Y fue como un león en sus obras, y como un cachorro que ruge "
            "sobre la presa.",
    (3, 5): "Y persiguió a los sin ley rastreándolos, y abrasó a los que "
            "perturbaban a su pueblo;",
    (3, 6): "y los sin ley se encogieron de miedo ante él, y todos los obreros "
            "de la iniquidad quedaron turbados, y la salvación prosperó en su "
            "mano.",
    (3, 7): "Y amargó a muchos reyes, y alegró a Jacob con sus obras; y por "
            "siempre será su memoria una bendición.",
    (3, 8): "Y recorrió las ciudades de Judá, y exterminó de ella a los "
            "impíos, y apartó de Israel la ira;",
    (3, 9): "y su nombre llegó hasta el extremo de la tierra, y reunió a los "
            "que perecían.",
    (3, 10): "Y Apolonio reunió gente de las naciones, y de Samaria un gran "
             "ejército, para pelear contra Israel.",
    (3, 11): "Y lo supo Judas, y salió a su encuentro y lo derrotó y lo mató; "
             "y cayeron muchos heridos, y los demás huyeron.",
    (3, 12): "Y tomaron sus despojos; y Judas se quedó con la espada de "
             "Apolonio, y con ella peleó todos sus días.",
    (3, 13): "Y oyó Serón, jefe del ejército de Siria, que Judas había reunido "
             "una tropa y una asamblea de fieles consigo, y que salían a la "
             "guerra.",
    (3, 14): "Y dijo: «Me haré un nombre y seré glorioso en el reino, y "
             "pelearé contra Judas y contra los suyos, los que desprecian la "
             "palabra del rey».",
    (3, 15): "Y se le añadió, y subió con él un fuerte campamento de impíos "
             "para ayudarle a tomar venganza de los hijos de Israel.",
    (3, 16): "Y se acercó hasta la subida de Bet-Horón; y Judas salió a su "
             "encuentro con muy poca gente.",
    (3, 17): "Y cuando vieron el ejército que venía a su encuentro, dijeron a "
             "Judas: «¿Cómo vamos a poder pelear, siendo tan pocos, contra una "
             "multitud tan grande? Y además estamos desfallecidos, que hoy no "
             "hemos comido».",
    (3, 18): "Y dijo Judas: «Es cosa fácil que muchos queden cercados por las "
             "manos de unos pocos; y para el Cielo no hay diferencia entre "
             "salvar con muchos o con pocos;",
    (3, 19): "porque la victoria en la guerra no está en la multitud del "
             "ejército, sino que la fuerza viene del Cielo.",
    (3, 20): "Ellos vienen contra nosotros llenos de insolencia y de "
             "iniquidad, para acabar con nosotros y con nuestras mujeres y con "
             "nuestros hijos, y para despojarnos;",
    (3, 21): "pero nosotros peleamos por nuestras vidas y por nuestras "
             "leyes.",
    (3, 22): "Y él los quebrantará delante de nosotros; vosotros no les "
             "tengáis miedo».",
    (3, 23): "Y cuando acabó de hablar, se lanzó de repente sobre ellos, y "
             "Serón y su ejército quedaron destrozados delante de él.",
    (3, 24): "Y los persiguieron por la bajada de Bet-Horón hasta la llanura; "
             "y cayeron de ellos unos ochocientos hombres, y los demás huyeron "
             "a tierra de los filisteos.",
    (3, 25): "Y empezó el miedo a Judas y a sus hermanos, y el espanto cayó "
             "sobre las naciones de alrededor.",
    (3, 26): "Y su nombre llegó hasta el rey, y todas las naciones contaban "
             "las batallas de Judas.",
    (3, 27): "Y cuando el rey Antíoco oyó estas noticias, se enfureció; y "
             "mandó reunir todas las fuerzas de su reino, un ejército "
             "poderosísimo.",
    (3, 28): "Y abrió su tesoro y dio a sus tropas la paga de un año, y les "
             "mandó que estuviesen preparados para cualquier necesidad.",
    (3, 29): "Y vio que se le había acabado la plata de los tesoros, y que los "
             "tributos del país eran escasos por la discordia y por el "
             "estrago que él mismo había causado en aquella tierra al querer "
             "abolir las costumbres que había desde los primeros días.",
    (3, 30): "Y temió no tener, como otras veces, para los gastos y para los "
             "regalos que antes repartía con mano generosa;",
    (3, 31): "y quedó muy apurado en su ánimo, y decidió ir a Persia y cobrar "
             "los tributos de aquellas regiones y reunir mucha plata.",
    (3, 32): "Y dejó a Lisias, hombre ilustre y del linaje real, al frente de "
             "los asuntos del rey desde el río Éufrates hasta los términos de "
             "Egipto,",
    (3, 33): "y para que criase a Antíoco su hijo hasta que él volviese.",
    (3, 34): "Y le entregó la mitad de las tropas y los elefantes, y le dio "
             "instrucciones sobre todo lo que quería, y sobre los habitantes "
             "de Judea y de Jerusalén:",
    (3, 35): "que enviase contra ellos un ejército para arrancar y acabar con "
             "la fuerza de Israel y con el resto de Jerusalén, y para borrar "
             "su memoria de aquel lugar,",
    (3, 36): "y para establecer extranjeros en todos sus términos y repartir "
             "su tierra en suertes.",
    (3, 37): "Y el rey tomó la otra mitad de las tropas que quedaban, y partió "
             "de Antioquía, capital de su reino, el año ciento cuarenta y "
             "siete; y pasó el río Éufrates y recorría las provincias de "
             "arriba.",
    (3, 38): "Y Lisias escogió a Tolomeo hijo de Dorimeno, y a Nicanor y a "
             "Gorgias, hombres poderosos de entre los amigos del rey;",
    (3, 39): "y envió con ellos cuarenta mil hombres y siete mil jinetes, para "
             "que fuesen a la tierra de Judá y la asolasen conforme a la "
             "palabra del rey.",
    (3, 40): "Y partieron con todo su ejército y llegaron, y acamparon cerca "
             "de Emaús, en el llano.",
    (3, 41): "Y oyeron su fama los mercaderes del país, y tomaron plata y oro "
             "en gran cantidad y grillos, y vinieron al campamento para tomar "
             "a los hijos de Israel como esclavos; y se les unieron tropas de "
             "Siria y de tierra de los filisteos.",
    (3, 42): "Y vio Judas, y sus hermanos, que los males se habían "
             "multiplicado y que las tropas acampaban en sus términos; y "
             "conocieron las órdenes del rey, que había mandado acabar con el "
             "pueblo y exterminarlo.",
    (3, 43): "Y se dijeron unos a otros: «Levantemos a nuestro pueblo de su "
             "ruina, y peleemos por nuestro pueblo y por el santuario».",
    (3, 44): "Y se reunió la asamblea para estar preparados para la guerra, y "
             "para orar y pedir misericordia y compasión.",
    (3, 45): "Y Jerusalén estaba deshabitada como un desierto; no había quien "
             "entrase ni saliese de los que en ella habían nacido; y el "
             "santuario estaba pisoteado, y en la ciudadela había extranjeros, "
             "que era posada de las naciones; y se había ido la alegría de "
             "Jacob, y habían cesado la flauta y la cítara.",
    (3, 46): "Y se reunieron y fueron a Masfá, frente a Jerusalén, porque "
             "antes había en Masfá un lugar de oración para Israel.",
    (3, 47): "Y ayunaron aquel día, y se vistieron de cilicio y se echaron "
             "ceniza en la cabeza, y rasgaron sus vestidos.",
    (3, 48): "Y desplegaron el libro de la ley, aquello mismo que las naciones "
             "escudriñaban buscando las imágenes de sus ídolos.",
    (3, 49): "Y trajeron las vestiduras del sacerdocio y las primicias y los "
             "diezmos; y presentaron a los nazireos que habían cumplido sus "
             "días;",
    (3, 50): "y clamaron a voz en grito al Cielo, diciendo: «¿Qué haremos con "
             "éstos, y adónde los llevaremos?",
    (3, 51): "Tu santuario está pisoteado y profanado, y tus sacerdotes en "
             "duelo y humillación.",
    (3, 52): "Y he aquí que las naciones se han reunido contra nosotros para "
             "acabar con nosotros; tú sabes lo que traman contra nosotros.",
    (3, 53): "¿Cómo vamos a poder resistir delante de ellos, si tú no nos "
             "ayudas?».",
    (3, 54): "Y tocaron las trompetas y clamaron a gran voz.",
    (3, 55): "Y después de esto Judas nombró jefes del pueblo: jefes de mil y "
             "de cien y de cincuenta y de diez.",
    (3, 56): "Y dijo a los que estaban construyendo casa, y a los que se "
             "habían prometido con una mujer, y a los que plantaban viñas, y a "
             "los cobardes, que se volviese cada uno a su casa conforme a la "
             "ley.",
    (3, 57): "Y levantó el campamento y acamparon al sur de Emaús.",
    (3, 58): "Y dijo Judas: «Ceñíos y portaos como valientes; y estad "
             "preparados para mañana temprano, para pelear contra esas "
             "naciones que se han juntado contra nosotros para acabar con "
             "nosotros y con nuestro santuario;",
    (3, 59): "porque más nos vale morir en la guerra que ver los males de "
             "nuestro pueblo y del santuario.",
    (3, 60): "Y como sea la voluntad del Cielo, así se hará».",

    (4, 1): "Y tomó Gorgias cinco mil hombres y mil jinetes escogidos, y el "
            "destacamento partió de noche,",
    (4, 2): "para caer sobre el campamento de los judíos y atacarlos por "
            "sorpresa; y los de la ciudadela le servían de guías.",
    (4, 3): "Y lo oyó Judas, y partió él con sus valientes para atacar al "
            "ejército del rey que estaba en Emaús,",
    (4, 4): "mientras las tropas seguían dispersas fuera del campamento.",
    (4, 5): "Y llegó Gorgias de noche al campamento de Judas y no encontró a "
            "nadie; y los buscaba por los montes, porque dijo: «Éstos huyen de "
            "nosotros».",
    (4, 6): "Y al amanecer apareció Judas en la llanura con tres mil hombres; "
            "sólo que no tenían ni corazas ni espadas como hubieran querido.",
    (4, 7): "Y vieron el campamento de las naciones, fuerte y acorazado, y la "
            "caballería que lo rodeaba, y que aquéllos estaban entrenados para "
            "la guerra. \u2078Y dijo Judas a los hombres que estaban con él: "
            "«No temáis su multitud, ni os acobardéis ante su acometida.",
    (4, 9): "Acordaos de cómo fueron salvados nuestros padres en el mar Rojo, "
            "cuando el faraón los perseguía con su ejército.",
    (4, 10): "Y ahora clamemos al Cielo, por si nos quiere y se acuerda de la "
             "alianza de nuestros padres, y quebranta hoy este ejército "
             "delante de nosotros;",
    (4, 11): "y conocerán todas las naciones que hay quien rescate y salve a "
             "Israel».",
    (4, 12): "Y los extranjeros alzaron los ojos y los vieron venir de "
             "frente,",
    (4, 13): "y salieron del campamento a la batalla; y los de Judas tocaron "
             "las trompetas.",
    (4, 14): "Y vinieron a las manos, y las naciones fueron destrozadas y "
             "huyeron a la llanura;",
    (4, 15): "y todos los rezagados cayeron a espada; y los persiguieron hasta "
             "Gázara y hasta las llanuras de Idumea y de Azoto y de Jamnia; y "
             "cayeron de ellos unos tres mil hombres.",
    (4, 16): "Y volvió Judas con su ejército de perseguirlos,",
    (4, 17): "y dijo al pueblo: «No codiciéis los despojos, porque tenemos "
             "batalla por delante,",
    (4, 18): "y Gorgias y su ejército están en el monte cerca de nosotros; "
             "estad ahora firmes frente a nuestros enemigos y pelead contra "
             "ellos, y después tomad los despojos con toda tranquilidad».",
    (4, 19): "Aún estaba Judas acabando de decir esto, cuando apareció un "
             "destacamento asomando por el monte.",
    (4, 20): "Y vieron que los suyos habían sido puestos en fuga y que estaban "
             "quemando el campamento, porque el humo que se veía mostraba lo "
             "que había pasado.",
    (4, 21): "Y al darse cuenta de esto se acobardaron muchísimo; y viendo "
             "además el ejército de Judas en la llanura, dispuesto para la "
             "batalla,",
    (4, 22): "huyeron todos a tierra de extranjeros.",
    (4, 23): "Y Judas volvió al saqueo del campamento; y tomaron mucho oro y "
             "plata y jacinto y púrpura marina, y grandes riquezas.",
    (4, 24): "Y al volver cantaban himnos y bendecían al Cielo: «Porque es "
             "bueno, porque su misericordia es eterna».",
    (4, 25): "Y hubo aquel día una gran salvación para Israel.",
    (4, 26): "Y cuantos extranjeros se salvaron fueron a contarle a Lisias "
             "todo lo ocurrido.",
    (4, 27): "Y él, al oírlo, quedó confundido y desanimado, porque no había "
             "salido con Israel como él quería, ni había resultado como el rey "
             "le había mandado.",
    (4, 28): "Y al año siguiente reclutó sesenta mil hombres escogidos y cinco "
             "mil jinetes, para acabar con ellos por la guerra.",
    (4, 29): "Y llegaron a Idumea y acamparon en Betsur; y les salió al "
             "encuentro Judas con diez mil hombres.",
    (4, 30): "Y vio que el ejército era fuerte, y oró diciendo: «Bendito seas, "
             "salvador de Israel, tú que quebrantaste la acometida del gigante "
             "por mano de tu siervo David, y entregaste el campamento de los "
             "extranjeros en manos de Jonatán hijo de Saúl y de su escudero.",
    (4, 31): "Entrega este ejército en manos de tu pueblo Israel, y queden "
             "avergonzados de su tropa y de su caballería.",
    (4, 32): "Infúndeles cobardía y derrite la audacia de su fuerza, y "
             "tiemblen ante su derrota.",
    (4, 33): "Derríbalos con la espada de los que te aman, y te alaben con "
             "himnos todos los que conocen tu nombre».",
    (4, 34): "Y vinieron a las manos, y cayeron del ejército de Lisias unos "
             "cinco mil hombres, cayeron frente a ellos.",
    (4, 35): "Y viendo Lisias la derrota de sus filas y el arrojo que había "
             "cobrado el de Judas, y que estaban dispuestos a vivir o a morir "
             "con nobleza, se marchó a Antioquía; y allí reclutaba mercenarios "
             "para volver a Judea con fuerzas todavía mayores.",
    (4, 36): "Y dijo Judas y sus hermanos: «Mirad, nuestros enemigos han sido "
             "destrozados; subamos a purificar el santuario y a dedicarlo de "
             "nuevo».",
    (4, 37): "Y se reunió todo el ejército y subieron al monte Sión.",
    (4, 38): "Y vieron el santuario desolado, y el altar profanado, y las "
             "puertas quemadas, y en los atrios plantas crecidas como en un "
             "bosque o como en uno de los montes, y las cámaras derribadas.",
    (4, 39): "Y rasgaron sus vestidos e hicieron gran duelo, y se echaron "
             "ceniza en la cabeza,",
    (4, 40): "y cayeron rostro en tierra, y tocaron las trompetas de llamada, "
             "y clamaron al Cielo.",
    (4, 41): "Entonces Judas mandó a unos hombres que atacasen a los de la "
             "ciudadela mientras él purificaba el santuario.",
    (4, 42): "Y escogió sacerdotes sin tacha, amantes de la ley;",
    (4, 43): "y purificaron el santuario, y llevaron las piedras de la "
             "profanación a un lugar impuro.",
    (4, 44): "Y deliberaron sobre el altar de los holocaustos, que había sido "
             "profanado, sobre qué hacer con él.",
    (4, 45): "Y les vino una idea acertada: derribarlo, para que no fuera para "
             "ellos una afrenta, porque las naciones lo habían manchado; y "
             "derribaron el altar.",
    (4, 46): "Y pusieron las piedras en el monte del templo, en un sitio "
             "conveniente, hasta que viniera un profeta que respondiese sobre "
             "ellas.",
    (4, 47): "Y tomaron piedras sin labrar, conforme a la ley, y construyeron "
             "un altar nuevo como el anterior.",
    (4, 48): "Y reconstruyeron el santuario y el interior del templo, y "
             "santificaron los atrios.",
    (4, 49): "E hicieron nuevos los utensilios sagrados, y llevaron al templo "
             "el candelabro y el altar de los holocaustos y de los inciensos y "
             "la mesa.",
    (4, 50): "Y quemaron incienso sobre el altar, y encendieron las lámparas "
             "del candelabro, y alumbraron en el templo.",
    (4, 51): "Y pusieron los panes sobre la mesa y colgaron las cortinas; y "
             "acabaron todas las obras que habían emprendido.",
    (4, 52): "Y se levantaron de madrugada el día veinticinco del mes noveno "
             "—que es el mes de Quisleu— del año ciento cuarenta y ocho,",
    (4, 53): "y ofrecieron sacrificio conforme a la ley sobre el altar nuevo "
             "de los holocaustos que habían hecho.",
    (4, 54): "En el mismo tiempo y en el mismo día en que las naciones lo "
             "habían profanado, en ése fue dedicado de nuevo, con cánticos y "
             "cítaras y arpas y címbalos.",
    (4, 55): "Y todo el pueblo cayó rostro en tierra y adoró y bendijo al "
             "Cielo, que los había hecho prosperar.",
    (4, 56): "E hicieron la dedicación del altar durante ocho días, y "
             "ofrecieron holocaustos con alegría, y ofrecieron sacrificios de "
             "salvación y de alabanza.",
    (4, 57): "Y adornaron la fachada del templo con coronas de oro y con "
             "escudos, y restauraron las puertas y las cámaras, y les pusieron "
             "hojas.",
    (4, 58): "Y hubo una alegría grandísima en el pueblo, y se apartó la "
             "afrenta de las naciones.",
    (4, 59): "Y Judas y sus hermanos y toda la asamblea de Israel "
             "establecieron que se celebrasen los días de la dedicación del "
             "altar en su fecha, año tras año, durante ocho días, desde el "
             "veinticinco del mes de Quisleu, con alegría y gozo.",
    (4, 60): "Y en aquel tiempo fortificaron el monte Sión con murallas altas "
             "alrededor y con torres fuertes, para que las naciones no "
             "volvieran a pisotearlo como habían hecho antes.",
    (4, 61): "Y pusieron allí una guarnición para guardarlo; y fortificaron "
             "Betsur para guardarla, de modo que el pueblo tuviera una plaza "
             "fuerte frente a Idumea.",

    (5, 1): "Y sucedió que, cuando las naciones de alrededor oyeron que el "
            "altar había sido reconstruido y el santuario dedicado de nuevo "
            "como antes, se enfurecieron mucho,",
    (5, 2): "y decidieron acabar con los del linaje de Jacob que vivían entre "
            "ellos, y empezaron a matar y a exterminar gente del pueblo.",
    (5, 3): "Y Judas peleó contra los hijos de Esaú en Idumea, en Acrabatene, "
            "porque tenían cercado a Israel; y les asestó un gran golpe y los "
            "sometió y tomó sus despojos.",
    (5, 4): "Y se acordó de la maldad de los hijos de Baián, que eran para el "
            "pueblo un lazo y un tropiezo por sus emboscadas en los caminos.",
    (5, 5): "Y quedaron encerrados por él en las torres, y acampó contra "
            "ellos, y los consagró al exterminio, y prendió fuego a sus torres "
            "con todos los que había dentro.",
    (5, 6): "Y pasó contra los hijos de Amón, y halló una fuerza poderosa y "
            "mucha gente, y a Timoteo como su jefe.",
    (5, 7): "Y trabó con ellos muchos combates, y quedaron destrozados delante "
            "de él, y los derrotó.",
    (5, 8): "Y tomó Jazer y sus aldeas, y se volvió a Judea.",
    (5, 9): "Y se juntaron las naciones de Galaad contra los israelitas que "
            "estaban en sus términos, para acabar con ellos; y ellos huyeron a "
            "la fortaleza de Datema,",
    (5, 10): "y enviaron cartas a Judas y a sus hermanos, diciendo: «Se han "
             "reunido contra nosotros las naciones que nos rodean para acabar "
             "con nosotros,",
    (5, 11): "y se preparan para venir y tomar la fortaleza en la que nos "
             "hemos refugiado; y Timoteo manda su ejército.",
    (5, 12): "Ven, pues, ahora, y líbranos de sus manos, porque han caído "
             "muchos de los nuestros;",
    (5, 13): "y todos nuestros hermanos que estaban en el territorio de Tobías "
             "han sido muertos, y han llevado cautivas a sus mujeres y a sus "
             "hijos y sus bienes, y han hecho perecer allí a unos mil "
             "hombres».",
    (5, 14): "Aún se estaban leyendo aquellas cartas, cuando llegaron otros "
             "mensajeros de Galilea con los vestidos rasgados, anunciando "
             "estas mismas cosas,",
    (5, 15): "diciendo: «Se han juntado contra ellos gentes de Tolemaida y de "
             "Tiro y de Sidón y de toda la Galilea de los extranjeros, para "
             "acabar con nosotros».",
    (5, 16): "Y cuando Judas y el pueblo oyeron estas palabras, se reunió una "
             "gran asamblea para deliberar sobre qué hacer por sus hermanos, "
             "que estaban en aflicción y atacados por aquéllos.",
    (5, 17): "Y dijo Judas a Simón su hermano: «Escógete hombres y ve a librar "
             "a tus hermanos de Galilea; yo y Jonatán mi hermano iremos a "
             "Galaad».",
    (5, 18): "Y dejó a José hijo de Zacarías y a Azarías como jefes del pueblo "
             "con el resto de las tropas en Judea, para guardarla;",
    (5, 19): "y les mandó, diciendo: «Poneos al frente de este pueblo, y no "
             "traféis batalla contra las naciones hasta que volvamos».",
    (5, 20): "Y se asignaron a Simón tres mil hombres para ir a Galilea, y a "
             "Judas ocho mil para Galaad.",
    (5, 21): "Y Simón fue a Galilea y trabó muchos combates contra las "
             "naciones, y las naciones quedaron destrozadas delante de él;",
    (5, 22): "y los persiguió hasta las puertas de Tolemaida; y cayeron de las "
             "naciones unos tres mil hombres, y tomó sus despojos.",
    (5, 23): "Y recogió a los judíos de Galilea y de Arbatas, con sus mujeres "
             "y sus hijos y todo cuanto tenían, y los llevó a Judea con gran "
             "alegría.",
    (5, 24): "Y Judas Macabeo y Jonatán su hermano pasaron el Jordán y "
             "caminaron tres días por el desierto;",
    (5, 25): "y se encontraron con los nabateos, que los recibieron en paz y "
             "les contaron todo lo que había pasado a sus hermanos en "
             "Galaad,",
    (5, 26): "y que muchos de ellos estaban encerrados en Bosorá y en Bosor, "
             "en Alemas, Casfor, Maqued y Carnain: todas ellas ciudades "
             "grandes y fortificadas;",
    (5, 27): "y que también en las demás ciudades de Galaad había gente "
             "encerrada; y que para el día siguiente estaba dispuesto acampar "
             "contra las fortalezas y tomarlas y acabar con todos ellos en un "
             "solo día.",
    (5, 28): "Y Judas y su ejército torcieron de repente camino del desierto "
             "hacia Bosor; y tomó la ciudad y mató a todo varón a filo de "
             "espada, y tomó todos sus despojos y la prendió fuego.",
    (5, 29): "Y partió de allí de noche, y caminaron hasta la fortaleza.",
    (5, 30): "Y al amanecer alzaron los ojos, y he aquí una muchedumbre sin "
             "número que llevaba escalas y máquinas para tomar la fortaleza; y "
             "estaban atacando a los de dentro.",
    (5, 31): "Y vio Judas que la batalla había comenzado, y que el clamor de "
             "la ciudad subía hasta el cielo con trompetas y con gran "
             "griterío;",
    (5, 32): "y dijo a los hombres de su ejército: «Pelead hoy por vuestros "
             "hermanos».",
    (5, 33): "Y salió por detrás de ellos en tres cuerpos; y tocaron las "
             "trompetas y clamaron en oración.",
    (5, 34): "Y el ejército de Timoteo se dio cuenta de que era el Macabeo, y "
             "huyeron delante de él; y les asestó un gran golpe, y cayeron de "
             "ellos aquel día unos ocho mil hombres.",
    (5, 35): "Y se desvió hacia Masfá y la atacó y la tomó, y mató a todos sus "
             "varones y tomó sus despojos y la prendió fuego.",
    (5, 36): "Y partió de allí y tomó Casfón, Maqued, Bosor y las demás "
             "ciudades de Galaad.",
    (5, 37): "Y después de estas cosas Timoteo reunió otro ejército y acampó "
             "frente a Rafón, al otro lado del torrente.",
    (5, 38): "Y Judas envió a reconocer el campamento, y le informaron "
             "diciendo: «Se les han juntado todas las naciones que nos rodean: "
             "un ejército muy numeroso;",
    (5, 39): "y han contratado árabes para que los ayuden, y acampan al otro "
             "lado del torrente, dispuestos a venir contra ti a la batalla». Y "
             "Judas fue a su encuentro.",
    (5, 40): "Y dijo Timoteo a los jefes de su ejército, cuando Judas y su "
             "ejército se acercaban al torrente: «Si él pasa primero hacia "
             "nosotros, no podremos resistirlo, porque sin duda podrá con "
             "nosotros;",
    (5, 41): "pero si se acobarda y acampa al otro lado del río, pasaremos "
             "nosotros contra él».",
    (5, 42): "Y cuando Judas se acercó al torrente, apostó a los escribas del "
             "pueblo junto al torrente y les mandó, diciendo: «No dejéis "
             "acampar a nadie, sino que vengan todos a la batalla».",
    (5, 43): "Y pasó él primero contra ellos, y todo el pueblo detrás de él; y "
             "todas las naciones fueron destrozadas delante de él, y arrojaron "
             "sus armas y huyeron al templo de Carnain.",
    (5, 44): "Y ellos tomaron la ciudad y prendieron fuego al templo con todos "
             "los que había dentro; y Carnain quedó derrotada, y ya no pudo "
             "resistir ante Judas.",
    (5, 45): "Y Judas reunió a todos los israelitas de Galaad, desde el más "
             "pequeño hasta el más grande, con sus mujeres y sus hijos y sus "
             "bienes: una caravana enorme, para ir a la tierra de Judá.",
    (5, 46): "Y llegaron hasta Efrón, que era una ciudad grande a la entrada "
             "del paso, muy fortificada; no había modo de desviarse ni a la "
             "derecha ni a la izquierda, sino que había que pasar por en medio "
             "de ella.",
    (5, 47): "Y los de la ciudad les cerraron el paso y taponaron las puertas "
             "con piedras.",
    (5, 48): "Y Judas les mandó decir con palabras de paz: «Pasaré por tu "
             "tierra para ir a la nuestra, y nadie os hará daño; sólo "
             "pasaremos a pie». Pero no quisieron abrirle.",
    (5, 49): "Y Judas mandó pregonar por el campamento que acampase cada uno "
             "en el sitio en que estaba.",
    (5, 50): "Y acamparon los hombres, y atacaron la ciudad todo aquel día y "
             "toda la noche; y la ciudad fue entregada en sus manos.",
    (5, 51): "Y mató a todo varón a filo de espada, y la arrasó y tomó sus "
             "despojos, y atravesó la ciudad por encima de los muertos.",
    (5, 52): "Y pasaron el Jordán hacia la gran llanura, frente a Betsán.",
    (5, 53): "Y Judas iba reuniendo a los rezagados y animando al pueblo por "
             "todo el camino, hasta que llegaron a la tierra de Judá.",
    (5, 54): "Y subieron al monte Sión con alegría y gozo, y ofrecieron "
             "holocaustos, porque ninguno de ellos había caído hasta volver en "
             "paz.",
    (5, 55): "Y en los días en que Judas y Jonatán estaban en Galaad, y Simón "
             "su hermano en Galilea frente a Tolemaida,",
    (5, 56): "oyeron José hijo de Zacarías y Azarías, jefes de las tropas, las "
             "hazañas y los combates que aquéllos habían hecho,",
    (5, 57): "y dijeron: «Hagámonos también nosotros un nombre, y vayamos a "
             "pelear contra las naciones que nos rodean».",
    (5, 58): "Y dieron orden a los de la tropa que tenían consigo, y marcharon "
             "contra Jamnia.",
    (5, 59): "Y salió Gorgias de la ciudad con sus hombres a su encuentro para "
             "la batalla;",
    (5, 60): "y José y Azarías fueron derrotados, y los persiguieron hasta los "
             "términos de Judea; y cayeron aquel día del pueblo de Israel unos "
             "dos mil hombres.",
    (5, 61): "Y hubo una gran derrota en el pueblo, porque no obedecieron a "
             "Judas y a sus hermanos, creyendo que harían alguna hazaña;",
    (5, 62): "pero ellos no eran del linaje de aquellos hombres por cuya mano "
             "se dio la salvación a Israel.",
    (5, 63): "Y Judas y sus hermanos fueron muy honrados delante de todo "
             "Israel y de todas las naciones donde se oía su nombre;",
    (5, 64): "y se les acercaban a aclamarlos.",
    (5, 65): "Y salió Judas con sus hermanos y pelearon contra los hijos de "
             "Esaú en la tierra del sur, y batió a Hebrón y a sus aldeas; y "
             "derribó su fortaleza y prendió fuego a sus torres alrededor.",
    (5, 66): "Y partió para ir a tierra de extranjeros, y atravesaba "
             "Samaria.",
    (5, 67): "Aquel día cayeron en la batalla unos sacerdotes que querían "
             "hacer alguna hazaña, saliendo a pelear sin consultar.",
    (5, 68): "Y Judas se desvió hacia Azoto, en tierra de extranjeros, y "
             "derribó sus aras y quemó las imágenes talladas de sus dioses, y "
             "saqueó los despojos de las ciudades, y volvió a Judea.",

    (6, 1): "Y el rey Antíoco recorría las provincias de arriba, y oyó que en "
            "Elimaida, en Persia, había una ciudad famosa por su riqueza en "
            "plata y en oro,",
    (6, 2): "y que el templo que había en ella era riquísimo, y que allí había "
            "cubiertas de oro y corazas y armas que había dejado Alejandro "
            "hijo de Filipo, el rey macedonio que reinó primero sobre los "
            "griegos.",
    (6, 3): "Y fue e intentaba tomar la ciudad y saquearla, y no pudo, porque "
            "el plan se supo entre los de la ciudad;",
    (6, 4): "y se levantaron contra él en son de guerra, y huyó y se marchó de "
            "allí con gran tristeza para volver a Babilonia.",
    (6, 5): "Y le vino uno a Persia a anunciarle que habían sido derrotadas "
            "las tropas que habían ido a la tierra de Judá,",
    (6, 6): "y que Lisias había ido con un ejército poderoso al frente, y "
            "había sido puesto en fuga por ellos, y que se habían hecho "
            "fuertes con las armas y las tropas y los muchos despojos que "
            "habían tomado de los ejércitos que habían destrozado;",
    (6, 7): "y que habían derribado la abominación que él había levantado "
            "sobre el altar de Jerusalén, y habían rodeado el santuario de "
            "murallas altas como antes, y también Betsur, ciudad suya.",
    (6, 8): "Y sucedió que, al oír el rey estas noticias, quedó estupefacto y "
            "muy conmovido; y cayó en cama y enfermó de tristeza, porque no "
            "le había salido como pensaba.",
    (6, 9): "Y estuvo allí muchos días, porque le volvía una gran tristeza, y "
            "pensó que se moría.",
    (6, 10): "Y llamó a todos sus amigos y les dijo: «Se me ha ido el sueño de "
             "los ojos, y se me ha desplomado el corazón por la inquietud.",
    (6, 11): "Y me he dicho: ¿A qué aflicción he llegado, y a qué gran "
             "tormenta, en la que ahora estoy? Porque yo era bueno y querido "
             "en mi poder.",
    (6, 12): "Pero ahora me acuerdo de los males que hice en Jerusalén, y de "
             "que me llevé todos los objetos de plata y de oro que en ella "
             "había, y de que mandé exterminar sin motivo a los habitantes de "
             "Judá.",
    (6, 13): "Reconozco que por esto me han sobrevenido estos males; y mira, "
             "muero de una gran tristeza en tierra extraña».",
    (6, 14): "Y llamó a Filipo, uno de sus amigos, y lo puso al frente de todo "
             "su reino;",
    (6, 15): "y le dio la diadema y su manto y el anillo, para que llevase a "
             "Antíoco su hijo y lo criase para que reinase.",
    (6, 16): "Y murió allí el rey Antíoco, el año ciento cuarenta y nueve.",
    (6, 17): "Y supo Lisias que el rey había muerto, y puso a reinar en su "
             "lugar a Antíoco su hijo, al que había criado desde pequeño; y lo "
             "llamó Eupátor.",
    (6, 18): "Y los de la ciudadela tenían cercado a Israel en torno al "
             "santuario, buscándole males de continuo y sirviendo de apoyo a "
             "las naciones.",
    (6, 19): "Y Judas decidió acabar con ellos, y convocó a todo el pueblo "
             "para asediarlos.",
    (6, 20): "Y se reunieron y los asediaron el año ciento cincuenta; e hizo "
             "contra ellos plataformas para las saetas y máquinas.",
    (6, 21): "Y salieron de allí algunos del cerco, y se les unieron unos "
             "impíos de Israel,",
    (6, 22): "y fueron al rey y dijeron: «¿Hasta cuándo no vas a hacer "
             "justicia y a vengar a nuestros hermanos?",
    (6, 23): "Nosotros aceptamos servir a tu padre y andar según sus órdenes y "
             "seguir sus mandatos;",
    (6, 24): "y por eso los de nuestro pueblo se apartaron de nosotros, y a "
             "cuantos de los nuestros encontraban los mataban, y nuestras "
             "heredades eran saqueadas.",
    (6, 25): "Y no sólo contra nosotros han extendido la mano, sino también "
             "contra todos sus términos.",
    (6, 26): "Y mira: hoy han acampado contra la ciudadela de Jerusalén para "
             "tomarla, y han fortificado el santuario y Betsur;",
    (6, 27): "y si no te adelantas a ellos rápidamente, harán cosas mayores "
             "que éstas, y no podrás dominarlos».",
    (6, 28): "Y se enfureció el rey al oírlo; y reunió a todos sus amigos, a "
             "los jefes de su ejército y a los de la caballería;",
    (6, 29): "y de otros reinos y de las islas del mar le llegaron tropas "
             "mercenarias.",
    (6, 30): "Y el número de sus tropas era de cien mil de a pie y veinte mil "
             "de a caballo, y treinta y dos elefantes adiestrados para la "
             "guerra.",
    (6, 31): "Y vinieron por Idumea y acamparon contra Betsur, y la atacaron "
             "muchos días e hicieron máquinas; y los de dentro salieron y las "
             "quemaron, y pelearon como hombres.",
    (6, 32): "Y Judas se retiró de la ciudadela y acampó en Betzacaría, frente "
             "al campamento del rey.",
    (6, 33): "Y el rey se levantó de madrugada y movió el campamento en "
             "formación de ataque por el camino de Betzacaría; y las tropas se "
             "dispusieron para la batalla y tocaron las trompetas.",
    (6, 34): "Y a los elefantes les mostraron zumo de uva y de moras, para "
             "excitarlos al combate.",
    (6, 35): "Y repartieron las fieras por las falanges, y pusieron junto a "
             "cada elefante mil hombres acorazados con cotas de malla y con "
             "cascos de bronce en la cabeza; y quinientos jinetes escogidos "
             "estaban asignados a cada fiera.",
    (6, 36): "Éstos se adelantaban a donde iba a estar la fiera; y adonde ella "
             "iba, iban con ella, y no se apartaban de ella.",
    (6, 37): "Y sobre cada fiera había torres de madera, firmes y cubiertas, "
             "sujetas con arreos; y en cada una iban treinta y dos hombres que "
             "combatían desde allí, además de su conductor indio.",
    (6, 38): "Y el resto de la caballería la apostó a un lado y a otro, en las "
             "dos alas del ejército, para hostigar y para cubrirse tras las "
             "falanges.",
    (6, 39): "Y cuando el sol brilló sobre los escudos de oro, resplandecieron "
             "los montes con ellos, y relucían como antorchas de fuego.",
    (6, 40): "Y una parte del ejército del rey se desplegó por los montes "
             "altos, y otra por la parte baja; y avanzaban con seguridad y en "
             "orden.",
    (6, 41): "Y todos los que oían el estruendo de su multitud y la marcha de "
             "aquella muchedumbre y el entrechocar de las armas temblaban, "
             "porque el ejército era grandísimo y poderoso.",
    (6, 42): "Y Judas se acercó con su ejército a la batalla, y cayeron del "
             "ejército del rey seiscientos hombres.",
    (6, 43): "Y Eleazar, llamado Auarán, vio que una de las fieras estaba "
             "acorazada con corazas reales y sobresalía entre todas las "
             "fieras, y le pareció que en ella iba el rey.",
    (6, 44): "Y se entregó para salvar a su pueblo y para ganarse un nombre "
             "eterno;",
    (6, 45): "y corrió hacia ella con audacia por en medio de la falange, "
             "matando a diestra y a siniestra, y se le abrían a uno y otro "
             "lado.",
    (6, 46): "Y se metió debajo del elefante y lo hirió por abajo y lo mató; y "
             "el elefante cayó a tierra encima de él, y allí murió.",
    (6, 47): "Y los judíos vieron la fuerza del reino y el ímpetu de las "
             "tropas, y se retiraron de ellos.",
    (6, 48): "Y las tropas del rey subieron a su encuentro hacia Jerusalén, y "
             "el rey acampó contra Judea y contra el monte Sión.",
    (6, 49): "E hizo las paces con los de Betsur, que salieron de la ciudad "
             "porque allí no tenían víveres para aguantar el cerco, ya que "
             "aquel año la tierra guardaba el descanso sabático.",
    (6, 50): "Y el rey ocupó Betsur y puso allí una guarnición para "
             "guardarla.",
    (6, 51): "Y acampó contra el santuario muchos días, y montó allí "
             "plataformas para saetas y máquinas y lanzallamas y catapultas de "
             "piedras y escorpiones para disparar saetas y hondas.",
    (6, 52): "Y también ellos hicieron máquinas contra las suyas, y pelearon "
             "muchos días.",
    (6, 53): "Pero no había víveres en el santuario, porque era el año "
             "séptimo, y los que se habían salvado en Judea escapando de las "
             "naciones se habían comido lo que quedaba de las reservas;",
    (6, 54): "y quedaron en el santuario pocos hombres, porque el hambre los "
             "dominó; y se dispersaron cada uno a su lugar.",
    (6, 55): "Y Lisias oyó que Filipo —a quien el rey Antíoco había nombrado "
             "en vida para criar a su hijo Antíoco y hacerlo reinar—",
    (6, 56): "había vuelto de Persia y de Media con las tropas del rey que "
             "habían ido con él, y que pretendía hacerse con el gobierno.",
    (6, 57): "Y se dio prisa y urgió a marcharse; y dijo al rey y a los jefes "
             "del ejército y a los hombres: «Cada día estamos peor, y tenemos "
             "poca comida, y el lugar contra el que acampamos es fuerte, y nos "
             "apremian los asuntos del reino.",
    (6, 58): "Ahora, pues, demos la mano a estos hombres y hagamos la paz con "
             "ellos y con todo su pueblo;",
    (6, 59): "y establezcamos que puedan vivir conforme a sus leyes, como "
             "antes; porque por causa de sus leyes, que nosotros abolimos, se "
             "irritaron e hicieron todo esto».",
    (6, 60): "Y la propuesta agradó al rey y a los jefes, y envió a hacer las "
             "paces con ellos; y ellos aceptaron.",
    (6, 61): "Y el rey y los jefes se lo juraron; y los judíos salieron de la "
             "fortaleza.",
    (6, 62): "Y entró el rey en el monte Sión y vio la fortificación de aquel "
             "lugar, y quebrantó el juramento que había hecho, y mandó "
             "derribar la muralla de alrededor.",
    (6, 63): "Y partió a toda prisa y volvió a Antioquía, y encontró a Filipo "
             "dueño de la ciudad; y peleó contra él y tomó la ciudad por la "
             "fuerza.",

    (7, 1): "El año ciento cincuenta y uno salió Demetrio hijo de Seleuco de "
            "Roma, y subió con unos pocos hombres a una ciudad de la costa, y "
            "empezó a reinar allí.",
    (7, 2): "Y sucedió que, cuando entraba en la casa real de sus padres, las "
            "tropas prendieron a Antíoco y a Lisias para llevárselos.",
    (7, 3): "Y él se enteró y dijo: «No me mostréis sus caras».",
    (7, 4): "Y las tropas los mataron, y Demetrio se sentó en el trono de su "
            "reino.",
    (7, 5): "Y vinieron a él todos los hombres sin ley e impíos de Israel, y "
            "los encabezaba Álcimo, que quería ser sumo sacerdote.",
    (7, 6): "Y acusaron al pueblo ante el rey, diciendo: «Judas y sus hermanos "
            "han hecho perecer a todos tus amigos, y a nosotros nos han "
            "dispersado de nuestra tierra.",
    (7, 7): "Ahora, pues, envía a un hombre de tu confianza, y que vaya y vea "
            "toda la ruina que nos ha causado a nosotros y a la provincia del "
            "rey, y que los castigue a ellos y a todos los que los ayudan».",
    (7, 8): "Y el rey escogió a Báquides, uno de los amigos del rey, que "
            "gobernaba al otro lado del río, grande en el reino y fiel al "
            "rey;",
    (7, 9): "y lo envió con Álcimo el impío, y le confirmó el sumo sacerdocio, "
            "y le mandó tomar venganza de los hijos de Israel.",
    (7, 10): "Y partieron y llegaron con un ejército numeroso a la tierra de "
             "Judá; y envió mensajeros a Judas y a sus hermanos con palabras "
             "de paz, pero con engaño.",
    (7, 11): "Y ellos no hicieron caso de sus palabras, porque vieron que "
             "habían venido con un ejército numeroso.",
    (7, 12): "Y se reunió con Álcimo y con Báquides un grupo de escribas para "
             "pedir lo que era justo;",
    (7, 13): "y los primeros entre los hijos de Israel fueron los asideos, que "
             "les pedían la paz,",
    (7, 14): "porque decían: «Un hombre sacerdote del linaje de Aarón ha "
             "venido con las tropas, y no nos hará daño».",
    (7, 15): "Y él les habló con palabras de paz y les juró diciendo: «No "
             "buscaremos haceros daño ni a vosotros ni a vuestros amigos».",
    (7, 16): "Y ellos le creyeron; y él prendió a sesenta de ellos y los mató "
             "en un solo día, conforme a lo que está escrito:",
    (7, 17): "«Las carnes de tus santos y su sangre las derramaron alrededor "
             "de Jerusalén, y no había quien los enterrase».",
    (7, 18): "Y cayó sobre todo el pueblo el miedo y el temblor de ellos, "
             "porque decían: «No hay en ellos verdad ni justicia; pues han "
             "traspasado el acuerdo y el juramento que habían jurado».",
    (7, 19): "Y Báquides partió de Jerusalén y acampó en Bezet; y mandó "
             "prender a muchos de los hombres que se le habían pasado y a "
             "algunos del pueblo, y los degolló y los echó en el pozo "
             "grande.",
    (7, 20): "Y entregó la provincia a Álcimo, y le dejó tropas para que lo "
             "ayudasen; y Báquides se volvió al rey.",
    (7, 21): "Y Álcimo peleó por el sumo sacerdocio;",
    (7, 22): "y se le juntaron todos los que perturbaban a su pueblo, y se "
             "apoderaron de la tierra de Judá, e hicieron un gran estrago en "
             "Israel.",
    (7, 23): "Y vio Judas todo el mal que Álcimo y los suyos habían hecho a "
             "los hijos de Israel, más que las naciones;",
    (7, 24): "y salió por todos los términos de Judea y por los alrededores, e "
             "hizo justicia con los tránsfugas, y éstos dejaron de recorrer la "
             "región.",
    (7, 25): "Y cuando Álcimo vio que Judas y los suyos se habían hecho "
             "fuertes, y comprendió que no podía resistirlos, volvió al rey y "
             "los acusó de maldades.",
    (7, 26): "Y el rey envió a Nicanor, uno de sus jefes más ilustres, que "
             "odiaba y era enemigo de Israel, y le mandó acabar con el "
             "pueblo.",
    (7, 27): "Y llegó Nicanor a Jerusalén con un gran ejército, y envió a "
             "decir a Judas y a sus hermanos, con engaño, palabras de paz:",
    (7, 28): "«Que no haya pelea entre vosotros y yo; iré con unos pocos "
             "hombres para veros las caras en paz».",
    (7, 29): "Y fue a Judas, y se saludaron amistosamente; pero los enemigos "
             "estaban preparados para llevarse a Judas por la fuerza.",
    (7, 30): "Y Judas se enteró de que había venido contra él con engaño, y se "
             "asustó de él y ya no quiso verle la cara.",
    (7, 31): "Y comprendió Nicanor que su plan había quedado al descubierto, y "
             "salió al encuentro de Judas junto a Cafarsalamá.",
    (7, 32): "Y cayeron de los de Nicanor unos cinco mil hombres, y huyeron a "
             "la ciudad de David.",
    (7, 33): "Y después de esto subió Nicanor al monte Sión; y salieron "
             "algunos de los sacerdotes del santuario y de los ancianos del "
             "pueblo a saludarlo amistosamente y a mostrarle el holocausto que "
             "se ofrecía por el rey.",
    (7, 34): "Y él se burló de ellos y se rió y los manchó, y habló con "
             "soberbia;",
    (7, 35): "y juró con furor diciendo: «Si no se me entrega ahora Judas con "
             "su ejército en mis manos, cuando vuelva sano y salvo quemaré "
             "esta casa». Y salió furioso.",
    (7, 36): "Y entraron los sacerdotes y se pusieron delante del altar y del "
             "templo, y lloraron y dijeron:",
    (7, 37): "«Tú escogiste esta casa para que fuera invocado sobre ella tu "
             "nombre, para que fuera casa de oración y de súplica para tu "
             "pueblo.",
    (7, 38): "Haz justicia con este hombre y con su ejército, y caigan a "
             "espada; acuérdate de sus blasfemias y no les des tregua».",
    (7, 39): "Y salió Nicanor de Jerusalén y acampó en Bet-Horón, y allí se le "
             "unió un ejército de Siria.",
    (7, 40): "Y Judas acampó en Adasá con tres mil hombres; y oró Judas y "
             "dijo:",
    (7, 41): "«Cuando los enviados del rey blasfemaron, salió tu ángel y mató "
             "a ciento ochenta y cinco mil de ellos.",
    (7, 42): "Destroza así hoy este ejército delante de nosotros; y sepan los "
             "que queden que él habló mal contra tu santuario, y júzgalo "
             "conforme a su maldad».",
    (7, 43): "Y los ejércitos vinieron a las manos el día trece del mes de "
             "Adar, y el ejército de Nicanor fue destrozado; y él fue el "
             "primero en caer en la batalla.",
    (7, 44): "Y cuando su ejército vio que Nicanor había caído, arrojaron las "
             "armas y huyeron.",
    (7, 45): "Y los persiguieron una jornada de camino, desde Adasá hasta "
             "llegar a Gázara, y tocaban tras ellos las trompetas de aviso;",
    (7, 46): "y salieron de todas las aldeas de Judea de alrededor y los "
             "envolvieron por los flancos; y aquéllos se volvían contra "
             "éstos, y cayeron todos a espada, y no quedó de ellos ni uno "
             "solo.",
    (7, 47): "Y tomaron los despojos y el botín, y le cortaron a Nicanor la "
             "cabeza y la mano derecha, que él había extendido con soberbia; y "
             "las trajeron y las expusieron a la vista de Jerusalén.",
    (7, 48): "Y el pueblo se alegró muchísimo, y celebraron aquel día como un "
             "gran día de fiesta.",
    (7, 49): "Y establecieron celebrar aquel día cada año, el trece de Adar.",
    (7, 50): "Y la tierra de Judá estuvo tranquila unos pocos días.",

    (8, 1): "Y oyó Judas hablar de los romanos: que eran poderosos en fuerza y "
            "que se mostraban favorables con todos los que se les unían, y que "
            "a cuantos se les agregaban y a cuantos acudían a ellos les "
            "otorgaban su amistad;",
    (8, 2): "y que eran poderosos en fuerza. Y le contaron sus guerras y las "
            "hazañas que hacían entre los gálatas, y cómo los habían dominado "
            "y sometido a tributo;",
    (8, 3): "y cuánto habían hecho en la región de España para apoderarse de "
            "las minas de plata y de oro que hay allí,",
    (8, 4): "y cómo se apoderaron de toda aquella región con su prudencia y su "
            "constancia —y aquel lugar estaba lejísimos de ellos—, y de los "
            "reyes que habían venido contra ellos desde el extremo de la "
            "tierra, hasta que los destrozaron y les asestaron un gran golpe; "
            "y los que quedaron les pagan tributo cada año.",
    (8, 5): "Y a Filipo y a Perseo, rey de los quitieos, y a los que se "
            "levantaron contra ellos, los destrozaron en la guerra y los "
            "dominaron.",
    (8, 6): "Y a Antíoco el grande, rey de Asia, que fue contra ellos a la "
            "guerra con ciento veinte elefantes y caballería y carros y un "
            "ejército numerosísimo, también lo destrozaron;",
    (8, 7): "y lo tomaron vivo, y le impusieron que él y los que reinasen "
            "después de él pagasen un gran tributo, y que entregasen rehenes y "
            "cedieran territorio:",
    (8, 8): "la región de la India y la de Media y la de Lidia, de entre sus "
            "mejores provincias; y tomándolas de él, se las dieron al rey "
            "Eumenes.",
    (8, 9): "Y cómo los de Grecia decidieron ir a acabar con ellos,",
    (8, 10): "y ellos se enteraron del plan, y enviaron contra ellos a un solo "
             "general, y pelearon contra ellos, y cayeron de ellos muchos "
             "heridos, y llevaron cautivas a sus mujeres y a sus hijos, y los "
             "saquearon y se apoderaron de su tierra, y derribaron sus "
             "fortalezas, y los sometieron y los tienen esclavizados hasta el "
             "día de hoy.",
    (8, 11): "Y a los demás reinos y a las islas, a cuantos alguna vez se les "
             "enfrentaron, los destruyeron y los esclavizaron;",
    (8, 12): "pero con sus amigos y con los que se apoyan en ellos mantuvieron "
             "la amistad. Y dominaron los reinos cercanos y los lejanos; y "
             "cuantos oían su nombre les tenían miedo.",
    (8, 13): "Y a quienes ellos quieren ayudar y hacer reinar, reinan; y a "
             "quienes quieren, los deponen; y se han encumbrado muchísimo.",
    (8, 14): "Y con todo esto, ninguno de ellos se ha ceñido la diadema ni se "
             "ha vestido de púrpura para engrandecerse con ella.",
    (8, 15): "Y se han hecho una sala de consejo, y cada día deliberan "
             "trescientos veinte, tratando siempre de los asuntos del pueblo "
             "para que esté bien gobernado.",
    (8, 16): "Y confían a un solo hombre el mando sobre ellos cada año, y el "
             "gobierno de toda su tierra; y todos obedecen a ése, y no hay "
             "envidia ni rivalidad entre ellos.",
    (8, 17): "Y Judas escogió a Eupólemo hijo de Juan, hijo de Acós, y a Jasón "
             "hijo de Eleazar, y los envió a Roma para concertar con ellos "
             "amistad y alianza,",
    (8, 18): "y para que les quitasen el yugo, porque veían que el reino de "
             "los griegos tenía sometido a Israel en esclavitud.",
    (8, 19): "Y fueron a Roma —y el camino era larguísimo—, y entraron en la "
             "sala del consejo y hablaron así:",
    (8, 20): "«Judas, llamado Macabeo, y sus hermanos y el pueblo de los "
             "judíos nos han enviado a vosotros para concertar con vosotros "
             "alianza y paz, y para que nos inscribáis como aliados y amigos "
             "vuestros».",
    (8, 21): "Y la propuesta les pareció bien.",
    (8, 22): "Y ésta es la copia del escrito que grabaron en tablas de bronce "
             "y enviaron a Jerusalén, para que allí quedara entre ellos como "
             "memoria de la paz y de la alianza:",
    (8, 23): "«Que les vaya bien a los romanos y al pueblo de los judíos en el "
             "mar y en la tierra para siempre; y que la espada y el enemigo "
             "estén lejos de ellos.",
    (8, 24): "Y si sobreviene guerra primero a Roma, o a cualquiera de sus "
             "aliados en todo su dominio,",
    (8, 25): "el pueblo de los judíos peleará a su lado, según lo pida la "
             "ocasión, de todo corazón;",
    (8, 26): "y a los que les hagan la guerra no les darán ni les "
             "suministrarán trigo, armas, dinero ni naves, conforme a lo "
             "decidido por Roma; y guardarán sus compromisos sin recibir "
             "nada.",
    (8, 27): "Y del mismo modo, si al pueblo de los judíos le sobreviene "
             "guerra primero, los romanos pelearán a su lado de buena gana, "
             "según lo pida la ocasión;",
    (8, 28): "y a los que peleen contra ellos no se les dará trigo, armas ni "
             "dinero, conforme a lo decidido por Roma; y guardarán estos "
             "compromisos, y sin engaño.",
    (8, 29): "Conforme a estas palabras establecieron los romanos el pacto con "
             "el pueblo de los judíos.",
    (8, 30): "Y si después de estas palabras unos y otros deciden añadir o "
             "quitar algo, lo harán conforme a su decisión; y lo que añadan o "
             "quiten tendrá validez.",
    (8, 31): "Y acerca de los males que el rey Demetrio les hace, le hemos "
             "escrito diciendo: “¿Por qué has hecho pesado tu yugo sobre "
             "nuestros amigos y aliados los judíos?",
    (8, 32): "Si vuelven a acudir a nosotros contra ti, les haremos justicia y "
             "te haremos la guerra por mar y por tierra”».",

    (9, 1): "Y oyó Demetrio que Nicanor y su ejército habían caído en la "
            "batalla, y volvió a enviar a Báquides y a Álcimo por segunda vez "
            "a la tierra de Judá, y con ellos el ala derecha del ejército.",
    (9, 2): "Y fueron por el camino de Gálgala y acamparon contra Mesalot, que "
            "está en Arbela, y la tomaron, e hicieron perecer a mucha gente.",
    (9, 3): "Y el mes primero del año ciento cincuenta y dos acamparon contra "
            "Jerusalén.",
    (9, 4): "Y partieron y fueron a Berea con veinte mil hombres y dos mil "
            "jinetes.",
    (9, 5): "Y Judas estaba acampado en Elasá, y con él tres mil hombres "
            "escogidos.",
    (9, 6): "Y vieron el gran número de aquellas tropas, y tuvieron mucho "
            "miedo; y muchos se escabulleron del campamento, y no quedaron de "
            "ellos más que ochocientos hombres.",
    (9, 7): "Y vio Judas que su ejército se le había escurrido y que la "
            "batalla lo apremiaba; y se le rompió el corazón, porque no tenía "
            "tiempo de reunirlos.",
    (9, 8): "Y, desfallecido, dijo a los que quedaban: «Levantémonos y subamos "
            "contra nuestros adversarios, por si acaso podemos pelear contra "
            "ellos».",
    (9, 9): "Y ellos intentaban disuadirlo, diciendo: «No podremos; salvemos "
            "por ahora nuestras vidas y volvamos con nuestros hermanos, y "
            "entonces pelearemos contra ellos; porque somos pocos».",
    (9, 10): "Y dijo Judas: «Lejos de mí hacer tal cosa, huir de ellos. Y si "
             "ha llegado nuestra hora, muramos con hombría por nuestros "
             "hermanos, y no dejemos mancha en nuestra gloria».",
    (9, 11): "Y el ejército salió del campamento y se pusieron frente a ellos; "
             "y la caballería se dividió en dos cuerpos, y los honderos y los "
             "arqueros iban delante del ejército, y todos los valientes en "
             "primera línea.",
    (9, 12): "Y Báquides estaba en el ala derecha; y la falange se acercó por "
             "los dos lados, y tocaban las trompetas; y también los de Judas "
             "tocaron las trompetas.",
    (9, 13): "Y tembló la tierra con el estruendo de los ejércitos; y el "
             "combate se trabó desde la mañana hasta la tarde.",
    (9, 14): "Y vio Judas que Báquides y el grueso del ejército estaban a la "
             "derecha, y se le juntaron todos los de corazón esforzado;",
    (9, 15): "y el ala derecha quedó destrozada por ellos, y los persiguió "
             "hasta el monte de Azoto.",
    (9, 16): "Y los del ala izquierda vieron que el ala derecha había sido "
             "destrozada, y se volvieron pisando los talones a Judas y a los "
             "suyos, por detrás.",
    (9, 17): "Y la batalla se hizo dura, y cayeron muchos heridos de una parte "
             "y de otra.",
    (9, 18): "Y Judas cayó, y los demás huyeron.",
    (9, 19): "Y Jonatán y Simón tomaron a Judas su hermano y lo sepultaron en "
             "el sepulcro de sus padres, en Modín.",
    (9, 20): "Y lo lloraron allí, y todo Israel hizo por él gran duelo, e "
             "hicieron luto muchos días y dijeron:",
    (9, 21): "«¡Cómo ha caído el valiente, el que salvaba a Israel!».",
    (9, 22): "Y el resto de los hechos de Judas, y de sus guerras y de las "
             "hazañas que hizo, y de su grandeza, no se ha escrito, porque "
             "eran muchísimas.",
    (9, 23): "Y sucedió que, después de la muerte de Judas, asomaron los sin "
             "ley por todos los términos de Israel, y brotaron todos los "
             "obreros de la injusticia.",
    (9, 24): "En aquellos días hubo una gran hambre, y la región se pasó a "
             "ellos. Y Báquides escogió a los hombres impíos y los puso como "
             "señores del país;",
    (9, 25): "y buscaban y rastreaban a los amigos de Judas, y los llevaban a "
             "Báquides; y él se vengaba de ellos y se burlaba de ellos.",
    (9, 26): "Y hubo en Israel una aflicción tan grande como no la había "
             "habido desde el día en que dejó de aparecérseles un profeta.",
    (9, 28): "Y se reunieron todos los amigos de Judas y dijeron a Jonatán:",
    (9, 29): "«Desde que tu hermano Judas murió, no hay un hombre como él para "
             "salir contra los enemigos y contra Báquides y contra los que "
             "aborrecen a nuestro pueblo.",
    (9, 30): "Así que hoy te hemos elegido a ti para que estés en su lugar "
             "como nuestro jefe y caudillo, para pelear nuestra guerra».",
    (9, 31): "Y Jonatán tomó en aquel tiempo el mando, y se puso en lugar de "
             "Judas su hermano.",
    (9, 32): "Y lo supo Báquides, y buscaba matarlo.",
    (9, 33): "Y lo supieron Jonatán y Simón su hermano y todos los suyos, y "
             "huyeron al desierto de Tecoa y acamparon junto al agua de la "
             "cisterna de Asfar.",
    (9, 34): "Y Báquides se enteró en día de sábado, y vino él con todo su "
             "ejército al otro lado del Jordán.",
    (9, 35): "Y Jonatán envió a su hermano como jefe de la gente, y rogó a sus "
             "amigos los nabateos que les guardasen su mucha impedimenta.",
    (9, 36): "Pero salieron los hijos de Jambrí de Medabá y prendieron a Juan "
             "con todo lo que llevaba, y se marcharon con ello.",
    (9, 37): "Y después de esto le comunicaron a Jonatán y a Simón su hermano "
             "que los hijos de Jambrí celebraban una gran boda, y que llevaban "
             "a la novia desde Nadabat —hija de uno de los grandes magnates de "
             "Canaán— con gran acompañamiento.",
    (9, 38): "Y se acordaron de Juan su hermano, y subieron y se escondieron "
             "al abrigo del monte.",
    (9, 39): "Y alzaron los ojos y miraron, y he aquí un alboroto y mucha "
             "impedimenta; y el novio salió con sus amigos y sus hermanos a su "
             "encuentro con panderos y músicos y muchas armas.",
    (9, 40): "Y se lanzaron sobre ellos desde la emboscada y los mataron; y "
             "cayeron muchos heridos, y los demás huyeron al monte, y ellos se "
             "llevaron todos sus bienes.",
    (9, 41): "Y la boda se volvió duelo, y la música de sus instrumentos, "
             "lamento.",
    (9, 42): "Y vengaron la sangre de su hermano, y se volvieron a los "
             "carrizales del Jordán.",
    (9, 43): "Y lo oyó Báquides, y vino en día de sábado hasta las riberas del "
             "Jordán con un gran ejército.",
    (9, 44): "Y dijo Jonatán a los suyos: «Levantémonos ahora y peleemos por "
             "nuestras vidas, porque hoy no es como ayer ni como anteayer.",
    (9, 45): "Porque mirad: tenemos la batalla delante y detrás; y el agua del "
             "Jordán a un lado y a otro, y pantano y bosque; y no hay sitio "
             "por donde escapar.",
    (9, 46): "Ahora, pues, clamad al Cielo para que seáis librados de la mano "
             "de nuestros enemigos».",
    (9, 47): "Y se trabó la batalla; y Jonatán extendió la mano para herir a "
             "Báquides, y éste se le escurrió hacia atrás.",
    (9, 48): "Y Jonatán y los suyos se lanzaron al Jordán y pasaron a nado a "
             "la otra orilla; y aquéllos no pasaron el Jordán tras ellos.",
    (9, 49): "Y cayeron aquel día de los de Báquides unos mil hombres.",
    (9, 50): "Y volvió a Jerusalén y fortificó ciudades en Judea: la fortaleza "
             "de Jericó, y Emaús y Bet-Horón y Betel y Tamnata Faratón y "
             "Tefón, con murallas altas y puertas y cerrojos;",
    (9, 51): "y puso en ellas guarniciones para hostigar a Israel.",
    (9, 52): "Y fortificó la ciudad de Betsur y Gázara y la ciudadela, y puso "
             "en ellas tropas y reservas de víveres.",
    (9, 53): "Y tomó como rehenes a los hijos de los principales del país, y "
             "los puso bajo custodia en la ciudadela de Jerusalén.",
    (9, 54): "Y el año ciento cincuenta y tres, en el mes segundo, mandó "
             "Álcimo derribar el muro del atrio interior del santuario; y "
             "derribó las obras de los profetas, y empezó a demoler.",
    (9, 55): "En aquel momento Álcimo sufrió un ataque, y sus obras quedaron "
             "detenidas; y se le trabó la boca y quedó paralítico, y ya no "
             "pudo decir palabra ni dar instrucciones sobre su casa.",
    (9, 56): "Y murió Álcimo en aquel momento con grandes tormentos.",
    (9, 57): "Y vio Báquides que Álcimo había muerto, y se volvió al rey; y la "
             "tierra de Judá estuvo tranquila dos años.",
    (9, 58): "Y todos los sin ley tomaron esta decisión, diciendo: «Mirad, "
             "Jonatán y los suyos viven tranquilos y confiados; traigamos, "
             "pues, a Báquides, y los prenderá a todos en una sola noche».",
    (9, 59): "Y fueron y se lo aconsejaron.",
    (9, 60): "Y él partió para venir con un gran ejército, y envió cartas en "
             "secreto a todos sus aliados de Judea para que prendiesen a "
             "Jonatán y a los suyos; pero no pudieron, porque el plan se supo.",
    (9, 61): "Y prendieron a unos cincuenta hombres del país, cabecillas de "
             "aquella maldad, y los mataron.",
    (9, 62): "Y Jonatán y Simón y los suyos se retiraron a Betbasí, en el "
             "desierto, y reconstruyeron lo que estaba derruido y la "
             "fortificaron.",
    (9, 63): "Y lo supo Báquides y reunió a toda su gente, y dio aviso a los "
             "de Judea.",
    (9, 64): "Y vino y acampó contra Betbasí, y la atacó muchos días e hizo "
             "máquinas.",
    (9, 65): "Y Jonatán dejó a Simón su hermano en la ciudad, y salió al "
             "campo, y fue con unos pocos.",
    (9, 66): "E hirió a Odomera y a sus hermanos y a los hijos de Fasirón en "
             "sus tiendas, y empezó a golpear y a subir con sus tropas.",
    (9, 67): "Y Simón y los suyos salieron de la ciudad y quemaron las "
             "máquinas.",
    (9, 68): "Y pelearon contra Báquides, y quedó destrozado por ellos; y lo "
             "apretaron mucho, porque su plan y su expedición habían resultado "
             "vanos.",
    (9, 69): "Y se enfureció contra los hombres sin ley que le habían "
             "aconsejado venir al país, y mató a muchos de ellos; y decidió "
             "volverse a su tierra.",
    (9, 70): "Y lo supo Jonatán, y le envió embajadores para concertar la paz "
             "con él y para que les devolviese a los cautivos.",
    (9, 71): "Y él aceptó e hizo conforme a sus palabras, y le juró no "
             "buscarle mal en todos los días de su vida.",
    (9, 72): "Y le devolvió los cautivos que antes había hecho en la tierra de "
             "Judá; y dando media vuelta, se fue a su tierra, y no volvió a "
             "venir a sus términos.",
    (9, 73): "Y cesó la espada en Israel; y Jonatán se estableció en Macmás. Y "
             "empezó Jonatán a juzgar al pueblo, e hizo desaparecer a los "
             "impíos de Israel.",

    (10, 1): "Y el año ciento sesenta subió Alejandro, hijo de Antíoco "
             "Epífanes, y tomó Tolemaida; y lo recibieron y reinó allí.",
    (10, 2): "Y lo oyó el rey Demetrio, y reunió tropas numerosísimas y salió "
             "a su encuentro para la guerra.",
    (10, 3): "Y Demetrio envió cartas a Jonatán con palabras de paz, para "
             "honrarlo;",
    (10, 4): "porque dijo: «Adelantémonos a hacer la paz con ellos, antes de "
             "que él la haga con Alejandro contra nosotros;",
    (10, 5): "porque se acordará de todos los males que le hemos causado a él "
             "y a sus hermanos y a su pueblo».",
    (10, 6): "Y le dio autoridad para reunir tropas y para fabricar armas, y "
             "para ser aliado suyo; y mandó que le entregasen los rehenes que "
             "estaban en la ciudadela.",
    (10, 7): "Y Jonatán vino a Jerusalén y leyó las cartas a oídos de todo el "
             "pueblo y de los de la ciudadela;",
    (10, 8): "y tuvieron mucho miedo cuando oyeron que el rey le había dado "
             "autoridad para reunir tropas.",
    (10, 9): "Y los de la ciudadela entregaron a Jonatán los rehenes, y él se "
             "los devolvió a sus padres.",
    (10, 10): "Y Jonatán se estableció en Jerusalén, y empezó a reconstruir y "
              "a renovar la ciudad.",
    (10, 11): "Y dijo a los que hacían las obras que edificasen las murallas y "
              "el monte Sión alrededor con piedras cuadradas para "
              "fortificarlo; y así lo hicieron.",
    (10, 12): "Y huyeron los extranjeros que estaban en las fortalezas que "
              "había construido Báquides;",
    (10, 13): "y cada uno dejó su puesto y se marchó a su tierra.",
    (10, 14): "Sólo en Betsur quedaron algunos de los que habían abandonado la "
              "ley y los mandamientos, porque aquello era para ellos un "
              "refugio.",
    (10, 15): "Y el rey Alejandro oyó las promesas que Demetrio había enviado "
              "a Jonatán, y le contaron las guerras y las hazañas que él y sus "
              "hermanos habían hecho, y las fatigas que habían pasado;",
    (10, 16): "y dijo: «¿Encontraremos otro hombre como éste? Hagámoslo ahora "
              "amigo y aliado nuestro».",
    (10, 17): "Y escribió cartas y se las envió, en estos términos:",
    (10, 18): "«El rey Alejandro a su hermano Jonatán, salud.",
    (10, 19): "Hemos oído de ti que eres hombre valiente y adecuado para ser "
              "amigo nuestro.",
    (10, 20): "Y ahora te nombramos hoy sumo sacerdote de tu nación, y que se "
              "te llame amigo del rey —y le envió una púrpura y una corona de "
              "oro—, y que seas de los nuestros y nos guardes amistad».",
    (10, 21): "Y Jonatán se vistió la vestidura sagrada el mes séptimo del año "
              "ciento sesenta, en la fiesta de las tiendas; y reunió tropas y "
              "fabricó muchas armas.",
    (10, 22): "Y Demetrio oyó estas noticias y se entristeció, y dijo:",
    (10, 23): "«¿Qué hemos hecho, que Alejandro se nos ha adelantado en "
              "ganarse la amistad de los judíos para reforzarse?",
    (10, 24): "También yo les escribiré palabras de aliento y de honra y de "
              "regalos, para que estén conmigo y me ayuden».",
    (10, 25): "Y les envió este escrito: «El rey Demetrio al pueblo de los "
              "judíos, salud.",
    (10, 26): "Puesto que habéis guardado los pactos con nosotros y os habéis "
              "mantenido en nuestra amistad, y no os habéis pasado a nuestros "
              "enemigos, lo hemos oído y nos hemos alegrado.",
    (10, 27): "Y ahora, seguid guardándonos fidelidad, y os pagaremos con "
              "bienes lo que hacéis con nosotros;",
    (10, 28): "y os concederemos muchas exenciones y os haremos donativos.",
    (10, 29): "Y ahora os libero y eximo a todos los judíos de los tributos y "
              "del impuesto de la sal y de las coronas;",
    (10, 30): "y en lugar del tercio de la cosecha y de la mitad del fruto de "
              "los árboles que me corresponde recibir, lo dejo desde hoy en "
              "adelante, de modo que no se recaude en la tierra de Judá ni en "
              "los tres distritos que se le agregan de Samaria y de Galilea, "
              "desde el día de hoy y para siempre.",
    (10, 31): "Y sea Jerusalén santa y exenta, ella y sus términos, en los "
              "diezmos y en los impuestos.",
    (10, 32): "Renuncio también a la autoridad sobre la ciudadela de "
              "Jerusalén, y se la doy al sumo sacerdote, para que ponga en "
              "ella los hombres que él escoja para guardarla.",
    (10, 33): "Y a toda persona judía llevada cautiva desde la tierra de Judá "
              "a cualquier parte de mi reino, la dejo libre sin rescate; y "
              "todos queden exentos de los tributos, también los de sus "
              "ganados.",
    (10, 34): "Y todas las fiestas y los sábados y las lunas nuevas y los días "
              "señalados, y los tres días antes de una fiesta y los tres días "
              "después, sean todos días de franquicia y de exención para todos "
              "los judíos que hay en mi reino;",
    (10, 35): "y nadie tenga autoridad para exigirles nada ni para molestar a "
              "ninguno de ellos por asunto alguno.",
    (10, 36): "Y alístense de los judíos en las tropas del rey hasta treinta "
              "mil hombres, y se les dará la paga como corresponde a todas las "
              "tropas del rey.",
    (10, 37): "Y se destinarán algunos de ellos a las grandes fortalezas del "
              "rey, y de entre éstos se pondrán algunos en los puestos de "
              "confianza del reino; y sus oficiales y sus jefes serán de entre "
              "ellos, y vivirán conforme a sus leyes, como el rey ha mandado "
              "en la tierra de Judá.",
    (10, 38): "Y los tres distritos agregados a Judea de la región de Samaria, "
              "agréguense a Judea, de modo que se consideren bajo uno solo y "
              "no obedezcan a otra autoridad que a la del sumo sacerdote.",
    (10, 39): "Tolemaida y su territorio los doy como donativo al santuario de "
              "Jerusalén, para los gastos que corresponden al santuario.",
    (10, 40): "Y yo doy cada año quince mil siclos de plata de las rentas "
              "reales, de los lugares que corresponden.",
    (10, 41): "Y todo lo que sobre, que los administradores no entregaron como "
              "en los primeros años, désele desde ahora para las obras de la "
              "Casa.",
    (10, 42): "Y además de esto, los cinco mil siclos de plata que se "
              "recaudaban de las rentas del santuario cada año, también se "
              "condonan, porque corresponden a los sacerdotes que ofician.",
    (10, 43): "Y cuantos se refugien en el templo de Jerusalén y en todos sus "
              "términos, debiendo algo al fisco o por cualquier otro asunto, "
              "queden libres, con todo lo que tengan en mi reino.",
    (10, 44): "Y para reconstruir y renovar las obras del santuario, el gasto "
              "se dará de las rentas del rey.",
    (10, 45): "Y para reconstruir las murallas de Jerusalén y fortificarla "
              "alrededor, el gasto se dará de las rentas del rey; y también "
              "para reconstruir las murallas en Judea».",
    (10, 46): "Y cuando Jonatán y el pueblo oyeron estas palabras, no las "
              "creyeron ni las aceptaron, porque se acordaban del gran mal que "
              "él había hecho en Israel y de cuánto los había afligido.",
    (10, 47): "Y se inclinaron por Alejandro, porque él había sido el primero "
              "en proponerles palabras de paz; y fueron sus aliados todos los "
              "días.",
    (10, 48): "Y el rey Alejandro reunió grandes tropas y acampó frente a "
              "Demetrio.",
    (10, 49): "Y los dos reyes trabaron batalla, y el ejército de Demetrio "
              "huyó; y Alejandro lo persiguió y pudo con ellos.",
    (10, 50): "Y sostuvo la batalla con dureza hasta que se puso el sol; y "
              "Demetrio cayó aquel día.",
    (10, 51): "Y Alejandro envió a Tolomeo, rey de Egipto, embajadores con "
              "este mensaje:",
    (10, 52): "«Puesto que he vuelto a mi reino y me he sentado en el trono de "
              "mis padres y me he hecho con el poder, y he destrozado a "
              "Demetrio y me he adueñado de nuestra tierra",
    (10, 53): "—pues trabé batalla con él, y él y su ejército fueron "
              "destrozados por nosotros, y nos hemos sentado en el trono de su "
              "reino—,",
    (10, 54): "establezcamos ahora amistad entre nosotros; y dame a tu hija "
              "por mujer, y seré tu yerno, y te daré a ti y a ella regalos "
              "dignos de ti».",
    (10, 55): "Y el rey Tolomeo respondió diciendo: «Feliz el día en que "
              "volviste a la tierra de tus padres y te sentaste en el trono de "
              "su reino.",
    (10, 56): "Y ahora haré contigo lo que has escrito; pero ven a mi "
              "encuentro a Tolemaida, para que nos veamos, y seré tu suegro "
              "como has dicho».",
    (10, 57): "Y Tolomeo salió de Egipto con Cleopatra su hija, y llegó a "
              "Tolemaida el año ciento sesenta y dos.",
    (10, 58): "Y el rey Alejandro salió a su encuentro, y él le entregó a "
              "Cleopatra su hija; y celebró su boda en Tolemaida, como los "
              "reyes, con gran esplendor.",
    (10, 59): "Y el rey Alejandro escribió a Jonatán que fuese a su "
              "encuentro.",
    (10, 60): "Y él fue con esplendor a Tolemaida y se encontró con los dos "
              "reyes; y les dio plata y oro, y a sus amigos, y muchos regalos, "
              "y halló gracia delante de ellos.",
    (10, 61): "Y se juntaron contra él unos hombres pestilentes de Israel, "
              "hombres sin ley, para acusarlo; pero el rey no les hizo caso.",
    (10, 62): "Y el rey mandó que quitasen a Jonatán sus vestidos y lo "
              "vistiesen de púrpura; y así lo hicieron.",
    (10, 63): "Y el rey lo sentó junto a sí, y dijo a sus jefes: «Salid con él "
              "por el centro de la ciudad y pregonad que nadie lo acuse por "
              "asunto alguno, y que nadie lo moleste por ninguna causa».",
    (10, 64): "Y sucedió que, cuando los acusadores vieron su honra según el "
              "pregón, y que iba vestido de púrpura, huyeron todos.",
    (10, 65): "Y el rey lo honró y lo inscribió entre sus primeros amigos, y "
              "lo hizo general y gobernador de distrito.",
    (10, 66): "Y Jonatán volvió a Jerusalén en paz y con alegría.",
    (10, 67): "Y el año ciento sesenta y cinco vino Demetrio, hijo de "
              "Demetrio, de Creta a la tierra de sus padres.",
    (10, 68): "Y lo oyó el rey Alejandro y se entristeció mucho, y se volvió a "
              "Antioquía.",
    (10, 69): "Y Demetrio nombró a Apolonio gobernador de Celesiria; y éste "
              "reunió un gran ejército y acampó en Jamnia, y envió a decir a "
              "Jonatán el sumo sacerdote:",
    (10, 70): "«Tú eres el único que se levanta contra nosotros, y yo he "
              "quedado en ridículo y en oprobio por tu causa; ¿y por qué "
              "ejerces el mando contra nosotros en los montes?",
    (10, 71): "Ahora, pues, si confías en tus fuerzas, baja a nosotros a la "
              "llanura y midámonos allí, porque conmigo está la fuerza de las "
              "ciudades.",
    (10, 72): "Pregunta y entérate de quién soy yo y quiénes son los que nos "
              "ayudan; y dicen: “No podéis hacernos frente, porque tus padres "
              "fueron puestos en fuga dos veces en su propia tierra”.",
    (10, 73): "Y ahora no podrás resistir a semejante caballería ni a "
              "semejante ejército en la llanura, donde no hay piedra ni "
              "guijarro ni sitio por donde huir».",
    (10, 74): "Y cuando Jonatán oyó las palabras de Apolonio, se le removió el "
              "ánimo; y escogió diez mil hombres y salió de Jerusalén, y se le "
              "unió Simón su hermano para ayudarlo.",
    (10, 75): "Y acampó contra Jope, y los de la ciudad le cerraron las "
              "puertas, porque había en Jope una guarnición de Apolonio; y la "
              "atacaron.",
    (10, 76): "Y los de la ciudad, atemorizados, abrieron; y Jonatán se hizo "
              "dueño de Jope.",
    (10, 77): "Y lo oyó Apolonio, y sacó al campo tres mil jinetes y un gran "
              "ejército, y fue hacia Azoto como si estuviera de paso, y al "
              "mismo tiempo avanzaba hacia la llanura, porque tenía mucha "
              "caballería y confiaba en ella.",
    (10, 78): "Y Jonatán lo persiguió hacia Azoto, y los ejércitos vinieron a "
              "las manos.",
    (10, 79): "Y Apolonio había dejado mil jinetes escondidos detrás de "
              "ellos;",
    (10, 80): "y Jonatán supo que había una emboscada a sus espaldas. Y le "
              "rodearon el campamento y dispararon saetas contra la gente "
              "desde la mañana hasta la tarde;",
    (10, 81): "pero la gente resistió como Jonatán había mandado, y los "
              "caballos de aquéllos se cansaron.",
    (10, 82): "Y Simón sacó su tropa y atacó a la falange, porque la "
              "caballería estaba agotada; y fueron destrozados por él y "
              "huyeron.",
    (10, 83): "Y la caballería se dispersó por la llanura, y huyeron a Azoto y "
              "entraron en Bet-Dagón, el templo de su ídolo, para salvarse.",
    (10, 84): "Y Jonatán prendió fuego a Azoto y a las ciudades de alrededor, "
              "y tomó sus despojos; y el templo de Dagón, con los que se "
              "habían refugiado en él, lo quemó.",
    (10, 85): "Y los caídos a espada, con los que perecieron en el fuego, "
              "fueron unos ocho mil hombres.",
    (10, 86): "Y Jonatán partió de allí y acampó frente a Ascalón; y los de la "
              "ciudad salieron a su encuentro con grandes honores.",
    (10, 87): "Y Jonatán volvió con los suyos a Jerusalén llevando muchos "
              "despojos.",
    (10, 88): "Y sucedió que, cuando el rey Alejandro oyó estas noticias, "
              "honró todavía más a Jonatán,",
    (10, 89): "y le envió una hebilla de oro, como es costumbre dar a los "
              "parientes de los reyes; y le dio Acarón con todos sus términos "
              "en posesión.",

    (11, 1): "Y el rey de Egipto reunió tropas numerosas como la arena de la "
             "orilla del mar, y muchas naves; y buscaba apoderarse con engaño "
             "del reino de Alejandro y añadirlo al suyo.",
    (11, 2): "Y salió hacia Siria con palabras de paz; y los de las ciudades "
             "le abrían y salían a su encuentro, porque el rey Alejandro había "
             "ordenado que salieran a recibirlo, por ser su suegro.",
    (11, 3): "Pero cuando entraba en las ciudades de Tolemaida, iba dejando "
             "tropas de guarnición en cada ciudad.",
    (11, 4): "Y cuando se acercó a Azoto, le enseñaron el templo de Dagón "
             "quemado, y Azoto y sus arrabales derruidos, y los cadáveres "
             "tirados, y los restos de los quemados en la guerra, porque "
             "habían hecho montones con ellos a su paso.",
    (11, 5): "Y le contaron al rey lo que había hecho Jonatán, para que lo "
             "culpase; pero el rey calló.",
    (11, 6): "Y Jonatán salió al encuentro del rey en Jope con toda pompa, y "
             "se saludaron y pasaron allí la noche.",
    (11, 7): "Y Jonatán fue con el rey hasta el río llamado Eléuteros, y se "
             "volvió a Jerusalén.",
    (11, 8): "Y el rey Tolomeo se hizo dueño de las ciudades de la costa hasta "
             "Seleucia la marítima, y tramaba planes perversos contra "
             "Alejandro.",
    (11, 9): "Y envió embajadores al rey Demetrio, diciendo: «Ven, hagamos "
             "entre nosotros un pacto, y te daré a mi hija, la que tiene "
             "Alejandro, y reinarás en el reino de tu padre;",
    (11, 10): "porque me he arrepentido de haberle dado a mi hija, pues ha "
              "intentado matarme».",
    (11, 11): "Y lo acusó porque codiciaba su reino.",
    (11, 12): "Y quitándole su hija, se la dio a Demetrio; y el rostro de "
              "Alejandro se mudó, y quedó clara su enemistad.",
    (11, 13): "Y Tolomeo entró en Antioquía y se ciñó la diadema de Asia; y "
              "llevaba dos diademas en la cabeza: la de Asia y la de Egipto.",
    (11, 14): "Y el rey Alejandro estaba por aquel tiempo en Cilicia, porque "
              "los de aquellos lugares se habían rebelado.",
    (11, 15): "Y lo oyó Alejandro y fue contra él en son de guerra; y Tolomeo "
              "sacó sus tropas y le salió al encuentro con mano fuerte, y lo "
              "puso en fuga.",
    (11, 16): "Y Alejandro huyó a Arabia para ponerse allí a salvo; y el rey "
              "Tolomeo quedó encumbrado.",
    (11, 17): "Y Zabdiel el árabe le cortó la cabeza a Alejandro y se la envió "
              "a Tolomeo.",
    (11, 18): "Y el rey Tolomeo murió al tercer día, y los que estaban en sus "
              "plazas fuertes fueron muertos por los habitantes de las "
              "plazas.",
    (11, 19): "Y Demetrio empezó a reinar el año ciento sesenta y siete.",
    (11, 20): "En aquellos días Jonatán reunió a los de Judea para atacar la "
              "ciudadela de Jerusalén; e hicieron contra ella muchas "
              "máquinas.",
    (11, 21): "Y fueron al rey algunos que odiaban a su propio pueblo, hombres "
              "sin ley, y le comunicaron que Jonatán tenía cercada la "
              "ciudadela.",
    (11, 22): "Y al oírlo se enfureció; y en cuanto lo supo partió en seguida "
              "y llegó a Tolemaida, y escribió a Jonatán que levantase el "
              "cerco y que fuese a verlo cuanto antes a Tolemaida.",
    (11, 23): "Y cuando Jonatán lo oyó, mandó seguir el cerco; y escogió a "
              "algunos de los ancianos de Israel y de los sacerdotes, y se "
              "expuso al peligro.",
    (11, 24): "Y tomando plata y oro y vestidos y otros muchos regalos, fue al "
              "rey a Tolemaida, y halló gracia delante de él.",
    (11, 25): "Y algunos sin ley de su nación lo acusaban;",
    (11, 26): "pero el rey hizo con él como habían hecho sus predecesores, y "
              "lo ensalzó delante de todos sus amigos;",
    (11, 27): "y le confirmó el sumo sacerdocio y todos los demás honores que "
              "antes tenía, y lo hizo figurar entre sus primeros amigos.",
    (11, 28): "Y Jonatán pidió al rey que declarase exenta de tributo a Judea "
              "y a las tres toparquías y a Samaria; y le prometió trescientos "
              "talentos.",
    (11, 29): "Y el rey accedió, y escribió a Jonatán cartas sobre todo esto "
              "en estos términos:",
    (11, 30): "«El rey Demetrio a su hermano Jonatán y al pueblo de los "
              "judíos, salud.",
    (11, 31): "La copia de la carta que hemos escrito acerca de vosotros a "
              "Lástenes, nuestro pariente, os la enviamos también a vosotros "
              "para que la veáis:",
    (11, 32): "“El rey Demetrio a Lástenes, su padre, salud.",
    (11, 33): "Al pueblo de los judíos, amigos nuestros y que guardan lo que "
              "es justo con nosotros, hemos decidido hacerles bien por su "
              "buena voluntad hacia nosotros.",
    (11, 34): "Les hemos confirmado, pues, los términos de Judea y los tres "
              "distritos de Aferema y Lida y Ratamín —que fueron agregados a "
              "Judea desde Samaria— y todo lo que les corresponde, para todos "
              "los que sacrifican en Jerusalén, en lugar de los derechos "
              "reales que el rey les cobraba antes cada año de los frutos de "
              "la tierra y de los árboles.",
    (11, 35): "Y todo lo demás que nos corresponde desde ahora de los diezmos "
              "y de los impuestos que nos pertenecen, y las salinas, y las "
              "coronas que nos corresponden, todo se lo cedemos.",
    (11, 36): "Y nada de esto será anulado desde ahora y para siempre.",
    (11, 37): "Ahora, pues, cuidad de hacer una copia de esto, y désele a "
              "Jonatán, y colóquese en el monte santo en un lugar adecuado y "
              "bien visible”».",
    (11, 38): "Y vio el rey Demetrio que la tierra estaba tranquila delante de "
              "él y que nadie le hacía frente, y licenció a todas sus tropas, "
              "cada uno a su lugar, salvo las tropas extranjeras que había "
              "reclutado de las islas de las naciones; y se le hicieron "
              "enemigas todas las tropas heredadas de sus padres.",
    (11, 39): "Y Trifón, que antes había sido de los de Alejandro, vio que "
              "todas las tropas murmuraban contra Demetrio, y fue a Simalcué "
              "el árabe, que criaba a Antíoco, el niño de Alejandro;",
    (11, 40): "y le insistía para que se lo entregase, para hacerlo reinar en "
              "lugar de su padre. Y le contó todo lo que Demetrio había hecho, "
              "y la enemistad que le tenían sus tropas; y estuvo allí muchos "
              "días.",
    (11, 41): "Y Jonatán envió a decir al rey Demetrio que echase a los de la "
              "ciudadela de Jerusalén y a los de las fortalezas, porque "
              "hostigaban a Israel.",
    (11, 42): "Y Demetrio envió a decir a Jonatán: «No sólo haré esto por ti y "
              "por tu pueblo, sino que te colmaré de honores a ti y a tu "
              "pueblo si encuentro la ocasión.",
    (11, 43): "Ahora, pues, harás bien en enviarme hombres que peleen a mi "
              "lado, porque todas mis tropas me han abandonado».",
    (11, 44): "Y Jonatán le envió a Antioquía tres mil hombres valientes; y "
              "llegaron ante el rey, y el rey se alegró de su llegada.",
    (11, 45): "Y se juntaron los de la ciudad en el centro de la ciudad, hasta "
              "ciento veinte mil hombres, y querían matar al rey.",
    (11, 46): "Y el rey huyó al palacio, y los de la ciudad ocuparon los pasos "
              "de la ciudad y empezaron a atacar.",
    (11, 47): "Y el rey llamó en su ayuda a los judíos, y todos acudieron a él "
              "a la vez; y se desplegaron por la ciudad, y mataron aquel día "
              "en la ciudad a unos cien mil.",
    (11, 48): "Y prendieron fuego a la ciudad y tomaron muchos despojos aquel "
              "día, y salvaron al rey.",
    (11, 49): "Y vieron los de la ciudad que los judíos se habían adueñado de "
              "la ciudad a su antojo, y se les vino abajo el ánimo, y clamaron "
              "al rey suplicando:",
    (11, 50): "«Danos la mano, y que los judíos dejen de pelear contra "
              "nosotros y contra la ciudad».",
    (11, 51): "Y arrojaron las armas e hicieron la paz; y los judíos fueron "
              "honrados delante del rey y delante de todos los de su reino, y "
              "volvieron a Jerusalén con muchos despojos.",
    (11, 52): "Y el rey Demetrio se sentó en el trono de su reino, y la tierra "
              "estuvo tranquila delante de él;",
    (11, 53): "pero faltó a todo lo que había dicho, y se apartó de Jonatán y "
              "no le devolvió los favores que él le había hecho, y lo afligió "
              "mucho.",
    (11, 54): "Y después de esto volvió Trifón con Antíoco, un muchacho "
              "todavía niño; y lo hizo rey y le puso la diadema.",
    (11, 55): "Y se le juntaron todas las tropas que Demetrio había despedido, "
              "y pelearon contra él; y él huyó y fue derrotado.",
    (11, 56): "Y Trifón se apoderó de los elefantes y se hizo dueño de "
              "Antioquía.",
    (11, 57): "Y Antíoco el joven escribió a Jonatán diciendo: «Te confirmo el "
              "sumo sacerdocio y te pongo al frente de los cuatro distritos, y "
              "que seas de los amigos del rey».",
    (11, 58): "Y le envió vajilla de oro y servicio de mesa, y le dio "
              "autoridad para beber en vasos de oro y para vestir de púrpura y "
              "para llevar la hebilla de oro.",
    (11, 59): "Y a Simón su hermano lo nombró general desde la Escala de Tiro "
              "hasta los términos de Egipto.",
    (11, 60): "Y Jonatán salió y recorría el otro lado del río y las ciudades; "
              "y se le juntaron todas las tropas de Siria como aliadas. Y "
              "llegó a Ascalón, y los de la ciudad salieron a recibirlo con "
              "honores.",
    (11, 61): "Y de allí fue a Gaza, y los de Gaza le cerraron las puertas; y "
              "la cercó y prendió fuego a sus arrabales y los saqueó.",
    (11, 62): "Y los de Gaza se lo pidieron a Jonatán, y él les dio la mano; y "
              "tomó como rehenes a los hijos de sus jefes y los envió a "
              "Jerusalén; y recorrió el país hasta Damasco.",
    (11, 63): "Y oyó Jonatán que los jefes de Demetrio estaban en Cedes de "
              "Galilea con un gran ejército, con intención de apartarlo de su "
              "cargo.",
    (11, 64): "Y salió a su encuentro, y dejó en el país a Simón su hermano.",
    (11, 65): "Y Simón acampó contra Betsur y la atacó muchos días, y la tuvo "
              "cercada.",
    (11, 66): "Y le pidieron la paz, y él se la concedió; y los echó de allí y "
              "tomó la ciudad, y puso en ella guarnición.",
    (11, 67): "Y Jonatán y su ejército acamparon junto al agua de Genesaret, y "
              "de madrugada salieron a la llanura de Jasor.",
    (11, 68): "Y he aquí que un ejército de extranjeros le salió al encuentro "
              "en la llanura; y habían puesto contra él una emboscada en los "
              "montes, mientras ellos le salían de frente.",
    (11, 69): "Y los de la emboscada salieron de sus puestos y trabaron "
              "combate; y todos los de Jonatán huyeron,",
    (11, 70): "y no quedó de ellos ni uno, salvo Matatías hijo de Absalón y "
              "Judas hijo de Calfí, jefes del ejército.",
    (11, 71): "Y Jonatán rasgó sus vestidos y se echó tierra en la cabeza, y "
              "oró.",
    (11, 72): "Y volvió contra ellos a la batalla, y los puso en fuga, y "
              "huyeron.",
    (11, 73): "Y lo vieron los suyos que habían huido, y se volvieron a él y "
              "los persiguieron con él hasta Cedes, hasta su campamento; y "
              "acamparon allí.",
    (11, 74): "Y cayeron de los extranjeros aquel día unos tres mil hombres; y "
              "Jonatán se volvió a Jerusalén.",

    # Capítulo 12
    (12, 1): "Y vio Jonatán que el momento le era favorable, y escogió hombres, y los envió a Roma a confirmar y renovar la amistad con ellos;",
    (12, 2): "y a los espartanos y a otros lugares envió cartas en el mismo sentido.",
    (12, 3): "Y fueron a Roma, y entraron en el senado, y dijeron: «Jonatán el sumo sacerdote y la nación de los judíos nos han enviado a renovar con vosotros la amistad y la alianza como antes.»",
    (12, 4): "Y les dieron cartas para los suyos en cada lugar, a fin de que los escoltaran hasta la tierra de Judá en paz.",
    (12, 5): "Y esta es la copia de las cartas que escribió Jonatán a los espartanos:",
    (12, 6): "«Jonatán, sumo sacerdote de la nación, y el consejo de ancianos y los sacerdotes y el resto del pueblo de los judíos, a los espartanos, sus hermanos: salud.",
    (12, 7): "Ya antes fueron enviadas cartas a Onías el sumo sacerdote de parte de Areo, el que reinaba entre vosotros, diciendo que sois hermanos nuestros, como lo muestra la copia que va debajo.",
    (12, 8): "Y Onías recibió con honor al hombre enviado, y tomó las cartas, en las cuales se hablaba con claridad de alianza y de amistad.",
    (12, 9): "Y nosotros, aunque no tenemos necesidad de esto, pues tenemos por consuelo los libros santos que están en nuestras manos,",
    (12, 10): "hemos intentado enviar a renovar la hermandad y la amistad con vosotros, para no quedar extraños a vosotros; porque han pasado muchos años desde que nos escribisteis.",
    (12, 11): "Nosotros, pues, en todo tiempo, sin cesar, en las fiestas y en los demás días señalados, nos acordamos de vosotros en los sacrificios que ofrecemos y en las oraciones, como es debido y conviene acordarse de hermanos.",
    (12, 12): "Y nos alegramos de vuestra gloria.",
    (12, 13): "Pero a nosotros nos han rodeado muchas tribulaciones y muchas guerras, y nos han hecho guerra los reyes que están a nuestro alrededor.",
    (12, 14): "No hemos querido, pues, importunaros a vosotros ni a los demás aliados y amigos nuestros en estas guerras,",
    (12, 15): "porque tenemos el auxilio del cielo que nos auxilia, y fuimos librados de nuestros enemigos, y nuestros enemigos fueron humillados.",
    (12, 16): "Escogimos, pues, a Numenio hijo de Antíoco y a Antípatro hijo de Jasón, y los hemos enviado a los romanos a renovar la amistad y la alianza que antes teníamos con ellos.",
    (12, 17): "Les hemos mandado, pues, que pasen también por donde vosotros y os saluden, y os entreguen nuestras cartas acerca de la renovación de nuestra hermandad.",
    (12, 18): "Y ahora haréis bien en respondernos a esto.»",
    (12, 19): "Y esta es la copia de las cartas que enviaron a Onías:",
    (12, 20): "«Areo, rey de los espartanos, a Onías, gran sacerdote: salud.",
    (12, 21): "Se ha encontrado en un escrito, acerca de los espartanos y de los judíos, que son hermanos y que son del linaje de Abrahán.",
    (12, 22): "Y ahora, desde que sabemos esto, haréis bien en escribirnos acerca de vuestra paz.",
    (12, 23): "Y nosotros a nuestra vez os escribimos: vuestros ganados y vuestros bienes son nuestros, y los nuestros son vuestros. Mandamos, pues, que os lo anuncien en este sentido.»",
    (12, 24): "Y oyó Jonatán que los jefes de Demetrio habían vuelto con un ejército mayor que el anterior para hacerle guerra.",
    (12, 25): "Y salió de Jerusalén y les salió al encuentro en la región de Hamat, porque no les dio tregua para poner pie en su territorio.",
    (12, 26): "Y envió espías a su campamento; y volvieron y le informaron que estaban dispuestos a caer sobre ellos de noche.",
    (12, 27): "Y cuando se puso el sol, mandó Jonatán a los suyos velar y estar sobre las armas, preparándose para la batalla toda la noche; y puso avanzadas alrededor del campamento.",
    (12, 28): "Y oyeron los adversarios que Jonatán y los suyos estaban preparados para la batalla, y tuvieron miedo, y su corazón se acobardó, y encendieron hogueras en su campamento.",
    (12, 29): "Pero Jonatán y los suyos no lo advirtieron hasta la mañana, porque veían las luces ardiendo.",
    (12, 30): "Y los persiguió, y no los alcanzó, porque habían pasado el río Eléutero.",
    (12, 31): "Y se desvió Jonatán contra los árabes llamados zabadeos, y los derrotó y tomó sus despojos.",
    (12, 32): "Y levantando el campo, fue a Damasco, y recorrió toda la región.",
    (12, 33): "Y Simón salió y recorrió hasta Ascalón y las fortalezas vecinas, y se desvió hacia Jope y la ocupó de antemano,",
    (12, 34): "porque había oído que querían entregar la fortaleza a los de Demetrio; y puso allí una guarnición para que la custodiara.",
    (12, 35): "Y volvió Jonatán y convocó a los ancianos del pueblo, y deliberó con ellos sobre edificar fortalezas en Judea,",
    (12, 36): "y levantar más los muros de Jerusalén, y alzar una gran altura entre la ciudadela y la ciudad, para separarla de la ciudad, de modo que quedara sola, y así no pudieran ni comprar ni vender.",
    (12, 37): "Y se reunieron para edificar, y se cayó parte del muro del torrente, el del oriente, y reparó el llamado Cafenatá.",
    (12, 38): "Y Simón edificó Hadidá en la Sefelá, y la fortificó con puertas y cerrojos.",
    (12, 39): "Y buscó Trifón reinar sobre Asia y ceñirse la diadema y levantar la mano contra el rey Antíoco.",
    (12, 40): "Y temió que quizá no se lo consintiera Jonatán y que le hiciera guerra, y buscaba el modo de prenderlo para matarlo; y partiendo, llegó a Betsán.",
    (12, 41): "Y salió Jonatán a su encuentro con cuarenta mil hombres escogidos para la batalla, y llegó a Betsán.",
    (12, 42): "Y vio Trifón que estaba allí con un ejército numeroso, y temió levantar la mano contra él.",
    (12, 43): "Y lo recibió con honor, y lo presentó a todos sus amigos, y le dio regalos, y mandó a sus amigos y a sus tropas que le obedecieran a él igual que a sí mismo.",
    (12, 44): "Y dijo a Jonatán: «¿Por qué has fatigado a todo este pueblo, no habiendo guerra entre nosotros?",
    (12, 45): "Ahora, pues, envíalos a sus casas, y escógete unos pocos hombres que estén contigo; y ven conmigo a Tolemaida, y te la entregaré, y las demás fortalezas y las tropas y todos los que están al frente de los servicios, y luego me volveré y me iré; porque para esto he venido.»",
    (12, 46): "Y confiando en él, hizo como le dijo, y despidió las tropas, y se fueron a la tierra de Judá.",
    (12, 47): "Y dejó consigo tres mil hombres; de ellos dejó dos mil en Galilea, y mil fueron con él.",
    (12, 48): "Y cuando entró Jonatán en Tolemaida, los tolemaidenses cerraron las puertas y lo prendieron, y a todos los que habían entrado con él los mataron a espada.",
    (12, 49): "Y envió Trifón tropas y caballería a Galilea, a la gran llanura, para destruir a todos los de Jonatán.",
    (12, 50): "Y ellos supieron que había sido apresado y que había perecido, y los que estaban con él; y se animaron unos a otros, y marchaban en formación cerrada, dispuestos a pelear.",
    (12, 51): "Y vieron los perseguidores que se jugaban la vida, y se volvieron.",
    (12, 52): "Y llegaron todos en paz a la tierra de Judá, e hicieron duelo por Jonatán y por los que estaban con él, y tuvieron gran miedo; e hizo Israel un gran duelo.",
    (12, 53): "Y buscaron todas las naciones de alrededor aniquilarlos, porque decían: «No tienen hombre que los mande ni que los socorra; peleemos, pues, ahora contra ellos, y borraremos de entre los hombres su memoria.»",

    # Capítulo 13
    (13, 1): "Y oyó Simón que Trifón había reunido un ejército numeroso para entrar en la tierra de Judá y aniquilarla.",
    (13, 2): "Y vio al pueblo que estaba tembloroso y atemorizado, y subió a Jerusalén y reunió al pueblo;",
    (13, 3): "y los animó, y les dijo: «Vosotros mismos sabéis cuánto hemos hecho yo y mis hermanos y la casa de mi padre por las leyes y por el santuario, y las guerras y las angustias.",
    (13, 4): "Por esta causa murieron todos mis hermanos por Israel, y quedé yo solo.",
    (13, 5): "Y ahora, lejos de mí perdonar mi propia vida en ningún tiempo de tribulación, porque no soy mejor que mis hermanos.",
    (13, 6): "Al contrario, vengaré a mi nación y al santuario y a nuestras mujeres y a nuestros hijos, porque se han juntado todas las naciones para aniquilarnos por odio.»",
    (13, 7): "Y se reavivó el espíritu del pueblo al oír estas palabras;",
    (13, 8): "y respondieron a gran voz diciendo: «Tú eres nuestro jefe en lugar de Judas y de Jonatán tu hermano;",
    (13, 9): "pelea nuestra guerra, y todo cuanto nos digas lo haremos.»",
    (13, 10): "Y reunió a todos los hombres de guerra, y se dio prisa a terminar los muros de Jerusalén, y la fortificó todo alrededor.",
    (13, 11): "Y envió a Jonatán hijo de Absalón, y con él una fuerza considerable, a Jope; y echó fuera a los que estaban en ella, y se quedó allí en ella.",
    (13, 12): "Y partió Trifón de Tolemaida con un ejército numeroso para entrar en la tierra de Judá, y Jonatán con él bajo custodia;",
    (13, 13): "y Simón acampó en Hadidá, frente a la llanura.",
    (13, 14): "Y supo Trifón que Simón se había levantado en lugar de Jonatán su hermano, y que estaba a punto de trabar batalla con él; y le envió embajadores diciendo:",
    (13, 15): "«Por el dinero que tu hermano Jonatán debía al tesoro real, por los cargos que tenía, lo retenemos.",
    (13, 16): "Y ahora envía cien talentos de plata y dos de sus hijos como rehenes, para que, una vez suelto, no se nos rebele, y lo soltaremos.»",
    (13, 17): "Y comprendió Simón que le hablaban con engaño, pero mandó el dinero y los muchachos, para que no levantara una gran enemistad contra él el pueblo,",
    (13, 18): "diciendo: «Porque no le envió el dinero y los muchachos, murió.»",
    (13, 19): "Y envió los muchachos y los cien talentos; y aquel mintió, y no soltó a Jonatán.",
    (13, 20): "Y después de esto vino Trifón para invadir el país y aniquilarlo, y dio un rodeo por el camino de Adorá; y Simón y su ejército le salían al paso dondequiera que iba.",
    (13, 21): "Y los de la ciudadela enviaban mensajeros a Trifón dándole prisa para que viniese a ellos por el desierto y les enviase víveres.",
    (13, 22): "Y preparó Trifón toda su caballería para ir; y aquella noche hubo muchísima nieve, y no fue a causa de la nieve; y levantó el campo y se fue a Galaad.",
    (13, 23): "Y cuando se acercó a Bascamá, mató a Jonatán, y allí fue sepultado.",
    (13, 24): "Y volvió Trifón y se fue a su tierra.",
    (13, 25): "Y envió Simón, y tomó los huesos de Jonatán su hermano, y lo sepultó en Modín, la ciudad de sus padres.",
    (13, 26): "Y todo Israel lo lloró con gran llanto, y le hicieron duelo muchos días.",
    (13, 27): "Y edificó Simón sobre el sepulcro de su padre y de sus hermanos, y lo levantó de modo que se viera, con piedra pulida por detrás y por delante.",
    (13, 28): "Y erigió siete pirámides, una frente a otra, para el padre y la madre y los cuatro hermanos.",
    (13, 29): "Y para ellas hizo obras, rodeándolas de grandes columnas, y puso sobre las columnas armaduras completas para memoria perpetua, y junto a las armaduras naves esculpidas, para que las vieran todos los que navegan el mar.",
    (13, 30): "Este es el sepulcro que hizo en Modín, hasta el día de hoy.",
    (13, 31): "Y Trifón procedía con engaño con Antíoco el rey joven, y lo mató,",
    (13, 32): "y reinó en su lugar, y se ciñó la diadema de Asia, y causó una gran plaga en la tierra.",
    (13, 33): "Y edificó Simón las fortalezas de Judea, y las rodeó de torres altas y de grandes murallas, y de torres y puertas y cerrojos, y puso provisiones en las fortalezas.",
    (13, 34): "Y escogió Simón hombres, y los envió al rey Demetrio para que hiciese remisión al país, porque todos los actos de Trifón eran rapiña.",
    (13, 35): "Y el rey Demetrio le envió respuesta conforme a estas palabras, y le respondió, y le escribió una carta como esta:",
    (13, 36): "«El rey Demetrio a Simón, sumo sacerdote y amigo de reyes, y a los ancianos y a la nación de los judíos: salud.",
    (13, 37): "La corona de oro y la palma que enviasteis las hemos recibido, y estamos dispuestos a hacer con vosotros una paz grande, y a escribir a los encargados de los servicios que os concedan exenciones.",
    (13, 38): "Y cuanto hemos establecido con vosotros queda firme, y las fortalezas que habéis edificado sean vuestras.",
    (13, 39): "Y os perdonamos los descuidos y las faltas hasta el día de hoy, y la corona que debíais; y si algún otro tributo se cobraba en Jerusalén, que no se cobre más.",
    (13, 40): "Y si algunos de vosotros son aptos para ser inscritos entre los de nuestra guardia, que se inscriban, y haya paz entre nosotros.»",
    (13, 41): "El año ciento setenta fue quitado el yugo de las naciones de sobre Israel,",
    (13, 42): "y comenzó el pueblo de Israel a escribir en los documentos y contratos: «Año primero, bajo Simón, sumo sacerdote grande, general y jefe de los judíos.»",
    (13, 43): "En aquellos días acampó contra Gazara, y la rodeó de campamentos, e hizo una torre de asalto y la acercó a la ciudad, y batió una torre y la tomó.",
    (13, 44): "Y los que estaban en la torre de asalto saltaron a la ciudad, y hubo un gran tumulto en la ciudad.",
    (13, 45): "Y subieron los de la ciudad con sus mujeres y sus hijos al muro, rasgados sus vestidos, y clamaron a gran voz pidiendo a Simón que les diera la mano.",
    (13, 46): "Y dijeron: «No nos trates conforme a nuestras maldades, sino conforme a tu misericordia.»",
    (13, 47): "Y Simón se avino con ellos, y no les hizo guerra; y los echó de la ciudad, y purificó las casas en que había ídolos, y así entró en ella cantando himnos y bendiciendo.",
    (13, 48): "Y echó de ella toda inmundicia, y estableció en ella hombres que cumplen la ley; y la fortificó más, y se edificó en ella una residencia.",
    (13, 49): "Y a los de la ciudadela de Jerusalén se les impedía salir al campo y comprar y vender; y pasaron mucha hambre, y perecieron de ellos no pocos por el hambre.",
    (13, 50): "Y clamaron a Simón pidiendo la mano, y él se la dio, y los echó de allí, y purificó la ciudadela de sus contaminaciones.",
    (13, 51): "Y entró en ella el día veintitrés del mes segundo del año ciento setenta y uno, con alabanza y con palmas, y con cítaras y con címbalos y con arpas, y con himnos y con cánticos, porque había sido quebrantado un gran enemigo de Israel.",
    (13, 52): "Y estableció que cada año se celebrase aquel día. Y fortificó más el monte del templo, el que está junto a la ciudadela, y habitó allí él y los suyos.",
    (13, 53): "Y vio Simón que Juan su hijo era ya un hombre, y lo puso por jefe de todas las tropas; y habitaba en Gazara.",

    # Capítulo 14
    (14, 1): "Y el año ciento setenta y dos reunió el rey Demetrio sus tropas, y fue a Media a procurarse ayuda para hacer guerra a Trifón.",
    (14, 2): "Y oyó Arsaces, rey de Persia y de Media, que Demetrio había entrado en su territorio, y envió a uno de sus jefes a prenderlo vivo.",
    (14, 3): "Y fue y derrotó el campamento de Demetrio y lo prendió, y lo llevó a Arsaces, y lo puso en prisión.",
    (14, 4): "Y la tierra tuvo reposo todos los días de Simón; y él buscó el bien de su nación, y les agradó su autoridad y su gloria todos los días.",
    (14, 5): "Y en medio de toda su gloria tomó a Jope por puerto, y abrió una entrada hacia las islas del mar.",
    (14, 6): "Y ensanchó las fronteras de su nación, y se adueñó del país.",
    (14, 7): "Y reunió muchos cautivos, y se enseñoreó de Gazara y de Betsur y de la ciudadela; y quitó de ella las inmundicias, y no hubo quien se le opusiera.",
    (14, 8): "Y cultivaban su tierra en paz, y la tierra daba sus frutos, y los árboles de los campos su fruto.",
    (14, 9): "Los ancianos se sentaban en las plazas, todos hablaban de los bienes, y los jóvenes se vistieron de gala y de arreos de guerra.",
    (14, 10): "A las ciudades proveyó de víveres, y las dotó de medios de fortificación, hasta que el nombre de su gloria fue nombrado hasta el extremo de la tierra.",
    (14, 11): "Hizo la paz en la tierra, y se alegró Israel con gran alegría.",
    (14, 12): "Y se sentó cada uno bajo su vid y su higuera, y no había quien los atemorizara;",
    (14, 13): "y no quedó quien les hiciera guerra en la tierra, y los reyes fueron quebrantados en aquellos días.",
    (14, 14): "Y sostuvo a todos los humildes de su pueblo; buscó la ley, y quitó a todo inicuo y malvado;",
    (14, 15): "glorificó el santuario, y multiplicó los utensilios del santuario.",
    (14, 16): "Y se oyó en Roma que había muerto Jonatán, y hasta en Esparta, y se entristecieron mucho.",
    (14, 17): "Y cuando oyeron que Simón su hermano había llegado a ser sumo sacerdote en lugar de él, y que dominaba el país y las ciudades que hay en él,",
    (14, 18): "le escribieron en tablas de bronce, para renovar con él la amistad y la alianza que habían establecido con Judas y con Jonatán sus hermanos.",
    (14, 19): "Y fueron leídas ante la asamblea en Jerusalén.",
    (14, 20): "Y esta es la copia de las cartas que enviaron los espartanos: «Los magistrados de los espartanos y la ciudad, a Simón, gran sacerdote, y a los ancianos y a los sacerdotes y al resto del pueblo de los judíos, hermanos: salud.",
    (14, 21): "Los embajadores enviados a nuestro pueblo nos han informado de vuestra gloria y honor, y nos hemos alegrado de su llegada.",
    (14, 22): "Y hemos registrado lo dicho por ellos en las actas del pueblo así: “Numenio hijo de Antíoco y Antípatro hijo de Jasón, embajadores de los judíos, vinieron a nosotros a renovar la amistad con nosotros.",
    (14, 23): "Y agradó al pueblo recibir a estos hombres con honor, y poner la copia de sus palabras en los libros asignados al pueblo, para que el pueblo de los espartanos guarde memoria de ello.” Y la copia de esto la escribieron a Simón el sumo sacerdote.»",
    (14, 24): "Después de esto envió Simón a Numenio a Roma llevando un gran escudo de oro de mil minas de peso, para confirmar con ellos la alianza.",
    (14, 25): "Y cuando el pueblo oyó estas cosas, dijeron: «¿Qué gratitud daremos a Simón y a sus hijos?",
    (14, 26): "Porque él y sus hermanos y la casa de su padre se mantuvieron firmes, y combatieron a los enemigos de Israel y los apartaron de ellos.» Y le confirmaron la libertad, y la consignaron en tablas de bronce, y las pusieron en una estela en el monte Sión.",
    (14, 27): "Y esta es la copia del escrito: «El dieciocho de Elul del año ciento setenta y dos, que es el año tercero de Simón el sumo sacerdote,",
    (14, 28): "en Saramel, en la gran asamblea de los sacerdotes y del pueblo y de los jefes de la nación y de los ancianos del país, se nos hizo saber esto:",
    (14, 29): "Puesto que muchas veces ha habido guerras en el país, Simón hijo de Matatías, de los hijos de Joarib, y sus hermanos se expusieron al peligro y resistieron a los adversarios de su nación, para que subsistiera su santuario y la ley, y con gran gloria glorificaron a su nación;",
    (14, 30): "y Jonatán congregó a su nación, y llegó a ser su sumo sacerdote, y fue reunido a su pueblo;",
    (14, 31): "y quisieron sus enemigos invadir su país para asolar su tierra y extender las manos contra su santuario;",
    (14, 32): "entonces se levantó Simón y peleó por su nación, y gastó mucho dinero de lo suyo, y armó a los hombres del ejército de su nación y les dio sueldo;",
    (14, 33): "y fortificó las ciudades de Judea, y Betsur, que está en la frontera de Judea, donde antes estaban las armas de los enemigos, y puso allí una guarnición de hombres judíos;",
    (14, 34): "y fortificó a Jope, la que está junto al mar, y a Gazara, la que está en la frontera de Azoto, donde antes habitaban los enemigos, y estableció allí judíos, y puso en ellas cuanto era necesario para su restauración;",
    (14, 35): "y vio el pueblo la lealtad de Simón y la gloria que se propuso dar a su nación, y lo pusieron por jefe suyo y sumo sacerdote, por haber hecho él todo esto, y por la justicia y la lealtad que guardó a su nación, y porque buscó por todos los medios exaltar a su pueblo;",
    (14, 36): "y en sus días prosperó en sus manos que fueran expulsadas las naciones de su país, y también los que estaban en la ciudad de David, en Jerusalén, los que se habían hecho una ciudadela desde la cual salían, y profanaban los alrededores del santuario, y causaban un gran daño a la pureza;",
    (14, 37): "y estableció en ella hombres judíos, y la fortificó para seguridad del país y de la ciudad, y levantó más los muros de Jerusalén;",
    (14, 38): "y el rey Demetrio le confirmó por ello el sumo sacerdocio,",
    (14, 39): "y lo hizo de sus amigos, y lo honró con gran honor;",
    (14, 40): "pues se oyó que los judíos eran llamados por los romanos amigos y aliados y hermanos, y que habían recibido con honor a los embajadores de Simón;",
    (14, 41): "y que los judíos y los sacerdotes tuvieron a bien que Simón fuera su jefe y sumo sacerdote para siempre, hasta que se levante un profeta digno de fe;",
    (14, 42): "y que fuera general sobre ellos, y que tuviera a su cargo el santuario, para nombrar por medio de él a los encargados de sus obras y del país y de las armas y de las fortalezas;",
    (14, 43): "y que tuviera a su cargo el santuario, y que fuera obedecido por todos, y que se escribieran en su nombre todos los documentos del país, y que se vistiera de púrpura y llevara oro.",
    (14, 44): "Y a nadie del pueblo ni de los sacerdotes le será lícito anular nada de esto, ni contradecir lo que él diga, ni convocar reunión en el país sin él, ni vestirse de púrpura ni ceñirse broche de oro.",
    (14, 45): "Y el que obre contra esto o anule algo de ello será culpable.»",
    (14, 46): "Y todo el pueblo tuvo a bien conceder a Simón obrar conforme a estas palabras.",
    (14, 47): "Y Simón lo aceptó, y tuvo a bien ejercer el sumo sacerdocio y ser general y etnarca de los judíos y de los sacerdotes, y presidirlo todo.",
    (14, 48): "Y este escrito mandaron ponerlo en tablas de bronce, y erigirlas en el recinto del santuario, en lugar seguro;",
    (14, 49): "y poner copias de ellas en el tesoro, para que las tuvieran Simón y sus hijos.",

    # Capítulo 15
    (15, 1): "Y envió Antíoco, hijo del rey Demetrio, cartas desde las islas del mar a Simón, sacerdote y etnarca de los judíos, y a toda la nación.",
    (15, 2): "Y decían de esta manera: «El rey Antíoco a Simón, gran sacerdote y etnarca, y a la nación de los judíos: salud.",
    (15, 3): "Puesto que unos hombres pestilentes se han apoderado del reino de nuestros padres, y yo me propongo reivindicar el reino para restablecerlo como estaba antes, he reclutado una multitud de tropas y he equipado naves de guerra;",
    (15, 4): "y quiero desembarcar en el país para perseguir a los que han arruinado nuestra tierra y han devastado muchas ciudades del reino.",
    (15, 5): "Ahora, pues, te confirmo todas las exenciones que te concedieron los reyes anteriores a mí, y cuantas otras franquicias te concedieron,",
    (15, 6): "y te permito acuñar moneda propia para tu país;",
    (15, 7): "y que Jerusalén y el santuario sean libres; y todas las armas que has fabricado, y las fortalezas que has edificado y tienes en tu poder, queden tuyas.",
    (15, 8): "Y toda deuda con el rey, y las que hubiere en adelante, desde ahora y para todo tiempo, te sea perdonada.",
    (15, 9): "Y cuando hayamos afianzado nuestro reino, te glorificaremos a ti y a tu nación y al templo con gran gloria, de modo que vuestra gloria se haga manifiesta en toda la tierra.»",
    (15, 10): "El año ciento setenta y cuatro salió Antíoco hacia la tierra de sus padres, y se le unieron todas las tropas, de modo que pocos quedaron con Trifón.",
    (15, 11): "Y lo persiguió el rey Antíoco, y llegó huyendo a Dora, la que está sobre el mar,",
    (15, 12): "porque sabía que se le habían acumulado desgracias, y las tropas lo habían abandonado.",
    (15, 13): "Y acampó Antíoco contra Dora, y con él ciento veinte mil hombres de guerra y ocho mil de caballería.",
    (15, 14): "Y rodeó la ciudad, y las naves cerraron desde el mar; y apretaba la ciudad por tierra y por mar, y no dejaba a nadie salir ni entrar.",
    (15, 15): "Y llegó Numenio y los suyos de Roma con cartas para los reyes y los países, en las cuales estaba escrito esto:",
    (15, 16): "«Lucio, cónsul de los romanos, al rey Tolomeo: salud.",
    (15, 17): "Los embajadores de los judíos vinieron a nosotros como amigos y aliados nuestros, a renovar la amistad y la alianza de antiguo, enviados por Simón el sumo sacerdote y por el pueblo de los judíos;",
    (15, 18): "y trajeron un escudo de oro de mil minas.",
    (15, 19): "Nos ha parecido bien, pues, escribir a los reyes y a los países que no procuren su daño, ni les hagan guerra a ellos ni a sus ciudades ni a sus tierras, y que no se alíen con los que les hagan guerra.",
    (15, 20): "Y nos ha parecido bien aceptar de ellos el escudo.",
    (15, 21): "Si, pues, algunos hombres pestilentes han huido de su país a vosotros, entregadlos a Simón el sumo sacerdote, para que los castigue conforme a su ley.»",
    (15, 22): "Y lo mismo escribió al rey Demetrio y a Átalo y a Ariarates y a Arsaces,",
    (15, 23): "y a todos los países, y a Sámpsames, y a los espartanos, y a Delos y a Mindos y a Sición y a Caria y a Samos y a Panfilia y a Licia y a Halicarnaso y a Cos y a Side y a Arado y a Rodas y a Faselis y a Gortina y a Cnido y a Chipre y a Cirene.",
    (15, 24): "Y la copia de estas cartas la escribieron a Simón el sumo sacerdote.",
    (15, 25): "Y el rey Antíoco acampó contra Dora por segunda vez, acosándola sin cesar y construyendo máquinas, y encerró a Trifón de modo que no pudiera entrar ni salir.",
    (15, 26): "Y le envió Simón dos mil hombres escogidos para ayudarle, y plata y oro y pertrechos en abundancia.",
    (15, 27): "Y él no quiso recibirlos, sino que anuló todo cuanto antes había pactado con él, y se le hizo extraño.",
    (15, 28): "Y le envió a Atenobio, uno de sus amigos, para tratar con él, diciéndole: «Vosotros retenéis a Jope y a Gazara y a la ciudadela de Jerusalén, ciudades de mi reino.",
    (15, 29): "Habéis devastado sus territorios, y habéis hecho un gran estrago en el país, y os habéis enseñoreado de muchos lugares de mi reino.",
    (15, 30): "Ahora, pues, entregad las ciudades que habéis tomado y los tributos de los lugares de que os habéis apoderado fuera de las fronteras de Judea;",
    (15, 31): "y si no, dad en su lugar quinientos talentos de plata, y por la destrucción que habéis causado y por los tributos de las ciudades, otros quinientos talentos; y si no, iremos y os haremos la guerra.»",
    (15, 32): "Y llegó Atenobio, amigo del rey, a Jerusalén, y vio la gloria de Simón, y el aparador con vajilla de oro y de plata, y un séquito considerable; y quedó atónito, y les comunicó las palabras del rey.",
    (15, 33): "Y respondiendo Simón le dijo: «Ni hemos tomado tierra ajena, ni nos hemos apoderado de lo ajeno, sino de la heredad de nuestros padres, de la cual nuestros enemigos se apoderaron injustamente en cierto tiempo.",
    (15, 34): "Y nosotros, teniendo la ocasión, recobramos la heredad de nuestros padres.",
    (15, 35): "Y en cuanto a Jope y Gazara, que reclamas: estas hacían gran daño al pueblo y a nuestra tierra; por ellas daremos cien talentos.» Y no le respondió ni una palabra.",
    (15, 36): "Y volvió con furor al rey, y le comunicó estas palabras y la gloria de Simón y todo cuanto había visto; y se encolerizó el rey con gran cólera.",
    (15, 37): "Y Trifón, embarcándose en una nave, huyó a Ortosia.",
    (15, 38): "Y puso el rey a Cendebeo por comandante de la costa, y le dio tropas de infantería y de caballería.",
    (15, 39): "Y le mandó acampar frente a Judea, y le mandó edificar Cedrón y fortificar las ciudades, y hacer la guerra al pueblo; y el rey perseguía a Trifón.",
    (15, 40): "Y llegó Cendebeo a Jamnia, y comenzó a hostigar al pueblo y a invadir Judea, y a hacer cautivo al pueblo y a matarlo.",
    (15, 41): "Y edificó Cedrón, y puso allí jinetes y tropas para que salieran y recorrieran los caminos de Judea, según le había mandado el rey.",
    # Capítulo 16
    (16, 1): "Y subió Juan desde Gazara, y contó a Simón su padre lo que hacía Cendebeo.",
    (16, 2): "Y llamó Simón a sus dos hijos mayores, Judas y Juan, y les dijo: «Yo y mis hermanos y la casa de mi padre hemos peleado las guerras de Israel desde nuestra juventud hasta el día de hoy, y ha prosperado en nuestras manos librar a Israel muchas veces.",
    (16, 3): "Pero ahora he envejecido, y vosotros, por la misericordia, tenéis edad suficiente; ocupad mi lugar y el de mi hermano, y salid a combatir por nuestra nación, y el auxilio del cielo sea con vosotros.»",
    (16, 4): "Y escogió del país veinte mil hombres de guerra y jinetes, y marcharon contra Cendebeo, y pernoctaron en Modín.",
    (16, 5): "Y levantándose de mañana marcharon a la llanura; y he aquí un ejército numeroso al encuentro de ellos, infantes y jinetes, y había un torrente entre unos y otros.",
    (16, 6): "Y acampó frente a ellos él y su gente; y vio que la gente tenía miedo de pasar el torrente, y pasó él primero; y lo vieron los hombres, y pasaron detrás de él.",
    (16, 7): "Y dividió la tropa, y puso la caballería en medio de la infantería; y la caballería de los adversarios era muy numerosa.",
    (16, 8): "Y tocaron las trompetas, y Cendebeo fue puesto en fuga con su campamento, y cayeron de ellos muchos heridos; y los que quedaron huyeron a la fortaleza.",
    (16, 9): "Entonces fue herido Judas, el hermano de Juan; pero Juan los persiguió hasta llegar a Cedrón, la que él había edificado.",
    (16, 10): "Y huyeron a las torres que están en los campos de Azoto, y él la incendió con fuego; y cayeron de ellos unos mil hombres, y se volvió a Judea en paz.",
    (16, 11): "Y Tolomeo hijo de Abubo había sido puesto por general en la llanura de Jericó, y tenía mucha plata y oro,",
    (16, 12): "porque era yerno del sumo sacerdote.",
    (16, 13): "Y se ensoberbeció su corazón, y quiso adueñarse del país, y tramaba con engaño contra Simón y contra sus hijos, para quitarlos de en medio.",
    (16, 14): "Y Simón estaba recorriendo las ciudades del país y atendiendo a su cuidado, y bajó a Jericó él y Matatías y Judas, sus hijos, el año ciento setenta y siete, en el mes undécimo, que es el mes de Sebat.",
    (16, 15): "Y el hijo de Abubo los recibió con engaño en la fortalecilla llamada Doc, que él había edificado, y les ofreció un gran banquete; y escondió allí hombres.",
    (16, 16): "Y cuando Simón y sus hijos estuvieron ebrios, se levantó Tolomeo y los suyos, y tomaron sus armas, y entraron contra Simón en el banquete, y lo mataron a él y a sus hijos y a algunos de sus criados.",
    (16, 17): "E hizo una gran traición, y devolvió mal por bien.",
    (16, 18): "Y escribió Tolomeo esto, y lo envió al rey para que le enviase tropas de auxilio, y le entregaría el país de ellos y las ciudades.",
    (16, 19): "Y envió a otros a Gazara para acabar con Juan, y a los comandantes envió cartas para que se presentaran ante él, a fin de darles plata y oro y regalos.",
    (16, 20): "Y a otros los envió a apoderarse de Jerusalén y del monte del templo.",
    (16, 21): "Y uno se adelantó corriendo y avisó a Juan en Gazara que su padre y sus hermanos habían perecido, y que «ha enviado también a matarte a ti».",
    (16, 22): "Y al oírlo quedó muy consternado, y prendió a los hombres que venían a matarlo, y los mató, porque supo que buscaban matarlo.",
    (16, 23): "Y lo demás de los hechos de Juan, y de sus guerras, y de las proezas que hizo, y de la construcción de los muros que edificó, y de sus obras,",
    (16, 24): "he aquí, esto está escrito en el libro de los anales de su sumo sacerdocio, desde que llegó a ser sumo sacerdote después de su padre.",
}
