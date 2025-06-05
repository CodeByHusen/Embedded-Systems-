# Servo-Steuerung mit Python und GPIO Zero

Dieses Python-Programm steuert einen Servo-Motor über GPIO18 eines Raspberry Pi mithilfe der `gpiozero`-Bibliothek. Der Servo bewegt sich abwechselnd zwischen Minimal-, Mittel- und Maximalposition.

## Voraussetzungen

- Raspberry Pi mit Raspbian (Raspberry Pi OS)
- Ein Servo-Motor, angeschlossen an GPIO18
- Python 3
- Bibliothek: `gpiozero`
  
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Servo/pictures/Komponenten.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Servo/pictures/Servo.png)

## Installation der Abhängigkeiten

Die `gpiozero`-Bibliothek ist in der Regel vorinstalliert. Falls nicht, installiere sie mit:

```bash
sudo apt update
sudo apt install python3-gpiozero
```
## Anschlussplan
- Signal: GPIO18 (Pin 12)

- VCC: 5V (z. B. Pin 2)

- GND: Masse (z. B. Pin 6)
  
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Servo/pictures/Schematische%20Darstellung.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Servo/pictures/Schematische%20Schaltung.png)

## Verwendung
Speichere das Skript z. B. unter servo_steuerung.py.

Ausführung:
```bash
chmod +x servo_steuerung.py
sudo ./servo_steuerung.py
```
Beende das Programm mit Strg + C.

## Funktionsweise
```css
Mitte
Minimal
Mitte
Maximal
...
```

## Anpassung
- Passe myGPIO an, falls du einen anderen GPIO-Pin verwendest.

- Ändere myCorrection, falls dein Servo andere Pulsbreiten benötigt.
