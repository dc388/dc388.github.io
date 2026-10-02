package com.dc388.bibliagriega.ui.screens

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.ExperimentalLayoutApi
import androidx.compose.foundation.layout.FlowRow
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dc388.bibliagriega.data.InterlinearWord
import com.dc388.bibliagriega.ui.PlainWordStudy
import com.dc388.bibliagriega.ui.WordStudy
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

/**
 * Interlineal: cada palabra sobre su transliteración, su definición breve —donde
 * la hay— y su número Strong. Al tocarla se abre su entrada del léxico.
 */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun InterlinearVerse(
    words: List<InterlinearWord>,
    fontSizeSp: Float,
    onWordClick: (InterlinearWord) -> Unit,
    modifier: Modifier = Modifier,
) {
    FlowRow(
        modifier = modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(10.dp),
        verticalArrangement = Arrangement.spacedBy(6.dp),
    ) {
        words.forEach { word ->
            Column(
                modifier = Modifier
                    .clickable { onWordClick(word) }
                    .padding(vertical = 2.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
            ) {
                Text(
                    text = word.surface,
                    fontFamily = ScriptureFontFamily,
                    fontSize = fontSizeSp.sp,
                    color = MaterialTheme.colorScheme.onBackground,
                )
                if (word.transliteration != null) {
                    Text(
                        text = word.transliteration,
                        fontSize = (fontSizeSp * 0.58f).sp,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        textAlign = TextAlign.Center,
                    )
                }
                if (word.gloss != null) {
                    Text(
                        text = word.gloss,
                        fontSize = (fontSizeSp * 0.55f).sp,
                        color = MaterialTheme.colorScheme.onSurface,
                        textAlign = TextAlign.Center,
                        modifier = Modifier.widthIn(max = 140.dp),
                    )
                }
                Text(
                    text = word.strong,
                    fontSize = (fontSizeSp * 0.52f).sp,
                    color = MaterialTheme.colorScheme.secondary,
                    fontWeight = FontWeight.Medium,
                )
            }
        }
    }
}

/** Fila de palabras tocables para analizar un versículo sin salir del modo lectura. */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun WordChips(
    words: List<InterlinearWord>,
    onWordClick: (InterlinearWord) -> Unit,
    modifier: Modifier = Modifier,
) {
    FlowRow(
        modifier = modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(6.dp),
        verticalArrangement = Arrangement.spacedBy(6.dp),
    ) {
        words.forEach { word ->
            Surface(
                shape = RoundedCornerShape(8.dp),
                color = MaterialTheme.colorScheme.surfaceVariant,
                modifier = Modifier.clickable { onWordClick(word) },
            ) {
                Text(
                    text = word.surface,
                    fontFamily = ScriptureFontFamily,
                    style = MaterialTheme.typography.bodyMedium,
                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 5.dp),
                )
            }
        }
    }
}

