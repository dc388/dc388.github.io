package com.dc388.bibliagriega.ui.theme

import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import com.dc388.bibliagriega.data.ThemeMode

// Paleta sobria de pergamino y tinta: el texto griego es el protagonista.
private val Ink = Color(0xFF1B1C22)
private val Parchment = Color(0xFFFBF7F0)
private val ParchmentDim = Color(0xFFF2EBDF)
private val Gold = Color(0xFF9A6E1F)
private val GoldLight = Color(0xFFE8B04B)
private val Indigo = Color(0xFF3E4A66)
private val IndigoLight = Color(0xFFAEBBDA)
private val NightSurface = Color(0xFF1A1B22)
private val Night = Color(0xFF12131A)

private val LightColors = lightColorScheme(
    primary = Indigo,
    onPrimary = Color.White,
    primaryContainer = Color(0xFFDCE2F2),
    onPrimaryContainer = Color(0xFF18203A),
    secondary = Gold,
    onSecondary = Color.White,
    secondaryContainer = Color(0xFFF6E6C8),
    onSecondaryContainer = Color(0xFF3D2B06),
    background = Parchment,
    onBackground = Ink,
    surface = Parchment,
    onSurface = Ink,
    surfaceVariant = ParchmentDim,
    onSurfaceVariant = Color(0xFF4C4A44),
    outlineVariant = Color(0xFFDED5C4),
)

private val DarkColors = darkColorScheme(
    primary = IndigoLight,
    onPrimary = Color(0xFF17203A),
    primaryContainer = Color(0xFF2C3550),
    onPrimaryContainer = Color(0xFFDCE2F2),
    secondary = GoldLight,
    onSecondary = Color(0xFF3D2B06),
    secondaryContainer = Color(0xFF4A3813),
    onSecondaryContainer = Color(0xFFF6E6C8),
    background = Night,
    onBackground = Color(0xFFE7E3DA),
    surface = Night,
    onSurface = Color(0xFFE7E3DA),
    surfaceVariant = NightSurface,
    onSurfaceVariant = Color(0xFFB9B4A9),
    outlineVariant = Color(0xFF33343C),
)

@Composable
fun BibliaGriegaTheme(
    themeMode: ThemeMode = ThemeMode.SYSTEM,
    content: @Composable () -> Unit,
) {
    val dark = when (themeMode) {
        ThemeMode.SYSTEM -> isSystemInDarkTheme()
        ThemeMode.LIGHT -> false
        ThemeMode.DARK -> true
    }
    MaterialTheme(
        colorScheme = if (dark) DarkColors else LightColors,
        typography = BibliaTypography,
        content = content,
    )
}
