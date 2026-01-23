@echo off
echo ================================
echo  FTB Quest Translator Builder
echo ================================
echo.

REM Verificar que Python esté instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en PATH
    echo Por favor instala Python desde https://www.python.org/
    pause
    exit /b 1
)

echo [1/4] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: No se pudieron instalar las dependencias
    pause
    exit /b 1
)

echo.
echo [2/4] Limpiando builds anteriores...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"
if exist "*.spec" del /q "*.spec"

echo.
echo [3/4] Compilando ejecutable...
pyinstaller --onefile ^
    --windowed ^
    --name "FTBQuestTranslator" ^
    --icon=NONE ^
    --add-data "README.md;." ^
    --noconsole ^
    translator_gui.py

if errorlevel 1 (
    echo ERROR: No se pudo compilar el ejecutable
    pause
    exit /b 1
)

echo.
echo [4/4] Limpiando archivos temporales...
rmdir /s /q "build"
del /q "*.spec"

echo.
echo ================================
echo  Compilacion completada!
echo ================================
echo.
echo El archivo ejecutable esta en: dist\FTBQuestTranslator.exe
echo.
pause
