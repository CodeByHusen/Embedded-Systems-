#!/usr/bin/env python3
import LCD1602  # Modul für die Schnittstelle mit LCD1602 importieren
import time     # Modul für Timing-Funktionen importieren

def setup():
    # LCD mit I2C-Adresse 0x27 initialisieren und Hintergrundbeleuchtung aktivieren
    LCD1602.init(0x27, 1)
    # Die Nachricht 'Greetings!' in der oberen linken Ecke anzeigen (Zeile 0, Spalte 0)
    LCD1602.write(0, 0, 'Hi')
    # Die Nachricht 'From SunFounder' in der zweiten Zeile anzeigen (Zeile 1, Spalte 1)
    LCD1602.write(1, 0, 'World')
    time.sleep(2)  # Nachrichten für 2 Sekunden anzeigen

try:
    setup()  # Setup-Funktion ausführen, um das LCD zu initialisieren und Nachrichten anzuzeigen

except KeyboardInterrupt:
    # LCD-Display löschen, wenn eine Tastaturunterbrechung (z. B. Ctrl+C) auftritt
    LCD1602.clear()
    pass  # Ohne weitere Aktion fortfahren