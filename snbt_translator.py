from google import genai
import time
import re
import os

GEMINI_API_KEY = "YOUR_API_KEY_HERE"  # Replace with your API key
client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = 'gemini-3-flash-preview'

# Configuration
BATCH_SIZE = 50  # Lines per batch
INPUT_FILE = "en_us.snbt"  # Input file name
OUTPUT_FILE = "es_es.snbt"  # Output file name
TARGET_LANGUAGE = "Spanish"  # Change to your target language

def is_translatable_line(line):
    """Determines if a line needs translation"""
    line_stripped = line.strip()
    
    if not line_stripped:
        return False
    
    if line_stripped in ['{', '}', '[', ']', '(', ')', ',']:
        return False
    
    if line_stripped.startswith('//') or line_stripped.startswith('#'):
        return False
    
    if '"' in line or "'" in line:
        return True
    
    return False

def validate_translation(original, translated):
    """Validates that the translation maintains structure"""
    for char in ['{', '}', '[', ']', ':', ',']:
        if original.count(char) != translated.count(char):
            return False, f"Different count of '{char}'"
    
    if original.count('"') != translated.count('"'):
        return False, "Different quote count"
    
    if ':' in original and ':' in translated:
        key_orig = original.split(':', 1)[0].strip()
        key_trad = translated.split(':', 1)[0].strip()
        if key_orig != key_trad:
            return False, f"Key modified: {key_orig} != {key_trad}"
    
    codes_orig = re.findall(r'&[0-9a-frlonmk]', original.lower())
    codes_trad = re.findall(r'&[0-9a-frlonmk]', translated.lower())
    if codes_orig != codes_trad:
        return False, "Color codes altered"
    
    return True, "OK"

def translate_batch(lines, target_language):
    """Translates a batch of lines using Gemini"""
    
    batch_text = "\n".join([f"LINE_{i}|||{line}" for i, line in enumerate(lines)])
    
    prompt = f"""You are an EXPERT translator for FTB Quests .snbt files for Minecraft.

CRITICAL: This file will BREAK if you change ANYTHING except text inside quotes.

FILE FORMAT:
quest.ID.title: "text here"
quest.ID.quest_desc: ["line 1", "line 2"]
chapter.ID.title: "text"

ABSOLUTE RULES - ONE VIOLATION = BROKEN FILE:

1. **NEVER CHANGE STRUCTURE**:
   ❌ DON'T modify: quest.XXX, chapter.XXX, task.XXX, file.XXX
   ❌ DON'T change: brackets [], braces {{}}, commas, colons, quotes ""
   ❌ DON'T add or remove spaces/tabs at line start
   ❌ DON'T move content between lines
   ✅ ONLY translate text INSIDE quotes

2. **COLOR CODES - CRITICAL**:
   Codes &a, &b, &c, &d, &e, &f, &0-&9, &r, &l, &o, &n, &m, &k MUST stay EXACTLY where they are.
   
   ✅ CORRECT: "&6Ancient Remnant" → "&6Remanente Antiguo"
   ❌ WRONG: "& 6Remanente Antiguo" (added space)
   ❌ WRONG: "Remanente Antiguo &6" (moved code)
   ❌ WRONG: "Remanente &6Antiguo" (moved code)

3. **JSON/ARRAYS - DON'T TOUCH**:
   If you see {{"text": "xxx", "color": "yyy"}}, ONLY translate text INSIDE the text quotes.
   DON'T change "text", "color", "clickEvent", "hoverEvent", etc.

4. **COMMANDS - DON'T TRANSLATE**:
   - {{@pagebreak}} → leave exactly as is
   - \\\\ &\\\\ → leave exactly as is  
   - {{"keybind": "xxx"}} → leave exactly as is

5. **RESPONSE**:
   Return EXACTLY: LINE_X|||translated_content
   One input line = One output line
   If line is empty → return LINE_X|||
   DON'T add extra text, explanations, or comments

CORRECT EXAMPLES:

INPUT:
LINE_0|||	chapter.08EC6A07A9C7A8F2.title: "Exploration"
LINE_1|||	quest.007.quest_desc: ["&aFree Runner&r boots."]
LINE_2|||	quest.008.quest_desc: ["Line 1", "Line 2"]

OUTPUT:
LINE_0|||	chapter.08EC6A07A9C7A8F2.title: "Exploración"
LINE_1|||	quest.007.quest_desc: ["Botas &aFree Runner&r."]
LINE_2|||	quest.008.quest_desc: ["Línea 1", "Línea 2"]

INCORRECT EXAMPLES (DON'T DO THIS):

❌ quest.007.desc: ["Botas &aFree Runner&r."]  (changed .quest_desc)
❌ ["Botas Free & a Runner & r."]  (separated codes)
❌ ["Free Runner boots."]  (removed codes)
❌ quest.007.quest_desc: ["Botas &a Free Runner &r."]  (added spaces)

TEXT TO TRANSLATE:
{batch_text}

IMPORTANT: Return ONLY translated lines with format LINE_X|||content"""

    try:
        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)
        result = response.text.strip()
        
        translated_lines = []
        for response_line in result.split('\n'):
            if '|||' in response_line and response_line.startswith('LINE_'):
                parts = response_line.split('|||', 1)
                if len(parts) > 1:
                    translated_lines.append(parts[1])
                else:
                    idx = int(parts[0].replace('LINE_', ''))
                    if idx < len(lines):
                        translated_lines.append(lines[idx])
                    else:
                        translated_lines.append('')
            else:
                if translated_lines:  
                    idx = len(translated_lines)
                    if idx < len(lines):
                        translated_lines.append(lines[idx])
        
        while len(translated_lines) < len(lines):
            idx = len(translated_lines)
            translated_lines.append(lines[idx])
        
        return translated_lines[:len(lines)]
    
    except Exception as e:
        print(f"Translation error: {e}")
        return lines  

