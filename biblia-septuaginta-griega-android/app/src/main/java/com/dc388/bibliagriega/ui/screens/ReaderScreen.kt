package com.dc388.bibliagriega.ui.screens

import android.content.ClipData
import android.content.ClipboardManager
import android.content.Context
import android.content.Intent
import android.widget.Toast
import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.width
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.automirrored.filled.ArrowBack
import androidx.compose.material.icons.automirrored.filled.ArrowForward
import androidx.compose.material.icons.filled.Bookmark
import androidx.compose.material.icons.filled.BookmarkBorder
import androidx.compose.material.icons.filled.ContentCopy
import androidx.compose.material.icons.filled.EditNote
import androidx.compose.material.icons.filled.Share
import androidx.compose.material.icons.filled.TextFields
import androidx.compose.material3.BottomAppBar
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.ModalBottomSheet
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.material3.TopAppBar
import androidx.compose.material3.rememberModalBottomSheetState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalLayoutDirection
import androidx.compose.ui.text.SpanStyle
import androidx.compose.ui.text.buildAnnotatedString
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.withStyle
import androidx.compose.ui.unit.LayoutDirection
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.dc388.bibliagriega.data.InterlinearWord
import com.dc388.bibliagriega.data.Verse
import com.dc388.bibliagriega.data.VerseRef
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.theme.ScriptureFontFamily

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ReaderScreen(
    vm: BibliaViewModel,
    bookId: Long,
    chapter: Int,
    onBack: () -> Unit,
    onOpenChapter: (Long, Int) -> Unit,
    onSettings: () -> Unit,
    onOpenConcordance: (strong: String, lemma: String) -> Unit,
) {
    val state by vm.chapter.collectAsState()
    val settings by vm.settings.collectAsState()
    val bookmarks by vm.bookmarks.collectAsState()
    val interlinear by vm.interlinear.collectAsState()
    val wordStudy by vm.wordStudy.collectAsState()
    val notes by vm.notes.collectAsState()
    val context = LocalContext.current

    var sheetVerse by remember { mutableStateOf<Verse?>(null) }
    var editingNote by remember { mutableStateOf<Verse?>(null) }
    val sheetState = rememberModalBottomSheetState()

    LaunchedEffect(bookId, chapter) { vm.loadChapter(bookId, chapter) }

    val book = state.book
    val bookName = book?.displayName ?: ""

    Scaffold(
        topBar = {
            TopAppBar(
                title = {
                    Column {
                        Text("$bookName $chapter")
                        if (book != null) {
                            Text(
                                text = book.nameOriginal,
                                style = MaterialTheme.typography.bodySmall,
                                color = MaterialTheme.colorScheme.onSurfaceVariant,
                            )
                        }
                    }
                },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.AutoMirrored.Filled.ArrowBack, contentDescription = "Atrás")
                    }
                },
                actions = {
                    IconButton(onClick = onSettings) {
                        Icon(Icons.Default.TextFields, contentDescription = "Tipografía")
                    }
                    IconButton(
                        onClick = {
                            share(context, "$bookName $chapter", chapterText(state.verses))
                        },
                    ) {
                        Icon(Icons.Default.Share, contentDescription = "Compartir capítulo")
                    }
                },
            )
        },
        bottomBar = {
            BottomAppBar {
                val total = book?.chapterCount ?: 1
                IconButton(
                    onClick = { onOpenChapter(bookId, chapter - 1) },
                    enabled = chapter > 1,
                ) {
                    Icon(
                        Icons.AutoMirrored.Filled.ArrowBack,
                        contentDescription = "Capítulo anterior",
                    )
                }
                Text(
                    text = "Capítulo $chapter de $total",
                    modifier = Modifier.weight(1f),
                    style = MaterialTheme.typography.bodyMedium,
                )
                IconButton(
                    onClick = { onOpenChapter(bookId, chapter + 1) },
                    enabled = chapter < total,
                ) {
                    Icon(
                        Icons.AutoMirrored.Filled.ArrowForward,
                        contentDescription = "Capítulo siguiente",
                    )
                }
            }
        },
    ) { padding ->
        if (state.loading) {
            Column(
                modifier = Modifier.fillMaxSize().padding(padding),
                verticalArrangement = Arrangement.Center,
                horizontalAlignment = Alignment.CenterHorizontally,
            ) { CircularProgressIndicator() }
            return@Scaffold
        }

        val rtl = book?.rtl == true
        val direction = if (rtl) LayoutDirection.Rtl else LayoutDirection.Ltr
        val fontSize = (18 * settings.fontScale).sp
        val numberColor = MaterialTheme.colorScheme.secondary
        val textColor = MaterialTheme.colorScheme.onBackground
        val lineHeight = (30 * settings.fontScale * settings.lineHeightScale).sp
        val marked = bookmarks.filter { it.bookId == bookId && it.chapter == chapter }
            .map { it.verse to it.suffix }
            .toSet()
        val annotated = notes.keys
            .filter { it.bookId == bookId && it.chapter == chapter }
            .map { it.verse to it.suffix }
            .toSet()

        CompositionLocalProvider(LocalLayoutDirection provides direction) {
            if (settings.paragraphMode) {
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(
                        start = 20.dp,
                        end = 20.dp,
                        top = padding.calculateTopPadding() + 12.dp,
                        bottom = padding.calculateBottomPadding() + 32.dp,
                    ),
                ) {
                    item {
                        Text(
                            text = buildAnnotatedString {
                                state.verses.forEach { verse ->
                                    if (settings.showVerseNumbers) {
                                        withStyle(
                                            SpanStyle(
                                                fontSize = fontSize * 0.6f,
                                                fontWeight = FontWeight.Bold,
                                                color = numberColor,
                                            ),
                                        ) { append("${verse.label} ") }
                                    }
                                    append(verse.text)
                                    append("  ")
                                }
                            },
                            fontFamily = ScriptureFontFamily,
                            fontSize = fontSize,
                            lineHeight = lineHeight,
                            color = textColor,
                        )
                    }
                }
            } else {
                LazyColumn(
                    modifier = Modifier.fillMaxSize(),
                    contentPadding = PaddingValues(
                        top = padding.calculateTopPadding() + 8.dp,
                        bottom = padding.calculateBottomPadding() + 32.dp,
                    ),
                ) {
                    items(state.verses, key = { "${it.verse}${it.suffix}" }) { verse ->
                        val isMarked = (verse.verse to verse.suffix) in marked
                        val hasNote = (verse.verse to verse.suffix) in annotated
                        val words = interlinear[verse.id]

                        if (settings.interlinear && !words.isNullOrEmpty()) {
                            InterlinearVerseRow(
                                label = if (hasNote) "${verse.label}•" else verse.label,
                                words = words,
                                showNumber = settings.showVerseNumbers,
                                marked = isMarked,
                                fontSizeSp = fontSize.value,
                                onWordClick = { word ->
                                    vm.studyWord(word, "$bookName $chapter:${verse.label}")
                                },
                                onVerseClick = { sheetVerse = verse },
                            )
                        } else {
                            VerseRow(
                                verse = verse,
                                showNumber = settings.showVerseNumbers,
                                marked = isMarked,
                                hasNote = hasNote,
                                fontSizeSp = fontSize.value,
                                lineHeightSp = lineHeight.value,
                                onClick = { sheetVerse = verse },
                            )
                        }
                    }
                }
            }
    }

    sheetVerse?.let { verse ->
        val ref = VerseRef(bookId, chapter, verse.verse, verse.suffix)
        val reference = "$bookName $chapter:${verse.label}"
        ModalBottomSheet(
            onDismissRequest = { sheetVerse = null },
            sheetState = sheetState,
        ) {
            Column(Modifier.fillMaxWidth().padding(20.dp, 0.dp, 20.dp, 28.dp)) {
                Text(reference, style = MaterialTheme.typography.titleMedium)
                Text(
                    text = verse.text,
                    fontFamily = ScriptureFontFamily,
                    style = MaterialTheme.typography.bodyLarge,
                    modifier = Modifier.padding(vertical = 12.dp),
                )
                interlinear[verse.id]?.takeIf { it.isNotEmpty() }?.let { words ->
                    Text(
                        text = "Toca una palabra para analizarla",
                        style = MaterialTheme.typography.labelMedium,
                        color = MaterialTheme.colorScheme.secondary,
                    )
                    WordChips(
                        words = words,
                        onWordClick = { word ->
                            sheetVerse = null
                            vm.studyWord(word, reference)
                        },
                        modifier = Modifier.padding(top = 8.dp, bottom = 12.dp),
                    )
                }
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    val isMarked = bookmarks.any {
                        it.bookId == bookId && it.chapter == chapter &&
                            it.verse == verse.verse && it.suffix == verse.suffix
                    }
                    TextButton(onClick = { vm.toggleBookmark(ref); sheetVerse = null }) {
                        Icon(
                            imageVector = if (isMarked) Icons.Default.Bookmark
                            else Icons.Default.BookmarkBorder,
                            contentDescription = null,
                        )
                        Text(
                            text = if (isMarked) " Quitar" else " Marcar",
                            modifier = Modifier.padding(start = 4.dp),
                        )
                    }
                    TextButton(
                        onClick = {
                            editingNote = verse
                            sheetVerse = null
                        },
                    ) {
                        Icon(Icons.Default.EditNote, contentDescription = null)
                        Text(
                            text = if (notes.containsKey(ref)) " Nota" else " Anotar",
                            modifier = Modifier.padding(start = 4.dp),
                        )
                    }
                    TextButton(
                        onClick = {
                            copy(context, "$reference — ${verse.text}")
                            sheetVerse = null
                        },
                    ) {
                        Icon(Icons.Default.ContentCopy, contentDescription = null)
                        Text(" Copiar", modifier = Modifier.padding(start = 4.dp))
                    }
                    TextButton(
                        onClick = {
                            share(context, reference, "$reference\n\n${verse.text}")
                            sheetVerse = null
                        },
                    ) {
                        Icon(Icons.Default.Share, contentDescription = null)
                        Text(" Compartir", modifier = Modifier.padding(start = 4.dp))
                    }
                }
            }
        }
        }
    }

    editingNote?.let { verse ->
        val ref = VerseRef(bookId, chapter, verse.verse, verse.suffix)
        NoteEditor(
            reference = "$bookName $chapter:${verse.label}",
            initialText = notes[ref].orEmpty(),
            onDismiss = { editingNote = null },
            onSave = { text ->
                vm.setNote(ref, text)
                editingNote = null
            },
        )
    }

    wordStudy?.let { study ->
        WordStudySheet(
            study = study,
            onDismiss = vm::closeWordStudy,
            onOpenConcordance = { strong, lemma ->
                vm.closeWordStudy()
                onOpenConcordance(strong, lemma)
            },
        )
    }
}

