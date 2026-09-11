package com.dc388.bibliagriega

import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.screens.BookmarksScreen
import com.dc388.bibliagriega.ui.screens.ChaptersScreen
import com.dc388.bibliagriega.ui.screens.ConcordanceScreen
import com.dc388.bibliagriega.ui.screens.HomeScreen
import com.dc388.bibliagriega.ui.screens.ReaderScreen
import com.dc388.bibliagriega.ui.screens.SearchScreen
import com.dc388.bibliagriega.ui.screens.SettingsScreen
import com.dc388.bibliagriega.ui.theme.BibliaGriegaTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        setContent { BibliaApp() }
    }
}

object Routes {
    const val HOME = "home"
    const val SEARCH = "search"
    const val BOOKMARKS = "bookmarks"
    const val SETTINGS = "settings"
    fun chapters(bookId: Long) = "chapters/$bookId"
    fun reader(bookId: Long, chapter: Int) = "reader/$bookId/$chapter"
    fun concordance(strong: String, lemma: String) =
        "concordance/$strong/${Uri.encode(lemma.ifBlank { "-" })}"
}

@Composable
fun BibliaApp(vm: BibliaViewModel = viewModel()) {
    val settings by vm.settings.collectAsState()

    BibliaGriegaTheme(themeMode = settings.theme) {
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colorScheme.background,
        ) {
            val nav = rememberNavController()
            NavHost(navController = nav, startDestination = Routes.HOME) {
                composable(Routes.HOME) {
                    HomeScreen(
                        vm = vm,
                        onOpenBook = { nav.navigate(Routes.chapters(it)) },
                        onContinue = { ref -> nav.navigate(Routes.reader(ref.bookId, ref.chapter)) },
                        onSearch = { nav.navigate(Routes.SEARCH) },
                        onBookmarks = { nav.navigate(Routes.BOOKMARKS) },
                        onSettings = { nav.navigate(Routes.SETTINGS) },
                    )
                }
                composable(
                    route = "chapters/{bookId}",
                    arguments = listOf(navArgument("bookId") { type = NavType.LongType }),
                ) { entry ->
                    val bookId = entry.arguments?.getLong("bookId") ?: 0L
                    ChaptersScreen(
                        vm = vm,
                        bookId = bookId,
                        onBack = { nav.popBackStack() },
                        onOpenChapter = { chapter -> nav.navigate(Routes.reader(bookId, chapter)) },
                    )
                }
                composable(
                    route = "reader/{bookId}/{chapter}",
                    arguments = listOf(
                        navArgument("bookId") { type = NavType.LongType },
                        navArgument("chapter") { type = NavType.IntType },
                    ),
                ) { entry ->
                    ReaderScreen(
                        vm = vm,
                        bookId = entry.arguments?.getLong("bookId") ?: 0L,
                        chapter = entry.arguments?.getInt("chapter") ?: 1,
                        onBack = { nav.popBackStack() },
                        onOpenChapter = { book, chapter ->
                            nav.navigate(Routes.reader(book, chapter)) {
                                popUpTo("reader/{bookId}/{chapter}") { inclusive = true }
                            }
                        },
                        onSettings = { nav.navigate(Routes.SETTINGS) },
                        onOpenConcordance = { strong, lemma ->
                            nav.navigate(Routes.concordance(strong, lemma))
                        },
                    )
                }
                composable(
                    route = "concordance/{strong}/{lemma}",
                    arguments = listOf(
                        navArgument("strong") { type = NavType.StringType },
                        navArgument("lemma") { type = NavType.StringType },
                    ),
                ) { entry ->
                    ConcordanceScreen(
                        vm = vm,
                        strong = entry.arguments?.getString("strong").orEmpty(),
                        lemma = entry.arguments?.getString("lemma")?.takeIf { it != "-" }.orEmpty(),
                        onBack = { nav.popBackStack() },
                        onOpenVerse = { hit ->
                            nav.navigate(Routes.reader(hit.verse.bookId, hit.verse.chapter))
                        },
                    )
                }
                composable(Routes.SEARCH) {
                    SearchScreen(
                        vm = vm,
                        onBack = { nav.popBackStack() },
                        onOpenVerse = { hit ->
                            nav.navigate(Routes.reader(hit.verse.bookId, hit.verse.chapter))
                        },
                    )
                }
                composable(Routes.BOOKMARKS) {
                    BookmarksScreen(
                        vm = vm,
                        onBack = { nav.popBackStack() },
                        onOpenVerse = { hit ->
                            nav.navigate(Routes.reader(hit.verse.bookId, hit.verse.chapter))
                        },
                    )
                }
                composable(Routes.SETTINGS) {
                    SettingsScreen(vm = vm, onBack = { nav.popBackStack() })
                }
            }
        }
    }
}
