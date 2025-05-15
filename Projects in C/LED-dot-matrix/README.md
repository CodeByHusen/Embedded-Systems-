# LED-Matrixsteuerung mit 74HC595 und Raspberry Pi (C-Version)

Dieses C-Programm steuert mithilfe des 74HC595-Schieberegisters eine LED-Matrix über GPIO-Pins des Raspberry Pi an. Es werden vordefinierte Muster in einer Schleife vorwärts und rückwärts dargestellt.

## Voraussetzungen

- Raspberry Pi mit installiertem Linux (z. B. Raspberry Pi OS)
- Installierte [wiringPi](http://wiringpi.com/) Bibliothek (Achtung: bei neueren Raspberry Pi OS Versionen ggf. manuell installieren)
- GCC zum Kompilieren des C-Codes

## Hardware-Komponenten

- Raspberry Pi
- 74HC595 Schieberegister
- LED-Matrix (anoden-/kathoden-gesteuert)
- Verbindungskabel

## GPIO-Pinbelegung (wiringPi-Pin-Nummern)

| wiringPi-Pin | Bezeichnung | 74HC595-Pin       |
|--------------|-------------|-------------------|
| 0            | SDI         | DS (Dateneingang) |
| 1            | RCLK        | ST_CP (Latch)     |
| 2            | SRCLK       | SH_CP (Takt)      |

> **Hinweis:** WiringPi-Nummern unterscheiden sich von GPIO-BCM-Nummern. Du kannst mit `gpio readall` die Zuordnung prüfen.

## Kompilieren

```bash
gcc -o led_matrix led_matrix.c -lwiringPi
./led_matrix
```
