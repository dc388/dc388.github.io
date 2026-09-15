import org.jetbrains.kotlin.gradle.dsl.JvmTarget
import java.io.FileInputStream
import java.util.Properties

plugins {
    alias(libs.plugins.android.application)
    alias(libs.plugins.kotlin.android)
    alias(libs.plugins.kotlin.compose)
}

// Firma de release. En local: app/keystore.properties (ignorado por git).
// En CI: variables de entorno definidas por .github/workflows/release.yml.
val keystorePropertiesFile = rootProject.file("app/keystore.properties")
val keystoreProperties = Properties().apply {
    if (keystorePropertiesFile.exists()) load(FileInputStream(keystorePropertiesFile))
}

fun secret(key: String, env: String): String? =
    keystoreProperties.getProperty(key) ?: System.getenv(env)

// Identificadores de AdMob.
//
// Los de aquí son los de PRUEBA que publica Google: enseñan un anuncio de
// mentira y no pagan nada. Sirven para desarrollar; usar los de verdad mientras
// se prueba va contra las políticas de AdMob y puede costar la cuenta.
//
// Los reales no se guardan en el repositorio: entran por -PadmobAppId=... o por
// las variables de entorno ADMOB_APP_ID y ADMOB_BANNER, que el flujo de
// publicación saca de los secretos de GitHub. Una compilación de release con
// los de prueba falla a propósito, para que no se suba a Play una versión que
// no puede ganar nada. Ver docs/ANUNCIOS_Y_SUSCRIPCION.md.
val admobAppIdDePrueba = "ca-app-pub-3940256099942544~3347511713"
val admobBannerDePrueba = "ca-app-pub-3940256099942544/6300978111"

fun ajuste(propiedad: String, env: String, pruebas: String): String =
    (findProperty(propiedad) as String?)?.takeIf { it.isNotBlank() }
        ?: System.getenv(env)?.takeIf { it.isNotBlank() }
        ?: pruebas

val admobAppId = ajuste("admobAppId", "ADMOB_APP_ID", admobAppIdDePrueba)
val admobBanner = ajuste("admobBanner", "ADMOB_BANNER", admobBannerDePrueba)
val admobEsDePrueba = admobAppId == admobAppIdDePrueba || admobBanner == admobBannerDePrueba

android {
    namespace = "com.dc388.bibliagriega"
    compileSdk = 36

    defaultConfig {
        applicationId = "com.dc388.bibliagriega"
        minSdk = 26
        targetSdk = 36
        versionCode = 1
        versionName = "1.0.0"
        testInstrumentationRunner = "androidx.test.runner.AndroidJUnitRunner"

        // El manifiesto necesita el identificador como recurso; el código, como
        // constante. Se generan los dos aquí para que no puedan discrepar.
        resValue("string", "admob_app_id", admobAppId)
        buildConfigField("String", "ADMOB_APP_ID", "\"$admobAppId\"")
        buildConfigField("String", "ADMOB_BANNER", "\"$admobBanner\"")
        buildConfigField("boolean", "ADMOB_DE_PRUEBA", admobEsDePrueba.toString())
    }

    signingConfigs {
        create("release") {
            // isNullOrBlank y no null: si el flujo de publicación exporta
            // KEYSTORE_FILE vacío porque no hay clave, file("") resuelve al
            // directorio del proyecto, que existe, y la firma se configuraría
            // apuntando a una carpeta.
            val storePath = secret("storeFile", "KEYSTORE_FILE")
            if (!storePath.isNullOrBlank() && file(storePath).exists()) {
                storeFile = file(storePath)
                storePassword = secret("storePassword", "KEYSTORE_PASSWORD")
                keyAlias = secret("keyAlias", "KEY_ALIAS")
                keyPassword = secret("keyPassword", "KEY_PASSWORD")
            }
        }
    }

    buildTypes {
        debug {
            applicationIdSuffix = ".debug"
            versionNameSuffix = "-debug"
        }
        release {
            isMinifyEnabled = true
            isShrinkResources = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro",
            )
            // Solo firma si hay keystore disponible; si no, genera un APK sin firmar.
            signingConfig = signingConfigs.getByName("release")
                .takeIf { it.storeFile != null }
        }
    }

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    buildFeatures {
        compose = true
        buildConfig = true
    }

    packaging {
        resources {
            excludes += "/META-INF/{AL2.0,LGPL2.1}"
        }
    }

    bundle {
        language {
            // No dividir por idioma: la app trae su propio texto griego.
            enableSplit = false
        }
    }
}

// Una release con los anuncios de prueba se ve idéntica y no ingresa un céntimo,
// así que es mejor que no compile. Para generar una release de prueba a
// propósito —probar la firma, por ejemplo— basta con -PadmobPruebasEnRelease=true.
tasks.matching { it.name == "bundleRelease" || it.name == "assembleRelease" }
    .configureEach {
        doFirst {
            val permitido = (findProperty("admobPruebasEnRelease") as String?) == "true"
            if (admobEsDePrueba && !permitido) {
                throw GradleException(
                    "Esta compilación de publicación lleva los anuncios de prueba de Google, " +
                        "que no pagan nada. Define ADMOB_APP_ID y ADMOB_BANNER con los " +
                        "identificadores de tu cuenta de AdMob (docs/ANUNCIOS_Y_SUSCRIPCION.md), " +
                        "o añade -PadmobPruebasEnRelease=true si de verdad quieres una " +
                        "release sin anuncios reales.",
                )
            }
        }
    }

kotlin {
    compilerOptions {
        jvmTarget.set(JvmTarget.JVM_17)
    }
}

dependencies {
    implementation(libs.androidx.core.ktx)
    implementation(libs.androidx.lifecycle.runtime.ktx)
    implementation(libs.androidx.lifecycle.viewmodel.compose)
    implementation(libs.androidx.activity.compose)

    implementation(platform(libs.androidx.compose.bom))
    implementation(libs.androidx.ui)
    implementation(libs.androidx.ui.graphics)
    implementation(libs.androidx.ui.tooling.preview)
    implementation(libs.androidx.material3)
    implementation(libs.androidx.material.icons.extended)
    implementation(libs.androidx.navigation.compose)
    implementation(libs.androidx.datastore.preferences)

    // Anuncios, consentimiento para el espacio europeo y suscripción para quitarlos.
    implementation(libs.play.services.ads)
    implementation(libs.user.messaging.platform)
    implementation(libs.billing.ktx)

    debugImplementation(libs.androidx.ui.tooling)

    testImplementation(libs.junit)

    androidTestImplementation(libs.junit)
    androidTestImplementation(libs.androidx.test.junit)
    androidTestImplementation(libs.androidx.espresso.core)
    // Captura de pantalla completa, con barra de estado: las de Compose
    // solo fotografían el árbol de Compose y salen sin el marco del sistema.
    androidTestImplementation(libs.androidx.uiautomator)
    androidTestImplementation(platform(libs.androidx.compose.bom))
    androidTestImplementation(libs.androidx.ui.test.junit4)
    debugImplementation(libs.androidx.ui.test.manifest)
}
