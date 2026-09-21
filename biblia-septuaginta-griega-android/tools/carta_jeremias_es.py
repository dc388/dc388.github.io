"""La Carta de Jeremías en español, traducida del griego.

Es Baruc 6 en la Vulgata y circula suelta en los códices griegos. Para las
Asambleas de Dios no es canon; aquí se ofrece para estudio, y vale la pena por
lo que es: setenta y dos versículos de sátira contra los ídolos, con el estribillo
«de donde se conoce que no son dioses; no los temáis» repetido como un martillo.

El argumento no es teológico sino de observación: a los dioses hay que
limpiarles el polvo, les vuelan murciélagos encima, los sacerdotes les roban el
oro, y si se caen alguien tiene que levantarlos. Isaías 44 y el Salmo 115 hacen
lo mismo, y comparar los tres es el ejercicio.

El versículo 0 es el encabezamiento de la carta, que la edición griega numera
aparte del cuerpo.
"""

from __future__ import annotations

CARTA_JEREMIAS_ES: dict[tuple[int, int], str] = {
    (1, 0): "Copia de la carta que envió Jeremías a los que iban a ser llevados "
            "cautivos a Babilonia por el rey de los babilonios, para anunciarles "
            "lo que Dios le había mandado.",
    (1, 1): "Por los pecados que habéis cometido delante de Dios, seréis "
            "llevados cautivos a Babilonia por Nabucodonosor, rey de los "
            "babilonios.",
    (1, 2): "Entrados, pues, en Babilonia, estaréis allí muchos años y largo "
            "tiempo, hasta siete generaciones; y después de esto os sacaré de "
            "allí en paz.",
    (1, 3): "Y ahora veréis en Babilonia dioses de plata y de oro y de madera, "
            "llevados en hombros, que infunden temor a las naciones.",
    (1, 4): "Guardaos, pues, de haceros semejantes a los extranjeros y de que el "
            "temor de ellos se apodere de vosotros",
    (1, 5): "al ver la multitud que delante y detrás de ellos se postra. Decid "
            "más bien en vuestro pensamiento: «A ti hay que postrarse, "
            "Soberano».",
    (1, 6): "Porque mi ángel está con vosotros, y él mismo cuida de vuestras "
            "vidas.",
    (1, 7): "Porque su lengua la pulió un artesano, y ellos están dorados y "
            "plateados; pero son falsos y no pueden hablar.",
    (1, 8): "Y como para una doncella amiga de adornos, tomando oro",
    (1, 9): "les fabrican coronas para las cabezas de sus dioses. Y sucede "
            "también que los sacerdotes sustraen de sus dioses el oro y la plata "
            "y lo gastan en sí mismos,",
    (1, 10): "y hasta dan de ello a las prostitutas del terrado. Y los adornan "
             "con vestidos como a hombres: dioses de plata y dioses de oro y de "
             "madera.",
    (1, 11): "Pero ellos no se libran del orín ni de la carcoma, aunque estén "
             "envueltos en vestidura de púrpura.",
    (1, 12): "Les limpian el rostro por el polvo de la casa, que se les acumula "
             "encima.",
    (1, 13): "Y tiene cetro como un hombre, juez de la comarca, pero no quita la "
             "vida al que peca contra él.",
    (1, 14): "Tiene puñal en la diestra, y hacha; pero a sí mismo no se librará "
             "de la guerra ni de los ladrones. De donde se conoce que no son "
             "dioses; no los temáis, pues.",
    (1, 15): "Porque, así como un vaso de hombre, cuando se quiebra, queda "
             "inservible,",
    (1, 16): "así son sus dioses, colocados en sus templos. Sus ojos están llenos "
             "del polvo de los pies de los que entran.",
    (1, 17): "Y como se cierran los atrios en torno al que ha ofendido al rey, "
             "como a quien llevan a la muerte, así los sacerdotes aseguran sus "
             "templos con puertas y cerrojos y barras, para que no los saqueen "
             "los ladrones.",
    (1, 18): "Encienden lámparas, y más que para sí mismos, y ellos no pueden "
             "ver ninguna.",
    (1, 19): "Son como una viga de las de la casa; y dicen que les roen el "
             "corazón: los reptiles de la tierra los devoran a ellos y a su "
             "vestidura, y no lo sienten.",
    (1, 20): "Tienen el rostro ennegrecido por el humo de la casa.",
    (1, 21): "Sobre su cuerpo y sobre su cabeza vuelan murciélagos, golondrinas "
             "y las demás aves; y también se les suben los gatos.",
    (1, 22): "De donde conoceréis que no son dioses; no los temáis, pues.",
    (1, 23): "Porque el oro con que están revestidos para hermosura, si alguien "
             "no les limpia el orín, no brillará; que ni siquiera cuando los "
             "fundían lo sentían.",
    (1, 24): "Comprados a todo precio, están hechos, y no hay aliento en ellos.",
    (1, 25): "Sin pies, son llevados en hombros, mostrando a los hombres su "
             "propia deshonra; y se avergüenzan también los que les sirven,",
    (1, 26): "porque, si acaso cae en tierra, tienen que levantarlo ellos; y si "
             "alguien lo pone derecho, no se moverá por sí mismo; y si se "
             "inclina, no se enderezará, sino que, como a los muertos, se le "
             "ponen delante las ofrendas.",
    (1, 27): "Y sus sacerdotes venden sus sacrificios y los gastan; e igualmente "
             "sus mujeres los ponen en salmuera, y no dan parte ni al pobre ni "
             "al desvalido.",
    (1, 28): "Y de sus sacrificios llegan a tocar la mujer en su impureza y la "
             "recién parida. Conociendo, pues, por esto que no son dioses, no "
             "los temáis.",
    (1, 29): "Porque ¿de dónde habrían de llamarse dioses? Pues son mujeres las "
             "que sirven la mesa a dioses de plata y de oro y de madera;",
    (1, 30): "y en sus templos los sacerdotes están sentados con las túnicas "
             "rasgadas y las cabezas y las barbas rapadas, y con la cabeza "
             "descubierta;",
    (1, 31): "y aúllan gritando delante de sus dioses, como algunos en el "
             "banquete fúnebre de un muerto.",
    (1, 32): "De la vestidura de ellos toman los sacerdotes y visten a sus "
             "mujeres y a sus hijos.",
    (1, 33): "Y ni si alguien les hace mal ni si les hace bien podrán "
             "devolverlo; ni pueden poner rey ni quitarlo.",
    (1, 34): "Igualmente, ni riqueza ni dinero pueden dar; y si alguien les hace "
             "un voto y no lo cumple, no se lo reclamarán.",
    (1, 35): "De la muerte no librarán a un hombre, ni arrancarán al débil de "
             "manos del fuerte.",
    (1, 36): "A un hombre ciego no le devolverán la vista, ni librarán al hombre "
             "que está en angustia.",
    (1, 37): "De la viuda no tendrán compasión, ni harán bien al huérfano.",
    (1, 38): "A las piedras del monte se parecen los de madera, los dorados y "
             "los plateados; y los que les sirven quedarán avergonzados.",
    (1, 39): "¿Cómo, pues, ha de pensarse o decirse que son dioses?",
    (1, 40): "Y todavía: hasta los mismos caldeos los deshonran, pues cuando ven "
             "a un mudo que no puede hablar, lo llevan a Bel y le piden que "
             "hable, como si él pudiera enterarse;",
    (1, 41): "y ni aun dándose cuenta son capaces de abandonarlos, porque no "
             "tienen entendimiento.",
    (1, 42): "Y las mujeres, ceñidas de cuerdas, se sientan en los caminos "
             "quemando salvado;",
    (1, 43): "y cuando alguna de ellas, arrastrada por alguno de los que pasan, "
             "se acuesta con él, echa en cara a su vecina que no ha sido tenida "
             "por digna como ella, ni se le ha roto su cuerda.",
    (1, 44): "Todo lo que se hace con ellos es falso. ¿Cómo, pues, ha de "
             "pensarse o decirse que son dioses?",
    (1, 45): "Por artesanos y orfebres han sido fabricados; y no llegan a ser "
             "otra cosa que la que los artífices quieren que sean.",
    (1, 46): "Y los mismos que los fabrican no llegan a vivir muchos años;",
    (1, 47): "¿cómo, pues, habrían de serlo las cosas fabricadas por ellos? "
             "Porque dejaron mentiras y oprobio a los que vienen después.",
    (1, 48): "Porque cuando viene sobre ellos guerra y males, los sacerdotes "
             "deliberan entre sí dónde esconderse con ellos.",
    (1, 49): "¿Cómo, pues, no se ha de entender que no son dioses, los que ni de "
             "la guerra ni de los males se salvan a sí mismos?",
    (1, 50): "Porque, siendo de madera y dorados y plateados, se conocerá "
             "después que son falsos; y a todas las naciones y a los reyes les "
             "será manifiesto que no son dioses, sino obra de manos de hombres, "
             "y que no hay en ellos obra alguna de Dios.",
    (1, 51): "¿A quién, pues, no le será claro que no son dioses?",
    (1, 52): "Porque no levantarán rey en la tierra, ni darán lluvia a los "
             "hombres;",
    (1, 53): "ni juzgarán pleito entre ellos mismos, ni librarán del agravio, "
             "porque no pueden;",
    (1, 54): "porque son como cornejas entre el cielo y la tierra. Pues cuando "
             "cae fuego en la casa de dioses de madera, dorados o plateados, sus "
             "sacerdotes huirán y se salvarán, pero ellos arderán en medio como "
             "vigas.",
    (1, 55): "Y a un rey y a unos enemigos no les harán frente.",
    (1, 56): "¿Cómo, pues, se ha de admitir o pensar que son dioses? Ni de "
             "ladrones ni de salteadores se librarán, esos dioses de madera y "
             "plateados y dorados,",
    (1, 57): "a quienes los fuertes despojarán del oro y de la plata, y se irán "
             "llevando la vestidura que los cubre; y ni a sí mismos se ayudarán.",
    (1, 58): "De modo que más vale un rey que muestra su valor, o un utensilio "
             "útil en una casa, del que se sirve su dueño, que los dioses "
             "falsos; o una puerta en una casa, que guarda lo que hay dentro, "
             "que los dioses falsos; y una columna de madera en un palacio […]",
    (1, 59): "Porque el sol y la luna y las estrellas, que son brillantes y son "
             "enviados a servir, obedecen.",
    (1, 60): "Igualmente el relámpago, cuando aparece, bien se ve; y lo mismo el "
             "viento sopla en toda comarca;",
    (1, 61): "y las nubes, cuando Dios les manda recorrer toda la tierra "
             "habitada, cumplen lo mandado.",
    (1, 62): "Y el fuego, enviado de arriba para consumir montes y bosques, hace "
             "lo que se le manda. Pero éstos no se parecen a aquéllos ni en su "
             "forma ni en su poder.",
    (1, 63): "De donde ni ha de pensarse ni decirse que son dioses, no siendo "
             "capaces ni de juzgar un pleito ni de hacer bien a los hombres.",
    (1, 64): "Conociendo, pues, que no son dioses, no los temáis.",
    (1, 65): "Porque ni maldecirán a los reyes ni los bendecirán.",
    (1, 66): "Ni mostrarán señales en el cielo a las naciones, ni brillarán como "
             "el sol, ni alumbrarán como la luna.",
    (1, 67): "Las fieras son mejores que ellos, pues pueden huir a un refugio y "
             "valerse.",
    (1, 68): "De ninguna manera, pues, nos es manifiesto que sean dioses; por "
             "eso, no los temáis.",
    (1, 69): "Porque como un espantajo en un melonar, que nada guarda, así son "
             "sus dioses de madera y dorados y plateados.",
    (1, 70): "Del mismo modo, a un espino en un huerto, sobre el que se posa "
             "toda ave, y también a un muerto arrojado en tinieblas, se parecen "
             "sus dioses de madera y dorados y plateados.",
    (1, 71): "Y por la púrpura y el mármol que sobre ellos se pudre conoceréis "
             "que no son dioses; y ellos mismos al fin serán roídos, y serán "
             "oprobio en la tierra.",
    (1, 72): "Más vale, pues, el hombre justo que no tiene ídolos, porque estará "
             "lejos del oprobio.",
}
