from gpiozero import OutputDevice  # Importieren Sie die Klasse zur Steuerung der GPIO-Pins
from time import sleep  # Importieren Sie die Schlaffunktion für Verzögerungen

# Initialisieren Sie das Relais, das mit dem GPIO-Pin 17 verbunden ist
relais = OutputDevice(17)

try:
    # Schleife zum kontinuierlichen Umschalten des Zustands des Relais alle Sekunde
    while True:
        print('Relais öffnet...')  # Informieren Sie, dass das Relais aktiviert wird
        relais.on()  # Schalten Sie das Relais ein (unter der Annahme einer aktiven Niedrigkonfiguration)
        sleep(1)   # Halten Sie das Relais für 1 Sekunde im eingeschalteten Zustand

        print('...Relais schließt')  # Informieren Sie, dass das Relais deaktiviert wird
        relais.off()  # Schalten Sie das Relais aus
        sleep(1)   # Halten Sie das Relais für 1 Sekunde im ausgeschalteten Zustand

except KeyboardInterrupt:
    # Behandeln Sie eine Tastaturunterbrechung (wie Ctrl+C), um aus der Schleife auszusteigen
    relais.off()  # Stellen Sie sicher, dass das Relais ausgeschaltet ist, bevor Sie den Vorgang beenden
    pass