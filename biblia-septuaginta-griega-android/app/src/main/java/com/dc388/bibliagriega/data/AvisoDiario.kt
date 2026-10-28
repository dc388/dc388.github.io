package com.dc388.bibliagriega.data

import android.Manifest
import android.annotation.SuppressLint
import android.app.AlarmManager
import android.app.NotificationChannel
import android.app.NotificationManager
import android.app.PendingIntent
import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.pm.PackageManager
import android.os.Build
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat
import androidx.core.content.ContextCompat
import com.dc388.bibliagriega.MainActivity
import com.dc388.bibliagriega.R
import com.dc388.bibliagriega.ui.Compartir
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.launch
import java.time.LocalDate
import java.time.ZonedDateTime

/**
 * El aviso de cada mañana con el versículo del día.
 *
 * **Por qué AlarmManager y no WorkManager.** WorkManager es lo que se usa para
 * trabajo que tiene que acabar; esto es un aviso que tiene que *salir a una
 * hora*. Un trabajo aplazado media mañana no sirve de nada, y la alarma
 * tampoco añade una dependencia más al proyecto. La ventana es ancha a
 * propósito —media hora— porque una alarma exacta exige el permiso
 * `SCHEDULE_EXACT_ALARM`, que Google Play solo concede a despertadores y
 * calendarios; pedirlo para esto sería motivo de rechazo.
 *
 * Cada disparo vuelve a programar el siguiente, así que la hora no se va
 * corriendo aunque el sistema retrase un aviso. Si el teléfono se reinicia,
 * Android borra las alarmas: por eso el receptor escucha también el arranque,
 * y la aplicación reprograma al abrirse.
 *
 * El aviso lleva dentro todo lo que hay que leer: el versículo en español, la
 * palabra del original y qué dice esa palabra. Quien lo despliega ya ha
 * estudiado algo sin entrar; quien quiera más, toca.
 */
object AvisoDiario {

    /** La alarma propia. El receptor la distingue del arranque del sistema. */
    const val ACCION = "com.dc388.bibliagriega.AVISO_DIARIO"

    const val EXTRA_COLECCION = "aviso_coleccion"
    const val EXTRA_CODIGO = "aviso_codigo"
    const val EXTRA_CAPITULO = "aviso_capitulo"

    private const val CANAL = "versiculo_del_dia"
    private const val AVISO = 1001

    /** Media hora de margen: ver arriba, es lo que evita pedir alarma exacta. */
    private const val VENTANA = 30L * 60 * 1000

    /**
     * Deja programado el próximo aviso. Si la hora de hoy ya pasó, el de mañana.
     *
     * Se puede llamar las veces que haga falta: la alarma es única y la última
     * llamada sustituye a la anterior.
     */
    fun programar(contexto: Context, hora: Int) {
        val gestor = contexto.getSystemService(AlarmManager::class.java) ?: return
        val ahora = ZonedDateTime.now()
        var cuando = ahora.toLocalDate().atTime(hora.coerceIn(0, 23), 0).atZone(ahora.zone)
        if (!cuando.isAfter(ahora)) cuando = cuando.plusDays(1)
        gestor.setWindow(
            AlarmManager.RTC_WAKEUP,
            cuando.toInstant().toEpochMilli(),
            VENTANA,
            alarma(contexto),
        )
    }

    fun cancelar(contexto: Context) {
        contexto.getSystemService(AlarmManager::class.java)?.cancel(alarma(contexto))
        NotificationManagerCompat.from(contexto).cancel(AVISO)
    }

    /**
     * Si el aviso puede salir de verdad: el permiso de Android 13 concedido y
     * los avisos de la aplicación no apagados en los ajustes del sistema.
     */
    fun hayPermiso(contexto: Context): Boolean {
        val concedido = Build.VERSION.SDK_INT < Build.VERSION_CODES.TIRAMISU ||
            ContextCompat.checkSelfPermission(contexto, Manifest.permission.POST_NOTIFICATIONS) ==
            PackageManager.PERMISSION_GRANTED
        // El permiso no es lo único: en cualquier versión de Android el usuario
        // puede apagar los avisos de la aplicación desde los ajustes del
        // sistema, y entonces no sale ninguno aunque el permiso esté dado.
        return concedido && NotificationManagerCompat.from(contexto).areNotificationsEnabled()
    }

    /** El mensaje tal como sale a WhatsApp cuando alguien lo comparte. */
    fun paraCompartir(v: VersiculoDiario): String = Compartir.versiculo(
        referencia = v.referencia,
        original = v.original,
        espanol = v.espanol,
        reflexion = "${v.palabra} · ${v.translit}\n${v.reflexion}",
    )

