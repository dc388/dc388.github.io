package com.dc388.bibliagriega.data

import android.content.Context
import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.MutablePreferences
import androidx.datastore.preferences.core.floatPreferencesKey
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.core.stringSetPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

enum class ThemeMode { SYSTEM, LIGHT, DARK }

data class Settings(
    val theme: ThemeMode = ThemeMode.SYSTEM,
    /** Multiplicador del tamaño de letra del lector (1.0 = tamaño base). */
    val fontScale: Float = 1.0f,
    val lineHeightScale: Float = 1.0f,
    val showVerseNumbers: Boolean = true,
    /** Cada versículo en su propio párrafo, o texto corrido como en las ediciones críticas. */
    val paragraphMode: Boolean = false,
)

private val Context.dataStore: DataStore<Preferences> by preferencesDataStore(name = "ajustes")

class Prefs private constructor(private val context: Context) {

    val settings: Flow<Settings> = context.dataStore.data.map { p ->
        Settings(
            theme = runCatching { ThemeMode.valueOf(p[KEY_THEME] ?: "SYSTEM") }
                .getOrDefault(ThemeMode.SYSTEM),
            fontScale = p[KEY_FONT_SCALE] ?: 1.0f,
            lineHeightScale = p[KEY_LINE_HEIGHT] ?: 1.0f,
            showVerseNumbers = (p[KEY_VERSE_NUMBERS] ?: "1") == "1",
            paragraphMode = (p[KEY_PARAGRAPH] ?: "0") == "1",
        )
    }

    val lastRead: Flow<VerseRef?> = context.dataStore.data.map { p ->
        p[KEY_LAST_READ]?.let(VerseRef::decode)
    }

    val bookmarks: Flow<List<VerseRef>> = context.dataStore.data.map { p ->
        (p[KEY_BOOKMARKS] ?: emptySet()).mapNotNull(VerseRef::decode)
            .sortedWith(compareBy({ it.bookId }, { it.chapter }, { it.verse }))
    }

    suspend fun setTheme(mode: ThemeMode) = put { it[KEY_THEME] = mode.name }

    suspend fun setFontScale(scale: Float) =
        put { it[KEY_FONT_SCALE] = scale.coerceIn(0.7f, 2.2f) }

    suspend fun setLineHeightScale(scale: Float) =
        put { it[KEY_LINE_HEIGHT] = scale.coerceIn(0.9f, 2.0f) }

    suspend fun setShowVerseNumbers(show: Boolean) =
        put { it[KEY_VERSE_NUMBERS] = if (show) "1" else "0" }

    suspend fun setParagraphMode(on: Boolean) =
        put { it[KEY_PARAGRAPH] = if (on) "1" else "0" }

    suspend fun setLastRead(ref: VerseRef) = put { it[KEY_LAST_READ] = ref.encode() }

    suspend fun toggleBookmark(ref: VerseRef) = put { prefs ->
        val current = prefs[KEY_BOOKMARKS] ?: emptySet()
        val encoded = ref.encode()
        prefs[KEY_BOOKMARKS] =
            if (encoded in current) current - encoded else current + encoded
    }

    suspend fun removeBookmark(ref: VerseRef) = put { prefs ->
        prefs[KEY_BOOKMARKS] = (prefs[KEY_BOOKMARKS] ?: emptySet()) - ref.encode()
    }

    private suspend fun put(block: suspend (MutablePreferences) -> Unit) {
        context.dataStore.edit(block)
    }

    companion object {
        private val KEY_THEME = stringPreferencesKey("theme")
        private val KEY_FONT_SCALE = floatPreferencesKey("font_scale")
        private val KEY_LINE_HEIGHT = floatPreferencesKey("line_height")
        private val KEY_VERSE_NUMBERS = stringPreferencesKey("verse_numbers")
        private val KEY_PARAGRAPH = stringPreferencesKey("paragraph_mode")
        private val KEY_LAST_READ = stringPreferencesKey("last_read")
        private val KEY_BOOKMARKS = stringSetPreferencesKey("bookmarks")

        @Volatile
        private var instance: Prefs? = null

        fun get(context: Context): Prefs =
            instance ?: synchronized(this) {
                instance ?: Prefs(context.applicationContext).also { instance = it }
            }
    }
}
