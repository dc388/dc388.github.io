# Copia de trabajo

Esta carpeta es una **copia de resguardo** del proyecto
`biblia-septuaginta-griega-android`, guardada aquí porque la sesión que lo generó
no tenía permiso para crear repositorios en GitHub.

Su destino es un **repositorio propio**. Para moverlo:

```bash
# 1. Crea el repositorio vacío en https://github.com/new
#    (sin README, sin .gitignore, sin licencia)

# 2. Publícalo desde esta carpeta
cd biblia-septuaginta-griega-android
python3 tools/build_db.py          # regenera app/src/main/assets/biblia.db
rm COPIA-DE-TRABAJO.md
git init -b main
git add -A
git commit -m "Biblia en lenguas originales: hebreo y griego con interlineal"
git remote add origin https://github.com/dc388/biblia-septuaginta-griega-android.git
git push -u origin main
```

Después puedes borrar esta carpeta de `dc388.github.io`.

## Qué falta aquí respecto al proyecto completo

Solo `app/src/main/assets/biblia.db` (63 MB), que no se subió a este repositorio
de sitio web para no engordarlo. `python3 tools/build_db.py` lo reconstruye
exactamente igual: clona las seis fuentes originales, limpia los artefactos de
OCR, alinea los interlineales hebreo y griego con sus números Strong y su
morfología, carga los léxicos y verifica siete invariantes antes de dar la base
por buena. Tarda unos minutos, casi todo en clonar.

**No fusiones esta rama en `main`**: `main` publica dc388.github.io.
