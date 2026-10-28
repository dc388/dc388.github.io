package com.dc388.bibliagriega

import android.content.Intent
import android.net.Uri
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.lifecycle.lifecycleScope
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.NavType
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController
import androidx.navigation.navArgument
import com.dc388.bibliagriega.data.Actualizaciones
import com.dc388.bibliagriega.data.AvisoDiario
import com.dc388.bibliagriega.data.Compras
import com.dc388.bibliagriega.data.Prefs
import com.dc388.bibliagriega.ui.BibliaViewModel
import com.dc388.bibliagriega.ui.prepararAnuncios
import com.dc388.bibliagriega.ui.screens.BookmarksScreen
import com.dc388.bibliagriega.ui.screens.ChaptersScreen
import com.dc388.bibliagriega.ui.screens.ConcordanceScreen
import com.dc388.bibliagriega.ui.screens.HomeScreen
import com.dc388.bibliagriega.ui.screens.NotesScreen
import com.dc388.bibliagriega.ui.screens.ReaderScreen
import com.dc388.bibliagriega.ui.screens.SearchScreen
import com.dc388.bibliagriega.ui.screens.SettingsScreen
import com.dc388.bibliagriega.ui.theme.BibliaGriegaTheme
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.launch
import kotlinx.coroutines.withTimeoutOrNull

class MainActivity : ComponentActivity() {
    // Se crea con la actividad, antes de que arranque: registra un lanzador de
    // resultados y Android no lo admite más tarde.
    private val actualizaciones = Actualizaciones(this)

    override fun onCreate(savedInstanceState: Bundle?) {
        enableEdgeToEdge()
        super.onCreate(savedInstanceState)
        // El aviso de la mañana abre la aplicación con el versículo dentro del
        // intento. Como la actividad no es singleTop y el aviso trae
        // FLAG_ACTIVITY_CLEAR_TOP, el sistema la recrea y el intento llega
        // siempre aquí: no hace falta onNewIntent.
        val apertura = aperturaDe(intent)
        setContent {
            val lista by actualizaciones.lista.collectAsState()
            BibliaApp(
                actualizacionLista = lista,
                onReiniciar = actualizaciones::reiniciar,
                onDespues = actualizaciones::despues,
                apertura = apertura,
            )
        }
        actualizaciones.comprobar()

        // Android borra las alarmas al reiniciar el teléfono y al actualizar la
        // aplicación. El receptor del arranque cubre lo primero; esto cubre lo
        // segundo y, de paso, cualquier otra forma de perderla.
        lifecycleScope.launch {
            val ajustes = Prefs.get(applicationContext).settings.first()
            if (ajustes.avisoDiario) {
                AvisoDiario.programar(applicationContext, ajustes.horaAviso)
            }
        }

        lifecycleScope.launch {
            val compras = Compras.get(applicationContext)
            // Se espera a que Play diga si hay suscripción, pero no
            // indefinidamente: si no contesta en tres segundos se sigue como si
            // no la hubiera, y el banner desaparecerá solo cuando conteste.
            withTimeoutOrNull(ESPERA_DE_PLAY) { compras.estadoConocido.first { it } }
            if (!compras.sinAnuncios.value) prepararAnuncios(this@MainActivity)
        }
    }

    override fun onResume() {
        super.onResume()
        // Se vuelve aquí después de comprar, de cancelar desde Play o de que
        // caduque el cobro; Play es quien sabe el estado real.
        lifecycleScope.launch { Compras.get(applicationContext).consultarEstado() }
        actualizaciones.alVolver()
    }

    override fun onDestroy() {
        actualizaciones.cerrar()
        super.onDestroy()
    }

    private fun aperturaDe(intento: Intent?): Apertura? {
        val coleccion = intento?.getStringExtra(AvisoDiario.EXTRA_COLECCION) ?: return null
        val codigo = intento.getStringExtra(AvisoDiario.EXTRA_CODIGO) ?: return null
        val capitulo = intento.getIntExtra(AvisoDiario.EXTRA_CAPITULO, 0)
            .takeIf { it > 0 } ?: return null
        return Apertura(coleccion, codigo, capitulo)
    }

