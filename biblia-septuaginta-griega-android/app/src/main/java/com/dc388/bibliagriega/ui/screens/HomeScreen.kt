package com.dc388.bibliagriega.ui.screens

import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Bookmarks
import androidx.compose.material.icons.filled.EditNote
import androidx.compose.material.icons.filled.PlayArrow
import androidx.compose.material.icons.filled.Search
import androidx.compose.material.icons.filled.Settings
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.SegmentedButton
import androidx.compose.material3.SegmentedButtonDefaults
import androidx.compose.material3.SingleChoiceSegmentedButtonRow
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.dc388.bibliagriega.data.Book
import com.dc388.bibliagriega.data.VerseRef
import com.dc388.bibliagriega.ui.AnchoDeLista
import com.dc388.bibliagriega.ui.columna
import com.dc388.bibliagriega.ui.BibliaViewModel

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun HomeScreen(
    vm: BibliaViewModel,
    onOpenBook: (Long) -> Unit,
    onContinue: (VerseRef) -> Unit,
    onSearch: () -> Unit,
    onBookmarks: () -> Unit,
    onNotes: () -> Unit,
    onSettings: () -> Unit,
) {
    val library by vm.library.collectAsState()
    val lastRead by vm.lastRead.collectAsState()
    var selected by rememberSaveable { mutableStateOf(0) }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Biblia Griega") },
                actions = {
                    IconButton(onClick = onSearch) {
                        Icon(Icons.Default.Search, contentDescription = "Buscar")
                    }
                    IconButton(onClick = onBookmarks) {
                        Icon(Icons.Default.Bookmarks, contentDescription = "Marcadores")
                    }
                    IconButton(onClick = onNotes) {
                        Icon(Icons.Default.EditNote, contentDescription = "Mis notas")
                    }
                    IconButton(onClick = onSettings) {
                        Icon(Icons.Default.Settings, contentDescription = "Ajustes")
                    }
                },
            )
        },
    ) { padding ->
        when {
            library.loading -> Box(
                Modifier.columna(AnchoDeLista).padding(padding),
                contentAlignment = Alignment.Center,
            ) { CircularProgressIndicator() }

            library.error != null -> Box(
                Modifier.columna(AnchoDeLista).padding(padding).padding(24.dp),
                contentAlignment = Alignment.Center,
            ) {
                Text(
                    "No se pudo abrir la biblioteca.\n${library.error}",
                    style = MaterialTheme.typography.bodyMedium,
                )
            }

            else -> {
                val collections = library.collections
                val current = collections.getOrNull(selected)
                val books = current?.let { library.booksByCollection[it.id] }.orEmpty()

                LazyColumn(
                    modifier = Modifier.columna(AnchoDeLista),
                    contentPadding = PaddingValues(
                        top = padding.calculateTopPadding(),
                        bottom = padding.calculateBottomPadding() + 16.dp,
                    ),
                ) {
                    if (lastRead != null) {
                        item {
                            ContinueCard(
                                ref = lastRead!!,
                                title = vm.bookOf(lastRead!!.bookId)?.displayName,
                                onClick = { onContinue(lastRead!!) },
                            )
                        }
                    }

                    item {
                        SingleChoiceSegmentedButtonRow(
                            modifier = Modifier
                                .fillMaxWidth()
                                .padding(horizontal = 16.dp, vertical = 8.dp),
                        ) {
                            collections.forEachIndexed { index, collection ->
                                SegmentedButton(
                                    selected = index == selected,
                                    onClick = { selected = index },
                                    shape = SegmentedButtonDefaults.itemShape(
                                        index = index,
                                        count = collections.size,
                                    ),
                                ) { Text(collection.shortName) }
                            }
                        }
                    }

                    if (current != null) {
                        item {
                            Text(
                                text = current.edition,
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                                modifier = Modifier.padding(horizontal = 16.dp, vertical = 4.dp),
                            )
                        }
                    }

                    if (current?.id == "padres") {
                        item { NotaPadres() }
                    }

                    items(books, key = { it.id }) { book ->
                        BookRow(book = book, onClick = { onOpenBook(book.id) })
                        HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant)
                    }
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun ContinueCard(ref: VerseRef, title: String?, onClick: () -> Unit) {
    Card(
        onClick = onClick,
        modifier = Modifier.fillMaxWidth().padding(16.dp, 12.dp, 16.dp, 4.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.secondaryContainer,
            contentColor = MaterialTheme.colorScheme.onSecondaryContainer,
        ),
    ) {
        Row(
            modifier = Modifier.fillMaxWidth().padding(16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            Icon(Icons.Default.PlayArrow, contentDescription = null)
            Column(Modifier.weight(1f)) {
                Text("Continuar leyendo", style = MaterialTheme.typography.labelLarge)
                Text(
                    text = "${title ?: "Capítulo"} ${ref.chapter}",
                    style = MaterialTheme.typography.titleMedium,
                )
            }
        }
    }
}

@Composable
private fun BookRow(book: Book, onClick: () -> Unit) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick)
            .padding(horizontal = 16.dp, vertical = 12.dp),
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Column(Modifier.weight(1f)) {
            Text(
                text = book.displayName,
                style = MaterialTheme.typography.bodyLarge,
                fontWeight = FontWeight.Medium,
            )
            Text(
                text = book.nameOriginal,
                style = MaterialTheme.typography.bodyMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
        Text(
            text = "${book.chapterCount} cap.",
            style = MaterialTheme.typography.bodySmall,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
    }
}

/**
 * Lo que más se pregunta de los Padres Apostólicos: qué son y si son
 * «católicos», porque Ignacio habla de «la iglesia católica». Es el mismo
 * texto que la biblioteca de la web; va plegado para no empujar la lista.
 */
private val PADRES_EXPLICACION = listOf(
    "Son los escritos de los cristianos que vinieron justo después de los " +
        "apóstoles, entre los años 90 y 150. Algunos conocieron a los apóstoles o a " +
        "sus discípulos: según la tradición, Policarpo fue discípulo de Juan. " +
        "Ninguna iglesia los recibe como Escritura inspirada; se leen como " +
        "testimonio de cómo creía y vivía la iglesia primitiva.",
    "No son católicos en el sentido de hoy: son anteriores a la separación " +
        "entre Roma y Oriente (1054) y a la Reforma (1517), y todas las tradiciones " +
        "los tienen por suyos. Católicos y ortodoxos subrayan en ellos los obispos, " +
        "la sucesión de los apóstoles (1 Clemente 42-44) y la eucaristía. Los " +
        "evangélicos subrayan la justificación por la fe —«no por nosotros " +
        "mismos… sino por la fe» (1 Clemente 32:4)—, que obispo y presbítero " +
        "parecen ser el mismo cargo (1 Clemente, Didaché) y que citan la Escritura " +
        "sin cesar.",
    "Cuando Ignacio escribe «donde está Jesucristo, allí está la iglesia " +
        "católica» (Esmirniotas 8:2), la palabra griega katholikós significa " +
        "«universal»: la iglesia entera frente a una congregación local, no el " +
        "nombre de una denominación, que vino siglos después.",
)

@OptIn(ExperimentalMaterial3Api::class)
@Composable
private fun NotaPadres() {
    var abierta by rememberSaveable { mutableStateOf(false) }
    Card(
        onClick = { abierta = !abierta },
        modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp, vertical = 8.dp),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceContainerHigh,
        ),
    ) {
        Column(
            modifier = Modifier.padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Text(
                text = "Cartas y manuales cristianos del siglo I y II. No son apócrifos: " +
                    "nunca se presentaron como Escritura.",
                style = MaterialTheme.typography.bodyMedium,
            )
            Text(
                text = if (abierta) "▾ ¿Qué son? ¿Son católicos?" else "▸ ¿Qué son? ¿Son católicos?",
                style = MaterialTheme.typography.labelLarge,
                fontWeight = FontWeight.SemiBold,
                color = MaterialTheme.colorScheme.primary,
            )
            if (abierta) {
                PADRES_EXPLICACION.forEach { parrafo ->
                    Text(
                        text = parrafo,
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }
        }
    }
}
