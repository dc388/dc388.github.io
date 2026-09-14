package com.dc388.bibliagriega.ui

import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.WindowInsetsSides
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.only
import androidx.compose.foundation.layout.safeDrawing
import androidx.compose.foundation.layout.widthIn
import androidx.compose.foundation.layout.windowInsetsPadding
import androidx.compose.foundation.layout.wrapContentWidth
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * Ancho máximo de una columna de texto.
 *
 * En un teléfono no cambia nada: la pantalla es más estrecha que esto y el
 * contenido la ocupa entera. Importa en tabletas, en horizontal y en pantalla
 * dividida, donde una línea de 1 000 dp obliga a barrer la cabeza de un lado a
 * otro y se pierde el renglón al volver. 680 dp deja unos 70 u 80 caracteres por
 * línea con el cuerpo predeterminado, que es lo que llevan usando los libros
 * desde hace siglos.
 */
val AnchoDeLectura: Dp = 680.dp

/** Las rejillas y las listas aguantan más ancho que el texto seguido. */
val AnchoDeLista: Dp = 840.dp

/**
 * Ocupa la pantalla, se aparta de los recortes laterales —muescas y barras de
 * navegación cuando el teléfono está tumbado— y, si sobra sitio, se queda en el
 * centro con un ancho legible en vez de estirarse.
 */
fun Modifier.columna(ancho: Dp = AnchoDeLectura): Modifier =
    this.fillMaxSize()
        .windowInsetsPadding(WindowInsets.safeDrawing.only(WindowInsetsSides.Horizontal))
        .wrapContentWidth(Alignment.CenterHorizontally)
        .widthIn(max = ancho)
