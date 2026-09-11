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
import com.dc388.bibliagriega.ui.WordStudy
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

/**
 * Interlineal: cada palabra griega sobre su transliteración y su número Strong.
 * Al tocar una palabra se abre su entrada del léxico.
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

            Field("Número Strong", study.word.strong)
            Field("Análisis", study.word.morphology ?: study.word.morphCode)
            entry?.definition?.let { Field("Definición", it) }
            entry?.derivation?.let { Field("Etimología", it) }
            entry?.kjvUsage?.let { Field("Traducciones (KJV)", it) }

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
                text = "Definiciones del Diccionario Strong (1890). El análisis morfológico " +
                    "es el de Robinson, traducido al español.",
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
