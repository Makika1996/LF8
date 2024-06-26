import mariadb

# Import der cvs-Bibliothek
import csv

# Verbindungsparameter zur Datenbank definieren
config = {
    'user': 'root',
    #'password': '123',
    #'host': '10.145.240.100',
    'host':'127.0.0.1',
    'port':3306,
    #'database': 'Heiner'
    'database':'heiner_it'
}

# SQL-Abfrage, um den gesamten Lagerbestand aus der Tabelle "artikel" abzurufen
query = "SELECT * FROM artikel"

# Dateiname für die CSV-Datei, in die die Daten geschrieben werden sollen
csv_file = "artikel.csv"

# Funktion zum Ausführen der SQL-Abfrage und Schreiben in die CSV-Datei
def write_to_csv(query, csv_file):
    try:
        # Verbindung zur Datenbank herstellen
        conn = mariadb.connect(**config)
        cursor = conn.cursor()

        # SQL-Abfrage ausführen
        cursor.execute(query)

        # Alle Zeilen der Abfrage abrufen
        rows = cursor.fetchall()

        # CSV-Datei öffnen und Daten schreiben
        with open(csv_file, 'w', newline='', encoding='utf-8') as file:
            csv_writer = csv.writer(file)
            
            # Spaltenüberschriften schreiben
            csv_writer.writerow([i[0] for i in cursor.description])
            
            # Daten aus der Datenbank in die CSV-Datei schreiben
            csv_writer.writerows(rows)

        print(f"Daten erfolgreich in {csv_file} geschrieben.")

    except mariadb.Error as e:
        print(f"Fehler bei der Datenbankabfrage: {e}")

    finally:
        # Verbindung schließen
        if conn:
            conn.close()

# Funktion aufrufen, um den Lagerbestand aus der Tabelle Artikel in die CSV-Datei zu schreiben
write_to_csv(query, csv_file)
