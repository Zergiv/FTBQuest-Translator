# FTBQuest Translator

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Gemini API](https://img.shields.io/badge/API-Gemini%203%20Flash-orange.svg)](https://ai.google.dev/)
[![Latest Release](https://img.shields.io/github/v/release/Zergiv/FTBQuest-Translator)](https://github.com/Zergiv/FTBQuest-Translator/releases)

AI-powered translator for FTB Quests `.snbt` language files. Translates quest content while preserving file structure, color codes, and Minecraft formatting.

Built for **FTB Quests 1.21+** where `.snbt` lang files are located in `config/ftbquests/quests/lang/`.

## Features

- **Smart Folder Search** — Scans your system to find `ftbquests/lang` folders automatically
- **AI Translation** — Google Gemini 3 Flash with structure-aware prompting
- **Validation** — Every line is checked for structural integrity before saving
- **Color Code Preservation** — `&a`, `&6`, `&r`, etc. stay exactly in place
- **Batch Processing** — Handles large files efficiently (50 lines/batch)
- **GUI & CLI** — Modern dark-themed GUI or command-line script

## Quick Start

### Download (Recommended)

1. Grab the latest [release](https://github.com/Zergiv/FTBQuest-Translator/releases) for your OS
2. Run the executable — no installation needed
3. Enter your [Gemini API key](https://aistudio.google.com/apikey) (free tier available)
4. Click **🔍 Auto** to find your quest folders, or browse manually
5. Translate

### From Source

```bash
git clone https://github.com/Zergiv/FTBQuest-Translator.git
cd FTBQuest-Translator
pip install -r requirements.txt
python translator_gui.py
```

## Folder Search

Click **🔍 Auto** in the GUI to scan your system for FTB Quest folders. It searches common locations (CurseForge, PrismLauncher, MultiMC, ATLauncher, etc.) and presents all found `ftbquests/quests/lang/` directories with their `.snbt` files. Select the one you want and the paths are configured automatically.

## How It Works

1. Reads the `.snbt` file and identifies translatable lines
2. Sends batches to Gemini with strict formatting rules
3. Validates each translated line (quotes, brackets, keys, color codes)
4. Keeps the original line if validation fails — file integrity first
5. Writes the output file

**Expected coverage**: ~80-90% auto-translated. Remaining lines are kept as-is for manual review.

## CLI Usage

Edit the config at the top of `snbt_translator.py`:

```python
GEMINI_API_KEY = "your-key"
INPUT_FILE = "en_us.snbt"
OUTPUT_FILE = "es_es.snbt"
TARGET_LANGUAGE = "Spanish"
```

```bash
python snbt_translator.py
```

## Build

```bash
# Windows
build.bat

# Linux / macOS
chmod +x build.sh && ./build.sh
```

Output goes to `dist/`.

## Supported Languages

| Language | Output File |
|----------|-------------|
| Spanish | `es_es.snbt` |
| French | `fr_fr.snbt` |
| German | `de_de.snbt` |
| Portuguese | `pt_br.snbt` |
| Italian | `it_it.snbt` |
| Japanese | `ja_jp.snbt` |
| Chinese | `zh_cn.snbt` |
| Korean | `ko_kr.snbt` |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| File not found | Use **🔍 Auto** or browse manually |
| API errors | Check key, internet, rate limits |
| Validation errors | Normal — originals kept for safety, reduce batch size for accuracy |
| Quest book broken | Verify output is in `config/ftbquests/quests/lang/` with correct filename |

## Contributing

PRs, bug reports, and feature requests welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

Open source — see [LICENSE](LICENSE).
