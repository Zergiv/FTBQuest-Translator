# 🌍 Traductor de Archivos SNBT para FTB Quests

[![Licencia: MIT](https://img.shields.io/badge/Licencia-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![API Gemini](https://img.shields.io/badge/API-Gemini%202.5-orange.svg)](https://ai.google.dev/)

Traduce automáticamente archivos de idioma `.snbt` de FTB Quests usando la API de Gemini de Google, preservando la estructura del archivo, códigos de color y formato. ¡Perfecto para creadores de modpacks que quieren hacer sus misiones accesibles en múltiples idiomas!

## 📋 Tabla de Contenidos

- [Acerca de](#-acerca-de)
- [Características](#-características)
- [Requisitos](#-requisitos)
- [Instalación](#-instalación)
- [Configuración](#-configuración)
- [Uso](#-uso)
- [Cómo Funciona](#-cómo-funciona)
- [Notas Importantes](#-notas-importantes)
- [Resultados](#-resultados)
- [Solución de Problemas](#-solución-de-problemas)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## 📖 Acerca de

**Este traductor está diseñado para FTB Quests 1.21+** donde el mod introdujo su propio sistema de idiomas, generando archivos `.snbt` ubicados en:

```
carpeta_raiz_minecraft/config/ftbquests/quests/lang/
```

Estos archivos son extremadamente sensibles - incluso un pequeño error de formato puede romper todo el libro de misiones. Este script usa traducción con IA y validación integrada para garantizar **100% de integridad del archivo** mientras traduce aproximadamente **80-90%** del contenido automáticamente.

### ¿Por Qué Esta Herramienta?

- ✅ Maneja archivos de 6000+ líneas automáticamente
- ✅ Preserva códigos de color de Minecraft (`&a`, `&e`, etc.)
- ✅ Mantiene estructura JSON y arrays
- ✅ Valida cada traducción
- ✅ Respaldo seguro al texto original en caso de errores
- ✅ Procesamiento por lotes con seguimiento de progreso

## ✨ Características

- 🤖 **Traducción con IA**: Usa Google Gemini 2.5 Flash para traducciones precisas
- 🔒 **Seguro por Diseño**: Valida cada línea y mantiene originales en caso de error
- 🎨 **Preservación de Códigos de Color**: Mantiene todos los códigos de formato de Minecraft
- 📊 **Seguimiento de Progreso**: Retroalimentación en tiempo real sobre el progreso de traducción
- 🔄 **Procesamiento por Lotes**: Maneja archivos grandes eficientemente
- ⚡ **Rápido y Confiable**: Procesa 50 líneas por lote con recuperación de errores

## 📦 Requisitos

- Python 3.8 o superior
- Clave API de Google Gemini (tier gratuito disponible)
- Conexión a internet

## 🚀 Instalación

1. **Clona este repositorio**:
   ```bash
   git clone https://github.com/tuusuario/snbt-translator.git
   cd snbt-translator
   ```

2. **Instala las dependencias**:
   ```bash
   pip install google-generativeai
   ```

3. **Obtén tu clave API de Gemini**:
   - Visita [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Crea una nueva clave API (¡es gratis!)
   - Copia tu clave

## ⚙️ Configuración

1. **Abre `snbt_translator.py` y configura**:

```python
# Reemplaza con tu clave API
GEMINI_API_KEY = "TU_CLAVE_API_AQUI"

# Configuración de archivos
INPUT_FILE = "en_us.snbt"      # Archivo de idioma origen
OUTPUT_FILE = "es_es.snbt"     # Archivo de idioma destino
TARGET_LANGUAGE = "Spanish"    # Nombre del idioma destino
BATCH_SIZE = 50                # Líneas por lote
```

2. **Establece el nombre de archivo de salida correcto**:

Según los [códigos de idioma de Minecraft](https://minecraft.fandom.com/wiki/Language), usa el formato apropiado:

| Idioma | Código | Nombre de Archivo |
|--------|--------|-------------------|
| Inglés (US) | `en_us` | `en_us.snbt` |
| Español (España) | `es_es` | `es_es.snbt` |
| Español (México) | `es_mx` | `es_mx.snbt` |
| Francés | `fr_fr` | `fr_fr.snbt` |
| Alemán | `de_de` | `de_de.snbt` |
| Portugués (Brasil) | `pt_br` | `pt_br.snbt` |
| Chino (Simplificado) | `zh_cn` | `zh_cn.snbt` |
| Japonés | `ja_jp` | `ja_jp.snbt` |

**Lista completa**: [Códigos de Idioma de Minecraft](https://minecraft.fandom.com/wiki/Language)

## 🎯 Uso

### Paso 1: Localiza tus Archivos de Misiones

Navega a la carpeta de tu instancia de Minecraft:
```
carpeta_raiz_minecraft/config/ftbquests/quests/lang/
```

### Paso 2: Copia el Archivo

Copia el archivo de idioma que quieres traducir (usualmente `en_us.snbt`) al directorio del script.

### Paso 3: Ejecuta el Script

```bash
python snbt_translator.py
```

### Paso 4: Sigue las Instrucciones

```
============================================================
SNBT FILE TRANSLATOR - FTB QUESTS
============================================================

Configuration:
  - Input file: en_us.snbt
  - Output file: es_es.snbt
  - Target language: Spanish
  - Batch size: 50 lines

Do you want to continue? (y/n): y
```

### Paso 5: Espera a que Complete

El script procesará tu archivo en lotes, mostrando el progreso:

```
Processing batch 1/120 (lines 1-50)
  - 45 translatable lines found
  ⚠️  Line 127: Color codes altered - using original
  ⚠️  2 lines with errors - keeping originals

Processing batch 2/120 (lines 51-100)
  - 48 translatable lines found

...

✅ Translation complete! File saved at: es_es.snbt
```

### Paso 6: Copia el Archivo Traducido

Copia el archivo generado de vuelta a:
```
carpeta_raiz_minecraft/config/ftbquests/quests/lang/
```

### Paso 7: Retoques Manuales (Opcional)

Para el 10-20% de líneas que no fueron traducidas (debido a errores de validación), puedes traducirlas manualmente usando cualquier editor de texto que soporte archivos `.snbt` (VS Code, Notepad++, etc.).

## 🔧 Cómo Funciona

1. **Lectura del Archivo**: Carga el archivo `.snbt` completo
2. **Identificación de Líneas**: Detecta qué líneas contienen texto traducible
3. **Traducción por Lotes**: Envía 50 líneas a la vez a la API de Gemini con reglas estrictas
4. **Validación**: Cada traducción se verifica por:
   - Conteo correcto de comillas
   - Códigos de color preservados
   - Estructura mantenida (corchetes, llaves, dos puntos)
   - Claves sin cambios (IDs de misiones, IDs de capítulos)
5. **Respaldo Seguro**: Si la validación falla, se mantiene la línea original
6. **Salida del Archivo**: Escribe la traducción validada al archivo de salida

## ⚠️ Notas Importantes

### Sensibilidad del Archivo

Los archivos `.snbt` son **extremadamente sensibles**. Un solo carácter mal ubicado puede romper todo el libro de misiones. Por eso este script:

- ✅ Valida cada línea individualmente
- ✅ Mantiene el texto original si la validación falla
- ✅ Nunca modifica la estructura o el formato
- ✅ Solo traduce texto dentro de comillas

### Cobertura de Traducción

- **Esperado**: 80-90% de traducción automática
- **Restante**: 10-20% mantenido como original (debido a formato complejo)
- **Solución**: Traducir líneas restantes manualmente en un editor de texto

### ¿Por Qué No 100%?

Algunas líneas tienen estructuras JSON complejas, comillas anidadas o formato especial que es muy arriesgado auto-traducir. El script prioriza **integridad del archivo** sobre traducción completa.

## 📸 Resultados

Así se ve un libro de misiones traducido:

### Antes de la Traducción
![Misión Original en Inglés](https://i.ibb.co/MxcP3spF/Screenshot-3.jpg)

### Después de la Traducción
![Misión Traducida 1](https://i.ibb.co/C560WV6n/Screenshot-7.jpg)
![Misión Traducida 2](https://i.ibb.co/kgC9KNCZ/Screenshot-6.jpg)
![Misión Traducida 3](https://i.ibb.co/DgsYCNZ9/Screenshot-5.jpg)
![Misión Traducida 4](https://i.ibb.co/Q7JnvfJd/Screenshot-4.jpg)

¡Como puedes ver, los códigos de color, formato y estructura están perfectamente preservados! 🎉

## 🐛 Solución de Problemas

### Error "File not found"
- Asegúrate de que `en_us.snbt` está en el mismo directorio que el script
- Verifica que el nombre del archivo coincida exactamente (sensible a mayúsculas)

### Errores de API
- Verifica que tu clave API sea correcta
- Revisa tu conexión a internet
- Asegúrate de no haber excedido los límites de tasa de la API

### Muchos Errores de Validación
- ¡Esto es normal! El script mantiene los originales por seguridad
- Puedes traducir manualmente las líneas omitidas más tarde
- Considera reducir `BATCH_SIZE` a 25 para mayor precisión

### El Libro de Misiones No Carga
- Asegúrate de que el nombre del archivo de salida coincida con el código de idioma de Minecraft
- Verifica que el archivo esté en la carpeta correcta
- Verifica que el archivo no se haya corrompido (vuelve a ejecutar el script)

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Por favor, siéntete libre de enviar un Pull Request.

1. Haz fork del repositorio
2. Crea tu rama de características (`git checkout -b feature/CaracteristicaIncreible`)
3. Haz commit de tus cambios (`git commit -m 'Agrega alguna CaracterísticaIncreible'`)
4. Haz push a la rama (`git push origin feature/CaracteristicaIncreible`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulta el archivo [LICENSE](LICENSE) para más detalles.

## 🙏 Agradecimientos

- Equipo de FTB por crear FTB Quests
- Google por la API de Gemini
- La comunidad de modding de Minecraft

---

Hecho con ❤️ para la comunidad de modding

**¡Dale una estrella ⭐ a este repo si te ayudó!**