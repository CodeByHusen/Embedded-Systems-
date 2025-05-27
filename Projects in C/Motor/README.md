# Motor-C

Ein einfaches C-Programm zur Steuerung eines Gleichstrommotors über die GPIO-Pins eines Raspberry Pi mit der Bibliothek [`wiringPi`](http://wiringpi.com/).  
Das Programm lässt den Motor abwechselnd im und gegen den Uhrzeigersinn laufen, jeweils für 3 Sekunden mit Pausen dazwischen.

## Voraussetzungen

- Raspberry Pi (mit GPIO-Pins)
- Ein Gleichstrommotor mit Motortreiber (z. B. L298N)
- Bibliothek `wiringPi` installiert (Hinweis: Wird offiziell nicht mehr gepflegt, aber über Repos oder manuell installierbar).

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Motor/pictures/Komponenten.png)


## GPIO-Pinbelegung (WiringPi-Nummerierung)

| Funktion         | WiringPi-Pin |
|------------------|---------------|
| Motor Input 1    | 0             |
| Motor Input 2    | 2             |
| Motor Enable     | 3             |.

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Motor/pictures/Schaltplan.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Motor/pictures/Schaltung.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Motor/pictures/L293D .png)
## Installation

1. Installiere `wiringPi` (sofern nicht vorhanden):
   ```bash
   sudo apt update
   sudo apt install wiringpi
