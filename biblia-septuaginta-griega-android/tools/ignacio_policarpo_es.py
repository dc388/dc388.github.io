"""Ignacio de Antioquía a Policarpo, traducida del griego.

La única de las siete dirigida a una persona: a Policarpo, obispo de Esmirna,
con consejos de un obispo a otro más joven.

Mismo criterio que el resto de las traducciones propias: se traduce del griego
que está en la aplicación (Kirsopp Lake, 1912-1913) y no de una traducción
inglesa; las lagunas van con […]; los corchetes del editor se conservan; las
citas de la Escritura siguen la Reina-Valera de 1909 cuando el griego dice lo
mismo, y lo que dice el griego cuando no. El saludo de las cartas va como
capítulo 1, versículo 0.
"""

from __future__ import annotations

IGNACIO_POLICARPO_ES: dict[tuple[int, ...], str] = {
    # Capítulo 1
    (1, 0): "Ignacio, llamado también Teóforo, a Policarpo, obispo de la "
            "iglesia de los esmirniotas, o más bien, que tiene por obispo a "
            "Dios Padre y al Señor Jesucristo: abundante salud.",
    (1, 1): "Aprobando tu sentir en Dios, afianzado como sobre roca "
            "inconmovible, glorifico sobremanera, por haber sido tenido por "
            "digno de ver tu rostro irreprensible, del cual ojalá goce yo en "
            "Dios.",
    (1, 2): "Te exhorto, por la gracia de que estás revestido, a que añadas a "
            "tu carrera y a que exhortes a todos para que sean salvos. Haz "
            "honor a tu puesto con toda diligencia, así carnal como "
            "espiritual. Cuida de la unión, que no hay cosa mejor. Sobrelleva "
            "a todos, como también a ti el Señor; soporta a todos en amor, "
            "como ya lo haces.",
    (1, 3): "Dedícate a oraciones incesantes; pide más entendimiento del que "
            "tienes; vela, poseyendo un espíritu que no duerme. Habla a cada "
            "uno en particular según la costumbre de Dios; sobrelleva las "
            "enfermedades de todos como atleta perfecto. Donde mayor es el "
            "trabajo, mucha es la ganancia.",

    # Capítulo 2
    (2, 1): "Si amas a los buenos discípulos, no tienes mérito; antes bien, "
            "somete con mansedumbre a los más dañinos. No toda herida se cura "
            "con el mismo emplasto. Calma los accesos de fiebre con fomentos.",
    (2, 2): "Sé prudente como la serpiente en todo, y sencillo siempre como "
            "la paloma. Por esto eres de carne y de espíritu, para que trates "
            "con blandura lo que se presenta a tu vista; y en cuanto a lo "
            "invisible, pide que te sea manifestado, para que no te falte "
            "nada y abundes en todo don. ³ El tiempo te reclama, como los "
            "pilotos los vientos y como el que es azotado por la tempestad el "
            "puerto, para alcanzar a Dios. Sé sobrio, como atleta de Dios; el "
            "premio es la incorrupción y la vida eterna, de la cual también "
            "tú estás persuadido. En todo soy rescate por ti, yo y mis "
            "cadenas, que tú amaste.",

    # Capítulo 3
    (3, 1): "Los que parecen dignos de crédito y enseñan doctrinas extrañas "
            "no te hagan temblar. Mantente firme como el yunque que es "
            "golpeado. Propio es de un gran atleta recibir golpes y vencer. Y "
            "sobre todo por causa de Dios debemos soportarlo todo, para que "
            "también él nos soporte a nosotros.",
    (3, 2): "Sé más diligente de lo que eres. Discierne los tiempos. Aguarda "
            "al que está por encima del tiempo, al intemporal, al invisible, "
            "que por nosotros se hizo visible; al impalpable, al impasible, "
            "que por nosotros se hizo pasible; al que de todas las maneras "
            "soportó por nosotros.",

    # Capítulo 4
    (4, 1): "Que las viudas no sean desatendidas; después del Señor, sé tú "
            "quien cuide de ellas. Nada se haga sin tu consentimiento, ni "
            "hagas tú nada sin Dios, como en efecto no lo haces. Mantente "
            "firme.",
    (4, 2): "Háganse las reuniones con más frecuencia; busca a todos por su "
            "nombre.",
    (4, 3): "No desprecies a los esclavos ni a las esclavas; pero que tampoco "
            "ellos se envanezcan, sino que sirvan más para la gloria de Dios, "
            "para que alcancen de Dios una libertad mejor. No deseen ser "
            "libertados a costa de la caja común, para que no sean hallados "
            "esclavos de la concupiscencia.",

    # Capítulo 5
    (5, 1): "Huye de las malas artes; antes bien, predica contra ellas. Di a "
            "mis hermanas que amen al Señor y se contenten con sus maridos en "
            "carne y en espíritu. Asimismo encarga a mis hermanos, en el "
            "nombre de Jesucristo, que amen a sus mujeres como el Señor a la "
            "iglesia.",
    (5, 2): "Si alguno puede permanecer en castidad para honra de la carne "
            "del Señor, permanezca en ella sin jactancia. Si se jacta, está "
            "perdido; y si se tiene por más que el obispo, se ha corrompido. "
            "Y conviene a los que se casan y a las que se casan contraer la "
            "unión con el consentimiento del obispo, para que el matrimonio "
            "sea según el Señor y no según la concupiscencia. Hágase todo "
            "para honra de Dios.",

    # Capítulo 6
    (6, 1): "Atended al obispo, para que también Dios os atienda a vosotros. "
            "Yo soy rescate por los que se someten al obispo, a los "
            "presbíteros, a los diáconos; y ojalá me toque tener parte con "
            "ellos en Dios. Trabajad juntos unos con otros, luchad juntos, "
            "corred juntos, padeced juntos, dormid juntos, levantaos juntos, "
            "como administradores de Dios, y asistentes, y servidores.",
    (6, 2): "Agradad a aquel en cuya milicia servís, de quien también recibís "
            "la soldada; que ninguno de vosotros sea hallado desertor. "
            "Permanezca vuestro bautismo como armas, la fe como yelmo, el "
            "amor como lanza, la paciencia como armadura completa. Vuestros "
            "depósitos sean vuestras obras, para que recibáis los haberes que "
            "os son debidos. Sed, pues, longánimes unos con otros en "
            "mansedumbre, como Dios lo es con vosotros. Ojalá goce yo de "
            "vosotros en todo tiempo.",

    # Capítulo 7
    (7, 1): "Puesto que la iglesia que está en Antioquía de Siria tiene paz, "
            "según se me ha manifestado, por vuestra oración, también yo he "
            "quedado más animado en la despreocupación que viene de Dios, si "
            "es que por el padecer alcanzo a Dios, para ser hallado discípulo "
            "en vuestra resurrección.",
    (7, 2): "Conviene, Policarpo, bienaventuradísimo en Dios, convocar un "
            "consejo dignísimo de Dios y elegir a mano alzada a alguno a "
            "quien tengáis por muy amado y diligente, que pueda ser llamado "
            "corredor de Dios; y tenerle por digno de ir a Siria, para que "
            "glorifique vuestro amor diligente para gloria de Dios.",
    (7, 3): "El cristiano no tiene potestad sobre sí mismo, sino que se "
            "dedica a Dios. Esta obra es de Dios y vuestra, cuando la llevéis "
            "a cabo. Porque confío en la gracia de que estáis prontos para la "
            "buena obra que corresponde a Dios. Conociendo vuestro celo por "
            "la verdad, os he exhortado con pocas letras.",

    # Capítulo 8
    (8, 1): "Puesto que no he podido escribir a todas las iglesias, por tener "
            "que zarpar de repente de Tróade a Neápolis, según lo manda la "
            "voluntad, tú escribirás a las iglesias de más adelante, como "
            "quien posee el sentir de Dios, para que también ellas hagan lo "
            "mismo: los que puedan, que envíen mensajeros a pie, y los demás, "
            "cartas por medio de los que tú envíes, para que seáis "
            "glorificados con una obra eterna, como tú eres digno.",
    (8, 2): "Saludo a todos por su nombre, y a la mujer de Epítropo con toda "
            "su casa y la de sus hijos. Saludo a Átalo, mi amado. Saludo al "
            "que ha de ser tenido por digno de ir a Siria. La gracia será con "
            "él en todo tiempo, y con Policarpo, que le envía.",
    (8, 3): "Os deseo que estéis bien en todo tiempo en nuestro Dios "
            "Jesucristo, en quien permanezcáis en la unidad de Dios y en su "
            "episcopado. Saludo a Alce, nombre que me es querido. Estad bien "
            "en el Señor.",
}
