import tkinter as tk
from tkinter import ttk
import mariadb

# Verbindung zur Datenbank herstellen
db = mariadb.connect(
    #host="10.145.240.100",
    host="127.0.0.1",
    port=3306,
    user="root",
    #password="123",
    #database="Heiner"
    database="heiner_it"
)

# Methode zur Überprüfung der Datenbankverbindung und Abruf der Daten
def fetch_data():
    try:
        cur = db.cursor()
        cur.execute("SELECT PersonalNr, Nachname, Vorname FROM personal")
        rows = cur.fetchall()
        return rows
    except mariadb.Error as e:
        print(f"Fehler bei der Verbindung: {e}")
        return []
    finally:
        cur.close()

# Funktion zum Befüllen des Treeviews mit den Daten
def populate_treeview():
    rows = fetch_data()
    for row in rows:
        tree.insert("", tk.END, values=row)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Mitarbeiterdaten")

# Treeview-Widget erstellen
tree = ttk.Treeview(root, columns=("PersonalNr", "Nachname", "Vorname"), show="headings")
tree.heading("PersonalNr", text="PersonalNr")
tree.heading("Nachname", text="Nachname")
tree.heading("Vorname", text="Vorname")
tree.pack(fill=tk.BOTH, expand=True)

# Treeview mit Daten befüllen
populate_treeview()

# Haupt-Event-Loop starten
root.mainloop()

# Verbindung zur Datenbank schließen, wenn das Fenster geschlossen wird
db.close()