    private companion object {
        const val ESPERA_DE_PLAY = 3_000L
    }
}

/**
 * El capítulo que hay que abrir nada más entrar, cuando se viene del aviso de
 * la mañana. Llega por colección y código de libro porque fuera de la base de
 * datos no se conoce el identificador numérico.
 */
data class Apertura(val coleccion: String, val codigo: String, val capitulo: Int)

/**
 * La versión nueva ya se descargó mientras se leía. Se pregunta en vez de
 * reiniciar por las buenas: quien está a media lectura decide cuándo.
 */
@Composable
private fun ActualizacionLista(onReiniciar: () -> Unit, onDespues: () -> Unit) {
    AlertDialog(
        onDismissRequest = onDespues,
        title = { Text("Actualización lista") },
        text = {
            Text(
                "Ya se descargó la versión nueva de la aplicación. Se instala al " +
                    "reiniciarla, y con «Continuar leyendo» vuelves al capítulo " +
                    "donde estabas.",
            )
        },
        confirmButton = { TextButton(onClick = onReiniciar) { Text("Reiniciar") } },
        dismissButton = { TextButton(onClick = onDespues) { Text("Más tarde") } },
    )
}

object Routes {
    const val HOME = "home"
    const val SEARCH = "search"
    const val BOOKMARKS = "bookmarks"
    const val NOTES = "notes"
    const val SETTINGS = "settings"
    fun chapters(bookId: Long) = "chapters/$bookId"
    fun reader(bookId: Long, chapter: Int) = "reader/$bookId/$chapter"
    fun concordance(strong: String, lemma: String) =
        "concordance/$strong/${Uri.encode(lemma.ifBlank { "-" })}"
}

@Composable
fun BibliaApp(
    vm: BibliaViewModel = viewModel(),
    actualizacionLista: Boolean = false,
    onReiniciar: () -> Unit = {},
    onDespues: () -> Unit = {},
    apertura: Apertura? = null,
) {
    val settings by vm.settings.collectAsState()
    val library by vm.library.collectAsState()

    BibliaGriegaTheme(themeMode = settings.theme) {
        // Dentro del tema, para que el diálogo salga con los colores de la app y
        // no con la paleta de fábrica de Material.
        if (actualizacionLista) {
            ActualizacionLista(onReiniciar = onReiniciar, onDespues = onDespues)
        }
        Surface(
            modifier = Modifier.fillMaxSize(),
            color = MaterialTheme.colorScheme.background,
        ) {
            val nav = rememberNavController()

            // Hay que esperar a que la biblioteca esté cargada: antes no se
            // puede traducir «at / SAL» al identificador del libro. Si el libro
            // no aparece, se queda en la portada, que ya muestra el versículo.
            LaunchedEffect(apertura, library.loading) {
                if (apertura == null || library.loading) return@LaunchedEffect
                vm.bookOf(apertura.coleccion, apertura.codigo)?.let { libro ->
                    nav.navigate(Routes.reader(libro.id, apertura.capitulo))
                }
            }

            NavHost(navController = nav, startDestination = Routes.HOME) {
                composable(Routes.HOME) {
                    HomeScreen(
                        vm = vm,
                        onOpenBook = { nav.navigate(Routes.chapters(it)) },
                        onContinue = { ref -> nav.navigate(Routes.reader(ref.bookId, ref.chapter)) },
                        onSearch = { nav.navigate(Routes.SEARCH) },
                        onBookmarks = { nav.navigate(Routes.BOOKMARKS) },
                        onNotes = { nav.navigate(Routes.NOTES) },
                        onSettings = { nav.navigate(Routes.SETTINGS) },
                        onOpenChapterOf = { bookId, chapter ->
                            nav.navigate(Routes.reader(bookId, chapter))
                        },
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
                        onSearch = { nav.navigate(Routes.SEARCH) },
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
                composable(Routes.NOTES) {
                    NotesScreen(
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