/** Panel con lema, transliteración, morfología y definición de una palabra. */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun WordStudySheet(
    study: WordStudy,
    onDismiss: () -> Unit,
    onOpenConcordance: (strong: String, lemma: String) -> Unit,
) {
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)
    val entry = study.entry

    ModalBottomSheet(onDismissRequest = onDismiss, sheetState = sheetState) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
                .padding(20.dp, 0.dp, 20.dp, 32.dp),
        ) {
            Text(
                text = study.word.surface,
                fontFamily = ScriptureFontFamily,
                fontSize = 30.sp,
                color = MaterialTheme.colorScheme.onSurface,
            )
            Text(
                text = study.reference,
                style = MaterialTheme.typography.labelLarge,
                color = MaterialTheme.colorScheme.secondary,
            )

            if (study.loading) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(vertical = 24.dp),
                    horizontalArrangement = Arrangement.Center,
                ) { CircularProgressIndicator() }
                return@Column
            }

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 14.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )

            if (entry != null) {
                Row(verticalAlignment = Alignment.Bottom) {
                    Text(
                        text = entry.lemma,
                        fontFamily = ScriptureFontFamily,
                        style = MaterialTheme.typography.titleLarge,
                    )
                    if (entry.transliteration != null) {
                        Text(
                            text = "  ${entry.transliteration}",
                            style = MaterialTheme.typography.bodyMedium,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                        )
                    }
                }
            }

            // Primero lo que está en español, que es lo que la mayoría viene a
            // leer. Los léxicos de referencia son obras inglesas del XIX y
            // principios del XX y no se pueden traducir sin reescribirlas, así
            // que van después y dichas por su nombre, como cita de la fuente.
            Field("Número Strong", study.word.strong)
            Field("Análisis", study.word.morphology ?: study.word.morphCode)
            study.article?.gloss?.let { Field("Definición", it) }
            entry?.derivationEs?.let { Field("Procede de", it) }
            // Traducida a mano por orden de frecuencia: va aquí arriba, con lo
            // demás que ya se lee en español.
            entry?.definitionEs?.let { Field("Diccionario Strong", it) }

            val faltaTraducirLaDefinicion = entry?.definitionEs == null && entry?.definition != null
            val hayObrasEnIngles = faltaTraducirLaDefinicion || study.article != null
            if (hayObrasEnIngles) {
                HorizontalDivider(
                    modifier = Modifier.padding(top = 22.dp, bottom = 4.dp),
                    color = MaterialTheme.colorScheme.outlineVariant,
                )
                Text(
                    text = "Obras de referencia, en su lengua original",
                    style = MaterialTheme.typography.labelMedium,
                    color = MaterialTheme.colorScheme.secondary,
                    fontWeight = FontWeight.Bold,
                    modifier = Modifier.padding(top = 10.dp),
                )
                Text(
                    text = "Los léxicos que se citan a continuación están escritos en inglés.",
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                if (faltaTraducirLaDefinicion) {
                    entry?.definition?.let { Field("Diccionario Strong (1890)", it) }
                }
                study.article?.let { Field(it.source, it.article) }
            }

            if (study.occurrences > 0 && entry != null) {
                TextButton(
                    onClick = { onOpenConcordance(study.word.strong, entry.lemma) },
                    modifier = Modifier.padding(top = 8.dp),
                ) {
                    Text(
                        if (study.occurrences == 1) "Ver la única aparición"
                        else "Ver las ${study.occurrences} apariciones",
                    )
                }
            }

            Text(
                text = "El análisis, la definición y la procedencia de la palabra están " +
                    "traducidos al español por este proyecto. Cuando una palabra poco " +
                    "frecuente todavía no tiene definición traducida, se deja en blanco " +
                    "antes que ponerla en un idioma que no sea el tuyo.",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.padding(top = 16.dp),
            )
        }
    }
}

@Composable
private fun Field(label: String, value: String) {
    Column(Modifier.padding(top = 14.dp).widthIn(max = 640.dp)) {
        Text(
            text = label,
            style = MaterialTheme.typography.labelMedium,
            color = MaterialTheme.colorScheme.secondary,
            fontWeight = FontWeight.Bold,
        )
        Text(text = value, style = MaterialTheme.typography.bodyLarge)
    }
}