@Composable
private fun InterlinearVerseRow(
    label: String,
    words: List<InterlinearWord>,
    showNumber: Boolean,
    marked: Boolean,
    fontSizeSp: Float,
    onWordClick: (InterlinearWord) -> Unit,
    onVerseClick: () -> Unit,
) {
    val background =
        if (marked) MaterialTheme.colorScheme.secondaryContainer
        else MaterialTheme.colorScheme.background

    Column(
        modifier = Modifier
            .fillMaxWidth()
            .background(background)
            .padding(horizontal = 20.dp, vertical = 10.dp),
    ) {
        if (showNumber) {
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.secondary,
                fontWeight = FontWeight.Bold,
                modifier = Modifier.clickable(onClick = onVerseClick),
            )
        }
        InterlinearVerse(
            words = words,
            fontSizeSp = fontSizeSp,
            onWordClick = onWordClick,
            modifier = Modifier.padding(top = 4.dp),
        )
    }
}

@Composable
private fun VerseRow(
    verse: Verse,
    showNumber: Boolean,
    marked: Boolean,
    hasNote: Boolean,
    fontSizeSp: Float,
    lineHeightSp: Float,
    onClick: () -> Unit,
) {
    val background =
        if (marked) MaterialTheme.colorScheme.secondaryContainer
        else MaterialTheme.colorScheme.background

    Row(
        modifier = Modifier
            .fillMaxWidth()
            .clickable(onClick = onClick)
            .background(background)
            .padding(horizontal = 20.dp, vertical = 6.dp),
    ) {
        if (showNumber) {
            Text(
                text = if (hasNote) "${verse.label}•" else verse.label,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.secondary,
                fontWeight = FontWeight.Bold,
                modifier = Modifier.padding(end = 10.dp, top = 4.dp).width(30.dp),
            )
        }
        Text(
            text = verse.text,
            fontFamily = ScriptureFontFamily,
            fontSize = fontSizeSp.sp,
            lineHeight = lineHeightSp.sp,
            color = MaterialTheme.colorScheme.onBackground,
            modifier = Modifier.weight(1f),
        )
    }
}

private fun chapterText(verses: List<Verse>): String =
    verses.joinToString(" ") { "${it.label} ${it.text}" }

private fun share(context: Context, subject: String, body: String) {
    val intent = Intent(Intent.ACTION_SEND).apply {
        type = "text/plain"
        putExtra(Intent.EXTRA_SUBJECT, subject)
        putExtra(Intent.EXTRA_TEXT, body)
    }
    context.startActivity(Intent.createChooser(intent, "Compartir"))
}

private fun copy(context: Context, text: String) {
    val clipboard = context.getSystemService(Context.CLIPBOARD_SERVICE) as ClipboardManager
    clipboard.setPrimaryClip(ClipData.newPlainText("Biblia Griega", text))
    Toast.makeText(context, "Copiado", Toast.LENGTH_SHORT).show()
}
