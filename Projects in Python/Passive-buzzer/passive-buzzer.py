#!/usr/bin/env python3
from gpiozero import TonalBuzzer
from time import sleep

# Initialisieren Sie einen TonalBuzzer am GPIO-Pin 17
tb = TonalBuzzer(17)  # Passe die Pinnummer ggf. an

def play(tune):
    """
    Spielen Sie eine musikalische Melodie mit dem Summer.
    :param tune: Liste von Tupeln (Note, Dauer), wobei jedes Tupel eine Note und ihre Dauer darstellt.
    """
    for note, duration in tune:
        print(note)
        tb.play(note)
        sleep(float(duration))
    tb.stop()

# Traurige Melodie in a-Moll
tune = [
    ('A4', 0.5), ('C5', 0.5), ('E5', 0.5), ('C5', 0.5),
    ('A4', 0.5), (None, 0.3),
    ('G4', 0.5), ('E4', 0.5), ('D4', 0.5), (None, 0.3),
    ('C4', 0.5), ('E4', 0.5), ('A4', 0.7), (None, 0.4),
    ('B4', 0.4), ('C5', 0.6), ('D5', 0.7), (None, 0.4),
    ('E5', 0.3), ('C5', 0.3), ('A4', 0.5), (None, 0.5)
]

try:
    play(tune)

except KeyboardInterrupt:
    pass
