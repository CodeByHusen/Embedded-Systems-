from gpiozero import Servo
from time import sleep

# Legen Sie die GPIO-Pin-Nummer fest, an die der Servomotor angeschlossen ist
myGPIO = 18

# Definieren Sie einen Korrekturfaktor, um die Pulsbreite des Servos feinzutunen
myCorrection = 0.45
maxPW = (2.0 + myCorrection) / 1000  # Berechnen Sie die maximale Pulsbreite
minPW = (1.0 - myCorrection) / 1000  # Berechnen Sie die minimale Pulsbreite

# Initialisieren Sie das Servo-Objekt mit benutzerdefinierten Pulsbreiten
servo = Servo(myGPIO, min_pulse_width=minPW, max_pulse_width=maxPW)

try:
    while True:
        # Positionieren Sie den Servo in der Mitte und warten Sie
        servo.mid()
        print("Mitte")  # Aktuelle Position anzeigen
        sleep(0.5)    # Kurze Pause für 0,5 Sekunden

        # Bewegen Sie den Servo in die Minimalposition und warten Sie
        servo.min()
        print("Minimal")  # Aktuelle Position anzeigen
        sleep(1)      # Position für 1 Sekunde halten

        # Bringen Sie den Servo in die Mitte zurück und warten Sie
        servo.mid()
        print("Mitte")  # Aktuelle Position anzeigen
        sleep(0.5)    # Kurze Pause für 0,5 Sekunden

        # Bewegen Sie den Servo in die Maximalposition und warten Sie
        servo.max()
        print("Maximal")  # Aktuelle Position anzeigen
        sleep(1)      # Position für 1 Sekunde halten

except KeyboardInterrupt:
    # Beenden Sie das Skript ordnungsgemäß bei einer Tastaturunterbrechung (Strg+C)
    pass