"""Primera carta de Clemente a los Corintios, traducida del griego.

La escribió la iglesia de Roma a la de Corinto hacia el año 96, cuando en
Corinto unos jóvenes habían depuesto a sus presbíteros. La tradición la
atribuye a Clemente, obispo de Roma, aunque el texto no da su nombre. Es el
escrito cristiano más antiguo fuera del Nuevo Testamento del que se sabe con
certeza la fecha, y en algunas iglesias se leía en el culto junto a las cartas
de Pablo.

Importa por lo que da por supuesto: que Pedro y Pablo murieron mártires (5),
que los apóstoles pusieron obispos y diáconos y dispusieron que otros les
sucedieran (42-44), y por la gran oración de los capítulos 59 al 61, que es la
más antigua que conservamos de la liturgia romana.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

CLEMENTE1_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "La iglesia de Dios que peregrina en Roma, a la iglesia de Dios "
            "que peregrina en Corinto, a los llamados, santificados en la "
            "voluntad de Dios por nuestro Señor Jesucristo. Gracia y paz os "
            "sean multiplicadas de parte del Dios todopoderoso por medio de "
            "Jesucristo.",
    (1, 1): "A causa de las repentinas y sucesivas desgracias y contratiempos "
            "que nos han sobrevenido, amados, pensamos que hemos tardado en "
            "prestar atención a los asuntos que se debaten entre vosotros, y "
            "a la sedición, extraña y ajena a los escogidos de Dios, "
            "abominable e impía, que unas pocas personas temerarias y "
            "arrogantes han encendido hasta tal grado de locura, que vuestro "
            "nombre, venerable y célebre y digno del amor de todos los "
            "hombres, ha sido grandemente blasfemado.",
    (1, 2): "Porque ¿quién, habiendo residido entre vosotros, no ha "
            "comprobado vuestra fe llena de toda virtud y firme? ¿Quién no ha "
            "admirado vuestra piedad sobria y mansa en Cristo? ¿Quién no ha "
            "pregonado la magnificencia de vuestra costumbre de hospitalidad? "
            "¿Y quién no ha tenido por dichoso vuestro conocimiento perfecto "
            "y seguro?",
    (1, 3): "Porque todo lo hacíais sin acepción de personas, y andabais en "
            "las leyes de Dios, sujetos a los que os gobiernan, y tributando "
            "la honra debida a los ancianos que hay entre vosotros; a los "
            "jóvenes les encargabais pensar cosas moderadas y dignas; a las "
            "mujeres les mandabais cumplirlo todo con conciencia "
            "irreprensible, digna y pura, amando como es debido a sus propios "
            "maridos; y les enseñabais que, permaneciendo en la regla de la "
            "sujeción, gobernasen con dignidad los asuntos de su casa, siendo "
            "del todo prudentes.",

    # Capítulo 2
    (2, 1): "Y todos erais humildes de ánimo, sin jactaros en nada, "
            "sujetándoos antes que sujetando a otros, dando con más gusto que "
            "recibiendo. Contentos con las provisiones de Cristo, y "
            "atendiendo a sus palabras, las teníais guardadas con diligencia "
            "en vuestras entrañas, y sus padecimientos estaban delante de "
            "vuestros ojos.",
    (2, 2): "Así se os había dado a todos una paz profunda y abundante, y un "
            "deseo insaciable de hacer el bien, y había sobre todos un pleno "
            "derramamiento del Espíritu Santo;",
    (2, 3): "y llenos de santo consejo, con buena disposición y con piadosa "
            "confianza, extendíais vuestras manos al Dios todopoderoso, "
            "suplicándole que os fuese propicio si en algo habíais pecado sin "
            "querer.",
    (2, 4): "Teníais combate día y noche por toda la hermandad, para que se "
            "salvase, con misericordia y conciencia, el número de sus "
            "escogidos.",
    (2, 5): "Erais sinceros e íntegros, y no guardabais rencor los unos "
            "contra los otros.",
    (2, 6): "Toda sedición y todo cisma os era abominable. Llorabais por las "
            "faltas de vuestro prójimo; teníais sus deficiencias por vuestras "
            "propias.",
    (2, 7): "No os arrepentíais de ningún bien que hicieseis, prontos para "
            "toda buena obra.",
    (2, 8): "Adornados de una conducta llena de toda virtud y venerable, lo "
            "cumplíais todo en su temor; los mandamientos y las ordenanzas "
            "del Señor estaban escritos en las tablas de vuestro corazón.",

    # Capítulo 3
    (3, 1): "Toda gloria y ensanchamiento os fue dado, y se cumplió lo que "
            "está escrito: Comió y bebió, y se ensanchó, y engordó, y tiró "
            "coces el amado.",
    (3, 2): "De aquí vinieron los celos y la envidia, la contienda y la "
            "sedición, la persecución y el desorden, la guerra y la "
            "cautividad.",
    (3, 3): "Así se levantaron los sin honra contra los honrados, los sin "
            "fama contra los de renombre, los insensatos contra los "
            "prudentes, los jóvenes contra los ancianos.",
    (3, 4): "Por esto se han alejado mucho la justicia y la paz, porque cada "
            "uno ha abandonado el temor de Dios y se ha vuelto corto de vista "
            "en su fe, y no anda en las leyes de sus mandamientos, ni vive "
            "como conviene a Cristo, sino que cada uno camina según las "
            "concupiscencias de su malvado corazón, habiendo tomado sobre sí "
            "los celos injustos e impíos, por los cuales también entró la "
            "muerte en el mundo.",

    # Capítulo 4
    (4, 1): "Porque así está escrito: Y aconteció, andando el tiempo, que "
            "Caín trajo del fruto de la tierra un sacrificio a Dios; y Abel "
            "trajo también de los primogénitos de sus ovejas, y de su "
            "grosura.",
    (4, 2): "Y miró Dios a Abel y a sus dones, mas a Caín y a sus sacrificios "
            "no atendió.",
    (4, 3): "Y se entristeció Caín en gran manera, y decayó su semblante.",
    (4, 4): "Y dijo Dios a Caín: ¿Por qué te has entristecido, y por qué ha "
            "decaído tu semblante? Si ofreces rectamente, pero no repartes "
            "rectamente, ¿no has pecado?",
    (4, 5): "Sosiégate: a ti se volverá él, y tú te enseñorearás de él.",
    (4, 6): "Y dijo Caín a Abel su hermano: Vamos al campo. Y aconteció que, "
            "estando ellos en el campo, se levantó Caín contra Abel su "
            "hermano, y lo mató.",
    (4, 7): "Ved, hermanos: los celos y la envidia obraron el fratricidio.",
    (4, 8): "Por los celos nuestro padre Jacob huyó de la presencia de Esaú "
            "su hermano.",
    (4, 9): "Los celos hicieron que José fuese perseguido hasta la muerte y "
            "llegase hasta la servidumbre.",
    (4, 10): "Los celos obligaron a Moisés a huir de la presencia de Faraón, "
             "rey de Egipto, cuando oyó de uno de su propio pueblo: ¿Quién te "
             "ha puesto por juez o por árbitro sobre nosotros? ¿Quieres tú "
             "matarme como mataste ayer al egipcio?",
    (4, 11): "Por los celos Aarón y María tuvieron que alojarse fuera del "
             "campamento.",
    (4, 12): "Los celos hicieron descender vivos al Hades a Datán y Abirón, "
             "porque se sublevaron contra el siervo de Dios, Moisés.",
    (4, 13): "Por los celos David no solo fue envidiado por los extranjeros, "
             "sino que también fue perseguido por Saúl, rey de Israel.",

    # Capítulo 5
    (5, 1): "Pero, para dejar los ejemplos antiguos, vengamos a los atletas "
            "que han vivido muy cerca de nosotros; tomemos los nobles "
            "ejemplos de nuestra generación.",
    (5, 2): "Por celos y envidia fueron perseguidas las columnas más grandes "
            "y más justas, y lucharon hasta la muerte.",
    (5, 3): "Pongamos delante de nuestros ojos a los buenos apóstoles:",
    (5, 4): "a Pedro, que por celos injustos soportó no uno ni dos, sino "
            "muchos trabajos, y habiendo dado así testimonio, se fue al lugar "
            "de gloria que le era debido.",
    (5, 5): "Por celos y contienda mostró Pablo el premio de la paciencia:",
    (5, 6): "siete veces llevó cadenas, fue desterrado, fue apedreado, fue "
            "heraldo en el oriente y en el occidente, y recibió la noble "
            "gloria de su fe;",
    (5, 7): "habiendo enseñado justicia a todo el mundo, y habiendo llegado "
            "hasta el límite del occidente, y habiendo dado testimonio ante "
            "los gobernantes, así partió del mundo y fue recibido en el lugar "
            "santo, hecho el mayor modelo de paciencia.",

    # Capítulo 6
    (6, 1): "A estos hombres, que vivieron santamente, se juntó una gran "
            "multitud de escogidos, los cuales, habiendo padecido por celos "
            "muchos ultrajes y tormentos, llegaron a ser entre nosotros el "
            "más hermoso ejemplo.",
    (6, 2): "Por celos fueron perseguidas mujeres, Danaides y Dirces, que, "
            "habiendo padecido ultrajes terribles e impíos, alcanzaron la "
            "meta segura de la carrera de la fe, y recibieron un noble "
            "galardón, ellas, débiles en el cuerpo.",
    (6, 3): "Los celos han apartado a las esposas de sus maridos y han "
            "trastornado lo dicho por nuestro padre Adán: Esto es ahora hueso "
            "de mis huesos y carne de mi carne.",
    (6, 4): "Los celos y la contienda han derribado grandes ciudades y han "
            "desarraigado grandes naciones.",

    # Capítulo 7
    (7, 1): "Esto os escribimos, amados, no solo para amonestaros a vosotros, "
            "sino también para recordárnoslo a nosotros mismos; porque "
            "estamos en la misma arena, y nos aguarda el mismo combate.",
    (7, 2): "Por tanto, abandonemos los cuidados vanos e inútiles, y vengamos "
            "a la regla gloriosa y venerable de nuestra tradición,",
    (7, 3): "y veamos qué es bueno, y qué es agradable, y qué es acepto "
            "delante del que nos hizo.",
    (7, 4): "Fijemos los ojos en la sangre de Cristo, y conozcamos cuán "
            "preciosa es para su Padre, pues, derramada por nuestra "
            "salvación, alcanzó para todo el mundo la gracia del "
            "arrepentimiento.",
    (7, 5): "Recorramos todas las generaciones, y aprendamos que de "
            "generación en generación el Soberano ha dado lugar de "
            "arrepentimiento a los que quieren volverse a él.",
    (7, 6): "Noé predicó el arrepentimiento, y los que le obedecieron fueron "
            "salvos.",
    (7, 7): "Jonás anunció la destrucción a los ninivitas; mas ellos, "
            "arrepintiéndose de sus pecados, aplacaron a Dios con sus "
            "súplicas y recibieron la salvación, aunque eran ajenos a Dios.",

    # Capítulo 8
    (8, 1): "Los ministros de la gracia de Dios hablaron del arrepentimiento "
            "por el Espíritu Santo.",
    (8, 2): "Y aun el mismo Soberano de todas las cosas habló del "
            "arrepentimiento con juramento: Vivo yo, dice el Señor, que no "
            "quiero la muerte del pecador, sino su arrepentimiento; añadiendo "
            "además una buena sentencia:",
    (8, 3): "Arrepentíos, casa de Israel, de vuestra iniquidad. Di a los "
            "hijos de mi pueblo: Aunque vuestros pecados lleguen desde la "
            "tierra hasta el cielo, y aunque sean más rojos que la grana y "
            "más negros que el cilicio, si os volvéis a mí de todo corazón y "
            "decís: Padre, os escucharé como a pueblo santo.",
    (8, 4): "Y en otro lugar dice así: Lavaos y limpiaos; quitad las maldades "
            "de vuestras almas de delante de mis ojos; dejad de hacer "
            "vuestras maldades; aprended a hacer el bien; buscad el juicio; "
            "librad al agraviado; haced justicia al huérfano, amparad a la "
            "viuda. Venid luego, y estemos a cuenta, dice el Señor: si "
            "vuestros pecados fueren como la púrpura, como la nieve los "
            "emblanqueceré; y si fueren como la grana, como la lana los "
            "emblanqueceré. Si quisiereis y me oyereis, comeréis el bien de "
            "la tierra; mas si no quisiereis ni me oyereis, la espada os "
            "devorará; porque la boca del Señor ha hablado estas cosas.",
    (8, 5): "Queriendo, pues, que todos sus amados participen del "
            "arrepentimiento, lo afirmó con su voluntad todopoderosa.",

    # Capítulo 9
    (9, 1): "Por tanto, obedezcamos a su voluntad magnífica y gloriosa, y "
            "haciéndonos suplicantes de su misericordia y de su bondad, "
            "postrémonos y volvámonos a sus compasiones, abandonando el "
            "trabajo vano, y la contienda, y los celos que llevan a la "
            "muerte.",
    (9, 2): "Fijemos los ojos en los que sirvieron perfectamente a su "
            "magnífica gloria.",
    (9, 3): "Tomemos a Enoc, que, hallado justo en la obediencia, fue "
            "trasladado, y no se halló su muerte.",
    (9, 4): "Noé, hallado fiel, predicó por su ministerio la regeneración al "
            "mundo, y por medio de él el Soberano salvó a los animales que "
            "entraron en concordia en el arca.",

    # Capítulo 10
    (10, 1): "Abrahán, que fue llamado el amigo, fue hallado fiel en que se "
             "hizo obediente a las palabras de Dios.",
    (10, 2): "Este, por obediencia, salió de su tierra, y de su parentela, y "
             "de la casa de su padre, para que, dejando una tierra pequeña, "
             "una parentela débil y una casa pequeña, heredase las promesas "
             "de Dios. Porque le dice:",
    (10, 3): "Vete de tu tierra, y de tu parentela, y de la casa de tu padre, "
             "a la tierra que yo te mostraré; y haré de ti una nación grande, "
             "y te bendeciré, y engrandeceré tu nombre, y serás bendito; y "
             "bendeciré a los que te bendijeren, y maldeciré a los que te "
             "maldijeren, y serán benditas en ti todas las tribus de la "
             "tierra.",
    (10, 4): "Y otra vez, cuando se separó de Lot, le dijo Dios: Alza tus "
             "ojos y mira desde el lugar donde ahora estás, hacia el norte y "
             "el mediodía, y el oriente y el mar; porque toda la tierra que "
             "tú ves, a ti la daré, y a tu simiente para siempre.",
    (10, 5): "Y haré tu simiente como la arena de la tierra: si alguno puede "
             "contar la arena de la tierra, también tu simiente será contada.",
    (10, 6): "Y otra vez dice: Sacó Dios a Abrahán y le dijo: Mira ahora "
             "hacia el cielo, y cuenta las estrellas, si las puedes contar: "
             "así será tu simiente. Y creyó Abrahán a Dios, y le fue contado "
             "por justicia.",
    (10, 7): "Por su fe y su hospitalidad le fue dado un hijo en la vejez, y "
             "por obediencia lo ofreció en sacrificio a Dios sobre uno de los "
             "montes que él le mostró.",

    # Capítulo 11
    (11, 1): "Por su hospitalidad y su piedad Lot fue salvado de Sodoma, "
             "cuando toda la comarca fue juzgada con fuego y azufre; con lo "
             "cual el Soberano puso de manifiesto que no desampara a los que "
             "esperan en él, y que entrega al castigo y al tormento a los que "
             "se desvían.",
    (11, 2): "Porque su mujer, que salió con él, siendo de otro parecer y no "
             "estando en concordia, fue puesta por señal, de modo que quedó "
             "hecha una columna de sal hasta el día de hoy, para que sea "
             "notorio a todos que los de doble ánimo y los que dudan del "
             "poder de Dios vienen a ser juicio y escarmiento para todas las "
             "generaciones.",

    # Capítulo 12
    (12, 1): "Por su fe y su hospitalidad fue salvada Rahab la ramera.",
    (12, 2): "Porque, habiendo sido enviados por Josué, hijo de Nun, unos "
             "espías a Jericó, supo el rey de la tierra que habían venido a "
             "espiar su país, y envió hombres que los prendiesen, para que, "
             "una vez presos, fuesen muertos.",
    (12, 3): "La hospitalaria Rahab, pues, habiéndolos recibido, los escondió "
             "en el aposento alto, bajo los tallos de lino.",
    (12, 4): "Y cuando se presentaron los enviados del rey y dijeron: A ti "
             "vinieron los espías de nuestra tierra; sácalos, porque así lo "
             "manda el rey, ella respondió: Es verdad que los hombres que "
             "buscáis vinieron a mí, pero se fueron en seguida y van por el "
             "camino; y les señalaba el camino contrario.",
    (12, 5): "Y dijo a los hombres: Bien sé yo que el Señor Dios os entrega "
             "esta tierra; porque vuestro temor y vuestro espanto ha caído "
             "sobre sus moradores. Cuando, pues, os toque tomarla, salvadme a "
             "mí y a la casa de mi padre.",
    (12, 6): "Y ellos le dijeron: Será así como nos has dicho. Cuando, pues, "
             "sepas que llegamos, reunirás a todos los tuyos bajo tu techo, y "
             "serán salvos; porque todos los que se hallaren fuera de la casa "
             "perecerán.",
    (12, 7): "Y además le dieron una señal: que colgase de su casa un cordón "
             "de grana; dando a entender de antemano que por la sangre del "
             "Señor habrá redención para todos los que creen y esperan en "
             "Dios.",
    (12, 8): "Ved, amados, que en esta mujer hubo no solo fe, sino también "
             "profecía.",

    # Capítulo 13
    (13, 1): "Seamos, pues, humildes de ánimo, hermanos, desechando toda "
             "jactancia, y vanidad, e insensatez, y toda ira, y hagamos lo "
             "que está escrito; porque dice el Espíritu Santo: No se alabe el "
             "sabio en su sabiduría, ni el fuerte en su fuerza, ni el rico en "
             "su riqueza; sino el que se alaba, alábese en el Señor, en "
             "buscarle y en hacer juicio y justicia; acordándonos sobre todo "
             "de las palabras del Señor Jesús, que habló enseñando la "
             "mansedumbre y la longanimidad.",
    (13, 2): "Porque así dijo: Tened misericordia, para que alcancéis "
             "misericordia; perdonad, para que os sea perdonado; como hacéis, "
             "así se os hará; como dais, así se os dará; como juzgáis, así "
             "seréis juzgados; como sois bondadosos, así se usará de bondad "
             "con vosotros; con la medida con que medís, con ella se os "
             "medirá.",
    (13, 3): "Con este mandamiento y con estos preceptos afirmémonos a "
             "nosotros mismos para andar obedientes a sus santas palabras, "
             "siendo humildes de ánimo; porque dice la santa palabra:",
    (13, 4): "¿A quién miraré, sino al manso y sosegado, y que tiembla de mis "
             "palabras?",

    # Capítulo 14
    (14, 1): "Justo es, pues, y santo, varones hermanos, que seamos "
             "obedientes a Dios antes que seguir a los que, con jactancia y "
             "desorden, son caudillos de unos celos abominables.",
    (14, 2): "Porque sufriremos no un daño cualquiera, sino más bien un gran "
             "peligro, si temerariamente nos entregamos a las voluntades de "
             "los hombres que se lanzan a la contienda y a las sediciones "
             "para apartarnos de lo que es bueno.",
    (14, 3): "Seamos bondadosos unos con otros, conforme a la compasión y "
             "dulzura del que nos hizo.",
    (14, 4): "Porque está escrito: Los bondadosos habitarán la tierra, y los "
             "inocentes quedarán en ella; mas los transgresores serán "
             "desarraigados de ella.",
    (14, 5): "Y otra vez dice: Vi al impío sumamente ensalzado, y que se "
             "levantaba como los cedros del Líbano; y pasé, y he aquí ya no "
             "estaba; y busqué su lugar, y no lo hallé. Guarda la inocencia y "
             "mira la rectitud, porque hay posteridad para el hombre "
             "pacífico.",

    # Capítulo 15
    (15, 1): "Unámonos, pues, a los que con piedad guardan la paz, y no a los "
             "que con hipocresía dicen querer la paz.",
    (15, 2): "Porque dice en cierto lugar: Este pueblo con los labios me "
             "honra, mas su corazón está lejos de mí.",
    (15, 3): "Y otra vez: Con su boca bendecían, mas con su corazón "
             "maldecían.",
    (15, 4): "Y otra vez dice: Le amaron con su boca, y con su lengua le "
             "mintieron; mas su corazón no era recto con él, ni fueron fieles "
             "en su pacto.",
    (15, 5): "Por tanto, enmudezcan los labios engañosos que hablan iniquidad "
             "contra el justo. Y otra vez: Destruya el Señor todos los labios "
             "engañosos, la lengua que habla grandezas, a los que dijeron: "
             "Engrandeceremos nuestra lengua; nuestros labios son nuestros; "
             "¿quién es señor de nosotros?",
    (15, 6): "Por la opresión de los pobres, por el gemido de los "
             "menesterosos, ahora me levantaré, dice el Señor; lo pondré en "
             "salvo;",
    (15, 7): "obraré con denuedo en su favor.",

    # Capítulo 16
    (16, 1): "Porque Cristo es de los humildes de ánimo, no de los que se "
             "ensalzan sobre su rebaño.",
    (16, 2): "El cetro de la majestad de Dios, el Señor Jesucristo, no vino "
             "con pompa de jactancia ni de soberbia, aunque podía, sino con "
             "humildad de ánimo, como el Espíritu Santo había hablado de él. "
             "Porque dice:",
    (16, 3): "Señor, ¿quién ha creído a nuestro anuncio? ¿y a quién se ha "
             "manifestado el brazo del Señor? Anunciamos delante de él: es "
             "como un niño, como raíz de tierra seca; no hay en él parecer ni "
             "gloria. Y lo vimos, y no tenía parecer ni hermosura, sino que "
             "su parecer era despreciable, inferior al parecer de los "
             "hombres; hombre puesto en llaga y en dolor, y que sabe sufrir "
             "quebranto; porque su rostro fue apartado, fue menospreciado y "
             "no fue estimado.",
    (16, 4): "Él lleva nuestros pecados y por nosotros sufre dolores; y "
             "nosotros le tuvimos por puesto en dolor, en llaga y en "
             "aflicción.",
    (16, 5): "Mas él fue herido por nuestros pecados, y molido por nuestras "
             "iniquidades; el castigo de nuestra paz fue sobre él; por su "
             "llaga fuimos nosotros curados.",
    (16, 6): "Todos nosotros nos descarriamos como ovejas; cada hombre se "
             "descarrió por su camino;",
    (16, 7): "y el Señor lo entregó por nuestros pecados, y él, por haber "
             "sido afligido, no abre la boca. Como oveja fue llevado al "
             "matadero, y como cordero mudo delante del que lo trasquila, así "
             "no abre su boca. En su humillación le fue quitado su juicio.",
    (16, 8): "Su generación, ¿quién la contará? Porque su vida es quitada de "
             "la tierra.",
    (16, 9): "Por las iniquidades de mi pueblo llega a la muerte.",
    (16, 10): "Y daré a los malvados en pago de su sepultura, y a los ricos "
              "en pago de su muerte; porque no hizo iniquidad, ni se halló "
              "engaño en su boca. Y el Señor quiere limpiarlo de la llaga.",
    (16, 11): "Si ofreciereis expiación por el pecado, vuestra alma verá "
              "linaje de larga vida.",
    (16, 12): "Y el Señor quiere quitarle del trabajo de su alma, mostrarle "
              "luz y formarle con entendimiento, justificar al justo que "
              "sirve bien a muchos; y él llevará los pecados de ellos.",
    (16, 13): "Por tanto él heredará a muchos, y repartirá los despojos de "
              "los fuertes; por cuanto su alma fue entregada a la muerte, y "
              "fue contado con los inicuos.",
    (16, 14): "Y él llevó los pecados de muchos, y por los pecados de ellos "
              "fue entregado.",
    (16, 15): "Y otra vez dice él mismo: Mas yo soy gusano, y no hombre; "
              "oprobio de los hombres y desprecio del pueblo.",
    (16, 16): "Todos los que me ven me escarnecen; hablan con los labios, "
              "menean la cabeza: Esperó en el Señor; líbrelo, sálvelo, puesto "
              "que se complace en él.",
    (16, 17): "Ved, varones amados, cuál es el modelo que se nos ha dado; "
              "porque si el Señor fue así de humilde de ánimo, ¿qué haremos "
              "nosotros, que por él hemos venido bajo el yugo de su gracia?",

    # Capítulo 17
    (17, 1): "Hagámonos imitadores también de aquellos que anduvieron "
             "vestidos de pieles de cabras y de ovejas, predicando la venida "
             "de Cristo; decimos Elías y Eliseo, y además Ezequiel, los "
             "profetas; y además de estos, también a los que recibieron buen "
             "testimonio.",
    (17, 2): "Abrahán recibió gran testimonio y fue llamado amigo de Dios; y "
             "fijando los ojos en la gloria de Dios, dice con humildad de "
             "ánimo: Mas yo soy tierra y ceniza.",
    (17, 3): "Y además, de Job está escrito así: Y Job era justo e "
             "irreprensible, verdadero, temeroso de Dios, apartado de todo "
             "mal.",
    (17, 4): "Pero él mismo se acusa, diciendo: Nadie está limpio de "
             "inmundicia, aunque su vida sea de un solo día.",
    (17, 5): "Moisés fue llamado fiel en toda su casa, y por su ministerio "
             "juzgó Dios a Egipto con las plagas y los tormentos que les "
             "vinieron; pero también él, aunque grandemente glorificado, no "
             "habló con jactancia, sino que, cuando le era dado el oráculo "
             "desde la zarza, dijo: ¿Quién soy yo para que me envíes? Yo soy "
             "tardo en el hablar y torpe de lengua.",
    (17, 6): "Y otra vez dice: Yo soy vapor de olla.",

    # Capítulo 18
    (18, 1): "¿Y qué diremos de David, que recibió buen testimonio? De él "
             "dijo Dios: He hallado un varón conforme a mi corazón, David, "
             "hijo de Isaí; con misericordia eterna lo he ungido.",
    (18, 2): "Pero también él dice a Dios: Ten misericordia de mí, oh Dios, "
             "conforme a tu gran misericordia; y conforme a la multitud de "
             "tus piedades borra mi rebelión.",
    (18, 3): "Lávame más y más de mi maldad, y límpiame de mi pecado; porque "
             "yo conozco mi maldad, y mi pecado está siempre delante de mí.",
    (18, 4): "A ti, a ti solo he pecado, y he hecho lo malo delante de tus "
             "ojos, para que seas justificado en tus palabras, y venzas "
             "cuando seas juzgado.",
    (18, 5): "Porque he aquí, en maldades fui concebido, y en pecados me "
             "concibió mi madre.",
    (18, 6): "Porque he aquí, amaste la verdad; lo incierto y lo oculto de tu "
             "sabiduría me manifestaste.",
    (18, 7): "Me rociarás con hisopo, y seré limpio; me lavarás, y seré "
             "emblanquecido más que la nieve.",
    (18, 8): "Me harás oír gozo y alegría; se regocijarán los huesos que has "
             "abatido.",
    (18, 9): "Esconde tu rostro de mis pecados, y borra todas mis maldades.",
    (18, 10): "Crea en mí, oh Dios, un corazón limpio, y renueva un espíritu "
              "recto dentro de mí.",
    (18, 11): "No me eches de delante de ti, y no quites de mí tu santo "
              "Espíritu.",
    (18, 12): "Vuélveme el gozo de tu salvación, y el espíritu principal me "
              "sustente.",
    (18, 13): "Enseñaré a los prevaricadores tus caminos, y los impíos se "
              "convertirán a ti.",
    (18, 14): "Líbrame de sangres, oh Dios, Dios de mi salud.",
    (18, 15): "Cantará mi lengua tu justicia. Señor, abrirás mi boca, y mis "
              "labios anunciarán tu alabanza.",
    (18, 16): "Porque si quisieras sacrificio, yo lo daría; no quieres "
              "holocausto.",
    (18, 17): "El sacrificio para Dios es el espíritu quebrantado; al corazón "
              "contrito y humillado no despreciará Dios.",

    # Capítulo 19
    (19, 1): "Así pues, la humildad de ánimo y la sumisión de tantos y tan "
             "grandes varones, que recibieron tan buen testimonio, por medio "
             "de la obediencia nos han hecho mejores no solo a nosotros, sino "
             "también a las generaciones anteriores a nosotros, y a los que "
             "recibieron sus oráculos con temor y verdad.",
    (19, 2): "Habiendo, pues, participado de muchos, grandes y gloriosos "
             "hechos, volvamos a correr hacia la meta de la paz que nos fue "
             "transmitida desde el principio, y fijemos los ojos en el Padre "
             "y Creador de todo el mundo, y adhirámonos a sus magníficos y "
             "sobreabundantes dones y beneficios de paz.",
    (19, 3): "Contemplémosle con el entendimiento, y miremos con los ojos del "
             "alma su voluntad longánime; consideremos cuán exento de ira es "
             "para con toda su creación.",

    # Capítulo 20
    (20, 1): "Los cielos, movidos por su gobierno, le están sujetos en paz.",
    (20, 2): "El día y la noche recorren el curso ordenado por él, sin "
             "estorbarse en nada el uno al otro.",
    (20, 3): "El sol y la luna, y los coros de las estrellas, conforme a su "
             "ordenación, desenvuelven en concordia, sin desvío alguno, los "
             "giros que les han sido señalados.",
    (20, 4): "La tierra, fecunda según su voluntad, hace brotar en sus "
             "propias estaciones el alimento abundantísimo para los hombres y "
             "para las fieras y para todos los animales que hay sobre ella, "
             "sin disentir ni alterar nada de lo que él ha decretado.",
    (20, 5): "Las regiones inescrutables de los abismos y las indecibles de "
             "los lugares inferiores son mantenidas por los mismos mandatos.",
    (20, 6): "La cavidad del mar inmenso, formada por su obra creadora para "
             "ser lugar de reunión de las aguas, no traspasa las barreras que "
             "le han sido puestas alrededor, sino que, como él se lo ordenó, "
             "así hace.",
    (20, 7): "Porque dijo: Hasta aquí llegarás, y tus olas se quebrarán "
             "dentro de ti.",
    (20, 8): "El océano, infranqueable para los hombres, y los mundos que hay "
             "más allá de él, son gobernados por las mismas ordenanzas del "
             "Soberano.",
    (20, 9): "Las estaciones de primavera, de verano, de otoño y de invierno "
             "se suceden en paz unas a otras.",
    (20, 10): "Los depósitos de los vientos cumplen su servicio a su debido "
              "tiempo y sin tropiezo; las fuentes perennes, creadas para el "
              "disfrute y la salud, ofrecen sin cesar sus pechos para la vida "
              "de los hombres; y los más pequeños de los animales se juntan "
              "en concordia y en paz.",
    (20, 11): "Todas estas cosas mandó el gran Creador y Soberano de todas "
              "las cosas que estuviesen en paz y concordia, haciendo bien a "
              "todas, pero sobreabundantemente a nosotros, que nos hemos "
              "refugiado en sus compasiones por nuestro Señor Jesucristo,",
    (20, 12): "a quien sea la gloria y la majestad por los siglos de los "
              "siglos. Amén.",

    # Capítulo 21
    (21, 1): "Mirad, amados, que sus muchos beneficios no se nos vuelvan en "
             "juicio, si no andamos como es digno de él, y hacemos en "
             "concordia lo que es bueno y agradable delante de él.",
    (21, 2): "Porque dice en cierto lugar: El espíritu del Señor es lámpara "
             "que escudriña lo más recóndito del vientre.",
    (21, 3): "Veamos cuán cerca está, y que nada se le oculta de nuestros "
             "pensamientos ni de los razonamientos que hacemos.",
    (21, 4): "Justo es, pues, que no desertemos de su voluntad.",
    (21, 5): "Ofendamos antes a hombres insensatos y necios, que se ensalzan "
             "y se glorían en la jactancia de su palabra, que a Dios.",
    (21, 6): "Reverenciemos al Señor Jesucristo, cuya sangre fue dada por "
             "nosotros; respetemos a los que nos presiden; honremos a los "
             "ancianos; instruyamos a los jóvenes en la disciplina del temor "
             "de Dios; encaminemos a nuestras mujeres al bien.",
    (21, 7): "Muestren la amable costumbre de la castidad; manifiesten la "
             "sincera voluntad de su mansedumbre; hagan patente con su "
             "silencio la moderación de su lengua; y den su amor, no según "
             "preferencias, sino por igual y santamente a todos los que temen "
             "a Dios.",
    (21, 8): "Participen nuestros hijos de la instrucción que es en Cristo; "
             "aprendan cuánto vale ante Dios la humildad de ánimo, cuánto "
             "puede ante Dios el amor puro, cuán bueno y grande es su temor, "
             "y cómo salva a todos los que en él se conducen santamente con "
             "mente pura.",
    (21, 9): "Porque él es escudriñador de los pensamientos y de los "
             "propósitos; su aliento está en nosotros, y cuando quiera, lo "
             "quitará.",

    # Capítulo 22
    (22, 1): "Todas estas cosas las confirma la fe que es en Cristo; porque "
             "él mismo, por el Espíritu Santo, nos llama así: Venid, hijos, "
             "oídme; el temor del Señor os enseñaré.",
    (22, 2): "¿Quién es el hombre que desea vida, que ama ver días buenos?",
    (22, 3): "Guarda tu lengua del mal, y tus labios de hablar engaño.",
    (22, 4): "Apártate del mal, y haz el bien.",
    (22, 5): "Busca la paz, y síguela.",
    (22, 6): "Los ojos del Señor están sobre los justos, y atentos sus oídos "
             "a la súplica de ellos; mas el rostro del Señor está contra los "
             "que hacen mal, para cortar de la tierra su memoria.",
    (22, 7): "Clamó el justo, y el Señor le oyó, y lo libró de todas sus "
             "angustias.",
    (22, 8): "Muchos son los azotes del pecador; mas a los que esperan en el "
             "Señor los rodeará la misericordia.",

    # Capítulo 23
    (23, 1): "El Padre, compasivo en todo y bienhechor, tiene entrañas para "
             "con los que le temen, y con benignidad y dulzura reparte sus "
             "gracias a los que se acercan a él con mente sencilla.",
    (23, 2): "Por tanto, no seamos de doble ánimo, ni se forje vanas "
             "imaginaciones nuestra alma acerca de sus dones sobreabundantes "
             "y gloriosos.",
    (23, 3): "Lejos esté de nosotros esta escritura donde dice: Desdichados "
             "son los de doble ánimo, los que dudan en su alma, los que "
             "dicen: Estas cosas oímos ya en tiempos de nuestros padres, y he "
             "aquí, hemos envejecido, y nada de esto nos ha acontecido.",
    (23, 4): "¡Oh insensatos! Comparaos a un árbol; tomad una vid: primero se "
             "le caen las hojas, luego viene el brote, luego la hoja, luego "
             "la flor, y después de esto el agraz, luego el racimo maduro. "
             "Ved que en poco tiempo el fruto del árbol llega a sazón.",
    (23, 5): "En verdad, pronto y de repente se cumplirá su voluntad, dando "
             "también testimonio de ello la escritura: que vendrá pronto y no "
             "tardará, y de repente vendrá el Señor a su templo, y el Santo, "
             "a quien vosotros esperáis.",

    # Capítulo 24
    (24, 1): "Consideremos, amados, cómo el Soberano nos muestra "
             "continuamente que habrá una resurrección venidera, de la cual "
             "hizo primicias al Señor Jesucristo, resucitándolo de entre los "
             "muertos.",
    (24, 2): "Veamos, amados, la resurrección que acontece a su debido "
             "tiempo.",
    (24, 3): "El día y la noche nos muestran una resurrección: la noche se "
             "duerme, el día se levanta; el día se va, la noche sobreviene.",
    (24, 4): "Tomemos los frutos: la siembra, ¿cómo y de qué manera se hace?",
    (24, 5): "Salió el sembrador y echó en la tierra cada una de las "
             "semillas; las cuales, cayendo en la tierra secas y desnudas, se "
             "descomponen; luego, de la descomposición, la grandeza de la "
             "providencia del Soberano las levanta, y de una sola hace crecer "
             "muchas y producir fruto.",

    # Capítulo 25
    (25, 1): "Veamos la señal maravillosa que acontece en las regiones de "
             "oriente, esto es, en las de alrededor de Arabia.",
    (25, 2): "Porque hay un ave que se llama fénix. Esta, siendo única en su "
             "especie, vive quinientos años; y cuando ya ha llegado al tiempo "
             "de su disolución y ha de morir, se hace un nido de incienso, y "
             "de mirra, y de los demás aromas, en el cual, cumplido el "
             "tiempo, entra y muere.",
    (25, 3): "Y pudriéndose la carne, se engendra un gusano, el cual, "
             "alimentándose de la humedad del animal muerto, echa alas; "
             "luego, hecho vigoroso, toma aquel nido donde están los huesos "
             "de su predecesor, y llevándolos hace el camino desde la tierra "
             "de Arabia hasta Egipto, a la ciudad llamada Heliópolis;",
    (25, 4): "y de día, viéndolo todos, volando sobre el altar del sol, los "
             "deposita allí, y así emprende el regreso.",
    (25, 5): "Los sacerdotes, pues, examinan los registros de los tiempos, y "
             "hallan que ha venido cumplido el año quingentésimo.",

    # Capítulo 26
    (26, 1): "¿Tendremos, pues, por cosa grande y maravillosa que el Creador "
             "de todas las cosas haga la resurrección de los que le han "
             "servido santamente con la confianza de una fe buena, cuando aun "
             "por medio de un ave nos muestra la grandeza de su promesa?",
    (26, 2): "Porque dice en cierto lugar: Y me levantarás, y te alabaré; y: "
             "Me acosté y dormí; desperté, porque tú estás conmigo.",
    (26, 3): "Y otra vez dice Job: Y resucitarás esta carne mía, que ha "
             "soportado todas estas cosas.",

    # Capítulo 27
    (27, 1): "Con esta esperanza, pues, estén ligadas nuestras almas a aquel "
             "que es fiel en sus promesas y justo en sus juicios.",
    (27, 2): "El que mandó no mentir, mucho menos mentirá él mismo; porque "
             "nada hay imposible para Dios, sino el mentir.",
    (27, 3): "Reavívese, pues, en nosotros la fe en él, y consideremos que "
             "todas las cosas están cerca de él.",
    (27, 4): "Con la palabra de su majestad estableció todas las cosas, y con "
             "una palabra puede destruirlas.",
    (27, 5): "¿Quién le dirá: Qué has hecho? ¿O quién resistirá el poder de "
             "su fuerza? Cuando quiere y como quiere hará todas las cosas, y "
             "nada de lo que él ha decretado dejará de cumplirse.",
    (27, 6): "Todas las cosas están delante de él, y nada se oculta a su "
             "consejo,",
    (27, 7): "si los cielos cuentan la gloria de Dios, y el firmamento "
             "anuncia la obra de sus manos; un día emite palabra al otro día, "
             "y una noche a otra noche declara sabiduría; no hay palabras ni "
             "discursos cuyas voces no se oigan.",

    # Capítulo 28
    (28, 1): "Puesto que todo es visto y oído, temámosle, y abandonemos los "
             "deseos impuros de las malas obras, para que por su misericordia "
             "seamos amparados de los juicios venideros.",
    (28, 2): "Porque ¿adónde podrá huir alguno de nosotros de su mano "
             "poderosa? ¿Y qué mundo recibirá a alguno de los que desertan de "
             "él?",
    (28, 3): "Porque dice en cierto lugar la escritura: ¿Adónde me iré, y "
             "dónde me esconderé de tu presencia? Si subiere al cielo, allí "
             "estás tú; si me fuere a los confines de la tierra, allí está tu "
             "diestra; si hiciere mi lecho en los abismos, allí está tu "
             "Espíritu.",
    (28, 4): "¿Adónde, pues, irá uno, o adónde huirá de aquel que abarca "
             "todas las cosas?",

    # Capítulo 29
    (29, 1): "Acerquémonos, pues, a él en santidad de alma, alzando hacia él "
             "manos puras y sin mancha, amando a nuestro Padre benigno y "
             "compasivo, que nos hizo para sí porción escogida.",
    (29, 2): "Porque así está escrito: Cuando el Altísimo repartía las "
             "naciones, cuando dispersaba a los hijos de Adán, estableció los "
             "términos de las naciones según el número de los ángeles de "
             "Dios. Su pueblo Jacob vino a ser la porción del Señor; Israel, "
             "la cuerda de su heredad.",
    (29, 3): "Y en otro lugar dice: He aquí, el Señor toma para sí una nación "
             "de en medio de las naciones, como un hombre toma las primicias "
             "de su era; y de aquella nación saldrá el Santo de los santos.",

    # Capítulo 30
    (30, 1): "Siendo, pues, porción del Santo, hagamos todo lo que es de la "
             "santificación, huyendo de las murmuraciones, de los abrazos "
             "impuros y deshonestos, de las borracheras, de las revueltas y "
             "de los deseos abominables, del inmundo adulterio, de la "
             "abominable soberbia.",
    (30, 2): "Porque Dios, dice, resiste a los soberbios, y da gracia a los "
             "humildes.",
    (30, 3): "Unámonos, pues, a aquellos a quienes ha sido dada la gracia de "
             "parte de Dios; revistámonos de la concordia, siendo humildes de "
             "ánimo y continentes, manteniéndonos lejos de toda chismografía "
             "y murmuración, justificados por obras y no por palabras.",
    (30, 4): "Porque dice: El que habla mucho, oirá también en respuesta; ¿o "
             "piensa el locuaz que es justo?",
    (30, 5): "Bendito el nacido de mujer, de pocos días. No seas abundante en "
             "palabras.",
    (30, 6): "Sea nuestra alabanza en Dios, y no de nosotros mismos; porque "
             "Dios aborrece a los que se alaban a sí mismos.",
    (30, 7): "El testimonio de nuestra buena conducta sea dado por otros, "
             "como fue dado a nuestros padres, los justos.",
    (30, 8): "La osadía, la arrogancia y el atrevimiento son de los malditos "
             "de Dios; la moderación, la humildad de ánimo y la mansedumbre "
             "están con los benditos de Dios.",

    # Capítulo 31
    (31, 1): "Unámonos, pues, a su bendición, y veamos cuáles son los caminos "
             "de la bendición. Desenvolvamos lo que aconteció desde el "
             "principio.",
    (31, 2): "¿Por qué fue bendecido nuestro padre Abrahán? ¿No fue porque "
             "obró justicia y verdad por la fe?",
    (31, 3): "Isaac, con confianza, conociendo lo que había de venir, se dejó "
             "llevar de buena gana al sacrificio.",
    (31, 4): "Jacob, con humildad, salió de su tierra a causa de su hermano, "
             "y se fue a Labán y le sirvió; y le fue dado el cetro de las "
             "doce tribus de Israel.",

    # Capítulo 32
    (32, 1): "Si alguno considera sinceramente estas cosas una por una, "
             "reconocerá la grandeza de los dones que por él fueron dados.",
    (32, 2): "Porque de él proceden todos los sacerdotes y levitas que sirven "
             "al altar de Dios; de él procede el Señor Jesús según la carne; "
             "de él, reyes y príncipes y gobernantes por la línea de Judá; y "
             "sus demás cetros no están en pequeña gloria, pues Dios había "
             "prometido: Tu simiente será como las estrellas del cielo.",
    (32, 3): "Todos ellos, pues, fueron glorificados y engrandecidos, no por "
             "sí mismos, ni por sus obras, ni por la justicia que obraron, "
             "sino por su voluntad.",
    (32, 4): "Y nosotros, pues, habiendo sido llamados por su voluntad en "
             "Cristo Jesús, no somos justificados por nosotros mismos, ni por "
             "nuestra sabiduría, o entendimiento, o piedad, o por las obras "
             "que hayamos hecho en santidad de corazón, sino por la fe, por "
             "la cual el Dios todopoderoso ha justificado a todos desde el "
             "principio; a quien sea la gloria por los siglos de los siglos. "
             "Amén.",

    # Capítulo 33
    (33, 1): "¿Qué haremos, pues, hermanos? ¿Cesaremos de hacer el bien y "
             "abandonaremos el amor? No permita el Soberano en modo alguno "
             "que esto suceda en nosotros; antes bien, apresurémonos con "
             "constancia y buen ánimo a cumplir toda buena obra.",
    (33, 2): "Porque el mismo Creador y Soberano de todas las cosas se "
             "regocija en sus obras.",
    (33, 3): "Porque con su poder inmenso afirmó los cielos, y con su "
             "entendimiento incomprensible los ordenó; y separó la tierra del "
             "agua que la rodeaba, y la asentó sobre el firme fundamento de "
             "su propia voluntad; y a los animales que andan por ella los "
             "mandó existir por su ordenación; y habiendo preparado el mar y "
             "los animales que hay en él, los encerró con su poder.",
    (33, 4): "Sobre todo, al hombre, la criatura más excelente y grandísima "
             "por su entendimiento, lo formó con sus manos santas e "
             "inmaculadas, como imagen impresa de sí mismo.",
    (33, 5): "Porque así dice Dios: Hagamos al hombre a nuestra imagen y "
             "conforme a nuestra semejanza. Y creó Dios al hombre; varón y "
             "hembra los creó.",
    (33, 6): "Habiendo, pues, acabado todas estas cosas, las alabó y las "
             "bendijo, y dijo: Creced y multiplicaos.",
    (33, 7): "Veamos que todos los justos fueron adornados de buenas obras, y "
             "el Señor mismo, habiéndose adornado de buenas obras, se "
             "regocijó.",
    (33, 8): "Teniendo, pues, este modelo, acerquémonos sin tardanza a su "
             "voluntad; con todas nuestras fuerzas obremos la obra de la "
             "justicia.",

    # Capítulo 34
    (34, 1): "El buen obrero recibe con confianza el pan de su trabajo; el "
             "perezoso y remiso no mira a la cara al que le da trabajo.",
    (34, 2): "Conviene, pues, que estemos prontos para hacer el bien; porque "
             "de él son todas las cosas.",
    (34, 3): "Porque nos avisa de antemano: He aquí el Señor, y su galardón "
             "delante de su rostro, para dar a cada uno conforme a su obra.",
    (34, 4): "Nos exhorta, pues, a nosotros que creemos en él de todo "
             "corazón, a que no seamos ociosos ni remisos para toda buena "
             "obra.",
    (34, 5): "Esté en él nuestra gloria y nuestra confianza; sometámonos a su "
             "voluntad; consideremos toda la multitud de sus ángeles, cómo, "
             "estando en pie a su lado, ministran a su voluntad.",
    (34, 6): "Porque dice la Escritura: Diez mil millares estaban delante de "
             "él, y millares de millares le ministraban, y clamaban: Santo, "
             "santo, santo es el Señor de los ejércitos; llena está toda la "
             "creación de su gloria.",
    (34, 7): "Nosotros, pues, también, reunidos en concordia en un mismo "
             "lugar con la conciencia, clamemos a él con instancia como de "
             "una sola boca, para que seamos hechos partícipes de sus grandes "
             "y gloriosas promesas.",
    (34, 8): "Porque dice: Ojo no vio, ni oreja oyó, ni subió en corazón de "
             "hombre, cuántas cosas ha preparado el Señor para los que le "
             "esperan.",

    # Capítulo 35
    (35, 1): "¡Cuán bienaventurados y maravillosos son los dones de Dios, "
             "amados!",
    (35, 2): "Vida en inmortalidad, esplendor en justicia, verdad en "
             "confianza, fe en seguridad, continencia en santificación; y "
             "todas estas cosas caían bajo nuestro entendimiento.",
    (35, 3): "¿Cuáles, pues, serán las cosas que se preparan para los que "
             "esperan? El Artífice y Padre de los siglos, el santísimo, él "
             "mismo conoce su grandeza y su hermosura.",
    (35, 4): "Luchemos, pues, nosotros por ser hallados en el número de los "
             "que esperan, para que participemos de los dones prometidos.",
    (35, 5): "¿Y cómo será esto, amados? Si nuestro entendimiento está "
             "afirmado fielmente en Dios; si buscamos las cosas que le son "
             "agradables y aceptas; si cumplimos lo que conviene a su "
             "voluntad intachable, y seguimos el camino de la verdad, "
             "desechando de nosotros toda injusticia y maldad, avaricia, "
             "contiendas, malignidades y engaños, murmuraciones y "
             "detracciones, aborrecimiento de Dios, soberbia y jactancia, "
             "vanagloria e inhospitalidad.",
    (35, 6): "Porque los que hacen estas cosas son aborrecibles a Dios; y no "
             "solamente los que las hacen, sino también los que se complacen "
             "con ellos.",
    (35, 7): "Porque dice la Escritura: Pero al pecador dijo Dios: ¿Qué "
             "tienes tú que contar mis estatutos, y tomar mi pacto en tu "
             "boca?",
    (35, 8): "Pues tú aborreciste la corrección, y echaste a tu espalda mis "
             "palabras. Si veías al ladrón, corrías con él, y con los "
             "adúlteros ponías tu parte. Tu boca multiplicaba la maldad, y tu "
             "lengua tramaba engaño. Sentado, hablabas contra tu hermano, y "
             "contra el hijo de tu madre ponías tropiezo.",
    (35, 9): "Estas cosas hiciste, y yo he callado; pensaste, inicuo, que "
             "sería yo semejante a ti.",
    (35, 10): "Te argüiré, y te las pondré delante de tu rostro.",
    (35, 11): "Entended ahora esto, los que os olvidáis de Dios; no sea que "
              "arrebate como león, y no haya quien libre.",
    (35, 12): "El sacrificio de alabanza me glorificará, y allí está el "
              "camino por el cual le mostraré la salvación de Dios.",

    # Capítulo 36
    (36, 1): "Este es el camino, amados, en el cual hallamos nuestra "
             "salvación, Jesucristo, el sumo sacerdote de nuestras ofrendas, "
             "el protector y ayudador de nuestra flaqueza.",
    (36, 2): "Por él fijamos los ojos en las alturas de los cielos; por él "
             "contemplamos como en espejo su rostro intachable y excelso; por "
             "él fueron abiertos los ojos de nuestro corazón; por él nuestro "
             "entendimiento, insensato y entenebrecido, reflorece hacia la "
             "luz; por él quiso el Soberano que gustásemos el conocimiento "
             "inmortal; el cual, siendo el resplandor de su majestad, es "
             "tanto mayor que los ángeles cuanto heredó más excelente nombre.",
    (36, 3): "Porque así está escrito: El que hace a sus ángeles espíritus, y "
             "a sus ministros llama de fuego.",
    (36, 4): "Pero acerca de su Hijo así dijo el Soberano: Mi Hijo eres tú, "
             "yo te he engendrado hoy. Pídeme, y te daré por heredad las "
             "naciones, y por posesión tuya los términos de la tierra.",
    (36, 5): "Y otra vez le dice: Siéntate a mi diestra, hasta que ponga a "
             "tus enemigos por estrado de tus pies.",
    (36, 6): "¿Quiénes son, pues, los enemigos? Los malvados y los que se "
             "oponen a su voluntad.",

    # Capítulo 37
    (37, 1): "Militemos, pues, varones hermanos, con toda instancia bajo sus "
             "mandamientos intachables.",
    (37, 2): "Consideremos a los que militan bajo nuestros gobernantes: cuán "
             "ordenadamente, cuán diestramente, cuán sumisamente cumplen lo "
             "que se les ordena.",
    (37, 3): "No todos son prefectos, ni tribunos, ni centuriones, ni jefes "
             "de cincuenta, y así sucesivamente; sino que cada uno en su "
             "propio rango cumple lo que le es mandado por el rey y por los "
             "gobernantes.",
    (37, 4): "Los grandes no pueden existir sin los pequeños, ni los pequeños "
             "sin los grandes; hay cierta mezcla en todos, y en esto está la "
             "utilidad.",
    (37, 5): "Tomemos nuestro cuerpo: la cabeza sin los pies no es nada, y "
             "así tampoco los pies sin la cabeza; y los miembros más pequeños "
             "de nuestro cuerpo son necesarios y útiles a todo el cuerpo; "
             "antes bien, todos conspiran a una y se valen de una sola "
             "sujeción para que todo el cuerpo sea salvo.",

    # Capítulo 38
    (38, 1): "Sea, pues, salvo todo nuestro cuerpo en Cristo Jesús, y "
             "sométase cada uno a su prójimo, según fue puesto en su don.",
    (38, 2): "El fuerte cuide del débil, y el débil respete al fuerte; el "
             "rico supla al pobre, y el pobre dé gracias a Dios porque le dio "
             "alguien por medio del cual sea suplida su necesidad; el sabio "
             "muestre su sabiduría no en palabras, sino en buenas obras; el "
             "humilde no dé testimonio de sí mismo, sino deje que otro dé "
             "testimonio de él; el que es casto en la carne no se jacte, "
             "sabiendo que es otro el que le suministra la continencia.",
    (38, 3): "Consideremos, pues, hermanos, de qué materia fuimos hechos; "
             "quiénes y cuáles entramos en el mundo; de qué sepulcro y "
             "tinieblas nos introdujo en su mundo el que nos formó y nos "
             "creó, habiendo preparado de antemano sus beneficios antes que "
             "nosotros naciésemos.",
    (38, 4): "Teniendo, pues, todas estas cosas de él, debemos darle gracias "
             "por todo; a él sea la gloria por los siglos de los siglos. "
             "Amén.",

    # Capítulo 39
    (39, 1): "Los insensatos, y necios, y fatuos, e indoctos se burlan de "
             "nosotros y nos escarnecen, queriendo ensalzarse a sí mismos en "
             "sus pensamientos.",
    (39, 2): "Porque ¿qué puede un mortal? ¿O qué fuerza tiene el nacido de "
             "la tierra?",
    (39, 3): "Porque está escrito: No había forma delante de mis ojos, sino "
             "que oía un soplo y una voz:",
    (39, 4): "¿Pues qué? ¿Será el mortal limpio delante del Señor? ¿O será el "
             "varón irreprensible por sus obras, si él no confía en sus "
             "siervos, y en sus ángeles notó algo torcido?",
    (39, 5): "Y el cielo no es limpio delante de él; ¡cuánto más los que "
             "habitan casas de barro, de las cuales también nosotros mismos "
             "somos, del mismo barro! Los hirió a manera de polilla, y de la "
             "mañana a la tarde ya no existen; por no poder valerse a sí "
             "mismos, perecieron.",
    (39, 6): "Sopló sobre ellos, y murieron, por no tener sabiduría.",
    (39, 7): "Llama ahora, si alguno te ha de responder, o si verás a alguno "
             "de los santos ángeles; porque al necio lo mata la ira, y al "
             "extraviado le da muerte la envidia.",
    (39, 8): "Yo he visto a los necios echar raíces, pero en seguida fue "
             "devorada su morada.",
    (39, 9): "Alejados sean sus hijos de la salvación; sean escarnecidos a "
             "las puertas de los menores, y no habrá quien los libre; porque "
             "lo que para ellos está preparado lo comerán los justos, y ellos "
             "no serán librados de los males.",

    # Capítulo 40
    (40, 1): "Siendo, pues, manifiestas para nosotros estas cosas, y habiendo "
             "penetrado en las profundidades del conocimiento divino, debemos "
             "hacer con orden todas las cosas que el Soberano mandó cumplir "
             "en tiempos señalados.",
    (40, 2): "Mandó que las ofrendas y los servicios sagrados se cumpliesen, "
             "y no al azar o sin orden, sino en tiempos y horas determinados.",
    (40, 3): "Y dónde y por quiénes quiere que se cumplan, él mismo lo "
             "determinó por su excelsa voluntad, para que, haciéndose todas "
             "las cosas santamente con beneplácito, fuesen aceptas a su "
             "voluntad.",
    (40, 4): "Así, pues, los que en los tiempos ordenados hacen sus ofrendas "
             "son aceptos y bienaventurados; porque, siguiendo las leyes del "
             "Soberano, no yerran.",
    (40, 5): "Porque al sumo sacerdote le están dados sus propios servicios, "
             "y a los sacerdotes les está señalado su propio lugar, y sobre "
             "los levitas pesan sus propios ministerios; el hombre laico está "
             "sujeto a los preceptos laicos.",

    # Capítulo 41
    (41, 1): "Cada uno de nosotros, hermanos, en su propio rango agrade a "
             "Dios, estando en buena conciencia, no traspasando la regla "
             "establecida de su servicio, con dignidad.",
    (41, 2): "No en todas partes, hermanos, se ofrecen los sacrificios "
             "perpetuos, o los de votos, o los del pecado y la transgresión, "
             "sino solamente en Jerusalén; y aun allí no se ofrece en "
             "cualquier lugar, sino delante del santuario, junto al altar, "
             "después de ser examinado en busca de defecto lo que se ofrece "
             "por el sumo sacerdote y los ministros antes dichos.",
    (41, 3): "Así, pues, los que hacen algo contra lo que conviene a su "
             "voluntad tienen por pena la muerte.",
    (41, 4): "Mirad, hermanos: cuanto mayor es el conocimiento de que hemos "
             "sido tenidos por dignos, tanto mayor es el peligro a que "
             "estamos expuestos.",

    # Capítulo 42
    (42, 1): "Los apóstoles recibieron para nosotros el evangelio de parte "
             "del Señor Jesucristo; Jesús el Cristo fue enviado de parte de "
             "Dios.",
    (42, 2): "Así, pues, Cristo viene de Dios, y los apóstoles de Cristo; "
             "ambas cosas, pues, sucedieron ordenadamente por voluntad de "
             "Dios.",
    (42, 3): "Habiendo, pues, recibido los mandatos, y estando plenamente "
             "certificados por la resurrección de nuestro Señor Jesucristo, y "
             "confirmados en la fe por la palabra de Dios, salieron con la "
             "plena certidumbre del Espíritu Santo, anunciando la buena nueva "
             "de que el reino de Dios estaba por venir.",
    (42, 4): "Predicando, pues, por regiones y ciudades, establecían a sus "
             "primicias, después de probarlas por el Espíritu, por obispos y "
             "diáconos de los que habían de creer.",
    (42, 5): "Y esto no era cosa nueva, porque desde hacía mucho tiempo se "
             "había escrito acerca de obispos y diáconos. Porque así dice en "
             "cierto lugar la Escritura: Estableceré a sus obispos en "
             "justicia, y a sus diáconos en fe.",

    # Capítulo 43
    (43, 1): "¿Y qué maravilla es que los que en Cristo fueron encargados por "
             "Dios de tal obra establecieran a los antes dichos? Pues también "
             "el bienaventurado Moisés, siervo fiel en toda la casa, anotó en "
             "los libros sagrados todas las cosas que le fueron ordenadas; al "
             "cual siguieron también los demás profetas, dando juntamente "
             "testimonio de lo que por él había sido legislado.",
    (43, 2): "Porque él, habiendo surgido celos acerca del sacerdocio, y "
             "estando en sedición las tribus sobre cuál de ellas sería "
             "adornada con aquel nombre glorioso, mandó a los doce jefes de "
             "tribu que le trajesen varas, en las que estuviera escrito el "
             "nombre de cada tribu; y tomándolas, las ató y las selló con los "
             "anillos de los jefes de tribu, y las depositó en el tabernáculo "
             "del testimonio sobre la mesa de Dios.",
    (43, 3): "Y cerrando el tabernáculo, selló las llaves, del mismo modo que "
             "las varas,",
    (43, 4): "y les dijo: Varones hermanos, la tribu cuya vara brotare, a "
             "esta ha escogido Dios para que ejerza el sacerdocio y le "
             "ministre.",
    (43, 5): "Y venida la mañana, convocó a todo Israel, los seiscientos mil "
             "varones, y mostró a los jefes de tribu los sellos, y abrió el "
             "tabernáculo del testimonio y sacó las varas; y fue hallada la "
             "vara de Aarón no solamente brotada, sino que también tenía "
             "fruto.",
    (43, 6): "¿Qué os parece, amados? ¿No sabía de antemano Moisés que esto "
             "había de suceder? Muy bien lo sabía; pero, para que no hubiese "
             "desorden en Israel, así lo hizo, a fin de que fuese glorificado "
             "el nombre del verdadero y único Dios; al cual sea la gloria por "
             "los siglos de los siglos. Amén.",

    # Capítulo 44
    (44, 1): "También nuestros apóstoles supieron por nuestro Señor "
             "Jesucristo que habría contienda sobre el nombre del episcopado.",
    (44, 2): "Por esta causa, pues, habiendo recibido perfecto conocimiento "
             "de antemano, establecieron a los antes dichos, y después dieron "
             "la disposición de que, si ellos durmiesen, otros varones "
             "probados recibiesen en sucesión su servicio.",
    (44, 3): "A los que, pues, fueron establecidos por ellos, o después por "
             "otros varones eminentes, con el consentimiento de toda la "
             "iglesia, y que han servido al rebaño de Cristo sin reproche, "
             "con humildad, sosegadamente y sin vileza, y que han recibido "
             "buen testimonio de todos durante mucho tiempo, a estos no "
             "tenemos por justo que se les expulse del servicio.",
    (44, 4): "Porque no pequeño pecado será el nuestro si expulsamos del "
             "episcopado a los que sin reproche y santamente han ofrecido los "
             "dones.",
    (44, 5): "Bienaventurados los presbíteros que nos han precedido en el "
             "camino, los cuales tuvieron una partida fructuosa y perfecta; "
             "porque no temen que nadie los remueva del lugar que les fue "
             "asignado.",
    (44, 6): "Porque vemos que vosotros habéis removido a algunos que se "
             "conducían bien, del servicio que sin reproche habían honrado.",

    # Capítulo 45
    (45, 1): "Sed contenciosos, hermanos, y celosos por las cosas que atañen "
             "a la salvación.",
    (45, 2): "Habéis escudriñado las Sagradas Escrituras, las verdaderas, las "
             "que son por el Espíritu Santo.",
    (45, 3): "Sabéis que nada injusto ni falsificado está escrito en ellas. "
             "No hallaréis que los justos hayan sido desechados por varones "
             "santos.",
    (45, 4): "Fueron perseguidos los justos, pero por los inicuos; fueron "
             "encarcelados, pero por los impíos; fueron apedreados por los "
             "transgresores; fueron muertos por los que habían concebido un "
             "celo abominable e injusto.",
    (45, 5): "Padeciendo estas cosas, las soportaron gloriosamente.",
    (45, 6): "Porque ¿qué diremos, hermanos? ¿Fue Daniel echado en el foso de "
             "los leones por los que temían a Dios?",
    (45, 7): "¿O fueron Ananías, y Azarías, y Misael encerrados en el horno "
             "de fuego por los que practicaban el culto magnífico y glorioso "
             "del Altísimo? En ninguna manera sea tal cosa. ¿Quiénes, pues, "
             "fueron los que hicieron estas cosas? Los aborrecibles y llenos "
             "de toda maldad llegaron a tal extremo de furor, que sometieron "
             "a tormento a los que con propósito santo e intachable servían a "
             "Dios, no sabiendo que el Altísimo es defensor y escudo de los "
             "que con conciencia pura rinden culto a su nombre excelentísimo; "
             "al cual sea la gloria por los siglos de los siglos. Amén.",
    (45, 8): "Mas los que perseveraron con confianza heredaron gloria y "
             "honra, y fueron ensalzados, y quedaron inscritos por Dios en su "
             "memoria por los siglos de los siglos. Amén.",

    # Capítulo 46
    (46, 1): "A tales ejemplos, pues, es necesario que también nosotros nos "
             "adhiramos, hermanos.",
    (46, 2): "Porque está escrito: Adheríos a los santos, porque los que se "
             "adhieren a ellos serán santificados.",
    (46, 3): "Y otra vez en otro lugar dice: Con el varón inocente serás "
             "inocente, y con el escogido serás escogido, y con el perverso "
             "te pervertirás.",
    (46, 4): "Adhirámonos, pues, a los inocentes y justos; y estos son los "
             "escogidos de Dios.",
    (46, 5): "¿Por qué hay entre vosotros contiendas, y enojos, y "
             "disensiones, y cismas, y guerra?",
    (46, 6): "¿O no tenemos un solo Dios, y un solo Cristo, y un solo "
             "Espíritu de gracia derramado sobre nosotros? ¿Y no es una sola "
             "la vocación en Cristo?",
    (46, 7): "¿Por qué desgarramos y despedazamos los miembros de Cristo, y "
             "nos sublevamos contra nuestro propio cuerpo, y llegamos a tal "
             "locura que nos olvidamos de que somos miembros los unos de los "
             "otros? Acordaos de las palabras del Señor Jesús.",
    (46, 8): "Porque dijo: ¡Ay de aquel hombre! Bueno le fuera no haber "
             "nacido, antes que escandalizar a uno de mis escogidos; mejor le "
             "fuera que se le colgase una piedra de molino y fuese hundido en "
             "el mar, antes que pervertir a uno de mis escogidos.",
    (46, 9): "Vuestro cisma ha pervertido a muchos, a muchos ha echado en el "
             "desaliento, a muchos en la duda, a todos nosotros en la "
             "tristeza; y vuestra sedición persiste.",

    # Capítulo 47
    (47, 1): "Tomad la epístola del bienaventurado Pablo el apóstol.",
    (47, 2): "¿Qué os escribió primero, en el principio del evangelio?",
    (47, 3): "En verdad os escribió inspirado por el Espíritu acerca de sí "
             "mismo, y de Cefas, y de Apolos, porque ya entonces habíais "
             "formado parcialidades.",
    (47, 4): "Pero aquella parcialidad os acarreó menor pecado; porque os "
             "inclinasteis a apóstoles acreditados y a un varón probado por "
             "ellos.",
    (47, 5): "Pero ahora considerad quiénes os han pervertido y han "
             "menoscabado la dignidad de vuestro renombrado amor fraternal.",
    (47, 6): "Cosa vergonzosa es, amados, y muy vergonzosa, e indigna de la "
             "conducta en Cristo, oír que la firmísima y antigua iglesia de "
             "los corintios, por causa de una o dos personas, se subleva "
             "contra los presbíteros.",
    (47, 7): "Y este rumor no solamente ha llegado a nosotros, sino también a "
             "los que son de otra inclinación que nosotros, de modo que aun "
             "se profieren blasfemias contra el nombre del Señor por causa de "
             "vuestra insensatez, y os acarreáis peligro a vosotros mismos.",

    # Capítulo 48
    (48, 1): "Quitemos, pues, esto prontamente, y postrémonos ante el "
             "Soberano, y lloremos suplicándole que, hecho propicio, se "
             "reconcilie con nosotros y nos restituya a la conducta digna y "
             "pura de nuestro amor fraternal.",
    (48, 2): "Porque esta es la puerta de la justicia abierta para la vida, "
             "como está escrito: Abridme las puertas de la justicia; entraré "
             "por ellas, y alabaré al Señor.",
    (48, 3): "Esta es la puerta del Señor; los justos entrarán por ella.",
    (48, 4): "Habiendo, pues, muchas puertas abiertas, la que es de justicia, "
             "esta es la que es en Cristo, en la cual son bienaventurados "
             "todos los que entran y enderezan su camino en santidad y "
             "justicia, cumpliendo todas las cosas sin turbación.",
    (48, 5): "Sea alguno fiel, sea capaz de declarar conocimiento, sea sabio "
             "en el discernimiento de las palabras, sea puro en las obras;",
    (48, 6): "porque tanto más debe ser humilde, cuanto más parece ser mayor, "
             "y buscar lo que es de provecho común para todos, y no lo suyo "
             "propio.",

    # Capítulo 49
    (49, 1): "El que tiene amor en Cristo, cumpla los mandamientos de Cristo.",
    (49, 2): "¿Quién puede explicar el vínculo del amor de Dios?",
    (49, 3): "¿Quién es suficiente para declarar la magnificencia de su "
             "hermosura?",
    (49, 4): "La altura a la cual conduce el amor es inefable.",
    (49, 5): "El amor nos une a Dios; el amor cubre multitud de pecados; el "
             "amor todo lo soporta, todo lo sufre con paciencia; nada vil hay "
             "en el amor, nada soberbio; el amor no tiene cisma, el amor no "
             "se subleva, el amor hace todas las cosas en concordia; en el "
             "amor fueron perfeccionados todos los escogidos de Dios; sin "
             "amor nada es agradable a Dios.",
    (49, 6): "En amor nos tomó para sí el Soberano; por el amor que tuvo para "
             "con nosotros, Jesucristo nuestro Señor dio su sangre por "
             "nosotros por voluntad de Dios, y su carne por nuestra carne, y "
             "su alma por nuestras almas.",

    # Capítulo 50
    (50, 1): "Mirad, amados, cuán grande y maravilloso es el amor, y de su "
             "perfección no hay explicación.",
    (50, 2): "¿Quién es capaz de ser hallado en él, sino aquellos a quienes "
             "Dios tuviere por dignos? Roguemos, pues, y pidamos de su "
             "misericordia que seamos hallados en amor, sin parcialidad "
             "humana, intachables.",
    (50, 3): "Todas las generaciones desde Adán hasta el día de hoy han "
             "pasado; pero los que fueron perfeccionados en amor, según la "
             "gracia de Dios, tienen el lugar de los piadosos; los cuales "
             "serán manifestados en la visitación del reino de Cristo.",
    (50, 4): "Porque está escrito: Entrad en las cámaras por un breve "
             "momento, hasta que pase mi ira y mi furor, y me acordaré del "
             "día bueno, y os levantaré de vuestros sepulcros.",
    (50, 5): "Bienaventurados somos, amados, si cumplimos los mandamientos de "
             "Dios en la concordia del amor, para que por el amor nos sean "
             "perdonados los pecados.",
    (50, 6): "Porque está escrito: Bienaventurados aquellos cuyas iniquidades "
             "son perdonadas, y cuyos pecados son cubiertos. Bienaventurado "
             "el varón a quien el Señor no imputará pecado, ni hay engaño en "
             "su boca.",
    (50, 7): "Esta bienaventuranza vino sobre los que han sido escogidos por "
             "Dios por medio de Jesucristo nuestro Señor; al cual sea la "
             "gloria por los siglos de los siglos. Amén.",

    # Capítulo 51
    (51, 1): "Todo cuanto, pues, hemos transgredido y hecho por algunas "
             "asechanzas del adversario, pidamos que nos sea perdonado. Y "
             "también aquellos que fueron cabecillas de la sedición y la "
             "disensión deben mirar a lo que es común a nuestra esperanza.",
    (51, 2): "Porque los que andan con temor y amor quieren más caer ellos "
             "mismos en tormentos que no sus prójimos; y prefieren sufrir la "
             "condenación de sí mismos antes que la de la concordia que nos "
             "ha sido transmitida bien y justamente.",
    (51, 3): "Porque mejor le es al hombre confesar sus transgresiones que "
             "endurecer su corazón, como se endureció el corazón de los que "
             "se sublevaron contra Moisés, el siervo de Dios, cuyo juicio fue "
             "manifiesto;",
    (51, 4): "porque descendieron vivos al Hades, y la muerte los pastoreará.",
    (51, 5): "Faraón y su ejército, y todos los príncipes de Egipto, los "
             "carros y los que en ellos subían, no por otra causa fueron "
             "sumergidos en el mar Rojo y perecieron, sino porque se "
             "endurecieron sus corazones insensatos después de haberse hecho "
             "las señales y los prodigios en la tierra de Egipto por medio de "
             "Moisés, el siervo de Dios.",

    # Capítulo 52
    (52, 1): "El Soberano de todas las cosas, hermanos, no tiene necesidad de "
             "nada; nada pide de nadie, sino que se le confiese.",
    (52, 2): "Porque dice el escogido David: Confesaré al Señor, y le "
             "agradará más que un becerro nuevo que echa cuernos y pezuñas. "
             "Véanlo los pobres, y alégrense.",
    (52, 3): "Y otra vez dice: Sacrifica a Dios sacrificio de alabanza, y "
             "paga tus votos al Altísimo; e invócame en el día de tu "
             "angustia, y te libraré, y tú me glorificarás.",
    (52, 4): "Porque sacrificio para Dios es el espíritu quebrantado.",

    # Capítulo 53
    (53, 1): "Porque conocéis, y bien conocéis, las Sagradas Escrituras, "
             "amados, y habéis escudriñado los oráculos de Dios. Así, pues, "
             "escribimos estas cosas para recordároslas.",
    (53, 2): "Porque habiendo subido Moisés al monte, y habiendo pasado "
             "cuarenta días y cuarenta noches en ayuno y humillación, le dijo "
             "Dios: Desciende pronto de aquí, porque tu pueblo, que sacaste "
             "de la tierra de Egipto, ha obrado inicuamente; pronto se han "
             "apartado del camino que tú les mandaste; se han hecho imágenes "
             "de fundición.",
    (53, 3): "Y le dijo el Señor: Te he hablado una y dos veces, diciendo: He "
             "visto a este pueblo, y he aquí que es de dura cerviz; déjame "
             "que los destruya, y borraré su nombre de debajo del cielo, y te "
             "haré a ti una nación grande y maravillosa, y mucho más numerosa "
             "que esta.",
    (53, 4): "Y dijo Moisés: De ninguna manera, Señor; perdona el pecado a "
             "este pueblo, o bórrame también a mí del libro de los vivientes.",
    (53, 5): "¡Oh gran amor! ¡Oh perfección insuperable! Habla el siervo con "
             "confianza a su Señor; pide perdón para la multitud, o pide que "
             "también él sea borrado con ellos.",

    # Capítulo 54
    (54, 1): "¿Quién, pues, entre vosotros es noble, quién compasivo, quién "
             "está lleno de amor?",
    (54, 2): "Diga: Si por causa mía hay sedición, y contienda, y cismas, me "
             "retiro, me voy adonde queráis, y hago lo que me sea mandado por "
             "la multitud; con tal que el rebaño de Cristo tenga paz con los "
             "presbíteros establecidos.",
    (54, 3): "El que hiciere esto se ganará gran gloria en Cristo, y todo "
             "lugar le recibirá; porque del Señor es la tierra y su plenitud.",
    (54, 4): "Estas cosas hicieron y harán los que viven como ciudadanos de "
             "la ciudadanía de Dios, de la cual no hay que arrepentirse.",

    # Capítulo 55
    (55, 1): "Y para que traigamos también ejemplos de los gentiles: muchos "
             "reyes y gobernantes, sobreviniendo algún tiempo de pestilencia, "
             "habiendo recibido un oráculo, se entregaron a la muerte para "
             "librar a sus ciudadanos por medio de su propia sangre; muchos "
             "se retiraron de sus propias ciudades, para que no hubiese más "
             "sediciones.",
    (55, 2): "Sabemos de muchos entre nosotros que se han entregado a sí "
             "mismos a las cadenas para rescatar a otros; muchos se "
             "entregaron a sí mismos a la esclavitud, y, recibiendo su "
             "precio, alimentaron a otros.",
    (55, 3): "Muchas mujeres, fortalecidas por la gracia de Dios, llevaron a "
             "cabo muchas hazañas varoniles.",
    (55, 4): "La bienaventurada Judit, estando la ciudad sitiada, pidió a los "
             "ancianos que se le permitiese salir al campamento de los "
             "extranjeros.",
    (55, 5): "Entregándose, pues, al peligro, salió por amor de su patria y "
             "del pueblo que estaba sitiado; y el Señor entregó a Holofernes "
             "en mano de una mujer.",
    (55, 6): "No menos también Ester, perfecta en la fe, se expuso al peligro "
             "para librar a la nación de Israel, que estaba a punto de "
             "perecer; porque por su ayuno y su humillación suplicó al "
             "Soberano de los siglos, que todo lo ve; el cual, viendo la "
             "humildad de su alma, libró al pueblo por causa del cual ella se "
             "había puesto en peligro.",

    # Capítulo 56
    (56, 1): "Intercedamos, pues, también nosotros por los que están en "
             "alguna transgresión, para que les sea dada mansedumbre y "
             "humildad, a fin de que cedan, no a nosotros, sino a la voluntad "
             "de Dios; porque así les será fructuoso y perfecto el recuerdo "
             "que con misericordias se haga de ellos ante Dios y ante los "
             "santos.",
    (56, 2): "Recibamos la corrección, de la cual nadie debe indignarse, "
             "amados. La amonestación que nos hacemos unos a otros es buena y "
             "sobremanera provechosa, porque nos une a la voluntad de Dios.",
    (56, 3): "Porque así dice la santa palabra: Castigóme gravemente el "
             "Señor, mas no me entregó a la muerte.",
    (56, 4): "Porque el Señor al que ama castiga, y azota a todo el que "
             "recibe por hijo.",
    (56, 5): "Porque el justo, dice, me corregirá con misericordia y me "
             "reprenderá; pero el aceite de los pecadores no unja mi cabeza.",
    (56, 6): "Y otra vez dice: Bienaventurado el hombre a quien el Señor ha "
             "reprendido; no menosprecies, pues, la amonestación del "
             "Todopoderoso; porque él es el que hace la llaga, y él la "
             "vendará;",
    (56, 7): "él hirió, y sus manos curaron.",
    (56, 8): "En seis angustias te librará, y en la séptima no te tocará el "
             "mal.",
    (56, 9): "En el hambre te librará de la muerte, y en la guerra te soltará "
             "de la mano del hierro;",
    (56, 10): "y del azote de la lengua te esconderá, y no temerás los males "
              "que vienen.",
    (56, 11): "De los injustos y los inicuos te reirás, y no temerás de las "
              "bestias fieras;",
    (56, 12): "porque las bestias fieras tendrán paz contigo.",
    (56, 13): "Luego sabrás que tu casa tendrá paz, y la morada de tu tienda "
              "no fallará.",
    (56, 14): "Y sabrás que tu simiente es mucha, y tus hijos como toda la "
              "hierba del campo.",
    (56, 15): "Y vendrás al sepulcro como el trigo maduro segado a su tiempo, "
              "o como el montón de la era recogido a su hora.",
    (56, 16): "Veis, amados, cuán grande protección hay para los que son "
              "corregidos por el Soberano; porque, siendo Padre bueno, nos "
              "corrige para que alcancemos misericordia por medio de su santa "
              "corrección.",

    # Capítulo 57
    (57, 1): "Vosotros, pues, los que pusisteis el fundamento de la sedición, "
             "someteos a los presbíteros, y recibid corrección para "
             "arrepentimiento, doblando las rodillas de vuestro corazón.",
    (57, 2): "Aprended a someteros, desechando la arrogancia jactanciosa y "
             "soberbia de vuestra lengua; porque mejor os es ser hallados "
             "pequeños y estimados en el rebaño de Cristo, que, pareciendo "
             "ser eminentes, ser echados fuera de su esperanza.",
    (57, 3): "Porque así dice la Sabiduría excelentísima: He aquí, os "
             "derramaré la palabra de mi espíritu, y os enseñaré mi palabra.",
    (57, 4): "Por cuanto llamé, y no me obedecisteis; extendí mis palabras, y "
             "no atendisteis, sino que tuvisteis en nada mis consejos, y "
             "fuisteis desobedientes a mis reprensiones; por tanto, también "
             "yo me reiré en vuestra perdición, y me burlaré cuando os "
             "viniere la ruina, y cuando os sobreviniere de repente la "
             "turbación, y la destrucción se presentare como un torbellino, o "
             "cuando os viniere tribulación y asedio.",
    (57, 5): "Porque sucederá que cuando me invocareis, yo no os escucharé; "
             "me buscarán los malos, y no me hallarán. Porque aborrecieron la "
             "sabiduría, y no escogieron el temor del Señor, ni quisieron "
             "atender a mis consejos, sino que escarnecieron mis "
             "reprensiones.",
    (57, 6): "Por tanto, comerán el fruto de su propio camino, y se hartarán "
             "de su propia impiedad.",
    (57, 7): "Porque, por cuanto hacían injusticia a los niños, serán "
             "muertos, y el examen destruirá a los impíos; mas el que me oye "
             "habitará confiado en la esperanza, y reposará sin temor de todo "
             "mal.",

    # Capítulo 58
    (58, 1): "Obedezcamos, pues, a su nombre santísimo y glorioso, huyendo de "
             "las amenazas antes dichas por la Sabiduría contra los "
             "desobedientes, para que habitemos confiados en el nombre "
             "santísimo de su majestad.",
    (58, 2): "Recibid nuestro consejo, y no tendréis de qué arrepentiros. "
             "Porque vive Dios, y vive el Señor Jesucristo, y el Espíritu "
             "Santo, la fe y la esperanza de los escogidos, que el que "
             "cumpliere con humildad, con constante mansedumbre, sin "
             "arrepentirse, los estatutos y mandamientos dados por Dios, este "
             "será ordenado y contado en el número de los que son salvos por "
             "medio de Jesucristo, por el cual sea a él la gloria por los "
             "siglos de los siglos. Amén.",

    # Capítulo 59
    (59, 1): "Pero si algunos desobedecieren a las cosas que por él han sido "
             "dichas por medio de nosotros, sepan que se enredarán en "
             "transgresión y en no pequeño peligro.",
    (59, 2): "Mas nosotros seremos inocentes de este pecado, y pediremos, "
             "haciendo con instancia oración y súplica, que el Artífice de "
             "todas las cosas guarde intacto el número contado de sus "
             "escogidos en todo el mundo, por medio de su amado Siervo "
             "Jesucristo, por el cual nos llamó de las tinieblas a la luz, de "
             "la ignorancia al conocimiento de la gloria de su nombre,",
    (59, 3): "[…] a esperar en tu nombre, principio de toda criatura, "
             "habiendo abierto los ojos de nuestro corazón para que te "
             "conozcamos a ti, el único Altísimo en las alturas, el Santo que "
             "reposa entre los santos; el que abate la insolencia de los "
             "soberbios, el que deshace los designios de las naciones, el que "
             "pone en alto a los humildes y abate a los altivos, el que "
             "enriquece y empobrece, el que mata y da vida; el único Hallador "
             "de los espíritus y Dios de toda carne; el que mira en los "
             "abismos, el que observa las obras de los hombres, el ayudador "
             "de los que están en peligro, el salvador de los desesperados, "
             "el Creador y Obispo de todo espíritu; el que multiplica las "
             "naciones sobre la tierra, y de entre todas escogió a los que te "
             "aman por medio de Jesucristo, tu amado Siervo, por el cual nos "
             "instruiste, nos santificaste, nos honraste.",
    (59, 4): "Te rogamos, Soberano, que seas nuestro ayudador y amparo. Salva "
             "a los que de entre nosotros están en tribulación; ten "
             "misericordia de los humildes; levanta a los caídos; muéstrate a "
             "los necesitados; sana a los enfermos; haz volver a los "
             "extraviados de tu pueblo; sacia a los hambrientos; rescata a "
             "nuestros presos; levanta a los débiles; consuela a los de poco "
             "ánimo. Conózcante todas las naciones, que tú eres el único "
             "Dios, y Jesucristo tu Siervo, y nosotros tu pueblo y ovejas de "
             "tu prado.",

    # Capítulo 60
    (60, 1): "Porque tú, por medio de tus obras, manifestaste la perpetua "
             "constitución del mundo; tú, Señor, creaste la tierra habitada; "
             "tú, el fiel en todas las generaciones, justo en tus juicios, "
             "admirable en fortaleza y magnificencia, el sabio en crear y el "
             "entendido en afirmar lo que fue hecho, el bueno en las cosas "
             "que se ven y benigno para con los que confían en ti; "
             "misericordioso y compasivo, perdónanos nuestras iniquidades, y "
             "nuestras injusticias, y nuestras transgresiones y faltas.",
    (60, 2): "No tomes en cuenta todo pecado de tus siervos y siervas, sino "
             "purifícanos con la purificación de tu verdad, y endereza "
             "nuestros pasos para que andemos en santidad de corazón, y "
             "hagamos las cosas buenas y agradables delante de ti y delante "
             "de nuestros gobernantes.",
    (60, 3): "Sí, Soberano, haz resplandecer tu rostro sobre nosotros para "
             "bien en paz, para que seamos protegidos por tu mano poderosa y "
             "librados de todo pecado por tu brazo excelso; y líbranos de los "
             "que nos aborrecen sin causa.",
    (60, 4): "Da concordia y paz a nosotros y a todos los que habitan la "
             "tierra, como la diste a nuestros padres, cuando te invocaban "
             "santamente en fe y verdad, para que seamos obedientes a tu "
             "nombre todopoderoso y glorioso, y a nuestros príncipes y "
             "gobernantes sobre la tierra.",

    # Capítulo 61
    (61, 1): "Tú, Soberano, les diste la potestad del reino por tu poder "
             "magnífico e inefable, para que nosotros, conociendo la gloria y "
             "la honra que por ti les ha sido dada, nos sometamos a ellos, "
             "sin oponernos en nada a tu voluntad. Dales, Señor, salud, paz, "
             "concordia, estabilidad, para que ejerzan sin tropiezo el "
             "gobierno que por ti les ha sido dado.",
    (61, 2): "Porque tú, Soberano celestial, Rey de los siglos, das a los "
             "hijos de los hombres gloria y honra y potestad sobre las cosas "
             "que hay sobre la tierra; tú, Señor, endereza su consejo "
             "conforme a lo que es bueno y agradable delante de ti, para que, "
             "ejerciendo piadosamente en paz y mansedumbre la potestad que "
             "por ti les ha sido dada, te hallen propicio.",
    (61, 3): "A ti, el único que puede hacer estas cosas y bienes más "
             "abundantes con nosotros, te confesamos por medio del sumo "
             "sacerdote y protector de nuestras almas, Jesucristo, por el "
             "cual a ti sea la gloria y la majestad, ahora y de generación en "
             "generación, y por los siglos de los siglos. Amén.",

    # Capítulo 62
    (62, 1): "Acerca de las cosas que atañen a nuestro culto, y de las más "
             "provechosas para una vida virtuosa a los que quieren conducirse "
             "piadosa y justamente, os hemos escrito suficientemente, varones "
             "hermanos.",
    (62, 2): "Porque acerca de la fe, y del arrepentimiento, y del amor "
             "sincero, y de la continencia, y de la templanza, y de la "
             "paciencia, hemos tocado todo punto, recordándoos que debéis "
             "agradar santamente al Dios todopoderoso en justicia, y verdad, "
             "y longanimidad, viviendo en concordia, sin guardar rencor, en "
             "amor y paz, con constante mansedumbre, así como también "
             "nuestros padres antes mencionados le agradaron, siendo humildes "
             "para con el Padre y Dios Creador y para con todos los hombres.",
    (62, 3): "Y os hemos recordado estas cosas con tanto mayor gusto, porque "
             "sabíamos bien que escribíamos a varones fieles y muy estimados, "
             "que habían escudriñado los oráculos de la enseñanza de Dios.",

    # Capítulo 63
    (63, 1): "Justo es, pues, que, acercándonos a tales y tantos ejemplos, "
             "inclinemos el cuello y ocupemos el lugar de la obediencia, para "
             "que, cesando de la vana sedición, lleguemos sin mancha alguna a "
             "la meta que en verdad nos está propuesta.",
    (63, 2): "Porque nos daréis gozo y alegría si, obedeciendo a lo que os "
             "hemos escrito por medio del Espíritu Santo, cortáis la ira "
             "ilícita de vuestro celo, conforme a la súplica que hemos hecho "
             "por la paz y la concordia en esta epístola.",
    (63, 3): "Y hemos enviado varones fieles y prudentes, que desde la "
             "juventud hasta la vejez han vivido entre nosotros sin reproche, "
             "los cuales serán también testigos entre vosotros y nosotros.",
    (63, 4): "Y esto lo hemos hecho para que sepáis que todo nuestro cuidado "
             "ha sido y es que pronto tengáis paz.",

    # Capítulo 64
    (64, 1): "Por lo demás, el Dios que todo lo ve, y Soberano de los "
             "espíritus, y Señor de toda carne, que escogió al Señor "
             "Jesucristo, y a nosotros por medio de él para ser un pueblo "
             "propio, dé a toda alma que ha invocado su nombre magnífico y "
             "santo fe, temor, paz, paciencia y longanimidad, continencia, "
             "pureza, templanza, para agradar a su nombre, por medio de "
             "nuestro sumo sacerdote y protector Jesucristo, por el cual sea "
             "a él gloria y majestad, poder y honra, ahora y por todos los "
             "siglos de los siglos. Amén.",

    # Capítulo 65
    (65, 1): "Y a los que os hemos enviado, Claudio Efebo y Valerio Bitón, "
             "juntamente con Fortunato, devolvédnoslos pronto en paz y con "
             "gozo, para que cuanto antes nos anuncien la paz y la concordia "
             "por nosotros rogada y deseada, a fin de que también nosotros "
             "nos gocemos más pronto de vuestra estabilidad.",
    (65, 2): "La gracia de nuestro Señor Jesucristo sea con vosotros y con "
             "todos, en todo lugar, los que han sido llamados por Dios por "
             "medio de él; por el cual sea a él gloria, honra, poder y "
             "majestad, trono eterno, desde los siglos hasta los siglos de "
             "los siglos. Amén. Epístola de los romanos a los corintios.",
}
