# Grupos de estudio — plan para la versión 1.1

Salas donde varias personas leen el mismo pasaje y lo comentan. Se decide
dejarlo para después de publicar la 1.0: meterlo antes obligaba a rehacer los
formularios de Play y a reiniciar la revisión, con la app ya probada y lista.

Esto no es una función que se active: es un servicio. La 1.0 no tiene servidor
ni cuentas, y no pide ni un permiso.

## Lo que cambia, y conviene saberlo antes de empezar

**La app deja de funcionar sin conexión para esta parte.** Hay que declarar el
permiso `INTERNET` en el manifiesto. La lectura, el interlineal y el léxico
siguen funcionando sin red —eso no cambia—, pero el argumento «no pide ni un
permiso» se pierde, y es hoy lo que la distingue de las demás biblias de Play.

**La app pasa a recoger datos.** Identificador de cuenta, mensajes y a qué
grupo pertenece cada uno. Hay que rehacer la declaración de Seguridad de los
datos, reescribir la política de privacidad publicada y actualizar la pantalla
de Ajustes, que hoy dice que no se recoge nada.

**Google exige cuatro cosas para el contenido generado por usuarios**, y sin
ellas rechaza la app:

1. un sistema de moderación;
2. un botón para denunciar mensajes, visible en cada mensaje;
3. poder bloquear a otro usuario;
4. términos de servicio aceptados al entrar.

**La clasificación de contenido sube.** El cuestionario pregunta si la app
permite comunicación entre usuarios; con chat sin moderación previa, la edad
mínima cambia y hay que rellenarlo otra vez.

## Cómo montarlo

La vía más corta es **Firebase**, que resuelve de una vez lo que si no habría
que programar y hospedar:

- **Authentication** — entrar con Google o de forma anónima. Sin contraseñas
  propias, que son un problema de seguridad que no merece la pena tener.
- **Firestore** — los grupos y los mensajes. Se sincroniza solo y funciona con
  el teléfono sin cobertura, guardando lo escrito hasta que vuelva.
- **Cloud Messaging** — avisar de un mensaje nuevo.
- **Cloud Functions** — la moderación: filtrar lo denunciado, aplicar bloqueos.

La alternativa es **Supabase**, que es Postgres y se puede llevar uno mismo si
no se quiere depender de Google. Firebase encaja mejor aquí porque el modo sin
conexión ya viene resuelto y porque la cuenta de Play ya es de Google.

### Datos

```
grupos/{grupoId}
  nombre, creadoPor, creado, miembros[], pasaje
  mensajes/{mensajeId}
    autor, texto, enviado, versiculo?, denunciado?
usuarios/{uid}
  nombre, bloqueados[]
```

El pasaje es lo que hace que sea un grupo de estudio y no un chat: la sala
apunta a un libro y capítulo, y quien entra abre ahí la lectura. Un mensaje
puede colgar de un versículo concreto, y entonces aparece marcado al leerlo.

### Reglas de seguridad

Escribirlas antes que la interfaz. Firestore abierto es una filtración de
datos, y es el error más común al empezar con Firebase:

- un usuario solo lee los grupos de los que es miembro;
- solo escribe mensajes como él mismo;
- nadie edita ni borra mensajes de otro;
- los bloqueos los aplica el servidor, no el teléfono.

## Coste

La capa gratuita de Firebase (plan Spark) cubre de sobra un grupo de amigos:
50 000 lecturas y 20 000 escrituras al día. Con cientos de usuarios activos hay
que pasar al plan de pago, que cobra por uso. Conviene ponerse un límite de
gasto desde el primer día: sin él, un fallo en bucle puede costar dinero de
verdad.

## Orden de trabajo

1. Proyecto de Firebase y `google-services.json` —lo crea el dueño de la cuenta,
   no se versiona—.
2. Reglas de seguridad y modelo de datos.
3. Entrar con Google, y poder usar la app sin entrar: quien no quiera grupos no
   debería tener que identificarse para leer.
4. Grupos: crear, invitar por enlace, entrar, salir.
5. Mensajes anclados a un versículo.
6. Denunciar, bloquear y moderación.
7. Términos de servicio y política de privacidad nuevas.
8. Rehacer en Play: Seguridad de los datos, clasificación de contenido y ficha.

Los puntos 6 y 7 no son el final: son lo que decide si Google aprueba la
actualización. Conviene tenerlos escritos antes de empezar el 4.
