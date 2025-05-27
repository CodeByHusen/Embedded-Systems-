# Motor

Ein einfaches Python-Skript zur Steuerung eines Motors über die GPIO-Pins eines Raspberry Pi mit der Bibliothek `gpiozero`.  
Das Programm wechselt automatisch die Drehrichtung des Motors zwischen im Uhrzeigersinn (CW) und gegen den Uhrzeigersinn (CCW), mit kurzen Stopps dazwischen.

## Voraussetzungen

- Raspberry Pi (mit GPIO-Pins)
- Python 3
- Bibliothek [`gpiozero`](https://gpiozero.readthedocs.io/)
- Ein Motor (z. B. DC-Motor) mit Motorentreiber

## GPIO-Pinbelegung

| Funktion     | GPIO-Pin |
|--------------|-----------|
| Vorwärts     | 17        |
| Rückwärts    | 27        |
| Enable (PWM) | 22        |

## Installation

1. Stelle sicher, dass Python 3 installiert ist.
2. Installiere die Bibliothek `gpiozero`:
   ```bash
   sudo apt update
   sudo apt install python3-gpiozero
