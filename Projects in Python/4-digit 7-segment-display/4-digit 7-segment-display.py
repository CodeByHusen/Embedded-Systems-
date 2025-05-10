#!/usr/bin/env python3
from gpiozero import OutputDevice
import time
import threading

# GPIO-Pins für das 74HC595 Schieberegister definieren
SDI = OutputDevice(24)   # Serieller Dateneingang
RCLK = OutputDevice(23)  # Register Clock
SRCLK = OutputDevice(18) # Schieberegistertakt

# GPIO-Pins für die Ziffernauswahl auf der 7-Segment-Anzeige definieren
placePin = [OutputDevice(pin) for pin in (10, 22, 27, 17)]

# Segmentcodes für die Zahlen 0-9 auf der 7-Segment-Anzeige definieren
number = (0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8, 0x80, 0x90)

counter = 0  # Zähler für die Anzeige initialisieren
timer1 = 0   # Timer für Zählererhöhung initialisieren

def clearDisplay():
    """ Die 7-Segment-Anzeige löschen. """
    for _ in range(8):
        SDI.on()
        SRCLK.on()
        SRCLK.off()
    RCLK.on()
    RCLK.off()

def hc595_shift(data):
    """ Ein Byte Daten in das 74HC595 Schieberegister schieben. """
    for i in range(8):
        SDI.value = 0x80 & (data << i)  # SDI auf Hoch/Niedrig basierend auf dem Datenbit setzen
        SRCLK.on()  # Schieberegistertakt auslösen
        SRCLK.off()
    RCLK.on()  # Daten durch Auslösen des Register Clocks in die Ausgabe übernehmen
    RCLK.off()

def pickDigit(digit):
    """ Eine Ziffer für die Anzeige auf der 7-Segment-Anzeige auswählen. """
    for pin in placePin:
        pin.off()  # Alle Ziffernauswahl-Pins ausschalten
    placePin[digit].on()  # Die ausgewählte Ziffer einschalten

def timer():
    """ Timerfunktion, um den Zähler jede Sekunde zu erhöhen. """
    global counter, timer1
    timer1 = threading.Timer(1.0, timer)  # Timer für nächste Erhöhung zurücksetzen
    timer1.start()
    counter += 1  # Zähler erhöhen
    print("%d" % counter)  # Aktuellen Zählerstand ausgeben

def setup():
    """ Anfangszustand einrichten und den Timer starten. """
    global timer1
    timer1 = threading.Timer(1.0, timer)  # Timer initialisieren und starten
    timer1.start()

def loop():
    """ Hauptloop, um die 7-Segment-Anzeige mit dem Zählerwert zu aktualisieren. """
    global counter
    while True:
        for i in range(4):  # Jede Ziffer durchlaufen
            clearDisplay()  # Anzeige löschen, bevor neue Ziffer gesetzt wird
            pickDigit(i)    # Ziffer für die Anzeige auswählen
            digit = (counter // (10 ** i)) % 10
            hc595_shift(number[digit])  # Ziffernwert in 74HC595 schieben
            time.sleep(0.001)  # Kurze Verzögerung für Anzeigestabilität

def destroy():
    """ GPIO-Ressourcen freigeben und Timer bei Beendigung stoppen. """
    global timer1
    timer1.cancel()  # Timer stoppen
    for device in [SDI, RCLK, SRCLK] + placePin:
        device.close()  # GPIO-Geräte schließen

try:
    setup()  # Initialisierung einrichten
    while True:
        loop()  # Hauptloop starten

except KeyboardInterrupt:
    # Skriptunterbrechung (z. B. Ctrl+C) behandeln
    destroy()  # Ressourcen bei Beendigung aufräumen