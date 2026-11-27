# Mudar esto a otra cuenta

Escrito el 27 de noviembre de 2026, cuando el dueño avisa de que va a perder el
acceso a la cuenta actual.

**Guarda una copia de este archivo fuera de GitHub.** Si la cuenta que se pierde
es la de GitHub, este documento se va con ella.

---

## Lo primero, hoy, pase lo que pase

### 1. El almacén de claves

`release.jks` y sus dos contraseñas. Es la identidad de la aplicación: con esa
clave se firma cada actualización.

**No está en GitHub de forma recuperable.** Está en el secreto
`KEYSTORE_BASE64`, y los secretos de GitHub **no se pueden volver a leer**, ni
por su dueño. Lo que hay en GitHub sirve para compilar, no para recuperar.

O sea: la única copia utilizable es el archivo `release.jks` del ordenador donde
se creó. Cópialo hoy a dos sitios que no dependan de ninguna de las dos cuentas
—un disco externo, un gestor de contraseñas con adjuntos, lo que sea— junto con:

- la contraseña del almacén,
- la contraseña de la clave,
- el alias: `biblia-griega`.

### 2. Mirar si está activada la firma de apps de Play

Esto decide cuánto duele perder lo anterior.

En Play Console, dentro de la aplicación:
**Protección de Play Store → Gestionar la firma de apps de Play**
(en inglés: *Protected with Play → Play Store protection → Manage Play app
signing*).

- **Si está activada:** Google guarda la clave definitiva y la tuya es solo la
  «clave de carga». Si se pierde, se pide un restablecimiento subiendo un
  certificado nuevo. Se puede recuperar.
- **Si no está activada:** perder `release.jks` es perder la aplicación. Nadie,
  ni Google, puede volver a publicar una actualización bajo esa ficha.

Haz esta comprobación antes de nada y apunta el resultado aquí.

---

## La mala noticia sobre Play

La cuenta es **personal** y **monetiza** (anuncios y suscripción). Para esa
combinación, Google cierra el camino fácil. De su propia página sobre el cambio
de propietario:

> *Individual developers who monetize their apps are currently ineligible for
> this direct transfer process.*

Es decir: **no se puede pasar la cuenta a otro propietario**. Hay que:

1. Crear una **cuenta de desarrollador nueva** con el correo destino.
   **25 dólares**, de una vez.
2. Darle un **perfil de pagos activo**, que hace falta porque la aplicación
   tiene suscripción.
3. Pedir la **transferencia de la aplicación** de la cuenta vieja a la nueva.

### Lo que hace falta para la transferencia

- Las dos cuentas **activas y con sesión iniciable**. Esta es la parte con
  prisa: **si se pierde el acceso a la cuenta vieja antes de pedir la
  transferencia, ya no se puede pedir.**
- El **identificador de transacción del registro** de cada una de las dos
  cuentas (el del pago de los 25 dólares). Se quita el prefijo al enviarlo:
  de `0.G.123456789` se manda `123456789`.
- Que el dueño de la cuenta destino **apruebe** la solicitud.
- Las dos cuentas en regla con las políticas de Play.

Google responde a la solicitud **en dos días hábiles** desde la aprobación. No
dice cuánto tarda la transferencia en sí.

### Lo que se lleva la aplicación y lo que se queda

**Se transfiere:** los usuarios, las estadísticas, las valoraciones y reseñas,
la clasificación de contenido, la ficha de la tienda y las suscripciones.

**No se transfiere:**

- Los informes de pagos y ganancias.
- La exportación masiva.
- Los grupos de prueba.
- **Los pedidos anteriores a la transferencia se quedan en la cuenta vieja.**

Las claves de firma sí acompañan a la aplicación. Google no promete
explícitamente que las actualizaciones no se interrumpan, pero sí explica cómo
pedir una clave de carga nueva después de transferir, si se prefiere no
compartir la vieja.

---

## Lo demás que hay que mudar, y no es poco

Play es solo una pata. Esto cuelga de tres cuentas distintas:

| Qué | De qué cuenta depende | Qué pasa si se pierde |
|---|---|---|
| Ficha y aplicación en Play | Google (Play Console) | ver arriba: cuenta nueva + transferencia |
| **AdMob** y el perfil de pagos | Google (AdMob, cuenta aparte) | los identificadores de anuncio son de esa cuenta; hay que crear unidades nuevas y cambiarlas en los secretos |
| **Repositorio y flujos** | GitHub (`dc388`) | se va el código, el historial y **todos los secretos** |
| **La web de la Biblia** | GitHub Pages (`dc388.github.io`) | se va la dirección; las páginas de palabra indexadas en Google mueren con ella |
| Los cuatro secretos de firma | GitHub, no recuperables | hay que volver a ponerlos desde `release.jks` |

Lo de la web merece pensarse aparte: hay **13 000 páginas de palabra**
indexadas bajo `dc388.github.io`. Cambiar de dirección tira ese
posicionamiento a menos que se monte una redirección, y GitHub Pages solo
redirige si se conserva el repositorio viejo. Si la cuenta de GitHub se pierde
del todo, no hay redirección posible.

---

## Orden recomendado

1. **Hoy:** copia de `release.jks` y sus contraseñas fuera de las dos cuentas.
2. **Hoy:** mirar si la firma de apps de Play está activada, y apuntarlo.
3. Crear la cuenta de desarrollador nueva (25 USD) y su perfil de pagos.
4. Pedir la transferencia de la aplicación **mientras la cuenta vieja siga
   accesible**.
5. Crear la cuenta de AdMob nueva, sus unidades de anuncio, y cambiar los
   secretos `ADMOB_APP_ID` y `ADMOB_BANNER`.
6. Mover el repositorio de GitHub y volver a poner los seis secretos.
7. Decidir qué hacer con `dc388.github.io`.

Los pasos 1 y 2 no dependen de ninguna decisión y no se deshacen. Los demás sí
pueden esperar a saber qué cuenta se pierde exactamente.
