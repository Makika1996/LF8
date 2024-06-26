import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import mariadb
import csv

# Verbindungsparameter zur Datenbank definieren
config = {
    'user': 'root',
    #'host': '10.145.240.100',
    'host':'127.0.0.1',
    'port': 3306,
    #'password':"123",
    #'database': 'Heiner'
    'database':'heiner_it'
}

# Funktion zur Auswahl der CSV-Datei und zum Schreiben der Daten
def select_and_write_to_csv(query):
    try:
        # Verbindung zur Datenbank herstellen
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(query)

        # Alle Zeilen der Abfrage abrufen
        rows = cursor.fetchall()

        # Datei auswählen und speichern
        filename = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if filename:
            # CSV-Datei öffnen und Daten schreiben
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                csv_writer = csv.writer(file)
                
                # Spaltenüberschriften schreiben
                csv_writer.writerow([i[0] for i in cursor.description])
                
                # Daten aus der Datenbank in die CSV-Datei schreiben
                csv_writer.writerows(rows)

            messagebox.showinfo("Erfolg", f"Daten erfolgreich in {filename} geschrieben.")
        else:
            messagebox.showwarning("Warnung", "Keine Datei ausgewählt.")

    except mariadb.Error as e:
        messagebox.showerror("Fehler", f"Fehler bei der Datenbankabfrage: {e}")

    finally:
        # Verbindung schließen
        if conn:
            conn.close()

# Funktion zur Anzeige der GUI für die Abfrage und Auswahl der CSV-Datei
def show_gui_for_query_and_csv():
    # Hauptfenster erstellen
    root = tk.Tk()
    root.title("Datenbankabfrage und CSV-Export")
    root.geometry("600x400")
    root.configure(bg="light grey")

    # SQL-Abfrage Textfeld
    query_label = tk.Label(root, text="SQL-Abfrage:", font=("Helvetica", 14), bg="light grey")
    query_label.pack()

    query_entry = scrolledtext.ScrolledText(root, width=70, height=5, wrap=tk.WORD, bg="light blue")
    query_entry.pack(pady=10)

    # Funktion zum Ausführen der SQL-Abfrage und Auswahl der CSV-Datei
    def execute_query_and_export():
        query = query_entry.get("1.0", tk.END).strip()
        if not query:
            messagebox.showwarning("Warnung", "Bitte geben Sie eine SQL-Abfrage ein.")
            return
        
        select_and_write_to_csv(query)

    # Binde die Enter-Taste an die Funktion execute_query_and_export
    query_entry.bind("<Return>", lambda event: execute_query_and_export())

    # Ausführen-Button
    execute_button = tk.Button(root, text="Abfrage ausführen und in CSV exportieren", command=execute_query_and_export, bg="light blue")
    execute_button.pack(pady=5)

    root.mainloop()

# Funktion aufrufen, um die GUI anzuzeigen und die Funktionen bereitzustellen
show_gui_for_query_and_csv()
