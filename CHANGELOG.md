# Changelog

All notable changes to this project will be documented in this file.

## [1.1.0] - 2026-02-25

### Changed
- 🔍 Reescrita completa de la búsqueda automática de archivos: ahora busca directamente en rutas conocidas de launchers (ATLauncher, CurseForge, MultiMC, PrismLauncher, Modrinth, FTB App) usando el patrón `config/ftbquests/quests/lang`
- 🚀 Al abrir la aplicación, se buscan archivos automáticamente y se muestra un diálogo para elegir cuál traducir
- ⚡ Búsqueda mucho más rápida: ya no escanea carpetas innecesarias como Users o Program Files completos

### Fixed
- 🐛 Corregido el problema de que la búsqueda tardaba mucho escaneando 7+ ubicaciones irrelevantes
- 🐛 Corregido que se excluía la carpeta AppData del escaneo, donde la mayoría de launchers guardan sus instancias

## [1.0.0] - 2026-01-23

### Added
- 🖥️ Modern GUI with dark theme interface
- 🔍 Automatic detection of quest files in common Minecraft locations
- 💾 API key persistence (save and load automatically)
- 📊 Real-time progress tracking with detailed logs
- 🌐 Multi-language support dropdown
- 📦 Configurable batch size
- 🔧 Windows build script (`build.bat`)
- 🔧 Linux/macOS build script (`build.sh`)
- 🤖 GitHub Actions workflow for automated builds
- 📁 Manual file browser for input/output files
- ⚡ Threading support for non-blocking UI
- ✅ Input validation before starting translation
- 🎨 Modern, clean interface design
- 📝 Comprehensive documentation (README, QUICK_START, GITHUB_SETUP)

### Changed
- Refactored translation logic into GUI application
- Improved error handling and user feedback
- Updated README with GUI instructions and screenshots
- Enhanced .gitignore with build artifacts

### Features
- Single executable, no installation required
- Cross-platform support (Windows, Linux, macOS)
- Auto-detection of Minecraft quest files
- Real-time translation progress
- Safe validation system
- Color code preservation
- Structure integrity checks

## [0.1.0] - Initial Release

### Added
- Initial CLI-based translator
- Basic translation functionality
- Gemini API integration
- SNBT file validation
- Color code preservation
- Batch processing

---

## Release Notes Template

Use this template for future releases:

## [X.Y.Z] - YYYY-MM-DD

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Vulnerability fixes
