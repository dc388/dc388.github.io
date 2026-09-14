# Publicar en Google Play

> Google Play y App Store son tiendas distintas. Este repositorio genera el
> **AAB de Android** para **Google Play Console**
> (https://play.google.com/console). Para iOS haría falta un proyecto aparte
> compilado en macOS con Xcode.

Son cuatro pasos, y el primero se hace una sola vez en la vida de la app.

## 1. Crear la clave de firma (una sola vez, en tu ordenador)

**Esta clave hay que crearla tú y guardarla tú.** Es la identidad de la app: con
ella se firma cada actualización, y si se pierde no hay forma de volver a
publicar bajo la misma ficha. Ni se envía por chat ni por correo ni se sube al
repositorio.

Necesitas `keytool`, que viene con cualquier JDK (`sudo apt install
default-jdk`, o con Android Studio ya lo tienes):

```bash
keytool -genkeypair -v \
  -keystore release.jks \
  -alias biblia-griega \
  -keyalg RSA -keysize 2048 -validity 10000
```

Te pedirá una contraseña —apúntala en tu gestor de contraseñas— y unos datos de
identidad; el resto se puede dejar en blanco. Sal del programa con `yes`.

Luego **haz una copia de seguridad del archivo `release.jks`** en un sitio
distinto del ordenador donde lo creaste.

> Activa además la **firma de apps de Play** cuando crees la app en Play
> Console. Con ella, Google guarda la clave definitiva y la tuya pasa a ser
> solo la «clave de carga»: si algún día la pierdes, se puede sustituir. Sin
> ella, perder el archivo significa perder la app.

## 2. Guardar la clave en los secretos de GitHub

Convierte el archivo a texto:

```bash
base64 -w0 release.jks
```

En **Settings → Secrets and variables → Actions → New repository secret** del
repositorio, crea estos cuatro:

| Secreto | Valor |
|---|---|
| `KEYSTORE_BASE64` | la salida completa del comando de arriba |
| `KEYSTORE_PASSWORD` | la contraseña del almacén |
| `KEY_ALIAS` | `biblia-griega` |
| `KEY_PASSWORD` | la contraseña de la clave (la misma, si no pusiste otra) |

Los secretos no se pueden volver a leer desde la web y no aparecen en los
registros de compilación.

Para compilar firmado en tu propio ordenador, en vez de secretos crea
`app/keystore.properties`, que está en `.gitignore` y no se sube nunca:

```properties
storeFile=/ruta/absoluta/release.jks
storePassword=...
keyAlias=biblia-griega
keyPassword=...
```

## 3. Compilar

El flujo **Publicación — Biblia** compila el AAB para Play y un APK del mismo
código para probarlo.

- **Sin los secretos puestos** compila igual, pero *sin firmar*. Sirve para
  comprobar que la compilación de publicación pasa —que es donde salen los
  fallos de R8, la reducción de código que no se aplica en la compilación de
  depuración— antes de tener la clave. Un AAB sin firmar no lo acepta Play.
- **Con los secretos puestos** sale firmado y listo para subir.

Se lanza desde **Actions → Publicación — Biblia → Run workflow**, o empujando
una etiqueta:

```bash
git tag biblia-v1.0.0
git push origin biblia-v1.0.0
```

Los archivos quedan en el artefacto `biblia-publicacion` de la ejecución, y el
resumen de la ejecución dice si salió firmado y cuánto pesa cada uno.

Para subir una versión nueva más adelante hay que subir `versionCode` en
`app/build.gradle.kts`: Play rechaza dos veces el mismo número.

## 4. Subirlo a Play Console

1. **Crear app** → nombre, idioma predeterminado español, gratuita.
2. Deja activada la **firma de apps de Play**.
3. **Versiones → Producción → Crear versión** y sube el `.aab`.
4. Rellena la ficha con los textos de [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md)
   y los gráficos de `docs/store/`.
5. En **Seguridad de los datos**, responde que la app **no recoge ni comparte
   ningún dato**: es cierto, no declara ni el permiso de internet. El
   cuestionario está resuelto en [PRIVACIDAD.md](PRIVACIDAD.md).
6. Las **capturas de pantalla** tómalas del teléfono con la app instalada; Play
   exige al menos dos y no admite montajes. La lista de las que mejor la
   enseñan está al final de la ficha.

Antes de enviar a revisión, prueba el AAB con la **prueba interna** de Play: se
instala desde un enlace en tu propio teléfono y es el mismo archivo que después
pasa a producción.
