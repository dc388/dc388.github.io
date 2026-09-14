# Publicar en Google Play

> Google Play y App Store son tiendas distintas. Este repositorio genera el
> **AAB de Android** para **Google Play Console** (https://play.google.com/console).
> Para iOS haría falta un proyecto aparte compilado en macOS con Xcode.

Lo que ya está hecho y lo que falta:

| | Qué | Estado |
|---|---|---|
| 1 | Clave de firma | **tuya, falta** |
| 2 | Secretos en GitHub | **falta** (depende de 1) |
| 3 | AAB compilado | listo — se genera solo |
| 4 | Textos de la ficha | listos, en [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md) |
| 5 | Icono y gráfico destacado | listos, en `docs/store/` |
| 6 | Capturas de pantalla | **tuyas, faltan** |
| 7 | Política de privacidad publicada | página lista, **falta subirla** |
| 8 | Formularios de Play Console | respuestas preparadas, abajo |

---

## 1. Crear la clave de firma (una sola vez, en tu ordenador)

**Esta clave la creas y la guardas tú.** Es la identidad de la app: con ella se
firma cada actualización, y si se pierde no hay forma de volver a publicar bajo
la misma ficha. No se envía por chat, ni por correo, ni se sube al repositorio.

Necesitas `keytool`, que viene con cualquier JDK (`sudo apt install default-jdk`,
o ya lo tienes si instalaste Android Studio):

```bash
keytool -genkeypair -v \
  -keystore release.jks \
  -alias biblia-griega \
  -keyalg RSA -keysize 2048 -validity 10000
```

Te pedirá una contraseña —apúntala en tu gestor de contraseñas— y unos datos de
identidad; el resto puede quedar en blanco. Confirma con `yes`.

Luego **haz una copia de seguridad de `release.jks`** en un sitio distinto del
ordenador donde lo creaste.

> **Activa la firma de apps de Play** cuando crees la app en Play Console. Con
> ella, Google guarda la clave definitiva y la tuya pasa a ser solo la «clave de
> carga»: si algún día la pierdes, se puede sustituir. Sin ella, perder ese
> archivo es perder la app.

## 2. Guardar la clave en los secretos de GitHub

Convierte el archivo a texto:

```bash
base64 -w0 release.jks
```

En **Settings → Secrets and variables → Actions → New repository secret**, crea:

| Secreto | Valor |
|---|---|
| `KEYSTORE_BASE64` | la salida completa del comando de arriba |
| `KEYSTORE_PASSWORD` | la contraseña del almacén |
| `KEY_ALIAS` | `biblia-griega` |
| `KEY_PASSWORD` | la contraseña de la clave (la misma, si no pusiste otra) |

Los secretos no se pueden volver a leer desde la web y no salen en los registros.

Para compilar firmado en tu propio ordenador, en vez de secretos crea
`app/keystore.properties`, que está en `.gitignore` y no se sube nunca:

```properties
storeFile=/ruta/absoluta/release.jks
storePassword=...
keyAlias=biblia-griega
keyPassword=...
```

## 3. Compilar el AAB

El flujo **Publicación — Biblia** compila el AAB para Play y un APK del mismo
código. Sin los secretos compila igual, pero *sin firmar*: sirve para comprobar
que la compilación pasa, y Play no lo acepta. Con los secretos, sale firmado.

Se lanza desde **Actions → Publicación — Biblia → Run workflow**, o empujando
una etiqueta:

```bash
git tag biblia-v1.0.0 && git push origin biblia-v1.0.0
```

Queda en el artefacto `biblia-publicacion`, y el resumen de la ejecución dice si
salió firmado y cuánto pesa.

Para cada versión nueva hay que subir `versionCode` en `app/build.gradle.kts`:
Play rechaza dos veces el mismo número.

## 7. Publicar la política de privacidad

**Play exige una dirección web pública** con la política de privacidad; no vale
un archivo dentro del repositorio.

La página está escrita y lista en `docs/store/privacidad.html`. Antes de subirla,
**sustituye `CORREO_DE_CONTACTO`** por la dirección donde quieras recibir dudas
—se queda a la vista de cualquiera, así que elige cuál—.

Tu sitio ya publica en `dc388.github.io`, así que lo más corto es dejarla ahí, en
la rama `main` del repositorio del sitio:

```bash
git checkout main
cp biblia-septuaginta-griega-android/docs/store/privacidad.html biblia-privacidad.html
git add biblia-privacidad.html
git commit -m "Política de privacidad de la app Biblia Griega"
git push
```

Queda publicada en **https://dc388.github.io/biblia-privacidad.html**, y esa es
la dirección que se pega en Play Console.

## 8. Los formularios de Play Console

Las respuestas, ya resueltas para esta app:

**Ficha principal**
- Nombre, descripción breve y completa: [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md)
- Categoría: **Libros y obras de consulta**
- Etiquetas: biblia, griego, hebreo, septuaginta, interlineal
- Correo de contacto: el tuyo (sale publicado en la ficha)
- Icono: `docs/store/icono-512.png` · Gráfico destacado: `docs/store/grafico-destacado-1024x500.png`
- Capturas: mínimo 2 (ver abajo)

**Seguridad de los datos** — el formulario más largo, y aquí es todo «no»:
- ¿La app recopila o comparte datos de usuario? **No**
- ¿Los datos están cifrados en tránsito? *(no aplica, no hay tránsito)*
- ¿Se pueden solicitar la eliminación de datos? *(no aplica)*

  Es cierto y comprobable: el manifiesto no declara ni un permiso. Si Play
  pregunta por qué, la razón está en `AndroidManifest.xml`.

**Clasificación de contenido** (cuestionario IARC)
- Categoría: **Libros y obras de consulta** (no es un juego)
- Violencia, sexo, lenguaje soez, drogas, juego, compras: **no** en todas
- Resultado esperado: apta para todos los públicos

  El texto bíblico contiene pasajes violentos, pero el cuestionario pregunta por
  contenido *representado* —imágenes, escenas interactivas—, no por literatura.

**Público objetivo y contenido**
- Edades: **13 años en adelante** o «todos». No marques que va dirigida a niños:
  activa los requisitos de la política para familias, que exigen cosas que esta
  app no necesita.

**Declaraciones**
- Anuncios: **no contiene anuncios**
- App de finanzas, salud, gobierno, noticias, COVID: **no**
- Contenido generado por usuarios: **no** (las notas se quedan en el teléfono)

**Política de privacidad**: la dirección del punto 7.

## Las capturas hay que hacerlas en el teléfono

Play pide al menos dos y exige que muestren la aplicación de verdad: no valen
maquetas ni montajes. Con el APK instalado, en el teléfono pulsa
**encendido + bajar volumen** en cada pantalla. Las que mejor la cuentan:

1. Un capítulo con la traducción debajo —por ejemplo Juan 3— que es lo primero
   que se entiende al verla.
2. Génesis 1 en hebreo, con el texto alineado a la derecha.
3. El interlineal de Juan 1, con la transliteración y el Strong bajo cada palabra.
4. La ficha de una palabra abierta, con el análisis y el léxico.
5. La búsqueda con resultados.

## Antes de enviar a revisión

- **Prueba interna**: sube el AAB ahí primero. Se instala desde un enlace en tu
  propio teléfono y es el mismo archivo que después pasa a producción.
- **Verificación de identidad**: Play la pide a toda cuenta de desarrollador
  antes de publicar. Tarda unos días; empieza pronto.
- **Cuentas personales creadas desde noviembre de 2023**: Google exige una
  prueba cerrada con **al menos 12 probadores durante 14 días seguidos** antes de
  poder pasar a producción. Si tu cuenta es de empresa, no aplica. Conviene
  comprobarlo antes de contar los plazos: son dos semanas de calendario.

## Una decisión que queda pendiente

La app instalada se llama **Biblia Griega** (`app_name` en `strings.xml`), que es
como aparece bajo el icono. La ficha propone **Biblia Griega y Hebrea**, porque
el nombre corto se quedó pequeño cuando entraron el Antiguo Testamento hebreo y
la traducción. Puedes:

- dejarlo como está —el nombre de la ficha y el del icono no tienen que coincidir—, o
- cambiar `app_name` antes de compilar la versión de publicación, para que
  coincidan.

Es decisión de marca, no técnica.
