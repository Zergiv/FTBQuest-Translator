import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import google.generativeai as genai
import time
import re
import os
import sys
from pathlib import Path
import threading

class SNBTTranslatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("FTB Quest Translator")
        self.root.geometry("700x650")
        self.root.resizable(False, False)
        
        # Variables
        self.api_key_var = tk.StringVar()
        self.input_file_var = tk.StringVar()
        self.output_file_var = tk.StringVar()
        self.target_lang_var = tk.StringVar(value="Spanish")
        self.batch_size_var = tk.IntVar(value=50)
        self.is_translating = False
        
        # Colores modernos
        self.bg_color = "#1e1e1e"
        self.fg_color = "#e0e0e0"
        self.accent_color = "#0078d4"
        self.entry_bg = "#2d2d2d"
        self.button_bg = "#0078d4"
        
        self.setup_ui()
        self.load_config()
        self.auto_detect_files()
        
    def setup_ui(self):
        """Crea la interfaz gráfica"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configurar colores
        style.configure('TLabel', background=self.bg_color, foreground=self.fg_color)
        style.configure('TButton', background=self.button_bg, foreground='white')
        style.configure('TEntry', fieldbackground=self.entry_bg, foreground=self.fg_color)
        
        self.root.configure(bg=self.bg_color)
        
        # Header
        header_frame = tk.Frame(self.root, bg=self.accent_color, height=60)
        header_frame.pack(fill=tk.X, pady=(0, 15))
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(
            header_frame, 
            text="🌍 FTB Quest Translator", 
            font=("Segoe UI", 18, "bold"),
            bg=self.accent_color,
            fg="white"
        )
        title_label.pack(pady=15)
        
        # Main container
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(padx=20, fill=tk.BOTH, expand=True)
        
        # API Key Section
        self.create_section(main_frame, "🔑 API Key de Gemini", 0)
        api_frame = tk.Frame(main_frame, bg=self.bg_color)
        api_frame.grid(row=1, column=0, sticky="ew", pady=(0, 15))
        
        api_entry = tk.Entry(
            api_frame, 
            textvariable=self.api_key_var,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
            font=("Segoe UI", 10)
        )
        api_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 5))
        
        save_api_btn = tk.Button(
            api_frame,
            text="💾",
            command=self.save_config,
            bg=self.button_bg,
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10),
            cursor="hand2",
            width=3
        )
        save_api_btn.pack(side=tk.RIGHT, ipady=5)
        
        # Input File Section
        self.create_section(main_frame, "📂 Archivo de Entrada (en_us.snbt)", 2)
        input_frame = tk.Frame(main_frame, bg=self.bg_color)
        input_frame.grid(row=3, column=0, sticky="ew", pady=(0, 15))
        
        input_entry = tk.Entry(
            input_frame,
            textvariable=self.input_file_var,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
            font=("Segoe UI", 9)
        )
        input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 5))
        
        browse_input_btn = tk.Button(
            input_frame,
            text="📁 Buscar",
            command=self.browse_input_file,
            bg=self.button_bg,
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 9),
            cursor="hand2"
        )
        browse_input_btn.pack(side=tk.RIGHT, ipady=5, padx=2)
        
        auto_btn = tk.Button(
            input_frame,
            text="🔍",
            command=self.auto_detect_files,
            bg=self.button_bg,
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 9),
            cursor="hand2",
            width=3
        )
        auto_btn.pack(side=tk.RIGHT, ipady=5)
        
        # Output File Section
        self.create_section(main_frame, "💾 Archivo de Salida", 4)
        output_frame = tk.Frame(main_frame, bg=self.bg_color)
        output_frame.grid(row=5, column=0, sticky="ew", pady=(0, 15))
        
        output_entry = tk.Entry(
            output_frame,
            textvariable=self.output_file_var,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
            font=("Segoe UI", 9)
        )
        output_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8, padx=(0, 5))
        
        browse_output_btn = tk.Button(
            output_frame,
            text="📁 Buscar",
            command=self.browse_output_file,
            bg=self.button_bg,
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 9),
            cursor="hand2"
        )
        browse_output_btn.pack(side=tk.RIGHT, ipady=5)
        
        # Language and Batch Size
        options_frame = tk.Frame(main_frame, bg=self.bg_color)
        options_frame.grid(row=6, column=0, sticky="ew", pady=(0, 15))
        
        # Language
        lang_frame = tk.Frame(options_frame, bg=self.bg_color)
        lang_frame.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
        self.create_section(lang_frame, "🌐 Idioma Destino", 0)
        lang_combo = ttk.Combobox(
            lang_frame,
            textvariable=self.target_lang_var,
            values=["Spanish", "French", "German", "Portuguese", "Italian", "Japanese", "Chinese", "Korean"],
            state="readonly",
            font=("Segoe UI", 9)
        )
        lang_combo.grid(row=1, column=0, sticky="ew", ipady=5)
        
        # Batch Size
        batch_frame = tk.Frame(options_frame, bg=self.bg_color)
        batch_frame.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        
        self.create_section(batch_frame, "📦 Tamaño Lote", 0)
        batch_spin = tk.Spinbox(
            batch_frame,
            from_=10,
            to=100,
            textvariable=self.batch_size_var,
            bg=self.entry_bg,
            fg=self.fg_color,
            insertbackground=self.fg_color,
            relief=tk.FLAT,
            font=("Segoe UI", 9),
            buttonbackground=self.button_bg
        )
        batch_spin.grid(row=1, column=0, sticky="ew", ipady=5)
        
        # Progress Section
        self.create_section(main_frame, "📊 Progreso", 7)
        self.log_text = scrolledtext.ScrolledText(
            main_frame,
            height=8,
            bg=self.entry_bg,
            fg=self.fg_color,
            relief=tk.FLAT,
            font=("Consolas", 9),
            wrap=tk.WORD
        )
        self.log_text.grid(row=8, column=0, sticky="ew", pady=(0, 15))
        
        # Translate Button
        self.translate_btn = tk.Button(
            main_frame,
            text="🚀 Iniciar Traducción",
            command=self.start_translation,
            bg="#28a745",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 12, "bold"),
            cursor="hand2",
            height=2
        )
        self.translate_btn.grid(row=9, column=0, sticky="ew")
        
        main_frame.columnconfigure(0, weight=1)
        
    def create_section(self, parent, text, row):
        """Crea una etiqueta de sección"""
        label = tk.Label(
            parent,
            text=text,
            font=("Segoe UI", 10, "bold"),
            bg=self.bg_color,
            fg=self.fg_color,
            anchor="w"
        )
        label.grid(row=row, column=0, sticky="w", pady=(0, 5))
        
    def log(self, message):
        """Agrega mensaje al log"""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()
        
    def load_config(self):
        """Carga configuración guardada"""
        config_file = Path("config.txt")
        if config_file.exists():
            try:
                with open(config_file, 'r') as f:
                    self.api_key_var.set(f.read().strip())
            except:
                pass
                
    def save_config(self):
        """Guarda la API key"""
        api_key = self.api_key_var.get().strip()
        if api_key:
            try:
                with open("config.txt", 'w') as f:
                    f.write(api_key)
                self.log("✅ API Key guardada correctamente")
            except Exception as e:
                self.log(f"❌ Error al guardar: {e}")
        else:
            messagebox.showwarning("Advertencia", "Ingrese una API Key primero")
            
    def auto_detect_files(self):
        """Detecta automáticamente archivos .snbt"""
        # Buscar en la carpeta actual
        found_files = list(Path(".").glob("*.snbt"))
        
        # Buscar en subdirectorios comunes
        common_paths = [
            Path("config/ftbquests/quests/lang"),
            Path("../config/ftbquests/quests/lang"),
            Path("../../config/ftbquests/quests/lang")
        ]
        
        for path in common_paths:
            if path.exists():
                found_files.extend(path.glob("*.snbt"))
                
        # Buscar en_us.snbt
        en_us_file = next((f for f in found_files if f.name == "en_us.snbt"), None)
        
        if en_us_file:
            self.input_file_var.set(str(en_us_file.absolute()))
            output_path = en_us_file.parent / "es_es.snbt"
            self.output_file_var.set(str(output_path.absolute()))
            self.log(f"✅ Archivos detectados automáticamente en: {en_us_file.parent}")
        else:
            self.log("ℹ️ No se encontraron archivos .snbt automáticamente")
            
    def browse_input_file(self):
        """Abre diálogo para seleccionar archivo de entrada"""
        filename = filedialog.askopenfilename(
            title="Seleccionar archivo de entrada",
            filetypes=[("SNBT files", "*.snbt"), ("All files", "*.*")]
        )
        if filename:
            self.input_file_var.set(filename)
            
            # Sugerir archivo de salida
            input_path = Path(filename)
            output_path = input_path.parent / "es_es.snbt"
            self.output_file_var.set(str(output_path))
            
    def browse_output_file(self):
        """Abre diálogo para seleccionar archivo de salida"""
        filename = filedialog.asksaveasfilename(
            title="Guardar traducción como",
            defaultextension=".snbt",
            filetypes=[("SNBT files", "*.snbt"), ("All files", "*.*")]
        )
        if filename:
            self.output_file_var.set(filename)
            
    def validate_inputs(self):
        """Valida que todos los campos estén completos"""
        if not self.api_key_var.get().strip():
            messagebox.showerror("Error", "Por favor ingrese su API Key de Gemini")
            return False
            
        if not self.input_file_var.get().strip():
            messagebox.showerror("Error", "Por favor seleccione un archivo de entrada")
            return False
            
        if not os.path.exists(self.input_file_var.get()):
            messagebox.showerror("Error", f"El archivo de entrada no existe:\n{self.input_file_var.get()}")
            return False
            
        if not self.output_file_var.get().strip():
            messagebox.showerror("Error", "Por favor especifique un archivo de salida")
            return False
            
        return True
        
    def start_translation(self):
        """Inicia el proceso de traducción"""
        if not self.validate_inputs():
            return
            
        if self.is_translating:
            messagebox.showwarning("Advertencia", "Ya hay una traducción en progreso")
            return
            
        # Ejecutar en thread separado
        thread = threading.Thread(target=self.translate_file, daemon=True)
        thread.start()
        
    def translate_file(self):
        """Proceso de traducción (core)"""
        self.is_translating = True
        self.translate_btn.config(state=tk.DISABLED, text="⏳ Traduciendo...")
        self.log_text.delete(1.0, tk.END)
        
        try:
            # Configurar API
            genai.configure(api_key=self.api_key_var.get().strip())
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            input_file = self.input_file_var.get()
            output_file = self.output_file_var.get()
            target_lang = self.target_lang_var.get()
            batch_size = self.batch_size_var.get()
            
            self.log("=" * 60)
            self.log("📝 Iniciando traducción...")
            self.log("=" * 60)
            self.log(f"📂 Entrada: {Path(input_file).name}")
            self.log(f"💾 Salida: {Path(output_file).name}")
            self.log(f"🌐 Idioma: {target_lang}")
            self.log(f"📦 Tamaño lote: {batch_size}")
            self.log("")
            
            # Leer archivo
            with open(input_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            total_lines = len(lines)
            self.log(f"📄 Total de líneas: {total_lines}")
            self.log("")
            
            translated_lines = []
            
            for i in range(0, total_lines, batch_size):
                current_batch = i // batch_size + 1
                total_batches = (total_lines + batch_size - 1) // batch_size
                
                self.log(f"🔄 Procesando lote {current_batch}/{total_batches} (líneas {i+1}-{min(i+batch_size, total_lines)})")
                
                batch = [line.rstrip('\n') for line in lines[i:i+batch_size]]
                
                # Filtrar líneas traducibles
                translatable_indices = []
                lines_to_translate = []
                
                for idx, line in enumerate(batch):
                    if self.is_translatable_line(line):
                        translatable_indices.append(idx)
                        lines_to_translate.append(line)
                
                if lines_to_translate:
                    self.log(f"   📝 {len(lines_to_translate)} líneas para traducir")
                    
                    # Traducir
                    translated = self.translate_batch(model, lines_to_translate, target_lang)
                    
                    # Validar y reemplazar
                    validation_errors = 0
                    for local_idx, global_idx in enumerate(translatable_indices):
                        if local_idx < len(translated):
                            original = batch[global_idx]
                            translated_line = translated[local_idx]
                            
                            valid, message = self.validate_translation(original, translated_line)
                            
                            if valid:
                                batch[global_idx] = translated_line
                            else:
                                self.log(f"   ⚠️ Línea {i+global_idx+1}: {message}")
                                validation_errors += 1
                    
                    if validation_errors > 0:
                        self.log(f"   ⚠️ {validation_errors} líneas con errores (se mantienen originales)")
                    else:
                        self.log(f"   ✅ Todas las líneas traducidas correctamente")
                else:
                    self.log(f"   ℹ️ No hay líneas traducibles en este lote")
                
                translated_lines.extend(batch)
                
                if i + batch_size < total_lines:
                    time.sleep(2)
            
            # Guardar archivo
            self.log("")
            self.log(f"💾 Guardando traducción...")
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in translated_lines:
                    f.write(line + '\n')
            
            self.log("")
            self.log("=" * 60)
            self.log("✅ ¡Traducción completada exitosamente!")
            self.log("=" * 60)
            
            messagebox.showinfo("Éxito", f"Traducción completada!\n\nArchivo guardado en:\n{output_file}")
            
        except Exception as e:
            self.log("")
            self.log(f"❌ ERROR: {str(e)}")
            messagebox.showerror("Error", f"Error durante la traducción:\n\n{str(e)}")
            
        finally:
            self.is_translating = False
            self.translate_btn.config(state=tk.NORMAL, text="🚀 Iniciar Traducción")
    
    def is_translatable_line(self, line):
        """Determina si una línea necesita traducción"""
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
    
    def validate_translation(self, original, translated):
        """Valida que la traducción mantenga la estructura"""
        for char in ['{', '}', '[', ']', ':', ',']:
            if original.count(char) != translated.count(char):
                return False, f"Cantidad diferente de '{char}'"
        
        if original.count('"') != translated.count('"'):
            return False, "Cantidad diferente de comillas"
        
        if ':' in original and ':' in translated:
            key_orig = original.split(':', 1)[0].strip()
            key_trad = translated.split(':', 1)[0].strip()
            if key_orig != key_trad:
                return False, f"Clave modificada: {key_orig} != {key_trad}"
        
        codes_orig = re.findall(r'&[0-9a-frlonmk]', original.lower())
        codes_trad = re.findall(r'&[0-9a-frlonmk]', translated.lower())
        if codes_orig != codes_trad:
            return False, "Códigos de color alterados"
        
        return True, "OK"
    
    def translate_batch(self, model, lines, target_language):
        """Traduce un lote de líneas usando Gemini"""
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

TEXT TO TRANSLATE TO {target_language}:
{batch_text}

IMPORTANT: Return ONLY translated lines with format LINE_X|||content"""

        try:
            response = model.generate_content(prompt)
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
            self.log(f"   ❌ Error en traducción: {e}")
            return lines

def main():
    root = tk.Tk()
    app = SNBTTranslatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
