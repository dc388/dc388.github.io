package com.dc388.bibliagriega.ui.screens

import android.Manifest
import android.content.Intent
import android.net.Uri
import android.os.Build
import android.provider.Settings as AjustesDeAndroid
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.selection.toggleable
import androidx.compose.foundation.verticalScroll
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material3.Button
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SegmentedButton
import androidx.compose.material3.SegmentedButtonDefaults
import androidx.compose.material3.SingleChoiceSegmentedButtonRow
import androidx.compose.material3.Slider
import androidx.compose.material3.Switch
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.lifecycle.Lifecycle
import androidx.lifecycle.compose.LifecycleEventEffect
import com.dc388.bibliagriega.data.Anuncios
import com.dc388.bibliagriega.data.AvisoDiario
import com.dc388.bibliagriega.data.Compras
import com.dc388.bibliagriega.data.Settings
import com.dc388.bibliagriega.data.ThemeMode
import com.dc388.bibliagriega.ui.actividad
import com.dc388.bibliagriega.ui.columna
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

private const val SAMPLE = "Ἐν ἀρχῇ ἦν ὁ λόγος, καὶ ὁ λόγος ἦν πρὸς τὸν θεόν."

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SettingsScreen(vm: BibliaViewModel, onBack: () -> Unit) {
    val settings by vm.settings.collectAsState()
    val library by vm.library.collectAsState()
    val context = LocalContext.current
    val compras = remember(context) { Compras.get(context) }
    val sinAnuncios by compras.sinAnuncios.collectAsState()
    val precio by compras.precio.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Ajustes") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Atrás")
                    }
                },
            )
        },
    ) { padding ->
        Column(
            modifier = Modifier
                .columna()
                .padding(padding)
                .verticalScroll(rememberScrollState())
                .padding(bottom = 32.dp),
        ) {
            SectionTitle("Anuncios")
            Suscripcion(
                sinAnuncios = sinAnuncios,
                precio = precio,
                onSuscribirse = { context.actividad()?.let(compras::suscribirse) },
                onGestionar = {
                    context.startActivity(
                        Intent(
                            Intent.ACTION_VIEW,
                            Uri.parse(
                                "https://play.google.com/store/account/subscriptions" +
                                    "?sku=${Anuncios.SUSCRIPCION_SIN_ANUNCIOS}" +
                                    "&package=${context.packageName}",
                            ),
                        ),
                    )
                },
            )

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 8.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )
            SectionTitle("Lectura")

            Card(
                modifier = Modifier.fillMaxWidth().padding(16.dp, 4.dp),
                colors = CardDefaults.cardColors(
                    containerColor = MaterialTheme.colorScheme.surfaceVariant,
                ),
            ) {
                Text(
                    text = SAMPLE,
                    fontFamily = ScriptureFontFamily,
                    fontSize = (18 * settings.fontScale).sp,
                    lineHeight = (30 * settings.fontScale * settings.lineHeightScale).sp,
                    modifier = Modifier.padding(16.dp),
                )
            }

            LabeledSlider(
                label = "Tamaño de letra",
                value = settings.fontScale,
                range = 0.8f..2.0f,
                steps = 11,
                onChange = vm::setFontScale,
            )
            LabeledSlider(
                label = "Interlineado",
                value = settings.lineHeightScale,
                range = 0.9f..1.8f,
                steps = 8,
                onChange = vm::setLineHeightScale,
            )

            SwitchRow(
                label = "Mostrar números de versículo",
                checked = settings.showVerseNumbers,
                onChange = vm::setShowVerseNumbers,
            )
            SwitchRow(
                label = "Modo interlineal",
                description = "Muestra cada palabra con su transliteración, su definición " +
                    "breve y su número Strong; al tocarla se abre el léxico. Disponible en " +
                    "el Nuevo Testamento y en el Antiguo Testamento hebreo.",
                checked = settings.interlinear,
                onChange = vm::setInterlinear,
            )
            SwitchRow(
                label = "Traducción al español",
                description = "Pone la Reina-Valera de 1909 debajo de cada versículo. No está " +
                    "en la Septuaginta: la Reina-Valera traduce del hebreo y la numeración de " +
                    "la Septuaginta no cuadra con la suya.",
                checked = settings.translation,
                onChange = vm::setTranslation,
            )
            SwitchRow(
                label = "Texto corrido",
                description = "Une los versículos en párrafo, como en las ediciones críticas.",
                checked = settings.paragraphMode,
                onChange = vm::setParagraphMode,
            )

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 8.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )
            SectionTitle("Versículo del día")
            AvisoDeCadaManana(vm = vm, settings = settings)

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 8.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )
            SectionTitle("Apariencia")

            SingleChoiceSegmentedButtonRow(
                modifier = Modifier.fillMaxWidth().padding(16.dp, 4.dp),
            ) {
                val modes = listOf(
                    ThemeMode.SYSTEM to "Sistema",
                    ThemeMode.LIGHT to "Claro",
                    ThemeMode.DARK to "Oscuro",
                )
                modes.forEachIndexed { index, (mode, label) ->
                    SegmentedButton(
                        selected = settings.theme == mode,
                        onClick = { vm.setTheme(mode) },
                        shape = SegmentedButtonDefaults.itemShape(index, modes.size),
                    ) { Text(label) }
                }
            }

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 8.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )
            SectionTitle("Textos y licencias")

            library.collections.forEach { collection ->
                Column(Modifier.fillMaxWidth().padding(16.dp, 8.dp)) {
                    Text(collection.name, style = MaterialTheme.typography.titleMedium)
                    Text(
                        text = collection.edition,
                        style = MaterialTheme.typography.bodyMedium,
                    )
                    Text(
                        text = collection.license,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                    Text(
                        text = collection.sourceUrl,
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }

            Column(Modifier.fillMaxWidth().padding(16.dp, 8.dp)) {
                Text("Traducción al español", style = MaterialTheme.typography.titleMedium)
                Text(
                    text = "Reina-Valera 1909",
                    style = MaterialTheme.typography.bodyMedium,
                )
                Text(
                    text = "Dominio público — https://github.com/seven1m/open-bibles",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }

            Column(Modifier.fillMaxWidth().padding(16.dp, 8.dp)) {
                Text("Léxico y análisis morfológico", style = MaterialTheme.typography.titleMedium)
                Text(
                    text = "Diccionario Strong (1890), Open Scriptures",
                    style = MaterialTheme.typography.bodyMedium,
                )
                Text(
                    text = "CC BY-SA — https://github.com/openscriptures/strongs",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                Text(
                    text = "Análisis morfológico de Robinson, dominio público, traducido al " +
                        "español por este proyecto, que traduce también la definición de " +
                        "los 1 196 lemas más frecuentes —el 85 % de las palabras del Nuevo " +
                        "Testamento y el 75 % del Antiguo— y la procedencia de la palabra.",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }

            Text(
                text = "Eclesiastés procede de la tradición Rahlfs porque la edición de Swete " +
                    "aún no está digitalizada para ese libro.",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.padding(16.dp, 4.dp),
            )
            Text(
                text = "La Biblia, el léxico y la traducción están dentro de la aplicación y " +
                    "se leen sin conexión. La red solo se usa para dos cosas: traer los " +
                    "anuncios y preguntarle a Google Play si la suscripción está activa. " +
                    "Los anuncios los sirve Google AdMob, que para elegirlos recibe datos " +
                    "de tu dispositivo; lo que lees, tus notas y tus marcadores no salen " +
                    "del teléfono. Con la suscripción activa no se carga ningún anuncio.",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.padding(16.dp, 8.dp),
            )
        }
    }
}

@Composable
private fun Suscripcion(
    sinAnuncios: Boolean,
    precio: String?,
    onSuscribirse: () -> Unit,
    onGestionar: () -> Unit,
) {
    Card(
        modifier = Modifier.fillMaxWidth().padding(16.dp, 4.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceVariant,
        ),
    ) {
        Column(Modifier.padding(16.dp)) {
            if (sinAnuncios) {
                Text("Suscripción activa", style = MaterialTheme.typography.titleMedium)
                Text(
                    text = "No verás anuncios. La suscripción se renueva y se cancela " +
                        "desde Google Play.",
                    style = MaterialTheme.typography.bodyMedium,
                )
                TextButton(onClick = onGestionar) { Text("Gestionar en Google Play") }
            } else {
                Text("Quitar los anuncios", style = MaterialTheme.typography.titleMedium)
                Text(
                    text = "La aplicación es gratuita y se sostiene con un anuncio al pie " +
                        "del lector. Con la suscripción desaparece y no se carga ninguno.",
                    style = MaterialTheme.typography.bodyMedium,
                )
                Button(
                    onClick = onSuscribirse,
                    enabled = precio != null,
                    modifier = Modifier.padding(top = 12.dp),
                ) {
                    // Sin precio es que Play aún no ha contestado o que no hay Play:
                    // más vale un botón apagado que un botón que no hace nada.
                    Text(
                        if (precio != null) "Suscribirme por $precio al mes"
                        else "Consultando el precio en Google Play…",
                    )
                }
            }
        }
    }
}

/**
 * El interruptor del aviso de la mañana y la hora a la que sale.
 *
 * Esto tiene más esquinas de las que parece. Desde Android 13 encenderlo no
 * basta: hay que pedirle el permiso al usuario, y el sistema solo deja
 * preguntar una vez —si lo niega, la siguiente petición vuelve negada sin
 * enseñar nada—. Y en cualquier versión de Android el usuario puede apagar los
 * avisos de la aplicación desde los ajustes del sistema, donde tampoco hay
 * permiso que pedir.
 *
 * De ahí las dos reglas: el interruptor no se queda encendido hasta que el
 * aviso puede salir de verdad, y **tocarlo nunca se queda sin hacer nada**. Si
 * no queda nada que preguntar, se abren los ajustes de Android, que es el único
 * sitio donde eso se deshace. Al volver de ahí se vuelve a mirar el permiso:
 * nada recompone por sí solo, y sin eso el interruptor se quedaba apagado
 * después de que el usuario lo acabara de desbloquear.
 */
@Composable
private fun AvisoDeCadaManana(vm: BibliaViewModel, settings: Settings) {
    val context = LocalContext.current
    var permiso by remember { mutableStateOf(AvisoDiario.hayPermiso(context)) }
    var yaPreguntado by rememberSaveable { mutableStateOf(false) }

    LifecycleEventEffect(Lifecycle.Event.ON_RESUME) {
        permiso = AvisoDiario.hayPermiso(context)
    }

    val pedirPermiso = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission(),
    ) {
        yaPreguntado = true
        permiso = AvisoDiario.hayPermiso(context)
        if (permiso) vm.setAvisoDiario(true)
    }

    fun abrirLosAjustesDeAndroid() {
        context.startActivity(
            Intent(AjustesDeAndroid.ACTION_APP_NOTIFICATION_SETTINGS)
                .putExtra(AjustesDeAndroid.EXTRA_APP_PACKAGE, context.packageName),
        )
    }

    SwitchRow(
        label = "Avisarme cada mañana",
        description = "Un versículo al día con la palabra del griego o del hebreo que lo " +
            "sostiene, y qué dice esa palabra. Se puede compartir desde el propio aviso.",
        checked = settings.avisoDiario && permiso,
        onChange = { encender ->
            when {
                !encender -> vm.setAvisoDiario(false)
                permiso -> vm.setAvisoDiario(true)
                Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU && !yaPreguntado ->
                    pedirPermiso.launch(Manifest.permission.POST_NOTIFICATIONS)
                else -> abrirLosAjustesDeAndroid()
            }
        },
    )

    if (settings.avisoDiario && permiso) {
        LabeledSlider(
            label = "Hora del aviso",
            value = settings.horaAviso.toFloat(),
            range = 5f..22f,
            steps = 16,
            formato = { "${it.toInt()}:00" },
            onChange = { vm.setHoraAviso(it.toInt()) },
        )
        Text(
            text = "Puede salir hasta media hora más tarde. Una alarma exacta hay que " +
                "pedírsela al sistema, y Google Play solo se la concede a los " +
                "despertadores y a los calendarios.",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
            modifier = Modifier.padding(16.dp, 0.dp, 16.dp, 8.dp),
        )
    }

    if ((settings.avisoDiario || yaPreguntado) && !permiso) {
        Text(
            text = "Android tiene bloqueados los avisos de esta aplicación, así que no " +
                "puede salir ninguno. Se desbloquea en los ajustes del sistema.",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.error,
            modifier = Modifier.padding(16.dp, 0.dp, 16.dp, 0.dp),
        )
        TextButton(
            onClick = { abrirLosAjustesDeAndroid() },
            modifier = Modifier.padding(horizontal = 8.dp),
        ) { Text("Abrir los ajustes de Android") }
    }
}

@Composable
private fun SectionTitle(text: String) {
    Text(
        text = text,
        style = MaterialTheme.typography.titleMedium,
        fontWeight = FontWeight.SemiBold,
        color = MaterialTheme.colorScheme.secondary,
        modifier = Modifier.padding(16.dp, 16.dp, 16.dp, 4.dp),
    )
}

@Composable
private fun LabeledSlider(
    label: String,
    value: Float,
    range: ClosedFloatingPointRange<Float>,
    steps: Int,
    onChange: (Float) -> Unit,
    formato: (Float) -> String = { "${(it * 100).toInt()}%" },
) {
    Column(Modifier.fillMaxWidth().padding(16.dp, 8.dp)) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
        ) {
            Text(label, style = MaterialTheme.typography.bodyLarge)
            Text(
                text = formato(value),
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Slider(
            value = value,
            onValueChange = onChange,
            valueRange = range,
            steps = steps,
        )
    }
}

@Composable
private fun SwitchRow(
    label: String,
    description: String? = null,
    checked: Boolean,
    onChange: (Boolean) -> Unit,
) {
    Row(
        // Toda la fila conmuta, no solo el interruptor: el texto explicativo
        // ocupa tres líneas y quien lo lee toca ahí, no a treinta píxeles a la
        // derecha. Es además lo que hace Material y lo que espera cualquiera.
        modifier = Modifier
            .fillMaxWidth()
            .toggleable(
                value = checked,
                role = Role.Switch,
                onValueChange = onChange,
            )
            .padding(16.dp, 10.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Column(Modifier.weight(1f)) {
            Text(label, style = MaterialTheme.typography.bodyLarge)
            if (description != null) {
                Text(
                    text = description,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
        }
        Switch(checked = checked, onCheckedChange = null)
    }
}
