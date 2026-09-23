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
            "la guerra.",
    (4, 8): "Y dijo Judas a los hombres que estaban con él: «No temáis su "
            "multitud, ni os acobardéis ante su acometida.",
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
}
