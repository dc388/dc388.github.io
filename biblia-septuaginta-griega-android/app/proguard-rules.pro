# El código propio no usa reflexión. Las dependencias sí, y eso no se ve hasta
# que la aplicación se abre en un teléfono con la compilación de publicación.
#
# Esto costó una versión rota en producción: la aplicación compilaba, se
# firmaba, se subía a Play, se instalaba, y se cerraba sola al tocar el icono.
# El volcado decía:
#
#     FATAL EXCEPTION: main
#     Caused by: vs: java.lang.RuntimeException:
#         Failed to create an instance of androidx.work.impl.WorkDatabase
#
# Ese «vs» es el nombre al que R8 renombró la clase, y ahí está el fallo
# entero: Room no construye la implementación de una base de datos llamándola
# por su nombre, la BUSCA por reflexión con el nombre de la clase más el
# sufijo «_Impl». Si R8 la renombra, la búsqueda no encuentra nada y lo que
# sale es una excepción en el arranque.
#
# WorkManager no se usa en este proyecto directamente: entra arrastrado por el
# SDK de anuncios, que lo usa para sus tareas en segundo plano. Por eso nadie
# lo tenía en la cabeza al escribir estas reglas.

# Se conservan los nombres de los modelos por claridad en los reportes de fallos.
-keep class com.dc388.bibliagriega.data.** { *; }

# Room: la implementación generada de cada base de datos se localiza por
# reflexión, así que su nombre no se puede tocar.
-keep class * extends androidx.room.RoomDatabase { <init>(); }
-keep class **_Impl { <init>(...); }

# WorkManager instancia cada tarea por el nombre de su clase, leído de su
# propia base de datos. Es la misma clase de fallo que el anterior, solo que
# aparecería más tarde —al ejecutarse la tarea— y no al arrancar.
-keep class * extends androidx.work.ListenableWorker { <init>(...); }
