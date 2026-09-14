# Publicar en Google Play

> Google Play y App Store son tiendas distintas. Este repositorio genera el
> **AAB de Android** para **Google Play Console** (https://play.google.com/console).
> Para iOS haría falta un proyecto aparte compilado en macOS con Xcode.

Lo que ya está hecho y lo que falta:

| | Qué | Estado |
|---|---|---|
| 1 | Clave de firma | **tuya, falta** |
| 2 | Secretos de firma en GitHub | **falta** (depende de 1) |
| 3 | Cuenta de AdMob y bloque de banner | **tuya, falta** — [ANUNCIOS_Y_SUSCRIPCION.md](ANUNCIOS_Y_SUSCRIPCION.md) |
| 4 | Secretos de AdMob en GitHub | **falta** (depende de 3) |
| 5 | Producto de suscripción en Play | **tuyo, falta** (después de subir la primera versión) |
| 6 | AAB compilado | listo — se genera solo |
| 7 | Textos de la ficha | listos, en [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md) |
| 8 | Icono y gráfico destacado | listos, en `docs/store/` |
| 9 | Capturas de pantalla | **tuyas, faltan** |
| 10 | Política de privacidad publicada | **hecho** — https://dc388.github.io/biblia-privacidad.html |
| 11 | Formularios de Play Console | respuestas preparadas, abajo |

Lo marcado como **tuyo** lo es porque exige una cuenta, un pago o un teléfono:
nadie más puede hacerlo por ti.

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

## 7. La política de privacidad — ya está publicada

**Play exige una dirección web pública** con la política de privacidad; no vale
un archivo dentro del repositorio. Está publicada en

**https://dc388.github.io/biblia-privacidad.html**

y esa es la dirección que se pega en Play Console. Su fuente es
`docs/store/privacidad.html`; para cambiarla, se edita ahí y se vuelve a copiar
a `biblia-privacidad.html` en la rama `main` del repositorio del sitio.

Ojo: esa página describe los anuncios y la suscripción. Si alguna vez se quitan
los anuncios, o se añade algo que recoja más datos, hay que actualizarla **antes**
de subir la versión que lo cambie.

## 8. Los formularios de Play Console

Las respuestas, ya resueltas para esta app:

**Ficha principal**
- Nombre, descripción breve y completa: [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md)
- Categoría: **Libros y obras de consulta**
- Etiquetas: biblia, griego, hebreo, septuaginta, interlineal
- Correo de contacto: el tuyo (sale publicado en la ficha)
- Icono: `docs/store/icono-512.png` · Gráfico destacado: `docs/store/grafico-destacado-1024x500.png`
- Capturas: mínimo 2 (ver abajo)

**Seguridad de los datos** — el formulario más largo. Desde que la aplicación
lleva anuncios ya no es todo «no»; contestarlo mal es de las cosas por las que
Play retira una aplicación, así que va literal:

- ¿La app recopila o comparte datos de usuario? **Sí**
- Tipo de dato: **Identificadores del dispositivo o de otro tipo** →
  *ID de publicidad*
  - ¿Se recopila? **Sí** · ¿Se comparte? **Sí**
  - ¿Es obligatorio? **Los usuarios pueden elegir** (la suscripción los quita)
  - Finalidad: **Publicidad o marketing**
- Tipo de dato: **Ubicación** → *Ubicación aproximada*
  - ¿Se recopila? **Sí** · ¿Se comparte? **Sí** · Finalidad: **Publicidad**
  - Es la que AdMob deduce de la dirección IP; la app no pide permiso de
    ubicación ni sabe dónde estás.
- ¿Los datos están cifrados en tránsito? **Sí** (AdMob y Play usan HTTPS)
- ¿Se puede solicitar la eliminación de datos? **Sí** — se borra el ID de
  publicidad desde Ajustes de Android → Google → Anuncios

Lo que **no** se declara, porque de verdad no sale del teléfono: las notas, los
marcadores, la posición de lectura, las preferencias y qué pasajes se leen.

Quien rellene esto encontrará las respuestas de AdMob ya preparadas en la
[guía de Google para el formulario](https://support.google.com/admob/answer/11116017).

**Clasificación de contenido** (cuestionario IARC)
- Categoría: **Libros y obras de consulta** (no es un juego)
- Violencia, sexo, lenguaje soez, drogas, juego: **no** en todas
- Compras dentro de la aplicación: **sí** (la suscripción que quita los anuncios)
- Resultado esperado: apta para todos los públicos

  El texto bíblico contiene pasajes violentos, pero el cuestionario pregunta por
  contenido *representado* —imágenes, escenas interactivas—, no por literatura.

**Público objetivo y contenido**
- Edades: **13 años en adelante** o «todos». No marques que va dirigida a niños:
  activa los requisitos de la política para familias, que exigen cosas que esta
  app no necesita.

**Declaraciones**
- Anuncios: **sí, contiene anuncios** — y hay que marcar la casilla en la ficha,
  porque Play pone la etiqueta «Contiene anuncios» junto al botón de instalar
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
