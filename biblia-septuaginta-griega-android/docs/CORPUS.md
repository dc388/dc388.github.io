# El corpus: qué hay dentro y de dónde sale

La aplicación nació con las tres colecciones canónicas. Este documento lleva la
cuenta de lo que se va añadiendo para el estudio, qué licencia tiene cada cosa
y qué falta.

## Lo que hay hoy

| Colección | Edición | Licencia |
|---|---|---|
| Antiguo Testamento hebreo | Códice de Leningrado (OSHB) | CC BY 4.0 |
| Septuaginta | H. B. Swete, Cambridge 1887–1912 | CC BY-SA 4.0 |
| Nuevo Testamento griego | Robinson–Pierpont 2018 | Dominio público |
| **Padres Apostólicos** | **Kirsopp Lake, Loeb 1912–1917** | **CC BY-SA 4.0** |

Los Padres Apostólicos son 15 obras y 1 941 versículos: 1 y 2 Clemente, las
siete cartas auténticas de Ignacio, Policarpo a los Filipenses, el Martirio de
Policarpo, la Didaché, Bernabé, el Pastor de Hermas y la carta a Diogneto.

Van en su propia colección, no mezclados con el Nuevo Testamento, porque no son
canónicos. Quien abra la aplicación para leer el canon no se los encuentra
delante; quien los busca sabe dónde están.

### Cómo se leen

El texto de Lake no viene analizado, igual que el de Swete. Se apoya en el mismo
puente: al tocar una palabra se muestra lo que esa misma forma significa en el
Nuevo Testamento, diciendo de dónde sale. Cubre el **82,6 %** de sus palabras,
algo más que el 82,3 % de la Septuaginta —era de esperar, porque es griego de la
misma época y del mismo registro.

`ReaderScreen` decide esto por `GRIEGO_SIN_ANALIZAR`, no por el nombre de una
colección concreta: cualquier colección griega sin etiquetar que se añada
después entra sola.

### Obligaciones de la licencia

CC BY-SA 4.0 exige citar la fuente y mantener la misma licencia sobre el texto.
La cita sale sola: la pantalla de ajustes recorre las colecciones de la base y
enseña edición, licencia y dirección de cada una, así que basta con que la fila
de `collections` esté bien puesta.

## Lo que falta, por orden de dificultad

**Josefo y Filón.** Griego, ediciones de Niese y de Cohn-Wendland, en dominio
público y ya en Perseus. Es el paso más rentable: mucho texto, cero problemas de
derechos y el mismo puente de formas los cubre.

**Pseudoepígrafos del Antiguo Testamento.** Enoc, Jubileos, los Testamentos de
los Doce Patriarcas, 4 Esdras, 2 Baruc, los Oráculos Sibilinos, la Vida de Adán
y Eva. El griego y el etiópico están disponibles; la traducción inglesa de
Charles (1913) también.

**Apócrifos del Nuevo Testamento.** Tomás (copto y los fragmentos griegos de
Oxirrinco), el Protoevangelio de Santiago, el Evangelio de Pedro, los Hechos de
Pablo y Tecla. Las ediciones de Tischendorf están en dominio público.

## Lo que no se puede incluir

Conviene tenerlo escrito para no volver a investigarlo cada vez:

- **Traducciones al español de los pseudoepígrafos.** La edición de Diez Macho y
  las demás están con derechos vivos. Es el hueco grande: el texto original sí,
  la traducción no.
- **Manuscritos del Mar Muerto.** Las transcripciones académicas están
  protegidas.
- **Nag Hammadi.** Igual: las ediciones críticas del copto tienen derechos.

## Al publicar la siguiente versión

Las cifras de `docs/FICHA_PLAY_STORE.md` describen la versión que está en Play,
no la base actual. Cuando esto salga a producción hay que subirlas: de 122 a
**137 libros** y de 60 651 a **62 592 versículos**.
