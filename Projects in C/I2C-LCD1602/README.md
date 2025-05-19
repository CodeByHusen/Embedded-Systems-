# LCD Steuerung über I2C mit WiringPi

Dieses Projekt zeigt, wie man ein I2C-basiertes 16x2 LCD-Display mit einem Raspberry Pi über die WiringPi-Bibliothek ansteuert. Das Display verwendet einen I2C-Adapter mit der Adresse `0x27`.

## 🧾 Voraussetzungen

- Raspberry Pi (mit installiertem Raspberry Pi OS)
- I2C-fähiges 16x2 LCD-Display (z. B. mit PCF8574-Chip)
- `wiringPi` Bibliothek
- GCC Compiler
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/I2C-LCD1602/pictures/Components.png)


## 🔧 Verkabelung

| LCD I2C Modul | Raspberry Pi GPIO |
|---------------|-------------------|
| VCC           | 5V                |
| GND           | GND               |
| SDA           | GPIO 2 (SDA)      |
| SCL           | GPIO 3 (SCL)      |

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/I2C-LCD1602/pictures/Circuit-diagram.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/I2C-LCD1602/pictures/circuit.png)

## 📦 Installation

### 1. WiringPi installieren

> Hinweis: WiringPi wurde offiziell eingestellt, aber einige Forks sind noch verfügbar. Alternativ kann auch `pigpio` oder `bcm2835` verwendet werden.

```bash
sudo apt-get install wiringpi
```
### 2. WiringPi installieren
```bash
sudo raspi-config
```
- Wähle Interfacing Options

- Aktiviere I2C

- Starte den Pi ggf. neu.

### 3. I2C-Adresse des LCD-Displays finden

```bash
sudo i2cdetect -y 1
```
Die typische Adresse ist 0x27. Falls anders, bitte im Code anpassen:
```c
int LCDAddr = 0x27;
```

## 🛠️ Kompilieren
```bash
gcc I2C-LCD1602.c -o lcd -lwiringPi
```

## ▶️ Ausführen
```bash
sudo ./lcd
```
