# 🌍 SNBT File Translator for FTB Quests

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/API-Gemini%202.5-orange.svg)](https://ai.google.dev/)
[![Made by AI](https://img.shields.io/badge/Made%20by-AI-lightgrey)](https://github.com/mefengl/made-by-ai)
[![Build Status](https://img.shields.io/github/actions/workflow/status/Zergiv/FTBQuest-Translator/build.yml)](https://github.com/Zergiv/FTBQuest-Translator/actions)
[![Latest Release](https://img.shields.io/github/v/release/Zergiv/FTBQuest-Translator)](https://github.com/Zergiv/FTBQuest-Translator/releases)

Automatically translate FTB Quests `.snbt` language files using Google's Gemini API while preserving file structure, color codes, and formatting. Perfect for modpack creators who want to make their quests accessible in multiple languages!


## 🚀 Quick Start (GUI Version)

### Option 1: Download Pre-built Executable (Recommended)

1. **Download the latest release**: Go to [Releases](https://github.com/Zergiv/FTBQuest-Translator/releases) and download the executable:
   - Windows: `FTBQuestTranslator.exe`

2. **Run the application**: Double-click the executable (no installation required!)

3. **Configure and translate**:
   - Enter your Gemini API Key
   - Select input/output files or let it auto-detect
   - Choose target language
   - Click "Iniciar Traducción"

### Option 2: Run from Source

```bash
# Clone repository
git clone https://github.com/Zergiv/FTBQuest-Translator.git
cd FTBQuest-Translator

# Install dependencies
pip install -r requirements.txt

# Run GUI
python translator_gui.py
```

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Usage](#-usage)
  - [GUI Version](#gui-version-recommended)
  - [CLI Version](#cli-version-advanced)
- [Building from Source](#-building-from-source)
- [How It Works](#-how-it-works)
- [Important Notes](#-important-notes)
- [Results](#-results)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)

## 📖 About

**This translator is designed for FTB Quests 1.21+** where the mod introduced its own language system, generating `.snbt` files located in:

```
minecraft_root_folder/config/ftbquests/quests/lang/
```

These files are extremely sensitive - even a small formatting error can break the entire quest book. This script uses AI-powered translation with built-in validation to help translate the content while trying to maintain file integrity.

## ✨ Features

- 🖥️ **Modern GUI**: Clean, intuitive interface with dark theme
- 🔍 **Auto-Detection**: Automatically finds quest files in common locations
- 🤖 **AI-Powered Translation**: Uses Google Gemini 2.5 Flash for accurate translations
- 🔒 **Safe by Design**: Validates each line and keeps originals on error
- 🎨 **Color Code Preservation**: Maintains all Minecraft formatting codes
- 📊 **Progress Tracking**: Real-time feedback on translation progress
- 🔄 **Batch Processing**: Efficiently handles large files
- ⚡ **Fast & Reliable**: Processes 50 lines per batch with error recovery
- 💾 **Portable**: Single executable, no installation needed
- 🔧 **GitHub Actions**: Automated builds for Windows, Linux, and macOS

## 📦 Requirements

### For Pre-built Executable:
- **Nothing!** Just download and run

### For Running from Source:
- Python 3.8 or higher
- Google Gemini API key (free tier available)
- Internet connection

## 🚀 Installation

### Using Pre-built Executable (Easiest)

1. Go to [Releases](https://github.com/Zergiv/FTBQuest-Translator/releases)
2. Download the latest version for your OS
3. Run the executable - that's it!

### From Source

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Zergiv/FTBQuest-Translator.git
   cd FTBQuest-Translator
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get your Gemini API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key (it's free!)
   - Copy your key

## 🎯 Usage

### GUI Version (Recommended)

1. **Run the application**:
   - Double-click the executable, or
   - Run `python translator_gui.py` from source

2. **Enter API Key**:
   - Paste your Gemini API key in the first field
   - Click the 💾 button to save it for future use

3. **Select Files**:
   - Click 🔍 to auto-detect quest files, or
   - Click 📁 to manually browse for files
   - Choose your output file location

4. **Configure**:
   - Select target language from dropdown
   - Adjust batch size if needed (default: 50)

5. **Translate**:
   - Click "🚀 Iniciar Traducción"
   - Monitor progress in the log window
   - Wait for completion message

### CLI Version (Advanced)

For the command-line version, edit `snbt_translator.py`:

```python
# Replace with your API key
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

# File configuration
INPUT_FILE = "en_us.snbt"      # Source language file
OUTPUT_FILE = "es_es.snbt"     # Target language file
TARGET_LANGUAGE = "Spanish"    # Target language name
BATCH_SIZE = 50                # Lines per batch
```

Then run:
```bash
python snbt_translator.py
```

### Supported Languages

According to [Minecraft's language codes](https://minecraft.fandom.com/wiki/Language), use the proper format:

| Language | Code | Filename |
|----------|------|----------|
| English (US) | `en_us` | `en_us.snbt` |
| Spanish (Spain) | `es_es` | `es_es.snbt` |
| Spanish (Mexico) | `es_mx` | `es_mx.snbt` |
| French | `fr_fr` | `fr_fr.snbt` |
| German | `de_de` | `de_de.snbt` |
| Portuguese (Brazil) | `pt_br` | `pt_br.snbt` |
| Chinese (Simplified) | `zh_cn` | `zh_cn.snbt` |
| Japanese | `ja_jp` | `ja_jp.snbt` |

**Full list**: [Minecraft Language Codes](https://minecraft.fandom.com/wiki/Language)

## 🛠️ Building from Source

### Windows

```bash
# Run the build script
build.bat
```

### Linux/macOS

```bash
# Make script executable
chmod +x build.sh

# Run the build script
./build.sh
```

The executable will be created in the `dist/` folder.

### Manual Build

```bash
# Install PyInstaller
pip install pyinstaller

# Build executable
pyinstaller --onefile --windowed --name "FTBQuestTranslator" --noconsole translator_gui.py
```


## 🔧 How It Works

1. **File Reading**: Loads the entire `.snbt` file
2. **Auto-Detection**: Searches for quest files in common Minecraft locations
3. **Line Identification**: Detects which lines contain translatable text
4. **Batch Translation**: Sends 50 lines at a time to Gemini API with strict rules
5. **Validation**: Each translation is checked for:
   - Correct quote count
   - Preserved color codes
   - Maintained structure (brackets, braces, colons)
   - Unchanged keys (quest IDs, chapter IDs)
6. **Safe Fallback**: If validation fails, the original line is kept
7. **File Output**: Writes the validated translation to the output file
8. **Progress Tracking**: Real-time updates in the GUI log window

## ⚠️ Important Notes

### File Sensitivity

`.snbt` files are **extremely sensitive**. A single misplaced character can break the entire quest book. That's why this script:

- ✅ Validates every single line
- ✅ Keeps original text if validation fails
- ✅ Never modifies structure or formatting
- ✅ Only translates text inside quotes

### Translation Coverage

- **Expected**: 80-90% automatic translation
- **Remaining**: 10-20% kept as original (due to complex formatting)
- **Solution**: Manually translate remaining lines in a text editor

### Why Not 100%?

Some lines have complex JSON structures, nested quotes, or special formatting that's too risky to auto-translate. The script prioritizes **file integrity** over complete translation.

## 📸 Results

Here's what a translated quest book looks like after translation:

![Translated Quest Examples](https://i.postimg.cc/pXKfc1tX/photo-collage-png.png)

The tool preserves color codes, formatting, and structure in most cases.

## 🐛 Troubleshooting

### "File not found" Error
- Click the 🔍 auto-detect button in the GUI
- Manually browse for the file with 📁
- Make sure `en_us.snbt` exists in your quest folder
- Check the filename matches exactly (case-sensitive)

### API Errors
- Verify your API key is correct
- Click 💾 to save the API key
- Check your internet connection
- Ensure you haven't exceeded API rate limits (free tier has limits)

### Many Validation Errors
- This is normal! The script keeps originals for safety
- You can manually translate skipped lines later
- Consider reducing batch size to 25 for more accuracy
- Complex JSON structures may be skipped automatically

### Quest Book Not Loading in Minecraft
- Make sure the output filename matches Minecraft's language code
- Check the file is in the correct folder: `config/ftbquests/quests/lang/`
- Verify the file wasn't corrupted (check file size)
- Re-run the script if needed

### GUI Not Opening
- Make sure you downloaded the correct version for your OS
- On Linux/macOS, make the file executable: `chmod +x FTBQuestTranslator`
- Try running from source: `python translator_gui.py`
- Check if Python 3.8+ is installed

### Build Issues
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Update PyInstaller: `pip install --upgrade pyinstaller`
- Check Python version: `python --version` (must be 3.8+)

## 🤝 Contributing

Contributions are welcome! Feel free to:

- 🐛 Report bugs
- 💡 Suggest features
- 🔧 Submit pull requests
- 📚 Improve documentation

## 📄 License

This project is open source and available for free use.

## 🙏 Acknowledgments

- FTB Team for creating FTB Quests
- Google for the Gemini API
- The Minecraft modding community

---

Made with ❤️ for the modding community

**Star ⭐ this repo if it helped you!**
