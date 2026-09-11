# Publicar en Google Play

> Nota: Google Play y App Store son tiendas distintas. Este repositorio genera
> el **AAB de Android** para **Google Play Console**
> (https://play.google.com/console). Para iOS haría falta un proyecto aparte
> compilado en macOS con Xcode.

## 1. Crear el almacén de claves (una sola vez)

La clave de firma es irrecuperable: si se pierde, no se puede actualizar la app.
Guárdala en un gestor de contraseñas y haz una copia de seguridad.

```bash
keytool -genkeypair -v \
  -keystore release.jks \
  -alias biblia-griega \
  -keyalg RSA -keysize 2048 -validity 10000
```

## 2. Configurar los secretos en GitHub

En el repositorio: **Settings → Secrets and variables → Actions → New repository secret**.

| Secreto | Valor |
|---|---|
| `KEYSTORE_BASE64` | salida de `base64 -w0 release.jks` |
| `KEYSTORE_PASSWORD` | contraseña del almacén |
| `KEY_ALIAS` | `biblia-griega` |
| `KEY_PASSWORD` | contraseña de la clave |

Para compilar firmado en local, en vez de secretos crea `app/keystore.properties`
(ya está en `.gitignore`):

```properties
storeFile=/ruta/absoluta/release.jks
storePassword=...
keyAlias=biblia-griega
keyPassword=...
```

## 3. Generar el AAB

```bash
git tag v1.0.0
git push origin v1.0.0
```

El flujo `release.yml` compila y adjunta `app-release.aab` a la GitHub Release.
También se puede lanzar a mano desde la pestaña **Actions → Release → Run workflow**.

## 4. Subirlo a Play Console

1. **Crear app** → nombre, idioma predeterminado español, gratuita.
2. **Versiones → Producción → Crear versión** y sube el `.aab`.
3. Deja activada la **firma de apps de Play** (Play Signing).

## 5. Ficha de Play Store

Los textos listos para copiar están en [FICHA_PLAY_STORE.md](FICHA_PLAY_STORE.md).

Recursos gráficos que pide Google:

| Recurso | Tamaño | Nota |
|---|---|---|
| Icono | 512 × 512 PNG | exportar de `docs/store/icono.svg` |
| Gráfico destacado | 1024 × 500 PNG | exportar de `docs/store/grafico-destacado.svg` |
| Capturas de teléfono | mín. 2, 1080 × 1920 | del emulador o de un dispositivo |

## 6. Seguridad de los datos

En **Contenido de la app → Seguridad de los datos**, declara:

- **¿La app recopila o comparte datos de usuario?** No.
- **¿Los datos se cifran en tránsito?** No aplica: la app no hace conexiones.
- **¿Se pueden solicitar la eliminación de los datos?** No aplica.

Es literalmente cierto: el manifiesto no declara ni un permiso, ni siquiera
`INTERNET`. Los marcadores y ajustes se guardan solo en el dispositivo.

## 7. Contenido de la app

- **Clasificación de contenido**: responde el cuestionario; una app de texto
  bíblico suele quedar como «Para todos».
- **Categoría**: Estilo de vida (o Libros y obras de consulta).
- **Política de privacidad**: es obligatoria una URL pública. Puedes publicar
  [PRIVACIDAD.md](PRIVACIDAD.md) en GitHub Pages y enlazar esa dirección.

## 8. Atribución de los textos

La Septuaginta de Swete está bajo CC BY-SA 4.0: la atribución tiene que ser
visible para el usuario. Ya lo está, en **Ajustes → Textos y licencias** dentro
de la app, y en `NOTICE.md`. No quites esa pantalla.
