# LCD1602 I2C Display – Beispielprogramm mit Python

Dieses Projekt demonstriert, wie man ein LCD1602-Display mit I2C-Schnittstelle über Python auf einem Raspberry Pi steuert. Es nutzt das `LCD1602`-Modul (separat erforderlich), um Nachrichten auf dem Display anzuzeigen.

## 📋 Voraussetzungen

- Raspberry Pi mit installiertem Raspberry Pi OS
- I2C aktiviert (`raspi-config`)
- LCD1602-Modul mit I2C (z. B. PCF8574T)
- Python 3
- `LCD1602.py`-Modul im selben Verzeichnis
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/I2C-LCD1602/pictures/Components.png)

## 🔧 Verkabelung

| LCD I2C Modul | Raspberry Pi GPIO |
|---------------|-------------------|
| VCC           | 5V                |
| GND           | GND               |
| SDA           | GPIO 2 (SDA)      |
| SCL           | GPIO 3 (SCL)      |

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/I2C-LCD1602/pictures/Circuit-diagram.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/I2C-LCD1602/pictures/circuit.png)

> Stelle sicher, dass I2C in `raspi-config` aktiviert ist:
> ```bash
> sudo raspi-config
> → Interface Options → I2C → Enable
> ```

## 📦 Installation (optional)

Falls du das `LCD1602`-Modul nicht hast, kannst du es z. B. so herunterladen:

```bash
webseite: https://toptechboy.com/?s=I2C

