# Contributing to FTB Quest Translator

¡Gracias por tu interés en contribuir! 🎉

## Cómo Contribuir

### Reportar Bugs 🐛

Si encuentras un bug, por favor abre un [Issue](https://github.com/Zergiv/FTBQuest-Translator/issues) con:

1. **Descripción clara** del problema
2. **Pasos para reproducir** el error
3. **Comportamiento esperado** vs **comportamiento actual**
4. **Versión** del programa que estás usando
5. **Sistema operativo** (Windows, Linux, macOS)
6. **Capturas de pantalla** si es relevante

### Sugerir Características 💡

Para sugerir nuevas características:

1. Verifica que no exista ya un issue similar
2. Abre un nuevo [Issue](https://github.com/Zergiv/FTBQuest-Translator/issues)
3. Describe claramente la característica
4. Explica por qué sería útil
5. Proporciona ejemplos de uso si es posible

### Pull Requests 🔧

1. **Fork** el repositorio
2. Crea una **rama** para tu feature: `git checkout -b feature/mi-caracteristica`
3. **Commit** tus cambios: `git commit -am 'Add: nueva característica'`
4. **Push** a la rama: `git push origin feature/mi-caracteristica`
5. Abre un **Pull Request**

#### Convenciones de Commits

Usamos prefijos claros:
- `Add:` - Nueva característica
- `Fix:` - Corrección de bug
- `Update:` - Actualización de código existente
- `Refactor:` - Reestructuración sin cambiar funcionalidad
- `Docs:` - Cambios en documentación
- `Style:` - Formato, estilo (no afecta código)
- `Test:` - Añadir o modificar tests

### Desarrollo Local

```bash
# 1. Clona tu fork
git clone https://github.com/TU_USUARIO/FTBQuest-Translator.git
cd FTBQuest-Translator

# 2. Crea un entorno virtual (opcional pero recomendado)
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

# 3. Instala dependencias
pip install -r requirements.txt

# 4. Ejecuta la aplicación
python translator_gui.py

# 5. Para compilar
build.bat  # Windows
./build.sh # Linux/macOS
```

### Estructura del Código

```
FTBQuest-Translator/
├── translator_gui.py      # GUI principal (Tkinter)
├── snbt_translator.py     # Lógica CLI (legacy)
├── requirements.txt       # Dependencias
├── build.bat/build.sh     # Scripts de compilación
└── .github/workflows/     # CI/CD
```

### Guías de Estilo

#### Python
- Sigue [PEP 8](https://pep8.org/)
- Nombres de funciones: `snake_case`
- Nombres de clases: `PascalCase`
- Constantes: `UPPER_CASE`
- Docstrings para funciones complejas

#### UI/UX
- Mantén la interfaz simple y clara
- Usa emojis para mejorar legibilidad
- Colores consistentes con el tema actual
- Mensajes de error claros y accionables

### Testing

Antes de hacer PR, verifica:

- ✅ La aplicación ejecuta sin errores
- ✅ La GUI responde correctamente
- ✅ Los archivos se guardan correctamente
- ✅ La validación funciona
- ✅ No hay regresiones

### Áreas que Necesitan Ayuda

Algunas áreas donde puedes contribuir:

- 🌍 **Traducciones**: Agregar más idiomas a la interfaz
- 🎨 **Temas**: Crear temas personalizables
- 📝 **Documentación**: Mejorar tutoriales y ejemplos
- 🧪 **Tests**: Agregar pruebas unitarias
- 🚀 **Performance**: Optimizar velocidad de traducción
- 🔧 **Features**: 
  - Soporte para archivos múltiples
  - Historial de traducciones
  - Configuraciones guardadas
  - Vista previa de traducción

## Código de Conducta

### Nuestro Compromiso

Nos comprometemos a hacer de la participación en nuestro proyecto una experiencia libre de acoso para todos.

### Comportamiento Esperado

- Usar lenguaje acogedor e inclusivo
- Respetar puntos de vista y experiencias diferentes
- Aceptar críticas constructivas con gracia
- Enfocarse en lo mejor para la comunidad
- Mostrar empatía hacia otros miembros

### Comportamiento Inaceptable

- Uso de lenguaje o imágenes sexualizadas
- Comentarios trolls, insultos o ataques personales
- Acoso público o privado
- Publicar información privada sin permiso
- Otras conductas inapropiadas

## Licencia

Al contribuir, aceptas que tus contribuciones serán licenciadas bajo la misma licencia del proyecto.

## Preguntas

Si tienes preguntas, abre un [Issue](https://github.com/Zergiv/FTBQuest-Translator/issues) o contacta a los mantenedores.

---

¡Gracias por contribuir! 🙏✨
