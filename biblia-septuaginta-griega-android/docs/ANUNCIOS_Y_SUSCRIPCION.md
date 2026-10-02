# Anuncios y suscripción

La aplicación es gratuita, muestra un banner al pie del lector y ofrece una
suscripción mensual que lo quita. Este documento explica cómo está montado y,
sobre todo, **qué tienes que crear tú** antes de que empiece a ingresar.

Resumen honesto de lo que se puede esperar: un banner deja del orden de
0,20 a 1,50 USD por cada mil impresiones en español, y el 1–3 % de quienes
usan una aplicación así pagan una suscripción. Con mil personas leyendo a
diario no son miles de dólares; son decenas. Lo que hace que crezca es que
la aplicación se use mucho, no que el anuncio sea más agresivo.

---

## 1. Lo que ya está hecho en el código

| Pieza | Dónde |
|---|---|
| Identificadores y estado de pruebas | `data/Anuncios.kt` (los valores los inyecta Gradle) |
| Suscripción contra Google Play | `data/Compras.kt` |
| Consentimiento europeo y banner | `ui/Publicidad.kt` |
| Banner al pie del lector | `ui/screens/ReaderScreen.kt` |
| Tarjeta «Quitar los anuncios» | `ui/screens/SettingsScreen.kt` |
| Permisos y `APPLICATION_ID` de AdMob | `AndroidManifest.xml` |

Decisiones que conviene no deshacer sin pensarlo:

- **El banner va en la barra inferior, nunca sobre el texto.** Un anuncio
  intersticial entre capítulos pagaría más y arruinaría la aplicación.
- **Quien paga no ve ni el hueco.** El banner no se oculta: no se crea.
- **El SDK de anuncios no arranca hasta tener el consentimiento.** Arrancarlo
  antes ya cuenta como tratar datos en Europa.
- **Play es la única fuente de verdad de la suscripción.** No se guarda en el
  teléfono ningún «ya pagó»: un archivo local se edita en cinco minutos.
- **Una compilación de publicación con los identificadores de prueba falla.**
  Se vería idéntica y no ingresaría un céntimo.

## 2. Crear la cuenta de AdMob

1. Entra en <https://admob.google.com> con la misma cuenta de Google que usas
   en Play Console y acepta las condiciones.
2. **Aplicaciones → Añadir aplicación → Android**. Si la aplicación aún no está
   publicada, elige «No» cuando pregunte si está en una tienda; podrás
   enlazarla después.
3. Apunta el **ID de la aplicación**, con la forma
   `ca-app-pub-0000000000000000~0000000000` (la tilde `~` es parte del ID).
4. **Bloques de anuncios → Añadir bloque → Banner**. Llámalo `lector-pie`.
   Apunta su **ID de bloque**: `ca-app-pub-0000000000000000/0000000000`
   (aquí la barra `/`).
5. En **Pagos**, rellena la dirección y los datos fiscales. Google no paga
   nada hasta que esto está completo y hasta llegar al umbral de 100 USD.

## 3. Meter esos identificadores en la compilación

No van en el repositorio. Entran por variables de entorno o por propiedades de
Gradle:

```bash
ADMOB_APP_ID='ca-app-pub-…~…' ADMOB_BANNER='ca-app-pub-…/…' ./gradlew bundleRelease
```

o bien

```bash
./gradlew bundleRelease -PadmobAppId='ca-app-pub-…~…' -PadmobBanner='ca-app-pub-…/…'
```

En GitHub Actions se añaden como **secretos del repositorio**, junto a los
cuatro de la firma, con esos mismos dos nombres: `ADMOB_APP_ID` y
`ADMOB_BANNER`. El flujo de publicación ya los pasa a Gradle.

Si no se definen, la compilación usa los identificadores de prueba de Google,
que enseñan un anuncio de mentira y no pagan nada; con ellos `assembleRelease`
y `bundleRelease` **fallan a propósito**. Para generar una release de prueba
—comprobar la firma, por ejemplo— se añade `-PadmobPruebasEnRelease=true`.

> Nunca pruebes con los identificadores de verdad en tu propio teléfono. AdMob
> lo interpreta como tráfico inválido y cierra cuentas por eso. Para probar con
> los reales, registra tu teléfono como dispositivo de prueba en AdMob.

## 4. Crear la suscripción en Play Console

En **Monetizar → Productos → Suscripciones → Crear suscripción**:

- **ID del producto**: `sin_anuncios_mensual` — tiene que ser exactamente este,
  es el que busca `Anuncios.SUSCRIPCION_SIN_ANUNCIOS`. No se puede cambiar
  después.
- **Nombre**: `Sin anuncios`
- **Descripción**: `Quita el anuncio del pie. Todo lo demás es igual.`
- **Plan base**: recurrente, mensual, renovación automática.
- **Precio**: entre 1 y 2 USD al mes funciona para este tipo de aplicación.
  Deja que Play convierta a las demás monedas automáticamente.
- **Periodo de prueba**: opcional; una semana gratis sube las altas.
- Activa el plan base: creado no es lo mismo que activo, y un plan inactivo
  hace que la aplicación no encuentre el precio y deje el botón apagado.

La suscripción **no existe hasta que hay una versión publicada** —aunque sea en
pruebas internas— con el `applicationId` `com.dc388.bibliagriega`.

## 5. Probar que la compra funciona

En **Configuración → Pruebas de licencia** de Play Console, añade tu correo
como probador. Desde esas cuentas la compra es real en todo menos en el cobro:
no se cobra nada y la renovación mensual pasa cada cinco minutos, para que se
pueda probar la caducidad.

Qué comprobar:

1. Con la aplicación recién instalada, aparece el banner al pie del lector.
2. En Ajustes, la tarjeta muestra el precio en tu moneda, no el botón apagado.
3. Al comprar, el banner desaparece sin tener que reiniciar.
4. Al cerrar y volver a abrir, sigue sin aparecer.
5. Al cancelar desde Play y esperar a que caduque, vuelve.

## 6. Lo que hay que declarar en Play

Ya está reflejado en [PUBLICAR_EN_PLAY.md](PUBLICAR_EN_PLAY.md), pero lo
importante en dos líneas: hay que marcar **«contiene anuncios»** y **«compras
dentro de la aplicación»**, y el formulario de seguridad de los datos pasa a
declarar el **ID de publicidad** y la **ubicación aproximada**, ambos
recopilados y compartidos con finalidad publicitaria. Contestar que no se
recoge nada cuando se lleva AdMob dentro es una de las formas más rápidas de
que retiren una aplicación.

La política de privacidad publicada en
<https://dc388.github.io/biblia-privacidad.html> ya dice todo esto; si se
cambia algo aquí, hay que cambiarla también.
