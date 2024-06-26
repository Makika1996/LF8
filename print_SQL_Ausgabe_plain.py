# Importieren der mariadb-Bibliothek
import mariadb

# Definition der Verbindung zur Datenbank (von Zuhause getestet, HEMS-Server auskommentiert)
db = mariadb.connect(
    #host="10.145.240.100",
    host="127.0.0.1",
    port=3306,
    user="root",
    #password="123",
    #database="Heiner"
    database="heiner_it"
)

# Die Methode prüft, ob erfolgreich eine Verbindung zur Datenbank hergestellt werden kann.
# Ausgabe: "Erfolgreich verbunden!" oder Fehlermeldung als print-Ausgabe zurück
def testConnection(dbc):  
    try:
        # Cursor erstellen
        cur = dbc.cursor()
        
        # Testabfrage ausführen
        cur.execute("SELECT 1")
        print("Erfolgreich verbunden!")
        
        # SQL-Abfrage, die alle Mitarbeiter ausgibt
        cur.execute("SELECT * FROM personal")
        
        # Alle Zeilen der Abfrage abrufen
        rows = cur.fetchall()
        
        # Ausgabe der Mitarbeiterdaten auf der Kommandozeile
        print("Mitarbeiterdaten:")
        for row in rows:
            print(f"PersonalNr: {row[0]}, Nachname: {row[1]}, Vorname: {row[2]}")
            
    except mariadb.Error as e:
        print(f"Fehler bei der Verbindung: {e}")
    finally:
        # Cursor schließen
        cur.close()

# Aufruf der Methode zum Testen der Datenbankverbindung
testConnection(db)

# Schließen der Verbindung
db.close()
