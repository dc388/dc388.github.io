package com.dc388.bibliagriega.ui.screens

import androidx.compose.foundation.clickable
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
import androidx.compose.material.icons.filled.BookmarkRemove
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.HorizontalDivider
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TopAppBar
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import com.dc388.bibliagriega.data.VerseHit
import com.dc388.bibliagriega.data.VerseRef
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun BookmarksScreen(
    vm: BibliaViewModel,
    onBack: () -> Unit,
    onOpenVerse: (VerseHit) -> Unit,
) {
    val hits by vm.bookmarkHits.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Marcadores") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Atrás")
                    }
                },
            )
        },
    ) { padding ->
        if (hits.isEmpty()) {
            Box(
                modifier = Modifier.fillMaxSize().padding(padding).padding(32.dp),
                contentAlignment = Alignment.Center,
            ) {
                Text(
                    text = "Todavía no has marcado ningún versículo.\n" +
                        "Toca un versículo mientras lees y elige «Marcar».",
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    textAlign = TextAlign.Center,
                )
            }
            return@Scaffold
        }

        LazyColumn(
            modifier = Modifier.fillMaxSize(),
            contentPadding = PaddingValues(
                top = padding.calculateTopPadding(),
                bottom = padding.calculateBottomPadding() + 24.dp,
            ),
        ) {
            items(hits, key = { it.reference }) { hit ->
                Row(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { onOpenVerse(hit) }
                        .padding(16.dp, 10.dp),
                    verticalAlignment = Alignment.CenterVertically,
                ) {
                    Column(Modifier.weight(1f)) {
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
                    IconButton(
                        onClick = {
                            vm.removeBookmark(
                                VerseRef(
                                    hit.verse.bookId,
                                    hit.verse.chapter,
                                    hit.verse.verse,
                                    hit.verse.suffix,
                                ),
                            )
                        },
                    ) {
                        Icon(Icons.Default.BookmarkRemove, contentDescription = "Quitar marcador")
                    }
                }
                HorizontalDivider(color = MaterialTheme.colorScheme.outlineVariant)
            }
        }
    }
}
