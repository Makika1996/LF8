import tkinter as tk
from tkinter import messagebox, scrolledtext
import mariadb

# Definition der Verbindung zur Datenbank
def connect_to_db():
    try:
        db = mariadb.connect(
            #host="10.145.240.100",
            host="127.0.0.1",
            port=3306,
            user="root",
            #password="123",
            #database="Heiner"
            database="heiner_it"
        )
        return db
    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler bei der Verbindung zur Datenbank: {e}")
        return None

# Funktion zur Ausführung von SQL-Abfragen
def execute_query(event=None):
    db = connect_to_db()
    if db is None:
        return
    
    query = query_entry.get("1.0", tk.END).strip()
    
    if not query:
        messagebox.showwarning("Warnung", "Bitte geben Sie eine SQL-Abfrage ein.")
        return
    
    try:
        cur = db.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        
        # Ergebnisse in neuem Fenster anzeigen
        show_results_window(rows)
        
        cur.close()
    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler bei der Ausführung der Abfrage: {e}")
    finally:
        db.close()

# Funktion zur Anzeige der Ergebnisse in einem neuen Fenster
def show_results_window(rows):
    results_window = tk.Toplevel(root)
    results_window.title("Abfrageergebnisse")
    results_window.geometry("500x400")  # Kleinere Breite für das Ergebnisfenster
    results_window.configure(bg="light grey")
    
    result_text = scrolledtext.ScrolledText(results_window, width=60, height=20, wrap=tk.WORD, bg="light blue")
    result_text.pack(pady=10)
    
    for row in rows:
        result_text.insert(tk.END, f"{row}\n")

# Hauptfenster erstellen
root = tk.Tk()
root.title("Heiner IT-Systems SQL-Abfrage")
root.geometry("500x400")
root.configure(bg="light grey")

# Logo hinzufügen (Pfad zum Bild anpassen)
logo = tk.PhotoImage(file=r"c:\Users\Juliane\Documents\Lernfeld 8\Projekt_LF8\Abgabe Projekt_LF8 Brinkmann, Marinkov, Kraft\LogoHeinerIT.png")
logo_label = tk.Label(root, image=logo, bg="light grey")
logo_label.image = logo
logo_label.pack(pady=10)

# SQL-Abfrage Textfeld
query_label = tk.Label(root, text="SQL-Abfrage:", font=("Calibri", 14), bg="light grey")
query_label.pack()

query_entry = scrolledtext.ScrolledText(root, width=50, height=4, wrap=tk.WORD, bg="light blue")
query_entry.pack(pady=10)

# Binde die Enter-Taste an die Funktion execute_query
query_entry.bind("<Return>", execute_query)

# Ausführen-Button
execute_button = tk.Button(root, text="Abfrage ausführen", command=execute_query, bg="light blue")
execute_button.pack(pady=5)

root.mainloop()
