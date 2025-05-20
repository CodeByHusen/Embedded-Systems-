# Raspberry Pi Buzzer Steuerung mit wiringPi (C)

Dieses Projekt zeigt, wie man einen aktiven Buzzer (Summer) mit der Bibliothek `wiringPi` in C programmiert. Der Buzzer wird über GPIO regelmäßig ein- und ausgeschaltet, wodurch ein Piepsgeräusch entsteht.

## Hardware-Anforderungen

- Raspberry Pi (mit installiertem Raspbian/Linux)
- Aktiver Buzzer (aktiv-low)
- Verbindungskabel
- Steckbrett (optional)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Active-Summer/pictures/Komponenten.png)
### Schaltung

- **+ (Plus)** → **GPIO 17** (physisch Pin 11 / wiringPi-Pin 0)
- **- (Minus)** → **GND**
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Active-Summer/pictures/Schaltkreis.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Active-Summer/pictures/Schaltplan.png)
**Hinweis:** Der verwendete Buzzer ist *aktiv-low*, das heißt:  
- `LOW` (0V) = **Ton an**  
- `HIGH` (3.3V) = **Ton aus**

## Software-Voraussetzungen

- GCC (C-Compiler)
- wiringPi-Bibliothek (Hinweis: offiziell nicht mehr gewartet, ggf. Fork verwenden)

### Installation von wiringPi (wenn nicht vorhanden)

```bash
git clone https://github.com/WiringPi/WiringPi.git
cd WiringPi
./build
