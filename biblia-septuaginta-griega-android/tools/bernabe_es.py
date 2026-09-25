"""La Carta de Bernabé, traducida del griego.

No es de Bernabé, el compañero de Pablo; es de un cristiano de Alejandría, de
hacia el año 130. Lee el Antiguo Testamento como una alegoría continua de
Cristo —los 318 siervos de Abraham son, en letras griegas, la cruz y el nombre
de Jesús (9)— y sostiene que los judíos nunca entendieron su propia ley. Esa
polémica se traduce tal como está. Termina con los dos caminos, como la
Didaché.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

BERNABE_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 1): "Salud, hijos e hijas, en el nombre del Señor que nos amó, en "
            "paz.",
    (1, 2): "Siendo grandes y ricas las ordenanzas de Dios para con vosotros, "
            "me regocijo sobremanera y en extremo por vuestros espíritus "
            "bienaventurados y gloriosos: tan arraigada es la gracia del don "
            "espiritual que habéis recibido.",
    (1, 3): "Por eso me congratulo aún más conmigo mismo, esperando ser "
            "salvo, porque verdaderamente veo en vosotros el Espíritu "
            "derramado sobre vosotros de la riqueza de la fuente del Señor. "
            "Tanto me asombró, en cuanto a vosotros, vuestra vista tan "
            "deseada por mí.",
    (1, 4): "Persuadido, pues, de esto, y teniendo conciencia de que, "
            "habiendo hablado mucho entre vosotros, sé que el Señor me "
            "acompañó en el camino de la justicia, me siento también yo del "
            "todo constreñido a esto: a amaros más que a mi propia alma, "
            "porque grande fe y amor habitan en vosotros en la esperanza de "
            "su vida.",
    (1, 5): "Considerando, pues, esto, que si me ocupo de vosotros para "
            "comunicaros alguna parte de lo que he recibido, me será en "
            "recompensa haber servido a tales espíritus, me apresuré a "
            "escribiros brevemente, para que junto con vuestra fe tengáis "
            "también perfecto el conocimiento.",
    (1, 6): "Tres son, pues, las enseñanzas del Señor: la esperanza de la "
            "vida, principio y fin de nuestra fe; y la justicia, principio y "
            "fin del juicio; el amor de la alegría y del regocijo, testimonio "
            "de las obras de justicia.",
    (1, 7): "Porque el Soberano nos dio a conocer por los profetas las cosas "
            "pasadas y las presentes, y nos dio a gustar las primicias de las "
            "venideras; y viendo que estas se cumplen una por una, como él "
            "habló, debemos acercarnos con más riqueza y más elevación a su "
            "temor.",
    (1, 8): "Pero yo, no como maestro, sino como uno de vosotros, os mostraré "
            "unas pocas cosas por las cuales os alegraréis en las "
            "circunstancias presentes.",

    # Capítulo 2
    (2, 1): "Siendo, pues, malos los días, y teniendo el poder el mismo que "
            "obra, debemos, atendiendo a nosotros mismos, buscar con "
            "diligencia las ordenanzas del Señor.",
    (2, 2): "Los auxiliares de nuestra fe son, pues, el temor y la paciencia, "
            "y los que combaten a nuestro lado, la longanimidad y la "
            "continencia.",
    (2, 3): "Permaneciendo estas cosas puras en lo que mira al Señor, se "
            "regocijan juntamente con ellas la sabiduría, la inteligencia, la "
            "ciencia y el conocimiento.",
    (2, 4): "Porque nos ha manifestado por todos los profetas que no tiene "
            "necesidad ni de sacrificios, ni de holocaustos, ni de ofrendas, "
            "diciendo en un lugar:",
    (2, 5): "¿Para qué me sirve la multitud de vuestros sacrificios?, dice el "
            "Señor. Harto estoy de holocaustos, y no quiero sebo de corderos, "
            "ni sangre de toros y de machos cabríos, ni aunque vengáis a "
            "presentaros delante de mí; porque ¿quién demandó esto de "
            "vuestras manos? No volveréis a hollar mis atrios. Si traéis flor "
            "de harina, es vano; el incienso me es abominación; vuestras "
            "lunas nuevas y vuestros sábados no los soporto.",
    (2, 6): "Estas cosas, pues, las abolió, para que la nueva ley de nuestro "
            "Señor Jesucristo, que está sin yugo de necesidad, no tenga una "
            "ofrenda hecha por hombres.",
    (2, 7): "Y otra vez les dice: ¿Acaso mandé yo a vuestros padres, cuando "
            "salían de la tierra de Egipto, que me ofrecieran holocaustos y "
            "sacrificios?",
    (2, 8): "Antes bien, esto les mandé: Ninguno de vosotros guarde en su "
            "corazón rencor contra su prójimo, y no améis el juramento falso.",
    (2, 9): "Debemos, pues, entender, no siendo insensatos, la intención de "
            "la bondad de nuestro Padre, porque nos habla a nosotros, "
            "queriendo que, no extraviados como aquellos, busquemos cómo "
            "acercarnos a él.",
    (2, 10): "A nosotros, pues, nos dice así: Sacrificio para el Señor es un "
             "corazón quebrantado; olor de suavidad para el Señor es un "
             "corazón que glorifica a aquel que lo formó. Debemos, pues, "
             "hermanos, examinar con cuidado lo que toca a nuestra salvación, "
             "no sea que el maligno, abriéndose entrada furtiva de error en "
             "nosotros, nos arroje como con honda fuera de nuestra vida.",

    # Capítulo 3
    (3, 1): "Dice, pues, otra vez acerca de estas cosas a ellos: ¿Para qué "
            "ayunáis para mí, dice el Señor, de modo que hoy se oiga vuestra "
            "voz con clamor? No es este el ayuno que yo escogí, dice el "
            "Señor: no el hombre que humilla su alma;",
    (3, 2): "ni aunque doblegáis vuestra cerviz como un aro, y os vistáis de "
            "saco y os echéis ceniza debajo, ni aun así llamaréis a esto "
            "ayuno aceptable.",
    (3, 3): "Pero a nosotros nos dice: He aquí el ayuno que yo escogí, dice "
            "el Señor: desata toda ligadura de injusticia, deshaz los nudos "
            "de los contratos violentos, deja ir libres a los quebrantados, y "
            "rompe todo documento injusto. Parte tu pan con los hambrientos, "
            "y si vieres al desnudo, cúbrelo; mete en tu casa a los que no "
            "tienen techo, y si vieres al humilde, no lo desprecies, ni a los "
            "de tu propia casa y linaje.",
    (3, 4): "Entonces nacerá tu luz como el alba, y tus vestidos brotarán "
            "presto, y tu justicia irá delante de ti, y la gloria de Dios te "
            "envolverá.",
    (3, 5): "Entonces clamarás, y Dios te oirá; mientras aún estés hablando, "
            "dirá: Heme aquí; si quitares de ti la ligadura, y el extender la "
            "mano, y la palabra de murmuración, y dieres de corazón tu pan al "
            "hambriento, y te compadecieres del alma afligida.",
    (3, 6): "Para esto, pues, hermanos, el que es longánime, previendo que el "
            "pueblo que él preparó en su Amado creería con sencillez, nos "
            "manifestó de antemano acerca de todas las cosas, para que no nos "
            "estrellemos, como prosélitos, contra la ley de aquellos.",

    # Capítulo 4
    (4, 1): "Es necesario, pues, que nosotros, investigando mucho acerca de "
            "las cosas presentes, busquemos las que pueden salvarnos. "
            "Huyamos, pues, del todo de todas las obras de la iniquidad, no "
            "sea que nos alcancen las obras de la iniquidad; y aborrezcamos "
            "el error del tiempo presente, para que seamos amados en el "
            "venidero.",
    (4, 2): "No demos descanso a nuestra alma, de modo que tenga libertad de "
            "correr juntamente con los pecadores y los malvados, no sea que "
            "nos hagamos semejantes a ellos.",
    (4, 3): "El escándalo final se ha acercado, acerca del cual está escrito, "
            "como dice Enoc. Porque para esto el Soberano ha acortado los "
            "tiempos y los días, para que su Amado se apresure y venga a su "
            "heredad.",
    (4, 4): "Y así dice también el profeta: Diez reinos reinarán sobre la "
            "tierra, y se levantará después de ellos un rey pequeño, que "
            "humillará a tres de los reyes de una vez.",
    (4, 5): "Asimismo dice Daniel acerca del mismo: Y vi la cuarta bestia, "
            "malvada y fuerte y más feroz que todas las bestias del mar, y "
            "cómo de ella brotaron diez cuernos, y de ellos un cuerno "
            "pequeño, como un retoño, y cómo humilló de una vez a tres de los "
            "cuernos grandes.",
    (4, 6): "Debéis, pues, entender. Y además os ruego también esto, como uno "
            "de vosotros que soy, y que os ama a cada uno en particular y a "
            "todos más que a mi propia alma: que atendáis ahora a vosotros "
            "mismos y no os hagáis semejantes a algunos que amontonan sobre "
            "vuestros pecados, diciendo que la alianza es de ellos y nuestra.",
    (4, 7): "Nuestra es; pero ellos la perdieron así para siempre, cuando ya "
            "Moisés la había recibido. Porque dice la Escritura: Y estaba "
            "Moisés en el monte ayunando cuarenta días y cuarenta noches, y "
            "recibió la alianza de parte del Señor, tablas de piedra escritas "
            "con el dedo de la mano del Señor.",
    (4, 8): "Pero, volviéndose a los ídolos, la perdieron. Porque así dice el "
            "Señor: Moisés, Moisés, desciende pronto, porque tu pueblo, el "
            "que sacaste de la tierra de Egipto, ha obrado inicuamente. Y lo "
            "entendió Moisés, y arrojó de sus manos las dos tablas; y se "
            "quebró la alianza de ellos, para que la del Amado, Jesús, fuese "
            "sellada en nuestro corazón en la esperanza de la fe en él.",
    (4, 9): "Y queriendo escribir muchas cosas, no como maestro, sino como "
            "conviene a quien ama no quedarse corto en lo que tenemos, me "
            "apresuré a escribir, yo, vuestra ínfima escoria. Por eso estemos "
            "atentos en los últimos días; porque de nada nos aprovechará todo "
            "el tiempo de nuestra fe, si ahora, en el tiempo inicuo y en los "
            "escándalos venideros, no resistimos, como conviene a hijos de "
            "Dios, para que el Negro no tenga entrada furtiva.",
    (4, 10): "Huyamos de toda vanidad, aborrezcamos del todo las obras del "
             "mal camino. No os retiréis a vivir solos, encerrándoos en "
             "vosotros mismos, como si estuvierais ya justificados; antes "
             "bien, reuniéndoos en uno, buscad juntos lo que es de provecho "
             "común.",
    (4, 11): "Porque dice la Escritura: ¡Ay de los que son sabios para sí "
             "mismos y entendidos delante de sí mismos! Hagámonos "
             "espirituales, hagámonos templo perfecto para Dios. En cuanto "
             "está en nosotros, meditemos el temor de Dios y luchemos por "
             "guardar sus mandamientos, para que nos alegremos en sus "
             "ordenanzas.",
    (4, 12): "El Señor juzgará al mundo sin acepción de personas. Cada uno "
             "recibirá según lo que hizo. Si es bueno, su justicia irá "
             "delante de él; si es malo, la paga de la maldad irá delante de "
             "él;",
    (4, 13): "no sea que, descansando como llamados, nos durmamos en nuestros "
             "pecados, y el príncipe maligno, tomando poder sobre nosotros, "
             "nos eche fuera del reino del Señor.",
    (4, 14): "Y además considerad también esto, hermanos míos: cuando veis "
             "que, después de tan grandes señales y prodigios hechos en "
             "Israel, aun así fueron abandonados, estemos atentos, no sea "
             "que, como está escrito, seamos hallados muchos llamados, pero "
             "pocos escogidos.",

    # Capítulo 5
    (5, 1): "Porque para esto soportó el Señor entregar su carne a la "
            "corrupción, para que fuésemos purificados por el perdón de los "
            "pecados, esto es, por la sangre de su aspersión.",
    (5, 2): "Porque está escrito acerca de él, parte respecto de Israel y "
            "parte respecto de nosotros, y dice así: Fue herido por nuestras "
            "iniquidades y molido por nuestros pecados; por su llaga nosotros "
            "fuimos sanados; como oveja fue llevado al matadero, y como "
            "cordero mudo delante del que lo trasquila.",
    (5, 3): "Así pues, debemos dar gracias sobremanera al Señor, porque nos "
            "dio a conocer las cosas pasadas, y nos hizo sabios en las "
            "presentes, y en cuanto a las venideras no somos ignorantes.",
    (5, 4): "Y dice la Escritura: No sin razón se tienden las redes a las "
            "aves. Esto quiere decir que con justicia perecerá el hombre que, "
            "teniendo conocimiento del camino de la justicia, se encierra a "
            "sí mismo en el camino de las tinieblas.",
    (5, 5): "Y además también esto, hermanos míos: si el Señor soportó "
            "padecer por nuestra alma, siendo Señor de todo el mundo, a quien "
            "dijo Dios desde la fundación del mundo: Hagamos al hombre a "
            "imagen y semejanza nuestra, ¿cómo, pues, soportó padecer a manos "
            "de hombres?",
    (5, 6): "Aprended. Los profetas, recibiendo de él la gracia, profetizaron "
            "acerca de él; y él, para destruir la muerte y mostrar la "
            "resurrección de entre los muertos, porque era necesario que "
            "fuese manifestado en carne, lo soportó,",
    (5, 7): "para cumplir a los padres la promesa, y para, preparándose a sí "
            "mismo el pueblo nuevo, mostrar, estando sobre la tierra, que él, "
            "después de haber obrado la resurrección, juzgará.",
    (5, 8): "Además, enseñando a Israel y haciendo tan grandes prodigios y "
            "señales, predicaba, y lo amó sobremanera.",
    (5, 9): "Y cuando escogió a sus propios apóstoles, los que habían de "
            "predicar su evangelio, que eran inicuos más allá de todo pecado, "
            "para mostrar que no vino a llamar a justos, sino a pecadores, "
            "entonces manifestó que él era Hijo de Dios.",
    (5, 10): "Porque si no hubiera venido en carne, ¿cómo se habrían salvado "
             "los hombres viéndolo, cuando, al mirar el sol que ha de dejar "
             "de existir, que es obra de sus manos, no pueden fijar los ojos "
             "en sus rayos?",
    (5, 11): "Así pues, el Hijo de Dios vino en carne para esto: para colmar "
             "la suma de los pecados de los que persiguieron hasta la muerte "
             "a sus profetas.",
    (5, 12): "Así pues, para esto lo soportó. Porque dice Dios que la herida "
             "de su carne vino de ellos: Cuando hieran a su propio pastor, "
             "entonces perecerán las ovejas del rebaño.",
    (5, 13): "Y él quiso padecer así; porque era necesario que padeciese "
             "sobre un madero. Porque dice el que profetiza acerca de él: "
             "Libra mi alma de la espada, y: Clava mis carnes, porque las "
             "asambleas de los malignos se han levantado contra mí.",
    (5, 14): "Y otra vez dice: He aquí, he puesto mi espalda a los azotes, y "
             "mis mejillas a las bofetadas; y puse mi rostro como peña firme.",

    # Capítulo 6
    (6, 1): "Cuando, pues, cumplió el mandamiento, ¿qué dice? ¿Quién es el "
            "que contiende conmigo? Que se me oponga; o ¿quién es el que "
            "pleitea conmigo? Que se acerque al siervo del Señor.",
    (6, 2): "¡Ay de vosotros, porque todos vosotros os envejeceréis como un "
            "vestido, y la polilla os comerá! Y otra vez dice el profeta, "
            "puesto que fue colocado como piedra fuerte para quebrantar: He "
            "aquí, pondré en los cimientos de Sion una piedra preciosa, "
            "escogida, angular, de gran estima.",
    (6, 3): "Luego, ¿qué dice? Y el que espere en ella vivirá para siempre. "
            "¿En una piedra, pues, está nuestra esperanza? ¡En ninguna "
            "manera! Sino que es porque el Señor puso su carne en fortaleza. "
            "Porque dice: Y me puso como peña firme.",
    (6, 4): "Y dice otra vez el profeta: La piedra que desecharon los "
            "edificadores, esta vino a ser cabeza del ángulo. Y otra vez "
            "dice: Este es el día grande y maravilloso que hizo el Señor.",
    (6, 5): "Os escribo con más sencillez, para que entendáis: yo, ínfima "
            "escoria de vuestro amor.",
    (6, 6): "¿Qué dice, pues, otra vez el profeta? Me rodeó una asamblea de "
            "malignos, me cercaron como abejas al panal, y: Sobre mi ropa "
            "echaron suertes.",
    (6, 7): "Habiendo, pues, de manifestarse y padecer en carne, fue "
            "manifestada de antemano su pasión. Porque dice el profeta acerca "
            "de Israel: ¡Ay de su alma, porque han tramado un consejo malvado "
            "contra sí mismos, diciendo: Atemos al justo, porque nos es "
            "molesto!",
    (6, 8): "¿Qué les dice el otro profeta, Moisés? He aquí, así dice el "
            "Señor Dios: Entrad en la tierra buena que el Señor juró a "
            "Abrahán, a Isaac y a Jacob, y heredadla, tierra que fluye leche "
            "y miel.",
    (6, 9): "Pero ¿qué dice el conocimiento? Aprended. Esperad, dice, en el "
            "que ha de manifestarse a vosotros en carne, Jesús. Porque el "
            "hombre es tierra que padece; pues de la faz de la tierra fue "
            "hecha la formación de Adán.",
    (6, 10): "¿Qué quiere decir, pues: En la tierra buena, tierra que fluye "
             "leche y miel? Bendito sea nuestro Señor, hermanos, que puso en "
             "nosotros sabiduría e inteligencia de sus secretos. Porque dice "
             "el profeta una parábola del Señor: ¿Quién la entenderá, sino el "
             "sabio y entendido y el que ama a su Señor?",
    (6, 11): "Puesto que, pues, nos renovó en el perdón de los pecados, nos "
             "hizo de otro molde, de modo que tengamos alma de niños, como si "
             "él nos formara de nuevo.",
    (6, 12): "Porque dice la Escritura acerca de nosotros, cuando dice al "
             "Hijo: Hagamos al hombre a nuestra imagen y semejanza, y señoree "
             "sobre las bestias de la tierra, y sobre las aves del cielo, y "
             "sobre los peces del mar. Y dijo el Señor, viendo nuestra "
             "hermosa formación: Creced y multiplicaos, y llenad la tierra. "
             "Esto se dijo al Hijo.",
    (6, 13): "Otra vez te mostraré cómo nos habla a nosotros. Hizo una "
             "segunda formación en los últimos tiempos. Y dice el Señor: He "
             "aquí, hago las postreras cosas como las primeras. Para esto, "
             "pues, predicó el profeta: Entrad en la tierra que fluye leche y "
             "miel, y enseñoreaos de ella.",
    (6, 14): "Mira, pues: nosotros hemos sido formados de nuevo, como dice "
             "otra vez en otro profeta: He aquí, dice el Señor, quitaré de "
             "estos, es decir, de aquellos que preveía el Espíritu del Señor, "
             "los corazones de piedra, y pondré corazones de carne; porque él "
             "había de manifestarse en carne y habitar en nosotros.",
    (6, 15): "Porque templo santo es para el Señor, hermanos míos, la morada "
             "de nuestro corazón.",
    (6, 16): "Porque dice otra vez el Señor: ¿Y con qué me presentaré delante "
             "del Señor mi Dios y seré glorificado? Dice: Te confesaré en la "
             "asamblea de mis hermanos, y te cantaré salmos en medio de la "
             "asamblea de los santos. Así pues, nosotros somos a quienes "
             "introdujo en la tierra buena.",
    (6, 17): "¿Qué significan, pues, la leche y la miel? Que el niño primero "
             "es vivificado con miel, y luego con leche; así pues también "
             "nosotros, vivificados por la fe en la promesa y por la palabra, "
             "viviremos enseñoreándonos de la tierra.",
    (6, 18): "Y ya dijimos antes: Y crezcan y multiplíquense y señoreen sobre "
             "los peces. ¿Quién es, pues, el que ahora puede señorear sobre "
             "las bestias, o los peces, o las aves del cielo? Porque debemos "
             "entender que el señorear es propio de la autoridad, de modo que "
             "uno mande y domine.",
    (6, 19): "Si, pues, esto no sucede ahora, entonces nos ha dicho cuándo: "
             "cuando también nosotros seamos perfeccionados para llegar a ser "
             "herederos de la alianza del Señor.",

    # Capítulo 7
    (7, 1): "Así pues, entended, hijos de alegría, que el Señor bueno nos "
            "manifestó de antemano todas las cosas, para que conozcamos a "
            "quién debemos alabar dándole gracias por todo.",
    (7, 2): "Si, pues, el Hijo de Dios, siendo Señor y habiendo de juzgar a "
            "vivos y muertos, padeció para que su herida nos diese vida, "
            "creamos que el Hijo de Dios no podía padecer sino por nosotros.",
    (7, 3): "Pero además, crucificado, le dieron a beber vinagre y hiel. Oíd "
            "cómo acerca de esto lo manifestaron los sacerdotes del templo. "
            "Estando escrito el mandamiento: El que no ayune el ayuno, será "
            "exterminado con muerte, lo mandó el Señor, puesto que también él "
            "mismo había de ofrecer por nuestros pecados el vaso del Espíritu "
            "como sacrificio, para que se cumpliese también la figura que "
            "tuvo lugar en Isaac, el que fue ofrecido sobre el altar.",
    (7, 4): "¿Qué dice, pues, en el profeta? Y coman del macho cabrío "
            "ofrecido en el ayuno por todos los pecados. Atended con "
            "exactitud: Y coman solos todos los sacerdotes las entrañas sin "
            "lavar, con vinagre.",
    (7, 5): "¿Para qué? Puesto que a mí, que he de ofrecer mi carne por los "
            "pecados de mi pueblo nuevo, me habéis de dar a beber hiel con "
            "vinagre, comed vosotros solos, mientras el pueblo ayuna y se "
            "lamenta en saco y ceniza. Para mostrar que era necesario que él "
            "padeciese a manos de ellos.",
    (7, 6): "Atended a lo que mandó: Tomad dos machos cabríos hermosos y "
            "semejantes, y ofrecedlos; y tome el sacerdote el uno en "
            "holocausto por los pecados.",
    (7, 7): "Y el otro, ¿qué harán con él? Maldito, dice, el otro. Atended "
            "cómo se manifiesta la figura de Jesús:",
    (7, 8): "Y escupidle todos, y punzadle, y poned la lana escarlata "
            "alrededor de su cabeza, y así sea echado al desierto. Y cuando "
            "así se ha hecho, el que lleva el macho cabrío lo conduce al "
            "desierto, y le quita la lana, y la pone sobre un arbusto llamado "
            "raquel, cuyos brotes solemos comer cuando los hallamos en el "
            "campo; así, solo del raquel son dulces los frutos.",
    (7, 9): "¿Qué significa, pues, esto? Atended: El uno sobre el altar, y el "
            "otro maldito; ¿y por qué el maldito está coronado? Porque le "
            "verán entonces, en aquel día, con la túnica talar escarlata "
            "sobre su carne, y dirán: ¿No es este aquel a quien nosotros en "
            "otro tiempo crucificamos, despreciándolo, punzándolo y "
            "escupiéndolo? Verdaderamente este era el que entonces decía que "
            "él era Hijo de Dios.",
    (7, 10): "Porque ¿cómo es semejante a aquel? Para esto son semejantes los "
             "machos cabríos, hermosos, iguales: para que, cuando le vean "
             "entonces venir, se asombren de la semejanza del macho cabrío. "
             "Así pues, ved la figura de Jesús, que había de padecer.",
    (7, 11): "¿Y por qué ponen la lana en medio de las espinas? Es una figura "
             "de Jesús puesta para la iglesia: que quien quiera quitar la "
             "lana escarlata, es necesario que padezca mucho, porque la "
             "espina es terrible, y que la consiga a través de la aflicción. "
             "Así, dice, los que quieren verme y alcanzar mi reino, deben "
             "recibirme a través de aflicciones y padecimientos.",

    # Capítulo 8
    (8, 1): "¿Y qué figura pensáis que es esta: que se mandó a Israel que los "
            "hombres en quienes hay pecados consumados ofrezcan una becerra, "
            "y que después de degollarla la quemen, y que luego unos niños "
            "recojan la ceniza y la echen en vasijas, y pongan la lana "
            "escarlata sobre un madero (mira otra vez la figura de la cruz y "
            "la lana escarlata) y el hisopo, y que así los niños rocíen al "
            "pueblo uno por uno, para que sean purificados de los pecados?",
    (8, 2): "Entended cómo os habla con sencillez. El becerro es Jesús; los "
            "hombres pecadores que lo ofrecen son los que lo llevaron al "
            "matadero. Después ya no son hombres, ya no es la gloria de los "
            "pecadores.",
    (8, 3): "Los niños que rocían son los que nos anunciaron el evangelio del "
            "perdón de los pecados y de la purificación del corazón, a "
            "quienes dio la autoridad del evangelio para predicar (siendo "
            "doce, en testimonio de las tribus, porque doce son las tribus de "
            "Israel).",
    (8, 4): "¿Y por qué son tres los niños que rocían? En testimonio de "
            "Abrahán, Isaac y Jacob, porque estos son grandes delante de "
            "Dios.",
    (8, 5): "¿Y por qué la lana sobre el madero? Porque el reino de Jesús "
            "está sobre el madero, y porque los que esperan en él vivirán "
            "para siempre.",
    (8, 6): "¿Y por qué la lana y el hisopo juntos? Porque en su reino habrá "
            "días malos e inmundos, en los cuales nosotros seremos salvos; "
            "porque también el que padece en su carne es sanado por medio de "
            "la suciedad del hisopo.",
    (8, 7): "Y por esto, las cosas así sucedidas son para nosotros claras, "
            "pero para aquellos oscuras, porque no oyeron la voz del Señor.",

    # Capítulo 9
    (9, 1): "Porque dice otra vez acerca de los oídos, cómo circuncidó "
            "nuestro corazón. Dice el Señor en el profeta: Al oír de su oído "
            "me obedecieron. Y otra vez dice: Con el oído oirán los que están "
            "lejos; conocerán lo que he hecho. Y: Circuncidad, dice el Señor, "
            "vuestros corazones.",
    (9, 2): "Y otra vez dice: Oye, Israel, porque así dice el Señor tu Dios. "
            "Y otra vez el Espíritu del Señor profetiza: ¿Quién es el que "
            "quiere vivir para siempre? Oiga con el oído la voz de mi siervo.",
    (9, 3): "Y otra vez dice: Oye, cielo, y escucha, tierra, porque el Señor "
            "ha dicho estas cosas en testimonio. Y otra vez dice: Oíd la "
            "palabra del Señor, príncipes de este pueblo. Y otra vez dice: "
            "Oíd, hijos, la voz del que clama en el desierto. Así pues, "
            "circuncidó nuestros oídos, para que, oyendo la palabra, creamos "
            "nosotros.",
    (9, 4): "Pero también la circuncisión en que han confiado ha sido "
            "abolida; porque él dijo que la circuncisión no había de ser de "
            "la carne; pero ellos transgredieron, porque un ángel malo los "
            "engañó.",
    (9, 5): "Les dice: Así dice el Señor vuestro Dios (aquí hallo un "
            "mandamiento): No sembréis entre espinas; circuncidaos para "
            "vuestro Señor. ¿Y qué dice? Circuncidad la dureza de vuestro "
            "corazón, y no endureceréis vuestra cerviz. Toma otra vez: He "
            "aquí, dice el Señor, todas las naciones son incircuncisas en el "
            "prepucio, pero este pueblo es incircunciso de corazón.",
    (9, 6): "Pero dirás: Ciertamente el pueblo ha sido circuncidado como "
            "sello. Pero también todo sirio y árabe, y todos los sacerdotes "
            "de los ídolos; ¿acaso, pues, también aquellos son de su alianza? "
            "Pero también los egipcios están en la circuncisión.",
    (9, 7): "Aprended, pues, hijos del amor, abundantemente acerca de todo: "
            "que Abrahán, que fue el primero en dar la circuncisión, "
            "circuncidó mirando de antemano en espíritu a Jesús, habiendo "
            "recibido las enseñanzas de tres letras.",
    (9, 8): "Porque dice: Y circuncidó Abrahán de su casa a dieciocho y "
            "trescientos hombres. ¿Cuál es, pues, el conocimiento que le fue "
            "dado? Aprended que dice primero los dieciocho, y, dejando un "
            "intervalo, dice los trescientos. El dieciocho: Ι, diez; Η, ocho: "
            "tienes a Jesús. Y porque la cruz, en la Τ, había de tener la "
            "gracia, dice también los trescientos. Así pues, muestra a Jesús "
            "en las dos letras, y en la una la cruz.",
    (9, 9): "Lo sabe el que puso en nosotros el don arraigado de su "
            "enseñanza. Nadie aprendió de mí palabra más genuina; pero sé que "
            "vosotros sois dignos.",

    # Capítulo 10
    (10, 1): "Y en cuanto a que Moisés dijo: No comeréis cerdo, ni águila, ni "
             "gavilán, ni cuervo, ni ningún pez que no tenga escamas en sí, "
             "recibió en su entendimiento tres enseñanzas.",
    (10, 2): "Además les dice en el Deuteronomio: Y estableceré con este "
             "pueblo mis ordenanzas. Así pues, el no comer no es mandamiento "
             "de Dios, sino que Moisés habló en espíritu.",
    (10, 3): "Así pues, dijo lo del cerdo con este sentido: No te juntarás, "
             "dice, con hombres tales que son semejantes a los cerdos; es "
             "decir, cuando viven en deleites se olvidan del Señor, y cuando "
             "pasan necesidad reconocen al Señor, como también el cerdo, "
             "cuando come, no conoce a su señor, pero cuando tiene hambre "
             "grita, y en cuanto recibe algo, calla otra vez.",
    (10, 4): "Ni comerás el águila, ni el gavilán, ni el milano, ni el "
             "cuervo: No te juntarás, dice, ni te harás semejante a hombres "
             "tales que no saben procurarse el sustento con trabajo y sudor, "
             "sino que arrebatan lo ajeno en su iniquidad, y acechan, aunque "
             "andan como en sencillez, y miran en derredor a quién despojarán "
             "por su codicia; como también estas aves son las únicas que no "
             "se procuran el sustento, sino que, sentadas ociosas, buscan "
             "cómo devorar carnes ajenas, siendo pestilentes por su maldad.",
    (10, 5): "Y no comerás, dice, la morena, ni el pulpo, ni la sepia: No te "
             "harás semejante, dice, juntándote con hombres tales que son del "
             "todo impíos y ya están condenados a muerte, como también estos "
             "pececillos son los únicos malditos que nadan en lo profundo, no "
             "nadando como los demás, sino que habitan en el fondo, bajo lo "
             "profundo.",
    (10, 6): "Pero tampoco comerás la liebre. ¿Para qué? No serás, dice, "
             "corruptor de niños, ni te harás semejante a los tales; porque "
             "la liebre cada año aumenta sus orificios; pues cuantos años "
             "vive, tantos agujeros tiene.",
    (10, 7): "Pero tampoco comerás la hiena: No serás, dice, adúltero, ni "
             "corruptor, ni te harás semejante a los tales. ¿Para qué? Porque "
             "este animal cambia de naturaleza cada año, y unas veces es "
             "macho y otras hembra.",
    (10, 8): "Pero también aborreció con razón la comadreja. No serás, dice, "
             "semejante a aquellos de quienes oímos que cometen iniquidad con "
             "la boca por su impureza, ni te juntarás con las impuras que "
             "cometen la iniquidad con la boca. Porque este animal concibe "
             "por la boca.",
    (10, 9): "Así pues, habiendo recibido Moisés acerca de los alimentos tres "
             "enseñanzas, habló así en espíritu; pero ellos, conforme al "
             "deseo de la carne, lo recibieron como si se tratara de comida.",
    (10, 10): "Y David recibe el conocimiento de estas mismas tres "
              "enseñanzas, y dice: Bienaventurado el varón que no anduvo en "
              "consejo de impíos, como los peces andan en tinieblas hacia lo "
              "profundo; ni estuvo en camino de pecadores, como los que "
              "parecen temer al Señor pecan como el cerdo; ni en silla de "
              "pestilentes se ha sentado, como las aves que se sientan para "
              "la rapiña. Tenéis perfectamente lo que toca también a la "
              "comida.",
    (10, 11): "Otra vez dice Moisés: Comeréis todo animal de pezuña hendida y "
              "que rumia. ¿Qué dice? Que el que recibe el alimento conoce al "
              "que lo alimenta, y descansando en él parece alegrarse. Bien "
              "dijo, mirando al mandamiento. ¿Qué dice, pues? Juntaos con los "
              "que temen al Señor, con los que meditan en su corazón el "
              "precepto de la palabra que recibieron, con los que hablan las "
              "ordenanzas del Señor y las guardan, con los que saben que la "
              "meditación es obra de alegría y rumian la palabra del Señor. "
              "¿Y qué es lo de la pezuña hendida? Que el justo anda en este "
              "mundo y a la vez espera el siglo santo. Ved cuán bien legisló "
              "Moisés.",
    (10, 12): "Pero ¿de dónde les vendría a aquellos entender o comprender "
              "estas cosas? Mas nosotros, habiendo entendido rectamente los "
              "mandamientos, los hablamos como quiso el Señor. Por esto "
              "circuncidó nuestros oídos y nuestros corazones, para que "
              "comprendamos estas cosas.",

    # Capítulo 11
    (11, 1): "Busquemos ahora si el Señor tuvo cuidado de manifestar de "
             "antemano acerca del agua y acerca de la cruz. Acerca del agua "
             "está escrito, respecto de Israel, cómo no recibirían el "
             "bautismo que trae el perdón de los pecados, sino que se "
             "edificarían otro para sí mismos.",
    (11, 2): "Porque dice el profeta: Espántate, cielo, y estremézcase más "
             "por esto la tierra, porque dos males ha hecho este pueblo: me "
             "dejaron a mí, fuente de vida, y se cavaron para sí una fosa de "
             "muerte.",
    (11, 3): "¿Es acaso peña desierta mi monte santo, Sinaí? Porque seréis "
             "como polluelos de ave que revolotean, arrancados del nido.",
    (11, 4): "Y otra vez dice el profeta: Yo iré delante de ti, y allanaré "
             "los montes, y quebrantaré las puertas de bronce, y haré pedazos "
             "los cerrojos de hierro, y te daré los tesoros escondidos, "
             "ocultos, invisibles, para que sepan que yo soy el Señor Dios.",
    (11, 5): "Y: Habitarás en una cueva alta de peña fuerte. Y: Su agua es "
             "fiel; veréis al Rey con gloria, y vuestra alma meditará el "
             "temor del Señor.",
    (11, 6): "Y otra vez dice en otro profeta: Y el que hace estas cosas será "
             "como el árbol plantado junto a las corrientes de las aguas, que "
             "dará su fruto en su tiempo, y su hoja no caerá, y todo lo que "
             "hiciere prosperará.",
    (11, 7): "No así los impíos, no así, sino como el tamo que arrebata el "
             "viento de la faz de la tierra. Por tanto no se levantarán los "
             "impíos en el juicio, ni los pecadores en el consejo de los "
             "justos, porque el Señor conoce el camino de los justos, y el "
             "camino de los impíos perecerá.",
    (11, 8): "Observad cómo señaló juntamente el agua y la cruz. Porque esto "
             "dice: Bienaventurados los que, habiendo esperado en la cruz, "
             "descendieron al agua; porque dice la recompensa: en su tiempo; "
             "entonces, dice, la daré. Y ahora, lo que dice: Las hojas no "
             "caerán, esto quiere decir: que toda palabra que salga de "
             "vosotros por vuestra boca en fe y amor será para conversión y "
             "esperanza de muchos.",
    (11, 9): "Y otra vez dice otro profeta: Y era la tierra de Jacob alabada "
             "sobre toda la tierra. Esto quiere decir: glorifica el vaso de "
             "su Espíritu.",
    (11, 10): "Luego, ¿qué dice? Y había un río que corría a la derecha, y de "
              "él subían árboles hermosos; y el que coma de ellos vivirá para "
              "siempre.",
    (11, 11): "Esto quiere decir que nosotros descendemos al agua llenos de "
              "pecados y de suciedad, y subimos llevando fruto en el corazón, "
              "teniendo en el espíritu el temor y la esperanza en Jesús. Y el "
              "que coma de estos vivirá para siempre, quiere decir esto: el "
              "que oiga, dice, estas cosas que se hablan y las crea, vivirá "
              "para siempre.",

    # Capítulo 12
    (12, 1): "Asimismo, otra vez, acerca de la cruz lo señala en otro profeta "
             "que dice: ¿Y cuándo se cumplirán estas cosas? Dice el Señor: "
             "Cuando un madero se incline y se levante, y cuando de un madero "
             "destile sangre. Tienes otra vez lo que toca a la cruz y al que "
             "había de ser crucificado.",
    (12, 2): "Y dice otra vez a Moisés, cuando Israel era atacado por los "
             "extranjeros, y para recordarles, mientras eran atacados, que "
             "por sus pecados habían sido entregados a la muerte: el Espíritu "
             "habla al corazón de Moisés para que haga una figura de la cruz "
             "y del que había de padecer, porque si no esperan en él, dice, "
             "serán combatidos para siempre. Pone, pues, Moisés un escudo "
             "sobre otro en medio de la batalla, y, puesto en pie más alto "
             "que todos, extendió las manos, y así otra vez vencía Israel. "
             "Luego, cuando las bajaba, eran muertos.",
    (12, 3): "¿Para qué? Para que sepan que no pueden ser salvos si no "
             "esperan en él.",
    (12, 4): "Y otra vez dice en otro profeta: Todo el día extendí mis manos "
             "a un pueblo desobediente y que contradice mi camino justo.",
    (12, 5): "Otra vez Moisés hace una figura de Jesús: que era necesario que "
             "padeciese, y que él mismo daría vida, aquel a quien pensarán "
             "haber hecho perecer, en una señal, cuando Israel caía (porque "
             "el Señor hizo que toda clase de serpientes los mordiesen, y "
             "morían, puesto que la transgresión se produjo en Eva por medio "
             "de la serpiente), para convencerlos de que por su transgresión "
             "serían entregados a la aflicción de la muerte.",
    (12, 6): "Además, el mismo Moisés, que había mandado: No tendréis ni "
             "imagen fundida ni tallada por dios vuestro, él mismo la hace "
             "para mostrar una figura de Jesús. Hace, pues, Moisés una "
             "serpiente de bronce, y la coloca en lugar glorioso, y convoca "
             "al pueblo por pregón.",
    (12, 7): "Venidos, pues, todos juntos, rogaban a Moisés que elevase por "
             "ellos una súplica por su curación. Y les dijo Moisés: Cuando, "
             "dice, alguno de vosotros sea mordido, venga a la serpiente "
             "puesta sobre el madero, y espere creyendo que ella, aun estando "
             "muerta, puede dar vida, y al instante será salvo. Y así lo "
             "hacían. Tienes otra vez también en esto la gloria de Jesús, "
             "porque en él son todas las cosas y para él.",
    (12, 8): "¿Qué dice otra vez Moisés a Jesús, hijo de Navé, cuando le puso "
             "este nombre, siendo profeta, solo para que todo el pueblo "
             "oyese? Que el Padre manifiesta todas las cosas acerca de su "
             "Hijo Jesús.",
    (12, 9): "Dice, pues, Moisés a Jesús, hijo de Navé, habiéndole puesto "
             "este nombre, cuando lo envió a espiar la tierra: Toma un libro "
             "en tus manos y escribe lo que dice el Señor: que el Hijo de "
             "Dios arrancará de raíz toda la casa de Amalec en los últimos "
             "días.",
    (12, 10): "Mira otra vez a Jesús, no hijo de hombre, sino Hijo de Dios, "
              "manifestado en figura en la carne. Puesto que, pues, han de "
              "decir que el Cristo es hijo de David, el mismo David "
              "profetiza, temiendo y comprendiendo el error de los pecadores: "
              "Dijo el Señor a mi Señor: Siéntate a mi diestra, hasta que "
              "ponga a tus enemigos por estrado de tus pies.",
    (12, 11): "Y otra vez dice así Isaías: Dijo el Señor a mi Cristo, el "
              "Señor, cuya diestra tomé, para que le obedezcan delante de él "
              "las naciones, y quebrantaré la fuerza de los reyes. Mira cómo "
              "David le llama Señor, y no le llama hijo.",

    # Capítulo 13
    (13, 1): "Veamos ahora si este pueblo es el heredero o el primero, y si "
             "la alianza es para nosotros o para aquellos.",
    (13, 2): "Oíd, pues, lo que dice la Escritura acerca del pueblo: Y oraba "
             "Isaac por Rebeca su mujer, porque era estéril; y concibió. "
             "Luego salió Rebeca a consultar al Señor, y le dijo el Señor: "
             "Dos naciones hay en tu vientre, y dos pueblos en tu seno; y un "
             "pueblo prevalecerá sobre el otro pueblo, y el mayor servirá al "
             "menor.",
    (13, 3): "Debéis entender quién es Isaac y quién es Rebeca, y en quiénes "
             "ha mostrado que este pueblo es mayor que aquel.",
    (13, 4): "Y en otra profecía lo dice más claramente Jacob a José su hijo, "
             "diciendo: He aquí, no me ha privado el Señor de tu rostro; "
             "tráeme a tus hijos, para que los bendiga.",
    (13, 5): "Y trajo a Efraín y a Manasés, queriendo que Manasés fuese "
             "bendecido, porque era el mayor; pues José lo acercó a la mano "
             "derecha de su padre Jacob. Pero vio Jacob en el espíritu una "
             "figura del pueblo de después. ¿Y qué dice? Y cruzó Jacob sus "
             "manos, y puso la derecha sobre la cabeza de Efraín, el segundo "
             "y el más joven, y lo bendijo. Y dijo José a Jacob: Pasa tu "
             "derecha sobre la cabeza de Manasés, porque es mi hijo "
             "primogénito. Y dijo Jacob a José: Lo sé, hijo, lo sé; pero el "
             "mayor servirá al menor, y este será bendecido.",
    (13, 6): "Ved en quiénes ha establecido que este pueblo sea el primero y "
             "el heredero de la alianza.",
    (13, 7): "Si, pues, además se hizo memoria de esto también por medio de "
             "Abrahán, tenemos el colmo de nuestro conocimiento. ¿Qué dice, "
             "pues, a Abrahán, cuando, solo él habiendo creído, le fue "
             "contado por justicia? He aquí, te he puesto, Abrahán, por padre "
             "de las naciones que creen a Dios en la incircuncisión.",

    # Capítulo 14
    (14, 1): "Sí. Pero veamos si la alianza que juró a los padres dar al "
             "pueblo, si la ha dado. La ha dado; pero ellos no fueron dignos "
             "de recibirla a causa de sus pecados.",
    (14, 2): "Porque dice el profeta: Y estaba Moisés ayunando en el monte "
             "Sinaí, para recibir la alianza del Señor para el pueblo, "
             "cuarenta días y cuarenta noches. Y recibió Moisés del Señor las "
             "dos tablas escritas por el dedo de la mano del Señor en "
             "espíritu; y tomándolas Moisés, las bajaba al pueblo para "
             "dárselas.",
    (14, 3): "Y dijo el Señor a Moisés: Moisés, Moisés, desciende pronto, "
             "porque tu pueblo, el que sacaste de la tierra de Egipto, ha "
             "obrado inicuamente. Y entendió Moisés que otra vez se habían "
             "hecho imágenes fundidas, y las arrojó de sus manos, y se "
             "quebraron las tablas de la alianza del Señor.",
    (14, 4): "Moisés la recibió, pero ellos no fueron dignos. Y cómo la "
             "recibimos nosotros, aprendedlo. Moisés la recibió siendo "
             "siervo, pero el Señor mismo nos la dio a nosotros para que "
             "fuésemos pueblo de heredad, habiendo padecido por nosotros.",
    (14, 5): "Y fue manifestado para que también aquellos llenasen la medida "
             "de sus pecados, y nosotros la recibiésemos por medio del que "
             "hereda la alianza, el Señor Jesús, que para esto fue preparado: "
             "para que, manifestándose él, rescatando de las tinieblas "
             "nuestros corazones, ya consumidos por la muerte y entregados a "
             "la iniquidad del error, estableciese en nosotros la alianza por "
             "la palabra.",
    (14, 6): "Porque está escrito cómo el Padre le manda que, rescatándonos "
             "de las tinieblas, se prepare un pueblo santo.",
    (14, 7): "Dice, pues, el profeta: Yo, el Señor tu Dios, te llamé en "
             "justicia, y tomaré tu mano, y te fortaleceré, y te di por "
             "alianza del linaje, por luz de las naciones, para abrir los "
             "ojos de los ciegos, y sacar de las cadenas a los aprisionados, "
             "y de la casa de la cárcel a los que están sentados en "
             "tinieblas. Conocemos, pues, de dónde fuimos rescatados.",
    (14, 8): "Otra vez dice el profeta: He aquí, te he puesto por luz de las "
             "naciones, para que seas salvación hasta lo último de la tierra; "
             "así dice el Señor, el Dios que te rescató.",
    (14, 9): "Y otra vez dice el profeta: El Espíritu del Señor está sobre "
             "mí, por cuanto me ungió para anunciar la gracia a los humildes; "
             "me ha enviado para sanar a los quebrantados de corazón, para "
             "pregonar a los cautivos libertad y a los ciegos vista, para "
             "proclamar el año agradable del Señor y el día de la "
             "retribución, para consolar a todos los que lloran.",

    # Capítulo 15
    (15, 1): "Además, también acerca del sábado está escrito en las diez "
             "palabras, en las cuales habló en el monte Sinaí a Moisés cara a "
             "cara: Y santificad el sábado del Señor con manos limpias y "
             "corazón limpio.",
    (15, 2): "Y en otro lugar dice: Si mis hijos guardan el sábado, entonces "
             "pondré mi misericordia sobre ellos.",
    (15, 3): "Del sábado habla al principio de la creación: E hizo Dios en "
             "seis días las obras de sus manos, y acabó en el día séptimo, y "
             "reposó en él, y lo santificó.",
    (15, 4): "Atended, hijos, a lo que dice: Acabó en seis días. Esto quiere "
             "decir que en seis mil años el Señor acabará todas las cosas; "
             "porque el día es para él mil años. Y él mismo me da testimonio, "
             "diciendo: He aquí, el día del Señor será como mil años. Así "
             "pues, hijos, en seis días, es decir, en los seis mil años, "
             "serán acabadas todas las cosas.",
    (15, 5): "Y reposó el día séptimo. Esto quiere decir: cuando su Hijo, "
             "viniendo, abolirá el tiempo del inicuo, y juzgará a los impíos, "
             "y cambiará el sol y la luna y las estrellas, entonces reposará "
             "bien en el día séptimo.",
    (15, 6): "Además dice: Lo santificarás con manos limpias y corazón "
             "limpio. Si, pues, alguno puede ahora santificar el día que Dios "
             "santificó, siendo limpio de corazón, en todo nos hemos "
             "engañado.",
    (15, 7): "Mira, pues, que entonces, reposando bien, lo santificaremos, "
             "cuando podamos, justificados nosotros mismos y habiendo "
             "recibido la promesa, no habiendo ya iniquidad, sino habiendo "
             "sido hechas nuevas todas las cosas por el Señor; entonces "
             "podremos santificarlo, santificados primero nosotros mismos.",
    (15, 8): "Además les dice: Vuestras lunas nuevas y vuestros sábados no "
             "los soporto. ¿Veis cómo dice? No me son aceptos los sábados de "
             "ahora, sino el que yo he hecho, en el cual, dando reposo a "
             "todas las cosas, haré el principio de un día octavo, que es el "
             "principio de otro mundo.",
    (15, 9): "Por eso también celebramos con alegría el día octavo, en el "
             "cual también Jesús resucitó de entre los muertos, y, habiéndose "
             "manifestado, subió a los cielos.",

    # Capítulo 16
    (16, 1): "Además os hablaré también acerca del templo: cómo, extraviados, "
             "los desdichados pusieron su esperanza en el edificio, y no en "
             "su Dios que los hizo, como si fuera casa de Dios.",
    (16, 2): "Porque casi como los gentiles lo consagraron en el templo. Pero "
             "aprended cómo habla el Señor, aboliéndolo: ¿Quién midió el "
             "cielo con el palmo, o la tierra con el puño? ¿No fui yo? Dice "
             "el Señor: El cielo es mi trono, y la tierra el estrado de mis "
             "pies; ¿qué casa me edificaréis, o cuál es el lugar de mi "
             "reposo? Habéis conocido que su esperanza es vana.",
    (16, 3): "Además dice otra vez: He aquí, los que derribaron este templo, "
             "ellos mismos lo edificarán.",
    (16, 4): "Así sucede; porque por hacer ellos la guerra, fue derribado por "
             "los enemigos; ahora también ellos mismos, los siervos de los "
             "enemigos, lo reedificarán.",
    (16, 5): "Otra vez fue manifestado cómo la ciudad, y el templo, y el "
             "pueblo de Israel habían de ser entregados. Porque dice la "
             "Escritura: Y sucederá en los últimos días que el Señor "
             "entregará las ovejas del pasto, y el redil, y la torre de ellas "
             "a la destrucción. Y sucedió conforme a lo que habló el Señor.",
    (16, 6): "Busquemos ahora si hay templo de Dios. Lo hay, donde él mismo "
             "dice que lo hace y lo perfecciona. Porque está escrito: Y "
             "sucederá que, cumpliéndose la semana, será edificado "
             "gloriosamente un templo de Dios en el nombre del Señor.",
    (16, 7): "Hallo, pues, que hay templo. Aprended, pues, cómo será "
             "edificado en el nombre del Señor. Antes de que nosotros "
             "creyésemos en Dios, la morada de nuestro corazón era "
             "corruptible y débil, verdaderamente como templo edificado por "
             "mano, porque estaba lleno de idolatría y era casa de demonios, "
             "por hacer cuanto era contrario a Dios.",
    (16, 8): "Pero será edificado en el nombre del Señor. Atended, pues, para "
             "que el templo del Señor sea edificado gloriosamente. Aprended "
             "cómo. Habiendo recibido el perdón de los pecados y esperado en "
             "el Nombre, fuimos hechos nuevos, creados otra vez desde el "
             "principio; por eso en nuestra morada verdaderamente Dios habita "
             "en nosotros.",
    (16, 9): "¿Cómo? Su palabra de fe, su llamamiento de la promesa, la "
             "sabiduría de las ordenanzas, los mandamientos de la enseñanza; "
             "él mismo profetizando en nosotros, él mismo habitando en "
             "nosotros; abriéndonos a nosotros, que estábamos esclavizados a "
             "la muerte, la puerta del templo, que es la boca, y dándonos "
             "arrepentimiento, nos introduce en el templo incorruptible.",
    (16, 10): "Porque el que anhela ser salvo no mira al hombre, sino al que "
              "habita y habla en él, asombrándose de él, porque nunca había "
              "oído de la boca del que habla tales palabras, ni él mismo "
              "había deseado jamás oírlas. Este es el templo espiritual que "
              "se edifica para el Señor.",

    # Capítulo 17
    (17, 1): "En cuanto fue posible y con sencillez manifestároslo, mi alma "
             "espera, conforme a mi deseo, no haber omitido nada de lo que "
             "conduce a la salvación.",
    (17, 2): "Porque si os escribo acerca de las cosas presentes o de las "
             "venideras, no las entenderéis, porque están puestas en "
             "parábolas. Esto, pues, sea así.",

    # Capítulo 18
    (18, 1): "Pasemos ahora también a otro conocimiento y enseñanza. Dos "
             "caminos hay de enseñanza y de poder: el de la luz y el de las "
             "tinieblas. Y es grande la diferencia entre los dos caminos. "
             "Porque sobre el uno están puestos ángeles de Dios portadores de "
             "luz, y sobre el otro, ángeles de Satanás.",
    (18, 2): "Y el uno es Señor desde los siglos y por los siglos; el otro, "
             "príncipe del tiempo presente de la iniquidad.",

    # Capítulo 19
    (19, 1): "El camino de la luz es, pues, este: si alguno, queriendo andar "
             "el camino hacia el lugar señalado, se apresura con sus obras. "
             "Es, pues, el conocimiento que se nos ha dado para andar en él "
             "el siguiente.",
    (19, 2): "Amarás al que te hizo, temerás al que te formó, glorificarás al "
             "que te rescató de la muerte; serás sencillo de corazón y rico "
             "de espíritu; no te juntarás con los que andan en el camino de "
             "la muerte; aborrecerás todo lo que no es agradable a Dios; "
             "aborrecerás toda hipocresía; no abandonarás los mandamientos "
             "del Señor.",
    (19, 3): "No te ensalzarás a ti mismo, sino que serás humilde de ánimo en "
             "todo; no te atribuirás gloria a ti mismo. No tomarás mal "
             "consejo contra tu prójimo; no darás a tu alma atrevimiento.",
    (19, 4): "No fornicarás, no adulterarás, no corromperás a los niños. No "
             "salga de ti la palabra de Dios entre la impureza de algunos. No "
             "harás acepción de personas al reprender a alguno por una falta. "
             "Serás manso, serás sosegado, serás temeroso de las palabras que "
             "has oído. No guardarás rencor a tu hermano.",
    (19, 5): "No serás de ánimo doble sobre si será o no. No tomarás en vano "
             "el nombre del Señor. Amarás a tu prójimo más que a tu propia "
             "alma. No matarás al hijo con el aborto, ni tampoco lo matarás "
             "después de nacido. No retirarás tu mano de tu hijo o de tu "
             "hija, sino que desde la juventud les enseñarás el temor de "
             "Dios.",
    (19, 6): "No codiciarás los bienes de tu prójimo, no serás avaro. Ni te "
             "juntarás de corazón con los altivos, sino que convivirás con "
             "los humildes y los justos. Los sucesos que te acontezcan los "
             "recibirás como buenos, sabiendo que sin Dios nada sucede.",
    (19, 7): "No serás de doble parecer ni charlatán. Te someterás a tus "
             "señores como a figura de Dios, con respeto y temor. No mandarás "
             "con amargura a tu siervo o a tu sierva, que esperan en el mismo "
             "Dios, no sea que dejen de temer al Dios que está sobre ambos; "
             "porque no vino a llamar según la apariencia de las personas, "
             "sino a aquellos a quienes el Espíritu preparó.",
    (19, 8): "Harás partícipe en todo a tu prójimo, y no dirás que las cosas "
             "son tuyas propias; porque si sois partícipes en lo "
             "incorruptible, ¿cuánto más en lo corruptible? No serás ligero "
             "de lengua, porque la boca es lazo de muerte. En cuanto puedas, "
             "guardarás la pureza por tu alma.",
    (19, 9): "No seas de los que para recibir extienden las manos y para dar "
             "las encogen. Amarás como a la niña de tu ojo a todo el que te "
             "hable la palabra del Señor.",
    (19, 10): "Te acordarás del día del juicio noche y día, y buscarás cada "
              "día el rostro de los santos, o trabajando con la palabra y "
              "yendo a exhortar y procurando salvar un alma por la palabra, o "
              "trabajando con tus manos para rescate de tus pecados.",
    (19, 11): "No vacilarás en dar, ni murmurarás cuando des; y conocerás "
              "quién es el buen remunerador de la recompensa. Guardarás lo "
              "que recibiste, sin añadir ni quitar. Aborrecerás el mal hasta "
              "el fin. Juzgarás con justicia.",
    (19, 12): "No harás cisma, sino que pondrás en paz a los que contienden, "
              "reconciliándolos. Confesarás tus pecados. No te acercarás a la "
              "oración con mala conciencia. Este es el camino de la luz.",

    # Capítulo 20
    (20, 1): "Pero el camino del Negro es tortuoso y lleno de maldición. "
             "Porque es camino de muerte eterna con castigo, en el cual están "
             "las cosas que pierden el alma de ellos: idolatría, "
             "atrevimiento, altivez de poder, hipocresía, doblez de corazón, "
             "adulterio, homicidio, rapiña, soberbia, transgresión, engaño, "
             "malicia, arrogancia, hechicería, magia, avaricia, falta de "
             "temor de Dios.",
    (20, 2): "Perseguidores de los buenos, que aborrecen la verdad, que aman "
             "la mentira, que no conocen la recompensa de la justicia, que no "
             "se juntan con el bien ni con el juicio justo, que no atienden a "
             "la viuda y al huérfano, que velan no para el temor de Dios, "
             "sino para el mal; de quienes están lejos y apartadas la "
             "mansedumbre y la paciencia; que aman las cosas vanas, que "
             "persiguen la retribución, que no se compadecen del pobre, que "
             "no se afligen por el oprimido, fáciles para la maledicencia, "
             "que no conocen al que los hizo, asesinos de niños, corruptores "
             "de la criatura de Dios, que se apartan del necesitado, que "
             "oprimen al afligido, abogados de los ricos, jueces inicuos de "
             "los pobres, pecadores en todo.",

    # Capítulo 21
    (21, 1): "Bueno es, pues, que el que ha aprendido las ordenanzas del "
             "Señor, cuantas están escritas, ande en ellas; porque el que "
             "hace estas cosas será glorificado en el reino de Dios; el que "
             "escoge aquellas otras perecerá juntamente con sus obras. Por "
             "esto hay resurrección, por esto hay retribución.",
    (21, 2): "Ruego a los que estáis en posición elevada, si aceptáis algún "
             "consejo de mi buena voluntad: tenéis entre vosotros a quienes "
             "hacer el bien; no faltéis.",
    (21, 3): "Cerca está el día en que todas las cosas perecerán juntamente "
             "con el maligno; cerca está el Señor y su recompensa.",
    (21, 4): "Una y otra vez os ruego: sed buenos legisladores de vosotros "
             "mismos, permaneced consejeros fieles de vosotros mismos, quitad "
             "de entre vosotros toda hipocresía.",
    (21, 5): "Y Dios, que señorea sobre todo el mundo, os dé sabiduría, "
             "inteligencia, ciencia, conocimiento de sus ordenanzas, "
             "paciencia.",
    (21, 6): "Y sed enseñados por Dios, buscando lo que el Señor busca de "
             "vosotros, y obrad de modo que seáis hallados en el día del "
             "juicio.",
    (21, 7): "Y si hay algún recuerdo del bien, acordaos de mí meditando "
             "estas cosas, para que tanto mi deseo como mi desvelo lleguen a "
             "algún bien. Os lo ruego, pidiéndolo como gracia.",
    (21, 8): "Mientras el buen vaso está todavía con vosotros, no faltéis en "
             "nada a vosotros mismos, sino buscad continuamente estas cosas y "
             "cumplid todo mandamiento; porque son dignas.",
    (21, 9): "Por eso me apresuré aún más a escribir de lo que pude, para "
             "alegraros. Sed salvos, hijos del amor y de la paz. El Señor de "
             "la gloria y de toda gracia sea con vuestro espíritu. Epístola "
             "de Bernabé.",
}
