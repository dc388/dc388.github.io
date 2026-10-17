# Traspaso — Biblia Griega y Hebrea

Todo lo que hace falta saber para seguir este proyecto sin haber estado en la
conversación donde se construyó. Escrito el 17 de octubre de 2026.

Dos avisos de método, porque el proyecto se ha llevado así y conviene seguir:

- **Medir, no opinar.** Si algo se puede contar —cobertura, contraste, bytes,
  píxeles— se cuenta y se da la cifra antes y después.
- **No fingir que algo está hecho.** Lo que no se ha comprobado se dice que no
  se ha comprobado. Hay cosas aquí marcadas como desconocidas a propósito.

---

## 1. Qué es

Una aplicación Android y un sitio web estático para estudiar la Biblia en sus
lenguas originales, en español.

| | |
|---|---|
| Repositorio | `dc388/dc388.github.io` |
| Rama de trabajo | `claude/biblia-septuaginta-android-repo-iyku9z` |
| Web | <https://dc388.github.io/biblia/> |
| Paquete Android | `com.dc388.bibliagriega` |
| Nombre en Play | Biblia Griega y Hebrea |
| Nombre bajo el icono | Biblia Griega (`app_name`) |

El contenido: **122 libros y 60 651 versículos**. La Septuaginta de Swete, el
Nuevo Testamento griego de Robinson-Pierpont, el Antiguo Testamento hebreo del
Códice de Leningrado, los Padres Apostólicos de Lake y varios pseudoepígrafos.
El Nuevo Testamento y el hebreo van interlineales, con número Strong y análisis
morfológico bajo cada palabra: **439 705 palabras analizadas**.

**La regla que manda sobre todas:** todo tiene que ser legible para un
hispanohablante. Es el motivo de la mitad del trabajo hecho.

---

## 2. Estado técnico

| | |
|---|---|
| Versión | **1.2.3** (`versionCode` 9) |
| Firma | clave real, en los secretos de GitHub Actions |
| Anuncios | AdMob con identificadores reales |
| Pruebas | 15 unitarias y 6 en emulador, en verde |
| Compilación de publicación | pasa, con R8 |
| Páginas web | 15 526, sin enlaces rotos |
| Léxico traducido al español | **11 898 de 14 610 artículos (81,4 %)** |

### Flujos de GitHub Actions

- **Pruebas — Biblia**: unitarias y de emulador.
- **Publicación — Biblia**: compila el AAB y el APK firmados en cada empujón.
- **APK para compartir**: publica el APK **y el AAB** en una release de GitHub.
  Saca la versión del propio binario con `aapt2` y comprueba la firma con
  `apksigner` antes de publicar nada. **Cuidado:** en `main` sigue la copia
  vieja de este flujo, que pisaría la release `biblia-apk-v3`. Mientras esta
  rama no se fusione, se lanza tocando el archivo y empujando, no desde el
  botón de Actions.

### Releases publicadas

- `biblia-apk-v9` — 1.2.3, la actual, con `.apk` y `.aab`
- `biblia-apk-v8`, `biblia-apk-v7` — anteriores
- `biblia-apk-v3` — 1.0.0, de septiembre, **no borrar**: tiene descargas

---

## 3. Lo que está a medias

### Variantes textuales del Nuevo Testamento

Lo más valioso que queda. El texto publicado es el Bizantino Mayoritario;
byztxt lo distribuye también con el aparato crítico incrustado:

```
τὸν Βοὸζ {NA Βοὸζ ἐκ > Βόες ἐκ } ἐκ τῆς Ῥαχάβ·
```

`tools/variantes.py` ya extrae eso, está comprobado y se audita solo. Medido
sobre los 27 libros que se publican:

```
versículos 7953   texto distinto al publicado: 0
variantes 7522   ancladas 7507   omiten o transponen 11   sin anclar 4
```

Que los 7 953 versículos limpios coincidan **carácter por carácter** con los
que la app ya muestra es lo que sostiene todo: cada variante sabe de qué
palabras exactas habla, sin alinear nada a ojo.

**Falta:** tabla `variants` en `tools/build_db.py`, interfaz en Android y en la
web. El dueño eligió **subrayado tenue bajo el tramo, que se toca la palabra**
— no subíndices volados, porque el 58,6 % de los versículos tienen variante y
el texto quedaría salpicado.

### Léxico

Faltan 2 712 artículos. Se añaden palabras a `tools/traducir_strong.py` y
siglas a `tools/traducir_articulo.py`.

**La disciplina no es negociable:** una palabra solo entra si tiene UNA
traducción buena en TODOS sus contextos. Si no, se queda fuera con el motivo
escrito en un comentario. Hay una docena así documentadas (`hit`, `coat`,
`doth`, `wilt`...). Al cerrar cada tanda se comprueba que todas las claves
planeadas están de verdad en la tabla: una vez se dieron seis por puestas sin
estarlo.

