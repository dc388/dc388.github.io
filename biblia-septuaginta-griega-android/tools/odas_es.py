"""Las Odas en español, traducidas del griego.

Para las Asambleas de Dios no son un libro aparte del canon: son una colección
litúrgica. Los códices griegos reunieron al final del Salterio los catorce
cánticos que la Iglesia antigua cantaba en las horas, y casi todos están ya en
la Biblia: el cántico del mar (Éxodo 15), el de Moisés (Deuteronomio 32), el de
Ana (1 Samuel 2), el de Habacuc, el de Isaías 26, el de Jonás, el de Ezequías
(Isaías 38), el de los tres jóvenes del horno, y del Nuevo Testamento el
Magníficat, el Nunc dimittis y el Benedictus.

Entonces, ¿para qué tenerlas aparte si ya están? Por dos razones.

La primera es que aquí están en griego, y el griego a veces dice otra cosa. El
ejemplo que más pesa es Oda 2:8 —Deuteronomio 32:8—: donde el texto hebreo que
usa la Reina-Valera dice «según el número de los hijos de Israel», el griego
dice «según el número de los ángeles de Dios». Los manuscritos de Qumrán dan la
razón al griego. Ésa es exactamente la clase de diferencia por la que vale la
pena tener la Septuaginta al lado, y por la que estos cánticos no se han
copiado de la Reina-Valera sino traducido del griego que está en la aplicación.

La segunda es la Oración de Manasés (oda 8), que no está en ninguna otra
parte: la súplica que se puso en boca del peor rey de Judá, el que llenó
Jerusalén de sangre y acabó preso en Babilonia. «He doblado las rodillas de mi
corazón» es de las mejores frases que dejó el judaísmo del segundo templo.

La numeración de esta edición griega es la suya: no hay oda 4, y algunos
epígrafes aparecen metidos dentro de un versículo en vez de encabezar el
cántico (así el título de la oda 2 dentro del versículo 19). Se traduce donde
el texto lo pone.
"""

from __future__ import annotations

