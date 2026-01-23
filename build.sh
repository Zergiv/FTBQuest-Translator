#!/bin/bash

echo "================================"
echo " FTB Quest Translator Builder"
echo "================================"
echo ""

# Verificar que Python esté instalado
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 no está instalado"
    exit 1
fi

echo "[1/4] Instalando dependencias..."
pip3 install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: No se pudieron instalar las dependencias"
    exit 1
fi

echo ""
echo "[2/4] Limpiando builds anteriores..."
rm -rf build dist *.spec

echo ""
echo "[3/4] Compilando ejecutable..."
pyinstaller --onefile \
    --windowed \
    --name "FTBQuestTranslator" \
    --add-data "README.md:." \
    --noconsole \
    translator_gui.py

if [ $? -ne 0 ]; then
    echo "ERROR: No se pudo compilar el ejecutable"
    exit 1
fi

echo ""
echo "[4/4] Limpiando archivos temporales..."
rm -rf build *.spec

echo ""
echo "================================"
echo " Compilación completada!"
echo "================================"
echo ""
echo "El archivo ejecutable está en: dist/FTBQuestTranslator"
echo ""