    // El permiso se comprueba en la primera línea, pero el analizador no sigue
    // la llamada a hayPermiso y marcaría la notificación como permiso ausente.
    @SuppressLint("MissingPermission")
    fun mostrar(contexto: Context, v: VersiculoDiario) {
        if (!hayPermiso(contexto)) return
        canal(contexto)

        // El cuerpo desplegado es el aviso entero: versículo, palabra y qué dice
        // esa palabra. Una línea en blanco separa el texto del análisis para que
        // se lean como dos cosas distintas y no como un párrafo largo.
        val cuerpo = buildString {
            append(v.espanol)
            append("\n\n")
            append(v.palabra).append("   ").append(v.translit)
            append("\n")
            append(v.reflexion)
        }

        val aviso = NotificationCompat.Builder(contexto, CANAL)
            .setSmallIcon(R.drawable.ic_aviso)
            .setColor(ContextCompat.getColor(contexto, R.color.aviso))
            .setContentTitle(v.referencia)
            .setContentText(v.espanol)
            .setSubText("Versículo del día")
            .setStyle(
                NotificationCompat.BigTextStyle()
                    .setBigContentTitle(v.referencia)
                    .bigText(cuerpo),
            )
            .setContentIntent(abrirLector(contexto, v))
            .addAction(R.drawable.ic_aviso, "Leer", abrirLector(contexto, v))
            .addAction(R.drawable.ic_aviso, "Compartir", compartir(contexto, v))
            .setCategory(NotificationCompat.CATEGORY_REMINDER)
            .setPriority(NotificationCompat.PRIORITY_DEFAULT)
            .setAutoCancel(true)
            .build()

        // Con el permiso comprobado arriba esto no lanza, pero el analizador no
        // lo sabe y un aviso no vale una caída.
        runCatching { NotificationManagerCompat.from(contexto).notify(AVISO, aviso) }
    }

    private fun canal(contexto: Context) {
        if (Build.VERSION.SDK_INT < Build.VERSION_CODES.O) return
        val canal = NotificationChannel(
            CANAL,
            "Versículo del día",
            NotificationManager.IMPORTANCE_DEFAULT,
        ).apply {
            description = "Un versículo cada mañana, con la palabra del griego o del " +
                "hebreo que lo sostiene."
            setShowBadge(true)
        }
        contexto.getSystemService(NotificationManager::class.java)
            ?.createNotificationChannel(canal)
    }

    private fun alarma(contexto: Context): PendingIntent = PendingIntent.getBroadcast(
        contexto,
        0,
        Intent(contexto, ReceptorDelAviso::class.java).setAction(ACCION),
        PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
    )

    private fun abrirLector(contexto: Context, v: VersiculoDiario): PendingIntent {
        val intento = Intent(contexto, MainActivity::class.java)
            .setFlags(Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TOP)
            .putExtra(EXTRA_COLECCION, v.coleccion)
            .putExtra(EXTRA_CODIGO, v.codigo)
            .putExtra(EXTRA_CAPITULO, v.capitulo)
        return PendingIntent.getActivity(
            contexto,
            1,
            intento,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
        )
    }

    private fun compartir(contexto: Context, v: VersiculoDiario): PendingIntent {
        val envio = Intent(Intent.ACTION_SEND)
            .setType("text/plain")
            .putExtra(Intent.EXTRA_TEXT, paraCompartir(v))
        val selector = Intent.createChooser(envio, "Compartir el versículo")
            .addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        return PendingIntent.getActivity(
            contexto,
            2,
            selector,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
        )
    }
}

/**
 * Quien recibe la alarma de la mañana y el arranque del sistema.
 *
 * Está declarado como exportado porque si no, Android no le entrega
 * `BOOT_COMPLETED`. Lo único que puede provocar quien lo llame desde fuera es
 * que salga el aviso del día, y solo si el usuario lo tiene activado: no hay
 * nada más que hacer aquí.
 */
class ReceptorDelAviso : BroadcastReceiver() {
    override fun onReceive(contexto: Context, intento: Intent) {
        // Leer los ajustes es asíncrono y onReceive no lo es: goAsync mantiene
        // vivo el proceso los segundos que tarda.
        val pendiente = goAsync()
        val app = contexto.applicationContext
        CoroutineScope(Dispatchers.Default).launch {
            try {
                val ajustes = Prefs.get(app).settings.first()
                if (ajustes.avisoDiario) {
                    if (intento.action == AvisoDiario.ACCION) {
                        AvisoDiario.mostrar(app, VersiculoDelDia.de(LocalDate.now()))
                    }
                    // Siempre: el disparo de hoy deja puesto el de mañana, y el
                    // reinicio del teléfono borra las alarmas.
                    AvisoDiario.programar(app, ajustes.horaAviso)
                }
            } finally {
                pendiente.finish()
            }
        }
    }
}
