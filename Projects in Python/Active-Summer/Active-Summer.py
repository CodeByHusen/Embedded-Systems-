from gpiozero import Buzzer
from time import sleep

# Initialisieren Sie ein Buzzer-Objekt am GPIO-Pin 17
buzzer = Buzzer(17)

try:
    while True:
        # Summer einschalten
        print('Summer Aus')
        buzzer.on()
        sleep(0.1)  # Summer für 0,1 Sekunden eingeschaltet lassen

        # Summer ausschalten
        print('Summer An')
        buzzer.off()
        sleep(0.1)  # Summer für 0,1 Sekunden ausgeschaltet lassen

except KeyboardInterrupt:
    # Tastaturunterbrechung (Ctrl+C) sauber behandeln
    pass