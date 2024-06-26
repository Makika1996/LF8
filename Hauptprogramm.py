import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Abteilungs-Tools
tools = {
    "Lager": ["print_SQL_Ausgabe", "DBinCSV"],
    "Verwaltung": ["print_SQL_Ausgabe", "DBinCSV", "DBausgabeFenster"],
    "Marketing": ["print_SQL_Ausgabe", "DBausgabeFenster", "csv_to_xml"],
    "Geschäftsführung": ["DBausgabeFenster", "Export_csv_xml_excel"]
}

# Funktion zur Ausführung von Tools mit subprocess
def run_tool(tool_name):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tool_path = os.path.join(script_dir, f"{tool_name}.py")
    
    if not os.path.exists(tool_path):
        messagebox.showerror("Fehler", f"Das Skript {tool_name}.py wurde nicht gefunden.")
        return
    
    try:
        result = subprocess.run(["python", tool_path], capture_output=True, text=True)
        if result.returncode == 0:
            messagebox.showinfo("Erfolg", result.stdout)
        else:
            messagebox.showerror("Fehler", result.stderr)
    except Exception as e:
        messagebox.showerror("Fehler", f"Fehler beim Ausführen von {tool_name}: {e}")

# Funktionen den Buttons zuordnen
tool_functions = {
    "print_SQL_Ausgabe": lambda: run_tool("print_SQL_Ausgabe"),
    "DBinCSV": lambda: run_tool("DBinCSV"),
    "DBausgabeFenster": lambda: run_tool("DBausgabeFenster"),
    "csv_to_xml": lambda: run_tool("csv_to_xml"),
    "Export_csv_xml_excel": lambda: run_tool("Export_csv_xml_excel")
}

# Login-Funktion
def login(event=None):
    abteilung = abteilung_var.get()
    password = password_entry.get()
    
    if abteilung in tools and password == abteilung:
        open_tools_window(abteilung)
    else:
        messagebox.showerror("Fehler", "Ungültiges Passwort")

# Öffnet das Fenster mit den verfügbaren Tools
def open_tools_window(abteilung):
    tools_window = tk.Toplevel(root)
    tools_window.title(f"Tools für {abteilung}")
    tools_window.geometry("250x200")  # Setzt die Größe des Fensters auf 250x200 Pixel
    tools_window.configure(bg="light blue")

    available_tools = tools[abteilung]
    for tool in available_tools:
        button = tk.Button(tools_window, text=tool, command=tool_functions[tool])
        button.pack(fill=tk.BOTH, expand=True)

# Erstelle das Dropdown-Login
def create_dropdown_login():
    # Logo laden
    logo = tk.PhotoImage(file=r"C:\Users\Juliane\Documents\Lernfeld 8\Projekt_LF8\Abgabe Projekt_LF8 Brinkmann, Marinkov, Kraft\LogoHeinerIT.png")  # Pfad zum Bild anpassen
    logo_label = tk.Label(root, image=logo, bg="light grey")
    logo_label.image = logo  # Verhindert, dass das Bild vom Garbage Collector entfernt wird
    logo_label.pack(pady=10)

    # Abteilung Label
    abteilung_label = tk.Label(root, text="\n\nAbteilung\n", font=("Calibri", 18), bg="light grey")
    abteilung_label.pack()
    
    global abteilung_var
    abteilung_var = tk.StringVar(root)
    abteilung_var.set("Lager")  # Standardwert
    
    abteilung_menu = tk.OptionMenu(root, abteilung_var, *tools.keys())
    abteilung_menu.config(bg="light blue")
    abteilung_menu.pack()

    tk.Label(root, text="\n\nPasswort\n", font=("Calibri", 16), bg="light grey").pack()
    global password_entry
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()
    password_entry.bind("<Return>", login)
    
    blank_space = tk.Frame(root, height=30)
    blank_space.pack()
    
    login_button = tk.Button(root, text="Login", command=login, bg="light blue")
    login_button.pack()

# Hauptfenster erstellen
root = tk.Tk()
root.title("Heiner IT-Systems Tools")
root.geometry("300x600")  # Setzt die Größe des Hauptfensters auf 300x600 Pixel
root.configure(bg="light grey")  # Setzt die Hintergrundfarbe auf hellgrau

create_dropdown_login()

root.mainloop()
