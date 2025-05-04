# RGB LED Color Cycle with GPIO Zero

Dieses Projekt steuert eine RGB-LED über den Raspberry Pi und lässt sie automatisch durch verschiedene Farben wechseln.

## 🛠 Voraussetzungen

- Raspberry Pi mit installiertem Raspbian/Linux
- Python 3
- [gpiozero](https://gpiozero.readthedocs.io/en/stable/) Bibliothek (in Raspbian vorinstalliert)
- Verkabelte RGB-LED:
  - Rot: GPIO 17
  - Grün: GPIO 18
  - Blau: GPIO 27
- 3 passende Vorwiderstände (z. B. 220 Ω) für die LED-Anschlüsse

## 📄 Beschreibung

Das Python-Skript durchläuft eine Liste vordefinierter RGB-Farben und zeigt jede Farbe für eine Sekunde auf der LED an. Die Farben werden über PWM gesteuert, sodass fließende Übergänge möglich wären (derzeit nicht genutzt).

## 🚀 Verwendung

1. Stelle sicher, dass deine RGB-LED korrekt mit den GPIO-Pins verbunden ist.
2. Führe das Skript aus:

   ```bash
   python3 rgb_led.py
![Diagram](Projects in Python/RGB-LED/pictures/Required Components.png)