ODAS_ES: dict[tuple[int, ...], str] = {
    (1, 0): "Cántico de Moisés en el Éxodo.",
    (1, 1): "Cantemos al Señor, porque se ha cubierto de gloria: caballo y "
            "jinete arrojó al mar.",
    (1, 2): "Auxilio y amparo fue para mí, para salvarme; éste es mi Dios, y "
            "lo glorificaré; Dios de mi padre, y lo ensalzaré.",
    (1, 3): "El Señor, que quebranta las guerras: Señor es su nombre.",
    (1, 4): "Los carros del faraón y su ejército los arrojó al mar; a sus "
            "mejores jinetes, a sus capitanes, los hundió en el mar Rojo;",
    (1, 5): "el piélago los cubrió; se hundieron en el abismo como una "
            "piedra.",
    (1, 6): "Tu diestra, Señor, se ha cubierto de gloria por su fuerza; tu "
            "mano derecha, Señor, quebrantó a los enemigos;",
    (1, 7): "y con la grandeza de tu gloria trituraste a los adversarios; "
            "enviaste tu ira, y los devoró como a rastrojo.",
    (1, 8): "Y con el soplo de tu furor se separó el agua; se cuajaron como un "
            "muro las aguas, se cuajaron las olas en medio del mar.",
    (1, 9): "Dijo el enemigo: «Los perseguiré y los alcanzaré; repartiré los "
            "despojos, saciaré mi deseo; los mataré con mi espada, mi mano se "
            "enseñoreará».",
    (1, 10): "Enviaste tu soplo, y los cubrió el mar; se hundieron como plomo "
             "en aguas impetuosas.",
    (1, 11): "¿Quién como tú entre los dioses, Señor? ¿Quién como tú, glorioso "
             "en los santos, admirable en tus hazañas, que hace prodigios?",
    (1, 12): "Extendiste tu diestra, y la tierra se los tragó.",
    (1, 13): "Guiaste con tu justicia a este pueblo tuyo, al que rescataste; "
             "lo condujiste con tu fuerza a tu morada santa.",
    (1, 14): "Lo oyeron las naciones y temieron; dolores de parto se "
             "apoderaron de los habitantes de Filistea.",
    (1, 15): "Entonces se apresuraron los caudillos de Edom, y a los príncipes "
             "de Moab los agarró el temblor; se derritieron todos los "
             "habitantes de Canaán.",
    (1, 16): "Caiga sobre ellos miedo y temblor; por la grandeza de tu brazo "
             "queden como piedra, hasta que pase tu pueblo, Señor, hasta que "
             "pase este pueblo tuyo que adquiriste.",
    (1, 17): "Introdúcelos y plántalos en el monte de tu heredad, en la morada "
             "dispuesta que te hiciste, en el santuario, Señor, que "
             "prepararon tus manos.",
    (1, 18): "El Señor reina por siempre y para siempre jamás.",
    (1, 19): "Porque entraron en el mar los caballos del faraón con sus carros "
             "y sus jinetes, y el Señor hizo volver sobre ellos el agua del "
             "mar; pero los hijos de Israel pasaron a pie enjuto por en medio "
             "del mar.",

    (2, 1): "Escucha, cielo, y hablaré; y oiga la tierra las palabras de mi "
            "boca.",
    (2, 2): "Espérese como lluvia mi sentencia, y baje como rocío mi palabra; "
            "como aguacero sobre la grama y como nevada sobre la hierba.",
    (2, 3): "Porque he invocado el nombre del Señor: dad grandeza a nuestro "
            "Dios.",
    (2, 4): "Dios: verdaderas son sus obras, y todos sus caminos, justicia; "
            "Dios fiel, y no hay en él injusticia; justo y santo es el Señor.",
    (2, 5): "Pecaron; no son hijos suyos, sino tachados; generación torcida y "
            "descarriada.",
    (2, 6): "¿Así se lo pagáis al Señor, pueblo necio y no sabio? ¿No es él tu "
            "padre, que te adquirió y te hizo y te creó?",
    (2, 7): "Acordaos de los días antiguos, considerad los años de "
            "generaciones y generaciones; pregunta a tu padre, y te lo "
            "anunciará; a tus ancianos, y te lo dirán.",
    (2, 8): "Cuando el Altísimo repartía las naciones, cuando dispersaba a los "
            "hijos de Adán, fijó los términos de los pueblos según el número "
            "de los ángeles de Dios;",
    (2, 9): "y la porción del Señor fue su pueblo Jacob, la cuerda de su "
            "heredad, Israel.",
    (2, 10): "Le bastó a él en el desierto, en la sed del calor abrasador, en "
             "tierra sin agua; lo rodeó y lo instruyó, y lo guardó como a la "
             "niña de sus ojos.",
    (2, 11): "Como el águila que protege su nido y se cierne sobre sus "
             "polluelos, extendió sus alas y los recibió y los llevó sobre sus "
             "espaldas.",
    (2, 12): "El Señor solo los guiaba, y no había con ellos dios extraño.",
    (2, 13): "Los hizo subir a lo alto de la tierra; los alimentó con los "
             "frutos de los campos; mamaron miel de la peña y aceite de la "
             "roca dura;",
    (2, 14): "manteca de vacas y leche de ovejas, con grasa de corderos y de "
             "carneros, de becerros y de machos cabríos, con la flor del "
             "trigo; y bebieron vino, sangre de uvas.",
    (2, 15): "Y comió Jacob y se sació, y el amado dio coces; engordó, se puso "
             "grueso, se ensanchó; y abandonó al Dios que lo hizo, y se apartó "
             "de Dios, su salvador.",
    (2, 16): "Me provocaron con dioses extraños; con sus abominaciones me "
             "irritaron.",
    (2, 17): "Ofrecieron sacrificios a los demonios y no a Dios, a dioses que "
             "no conocían; nuevos y recién llegados, a los que no conocieron "
             "sus padres.",
    (2, 18): "Abandonaste al Dios que te hizo, y te olvidaste del Dios que te "
             "alimenta.",
    (2, 19): "Cántico de Moisés en el Deuteronomio. Y lo vio el Señor y tuvo "
             "celos, y se irritó de ira por sus hijos y por sus hijas;",
    (2, 20): "y dijo: «Apartaré de ellos mi rostro y mostraré lo que les "
             "sucederá al final; porque son una generación pervertida, hijos "
             "en quienes no hay fidelidad.",
    (2, 21): "Ellos me dieron celos con lo que no es Dios, me irritaron con "
             "sus ídolos; y yo les daré celos con lo que no es pueblo, con una "
             "nación insensata los irritaré.",
    (2, 22): "Porque un fuego se ha encendido de mi furor, y arderá hasta lo "
             "hondo del Hades; devorará la tierra y sus frutos, abrasará los "
             "cimientos de los montes.",
    (2, 23): "Amontonaré males sobre ellos y agotaré en ellos mis flechas.",
    (2, 24): "Consumidos por el hambre y devorados por las aves, y por una "
             "peste incurable; enviaré contra ellos dientes de fieras, con el "
             "furor de las que se arrastran por la tierra.",
    (2, 25): "Por fuera los dejará sin hijos la espada, y por dentro el "
             "espanto: al joven con la doncella, al niño de pecho con el "
             "anciano.",
    (2, 26): "Dije: «Los dispersaré, haré desaparecer de entre los hombres su "
             "memoria»;",
    (2, 27): "si no fuera por la ira de los enemigos, para que no se "
             "envalentonen, y para que no se echen encima los adversarios; no "
             "vayan a decir: «Nuestra mano es poderosa, y no ha sido el Señor "
             "quien ha hecho todo esto».",
    (2, 28): "Porque son una nación que ha perdido el juicio, y no hay en "
             "ellos entendimiento.",
    (2, 29): "No fueron capaces de comprender esto; acéptenlo para el tiempo "
             "que viene.",
    (2, 30): "¿Cómo perseguirá uno a mil, y dos pondrán en fuga a diez mil, si "
             "no es porque Dios los vendió y el Señor los entregó?",
    (2, 31): "Porque sus dioses no son como nuestro Dios; y nuestros enemigos "
             "son necios.",
    (2, 32): "Porque de la viña de Sodoma es su viña, y su sarmiento de "
             "Gomorra; sus uvas son uvas de hiel, racimos amargos para ellos;",
    (2, 33): "su vino es furor de dragones, y furor incurable de áspides.",
    (2, 34): "¿No está todo esto guardado junto a mí y sellado en mis "
             "tesoros?",
    (2, 35): "En el día de la venganza daré el pago, en el momento en que "
             "resbale su pie; porque está cerca el día de su perdición, y os "
             "está preparado lo que ha de venir.",
    (2, 36): "Porque el Señor juzgará a su pueblo y se compadecerá de sus "
             "siervos; porque los vio agotados y desfallecidos por la "
             "opresión, y abatidos.",
    (2, 37): "Y dijo el Señor: «¿Dónde están sus dioses, aquellos en los que "
             "confiaban,",
    (2, 38): "de cuyos sacrificios comíais la grasa y bebíais el vino de sus "
             "libaciones? Levántense y os socorran, y sean vuestro amparo.",
    (2, 39): "Ved, ved que yo soy, y que no hay Dios fuera de mí; yo hago "
             "morir y hago vivir; yo hiero y yo sano, y no hay quien libre de "
             "mis manos.",
    (2, 40): "Porque alzaré al cielo mi mano y juraré por mi diestra, y diré: "
             "Vivo yo para siempre;",
    (2, 41): "porque afilaré mi espada como un relámpago, y mi mano se "
             "aferrará al juicio; y me vengaré, y daré su merecido a mis "
             "enemigos, y a los que me aborrecen les daré su pago.",
    (2, 42): "Embriagaré mis flechas de sangre, y mi espada devorará carne: "
             "sangre de heridos y de cautivos, de la cabeza de los príncipes "
             "de las naciones».",
    (2, 43): "Alegraos, cielos, con él, y adórenlo todos los ángeles de Dios; "
             "alegraos, naciones, con su pueblo, y fortalézcanlo todos los "
             "hijos de Dios; porque él venga la sangre de sus hijos, y tomará "
             "venganza y dará su merecido a los enemigos; y a los que lo "
             "aborrecen les dará su pago, y el Señor limpiará la tierra de su "
             "pueblo.",

    (3, 1): "Se ha afianzado mi corazón en el Señor, se ha exaltado mi poder "
            "en mi Dios; se ha ensanchado mi boca contra mis enemigos, me he "
            "alegrado en tu salvación.",
    (3, 2): "Porque no hay santo como el Señor, y no hay justo como nuestro "
            "Dios; no hay santo fuera de ti.",
    (3, 3): "No os jactéis ni habléis con altanería, ni salga de vuestra boca "
            "la fanfarronería; porque el Señor es un Dios que sabe, y un Dios "
            "que dispone sus obras.",
    (3, 4): "El arco de los fuertes se ha quebrado, y los débiles se han "
            "ceñido de fuerza.",
    (3, 5): "Los que estaban hartos de pan han quedado menguados, y los "
            "hambrientos han dejado atrás la tierra; porque la estéril ha dado "
            "a luz siete, y la que tenía muchos hijos ha quedado sin fuerzas.",
    (3, 6): "El Señor hace morir y hace vivir; hace bajar al Hades y hace "
            "subir.",
    (3, 7): "El Señor empobrece y enriquece, humilla y ensalza;",
    (3, 8): "levanta del polvo al indigente y alza del estercolero al pobre, "
            "para sentarlo con los poderosos del pueblo y darles en herencia "
            "un trono de gloria;",
    (3, 9): "concede lo pedido al que hace un voto, y bendijo los años del "
            "justo. Porque el hombre no es fuerte por su propia fuerza;",
    (3, 10): "el Señor debilitará a su adversario; el Señor es santo. No se "
             "gloríe el sabio en su sabiduría, ni se gloríe el fuerte en su "
             "fuerza, ni se gloríe el rico en su riqueza; sino que en esto se "
             "gloríe el que se gloría: en entender y conocer al Señor, y en "
             "hacer juicio y justicia en medio de la tierra. El Señor subió a "
             "los cielos y tronó; él juzgará los confines de la tierra, siendo "
             "justo; y da fuerza a nuestros reyes, y exaltará el poder de su "
             "ungido.",
    (3, 43): "Oración de Ana, madre de Samuel.",

    (5, 3): "Clamé en mi angustia al Señor mi Dios, y me escuchó; desde el "
            "vientre del Hades subió mi grito: oíste mi voz.",
    (5, 4): "Me arrojaste a lo hondo del corazón del mar, y los ríos me "
            "rodearon; todas tus olas y tus oleajes pasaron sobre mí.",
    (5, 5): "Y yo dije: «He sido arrojado lejos de tus ojos; ¿volveré acaso a "
            "mirar hacia tu templo santo?».",
    (5, 6): "Me rodeó el agua hasta el alma; el abismo profundo me cercó, mi "
            "cabeza se hundió en las hendiduras de los montes;",
    (5, 7): "bajé a la tierra cuyos cerrojos son cerraduras eternas. Pero haz "
            "subir de la corrupción mi vida, Señor Dios mío.",
    (5, 8): "Cuando mi alma desfallecía dentro de mí, me acordé del Señor; y "
            "llegue hasta ti mi oración, a tu templo santo.",
    (5, 9): "Los que guardan cosas vanas y falsas abandonaron su propia "
            "misericordia;",
    (5, 10): "pero yo, con voz de alabanza y de acción de gracias, te ofreceré "
             "sacrificio; cumpliré lo que prometí, para salvación mía, al "
             "Señor.",
    (5, 20): "Oración de Jonás.",

    (6, 1): "Oración de Habacuc.",
    (6, 2): "Señor, he oído tu fama y he temido; he considerado tus obras y he "
            "quedado atónito. En medio de dos seres vivos serás conocido; al "
            "acercarse los años serás reconocido; al llegar el tiempo serás "
            "manifestado; cuando se turbe mi alma, en la ira te acordarás de "
            "la misericordia.",
    (6, 3): "Dios vendrá de Temán, y el Santo del monte Farán, umbroso y "
            "espeso. Su poder cubrió los cielos, y la tierra se llenó de su "
            "alabanza.",
    (6, 4): "Y su resplandor será como la luz; prodigios hay en sus manos; y "
            "puso allí el amor poderoso de su fuerza.",
    (6, 5): "Delante de él irá la palabra, y saldrá al campo; sus pies van "
            "calzados.",
    (6, 6): "Se detuvo, y se estremeció la tierra; miró, y se derritieron las "
            "naciones; y los montes se hicieron pedazos con violencia; se "
            "derritieron las colinas eternas por sus caminos eternos.",
    (6, 7): "En lugar de fatigas vi las tiendas de los etíopes; se espantarán "
            "también las tiendas de la tierra de Madián. Pausa.",
    (6, 8): "¿Acaso te irritaste contra los ríos, Señor? ¿Acaso fue contra los "
            "ríos tu furor, o contra el mar tu arremetida? Porque montarás "
            "sobre tus caballos, y tu cabalgata es salvación.",
    (6, 9): "Tensando tensarás tu arco contra los cetros, dice el Señor; la "
            "tierra se hendirá con torrentes.",
    (6, 10): "Te verán y se retorcerán los pueblos; esparces las aguas a tu "
             "paso; el abismo dio su voz, alzó a lo alto su figura.",
    (6, 11): "El sol y la luna se detuvieron en su lugar; tus saetas caminarán "
             "hacia la luz, hacia el resplandor del relámpago de tus armas.",
    (6, 12): "Con tu amenaza mermarás la tierra, y con tu furor abatirás a las "
             "naciones.",
    (6, 13): "Saliste para la salvación de tu pueblo, para salvar a tus "
             "ungidos; lanzaste la muerte sobre las cabezas de los inicuos; "
             "tendiste tus ataduras hasta el cuello.",
    (6, 14): "Partiste en el espanto las cabezas de los poderosos; temblarán "
             "en ella; abrirán sus bocados como el pobre que come a "
             "escondidas.",
    (6, 15): "E hiciste entrar en el mar tus caballos, que revolvían muchas "
             "aguas.",
    (6, 16): "Estuve alerta, y se estremecieron mis entrañas por la voz de la "
             "oración de mis labios, y entró el temblor en mis huesos, y por "
             "dentro se turbó mi ánimo. Descansaré en el día de mi angustia, "
             "para subir al pueblo de mi destierro.",
    (6, 17): "Porque la higuera no dará fruto, ni habrá cosecha en las viñas; "
             "fallará el trabajo del olivo, y los campos no darán alimento; se "
             "acabaron las ovejas del redil, y no hay bueyes en los pesebres "
             "de su expiación;",
    (6, 18): "pero yo me alegraré en el Señor, me gozaré en Dios, mi "
             "salvador.",
    (6, 19): "El Señor Dios es mi fuerza, y afirmará mis pies hasta el fin; me "
             "hará subir a las alturas, para vencer con su cántico.",

    (7, 10): "Yo dije: «En la plenitud de mis días iré a las puertas del "
             "Hades; dejaré los años que me quedaban».",
    (7, 11): "Dije: «Ya no veré la salvación de Dios sobre la tierra; ya no "
             "veré a hombre alguno entre los que habitan el mundo».",
    (7, 12): "Me he ido de entre los míos, he dejado el resto de mi vida; se "
             "fue y se apartó de mí como el que desmonta la tienda que había "
             "plantado; mi vida se me ha vuelto como un telar cuando la "
             "tejedora se acerca a cortarlo.",
    (7, 13): "Aquel día fui entregado hasta la mañana como a un león; así me "
             "trituró todos los huesos; porque desde el día hasta la noche fui "
             "entregado.",
    (7, 14): "Como una golondrina, así gritaré, y como una paloma, así "
             "gemiré. Porque se me acabaron los ojos de mirar a lo alto del "
             "cielo hacia el Señor, que me libró y me quitó el dolor del "
             "alma.",
    (7, 16): "Señor, también de esto se te dio aviso; y despertaste mi "
             "aliento, y, consolado, viví.",
    (7, 17): "Porque tomaste mi alma para que no pereciese, y arrojaste detrás "
             "de mí todos mis pecados.",
    (7, 18): "Porque no te alabarán los que están en el Hades, ni te "
             "bendecirán los muertos, ni esperarán tu misericordia los que "
             "están en el Hades.",
    (7, 19): "Oración de Ezequías. Los vivos te bendecirán, como también yo; "
             "porque desde hoy engendraré hijos que anunciarán tu justicia, "
             "Señor de mi salvación;",
    (7, 20): "y no dejaré de bendecirte con el salterio todos los días de mi "
             "vida, delante de la casa de Dios.",

    (8, 1): "Señor todopoderoso, que estás en el cielo, Dios de nuestros "
            "padres, de Abrahán y de Isaac y de Jacob y de su descendencia "
            "justa;",
    (8, 2): "el que hizo el cielo y la tierra con todo su ornato;",
    (8, 3): "el que encadenó el mar con la palabra de tu mandato; el que cerró "
            "el abismo y lo selló con tu nombre temible y glorioso,",
    (8, 4): "ante quien todo se estremece y tiembla delante de tu poder;",
    (8, 5): "porque es insoportable la magnificencia de tu gloria, e "
            "irresistible la ira de tu amenaza contra los pecadores;",
    (8, 6): "y sin medida e inescrutable la misericordia de tu promesa;",
    (8, 7): "porque tú eres el Señor altísimo, entrañable, paciente y muy "
            "misericordioso, y que se arrepiente de los males de los hombres.",
    (8, 8): "Tú, pues, Señor, Dios de los justos, no pusiste arrepentimiento "
            "para los justos, para Abrahán y para Isaac y para Jacob, que no "
            "pecaron contra ti; sino que pusiste arrepentimiento para mí, que "
            "soy pecador.",
    (8, 9): "Porque he pecado más que la arena del mar, y se han multiplicado "
            "mis iniquidades; y no soy digno de levantar la vista y de mirar a "
            "lo alto del cielo, por la multitud de mis injusticias;",
    (8, 10): "encorvado bajo el peso de muchas cadenas de hierro, sin poder "
             "levantar la cabeza por mis pecados, y no hay alivio para mí; "
             "porque provoqué tu furor e hice el mal delante de ti, levantando "
             "abominaciones y multiplicando los ídolos.",
    (8, 11): "Y ahora doblo las rodillas de mi corazón, suplicando tu "
             "bondad.",
    (8, 12): "He pecado, Señor, he pecado, y reconozco mis iniquidades;",
    (8, 13): "te pido suplicándote: perdóname, Señor, perdóname; no me hagas "
             "perecer con mis iniquidades, ni me guardes rencor eterno "
             "reservándome los males, ni me condenes a lo más hondo de la "
             "tierra; porque tú eres, Señor, el Dios de los que se "
             "arrepienten,",
    (8, 14): "y en mí mostrarás tu bondad; porque, siendo yo indigno, me "
             "salvarás según tu gran misericordia,",
    (8, 15): "y te alabaré continuamente todos los días de mi vida. Porque a "
             "ti te canta todo el ejército de los cielos, y tuya es la gloria "
             "por los siglos. Amén.",
    (8, 20): "Oración de Manasés.",
    (9, 15): "Oración de Azarías.",
    (9, 26): "Bendito eres tú, Señor Dios de nuestros padres, y digno de alabanza y glorificado es tu nombre por los siglos;",
    (9, 27): "porque eres justo en todo lo que has hecho con nosotros, y todas tus obras son verdaderas, y rectos tus caminos, y todos tus juicios verdaderos;",
    (9, 28): "y sentencias de verdad has dictado en todo cuanto has hecho con nosotros y con la ciudad santa de nuestros padres, Jerusalén; porque con verdad y con juicio has traído todo esto por nuestros pecados.",
    (9, 29): "Porque hemos pecado y hemos cometido iniquidad apartándonos de ti, y hemos delinquido en todo;",
    (9, 30): "y no escuchamos tus mandamientos, ni los guardamos ni los cumplimos como nos mandaste para que nos fuera bien.",
    (9, 31): "Y todo cuanto has traído sobre nosotros, y todo cuanto has hecho con nosotros, lo has hecho con juicio verdadero;",
    (9, 32): "y nos entregaste en manos de enemigos inicuos, odiosísimos y rebeldes, y a un rey injusto y el más perverso de toda la tierra.",
    (9, 33): "Y ahora no podemos abrir la boca: la vergüenza y el oprobio han caído sobre tus siervos y sobre los que te veneran.",
    (9, 34): "No nos entregues del todo, por causa de tu nombre, ni deshagas tu alianza,",
    (9, 35): "ni apartes de nosotros tu misericordia, por Abrahán, tu amado, y por Isaac, tu siervo, y por Israel, tu santo,",
    (9, 36): "a los que hablaste prometiendo multiplicar su descendencia como las estrellas del cielo y como la arena de la orilla del mar.",
    (9, 37): "Porque, Señor, hemos quedado reducidos más que todas las naciones, y hoy estamos humillados en toda la tierra por nuestros pecados;",
    (9, 38): "y en este tiempo no hay príncipe ni profeta ni caudillo, ni holocausto ni sacrificio ni ofrenda ni incienso, ni lugar donde ofrecerte los frutos y hallar misericordia.",
    (9, 39): "Pero seamos recibidos con el alma quebrantada y con espíritu humillado,",
    (9, 40): "como con holocaustos de carneros y de toros, y como con millares de corderos cebados; así sea hoy nuestro sacrificio delante de ti, y que se cumpla en pos de ti; porque no hay vergüenza para los que confían en ti.",
    (9, 41): "Y ahora te seguimos de todo corazón y te tememos, y buscamos tu rostro.",
    (9, 42): "No nos avergüences, sino trátanos conforme a tu indulgencia y conforme a la abundancia de tu misericordia;",
    (9, 43): "y líbranos conforme a tus maravillas, y da gloria a tu nombre, Señor.",
    (9, 44): "Y queden confundidos todos los que hacen mal a tus siervos; sean avergonzados y despojados de todo poder y dominio, y sea quebrantada su fuerza;",
    (9, 45): "y sepan que tú eres el Señor, el único Dios, y glorioso sobre toda la tierra habitada.",
    (10, 51): "Himno de nuestros padres.",
    (10, 52): "Bendito eres tú, Señor Dios de nuestros padres, y digno de alabanza y ensalzado por los siglos; y bendito el nombre santo de tu gloria, y digno de suma alabanza y ensalzado por los siglos.",
    (10, 53): "Bendito eres en el templo de tu santa gloria, y digno de sumo himno y sumamente glorioso por los siglos.",
    (10, 54): "Bendito eres tú, que miras los abismos, sentado sobre los querubines, y digno de sumo himno y ensalzado por los siglos.",
    (10, 55): "Bendito eres en el trono de tu reino, y digno de sumo himno y ensalzado por los siglos.",
    (10, 56): "Bendito eres en el firmamento del cielo, y digno de sumo himno y sumamente glorioso por los siglos.",
    (10, 57): "Bendecid al Señor, todas las obras del Señor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 58): "Bendecid al Señor, cielos; cantadle himnos y ensalzadlo por los siglos.",
    (10, 59): "Bendecid al Señor, ángeles del Señor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 60): "Bendecid al Señor, todas las aguas que están sobre el cielo; cantadle himnos y ensalzadlo por los siglos.",
    (10, 61): "Bendecid al Señor, todos los ejércitos del Señor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 62): "Bendecid al Señor, sol y luna; cantadle himnos y ensalzadlo por los siglos.",
    (10, 63): "Bendecid al Señor, estrellas del cielo; cantadle himnos y ensalzadlo por los siglos.",
    (10, 64): "Bendecid al Señor, toda lluvia y rocío; cantadle himnos y ensalzadlo por los siglos.",
    (10, 65): "Bendecid al Señor, todos los vientos; cantadle himnos y ensalzadlo por los siglos.",
    (10, 66): "Bendecid al Señor, fuego y calor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 67): "Bendecid al Señor, frío y bochorno; cantadle himnos y ensalzadlo por los siglos.",
    (10, 68): "Bendecid al Señor, rocíos y nevadas; cantadle himnos y ensalzadlo por los siglos.",
    (10, 69): "Bendecid al Señor, hielo y frío; cantadle himnos y ensalzadlo por los siglos.",
    (10, 70): "Bendecid al Señor, escarchas y nieves; cantadle himnos y ensalzadlo por los siglos.",
    (10, 71): "Bendecid al Señor, noches y días; cantadle himnos y ensalzadlo por los siglos.",
    (10, 72): "Bendecid al Señor, luz y tinieblas; cantadle himnos y ensalzadlo por los siglos.",
    (10, 73): "Bendecid al Señor, relámpagos y nubes; cantadle himnos y ensalzadlo por los siglos.",
    (10, 74): "Bendiga la tierra al Señor; cántele himnos y ensálcelo por los siglos.",
    (10, 75): "Bendecid al Señor, montes y colinas; cantadle himnos y ensalzadlo por los siglos.",
    (10, 76): "Bendecid al Señor, todo lo que germina en la tierra; cantadle himnos y ensalzadlo por los siglos.",
    (10, 77): "Bendecid al Señor, fuentes; cantadle himnos y ensalzadlo por los siglos.",
    (10, 78): "Bendecid al Señor, mares y ríos; cantadle himnos y ensalzadlo por los siglos.",
    (10, 79): "Bendecid al Señor, cetáceos y todo lo que se mueve en las aguas; cantadle himnos y ensalzadlo por los siglos.",
    (10, 80): "Bendecid al Señor, todas las aves del cielo; cantadle himnos y ensalzadlo por los siglos.",
    (10, 81): "Bendecid al Señor, fieras y todos los ganados; cantadle himnos y ensalzadlo por los siglos.",
    (10, 82): "Bendecid al Señor, hijos de los hombres; cantadle himnos y ensalzadlo por los siglos.",
    (10, 83): "Bendiga Israel al Señor; cántele himnos y ensálcelo por los siglos.",
    (10, 84): "Bendecid al Señor, sacerdotes del Señor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 85): "Bendecid al Señor, siervos del Señor; cantadle himnos y ensalzadlo por los siglos.",
    (10, 86): "Bendecid al Señor, espíritus y almas de los justos; cantadle himnos y ensalzadlo por los siglos.",
    (10, 87): "Bendecid al Señor, santos y humildes de corazón; cantadle himnos y ensalzadlo por los siglos.",
    (10, 88): "Bendecid al Señor, Ananías, Azarías, Misael; cantadle himnos y ensalzadlo por los siglos.",
    (11, 46): "Engrandece mi alma al Señor,",
    (11, 47): "y se ha alegrado mi espíritu en Dios mi salvador;",
    (11, 48): "porque ha mirado la humildad de su sierva; pues desde ahora me llamarán dichosa todas las generaciones,",
    (11, 49): "porque me ha hecho grandes cosas el Poderoso; y santo es su nombre.",
    (11, 50): "Y su misericordia va de generación en generación sobre los que le temen.",
    (11, 51): "Hizo proezas con su brazo; dispersó a los soberbios en el pensamiento de su corazón.",
    (11, 52): "Derribó a los poderosos de sus tronos y ensalzó a los humildes.",
    (11, 53): "A los hambrientos los colmó de bienes, y a los ricos los despidió vacíos.",
    (11, 54): "Socorrió a Israel su siervo, acordándose de su misericordia,",
    (11, 55): "como lo había dicho a nuestros padres, a Abrahán y a su descendencia para siempre.",
    (11, 88): "Oración de María, la madre de Dios.",
    (12, 29): "Ahora, Señor, despides a tu siervo en paz, conforme a tu palabra;",
    (12, 30): "porque han visto mis ojos tu salvación,",
    (12, 31): "la que has preparado ante la faz de todos los pueblos:",
    (12, 32): "luz para revelación de las naciones y gloria de tu pueblo Israel.",
    (12, 55): "Oración de Simeón.",
    (13, 32): "Oración de Zacarías.",
    (13, 68): "Bendito el Señor, Dios de Israel, porque ha visitado y ha hecho redención a su pueblo,",
    (13, 69): "y nos ha levantado un cuerno de salvación en la casa de David su siervo,",
    (13, 70): "como lo había dicho por boca de sus santos profetas de siempre:",
    (13, 71): "salvación de nuestros enemigos y de la mano de todos los que nos aborrecen;",
    (13, 72): "para hacer misericordia con nuestros padres y acordarse de su santa alianza,",
    (13, 73): "del juramento que juró a Abrahán nuestro padre, de concedernos que, librados de la mano de nuestros enemigos, le sirvamos sin temor",
    (13, 75): "en santidad y justicia delante de él todos nuestros días.",
    (13, 76): "Y tú, niño, serás llamado profeta del Altísimo, porque irás delante del Señor a preparar sus caminos,",
    (13, 77): "para dar a su pueblo el conocimiento de la salvación en el perdón de sus pecados,",
    (13, 78): "por las entrañas de misericordia de nuestro Dios, con las que nos ha visitado el sol que nace de lo alto,",
    (13, 79): "para alumbrar a los que están sentados en tinieblas y en sombra de muerte, y para enderezar nuestros pies por el camino de la paz.",
    (14, 79): "Himno de la mañana. Gloria a Dios en las alturas, y en la tierra paz, en los hombres la buena voluntad. Te alabamos, te bendecimos, te adoramos, te glorificamos, te damos gracias por tu gran gloria, Señor, rey celestial, Dios Padre todopoderoso; Señor, Hijo unigénito, Jesucristo, y Espíritu Santo. Señor Dios, Cordero de Dios, Hijo del Padre, que quitas los pecados del mundo, ten piedad de nosotros; tú que quitas los pecados del mundo, ten piedad de nosotros; recibe nuestra súplica; tú que estás sentado a la derecha del Padre, ten piedad de nosotros. Porque sólo tú eres santo, sólo tú Señor, Jesucristo, para gloria de Dios Padre. Amén. Cada día te bendeciré y alabaré tu nombre por siempre y por los siglos de los siglos. Dígnate, Señor, guardarnos también hoy sin pecado. Bendito eres tú, Señor Dios de nuestros padres, y digno de alabanza y glorificado es tu nombre por los siglos. Amén. Bendito eres, Señor: enséñame tus preceptos; bendito eres, Señor: enséñame tus preceptos; bendito eres, Señor: enséñame tus preceptos. Señor, tú has sido nuestro refugio de generación en generación. Yo dije: «Señor, ten piedad de mí; sana mi alma, porque he pecado contra ti». Señor, a ti me he acogido; enséñame a hacer tu voluntad, porque tú eres mi Dios; porque en ti está la fuente de la vida, y en tu luz veremos la luz. Extiende tu misericordia a los que te conocen.",
}
