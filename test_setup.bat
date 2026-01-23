@echo off
echo ================================
echo  Test FTB Quest Translator
echo ================================
echo.

echo [Verificando Python...]
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no instalado
    pause
    exit /b 1
)
echo OK: Python instalado

echo.
echo [Verificando dependencias...]
pip show google-generativeai >nul 2>&1
if errorlevel 1 (
    echo Instalando google-generativeai...
    pip install google-generativeai
) else (
    echo OK: google-generativeai instalado
)

echo.
echo [Probando importaciones...]
python -c "import google.generativeai; print('OK: Gemini API')"
python -c "import tkinter; print('OK: Tkinter')"
python -c "import threading; print('OK: Threading')"
python -c "import pathlib; print('OK: Pathlib')"

echo.
echo [Verificando archivos...]
if exist "translator_gui.py" (
    echo OK: translator_gui.py encontrado
) else (
    echo ERROR: translator_gui.py no encontrado
    pause
    exit /b 1
)

if exist "requirements.txt" (
    echo OK: requirements.txt encontrado
) else (
    echo ERROR: requirements.txt no encontrado
)

if exist "README.md" (
    echo OK: README.md encontrado
) else (
    echo ERROR: README.md no encontrado
)

echo.
echo ================================
echo  Todas las verificaciones OK!
echo ================================
echo.
echo Puedes ejecutar la aplicacion con:
echo   python translator_gui.py
echo.
echo O compilar con:
echo   build.bat
echo.
pause
