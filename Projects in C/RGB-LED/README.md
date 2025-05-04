# 🌈 RGB-LED Steuerung mit wiringPi (C)

Dieses Projekt steuert eine RGB-LED mithilfe von Pulse-Width Modulation (PWM) auf einem Raspberry Pi. Die LED wechselt automatisch durch mehrere Farben.

## 📦 Voraussetzungen

- Raspberry Pi (mit GPIO)
- RGB-LED (gemeinsame Kathode empfohlen)
- 3x Vorwiderstände (z. B. 220 Ω)
- Jumper-Kabel
- wiringPi installiert (Hinweis: offiziell nicht mehr gewartet, funktioniert aber weiterhin)
- C-Compiler (`gcc`)

## 🧠 Beschreibung

Das C-Programm verwendet `softPwm` von wiringPi, um die Helligkeit der roten, grünen und blauen Kanäle der RGB-LED zu steuern. Das Programm wechselt alle 500 ms durch verschiedene Farben.

## 🔌 GPIO-Verbindungen
| Farbe der LED | GPIO (BCM) | wiringPi Pin | Beschreibung         |
|---------------|------------|---------------|-----------------------|
| Rot           | GPIO 17    | 0             | PWM-Ausgang für Rot   |
| Grün          | GPIO 18    | 1             | PWM-Ausgang für Grün  |
| Blau          | GPIO 27    | 2             | PWM-Ausgang für Blau  |.

## Required Components
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/RGB-LED/pictures/Required%20Components.png)

## Build the circuit
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/RGB-LED/pictures/Build%20the%20circuit.png)


## 🔌 GPIO-Verbindungen
| Farbe der LED | GPIO (BCM) | wiringPi Pin | Beschreibung         |
|---------------|------------|---------------|-----------------------|
| Rot           | GPIO 17    | 0             | PWM-Ausgang für Rot   |
| Grün          | GPIO 18    | 1             | PWM-Ausgang für Grün  |
| Blau          | GPIO 27    | 2             | PWM-Ausgang für Blau  |

### 🖥️ Beispielausgabe
```bash
Red
Green
Blue
Yellow
Purple
Cyan
...
=======
