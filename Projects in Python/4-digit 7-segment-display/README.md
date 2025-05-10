# 7-Segment-Zähler mit Raspberry Pi und 74HC595 (Python-Version)

Dieses Python-Projekt zeigt, wie ein 4-stelliges 7-Segment-Display mithilfe eines 74HC595-Schieberegisters am Raspberry Pi angesteuert werden kann. Die Anzeige zählt automatisch jede Sekunde hoch.

## Voraussetzungen

- Raspberry Pi mit Raspberry Pi OS
- Python 3
- Bibliothek `gpiozero` (standardmäßig auf Raspberry Pi OS vorhanden)
- 74HC595 Schieberegister
- 4-stellige 7-Segment-Anzeige
- Breadboard und Jumper-Kabel

## Pinbelegung

### 74HC595-Ansteuerung

| Funktion      | GPIO (BCM) |
|---------------|------------|
| SDI (Daten)   | 24         |
| RCLK (Latch)  | 23         |
| SRCLK (Clock) | 18         |

### Ziffernwahl (Digit Enable)

| Ziffer | GPIO (BCM) |
|--------|------------|
| 1      | 10         |
| 2      | 22         |
| 3      | 27         |
| 4      | 17         |

## Installation

1. Python 3 sicherstellen:

    ```bash
    python3 --version
    ```

2. Ggf. fehlende Bibliotheken installieren:

    ```bash
    sudo apt update
    sudo apt install python3-gpiozero
    ```

3. Skript ausführbar machen:

    ```bash
    chmod +x zaehler.py
    ```

## Ausführung

Starte das Skript mit Root-Rechten, da GPIO-Zugriff benötigt wird:

```bash
sudo ./zaehler.py
