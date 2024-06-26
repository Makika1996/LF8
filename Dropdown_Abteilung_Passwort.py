import tkinter as tk
from tkinter import messagebox
import csv
import xml.etree.ElementTree as ET
import mariadb

# Abteilungs-Tools
tools = {
    "Lager": ["print_SQL_Ausgabe", "DBinCSV"],
    "Verwaltung": ["print_SQL_Ausgabe", "DBinCSV", "DBausgabeFenster"],
    "Marketing": ["print_SQL_Ausgabe", "DBausgabeFenster", "CSV_to_XML"],
    "Geschäftsführung": ["print_SQL_Ausgabe", "DBinCSV", "DBausgabeFenster", "CSV_to_XML"]
}

# Dummy-Funktionen für die Tools
def print_SQL_Ausgabe():
    print("print_SQL_Ausgabe ausgeführt")

def DBinCSV():
    print("DBinCSV ausgeführt")

def DBausgabeFenster():
    print("DBausgabeFenster ausgeführt")

def CSV_to_XML():
    print("CSV_to_XML ausgeführt")

# Funktionen den Buttons zuordnen
tool_functions = {
    "print_SQL_Ausgabe": print_SQL_Ausgabe,
    "DBinCSV": DBinCSV,
    "DBausgabeFenster": DBausgabeFenster,
    "CSV_to_XML": CSV_to_XML
}

# Login-Funktion
def login():
    abteilung = abteilung_entry.get()
    password = password_entry.get()
    
    if abteilung in tools and password == abteilung:
        open_tools_window(abteilung)
    else:
        messagebox.showerror("Fehler", "Ungültige Abteilung oder Passwort")

# Öffnet das Fenster mit den verfügbaren Tools
def open_tools_window(abteilung):
    tools_window = tk.Toplevel(root)
    tools_window.title(f"Tools für {abteilung}")

    available_tools = tools[abteilung]
    for tool in available_tools:
        button = tk.Button(tools_window, text=tool, command=tool_functions[tool])
        button.pack(fill=tk.BOTH, expand=True)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Heiner-IT Tool Login")

# Login-Formular
tk.Label(root, text="Abteilung").pack()
abteilung_entry = tk.Entry(root)
abteilung_entry.pack()

tk.Label(root, text="Passwort").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

login_button = tk.Button(root, text="Login", command=login)
login_button.pack()

root.mainloop()
