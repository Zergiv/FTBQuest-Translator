# 🌍 SNBT File Translator for FTB Quests

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/API-Gemini%202.5-orange.svg)](https://ai.google.dev/)

Automatically translate FTB Quests `.snbt` language files using Google's Gemini API while preserving file structure, color codes, and formatting. Perfect for modpack creators who want to make their quests accessible in multiple languages!

## 📋 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
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

- 🤖 **AI-Powered Translation**: Uses Google Gemini 2.5 Flash for accurate translations
- 🔒 **Safe by Design**: Validates each line and keeps originals on error
- 🎨 **Color Code Preservation**: Maintains all Minecraft formatting codes
- 📊 **Progress Tracking**: Real-time feedback on translation progress
- 🔄 **Batch Processing**: Efficiently handles large files
- ⚡ **Fast & Reliable**: Processes 50 lines per batch with error recovery

## 📦 Requirements

- Python 3.8 or higher
- Google Gemini API key (free tier available)
- Internet connection

## 🚀 Installation

1. **Clone this repository**:
   ```bash
   git clone https://github.com/Zergiv/FTBQuest-Translator.git
   cd FTBQuest-Translator
   ```

2. **Install dependencies**:
   ```bash
   pip install google-generativeai
   ```

3. **Get your Gemini API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Create a new API key (it's free!)
   - Copy your key

## ⚙️ Configuration

1. **Open `snbt_translator.py` and configure**:

```python
# Replace with your API key
GEMINI_API_KEY = "YOUR_API_KEY_HERE"

# File configuration
INPUT_FILE = "en_us.snbt"      # Source language file
OUTPUT_FILE = "es_es.snbt"     # Target language file
TARGET_LANGUAGE = "Spanish"    # Target language name
BATCH_SIZE = 50                # Lines per batch
```

2. **Set the correct output filename**:

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

## 🎯 Usage

### Step 1: Locate Your Quest Files

Navigate to your Minecraft instance folder:
```
minecraft_root_folder/config/ftbquests/quests/lang/
```

### Step 2: Copy the File

Copy the language file you want to translate (usually `en_us.snbt`) to the script directory.

### Step 3: Run the Script

```bash
python snbt_translator.py
```

### Step 4: Follow the Prompts

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

### Step 5: Wait for Completion

The script will process your file in batches, showing progress:

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

### Step 6: Copy the Translated File

Copy the generated file back to:
```
minecraft_root_folder/config/ftbquests/quests/lang/
```

### Step 7: Manual Touch-ups (Optional)

For the 10-20% of lines that weren't translated (due to validation errors), you can manually translate them using any text editor that supports `.snbt` files (VS Code, Notepad++, etc.).

## 🔧 How It Works

1. **File Reading**: Loads the entire `.snbt` file
2. **Line Identification**: Detects which lines contain translatable text
3. **Batch Translation**: Sends 50 lines at a time to Gemini API with strict rules
4. **Validation**: Each translation is checked for:
   - Correct quote count
   - Preserved color codes
   - Maintained structure (brackets, braces, colons)
   - Unchanged keys (quest IDs, chapter IDs)
5. **Safe Fallback**: If validation fails, the original line is kept
6. **File Output**: Writes the validated translation to the output file

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

![Translated Quest Examples](https://drive.google.com/u/0/drive-viewer/AKGpihaieSOhTITrJHjqFCsXo_Dg4Rt7aMWXp4IVwal2fhOLC0TQRV45aWuSKbfWKWKjBgq7KmiBgSmEKTbV0n1mXVVL-D4o7VTKmhQ=s1600-rw-v1)

The tool preserves color codes, formatting, and structure in most cases.

## 🐛 Troubleshooting

### "File not found" Error
- Make sure `en_us.snbt` is in the same directory as the script
- Check the filename matches exactly (case-sensitive)

### API Errors
- Verify your API key is correct
- Check your internet connection
- Ensure you haven't exceeded API rate limits

### Many Validation Errors
- This is normal! The script keeps originals for safety
- You can manually translate skipped lines later
- Consider reducing `BATCH_SIZE` to 25 for more accuracy

### Quest Book Not Loading
- Make sure the output filename matches Minecraft's language code
- Check the file is in the correct folder
- Verify the file wasn't corrupted (re-run the script)

## 🙏 Acknowledgments

- FTB Team for creating FTB Quests
- Google for the Gemini API
- The Minecraft modding community

---

Made with ❤️ for the modding community

**Star ⭐ this repo if it helped you!**
