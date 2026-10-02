"""La Sabiduría de Salomón en español, traducida del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. No la escribió
Salomón: está compuesta en griego, en Alejandría, probablemente en el siglo I
antes de Cristo, por un judío que escribe bajo su nombre —era un modo aceptado
de decir «esto es sabiduría del rey sabio», no una falsificación.

Vale la pena por tres cosas que un lector del Nuevo Testamento reconoce en
seguida. La primera es el capítulo 2: los impíos deciden acechar al justo
porque «se llama a sí mismo hijo de Dios» y resuelven condenarlo «a muerte
afrentosa» para ver si Dios lo libra. Los evangelios de la pasión hablan ese
mismo idioma. La segunda es el capítulo 7, donde la Sabiduría es «resplandor de
la luz eterna» e «imagen de su bondad»: Hebreos 1:3 y Colosenses 1:15 están
escritos con ese vocabulario. La tercera es el capítulo 13, la crítica de la
idolatría —los que por las obras no llegaron a conocer al artífice—, que es
casi punto por punto el argumento de Romanos 1.

Que el Nuevo Testamento use un lenguaje no lo convierte en Escritura, y este
libro tampoco lo pretende de sí mismo. Pero explica de dónde salen esas
palabras, y por eso está aquí.

La edición griega de esta aplicación numera los capítulos de un modo propio: el
capítulo 3 queda cortado en seis versículos y no hay capítulo 15. Se respeta lo
que trae el texto sin coser nada por cuenta propia.
"""

from __future__ import annotations

