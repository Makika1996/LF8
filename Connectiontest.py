# Importieren der mariadb-Bibliothek
import mariadb

# Definition der Verbindung zur Datenbank
db = mariadb.connect(
  host="127.0.0.1",
  port=3306,
  user="root",
  #password="123",
  #database="Heiner")
  database="heiner_it")

# Die Methode testet, ob erfolgreich eine Verbindung zur Datenbank hergestellt werden kann.
# Ausgabe "Erfolgreich verbunden!" oder Fehlermeldung als print-Ausgabe zurück
def testConnection(dbc):      #dbc steht für die Datenbankverbindung (database connection), die überprüft werden soll
  # Definition des Tests und der Ausgabe
  cur = dbc.cursor()
  cur.execute("SELECT * FROM artikel;")
  print("Erfolgreich verbunden!")
  cur.close()


# Aufruf der Methode zum Testen der Datenbankverbindung
testConnection(db)  