/**
 * Panel de una palabra de un texto sin análisis.
 *
 * La Septuaginta de Swete es texto corrido: no lleva números Strong ni
 * morfología. Lo que se enseña aquí es lo que esa misma forma significa en el
 * Nuevo Testamento, y el panel lo dice con todas las letras, porque no es lo
 * mismo: una forma puede coincidir y venir de otra palabra, y el griego de los
 * Setenta no siempre usa el vocabulario con el sentido que tiene en el Nuevo.
 */
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun PlainWordSheet(
    study: PlainWordStudy,
    onDismiss: () -> Unit,
    onSearch: (String) -> Unit,
) {
    val sheetState = rememberModalBottomSheetState(skipPartiallyExpanded = true)

    ModalBottomSheet(onDismissRequest = onDismiss, sheetState = sheetState) {
        Column(
            modifier = Modifier
                .fillMaxWidth()
                .verticalScroll(rememberScrollState())
                .padding(20.dp, 0.dp, 20.dp, 32.dp),
        ) {
            Text(
                text = study.surface,
                fontFamily = ScriptureFontFamily,
                fontSize = 30.sp,
                color = MaterialTheme.colorScheme.onSurface,
            )
            Text(
                text = study.reference,
                style = MaterialTheme.typography.labelLarge,
                color = MaterialTheme.colorScheme.secondary,
            )

            if (study.loading) {
                Row(
                    modifier = Modifier.fillMaxWidth().padding(vertical = 24.dp),
                    horizontalArrangement = Arrangement.Center,
                ) { CircularProgressIndicator() }
                return@Column
            }

            HorizontalDivider(
                modifier = Modifier.padding(vertical = 14.dp),
                color = MaterialTheme.colorScheme.outlineVariant,
            )

            if (study.readings.isEmpty()) {
                Text(
                    text = "Esta palabra no aparece con esta misma forma en el Nuevo " +
                        "Testamento, que es el texto griego que llevamos analizado, así que " +
                        "no hay nada que enseñar de ella.",
                    style = MaterialTheme.typography.bodyMedium,
                )
            } else {
                Text(
                    text = "La Septuaginta no viene analizada. Esta forma aparece así en el " +
                        "Nuevo Testamento:",
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                // Agrupadas por lema: la misma palabra en dos casos distintos es
                // una entrada con dos análisis, no dos entradas repetidas.
                study.readings.groupBy { it.strong }.forEach { (strong, lecturas) ->
                    val primera = lecturas.first()
                    Column(Modifier.padding(top = 16.dp)) {
                        Row(verticalAlignment = Alignment.Bottom) {
                            Text(
                                text = primera.lemma ?: strong,
                                fontFamily = ScriptureFontFamily,
                                style = MaterialTheme.typography.titleLarge,
                            )
                            primera.transliteration?.let {
                                Text(
                                    text = "  $it",
                                    style = MaterialTheme.typography.bodyMedium,
                                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                                )
                            }
                        }
                        primera.gloss?.let {
                            Text(text = it, style = MaterialTheme.typography.bodyLarge)
                        }
                        lecturas.forEach { lectura ->
                            Text(
                                text = lectura.morphology ?: lectura.morphCode,
                                style = MaterialTheme.typography.bodyMedium,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                            )
                        }
                        val veces = lecturas.sumOf { it.times }
                        Text(
                            text = "$strong · $veces " +
                                if (veces == 1) "vez en el NT" else "veces en el NT",
                            style = MaterialTheme.typography.labelMedium,
                            color = MaterialTheme.colorScheme.secondary,
                        )
                    }
                }
            }

            TextButton(
                onClick = { onSearch(study.surface) },
                modifier = Modifier.padding(top = 12.dp),
            ) { Text("Buscar esta palabra") }

            Text(
                text = "La edición de Swete es texto corrido, sin numeración Strong ni " +
                    "morfología: no existe una digitalización analizada de la Septuaginta " +
                    "cuya licencia permita distribuirla con la aplicación. Esto es una ayuda " +
                    "por coincidencia de forma, no un análisis del texto griego de los Setenta.",
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
                modifier = Modifier.padding(top = 18.dp),
            )
        }
    }
}

/**
 * Las palabras de un versículo sin análisis, para poder tocarlas.
 *
 * Se parte el texto por espacios, que es lo que hay: sin etiquetar, no existe
 * una segmentación mejor. La puntuación se recorta al consultar, no aquí, para
 * que en pantalla la palabra se vea como está impresa.
 */
@OptIn(ExperimentalLayoutApi::class)
@Composable
fun PlainWordChips(
    text: String,
    onWordClick: (String) -> Unit,
    modifier: Modifier = Modifier,
) {
    FlowRow(
        modifier = modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.spacedBy(6.dp),
        verticalArrangement = Arrangement.spacedBy(6.dp),
    ) {
        text.split(' ').filter { it.isNotBlank() }.forEach { palabra ->
            Surface(
                shape = RoundedCornerShape(8.dp),
                color = MaterialTheme.colorScheme.surfaceVariant,
                modifier = Modifier.clickable { onWordClick(palabra) },
            ) {
                Text(
                    text = palabra,
                    fontFamily = ScriptureFontFamily,
                    style = MaterialTheme.typography.bodyMedium,
                    modifier = Modifier.padding(horizontal = 8.dp, vertical = 5.dp),
                )
            }
        }
    }
}
