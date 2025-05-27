from gpiozero import Motor
from time import sleep

# Initialisieren Sie den Motor mit GPIO Zero, indem Sie GPIO-Pins für Vorwärts (17), Rückwärts (27) und Enable (22) Kontrolle angeben
motor = Motor(forward=17, backward=27, enable=22)

try:
    # Hauptfunktion zur Steuerung der Richtung und Bewegung des Motors.
    # Wechselt die Drehrichtung des Motors zwischen im Uhrzeigersinn und gegen den Uhrzeigersinn mit Stopps dazwischen.
    actions = {'CW': motor.forward, 'CCW': motor.backward, 'STOP': motor.stop}  # Motoraktionen für Lesbarkeit definieren

    while True:
        # Durch die definierten Aktionen zyklen, um die Motordrehrichtung zu steuern
        for action in ['CW', 'STOP', 'CCW', 'STOP']:
            actions[action]()  # Führen Sie die aktuelle Aktion aus (vorwärts, stoppen, rückwärts, stoppen)
            print(f"{action}")  # Zeigen Sie die aktuelle Aktion in der Konsole an
            sleep(5)  # Pause für 5 Sekunden, bevor Sie zur nächsten Aktion übergehen

except KeyboardInterrupt:
    # Tastaturunterbrechung (z. B. Ctrl+C) sauber behandeln
    pass