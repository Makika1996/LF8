import tkinter as tk
from tkinter import ttk
import mysql.connector

# Verbindung zur Datenbank herstellen
db_connection = mysql.connector.connect(
    #host="10.145.240.100",
    host="127.0.0.1",
    user="root",
    #password="123",
    #database="Heiner"
    database="heiner_it"
)

# SQL-Abfrage, um Daten abzurufen (Beispiel: Mitarbeiterdaten)
query = "SELECT PersonalNr, Nachname, Vorname FROM personal;"

# Funktion zum Abrufen und Anzeigen der Daten
def show_data():
    try:
        cursor = db_connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()

        # Vorhandene Daten in der Tabelle löschen
        for item in table_tree.get_children():
            table_tree.delete(item)

        # Daten in Tkinter-Tabelle anzeigen
        for row in rows:
            table_tree.insert("", tk.END, values=row)

        cursor.close()

    except mysql.connector.Error as e:
        print(f"Fehler bei der Datenbankabfrage: {e}")

# Tkinter GUI erstellen
root = tk.Tk()
root.title("Datenbankdaten anzeigen")

# Frame für die Tabelle erstellen
frame = ttk.Frame(root)
frame.pack(pady=20)

# Treeview (Tkinter Tabelle) erstellen
table_tree = ttk.Treeview(frame, columns=("PersonalNr", "Nachname", "Vorname"), show="headings")
table_tree.heading("PersonalNr", text="PersonalNr")
table_tree.heading("Nachname", text="Nachname")
table_tree.heading("Vorname", text="Vorname")
table_tree.pack()

# Button zum Abrufen und Anzeigen der Daten erstellen
show_data_button = ttk.Button(root, text="Daten anzeigen", command=show_data)
show_data_button.pack(pady=10)

# Hauptloop starten
root.mainloop()

# Verbindung zur Datenbank schließen
db_connection.close()
