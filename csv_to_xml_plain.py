import csv
import xml.etree.ElementTree as ET

def csv_to_xml(csv_file_path, xml_file_path):
    # Erstelle das Wurzelelement des XML-Dokuments
    root = ET.Element("data")

    # Öffne die CSV-Datei und lese die Inhalte
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        
        # Durchlaufe jede Zeile in der CSV-Datei
        for row in csv_reader:
            # Erstelle ein Element für jede Zeile
            item = ET.Element("item")
            root.append(item)
            
            # Füge die Spalten als Unterelemente hinzu
            for key, value in row.items():
                child = ET.SubElement(item, key)
                child.text = value
    
    # Erstelle einen Baum aus dem Wurzelelement
    tree = ET.ElementTree(root)
    
    # Speichere das XML-Dokument in der angegebenen Datei
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)

# Beispielaufruf der Funktion
csv_file_path = 'Projekt_LF8/artikel.csv'
xml_file_path = 'Projekt_LF8/artikel.xml'
csv_to_xml(csv_file_path, xml_file_path)