Ciclo completo: editar tablas → `rellenar_web.py ../../biblia/datos` →
`corregir_glosas.py ../../biblia` → `generar_palabras.py ../../biblia` →
`generar_paginas.py ../../biblia` → subir el sello de `biblia/datos/version.json`
→ auditar → confirmar y empujar. **El orden importa:** `rellenar_web` recalcula
las glosas, así que va antes de `corregir_glosas`.

### Auditoría de diseño

La **web ya está auditada**: los blancos táctiles pasaron de 22 px a 44 y el
borde de los controles de 1,26:1 a 3,12:1. El contraste del texto ya estaba en
AA o mejor en los seis pares de color.

La **app Android no**. Falta mirar los mínimos de 48 dp de Material, los tonos
del tema y la tipografía.

---

## 4. Google Play — aquí está el bloqueo

**Nada de esta sección se ha podido verificar desde las sesiones de Claude
Code:** `play.google.com` está bloqueado por el proxy. Todo lo que sigue viene
de capturas que mandó el dueño.

| | Punto | Estado |
|---|---|---|
| 1 | Acceso a producción | ❓ **solicitud enviada, resultado desconocido** |
| 2 | Estados Unidos en la lista de países | ❓ sin confirmar |
| 3 | Seguridad de los datos | ❓ sin confirmar |
| 4 | Verificación de desarrollador | ✅ **Registrada**, 14 sept |
| 5 | AdMob: perfil de pagos + formulario fiscal de EE. UU. | ❓ sin confirmar |

- **Prueba cerrada**: completada, 12 probadores, 14 días seguidos.
- **Prueba abierta**: canal activo, 178 países, con la versión 9 dentro.
- **Producción**: borrador creado con el AAB subido, sin lanzar.

**El punto 1 decide si hay registros de verdad.** La prueba abierta no aparece
en el buscador de Play y exige aceptar ser probador antes de instalar: por
mucho que se ajusten los países, de ahí no salen instalaciones en volumen.

**El punto 5 decide si se cobra.** Sin perfil de pagos los anuncios se sirven y
no ingresan nada; sin el formulario fiscal se retiene lo que generen los
usuarios estadounidenses.

### Respuestas listas para «Seguridad de los datos»

- ¿Recopila o comparte datos? **Sí**
- **ID de publicidad**: se recopila **sí**, se comparte **sí**, obligatorio
  **no** (la suscripción lo quita), finalidad **publicidad o marketing**
- **Ubicación aproximada**: se recopila **sí**, se comparte **sí**, finalidad
  **publicidad**. Es la que AdMob deduce de la IP; la app no pide permiso de
  ubicación.
- Cifrado en tránsito **sí**. Se puede solicitar la eliminación **sí** (borrando
  el ID de publicidad en Ajustes de Android).
- **No declarar** notas, marcadores, posición de lectura ni preferencias: no
  salen del teléfono. Declarar de más también da problemas.

### Dos usuarias esperando

- **Susana, Estados Unidos**: recibe «no está disponible en tu país» abriendo
  el enlace directo. Eso es disponibilidad por país, no un problema de
  búsqueda. O EE. UU. no está marcado, o el país de su cuenta de Google no es
  EE. UU. (Play mira el país de la cuenta, no dónde está el teléfono).
- **Dayanis, Cuba**: **no tiene arreglo por Play.** Google Play no opera en
  Cuba; el país ni siquiera aparece en la lista. La única vía es mandarle el
  APK como archivo, por Telegram.

**Un APK instalado a mano no cuenta como instalación en Play**, no suma a las
estadísticas ni al posicionamiento. Sirve para que esas dos personas lean hoy,
no como plan de difusión.

---

## 5. Reglas que no se rompen

- Desarrollar, confirmar y empujar **solo** en
  `claude/biblia-septuaginta-android-repo-iyku9z`. Nunca `main`.
- **No abrir pull requests** sin que el dueño lo pida.
- Nunca confirmar `app/keystore.properties`, `*.jks` ni `*.keystore`. Los
  secretos de firma viven solo en los secretos de GitHub Actions.
- **No publicar releases de GitHub** sin permiso: eso sale hacia fuera.
- No poner identificadores de modelo en commits, código ni nada que se empuje.
- Al empezar una sesión: `git fetch` y `git reset --hard` al origen de la rama.
  El contenedor vuelve a veces con la rama apuntando a otro sitio.
- Mensajes de commit en español, explicando **por qué**, no solo qué.

---

## 6. Qué puede hacer quién

**Lo que una sesión de Claude Code puede hacer:** todo el código, los datos,
la web, los flujos de Actions, las releases de GitHub (con permiso).

**Lo que no puede, y no debe fingir:** entrar en Google Play Console o AdMob.
Exigen la cuenta, la identidad verificada y la firma legal del dueño. Tampoco
puede ver su navegador ni su pantalla: solo las capturas que él mande.

**Lo que sí puede hacerlo:** la extensión de Claude para Chrome, que corre en
su navegador con su sesión ya iniciada. Ahí no hacen falta credenciales
—ya está dentro— y nada sale de su máquina.

**Rutina en marcha:** «Biblia Griega — trabajo continuo», cada 6 horas, abre
una sesión nueva que sigue con CI, variantes, léxico, diseño y documentación.