SABIDURIA_ES: dict[tuple[int, int], str] = {
    (1, 1): "Amad la justicia, los que juzgáis la tierra; pensad rectamente "
            "del Señor, y buscadlo con sencillez de corazón.",
    (1, 2): "Porque se deja hallar de los que no lo tientan, y se manifiesta a "
            "los que no desconfían de él;",
    (1, 3): "pues los razonamientos torcidos apartan de Dios, y su poder, "
            "puesto a prueba, deja en evidencia a los insensatos.",
    (1, 4): "Porque en un alma que trama el mal no entrará la sabiduría, ni "
            "habitará en un cuerpo empeñado en el pecado.",
    (1, 5): "Porque el espíritu santo que educa huye del engaño, y se aparta "
            "de los razonamientos sin sentido, y se retira cuando sobreviene "
            "la injusticia.",
    (1, 6): "Porque la sabiduría es un espíritu amigo de los hombres, y no "
            "dejará impune al blasfemo por lo que salga de sus labios; porque "
            "Dios es testigo de sus riñones, y observador veraz de su corazón, "
            "y oyente de su lengua.",
    (1, 7): "Porque el espíritu del Señor llena la tierra habitada, y el que "
            "todo lo abarca tiene conocimiento de cuanto se dice.",
    (1, 8): "Por eso, nadie que hable injusticias pasará inadvertido, ni "
            "escapará de la justicia cuando lo acuse.",
    (1, 9): "Porque los planes del impío serán examinados, y el eco de sus "
            "palabras llegará al Señor para probar sus iniquidades;",
    (1, 10): "porque un oído celoso lo escucha todo, y ni el rumor de las "
             "murmuraciones se le oculta.",
    (1, 11): "Guardaos, pues, de la murmuración inútil, y preservad vuestra "
             "lengua de la maledicencia; porque ni una palabra dicha a "
             "escondidas se irá sin consecuencia, y una boca que miente mata "
             "el alma.",
    (1, 12): "No busquéis la muerte con el extravío de vuestra vida, ni os "
             "atraigáis la ruina con las obras de vuestras manos;",
    (1, 13): "porque Dios no hizo la muerte, ni se alegra con la perdición de "
             "los vivientes.",
    (1, 14): "Porque todo lo creó para que existiera, y las criaturas del "
             "mundo son saludables, y no hay en ellas veneno de muerte, ni "
             "tiene el Hades reinado sobre la tierra;",
    (1, 15): "porque la justicia es inmortal. Pero los impíos con sus manos y "
             "con sus palabras llamaron a la muerte; teniéndola por amiga se "
             "consumieron, e hicieron pacto con ella, porque son dignos de ser "
             "de su bando.",

    (2, 1): "Porque se dijeron entre sí, razonando mal: «Corta y triste es "
            "nuestra vida, y no hay remedio cuando el hombre acaba, ni se ha "
            "conocido a nadie que volviese del Hades.",
    (2, 2): "Porque nacimos por azar, y después seremos como si no hubiéramos "
            "existido; porque humo es el aliento en nuestras narices, y la "
            "palabra, una chispa en el latir de nuestro corazón:",
    (2, 3): "apagada ésta, el cuerpo se volverá ceniza, y el espíritu se "
            "disipará como aire ligero.",
    (2, 4): "Y nuestro nombre será olvidado con el tiempo, y nadie se acordará "
            "de nuestras obras; y pasará nuestra vida como rastro de nube, y "
            "se disipará como niebla perseguida por los rayos del sol y "
            "agobiada por su calor.",
    (2, 5): "Porque nuestra vida es el paso de una sombra, y no hay vuelta "
            "atrás de nuestro fin, porque queda sellado y nadie regresa.",
    (2, 6): "Venid, pues, y gocemos de los bienes que hay, y usemos de lo "
            "creado con el ardor de la juventud.",
    (2, 7): "Hartémonos de vino costoso y de perfumes, y que no se nos escape "
            "ninguna flor de primavera;",
    (2, 8): "coronémonos de capullos de rosas antes de que se marchiten;",
    (2, 9): "que ninguno de nosotros falte a nuestra francachela; dejemos por "
            "todas partes las señales de nuestra alegría, porque ésta es "
            "nuestra parte y ésta nuestra suerte.",
    (2, 10): "Oprimamos al pobre que es justo, no perdonemos a la viuda ni "
             "respetemos las canas venerables del anciano;",
    (2, 11): "y sea nuestra fuerza la ley de la justicia, porque lo débil "
             "queda probado como inútil.",
    (2, 12): "Acechemos al justo, porque nos resulta incómodo y se opone a "
             "nuestras obras, y nos echa en cara los pecados contra la ley y "
             "nos reprocha los pecados contra nuestra educación.",
    (2, 13): "Presume de tener conocimiento de Dios, y se llama a sí mismo "
             "hijo del Señor.",
    (2, 14): "Ha venido a ser un reproche de nuestros pensamientos; nos pesa "
             "hasta el verlo,",
    (2, 15): "porque su vida no se parece a la de los demás, y sus senderos "
             "son distintos.",
    (2, 16): "Nos tiene por moneda falsa, y se aparta de nuestros caminos como "
             "de inmundicias; proclama dichoso el fin de los justos, y se "
             "jacta de tener a Dios por padre.",
    (2, 17): "Veamos si sus palabras son verdaderas, y probemos cómo acaba.",
    (2, 18): "Porque si el justo es hijo de Dios, él lo socorrerá y lo librará "
             "de la mano de sus adversarios.",
    (2, 19): "Pongámoslo a prueba con ultraje y tormento, para conocer su "
             "mansedumbre y comprobar su aguante.",
    (2, 20): "Condenémoslo a muerte afrentosa, porque, según sus palabras, "
             "Dios lo visitará».",
    (2, 21): "Así razonaron, y se extraviaron, porque su maldad los cegó,",
    (2, 22): "y no conocieron los secretos de Dios, ni esperaron recompensa "
             "por la santidad, ni estimaron el galardón de las almas sin "
             "tacha.",
    (2, 23): "Porque Dios creó al hombre para la incorrupción, y lo hizo "
             "imagen de su propio ser;",
    (2, 24): "pero por envidia del diablo entró la muerte en el mundo, y la "
             "experimentan los que son de su bando.",

    (3, 1): "Pero las almas de los justos están en la mano de Dios, y no las "
            "tocará tormento alguno.",
    (3, 2): "A los ojos de los insensatos parecieron morir, y se tuvo su "
            "partida por desgracia,",
    (3, 3): "y por ruina el irse de entre nosotros; pero ellos están en paz.",
    (3, 4): "Porque, aunque a la vista de los hombres hayan sido castigados, y "
            "sin honra haya sido al final su vejez,",
    (3, 18): "y si mueren pronto, no tienen esperanza ni consuelo en el día "
             "del juicio;",
    (3, 19): "porque el final de una generación injusta es terrible.",

    (4, 1): "Mejor es no tener hijos y tener virtud, porque en su memoria hay "
            "inmortalidad, ya que es reconocida por Dios y por los hombres.",
    (4, 2): "Cuando está presente la imitan, y cuando se ha ido la añoran; y "
            "en la eternidad desfila coronada, tras vencer en el certamen de "
            "premios sin mancha.",
    (4, 3): "Pero la muchedumbre prolífica de los impíos no servirá de nada, y "
            "de sus retoños bastardos no echará raíz profunda ni asentará base "
            "firme.",
    (4, 4): "Porque, aunque por un tiempo eche ramas y reverdezca, mal "
            "asentada será sacudida por el viento y arrancada de raíz por la "
            "violencia de los vendavales.",
    (4, 5): "Se quebrarán las ramas sin haber madurado, y su fruto será "
            "inservible, verde para comerlo y para nada aprovechable.",
    (4, 6): "Porque los hijos nacidos de uniones ilícitas son testigos de la "
            "maldad de sus padres cuando se los examina.",
    (4, 7): "Pero el justo, aunque muera antes de tiempo, estará en reposo.",
    (4, 8): "Porque la vejez venerable no es la de muchos años, ni se mide por "
            "el número de los años:",
    (4, 9): "las canas del hombre son la prudencia, y la edad de la vejez, una "
            "vida sin mancha.",
    (4, 10): "Agradó a Dios y fue amado, y viviendo entre pecadores fue "
             "trasladado;",
    (4, 11): "fue arrebatado para que la maldad no alterase su entendimiento "
             "ni el engaño sedujese su alma.",
    (4, 12): "Porque el hechizo de la maldad oscurece lo bueno, y el vértigo "
             "del deseo trastorna una mente sin malicia.",
    (4, 13): "Llegado pronto a la perfección, cumplió muchos años.",
    (4, 14): "Porque su alma era grata al Señor; por eso se apresuró a sacarlo "
             "de en medio de la maldad. Y las gentes lo vieron y no lo "
             "entendieron, ni pusieron en su ánimo esta reflexión:",
    (4, 15): "que la gracia y la misericordia son para sus elegidos, y su "
             "cuidado para sus santos.",
    (4, 16): "Y el justo, ya muerto, condenará a los impíos que viven; y una "
             "juventud pronto consumada, a la larga vejez del injusto.",
    (4, 17): "Porque verán el fin del sabio y no entenderán qué determinó Dios "
             "sobre él, ni para qué lo puso a salvo el Señor.",
    (4, 18): "Lo verán y lo despreciarán, pero el Señor se reirá de ellos;",
    (4, 19): "y después de esto serán cadáver sin honra y objeto de ultraje "
             "entre los muertos para siempre; porque los derribará de bruces y "
             "sin habla, y los sacudirá desde los cimientos; y quedarán "
             "asolados hasta el extremo, y estarán en dolor, y su memoria "
             "perecerá.",
    (4, 20): "Vendrán acobardados al recuento de sus pecados, y sus iniquidades "
             "los acusarán cara a cara.",
    (4, 21): "Entonces se pondrá en pie el justo con mucha confianza frente a "
             "los que lo oprimieron",

    (5, 1): "y despreciaron sus fatigas.",
    (5, 2): "Al verlo se turbarán con un miedo terrible, y quedarán atónitos "
            "ante lo inesperado de su salvación;",
    (5, 3): "y dirán entre sí, arrepentidos, y gemirán con angustia de "
            "espíritu: «Éste es aquel de quien un tiempo nos reímos",
    (5, 4): "y a quien pusimos como ejemplo de escarnio, insensatos de "
            "nosotros. Tuvimos su vida por locura y su muerte por deshonra.",
    (5, 5): "¿Cómo es que ha sido contado entre los hijos de Dios, y entre los "
            "santos está su herencia?",
    (5, 6): "Luego nos extraviamos del camino de la verdad, y no nos alumbró "
            "la luz de la justicia, ni salió para nosotros el sol.",
    (5, 7): "Nos hartamos de las sendas de la iniquidad y de la perdición, y "
            "atravesamos desiertos intransitables, pero el camino del Señor no "
            "lo conocimos.",
    (5, 8): "¿De qué nos sirvió la soberbia? ¿Y qué nos ha aportado la riqueza "
            "con toda su jactancia?",
    (5, 9): "Pasó todo aquello como una sombra y como una noticia que corre;",
    (5, 10): "como nave que atraviesa el agua agitada, de cuyo paso no se "
             "puede hallar rastro ni sendero de su quilla entre las olas;",
    (5, 11): "o como de un pájaro que cruza el aire no se encuentra prueba "
             "alguna de su viaje: golpeado por el batir de sus alas y hendido "
             "por la fuerza de su impulso, el aire ligero es atravesado por el "
             "movimiento de las plumas, y después no se halla en él señal de "
             "su paso;",
    (5, 12): "o como, disparada una flecha al blanco, el aire cortado vuelve "
             "en seguida a cerrarse sobre sí mismo, de modo que no se sabe por "
             "dónde pasó.",
    (5, 13): "Así también nosotros: apenas nacidos, dejamos de ser, y no "
             "pudimos mostrar señal alguna de virtud, sino que nos consumimos "
             "en nuestra maldad».",
    (5, 14): "Porque la esperanza del impío es como tamo llevado por el "
             "viento, y como escarcha ligera perseguida por el vendaval, y "
             "como humo que el viento disipa, y pasa como el recuerdo de un "
             "huésped de un solo día.",
    (5, 15): "Pero los justos viven para siempre, y en el Señor está su "
             "recompensa, y el Altísimo cuida de ellos.",
    (5, 16): "Por eso recibirán el reino de la magnificencia y la diadema de "
             "la hermosura de mano del Señor, porque con su diestra los "
             "cubrirá y con su brazo los escudará.",
    (5, 17): "Tomará por armadura su celo, y armará a la creación para "
             "rechazar a sus enemigos.",
    (5, 18): "Se vestirá como coraza la justicia, y se pondrá como yelmo un "
             "juicio sin doblez;",
    (5, 19): "tomará como escudo invencible la santidad,",
    (5, 20): "y afilará como espada su ira inflexible; y el universo peleará "
             "con él contra los insensatos.",
    (5, 21): "Partirán certeros los dardos de los relámpagos, y como de un "
             "arco bien curvado saltarán de las nubes al blanco;",
    (5, 22): "y de la honda de su furor se arrojarán granizos a puñados. Se "
             "indignará contra ellos el agua del mar, y los ríos los anegarán "
             "sin piedad.",
    (5, 23): "Se levantará contra ellos un viento poderoso, y como un vendaval "
             "los aventará; y la iniquidad dejará desierta toda la tierra, y "
             "la maldad derribará los tronos de los poderosos.",

    (6, 1): "Oíd, pues, reyes, y entended; aprended, jueces de los confines de "
            "la tierra;",
    (6, 2): "prestad oído los que domináis multitudes y os gloriáis de "
            "gobernar muchedumbres de naciones.",
    (6, 3): "Porque del Señor os fue dado el mando, y del Altísimo la "
            "soberanía; y él examinará vuestras obras y escudriñará vuestros "
            "designios.",
    (6, 4): "Porque, siendo servidores de su reino, no juzgasteis rectamente "
            "ni guardasteis la ley ni caminasteis según el designio de Dios.",
    (6, 5): "Espantosamente y sin tardanza se presentará ante vosotros, porque "
            "para los que están en alto el juicio es inflexible.",
    (6, 6): "Porque al humilde se le perdona por misericordia, pero los "
            "poderosos serán examinados poderosamente.",
    (6, 7): "Porque el Señor de todos no se retraerá ante nadie ni le impondrá "
            "la grandeza de ninguno, ya que él hizo al pequeño y al grande, y "
            "de todos cuida por igual;",
    (6, 8): "pero a los fuertes les aguarda un examen riguroso.",
    (6, 9): "A vosotros, pues, oh soberanos, van mis palabras, para que "
            "aprendáis sabiduría y no caigáis.",
    (6, 10): "Porque los que guardan santamente las cosas santas serán "
             "santificados, y los que las aprenden hallarán defensa.",
    (6, 11): "Desead, pues, mis palabras; anheladlas, y seréis instruidos.",
    (6, 12): "Espléndida es la sabiduría y no se marchita, y fácilmente la "
             "contemplan los que la aman.",
    (6, 13): "Se adelanta a darse a conocer a los que la desean.",
    (6, 14): "El que madruga por ella no se fatigará, porque la hallará "
             "sentada a su puerta.",
    (6, 15): "Porque meditar en ella es la perfección de la prudencia, y el "
             "que por ella vela quedará pronto libre de inquietud;",
    (6, 16): "porque ella misma va por todas partes buscando a los que son "
             "dignos de ella, y se les muestra benévola en los caminos, y en "
             "todo pensamiento les sale al encuentro.",
    (6, 17): "Porque su principio es el deseo más verdadero de instrucción,",
    (6, 18): "y el cuidado de la instrucción es amor, y el amor es guardar sus "
             "leyes, y atender a sus leyes es la garantía de la incorrupción,",
    (6, 19): "y la incorrupción hace estar cerca de Dios;",
    (6, 20): "así que el deseo de la sabiduría conduce al reino.",
    (6, 21): "Si, pues, os complacéis en tronos y en cetros, soberanos de los "
             "pueblos, honrad la sabiduría, para que reinéis para siempre.",
    (6, 22): "Qué es la sabiduría y cómo llegó a ser, os lo voy a anunciar; y "
             "no os ocultaré sus secretos, sino que la rastrearé desde el "
             "principio de su origen y pondré a la vista su conocimiento, y no "
             "me apartaré de la verdad;",
    (6, 23): "ni haré camino con la envidia consumidora, porque ésa no tiene "
             "parte con la sabiduría.",
    (6, 24): "Una muchedumbre de sabios es la salvación del mundo, y un rey "
             "prudente, la estabilidad del pueblo.",
    (6, 25): "Así que dejaos instruir por mis palabras, y sacaréis provecho.",

    (7, 1): "También yo soy hombre mortal, igual que todos, descendiente del "
            "primer hombre formado de la tierra; y en el vientre de mi madre "
            "fui esculpido como carne",
    (7, 2): "en el espacio de diez meses, cuajado en sangre, de semilla de "
            "varón y del placer que acompaña al sueño.",
    (7, 3): "Y yo, una vez nacido, aspiré el aire común, y caí sobre la tierra "
            "que a todos nos hace iguales, y lo primero que hice fue llorar, "
            "igual que todos.",
    (7, 4): "Fui criado entre pañales y entre cuidados,",
    (7, 5): "porque ningún rey tuvo otro comienzo de su existencia:",
    (7, 6): "una sola es la entrada de todos en la vida, y una misma la "
            "salida.",
    (7, 7): "Por eso oré, y se me dio la prudencia; invoqué, y vino a mí el "
            "espíritu de la sabiduría.",
    (7, 8): "La preferí a cetros y a tronos, y tuve la riqueza por nada en "
            "comparación con ella;",
    (7, 9): "ni le comparé la piedra más preciosa, porque todo el oro, a su "
            "lado, es un puñado de arena, y la plata será tenida por barro "
            "delante de ella.",
    (7, 10): "La amé más que a la salud y a la hermosura, y preferí tenerla a "
             "ella antes que a la luz, porque el resplandor que de ella sale "
             "no duerme.",
    (7, 11): "Y con ella me vinieron a la vez todos los bienes, y en sus manos "
             "una riqueza incontable.",
    (7, 12): "Y me alegré por todo ello, porque la sabiduría los guía; pero "
             "ignoraba que ella es la madre de todo esto.",
    (7, 13): "Sin doblez la aprendí, y sin envidia la comunico; no escondo su "
             "riqueza,",
    (7, 14): "porque es un tesoro inagotable para los hombres, y los que lo "
             "emplearon se granjearon la amistad de Dios, recomendados por los "
             "dones que da la instrucción.",
    (7, 15): "Y a mí concédame Dios hablar conforme a su parecer y pensar de "
             "modo digno de lo que se me ha dado, porque él mismo es guía de "
             "la sabiduría y enderezador de los sabios.",
    (7, 16): "Porque en su mano estamos nosotros y nuestras palabras, y toda "
             "prudencia y toda pericia en el trabajo.",
    (7, 17): "Porque él me dio el conocimiento verdadero de cuanto existe: "
             "conocer la estructura del mundo y la acción de los elementos,",
    (7, 18): "el principio y el fin y el medio de los tiempos, los cambios de "
             "los solsticios y las mudanzas de las estaciones,",
    (7, 19): "los ciclos de los años y las posiciones de los astros,",
    (7, 20): "las naturalezas de los animales y los instintos de las fieras, "
             "la fuerza de los vientos y los razonamientos de los hombres, las "
             "variedades de las plantas y las virtudes de las raíces.",
    (7, 21): "Todo cuanto está oculto y cuanto está a la vista lo conocí,",
    (7, 22): "porque me lo enseñó la sabiduría, artífice de todas las cosas. "
             "Porque hay en ella un espíritu inteligente, santo, único en su "
             "género, múltiple, sutil, ágil, penetrante, sin mancha, claro, "
             "incapaz de dañar, amigo del bien, agudo, libre, bienhechor,",
    (7, 23): "amigo de los hombres, firme, seguro, sin inquietud, todopoderoso "
             "y que todo lo vigila, y que penetra todos los espíritus "
             "inteligentes, puros y sutilísimos.",
    (7, 24): "Porque la sabiduría es más ágil que todo movimiento, y por su "
             "pureza lo atraviesa y lo penetra todo.",
    (7, 25): "Porque es un hálito del poder de Dios y una emanación pura de la "
             "gloria del Todopoderoso; por eso nada manchado se abre paso "
             "hasta ella.",
    (7, 26): "Porque es resplandor de la luz eterna, y espejo sin mancha de la "
             "actividad de Dios, e imagen de su bondad.",
    (7, 27): "Y siendo una sola, todo lo puede; y permaneciendo en sí misma, "
             "todo lo renueva; y de generación en generación, pasando a las "
             "almas santas, va formando amigos de Dios y profetas,",
    (7, 28): "porque Dios no ama a nadie sino al que convive con la sabiduría.",
    (7, 29): "Porque ella es más hermosa que el sol y supera a toda "
             "constelación de estrellas; comparada con la luz, sale ganando,",
    (7, 30): "pues a ésta la sucede la noche, mientras que a la sabiduría no "
             "la vence la maldad.",

    (8, 1): "Se extiende con vigor de un extremo a otro, y todo lo gobierna "
            "con acierto.",
    (8, 2): "A ésta amé y busqué desde mi juventud, y pretendí tomarla por "
            "esposa, y me enamoré de su hermosura.",
    (8, 3): "Ella hace ilustre su linaje por convivir con Dios, y el Señor de "
            "todas las cosas la amó;",
    (8, 4): "porque está iniciada en la ciencia de Dios y elige sus obras.",
    (8, 5): "Y si la riqueza es un bien deseable en esta vida, ¿qué hay más "
            "rico que la sabiduría, que todo lo hace?",
    (8, 6): "Y si la prudencia obra, ¿quién es más que ella artífice de cuanto "
            "existe?",
    (8, 7): "Y si alguien ama la justicia, sus trabajos son las virtudes: "
            "porque ella enseña templanza y prudencia, justicia y fortaleza, "
            "de las que nada hay más provechoso en la vida para los hombres.",
    (8, 8): "Y si alguien anhela mucha experiencia, ella conoce lo pasado y "
            "conjetura lo por venir, entiende los giros de las palabras y la "
            "solución de los enigmas, prevé señales y prodigios y el desenlace "
            "de las épocas y de los tiempos.",
    (8, 9): "Decidí, pues, tomarla por compañera de mi vida, sabiendo que "
            "sería para mí consejera en el bien y aliento en las "
            "preocupaciones y en la tristeza.",
    (8, 10): "Por ella tendré gloria entre las multitudes, y honra ante los "
             "ancianos siendo joven;",
    (8, 11): "seré hallado agudo en el juicio, y ante los poderosos seré "
             "admirado.",
    (8, 12): "Cuando calle, me esperarán; cuando hable, me atenderán; y si me "
             "alargo hablando, se pondrán la mano en la boca.",
    (8, 13): "Por ella alcanzaré la inmortalidad, y dejaré memoria eterna a "
             "los que vengan después de mí.",
    (8, 14): "Gobernaré pueblos, y me estarán sometidas naciones;",
    (8, 15): "me temerán al oírme soberanos terribles; entre la multitud me "
             "mostraré bueno, y en la guerra, valiente.",
    (8, 16): "Cuando entre en mi casa, descansaré junto a ella, porque su "
             "trato no tiene amargura, ni dolor su convivencia, sino alegría y "
             "gozo.",
    (8, 17): "Pensando yo esto conmigo mismo y meditando en mi corazón que hay "
             "inmortalidad en el parentesco con la sabiduría,",
    (8, 18): "y en su amistad un deleite bueno, y en los trabajos de sus manos "
             "riqueza inagotable, y prudencia en el ejercicio de su trato, y "
             "buena fama en compartir sus palabras, andaba buscando el modo de "
             "tomarla para mí.",
    (8, 19): "Era yo un muchacho de buen natural, y me tocó en suerte un alma "
             "buena;",
    (8, 20): "o más bien, siendo bueno, vine a un cuerpo sin mancha.",
    (8, 21): "Y comprendiendo que de otro modo no la poseería si Dios no me la "
             "daba —y ya era propio de la prudencia saber de quién viene ese "
             "don—, acudí al Señor y le supliqué, y dije con todo mi corazón:",

    (9, 1): "«Dios de los padres y Señor de la misericordia, que hiciste todas "
            "las cosas con tu palabra,",
    (9, 2): "y con tu sabiduría formaste al hombre para que dominase sobre las "
            "criaturas hechas por ti,",
    (9, 3): "y rigiese el mundo con santidad y justicia, y juzgase con "
            "rectitud de alma:",
    (9, 4): "dame la sabiduría, que se sienta junto a tu trono, y no me "
            "excluyas del número de tus hijos.",
    (9, 5): "Porque yo soy siervo tuyo e hijo de tu sierva, hombre débil y de "
            "pocos días, y falto de inteligencia para el juicio y para las "
            "leyes.",
    (9, 6): "Porque, aunque uno sea perfecto entre los hijos de los hombres, "
            "si le falta la sabiduría que viene de ti, será tenido por nada.",
    (9, 7): "Tú me escogiste por rey de tu pueblo y por juez de tus hijos y de "
            "tus hijas;",
    (9, 8): "me dijiste que edificase un templo en tu monte santo, y un altar "
            "en la ciudad donde moras, copia de la tienda santa que preparaste "
            "desde el principio.",
    (9, 9): "Y contigo está la sabiduría, que conoce tus obras y estaba "
            "presente cuando hacías el mundo, y sabe lo que es grato a tus "
            "ojos y lo que es recto según tus mandamientos.",
    (9, 10): "Envíala desde los cielos santos, y mándala desde el trono de tu "
             "gloria, para que esté conmigo y trabaje a mi lado, y sepa yo qué "
             "es lo que te agrada.",
    (9, 11): "Porque ella lo sabe todo y lo entiende, y me guiará con acierto "
             "en mis acciones y me guardará con su gloria;",
    (9, 12): "y serán aceptas mis obras, y juzgaré con justicia a tu pueblo, y "
             "seré digno del trono de mi padre.",
    (9, 13): "Porque ¿qué hombre podrá conocer el designio de Dios, o quién "
             "podrá imaginar qué quiere el Señor?",
    (9, 14): "Porque los razonamientos de los mortales son tímidos, y "
             "vacilantes nuestras ideas;",
    (9, 15): "porque el cuerpo corruptible agobia el alma, y la tienda "
             "terrena oprime la mente cargada de cuidados.",
    (9, 16): "Y a duras penas conjeturamos las cosas de la tierra, y con "
             "trabajo hallamos lo que tenemos entre manos; ¿quién ha "
             "rastreado, pues, lo que está en los cielos?",
    (9, 17): "¿Y quién habría conocido tu voluntad si tú no hubieses dado la "
             "sabiduría y enviado desde lo alto tu santo espíritu?",
    (9, 18): "Así fueron enderezados los senderos de los que están en la "
             "tierra, y aprendieron los hombres lo que a ti te agrada,",
    (9, 19): "y por la sabiduría fueron salvados».",

    (10, 1): "Ella guardó al padre del mundo, primer hombre formado y creado "
             "solo, y lo libró de su propia caída,",
    (10, 2): "y le dio fuerza para dominarlo todo.",
    (10, 3): "Pero el injusto, apartándose de ella en su ira, pereció con los "
             "furores de su fratricidio.",
    (10, 4): "Cuando por su causa la tierra fue anegada, la sabiduría volvió a "
             "salvarla, guiando al justo en un madero de poco valor.",
    (10, 5): "Ella también, cuando las naciones se confundieron por acuerdo en "
             "la maldad, halló al justo y lo conservó irreprensible ante Dios, "
             "y lo mantuvo firme frente al amor entrañable por su hijo.",
    (10, 6): "Ella libró al justo cuando perecían los impíos, haciéndolo huir "
             "del fuego que cayó sobre las Cinco Ciudades;",
    (10, 7): "de cuya maldad queda todavía por testimonio una tierra yerma y "
             "humeante, y plantas que dan fruto que no llega a sazón, y, como "
             "recuerdo de un alma incrédula, una estatua de sal que sigue en "
             "pie.",
    (10, 8): "Porque los que dejaron de lado la sabiduría no sólo se "
             "perjudicaron al no conocer el bien, sino que dejaron a la "
             "posteridad un recuerdo de su insensatez, para que ni siquiera "
             "aquello en que fallaron pudiera quedar oculto.",
    (10, 9): "Pero la sabiduría libró de sus fatigas a los que la sirvieron.",
    (10, 10): "Ella guió por sendas derechas al justo que huía de la ira de su "
              "hermano; le mostró el reino de Dios y le dio conocimiento de "
              "cosas santas; lo enriqueció en sus trabajos y multiplicó el "
              "fruto de sus esfuerzos.",
    (10, 11): "Cuando lo oprimían con codicia, estuvo a su lado y lo hizo "
              "rico;",
    (10, 12): "lo guardó de sus enemigos y lo puso a salvo de los que lo "
              "acechaban, y le concedió la victoria en una lucha reñida, para "
              "que supiese que la piedad es más poderosa que todo.",
    (10, 13): "Ella no abandonó al justo cuando fue vendido, sino que lo libró "
              "del pecado;",
    (10, 14): "bajó con él a la cisterna y no lo dejó en las cadenas, hasta "
              "que le trajo el cetro del reino y autoridad sobre los que lo "
              "tiranizaban; y mostró que eran mentirosos los que lo habían "
              "difamado, y le dio gloria eterna.",
    (10, 15): "Ella libró a un pueblo santo y a una descendencia irreprensible "
              "de una nación que los oprimía.",
    (10, 16): "Entró en el alma de un siervo del Señor, y se enfrentó a reyes "
              "temibles con prodigios y señales.",
    (10, 17): "Dio a los santos el salario de sus fatigas, los guió por un "
              "camino admirable, y fue para ellos sombra de día y luz de "
              "estrellas por la noche.",
    (10, 18): "Les hizo pasar el mar Rojo y los condujo a través de muchas "
              "aguas;",
    (10, 19): "y a sus enemigos los anegó, y los arrojó a la superficie desde "
              "el fondo del abismo.",
    (10, 20): "Por eso los justos despojaron a los impíos, y cantaron himnos, "
              "Señor, a tu santo nombre, y alabaron a una tu mano que peleaba "
              "por ellos;",
    (10, 21): "porque la sabiduría abrió la boca de los mudos e hizo elocuentes "
              "las lenguas de los niños.",

    (11, 1): "Ella hizo prosperar sus obras por mano de un profeta santo.",
    (11, 2): "Atravesaron un desierto inhabitado, y plantaron sus tiendas en "
             "lugares intransitables;",
    (11, 3): "se enfrentaron a sus adversarios y rechazaron a sus enemigos.",
    (11, 4): "Tuvieron sed y te invocaron, y se les dio agua de una roca "
             "cortada a pico, y remedio de la sed de una piedra dura.",
    (11, 5): "Porque aquello mismo con que fueron castigados sus enemigos les "
             "sirvió a ellos de beneficio en su necesidad.",
    (11, 6): "En lugar de la fuente de un río perenne, turbada con sangre "
             "cuajada",
    (11, 7): "en castigo del decreto que mandaba matar a los niños,",
    (11, 8): "les diste a ellos agua abundante cuando no la esperaban, "
             "mostrando con aquella sed cómo habías castigado a sus "
             "adversarios.",
    (11, 9): "Porque cuando fueron probados, aunque corregidos con "
             "misericordia, conocieron cómo eran atormentados los impíos, "
             "juzgados con ira.",
    (11, 10): "Porque a éstos los probaste como padre que amonesta, mientras "
              "que a aquéllos los examinaste como rey severo que condena.",
    (11, 11): "Y lejos o cerca, unos y otros eran igualmente afligidos,",
    (11, 12): "porque los alcanzó una doble pena y el gemido del recuerdo de "
              "lo pasado.",
    (11, 13): "Porque cuando oyeron que por medio de sus propios castigos "
              "aquéllos recibían beneficio, percibieron al Señor.",
    (11, 14): "Pues a aquel que antes habían expuesto y arrojado, y de quien "
              "se burlaron rechazándolo, lo admiraron al final de los "
              "acontecimientos, después de haber pasado una sed muy distinta "
              "de la de los justos.",
    (11, 15): "Y en pago de los razonamientos insensatos de su injusticia, con "
              "los que, extraviados, daban culto a reptiles sin razón y a "
              "bichos despreciables, les enviaste una multitud de animales "
              "irracionales como castigo,",
    (11, 16): "para que supieran que con aquello mismo con que uno peca, con "
              "eso es castigado.",
    (11, 17): "Porque no le faltaba a tu mano todopoderosa —que creó el mundo "
              "de una materia informe— con qué enviarles una multitud de osos "
              "o leones feroces,",
    (11, 18): "o fieras desconocidas, recién creadas y llenas de furia, que "
              "echasen resoplidos de fuego, o despidiesen rugidos de humo, o "
              "lanzasen de los ojos chispas terribles,",
    (11, 19): "y que no sólo con su daño podían destrozarlos, sino que con su "
              "sola vista, de espanto, los habrían matado.",
    (11, 20): "Y aun sin todo esto podían haber caído de un solo soplo, "
              "perseguidos por la justicia y aventados por el aliento de tu "
              "poder; pero tú todo lo dispusiste con medida, número y peso.",
    (11, 21): "Porque el poder desplegar una gran fuerza lo tienes siempre a "
              "tu alcance, ¿y quién resistirá al poder de tu brazo?",
    (11, 22): "Porque el mundo entero es delante de ti como el grano que "
              "inclina la balanza, y como gota de rocío mañanero que cae sobre "
              "la tierra.",
    (11, 23): "Pero te compadeces de todos, porque todo lo puedes, y pasas por "
              "alto los pecados de los hombres para que se arrepientan.",
    (11, 24): "Porque amas todo cuanto existe, y no aborreces nada de lo que "
              "hiciste, pues, si algo odiaras, no lo habrías formado.",
    (11, 25): "¿Y cómo subsistiría algo si tú no lo quisieras, o cómo se "
              "conservaría lo que tú no hubieses llamado?",
    (11, 26): "Pero de todo tienes piedad, porque todo es tuyo, Señor amigo de "
              "la vida.",

    (12, 1): "Porque tu espíritu incorruptible está en todas las cosas.",
    (12, 2): "Por eso corriges poco a poco a los que caen, y los amonestas "
             "recordándoles en qué pecan, para que, apartados de la maldad, "
             "crean en ti, Señor.",
    (12, 3): "Porque también a los antiguos habitantes de tu tierra santa,",
    (12, 4): "aborreciéndolos por practicar obras odiosísimas —hechicerías y "
             "ritos impíos,",
    (12, 5): "asesinos despiadados de niños, devoradores de entrañas en "
             "banquetes de carne y sangre humanas, iniciados en medio de "
             "cofradías,",
    (12, 6): "padres que con sus propias manos mataban a seres indefensos—, "
             "quisiste destruirlos por mano de nuestros padres,",
    (12, 7): "para que recibiera colonos dignos, hijos de Dios, la tierra que "
             "es para ti la más preciada de todas.",
    (12, 8): "Pero aun a ésos, por ser hombres, los perdonaste; y enviaste "
             "avispas como avanzada de tu ejército, para que los fueran "
             "exterminando poco a poco.",
    (12, 9): "No es que te faltase poder para entregar en batalla a los impíos "
             "en manos de los justos, o para aniquilarlos de una vez con "
             "fieras terribles o con una palabra tajante;",
    (12, 10): "pero, juzgando poco a poco, dabas lugar al arrepentimiento, "
              "aunque no ignorabas que su origen era malo y su maldad "
              "connatural, y que su modo de pensar no cambiaría jamás,",
    (12, 11): "porque era una descendencia maldita desde el principio; y no "
              "por temor a nadie dejabas impune lo que hacían.",
    (12, 12): "Porque ¿quién te dirá: «Qué has hecho»? ¿O quién se opondrá a "
              "tu sentencia? ¿Y quién te pedirá cuentas por las naciones que "
              "has destruido y que tú hiciste? ¿O quién comparecerá ante ti "
              "como vengador de hombres injustos?",
    (12, 13): "Porque no hay Dios fuera de ti, que cuides de todas las cosas, "
              "ante quien hubieras de probar que no juzgaste injustamente;",
    (12, 14): "ni habrá rey ni soberano que pueda mirarte cara a cara por "
              "aquellos a quienes castigaste.",
    (12, 15): "Y siendo justo, gobiernas todas las cosas con justicia, "
              "teniendo por ajeno a tu poder condenar al que no merece "
              "castigo.",
    (12, 16): "Porque tu fuerza es el principio de la justicia, y el ser "
              "dueño de todo te hace perdonarlo todo.",
    (12, 17): "Porque muestras tu fuerza cuando no se cree en la plenitud de "
              "tu poder, y en los que la conocen dejas en evidencia la "
              "insolencia;",
    (12, 18): "pero tú, dueño de la fuerza, juzgas con indulgencia y nos "
              "gobiernas con mucho miramiento, porque tienes el poder a mano "
              "siempre que quieras.",
    (12, 19): "Y con tales obras enseñaste a tu pueblo que el justo ha de ser "
              "amigo de los hombres; y llenaste de buena esperanza a tus "
              "hijos, porque das lugar al arrepentimiento en los pecados.",
    (12, 20): "Porque si a los enemigos de tus hijos, reos de muerte, los "
              "castigaste con tanto miramiento y contemplación, dándoles "
              "tiempo y ocasión para apartarse de la maldad,",
    (12, 21): "¡con cuánta mayor consideración habrás juzgado a tus hijos, a "
              "cuyos padres diste juramentos y alianzas de promesas "
              "favorables!",
    (12, 22): "Así que, mientras nos corriges a nosotros, a nuestros enemigos "
              "los azotas mil veces, para que, al juzgar, tengamos presente tu "
              "bondad, y, al ser juzgados, esperemos misericordia.",
    (12, 23): "Por eso también a los injustos que vivieron una vida "
              "insensata los atormentaste con sus propias abominaciones.",
    (12, 24): "Porque se extraviaron más allá de todos los caminos del "
              "extravío, tomando por dioses a los animales más viles aun entre "
              "los de sus enemigos, engañados como niños sin juicio.",
    (12, 25): "Por eso, como a niños sin razón, les mandaste un castigo "
              "ridículo;",
    (12, 26): "pero los que no se dejan corregir por una reprensión de burlas "
              "conocerán un juicio digno de Dios.",
    (12, 27): "Porque, indignándose por lo que padecían a manos de aquellos "
              "mismos a quienes tenían por dioses, al ser castigados con "
              "ellos, vieron y reconocieron como Dios verdadero a aquel a "
              "quien antes se negaban a conocer; y por eso vino sobre ellos el "
              "colmo de la condenación.",

    (13, 1): "Vanos por naturaleza son todos los hombres en quienes había "
             "ignorancia de Dios, y que por los bienes visibles no fueron "
             "capaces de conocer al que es, ni, atendiendo a las obras, "
             "reconocieron al artífice;",
    (13, 2): "sino que tuvieron por dioses al fuego, o al viento, o al aire "
             "veloz, o a la bóveda de las estrellas, o al agua impetuosa, o a "
             "las lumbreras del cielo, que gobiernan el mundo.",
    (13, 3): "Si, cautivados por su hermosura, los tomaron por dioses, sepan "
             "cuánto mejor es el dueño de todos ellos, porque el autor de la "
             "belleza fue quien los creó.",
    (13, 4): "Y si quedaron asombrados por su fuerza y su energía, entiendan "
             "por ellos cuánto más poderoso es el que los formó;",
    (13, 5): "porque por la grandeza y la hermosura de las criaturas se "
             "contempla, por analogía, a su Hacedor.",
    (13, 6): "Y con todo, éstos merecen poco reproche, porque acaso se "
             "extravían buscando a Dios y queriendo encontrarlo;",
    (13, 7): "porque, viviendo entre sus obras, las escudriñan, y se dejan "
             "convencer por lo que ven, porque es hermoso lo que se ve.",
    (13, 8): "Pero tampoco ellos son excusables,",
    (13, 9): "porque, si fueron capaces de saber tanto como para poder "
             "escrutar el universo, ¿cómo no encontraron antes al dueño de "
             "todo eso?",
    (13, 10): "Desdichados, en cambio, y con la esperanza puesta en cosas "
              "muertas, los que llamaron dioses a obras de manos de hombres: "
              "oro y plata, labor de arte, y figuras de animales, o una piedra "
              "inútil, obra de una mano antigua.",
    (13, 11): "Ahí tienes a un leñador carpintero: sierra un árbol fácil de "
              "manejar, le raspa diestramente toda la corteza y, trabajándolo "
              "con arte, fabrica un utensilio útil para el servicio de la "
              "vida;",
    (13, 12): "y con los desperdicios del trabajo cocina su comida y se harta.",
    (13, 13): "Pero de esos desperdicios queda uno que no sirve para nada, un "
              "leño torcido y lleno de nudos: lo toma y lo talla en sus ratos "
              "de ocio, y con la pericia de sus descansos le da forma, y lo "
              "hace semejante a la figura de un hombre,",
    (13, 14): "o lo asemeja a algún animal despreciable, y lo embadurna de "
              "bermellón y le enrojece la superficie con afeite, y le tapa con "
              "pintura toda mancha;",
    (13, 15): "y haciéndole una habitación digna de él, lo coloca en la pared "
              "asegurándolo con un hierro.",
    (13, 16): "Así se cuida de que no se le caiga, sabiendo que es incapaz de "
              "valerse a sí mismo, porque no pasa de ser una imagen y necesita "
              "ayuda.",
    (13, 17): "Y al orar por sus bienes y por su matrimonio y por sus hijos no "
              "se avergüenza de dirigir la palabra a una cosa sin vida; y para "
              "la salud invoca a lo que es débil,",
    (13, 18): "y para la vida ruega a lo que está muerto, y para el socorro "
              "suplica a lo más inexperto, y para el viaje a lo que ni siquiera "
              "puede servirse de sus pies;",
    (13, 19): "y para las ganancias y el trabajo y el buen éxito de sus manos "
              "pide vigor a lo que no tiene manos con que valerse.",

    (14, 1): "Otro, dispuesto a navegar y a punto de cruzar olas salvajes, "
             "clama a un leño más frágil que la nave que lo lleva.",
    (14, 2): "Porque a ésta la ideó el afán de ganancia, y la fabricó la "
             "sabiduría como artífice;",
    (14, 3): "pero es tu providencia, Padre, la que la gobierna, porque "
             "también en el mar abriste camino y senda segura entre las olas,",
    (14, 4): "mostrando que puedes salvar de todo, aunque alguien se embarque "
             "sin pericia.",
    (14, 5): "Pero no quieres que queden ociosas las obras de tu sabiduría; "
             "por eso los hombres confían su vida a un leño mínimo, y "
             "atravesando el oleaje en una balsa se salvan.",
    (14, 6): "Porque también al principio, cuando perecían los gigantes "
             "soberbios, la esperanza del mundo se refugió en una balsa y dejó "
             "al mundo una semilla de generación, gobernada por tu mano.",
    (14, 7): "Porque bendito es el leño por el que viene la justicia;",
    (14, 8): "pero el ídolo hecho a mano es maldito, él y el que lo hizo: "
             "éste, por haberlo fabricado; aquél, porque, siendo corruptible, "
             "fue llamado dios.",
    (14, 9): "Porque igualmente aborrecibles son para Dios el impío y su "
             "impiedad,",
    (14, 10): "y lo hecho será castigado junto con el que lo hizo.",
    (14, 11): "Por eso habrá también un juicio sobre los ídolos de las "
              "naciones, porque, siendo criaturas de Dios, se han convertido "
              "en abominación y en tropiezo para las almas de los hombres y en "
              "lazo para los pies de los insensatos.",
    (14, 12): "Porque el principio de la fornicación es la invención de los "
              "ídolos, y su hallazgo, la corrupción de la vida.",
    (14, 13): "Porque ni existieron desde el principio ni existirán para "
              "siempre;",
    (14, 14): "pues entraron en el mundo por la vanidad de los hombres, y por "
              "eso se les tiene reservado un final rápido.",
    (14, 15): "Porque un padre, consumido por un duelo prematuro, hizo una "
              "imagen del hijo que le habían arrebatado tan pronto, y al que "
              "entonces era un hombre muerto empezó a honrarlo ahora como a un "
              "dios, y transmitió a los suyos ritos y ceremonias;",
    (14, 16): "luego, afianzada con el tiempo, aquella costumbre impía se "
              "guardó como ley, y por mandato de los soberanos se daba culto a "
              "las imágenes talladas.",
    (14, 17): "A los que los hombres no podían honrar de vista, por vivir "
              "lejos, los reprodujeron según su aspecto distante, e hicieron "
              "una imagen visible del rey al que honraban, para adular con "
              "diligencia al ausente como si estuviera presente.",
    (14, 18): "Y a intensificar el culto, incluso entre los que no lo "
              "conocían, empujó el afán de gloria del artista.",
    (14, 19): "Porque éste, queriendo tal vez agradar al que manda, forzó con "
              "su arte el parecido hacia lo más hermoso;",
    (14, 20): "y la multitud, atraída por la gracia de la obra, tuvo por "
              "objeto de adoración al que poco antes era un hombre honrado.",
    (14, 21): "Y esto vino a ser una emboscada para la vida, porque los "
              "hombres, esclavizados por la desgracia o por la tiranía, "
              "pusieron a piedras y a maderos el nombre incomunicable.",
    (14, 22): "Y no les bastó errar en el conocimiento de Dios, sino que, "
              "viviendo en la gran guerra de la ignorancia, llaman paz a tan "
              "grandes males.",
    (14, 23): "Porque, celebrando ritos que matan a los hijos, o misterios "
              "secretos, o comparsas enloquecidas de costumbres extrañas,",
    (14, 24): "ya no guardan puras ni la vida ni el matrimonio, sino que uno "
              "mata a otro a traición, o lo hace sufrir con el adulterio.",
    (14, 25): "Y todo anda mezclado: sangre y asesinato, robo y engaño, "
              "corrupción, deslealtad, desorden, perjurio, trastorno de lo "
              "bueno,",
    (14, 26): "olvido de los favores, contaminación de las almas, perversión "
              "de la naturaleza, desconcierto en los matrimonios, adulterio y "
              "libertinaje.",
    (14, 27): "Porque el culto de los ídolos sin nombre es principio y causa y "
              "término de todo mal;",
    (14, 28): "porque, o bien se enloquecen en sus fiestas, o profetizan "
              "mentiras, o viven injustamente, o perjuran sin reparo;",
    (14, 29): "pues, como confían en ídolos sin vida, no temen sufrir daño "
              "alguno por haber jurado en falso.",
    (14, 30): "Pero por ambas cosas les alcanzará la justicia: porque "
              "pensaron mal de Dios al entregarse a los ídolos, y porque "
              "juraron injustamente y con engaño, despreciando la santidad.",
    (14, 31): "Porque no es el poder de aquello por lo que se jura, sino la "
              "justicia debida a los que pecan, la que persigue siempre la "
              "transgresión de los injustos.",

    (16, 1): "Pero tú, Dios nuestro, eres bueno y veraz, paciente, y con "
             "misericordia lo gobiernas todo.",
    (16, 2): "Porque, aunque pequemos, tuyos somos, pues conocemos tu poder; "
             "pero no pecaremos, sabiendo que somos contados por tuyos.",
    (16, 3): "Porque conocerte a ti es la justicia entera, y saber de tu poder "
             "es la raíz de la inmortalidad.",
    (16, 4): "Porque no nos extravió la invención malintencionada de los "
             "hombres, ni el trabajo estéril de los pintores de sombras, una "
             "figura embadurnada de colores diversos,",
    (16, 5): "cuya vista lleva a los insensatos al deseo, y suspiran por la "
             "figura sin aliento de una imagen muerta.",
    (16, 6): "Amantes del mal y dignos de tales esperanzas son los que las "
             "hacen y los que las desean y los que las veneran.",
    (16, 7): "Porque también el alfarero, amasando con fatiga la tierra "
             "blanda, modela cada objeto para nuestro servicio; pero del mismo "
             "barro forma tanto las vasijas destinadas a usos limpios como las "
             "contrarias, todas igual; y cuál sea el uso de cada una, lo "
             "decide el que trabaja el barro.",
    (16, 8): "Y con mal esfuerzo modela del mismo barro un dios vano quien, "
             "hecho hace poco de la tierra, dentro de poco volverá a aquella "
             "de donde fue tomado, cuando se le reclame la deuda del alma.",
    (16, 9): "Pero a él no le preocupa que vaya a morir ni que tenga una vida "
             "corta, sino que compite con los orfebres y con los plateros e "
             "imita a los broncistas, y tiene por gloria modelar cosas falsas.",
    (16, 10): "Ceniza es su corazón, y su esperanza más vil que la tierra, y "
              "su vida más despreciable que el barro,",
    (16, 11): "porque no reconoció al que lo modeló y le infundió un alma que "
              "obra, y le sopló un espíritu de vida;",
    (16, 12): "sino que tuvo nuestra vida por un juego y la existencia por una "
              "feria de ganancias, porque —dice— hay que sacar provecho de "
              "donde sea, aunque sea del mal.",
    (16, 13): "Porque éste sabe, más que ninguno, que peca, cuando fabrica de "
              "materia terrena vasijas quebradizas e imágenes talladas.",
    (16, 14): "Pero los más insensatos de todos y más desdichados que el alma "
              "de un niño son los enemigos de tu pueblo, los que lo "
              "oprimieron,",
    (16, 15): "porque tuvieron por dioses a todos los ídolos de las naciones, "
              "que no tienen ojos que sirvan para ver, ni narices para aspirar "
              "el aire, ni oídos para oír, ni dedos en las manos para palpar, "
              "y sus pies son inútiles para andar.",
    (16, 16): "Porque los hizo un hombre, y los modeló uno que tiene el "
              "aliento prestado; porque ningún hombre es capaz de modelar un "
              "dios semejante a sí mismo.",
    (16, 17): "Siendo mortal, hace una cosa muerta con manos impías; porque él "
              "vale más que aquello que venera, ya que él, al menos, vivió, y "
              "aquellas cosas nunca.",
    (16, 18): "Y hasta veneran a los animales más odiosos, que son peores que "
              "los demás cuando se los compara por su falta de razón;",
    (16, 19): "y ni siquiera son hermosos, como puede serlo un animal, para "
              "que se los desee; y se han quedado sin la alabanza de Dios y "
              "sin su bendición […].",

    (17, 1): "Por eso fueron castigados con toda razón por medio de seres "
             "semejantes, y atormentados con una multitud de bichos.",
    (17, 2): "En lugar de aquel castigo, favoreciste a tu pueblo, y para "
             "satisfacer su apetito le preparaste como alimento un manjar "
             "extraño: codornices,",
    (17, 3): "para que aquéllos, aun deseando comer, sintiesen asco por el "
             "aspecto repugnante de los animales que les habías enviado, "
             "mientras que éstos, después de pasar poco tiempo de escasez, "
             "gustaran de un manjar extraordinario.",
    (17, 4): "Porque era preciso que a aquellos tiranos les sobreviniese una "
             "escasez ineludible, y que a éstos sólo se les mostrase cómo eran "
             "atormentados sus enemigos.",
    (17, 5): "Porque, aun cuando vino sobre ellos el furor terrible de las "
             "fieras y perecían por las mordeduras de serpientes tortuosas, tu "
             "ira no duró hasta el fin;",
    (17, 6): "por vía de corrección fueron turbados por poco tiempo, teniendo "
             "una señal de salvación para recordarles el mandamiento de tu "
             "ley.",
    (17, 7): "Porque el que se volvía hacia ella no se salvaba por lo que "
             "veía, sino por ti, salvador de todos.",
    (17, 8): "Y con esto convenciste también a nuestros enemigos de que tú "
             "eres el que libra de todo mal.",
    (17, 9): "Porque a aquéllos los mataron picaduras de langostas y de "
             "moscas, y no se halló remedio para su vida, porque merecían ser "
             "castigados con tales cosas;",
    (17, 10): "pero a tus hijos ni los dientes de serpientes venenosas los "
              "vencieron, porque tu misericordia salió a su encuentro y los "
              "sanó.",
    (17, 11): "Porque eran aguijoneados para que se acordasen de tus palabras, "
              "y en seguida eran curados, para que no cayesen en un olvido "
              "profundo y quedasen sin atención a tu beneficio.",
    (17, 12): "Porque ni hierba ni emplasto los curó, sino tu palabra, Señor, "
              "que todo lo sana.",
    (17, 13): "Porque tú tienes potestad sobre la vida y la muerte, y haces "
              "bajar a las puertas del Hades y volver a subir.",
    (17, 14): "El hombre, en cambio, mata con su maldad, pero no hace volver "
              "el espíritu que salió, ni suelta el alma que ha sido tomada.",
    (17, 15): "Pero huir de tu mano es imposible.",
    (17, 16): "Porque los impíos, que se negaban a conocerte, fueron azotados "
              "por la fuerza de tu brazo, perseguidos por lluvias extrañas y "
              "granizos y aguaceros implacables, y consumidos por el fuego.",
    (17, 17): "Porque lo más asombroso es que en el agua, que todo lo apaga, "
              "el fuego actuaba con más fuerza; porque el universo pelea a "
              "favor de los justos.",
    (17, 18): "Porque a veces la llama se amansaba, para no abrasar a los "
              "animales enviados contra los impíos, y para que ellos, "
              "viéndolo, supieran que eran perseguidos por juicio de Dios;",
    (17, 19): "y a veces, en medio del agua, ardía por encima de la fuerza del "
              "fuego, para destruir los frutos de una tierra injusta.",
    (17, 20): "En cambio a tu pueblo lo alimentaste con manjar de ángeles, y "
              "les enviaste desde el cielo, sin trabajo alguno, un pan ya "
              "preparado, capaz de dar todo deleite y de acomodarse a todos "
              "los gustos.",
    (17, 21): "Porque aquel sustento tuyo manifestaba tu dulzura para con tus "
              "hijos, y, sirviendo al deseo del que lo tomaba, se transformaba "
              "en lo que cada uno quería.",
    (17, 22): "Y la nieve y el hielo resistían el fuego y no se derretían, "
              "para que supieran que el fuego que ardía en el granizo y "
              "relampagueaba en los aguaceros destruía los frutos de sus "
              "enemigos;",
    (17, 23): "y en cambio, para que se alimentasen los justos, ese mismo "
              "fuego olvidaba su propia fuerza.",
    (17, 24): "Porque la creación, que te sirve a ti que la hiciste, redobla "
              "su fuerza para castigar a los injustos y la modera para hacer "
              "bien a los que confían en ti.",
    (17, 25): "Por eso también entonces, transformándose en todas las cosas, "
              "servía a tu don que a todos alimenta, conforme a la voluntad de "
              "los que lo necesitaban,",
    (17, 26): "para que tus hijos, a quienes amaste, Señor, aprendieran que no "
              "son las distintas clases de frutos las que alimentan al hombre, "
              "sino que tu palabra es la que conserva a los que creen en ti.",
    (17, 27): "Porque aquello que el fuego no destruía, con sólo calentarse al "
              "breve rayo del sol se derretía,",
    (17, 28): "para que se supiera que hay que adelantarse al sol para darte "
              "gracias, y acudir a ti al despuntar la luz.",
    (17, 29): "Porque la esperanza del desagradecido se derretirá como "
              "escarcha de invierno, y correrá como agua inservible.",

    (18, 1): "Porque grandes son tus juicios y difíciles de explicar; por eso "
             "las almas sin instrucción se extraviaron.",
    (18, 2): "Porque los inicuos, que se creían capaces de oprimir a una "
             "nación santa, quedaron prisioneros de las tinieblas y "
             "encadenados a una larga noche, encerrados bajo sus techos, "
             "desterrados de la providencia eterna.",
    (18, 3): "Porque, pensando que quedaban ocultos en sus pecados secretos, "
             "fueron dispersados bajo el velo sin luz del olvido, presa de un "
             "espanto terrible y aterrados por las apariciones.",
    (18, 4): "Porque ni el rincón donde se escondían los guardaba del miedo, "
             "sino que resonaban en torno a ellos ruidos que los sobresaltaban, "
             "y se les aparecían fantasmas lúgubres de rostro sin sonrisa.",
    (18, 5): "Y ninguna fuerza del fuego lograba alumbrar, ni las llamas "
             "brillantes de los astros conseguían iluminar aquella noche "
             "siniestra.",
    (18, 6): "Sólo les aparecía una hoguera encendida por sí sola, llena de "
             "espanto; y aterrados por aquella visión que apenas veían, tenían "
             "por peor lo que sí alcanzaban a ver.",
    (18, 7): "Y las burlas del arte mágico yacían por tierra, y la jactancia "
             "de su sabiduría quedaba en vergonzosa evidencia;",
    (18, 8): "porque los que prometían expulsar los terrores y las turbaciones "
             "de un alma enferma, ellos mismos padecían un miedo ridículo.",
    (18, 9): "Porque, aunque nada espantoso los asustara, sobresaltados por el "
             "paso de los bichos y por los silbidos de los reptiles,",
    (18, 10): "perecían temblando y negándose a mirar aquel aire del que no "
              "hay modo de huir.",
    (18, 11): "Porque la maldad es cobarde por sí misma y se condena por su "
              "propio testimonio, y, oprimida por la conciencia, siempre "
              "supone lo peor.",
    (18, 12): "Porque el miedo no es otra cosa que la renuncia a los auxilios "
              "de la razón;",
    (18, 13): "y cuanto menor es por dentro la esperanza, tanto más se agranda "
              "la ignorancia de la causa que produce el tormento.",
    (18, 14): "Y ellos, durante aquella noche verdaderamente impotente, venida "
              "de las honduras del Hades impotente,",
    (18, 15): "durmiendo todos el mismo sueño, unas veces eran acosados por "
              "prodigios de fantasmas y otras desfallecían por la traición de "
              "su alma; porque les sobrevino un terror repentino e "
              "inesperado.",
    (18, 16): "Y así, quienquiera que cayese allí donde estaba, quedaba "
              "guardado, encerrado en aquella cárcel sin rejas;",
    (18, 17): "porque, fuese labrador o pastor u obrero de faenas en despoblado, "
              "una vez sorprendido aguardaba aquella fatalidad inevitable.",
    (18, 18): "Porque todos quedaron atados con una sola cadena de tinieblas. "
              "Ya fuese un viento silbante, o el canto armonioso de los pájaros "
              "entre las ramas tupidas, o el ritmo impetuoso del agua que "
              "corre,",
    (18, 19): "o el estrépito áspero de las piedras que ruedan, o la carrera "
              "invisible de animales que saltan, o el aullido de las fieras "
              "más crueles, o el eco devuelto por la hondonada de los montes: "
              "todo los dejaba paralizados de espanto.",
    (18, 20): "Porque el mundo entero estaba iluminado por una luz "
              "resplandeciente y ocupado en sus trabajos sin estorbo;",
    (18, 21): "y sólo sobre aquéllos se extendía una noche pesada, imagen de "
              "las tinieblas que habían de recibirlos; pero eran para sí "
              "mismos más pesados que las tinieblas.",

    (19, 1): "En cambio, para tus santos había una luz grandísima. Aquéllos "
             "oían su voz sin verles la figura, y los tenían por dichosos "
             "porque no padecían lo mismo que ellos;",
    (19, 2): "y les daban gracias porque, habiendo sido agraviados antes, no "
             "les hacían daño; y les pedían por favor que se marcharan.",
    (19, 3): "En cambio, a los tuyos les diste una columna ardiente como guía "
             "de un camino desconocido y como sol inofensivo para su honroso "
             "peregrinar.",
    (19, 4): "Porque aquéllos merecían verse privados de la luz y encarcelados "
             "en tinieblas, los que habían tenido encerrados a tus hijos, por "
             "quienes había de darse al mundo la luz incorruptible de la ley.",
    (19, 5): "Cuando planearon matar a los niños de los santos, y de un solo "
             "niño expuesto y salvado, en castigo les quitaste la multitud de "
             "sus hijos, y los hiciste perecer a todos juntos en un agua "
             "impetuosa.",
    (19, 6): "Aquella noche les fue anunciada de antemano a nuestros padres, "
             "para que, sabiendo con certeza a qué juramentos se habían "
             "confiado, cobrasen ánimo.",
    (19, 7): "Y tu pueblo esperó la salvación de los justos y la perdición de "
             "los enemigos;",
    (19, 8): "porque con aquello mismo con que castigaste a los adversarios, "
             "con eso nos llamaste a nosotros y nos glorificaste.",
    (19, 9): "Porque los hijos santos de los buenos ofrecían sacrificio en "
             "secreto, y de común acuerdo se comprometieron a la ley divina: "
             "que los santos compartirían por igual los mismos bienes y los "
             "mismos peligros; y ya los padres entonaban por anticipado los "
             "cantos de alabanza.",
    (19, 10): "Y respondía como contrapunto el clamor discordante de los "
              "enemigos, y se extendía el lamento por los hijos a quienes "
              "lloraban.",
    (19, 11): "Con la misma pena era castigado el esclavo junto con el señor, "
              "y el hombre del pueblo padecía lo mismo que el rey.",
    (19, 12): "Y todos a una, bajo un mismo nombre de muerte, tenían muertos "
              "sin número; porque ni siquiera bastaban los vivos para "
              "enterrarlos, ya que en un solo instante fue destruida la flor "
              "de su descendencia.",
    (19, 13): "Porque los que no habían creído nada, por causa de sus "
              "hechicerías, ante la ruina de los primogénitos confesaron que "
              "aquel pueblo era hijo de Dios.",
    (19, 14): "Porque, mientras un silencio apacible lo envolvía todo y la "
              "noche llegaba a la mitad de su curso,",
    (19, 15): "tu palabra todopoderosa se lanzó desde los cielos, desde el "
              "trono real, como guerrero implacable, en medio de aquella "
              "tierra condenada,",
    (19, 16): "llevando como espada afilada tu mandato inflexible; y, "
              "deteniéndose, lo llenó todo de muerte: tocaba el cielo y se "
              "asentaba en la tierra.",
    (19, 17): "Entonces, de repente, visiones de sueños terribles los "
              "turbaron, y les sobrevinieron miedos inesperados;",
    (19, 18): "y cada uno, arrojado aquí y allá medio muerto, declaraba la "
              "causa por la que moría.",
    (19, 19): "Porque los sueños que los sobresaltaron se lo habían anunciado, "
              "para que no pereciesen sin saber por qué padecían aquel mal.",
    (19, 20): "También alcanzó a los justos la prueba de la muerte, y hubo en "
              "el desierto una mortandad de la multitud; pero la ira no duró "
              "mucho,",
    (19, 21): "porque un hombre irreprochable se apresuró a salir en su "
              "defensa, llevando como arma propia de su ministerio la oración "
              "y el incienso expiatorio; se enfrentó a la ira y puso fin a la "
              "desgracia, mostrando que era siervo tuyo.",
    (19, 22): "Venció a la muchedumbre no con la fuerza del cuerpo ni con la "
              "eficacia de las armas, sino que con la palabra sometió al que "
              "castigaba, recordándole los juramentos y las alianzas hechas a "
              "los padres.",
    (19, 23): "Porque, cuando ya yacían los muertos amontonados unos sobre "
              "otros, él se puso en medio y detuvo la ira, y cortó el paso "
              "hacia los vivos.",
    (19, 24): "Porque en su vestidura talar estaba el mundo entero, y las "
              "glorias de los padres en el grabado de las cuatro hileras de "
              "piedras, y tu majestad en la diadema de su cabeza.",
    (19, 25): "Ante esto cedió el exterminador, y esto fue lo que temieron; "
              "porque bastó con la sola prueba de la ira.",

    (20, 1): "Pero sobre los impíos se cernió hasta el fin una cólera sin "
             "misericordia, porque él conocía de antemano también lo que "
             "habían de hacer:",
    (20, 2): "que, después de haberles permitido marcharse y de haberlos "
             "despedido con prisa, cambiarían de parecer y los perseguirían.",
    (20, 3): "Porque, teniendo aún entre manos el luto y llorando junto a las "
             "tumbas de sus muertos, se dejaron llevar de otro razonamiento "
             "insensato, y a los que habían echado suplicándoles que se fueran "
             "los perseguían ahora como a fugitivos.",
    (20, 4): "Porque los arrastraba a ese fin la fatalidad que merecían, y les "
             "hizo olvidar lo sucedido, para que colmasen con nuevos tormentos "
             "el castigo que aún les faltaba,",
    (20, 5): "y para que tu pueblo hiciese un viaje asombroso y aquéllos "
             "hallasen una muerte extraordinaria.",
    (20, 6): "Porque toda la creación fue de nuevo transformada desde su "
             "origen en su propia naturaleza, sirviendo a tus mandatos, para "
             "que tus hijos quedasen a salvo de todo daño.",
    (20, 7): "Se vio la nube que daba sombra al campamento, y el surgir de "
             "tierra seca de donde antes había agua: un camino sin obstáculos "
             "a través del mar Rojo, y una llanura cubierta de hierba donde "
             "había un oleaje violento;",
    (20, 8): "por él pasaron como un solo pueblo los que estaban cubiertos por "
             "tu mano, después de contemplar prodigios admirables.",
    (20, 9): "Porque pacían como caballos y brincaban como corderos, "
             "alabándote a ti, Señor, que los libraste.",
    (20, 10): "Porque se acordaban todavía de lo ocurrido durante su estancia "
              "en tierra extraña: cómo la tierra, en lugar de criar animales, "
              "produjo mosquitos, y el río, en vez de peces, vomitó una "
              "multitud de ranas.",
    (20, 11): "Y más tarde vieron también una nueva clase de aves, cuando, "
              "llevados por el apetito, pidieron manjares regalados;",
    (20, 12): "porque, para consolarlos, les subió del mar la codorniz.",
    (20, 13): "Y sobre los pecadores vinieron los castigos, no sin las señales "
              "previas de la violencia de los rayos; porque padecían "
              "justamente por sus propias maldades, ya que habían practicado "
              "un odio al forastero más cruel todavía.",
    (20, 14): "Porque aquéllos no recibían a los desconocidos cuando llegaban; "
              "pero éstos esclavizaron a huéspedes que los habían "
              "beneficiado.",
    (20, 15): "Y no sólo eso: aquéllos habrán de ser visitados por el juicio, "
              "puesto que recibieron con hostilidad a los extranjeros;",
    (20, 16): "pero éstos, que los habían acogido con fiestas y que ya habían "
              "compartido con ellos los mismos derechos, los maltrataron con "
              "trabajos terribles.",
    (20, 17): "Y fueron heridos de ceguera, como aquellos otros a las puertas "
              "del justo, cuando, envueltos en una oscuridad total, cada uno "
              "buscaba el paso de su propia puerta.",
    (20, 18): "Porque los elementos, reajustándose entre sí, como las notas en "
              "un salterio cambian el nombre del ritmo permaneciendo siempre "
              "el mismo sonido, es lo que se puede deducir con exactitud de lo "
              "que se vio suceder.",
    (20, 19): "Porque los animales de tierra se volvían acuáticos, y los que "
              "nadan pasaban a la tierra;",
    (20, 20): "el fuego conservó en el agua su propia fuerza, y el agua olvidó "
              "su poder de apagar.",
    (20, 21): "Y al contrario, las llamas no consumieron las carnes de "
              "animales frágiles que andaban por ellas, ni derritieron aquel "
              "manjar celestial, parecido al hielo y fácil de derretirse.",
    (20, 22): "Porque en todo, Señor, engrandeciste a tu pueblo y lo "
              "glorificaste; y no lo despreciaste, sino que le asististe en "
              "todo tiempo y lugar.",
}
