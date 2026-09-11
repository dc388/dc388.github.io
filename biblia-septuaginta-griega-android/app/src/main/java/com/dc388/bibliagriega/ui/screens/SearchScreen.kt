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
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.filled.Close
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.FilterChip
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedTextField
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.focus.focusRequester
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import com.dc388.bibliagriega.data.VerseHit
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SearchScreen(
    vm: BibliaViewModel,
    onBack: () -> Unit,
    onOpenVerse: (VerseHit) -> Unit,
) {
    val search by vm.search.collectAsState()
    val library by vm.library.collectAsState()
    val focus = remember { FocusRequester() }

    LaunchedEffect(Unit) { runCatching { focus.requestFocus() } }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Buscar") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Atrás")
                    }
                },
            )
        },
    ) { padding ->
        Column(Modifier.fillMaxSize().padding(padding)) {
            OutlinedTextField(
                value = search.query,
                onValueChange = { vm.onQueryChange(it, search.scope) },
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(16.dp, 8.dp)
                    .focusRequester(focus),
                singleLine = true,
                label = { Text("Palabra griega") },
                supportingText = {
                    Text(
                        "Sin acentos y por el comienzo de la palabra: «λογ» encuentra " +
                            "«λόγος», «λόγῳ» y «λόγον».",
                    )
                },
                trailingIcon = {
                    if (search.query.isNotEmpty()) {
                        IconButton(onClick = { vm.onQueryChange("", search.scope) }) {
                            Icon(Icons.Default.Close, contentDescription = "Limpiar")
                        }
                    }
                },
            )

            Row(
                modifier = Modifier.fillMaxWidth().padding(horizontal = 16.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                FilterChip(
                    selected = search.scope == null,
                    onClick = { vm.setScope(null) },
                    label = { Text("Toda la Biblia") },
                )
                library.collections.forEach { collection ->
                    FilterChip(
                        selected = search.scope == collection.id,
                        onClick = { vm.setScope(collection.id) },
                        label = { Text(collection.shortName) },
                    )
                }
            }

            when {
                search.searching -> Box(
                    Modifier.fillMaxSize(),
                    contentAlignment = Alignment.Center,
                ) { CircularProgressIndicator() }

                search.ran && search.results.isEmpty() -> Box(
                    Modifier.fillMaxSize().padding(32.dp),
                    contentAlignment = Alignment.Center,
                ) {
                    Text(
                        "Sin resultados para «${search.query}».",
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }

                else -> LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(top = 8.dp, bottom = 24.dp),
                ) {
                    if (search.results.isNotEmpty()) {
                        item {
                            Text(
                                text = "${search.results.size} versículos",
                                style = MaterialTheme.typography.labelMedium,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                                modifier = Modifier.padding(16.dp, 4.dp),
                            )
                        }
                    }
                    items(search.results, key = { it.reference }) { hit ->
                        Column(
                            modifier = Modifier
                                .fillMaxWidth()
                                .clickable { onOpenVerse(hit) }
                                .padding(16.dp, 10.dp),
                        ) {
                            Text(
                                text = hit.reference,
                                style = MaterialTheme.typography.labelLarge,
                                color = MaterialTheme.colorScheme.secondary,
                                fontWeight = FontWeight.Bold,
                            )
                            Text(
                                text = hit.verse.text,
                                fontFamily = ScriptureFontFamily,
                                style = MaterialTheme.typography.bodyLarge,
                            )
                        }
                        HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant)
                    }
                }
            }
        }
    }
}
