# Raspberry Pi Buzzer Blinker mit gpiozero

Dieses Projekt verwendet die Python-Bibliothek `gpiozero`, um einen aktiven Buzzer (Summer) am Raspberry Pi ein- und auszuschalten. Der Buzzer wird alle 0,1 Sekunden abwechselnd aktiviert und deaktiviert und gibt so ein schnelles Piepsen von sich.

## Hardware-Anforderungen

- Raspberry Pi (alle Modelle mit GPIO-Unterstützung)
- Aktiver Buzzer (aktiv-low)
- Verbindungskabel
- Steckbrett (optional)

### Schaltung

Der aktive Buzzer wird wie folgt angeschlossen:

- **+ (Plus)** → **GPIO 17** (BCM)
- **- (Minus)** → **GND**

**Hinweis:** Dieser Buzzer ist *aktiv-low*, d.h. er piept, wenn der GPIO auf LOW geschaltet wird.

## Software-Anforderungen

- Python 3
- gpiozero-Bibliothek

### Installation (falls nötig)

```bash
sudo apt update
sudo apt install python3-gpiozero
