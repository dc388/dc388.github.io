package com.dc388.bibliagriega.ui

import android.app.Application
import androidx.lifecycle.AndroidViewModel
import androidx.lifecycle.viewModelScope
import com.dc388.bibliagriega.data.BibleRepository
import com.dc388.bibliagriega.data.Book
import com.dc388.bibliagriega.data.BibleCollection
import com.dc388.bibliagriega.data.Prefs
import com.dc388.bibliagriega.data.Settings
import com.dc388.bibliagriega.data.ThemeMode
import com.dc388.bibliagriega.data.Verse
import com.dc388.bibliagriega.data.VerseHit
import com.dc388.bibliagriega.data.VerseRef
import kotlinx.coroutines.Job
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

data class LibraryState(
    val collections: List<BibleCollection> = emptyList(),
    val booksByCollection: Map<String, List<Book>> = emptyMap(),
    val loading: Boolean = true,
    val error: String? = null,
)

data class ChapterState(
    val book: Book? = null,
    val chapter: Int = 1,
    val verses: List<Verse> = emptyList(),
    val loading: Boolean = true,
)

data class SearchState(
    val query: String = "",
    val scope: String? = null,
    val results: List<VerseHit> = emptyList(),
    val searching: Boolean = false,
    val ran: Boolean = false,
)

class BibliaViewModel(app: Application) : AndroidViewModel(app) {

    private val repo = BibleRepository.get(app)
    private val prefs = Prefs.get(app)

    private val _library = MutableStateFlow(LibraryState())
    val library: StateFlow<LibraryState> = _library.asStateFlow()

    private val _chapter = MutableStateFlow(ChapterState())
    val chapter: StateFlow<ChapterState> = _chapter.asStateFlow()

    private val _search = MutableStateFlow(SearchState())
    val search: StateFlow<SearchState> = _search.asStateFlow()

    private val _bookmarkHits = MutableStateFlow<List<VerseHit>>(emptyList())
    val bookmarkHits: StateFlow<List<VerseHit>> = _bookmarkHits.asStateFlow()

    val settings: StateFlow<Settings> =
        prefs.settings.stateIn(viewModelScope, SharingStarted.Eagerly, Settings())

    val lastRead: StateFlow<VerseRef?> =
        prefs.lastRead.stateIn(viewModelScope, SharingStarted.Eagerly, null)

    val bookmarks: StateFlow<List<VerseRef>> =
        prefs.bookmarks.stateIn(viewModelScope, SharingStarted.Eagerly, emptyList())

    private var searchJob: Job? = null

    init {
        viewModelScope.launch {
            runCatching {
                val collections = repo.collections()
                val books = collections.associate { it.id to repo.books(it.id) }
                LibraryState(collections, books, loading = false)
            }.onSuccess { _library.value = it }
                .onFailure {
                    _library.value = LibraryState(
                        loading = false,
                        error = it.message ?: "No se pudo abrir la base de datos",
                    )
                }
        }
        viewModelScope.launch {
            bookmarks.collect { refs -> _bookmarkHits.value = repo.verses(refs) }
        }
    }

    fun bookOf(bookId: Long): Book? =
        _library.value.booksByCollection.values.flatten().firstOrNull { it.id == bookId }

    fun loadChapter(bookId: Long, chapter: Int) {
        viewModelScope.launch {
            _chapter.value = ChapterState(book = bookOf(bookId), chapter = chapter, loading = true)
            val book = bookOf(bookId) ?: repo.book(bookId)
            val verses = repo.chapter(bookId, chapter)
            _chapter.value = ChapterState(book, chapter, verses, loading = false)
            verses.firstOrNull()?.let {
                prefs.setLastRead(VerseRef(bookId, chapter, it.verse, it.suffix))
            }
        }
    }

    fun onQueryChange(query: String, scope: String?) {
        _search.value = _search.value.copy(query = query, scope = scope)
        searchJob?.cancel()
        if (query.isBlank()) {
            _search.value = _search.value.copy(results = emptyList(), searching = false, ran = false)
            return
        }
        searchJob = viewModelScope.launch {
            delay(250) // antirrebote mientras se escribe
            _search.value = _search.value.copy(searching = true)
            val results = repo.search(query, scope)
            _search.value = _search.value.copy(results = results, searching = false, ran = true)
        }
    }

    fun setScope(scope: String?) = onQueryChange(_search.value.query, scope)

    fun toggleBookmark(ref: VerseRef) {
        viewModelScope.launch { prefs.toggleBookmark(ref) }
    }

    fun removeBookmark(ref: VerseRef) {
        viewModelScope.launch { prefs.removeBookmark(ref) }
    }

    fun setTheme(mode: ThemeMode) {
        viewModelScope.launch { prefs.setTheme(mode) }
    }

    fun setFontScale(scale: Float) {
        viewModelScope.launch { prefs.setFontScale(scale) }
    }

    fun setLineHeightScale(scale: Float) {
        viewModelScope.launch { prefs.setLineHeightScale(scale) }
    }

    fun setShowVerseNumbers(show: Boolean) {
        viewModelScope.launch { prefs.setShowVerseNumbers(show) }
    }

    fun setParagraphMode(on: Boolean) {
        viewModelScope.launch { prefs.setParagraphMode(on) }
    }
}
