# 📤 Instrucciones para Subir a GitHub

## Configuración Inicial

### 1. Inicializar repositorio (si no lo has hecho)

```bash
cd "c:\Users\zergi\Documents\FTBQuestTranslator\FTBQuest-Translator"
git init
git branch -M main
```

### 2. Conectar con GitHub

Primero crea un repositorio en GitHub:
- Ve a https://github.com/new
- Nombre: `FTBQuest-Translator`
- Descripción: "AI-powered SNBT translator for FTB Quests with GUI"
- Público o Privado según prefieras
- **NO** inicialices con README (ya tienes uno)

Luego conecta tu repositorio local:

```bash
git remote add origin https://github.com/TU_USUARIO/FTBQuest-Translator.git
```

### 3. Primer commit y push

```bash
# Agregar todos los archivos
git add .

# Hacer commit
git commit -m "Initial commit: GUI translator with auto-detection and GitHub Actions"

# Subir a GitHub
git push -u origin main
```

## Crear tu Primera Release

### Opción 1: Con GitHub Actions (Automático)

GitHub Actions compilará automáticamente los ejecutables para ti:

```bash
# Crea un tag de versión
git tag v1.0.0

# Sube el tag
git push origin v1.0.0
```

GitHub Actions automáticamente:
1. ✅ Compilará ejecutables para Windows, Linux y macOS
2. ✅ Creará una release con los archivos
3. ✅ Los usuarios podrán descargar los .exe directamente

### Opción 2: Manual (si quieres compilar tú mismo)

1. Compila localmente:
```bash
build.bat  # En Windows
# o
./build.sh  # En Linux/macOS
```

2. Ve a GitHub → Tu repositorio → Releases → "Create a new release"
3. Elige un tag (ej: `v1.0.0`)
4. Sube los archivos de `dist/`
5. Publica la release

## Actualizaciones Futuras

Cada vez que hagas cambios:

```bash
# 1. Guarda tus cambios
git add .
git commit -m "Descripción de los cambios"
git push

# 2. Para crear una nueva release:
git tag v1.1.0
git push origin v1.1.0
```

¡GitHub Actions se encargará del resto automáticamente!

## Verificar GitHub Actions

Después de hacer push:

1. Ve a tu repositorio en GitHub
2. Click en la pestaña "Actions"
3. Verás el workflow "Build Executable" ejecutándose
4. Espera a que termine (5-10 minutos)
5. Los ejecutables estarán en:
   - Artifacts (para cada push)
   - Releases (solo para tags)

## Estructura del Repositorio

```
FTBQuest-Translator/
├── .github/
│   └── workflows/
│       └── build.yml          # GitHub Actions config
├── .gitignore                 # Archivos a ignorar
├── README.md                  # Documentación principal
├── QUICK_START.md             # Guía rápida
├── requirements.txt           # Dependencias Python
├── translator_gui.py          # Aplicación GUI
├── snbt_translator.py         # Script CLI (legacy)
├── build.bat                  # Script de build para Windows
└── build.sh                   # Script de build para Linux/macOS
```

## Archivos Ignorados (.gitignore)

Estos archivos NO se subirán a GitHub (y está bien):
- `config.txt` - Tu API key personal
- `*.snbt` - Archivos de usuario
- `build/`, `dist/` - Archivos compilados
- `__pycache__/` - Archivos temporales Python

## Consejos

✅ **Commits frecuentes** - Haz commit cada vez que completes una característica  
✅ **Tags semánticos** - Usa v1.0.0, v1.1.0, v2.0.0, etc.  
✅ **Mensajes claros** - Describe qué cambios hiciste  
✅ **GitHub Actions** - Deja que compile automáticamente  

## Solución de Problemas

### Error: "remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/TU_USUARIO/FTBQuest-Translator.git
```

### Error: "refusing to merge unrelated histories"
```bash
git pull origin main --allow-unrelated-histories
```

### GitHub Actions falla
1. Ve a Actions → Click en el workflow fallido
2. Lee el log de errores
3. Usualmente son problemas de sintaxis en build.yml

---

¡Listo! Tu herramienta estará disponible para todo el mundo 🌍
