"""Tobías en español, traducido del griego.

Para las Asambleas de Dios no es canon; se ofrece para estudio. Es una novela
doméstica del destierro, y lo que la hace valiosa no es la doctrina sino la
escena: un hombre que entierra muertos a escondidas y se queda ciego porque unos
pájaros le ensucian los ojos mientras duerme en el patio; su mujer que le echa
en cara sus limosnas; una muchacha en Ecbátana a la que se le han muerto siete
maridos y a la que las criadas insultan. Dos oraciones desesperadas, dichas el
mismo día a cientos de kilómetros, y un ángel enviado a las dos.

Aquí se sigue el texto griego breve, que es el que trae esta edición. Hay otro
más largo —el del Sinaítico— que cuenta lo mismo con más detalle; cuando los dos
difieren, lo que se lee aquí es lo que dice el texto que está al lado, no una
mezcla de los dos.

El nombre del padre se translitera Tobit y el del hijo Tobías, que es como los
distingue el griego (Τωβείτ / Τωβίας) y como hace falta para no perderse: el
libro los llama a los dos «Tobías» en algunas versiones y entonces no se sabe
quién habla.
"""

from __future__ import annotations

TOBIAS_ES: dict[tuple[int, int], str] = {
    # --- 1. Tobit cuenta su vida -------------------------------------------
    (1, 1): "Libro de las palabras de Tobit, hijo de Tobiel, hijo de Ananiel, "
            "hijo de Aduel, hijo de Gabael, del linaje de Asiel, de la tribu de "
            "Neftalí,",
    (1, 2): "el cual fue llevado cautivo en los días de Enemesar, rey de los "
            "asirios, desde Tisbe, que está a la derecha de Cidiós de Neftalí, "
            "en Galilea, más arriba de Aser.",
    (1, 3): "Yo, Tobit, anduve por caminos de verdad y de justicia todos los "
            "días de mi vida; e hice muchas obras de misericordia a mis hermanos "
            "y a mi pueblo, a los que fueron conmigo al país de los asirios, a "
            "Nínive.",
    (1, 4): "Y cuando estaba en mi tierra, en la tierra de Israel, siendo yo muy "
            "joven, toda la tribu de Neftalí, mi padre, se apartó de la casa de "
            "Jerusalén, la que había sido escogida de entre todas las tribus de "
            "Israel para que sacrificaran allí todas ellas; y fue consagrado el "
            "templo de la morada del Altísimo, y fue edificado para todas las "
            "generaciones del siglo.",
    (1, 5): "Y todas las tribus que se apartaron sacrificaban a Baal, la "
            "becerra; y también la casa de Neftalí, mi padre.",
    (1, 6): "Pero yo solo iba muchas veces a Jerusalén en las fiestas, conforme "
            "está escrito para todo Israel en precepto eterno, llevando las "
            "primicias y los diezmos de los frutos y las primeras esquilas;",
    (1, 7): "y se los daba a los sacerdotes, hijos de Aarón, para el altar. El "
            "diezmo lo daba a los hijos de Leví que servían en Jerusalén, y el "
            "segundo diezmo lo vendía, e iba y lo gastaba en Jerusalén cada año; "
            "y el tercero lo daba a quienes correspondía, según había mandado "
            "Débora, la madre de mi padre, porque quedé huérfano de padre.",
    (1, 9): "Y cuando llegué a ser hombre, tomé por mujer a Ana, del linaje de "
            "nuestra familia, y engendré de ella a Tobías.",
    (1, 10): "Y cuando fuimos llevados cautivos a Nínive, todos mis hermanos y "
             "los de mi linaje comían de los panes de los gentiles;",
    (1, 11): "pero yo me guardé de comer,",
    (1, 12): "porque me acordaba de Dios con toda mi alma.",
    (1, 13): "Y el Altísimo me dio gracia y buen aspecto delante de Enemesar, y "
             "yo era su comprador.",
    (1, 14): "Iba a Media, y dejé en depósito a Gabael, hermano de Gabrías, en "
             "Ragues de Media, diez talentos de plata.",
    (1, 15): "Y cuando murió Enemesar, reinó en su lugar Aquerel su hijo; y sus "
             "caminos se volvieron inseguros, y ya no pude ir a Media.",
    (1, 16): "Y en los días de Enemesar hacía muchas obras de misericordia a mis "
             "hermanos:",
    (1, 17): "daba mis panes a los hambrientos y vestidos a los desnudos; y si "
             "veía a alguno de mi linaje muerto y arrojado detrás de la muralla "
             "de Nínive, lo sepultaba.",
    (1, 18): "Y si el rey Aquerel mataba a alguno, cuando vino huyendo de Judea, "
             "yo los sepultaba a escondidas; porque mató a muchos en su furor. Y "
             "el rey buscó los cuerpos, y no fueron hallados.",
    (1, 19): "Y uno de los de Nínive fue y denunció al rey acerca de mí, que yo "
             "los sepultaba, y me escondí; y al saber que me buscaban para "
             "matarme, tuve miedo y huí.",
    (1, 20): "Y me saquearon todos mis bienes, y no me quedó nada, sino Ana mi "
             "mujer y Tobías mi hijo.",
    (1, 21): "Y no pasaron cincuenta días hasta que lo mataron sus dos hijos, y "
             "huyeron a los montes de Ararat; y reinó Saquerdón su hijo en su "
             "lugar, y puso a Ajícar, hijo de Anael, mi hermano, sobre toda la "
             "contaduría de su reino y sobre toda la administración.",
    (1, 22): "Y Ajícar intercedió por mí, y volví a Nínive. Y Ajícar era el "
             "copero y guardaba el anillo, y era administrador y contador; y "
             "Saquerdón lo puso en el segundo puesto. Y era sobrino mío.",

    # --- 2. El entierro, y la ceguera --------------------------------------
    (2, 1): "Y cuando volví a mi casa y me fueron devueltos Ana mi mujer y "
            "Tobías mi hijo, en la fiesta de Pentecostés, que es la fiesta santa "
            "de las siete semanas, me prepararon una buena comida, y me recosté "
            "para comer.",
    (2, 2): "Y vi muchos manjares, y dije a mi hijo: «Ve y trae al que halles "
            "necesitado de nuestros hermanos, que se acuerde del Señor; y he "
            "aquí que te espero».",
    (2, 3): "Y él volvió y dijo: «Padre, uno de nuestro linaje está "
            "estrangulado, arrojado en la plaza».",
    (2, 4): "Y yo, antes de probar bocado, me levanté de un salto y lo recogí en "
            "una habitación hasta que se puso el sol.",
    (2, 5): "Y volviendo, me lavé, y comía mi pan con tristeza;",
    (2, 6): "y me acordé de la profecía de Amós, cuando dijo: «Vuestras fiestas "
            "se volverán duelo, y todas vuestras alegrías, llanto».",
    (2, 7): "Y lloré. Y cuando se puso el sol, fui y, cavando, lo sepulté.",
    (2, 8): "Y los vecinos se burlaban, diciendo: «Ya no teme que lo maten por "
            "este asunto; y aunque huyó, he aquí que otra vez sepulta a los "
            "muertos».",
    (2, 9): "Y aquella misma noche volví de sepultarlo, y me acosté contaminado "
            "junto a la pared del patio, con el rostro descubierto.",
    (2, 10): "Y no sabía que había pájaros en la pared; y estando abiertos mis "
             "ojos, los pájaros dejaron caer su excremento caliente en mis ojos, "
             "y me salieron manchas blancas en los ojos. Y fui a los médicos, y "
             "no me aprovecharon; y Ajícar me sustentó hasta que se fue a "
             "Elimaida.",
    (2, 11): "Y mi mujer Ana trabajaba a jornal en labores de mujeres;",
    (2, 12): "y enviaba el trabajo a sus dueños, y ellos le pagaban su jornal, y "
             "le dieron además un cabrito.",
    (2, 13): "Y cuando vino a mí, el cabrito empezó a balar; y le dije: «¿De "
             "dónde es el cabrito? ¿No será robado? Devuélveselo a sus dueños, "
             "porque no es lícito comer cosa robada».",
    (2, 14): "Y ella dijo: «Regalo me ha sido dado, además del jornal». Y yo no "
             "le creía, y le decía que lo devolviera a sus dueños, y me "
             "sonrojaba ante ella. Y ella me respondió y me dijo: «¿Dónde están "
             "tus obras de misericordia y tus justicias? He aquí que todo se ve "
             "en ti».",

    # --- 3. Las dos oraciones, el mismo día --------------------------------
    (3, 1): "Y afligido, lloré, y oré con dolor, diciendo:",
    (3, 2): "«Justo eres, Señor, y todas tus obras y todos tus caminos son "
            "misericordia y verdad; y tú juzgas juicio verdadero y justo para "
            "siempre.",
    (3, 3): "Acuérdate de mí y mírame; no tomes venganza por mis pecados ni por "
            "mis ignorancias ni por las de mis padres, con que pecaron delante "
            "de ti.",
    (3, 4): "Porque desobedecieron tus mandamientos; nos entregaste al saqueo y "
            "al cautiverio y a la muerte, y a ser proverbio de oprobio para "
            "todas las naciones entre las que fuimos esparcidos.",
    (3, 5): "Y ahora, muchos son tus juicios, y verdaderos, para hacer conmigo "
            "conforme a mis pecados y a los de mis padres; porque no cumplimos "
            "tus mandamientos, ni anduvimos en verdad delante de ti.",
    (3, 6): "Y ahora, haz conmigo según te agrade: manda que se recoja mi "
            "espíritu, para que sea liberado y me vuelva tierra; porque más me "
            "vale morir que vivir, pues he oído oprobios falsos y hay mucha "
            "tristeza en mí. Manda que sea liberado de esta angustia y llevado "
            "al lugar eterno; no apartes tu rostro de mí».",
    (3, 7): "En aquel mismo día sucedió que a Sara, hija de Raguel, en Ecbátana "
            "de Media, también la afrentaban las criadas de su padre;",
    (3, 8): "porque había sido dada a siete maridos, y Asmodeo, el demonio malo, "
            "los había matado antes de que se unieran a ella como se hace con "
            "las mujeres. Y le decían: «¿No te das cuenta de que estrangulas a "
            "tus maridos? Ya has tenido siete, y de ninguno de ellos has sacado "
            "provecho.",
    (3, 9): "¿Por qué nos azotas? Si murieron, vete con ellos; que no veamos "
            "jamás hijo ni hija tuyos».",
    (3, 10): "Al oír esto se afligió tanto que quiso ahorcarse; y dijo: «Hija "
             "única soy de mi padre; si hago esto, será oprobio para él, y haré "
             "bajar su vejez con dolor al Hades».",
    (3, 11): "Y oró junto a la ventana y dijo: «Bendito eres, Señor Dios mío, y "
             "bendito tu nombre santo y honorable por los siglos; bendígante "
             "todas tus obras para siempre.",
    (3, 12): "Y ahora, Señor, a ti he dirigido mis ojos y mi rostro.",
    (3, 13): "Manda que sea liberada de la tierra, y que no oiga más oprobio.",
    (3, 14): "Tú sabes, Señor, que estoy limpia de todo pecado con varón,",
    (3, 15): "y que no he manchado mi nombre ni el nombre de mi padre en la "
             "tierra de mi cautiverio. Hija única soy de mi padre, y no tiene "
             "otro hijo que lo herede, ni hermano cercano, ni le queda hijo "
             "alguno para que yo me guarde para él como mujer. Ya se me han "
             "muerto siete; ¿para qué vivir? Y si no te parece bien matarme, "
             "manda que se ponga en mí tu mirada y se tenga de mí misericordia, "
             "y que no oiga más oprobio».",
    (3, 16): "Y fue escuchada la oración de ambos delante de la gloria del "
             "Grande; y Rafael",
    (3, 17): "fue enviado a sanar a los dos: a Tobit, a quitarle las manchas "
             "blancas de los ojos; y a Sara, la de Raguel, a darla por mujer a "
             "Tobías, hijo de Tobit, y a atar a Asmodeo, el demonio malo, porque "
             "a Tobías le corresponde heredarla. En aquel mismo momento Tobit, "
             "volviéndose, entró en su casa, y Sara, la de Raguel, bajó de su "
             "aposento alto.",
    # --- 4. Los consejos del padre al hijo ---------------------------------
    (4, 1): "En aquel día se acordó Tobit de la plata que había dejado en "
            "depósito a Gabael en Ragues de Media.",
    (4, 2): "Y se dijo a sí mismo: «Yo he pedido la muerte; ¿por qué no llamo a "
            "Tobías mi hijo para enseñárselo antes de morir?».",
    (4, 3): "Y llamándolo, le dijo: «Hijo, si muero, sepúltame; y no descuides a "
            "tu madre: hónrala todos los días de tu vida, y haz lo que le agrade "
            "y no la aflijas.",
    (4, 4): "Acuérdate, hijo, de que pasó muchos peligros por ti cuando te "
            "llevaba en el vientre; cuando muera, sepúltala junto a mí, en una "
            "misma tumba.",
    (4, 5): "Todos los días, hijo, acuérdate del Señor nuestro Dios; no quieras "
            "traspasar sus mandamientos. Haz justicia todos los días de tu vida, "
            "y no andes por los caminos de la injusticia;",
    (4, 6): "porque, si obras la verdad, habrá prosperidad en tus obras, y en "
            "las de todos los que hacen justicia.",
    (4, 7): "De lo que tengas, haz misericordia; y no sea mezquino tu ojo cuando "
            "hagas misericordia. No apartes tu rostro de ningún pobre, y no se "
            "apartará de ti el rostro de Dios.",
    (4, 8): "Conforme a lo mucho que tengas, haz de ello misericordia; si tienes "
            "poco, conforme a lo poco, no temas hacer misericordia.",
    (4, 9): "Porque así atesoras para ti un buen depósito para el día de la "
            "necesidad;",
    (4, 10): "porque la misericordia libra de la muerte, y no deja ir a las "
             "tinieblas.",
    (4, 11): "Porque la misericordia es un buen regalo delante del Altísimo para "
             "todos los que la hacen.",
    (4, 12): "Guárdate, hijo, de toda fornicación; y toma mujer, ante todo, del "
             "linaje de tus padres. No tomes mujer extraña, que no sea de la "
             "tribu de tu padre, porque somos hijos de profetas. Noé, Abraham, "
             "Isaac, Jacob, nuestros padres desde el principio: acuérdate, hijo, "
             "de que todos ellos tomaron mujeres de entre sus hermanos, y fueron "
             "bendecidos en sus hijos, y su descendencia heredará la tierra.",
    (4, 13): "Y ahora, hijo, ama a tus hermanos, y no te ensoberbezcas en tu "
             "corazón contra tus hermanos y contra los hijos y las hijas de tu "
             "pueblo, hasta el punto de no tomar de entre ellos mujer. Porque en "
             "la soberbia hay perdición y mucha inquietud, y en la holgazanería, "
             "menoscabo y gran necesidad; que la holgazanería es la madre del "
             "hambre.",
    (4, 14): "El jornal de todo hombre que trabaje para ti no se quede contigo "
             "de un día para otro, sino págaselo al momento; si sirves a Dios, "
             "se te pagará. Guárdate, hijo, en todas tus obras, y sé bien criado "
             "en toda tu conducta.",
    (4, 15): "Y lo que aborreces, no se lo hagas a nadie. No bebas vino hasta "
             "embriagarte, y no vaya la embriaguez contigo por tu camino.",
    (4, 16): "De tu pan da al hambriento, y de tus vestidos a los desnudos; de "
             "todo lo que te sobre haz misericordia, y no sea mezquino tu ojo "
             "cuando hagas misericordia.",
    (4, 17): "Derrama tus panes sobre la tumba de los justos, y no los des a los "
             "pecadores.",
    (4, 18): "Busca consejo de todo hombre prudente, y no desprecies ningún "
             "consejo provechoso.",
    (4, 19): "Y en todo tiempo bendice al Señor tu Dios, y pídele que tus "
             "caminos se enderecen y que todas tus sendas y designios prosperen. "
             "Porque ninguna nación tiene consejo por sí misma, sino que el "
             "Señor mismo da todos los bienes, y a quien quiere lo humilla como "
             "le place. Y ahora, hijo, acuérdate de mis mandamientos, y no se "
             "borren de tu corazón.",
    (4, 20): "Y ahora te hago saber lo de los diez talentos de plata que dejé en "
             "depósito a Gabael, el de Gabrías, en Ragues de Media.",
    (4, 21): "Y no temas, hijo, porque hayamos empobrecido: mucho tienes, si "
             "temes a Dios y te apartas de todo pecado y haces lo que le agrada».",

    # --- 5. El compañero de viaje ------------------------------------------
    (5, 1): "Y respondiendo Tobías, le dijo: «Padre, haré todo cuanto me has "
            "mandado.",
    (5, 2): "Pero ¿cómo podré recoger la plata, si no lo conozco?».",
    (5, 3): "Y le dio el recibo, y le dijo: «Búscate un hombre que vaya contigo, "
            "y le daré su jornal mientras yo viva; y ve y recoge la plata».",
    (5, 4): "Y fue a buscar un hombre, y encontró a Rafael, que era un ángel, y "
            "él no lo sabía;",
    (5, 5): "y le dijo: «¿Podrías ir conmigo a Ragues de Media? ¿Conoces bien "
            "esos lugares?».",
    (5, 6): "Y le dijo el ángel: «Iré contigo, y conozco el camino, y me he "
            "alojado en casa de Gabael, nuestro hermano».",
    (5, 7): "Y le dijo Tobías: «Espérame, y se lo diré a mi padre».",
    (5, 8): "Y él le dijo: «Ve, y no tardes».",
    (5, 9): "Y entrando, dijo a su padre: «He aquí que he encontrado quien vaya "
            "conmigo». Y él dijo: «Llámalo a mí, para que sepa de qué tribu es y "
            "si es de fiar para ir contigo».",
    (5, 10): "Y lo llamó; y entró, y se saludaron el uno al otro.",
    (5, 11): "Y le dijo Tobit: «Hermano, ¿de qué tribu y de qué familia eres? "
             "Dímelo».",
    (5, 12): "Y él le dijo: «¿Buscas tribu y familia, o un jornalero que vaya "
             "con tu hijo?». Y le dijo Tobit: «Quiero, hermano, conocer tu "
             "linaje y tu nombre».",
    (5, 13): "Y él dijo: «Yo soy Azarías, hijo de Ananías el grande, de tus "
             "hermanos».",
    (5, 14): "Y le dijo: «Bienvenido seas, hermano; y no te enojes conmigo "
             "porque quise conocer tu tribu y tu familia. Y resulta que eres "
             "hermano mío, de generación buena y honrada; porque yo conocía a "
             "Ananías y a Jatán, los hijos de Semeo el grande, cuando íbamos "
             "juntos a Jerusalén a adorar, llevando los primogénitos y los "
             "diezmos de los frutos, y no se extraviaron en el extravío de "
             "nuestros hermanos. De buena raíz eres, hermano.",
    (5, 15): "Pero dime: ¿qué jornal te he de dar? ¿Una dracma al día y lo que "
             "necesites, como a mi hijo?",
    (5, 16): "Y aún te añadiré al jornal, si volvéis sanos».",
    (5, 17): "Y así lo acordaron. Y dijo a Tobías: «Prepárate para el camino, y "
             "que tengáis buen viaje». Y su hijo preparó lo necesario para el "
             "camino; y le dijo su padre: «Ve con este hombre; y el Dios que "
             "habita en el cielo enderece vuestro camino, y su ángel os "
             "acompañe». Y salieron los dos para partir, y el perro del muchacho "
             "con ellos.",
    (5, 18): "Y lloró Ana su madre, y dijo a Tobit: «¿Por qué has enviado a "
             "nuestro hijo? ¿No es él el báculo de nuestra mano, cuando entra y "
             "sale delante de nosotros?",
    (5, 19): "Que no vaya plata tras plata; sea todo ello escoria comparado con "
             "nuestro hijo.",
    (5, 20): "Porque lo que se nos ha dado para vivir de parte del Señor, eso "
             "nos basta».",
    (5, 21): "Y le dijo Tobit: «No te apures, hermana; sano volverá, y tus ojos "
             "lo verán.",
    (5, 22): "Porque un buen ángel irá con él, y su camino prosperará, y volverá "
             "sano».",

    # --- 6. El pez del Tigris ----------------------------------------------
    (6, 1): "Y ella dejó de llorar.",
    (6, 2): "Y los que iban de camino llegaron al atardecer al río Tigris, y "
            "pasaron allí la noche.",
    (6, 3): "Y el muchacho bajó a lavarse, y saltó un pez del río y quiso "
            "tragarse al muchacho.",
    (6, 4): "Y el ángel le dijo: «Agarra el pez». Y el muchacho sujetó el pez y "
            "lo echó a tierra.",
    (6, 5): "Y le dijo el ángel: «Abre el pez, y toma el corazón y el hígado y "
            "la hiel, y guárdalos bien».",
    (6, 6): "Y el muchacho hizo como le dijo el ángel; y asaron el pez y "
            "comieron. Y los dos caminaron hasta acercarse a Ecbátana.",
    (6, 7): "Y dijo el muchacho al ángel: «Azarías, hermano, ¿para qué sirven el "
            "hígado y el corazón y la hiel del pez?».",
    (6, 8): "Y él le dijo: «El corazón y el hígado, si a alguien lo atormenta un "
            "demonio o un espíritu malo, se queman delante del hombre o de la "
            "mujer, y ya no será atormentado.",
    (6, 9): "Y con la hiel se unta al hombre que tiene manchas blancas en los "
            "ojos, y sanará».",
    (6, 10): "Y cuando se acercaron a Ragues,",
    (6, 11): "dijo el ángel al muchacho: «Hermano, hoy nos alojaremos en casa de "
             "Raguel; y él es pariente tuyo, y tiene una hija de nombre Sara.",
    (6, 12): "Hablaré de ella para que te la den por mujer, porque a ti te "
             "corresponde su herencia, y tú eres el único de su linaje; y la "
             "muchacha es hermosa y prudente.",
    (6, 13): "Y ahora escúchame: hablaré a su padre y, cuando volvamos de "
             "Ragues, celebraremos la boda. Porque sé de Raguel que no la dará a "
             "otro hombre, conforme a la ley de Moisés, o se hará reo de muerte, "
             "porque a ti te toca recibir la herencia antes que a ningún otro».",
    (6, 14): "Entonces dijo el muchacho al ángel: «Azarías, hermano, he oído que "
             "la muchacha ha sido dada a siete maridos, y que todos murieron en "
             "la alcoba nupcial.",
    (6, 15): "Y ahora yo soy hijo único de mi padre, y temo entrar y morir como "
             "los anteriores, porque a ella la ama un demonio que no hace daño a "
             "nadie sino a los que se le acercan. Y ahora temo morir y hacer "
             "bajar con dolor la vida de mi padre y de mi madre a su sepultura "
             "por causa mía; y no tienen otro hijo que los sepulte».",
    (6, 16): "Y le dijo el ángel: «¿No te acuerdas de las palabras que te mandó "
             "tu padre, que tomaras mujer de tu linaje? Pues ahora escúchame, "
             "hermano: ella será tu mujer, y del demonio no hagas caso, porque "
             "esta misma noche te será dada por mujer.",
    (6, 17): "Y cuando entres en la alcoba, tomarás ceniza de incienso y pondrás "
             "encima algo del corazón y del hígado del pez, y lo quemarás;",
    (6, 18): "y el demonio lo olerá y huirá, y no volverá jamás. Y cuando te "
             "acerques a ella, levantaos los dos y clamad al Dios misericordioso, "
             "y os salvará y tendrá misericordia. No temas, porque ella te "
             "estaba destinada desde siempre, y tú la salvarás, e irá contigo; y "
             "supongo que tendrás de ella hijos». Y cuando Tobías oyó esto, la "
             "amó, y su alma se unió a ella profundamente.",
    # --- 7. En casa de Raguel ----------------------------------------------
    (7, 1): "Y llegó a Ecbátana y entró en la casa de Raguel, y Sara le salió al "
            "encuentro; y ella lo saludó, y él a ellos. Y los hizo entrar en la "
            "casa.",
    (7, 2): "Y dijo a Edna su mujer: «¡Qué parecido es este joven a Tobit, mi "
            "primo!».",
    (7, 3): "Y Raguel les preguntó: «¿De dónde sois, hermanos?». Y ellos le "
            "dijeron: «De los hijos de Neftalí, de los cautivos de Nínive».",
    (7, 4): "Y les dijo: «¿Conocéis a Tobit, nuestro hermano?».",
    (7, 5): "Y ellos dijeron: «Vive y está bien». Y dijo Tobías: «Es mi padre».",
    (7, 6): "Y Raguel se levantó de un salto, y lo besó y lloró;",
    (7, 7): "y lo bendijo y le dijo: «¡Hijo del hombre honrado y bueno!». Y al "
            "oír que Tobit había perdido los ojos, se entristeció y lloró.",
    (7, 8): "Y Edna su mujer y Sara su hija lloraron; y los recibieron de buena "
            "gana.",
    (7, 9): "Y degollaron un carnero del rebaño y sirvieron muchos manjares. Y "
            "dijo Tobías a Rafael: «Azarías, hermano, habla de aquello que "
            "decías en el camino, y que se cumpla el asunto».",
    (7, 10): "Y él transmitió la palabra a Raguel. Y dijo Raguel a Tobías: "
             "«Come, bebe y alégrate, porque a ti te toca tomar a mi hija; pero "
             "te diré la verdad.",
    (7, 11): "He dado a mi hija a siete maridos, y cada vez que entraban a ella "
             "morían aquella noche. Pero por ahora alégrate». Y dijo Tobías: «No "
             "probaré nada aquí hasta que os comprometáis conmigo». Y dijo "
             "Raguel: «Tómala desde ahora, conforme a la sentencia; tú eres su "
             "hermano y ella es tuya. Y el Dios misericordioso os conceda lo "
             "mejor».",
    (7, 12): "Y llamó a Sara su hija y, tomándola de la mano, la entregó a "
             "Tobías por mujer, y dijo: «He aquí que, conforme a la ley de "
             "Moisés, tómala y llévala a tu padre». Y los bendijo.",
    (7, 13): "Y llamó a Edna su mujer; y tomando un libro, escribió el contrato, "
             "y lo sellaron.",
    (7, 14): "Y comenzaron a comer.",
    (7, 15): "Y llamó Raguel a Edna su mujer y le dijo: «Hermana, prepara la "
             "otra habitación y llévala allí».",
    (7, 16): "Y ella hizo como dijo, y la llevó allí, y lloró; y recogió las "
             "lágrimas de su hija, y le dijo:",
    (7, 17): "«Ten ánimo, hija; el Señor del cielo y de la tierra te dé gozo en "
             "lugar de esta tu tristeza. Ten ánimo, hija».",

    # --- 8. La noche de bodas y la oración ---------------------------------
    (8, 1): "Y cuando acabaron de cenar, llevaron a Tobías a ella.",
    (8, 2): "Y al ir, se acordó de las palabras de Rafael, y tomó la ceniza del "
            "incienso y puso encima el corazón del pez y el hígado, y lo quemó.",
    (8, 3): "Y cuando el demonio olió el humo, huyó a lo más alto de Egipto, y "
            "el ángel lo ató.",
    (8, 4): "Y cuando los dos quedaron encerrados, se levantó Tobías de la cama "
            "y dijo: «Levántate, hermana, y oremos para que el Señor tenga "
            "misericordia de nosotros».",
    (8, 5): "Y comenzó Tobías a decir: «Bendito eres, Dios de nuestros padres, y "
            "bendito tu nombre santo y glorioso por los siglos; bendígante los "
            "cielos y todas tus criaturas.",
    (8, 6): "Tú hiciste a Adán y le diste por ayuda y apoyo a Eva su mujer; de "
            "ellos nació la simiente de los hombres. Tú dijiste: No es bueno que "
            "el hombre esté solo; hagámosle una ayuda semejante a él.",
    (8, 7): "Y ahora, Señor, no por lujuria tomo yo a esta hermana mía, sino de "
            "verdad; manda que se tenga misericordia de mí, y que con ella "
            "llegue a viejo».",
    (8, 8): "Y ella dijo con él: «Amén».",
    (8, 9): "Y durmieron los dos aquella noche. Y levantándose Raguel, fue y "
            "cavó una fosa,",
    (8, 10): "diciendo: «No sea que también éste muera».",
    (8, 11): "Y volvió Raguel a su casa,",
    (8, 12): "y dijo a Edna su mujer: «Envía a una de las criadas y vean si "
             "vive; y si no, para que lo sepultemos sin que nadie lo sepa».",
    (8, 13): "Y entró la criada, abriendo la puerta, y encontró a los dos "
             "durmiendo.",
    (8, 14): "Y saliendo, les anunció que vivía.",
    (8, 15): "Y bendijo Raguel a Dios, diciendo: «Bendito eres tú, oh Dios, con "
             "toda bendición; y bendígante tus santos y todas tus criaturas; "
             "todos tus ángeles y tus escogidos te bendigan por los siglos.",
    (8, 16): "Bendito eres porque me has alegrado, y no me ha sucedido lo que "
             "sospechaba, sino que conforme a tu mucha misericordia has obrado "
             "con nosotros.",
    (8, 17): "Bendito eres porque tuviste misericordia de dos hijos únicos; "
             "hazles, Soberano, misericordia; cumple su vida en salud, con "
             "alegría y misericordia».",
    (8, 18): "Y mandó a los criados que cegaran la fosa.",
    (8, 19): "Y les hizo boda de catorce días.",
    (8, 20): "Y le dijo Raguel, antes de que se cumplieran los días de la boda, "
             "bajo juramento, que no saliera hasta que se cumplieran los catorce "
             "días de la boda,",
    (8, 21): "y que entonces, tomando la mitad de sus bienes, se fuera con salud "
             "a su padre; y el resto, cuando muriera él y su mujer.",

    # --- 9. Rafael va por la plata -----------------------------------------
    (9, 1): "Y llamó Tobías a Rafael y le dijo:",
    (9, 2): "«Azarías, hermano, toma contigo un criado y dos camellos, y ve a "
            "Ragues de Media, a casa de Gabael, y tráeme la plata, y tráelo a él "
            "a la boda.",
    (9, 3): "Porque Raguel ha jurado que yo no salga;",
    (9, 4): "y mi padre cuenta los días, y si me retraso mucho, se afligirá en "
            "gran manera».",
    (9, 5): "Y fue Rafael, y se alojó en casa de Gabael, y le dio el recibo; y "
            "él sacó las bolsas con sus sellos y se las dio.",
    (9, 6): "Y madrugaron juntos y llegaron a la boda; y bendijo Tobías a su "
            "mujer.",

    # --- 10. La espera de los padres ---------------------------------------
    (10, 1): "Y Tobit su padre iba contando cada día; y cuando se cumplieron los "
             "días del viaje y no llegaba,",
    (10, 2): "dijo: «¿Los habrán avergonzado? ¿O habrá muerto Gabael, y no hay "
             "quien le dé la plata?».",
    (10, 3): "Y se afligía mucho.",
    (10, 4): "Y le dijo su mujer: «Se ha perdido el muchacho, porque se ha "
             "retrasado». Y empezó a llorarlo y dijo:",
    (10, 5): "«¿Qué me importa ya nada, hijo, después de haberte dejado ir, luz "
             "de mis ojos?».",
    (10, 6): "Y Tobit le decía: «Calla, no te apures; está bien».",
    (10, 7): "Y ella le decía: «Calla, no me engañes; se ha perdido mi hijo». Y "
             "salía cada día al camino por donde se había ido, y de día no comía "
             "pan, y de noche no dejaba de llorar por Tobías su hijo, hasta que "
             "se cumplieron los catorce días de la boda que Raguel había jurado "
             "que pasara allí. Y dijo Tobías a Raguel: «Despídeme, porque mi "
             "padre y mi madre ya no esperan verme».",
    (10, 8): "Y le dijo su suegro: «Quédate conmigo, y yo enviaré a tu padre "
             "quien le cuente cómo estás».",
    (10, 9): "Y Tobías dijo: «Despídeme a casa de mi padre».",
    (10, 10): "Y levantándose Raguel, le dio a Sara su mujer y la mitad de sus "
              "bienes: siervos y ganado y plata;",
    (10, 11): "y bendiciéndolos, los despidió, diciendo: «El Dios del cielo os "
              "prospere, hijos, antes de que yo muera».",
    (10, 12): "Y dijo a su hija: «Honra a tus suegros; ellos son ahora tus "
              "padres. Que yo oiga buena fama de ti». Y la besó. Y Edna dijo a "
              "Tobías: «Hermano amado, el Señor del cielo te devuelva, y me "
              "conceda ver hijos tuyos de Sara mi hija, para que me alegre "
              "delante del Señor. Y he aquí que te confío mi hija en depósito: "
              "no la aflijas».",

    # --- 11. La vuelta, y los ojos abiertos --------------------------------
    (11, 1): "Después de esto se puso en camino Tobías, bendiciendo a Dios "
             "porque había hecho próspero su camino, y bendecía a Raguel y a "
             "Edna su mujer; y caminó hasta acercarse a Nínive.",
    (11, 2): "Y dijo Rafael a Tobías: «¿No sabes, hermano, cómo dejaste a tu "
             "padre?",
    (11, 3): "Adelantémonos a tu mujer y preparemos la casa;",
    (11, 4): "y lleva a mano la hiel del pez». Y fueron, y el perro iba detrás "
             "de ellos.",
    (11, 5): "Y Ana estaba sentada mirando al camino por donde había de venir su "
             "hijo,",
    (11, 6): "y lo vio venir; y dijo a su padre: «He aquí que viene mi hijo, y "
             "el hombre que fue con él».",
    (11, 7): "Y Rafael dijo: «Yo sé que tu padre abrirá los ojos.",
    (11, 8): "Úntale la hiel en los ojos, y le escocerá y se los frotará, y se "
             "le caerán las manchas blancas, y te verá».",
    (11, 9): "Y corriendo Ana, se echó al cuello de su hijo y le dijo: «Te he "
             "visto, hijo; desde ahora puedo morir». Y lloraron los dos.",
    (11, 10): "Y Tobit salía hacia la puerta y tropezaba; pero su hijo corrió "
              "hacia él,",
    (11, 11): "y sostuvo a su padre, y le roció la hiel sobre los ojos, "
              "diciendo: «Ten ánimo, padre».",
    (11, 12): "Y cuando le escoció, se frotó los ojos,",
    (11, 13): "y se le desprendieron de los lagrimales las manchas blancas. Y al "
              "ver a su hijo, se echó sobre su cuello,",
    (11, 14): "y lloró y dijo: «Bendito eres, oh Dios, y bendito tu nombre por "
              "los siglos, y benditos todos tus santos ángeles;",
    (11, 15): "porque me azotaste y tuviste misericordia de mí: he aquí que veo "
              "a Tobías mi hijo». Y entró su hijo gozoso, y contó a su padre las "
              "maravillas que le habían sucedido en Media.",
    (11, 16): "Y salió Tobit al encuentro de su nuera, gozoso y bendiciendo a "
              "Dios, hasta la puerta de Nínive. Y se admiraban los que lo veían "
              "caminar, porque veía;",
    (11, 17): "y Tobit confesaba delante de ellos que Dios había tenido "
              "misericordia de ellos. Y cuando Tobit se acercó a Sara su nuera, "
              "la bendijo diciendo: «Bienvenida seas, hija; bendito sea Dios, "
              "que te ha traído a nosotros, y benditos tu padre y tu madre». Y "
              "hubo alegría entre todos sus hermanos en Nínive.",
    (11, 18): "Y vinieron Ajícar y Nasbas su sobrino,",
    (11, 19): "y se celebró la boda de Tobías con alegría durante siete días.",

    # --- 12. Rafael se da a conocer ----------------------------------------
    (12, 1): "Y llamó Tobit a Tobías su hijo y le dijo: «Mira, hijo, el jornal "
             "para el hombre que fue contigo; y hay que añadirle algo».",
    (12, 2): "Y él dijo: «Padre, no salgo perdiendo si le doy la mitad de lo que "
             "he traído,",
    (12, 3): "porque me ha traído a ti sano, y curó a mi mujer, y trajo mi "
             "plata, y a ti igualmente te curó».",
    (12, 4): "Y dijo el anciano: «Le corresponde».",
    (12, 5): "Y llamó al ángel y le dijo: «Toma la mitad de todo lo que habéis "
             "traído».",
    (12, 6): "Y llamándolos a los dos aparte, les dijo: «Bendecid a Dios y "
             "confesadle, dadle grandeza, y confesadle delante de todos los "
             "vivientes por lo que ha hecho con vosotros. Bueno es bendecir a "
             "Dios y ensalzar su nombre, dando a conocer con honra las palabras "
             "de las obras de Dios; y no os canséis de confesarle.",
    (12, 7): "Bueno es guardar el secreto del rey, pero las obras de Dios hay "
             "que descubrirlas con gloria. Haced el bien, y el mal no os "
             "alcanzará.",
    (12, 8): "Buena es la oración con ayuno y con misericordia y con justicia; "
             "mejor es lo poco con justicia que lo mucho con injusticia; mejor "
             "es hacer misericordia que atesorar oro.",
    (12, 9): "La misericordia libra de la muerte, y ella limpia todo pecado; los "
             "que hacen misericordia y justicia se hartarán de vida;",
    (12, 10): "pero los que pecan son enemigos de su propia vida.",
    (12, 11): "No os ocultaré ninguna palabra: ya he dicho que el secreto del "
              "rey es bueno guardarlo, pero las obras de Dios hay que "
              "descubrirlas con gloria.",
    (12, 12): "Y ahora: cuando orabais tú y tu nuera Sara, yo presentaba el "
              "memorial de vuestra oración delante del Santo; y cuando "
              "sepultabas a los muertos, igualmente estaba yo contigo;",
    (12, 13): "y cuando no te dio pereza levantarte y dejar tu comida para ir a "
              "amortajar al muerto, no se me escapó que hacías el bien, sino que "
              "estaba yo contigo.",
    (12, 14): "Y ahora Dios me ha enviado a sanarte a ti y a Sara tu nuera.",
    (12, 15): "Yo soy Rafael, uno de los siete santos ángeles que presentan las "
              "oraciones de los santos y entran delante de la gloria del Santo».",
    (12, 16): "Y se turbaron los dos y cayeron sobre su rostro, porque tuvieron "
              "miedo.",
    (12, 17): "Y él les dijo: «No temáis; paz sea con vosotros. Y bendecid a "
              "Dios por siempre,",
    (12, 18): "porque no ha sido por gracia mía, sino por la voluntad de vuestro "
              "Dios; por eso bendecidlo por siempre.",
    (12, 19): "Todos estos días me habéis visto, y no comí ni bebí, sino que "
              "estabais viendo una visión.",
    (12, 20): "Y ahora confesad a Dios, porque yo subo al que me envió; y "
              "escribid en un libro todo lo que ha sucedido».",
    (12, 21): "Y se levantaron, y ya no lo vieron.",
    (12, 22): "Y confesaban sus obras grandes y admirables, y cómo se les había "
              "aparecido un ángel del Señor.",

    # --- 13. El cántico de Tobit -------------------------------------------
    (13, 1): "Y Tobit escribió una oración de alegría, y dijo: «Bendito sea Dios "
             "que vive por los siglos, y su reino;",
    (13, 2): "porque él azota y tiene misericordia, hace bajar al Hades y hace "
             "subir, y no hay quien escape de su mano.",
    (13, 3): "Confesadle, hijos de Israel, delante de las naciones, porque él "
             "nos dispersó entre ellas.",
    (13, 4): "Allí mostrad su grandeza, ensalzadlo delante de todo viviente; "
             "porque él es nuestro Señor, y él es Dios, Padre nuestro por todos "
             "los siglos.",
    (13, 5): "Y nos azotará por nuestras injusticias, y de nuevo tendrá "
             "misericordia y nos reunirá de entre todas las naciones donde "
             "hayáis sido esparcidos.",
    (13, 6): "Si os volvéis a él de todo vuestro corazón y de toda vuestra alma, "
             "para obrar la verdad delante de él, entonces él se volverá a "
             "vosotros y no os esconderá su rostro. Y ved lo que hará con "
             "vosotros, y confesadle con todo vuestro ser; y bendecid al Señor "
             "de la justicia, y ensalzad al Rey de los siglos. Yo, en la tierra "
             "de mi cautiverio, le confieso, y muestro su fuerza y su grandeza a "
             "una nación de pecadores. Volveos, pecadores, y obrad justicia "
             "delante de él: ¿quién sabe si querrá recibiros y os hará "
             "misericordia?",
    (13, 7): "Yo ensalzo a mi Dios, y mi alma al Rey del cielo, y se alegrará en "
             "su grandeza.",
    (13, 8): "Díganlo todos y confiésenle en Jerusalén.",
    (13, 9): "Jerusalén, ciudad del Santo: él azotará por las obras de tus "
             "hijos, y de nuevo tendrá misericordia de los hijos de los justos.",
    (13, 10): "Confiesa al Señor como es debido, y bendice al Rey de los siglos, "
              "para que de nuevo su tienda te sea edificada con gozo, y para que "
              "alegre en ti a los cautivos y ame en ti a los desdichados por "
              "todas las generaciones del siglo.",
    (13, 11): "Muchas naciones vendrán de lejos al nombre del Señor Dios, "
              "trayendo dones en las manos, dones para el Rey del cielo; "
              "generaciones de generaciones te darán alegría.",
    (13, 12): "Malditos todos los que te aborrecen; benditos serán para siempre "
              "todos los que te aman.",
    (13, 13): "Gózate y alégrate por los hijos de los justos, porque serán "
              "reunidos y bendecirán al Señor de los justos.",
    (13, 14): "¡Oh bienaventurados los que te aman! Se gozarán en tu paz. "
              "Bienaventurados cuantos se afligieron por tus azotes, porque en "
              "ti se gozarán al contemplar toda tu gloria; y mi alma se alegrará "
              "para siempre.",
    (13, 15): "Bendice a Dios, el Rey grande.",
    (13, 16): "Porque Jerusalén será edificada de nuevo con zafiro y esmeralda, "
              "y tus muros con piedra preciosa, y las torres y los baluartes con "
              "oro puro;",
    (13, 17): "y las plazas de Jerusalén serán enlosadas con berilo y con "
              "carbunclo y con piedra de Sufir.",
    (13, 18): "Y todas sus calles dirán: «¡Aleluya!», y darán alabanza, "
              "diciendo: «Bendito sea Dios, que ha exaltado todos los siglos».",

    # --- 14. La vejez de Tobit y el final ----------------------------------
    (14, 1): "Y Tobit acabó su confesión.",
    (14, 2): "Y tenía cincuenta y ocho años cuando perdió la vista, y a los ocho "
             "años volvió a ver; y hacía obras de misericordia, y siguió temiendo "
             "al Señor Dios y confesándole.",
    (14, 3): "Y envejeció mucho; y llamó a su hijo y a los hijos de éste, y le "
             "dijo: «Hijo, toma a tus hijos: he aquí que he envejecido y estoy a "
             "punto de salir de esta vida.",
    (14, 4): "Vete a Media, hijo, porque estoy persuadido de cuanto habló Jonás "
             "el profeta acerca de Nínive, que será destruida; y en Media habrá "
             "más paz por un tiempo. Y nuestros hermanos serán esparcidos por la "
             "tierra lejos de la tierra buena, y Jerusalén quedará desierta, y la "
             "casa de Dios en ella será quemada, y quedará desierta por un "
             "tiempo.",
    (14, 5): "Y de nuevo Dios tendrá misericordia de ellos y los hará volver a "
             "la tierra, y edificarán la casa, no como la primera, hasta que se "
             "cumplan los tiempos del siglo. Y después de esto volverán de sus "
             "cautiverios y edificarán Jerusalén con honra, y la casa de Dios "
             "será edificada en ella gloriosamente, según hablaron de ella los "
             "profetas.",
    (14, 6): "Y todas las naciones se volverán a temer de verdad al Señor Dios; "
             "y enterrarán sus ídolos,",
    (14, 7): "y todas las naciones bendecirán al Señor. Y su pueblo confesará a "
             "Dios, y el Señor ensalzará a su pueblo; y se gozarán todos los que "
             "aman al Señor Dios en verdad y en justicia, haciendo misericordia "
             "con nuestros hermanos.",
    (14, 8): "Y ahora, hijo, vete de Nínive, porque sin duda sucederá lo que "
             "habló el profeta Jonás.",
    (14, 9): "Y tú guarda la ley y los preceptos, y sé amigo de la misericordia "
             "y justo, para que te vaya bien.",
    (14, 10): "Y sepúltame con decencia, y a tu madre conmigo; y no os quedéis "
              "más en Nínive. Hijo, mira lo que hizo Adam a Ajícar, que lo había "
              "criado: cómo lo llevó de la luz a las tinieblas, y cuánto le "
              "pagó. Y a Ajícar lo salvó, pero a aquél le fue dada su paga, y él "
              "bajó a las tinieblas. Manasés hizo misericordia, y fue librado "
              "del lazo de muerte que le habían tendido; pero Adam cayó en el "
              "lazo y pereció.",
    (14, 11): "Y ahora, hijos, ved lo que hace la misericordia y de qué libra la "
              "justicia». Y diciendo esto, se le fue el alma en la cama; y tenía "
              "ciento cincuenta y ocho años, y lo sepultó con honra.",
    (14, 12): "Y cuando murió Ana, la sepultó junto a su padre. Y se fue Tobías "
              "con su mujer y sus hijos a Ecbátana, a casa de Raguel su suegro.",
    (14, 13): "Y envejeció con honra, y sepultó a sus suegros gloriosamente, y "
              "heredó los bienes de ellos y los de Tobit su padre.",
    (14, 14): "Y murió a los ciento siete años en Ecbátana de Media.",
    (14, 15): "Y antes de morir oyó la destrucción de Nínive, a la que llevaron "
              "cautiva Nabucodonosor y Asuero; y se alegró antes de morir por lo "
              "de Nínive. Amén.",
}