def translate_file(input_file, output_file, target_language, batch_size):
    """Translates entire file in batches"""
    
    print(f"Reading file: {input_file}")
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    print(f"Total lines: {total_lines}")
    
    translated_lines = []
    
    for i in range(0, total_lines, batch_size):
        current_batch = i // batch_size + 1
        total_batches = (total_lines + batch_size - 1) // batch_size
        
        print(f"\nProcessing batch {current_batch}/{total_batches} (lines {i+1}-{min(i+batch_size, total_lines)})")
        
        batch = [line.rstrip('\n') for line in lines[i:i+batch_size]]
        
        translatable_indices = []
        lines_to_translate = []
        
        for idx, line in enumerate(batch):
            if is_translatable_line(line):
                translatable_indices.append(idx)
                lines_to_translate.append(line)
        
        if lines_to_translate:
            print(f"  - {len(lines_to_translate)} translatable lines found")
                        
            translated = translate_batch(lines_to_translate, target_language)
            
            validation_errors = 0
            for local_idx, global_idx in enumerate(translatable_indices):
                if local_idx < len(translated):
                    original = batch[global_idx]
                    translated_line = translated[local_idx]
                    
                    valid, message = validate_translation(original, translated_line)
                    
                    if valid:
                        batch[global_idx] = translated_line
                    else:
                        print(f"    ⚠️  Line {i+global_idx+1}: {message} - using original")
                        validation_errors += 1
            
            if validation_errors > 0:
                print(f"    ⚠️  {validation_errors} lines with errors - keeping originals")
        else:
            print(f"  - No translatable lines in this batch")
        
        translated_lines.extend(batch)
        
        if i + batch_size < total_lines:
            time.sleep(2)
    
    print(f"\nSaving translated file: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        for line in translated_lines:
            f.write(line + '\n')
    
    print(f"\n✅ Translation complete! File saved at: {output_file}")

def main():
    print("=" * 60)
    print("SNBT FILE TRANSLATOR - FTB QUESTS")
    print("=" * 60)
    
    if not os.path.exists(INPUT_FILE):
        print(f"\n❌ ERROR: File '{INPUT_FILE}' not found.")
        print("Please place the file in the same directory as this script.")
        return
    
    print(f"\nConfiguration:")
    print(f"  - Input file: {INPUT_FILE}")
    print(f"  - Output file: {OUTPUT_FILE}")
    print(f"  - Target language: {TARGET_LANGUAGE}")
    print(f"  - Batch size: {BATCH_SIZE} lines")
    
    response = input("\nDo you want to continue? (y/n): ")
    if response.lower() != 'y':
        print("Operation cancelled.")
        return
    
    translate_file(INPUT_FILE, OUTPUT_FILE, TARGET_LANGUAGE, BATCH_SIZE)

if __name__ == "__main__":
    main()