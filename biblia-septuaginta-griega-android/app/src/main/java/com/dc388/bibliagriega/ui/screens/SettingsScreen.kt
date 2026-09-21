package com.dc388.bibliagriega.ui.screens

import android.content.Intent
import android.net.Uri
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
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.semantics.Role
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dc388.bibliagriega.data.Anuncios
import com.dc388.bibliagriega.data.Compras
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
) {
    Column(Modifier.fillMaxWidth().padding(16.dp, 8.dp)) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.SpaceBetween,
        ) {
            Text(label, style = MaterialTheme.typography.bodyLarge)
            Text(
                text = "${(value * 100).toInt()}%",
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
