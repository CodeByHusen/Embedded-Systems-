# 7-Segment-Zähler mit Raspberry Pi und 74HC595

Dieses Projekt zeigt, wie man ein 4-stelliges 7-Segment-Display mithilfe eines 74HC595-Schieberegisters und der WiringPi-Bibliothek auf einem Raspberry Pi ansteuert. Der Zähler erhöht sich jede Sekunde automatisch und zeigt den aktuellen Wert auf dem Display an.

## Voraussetzungen

- Raspberry Pi mit installiertem Raspberry Pi OS
- WiringPi-Bibliothek (trotz Deprecation noch verwendet)
- 74HC595 Schieberegister
- 4-stelliges 7-Segment-Display
- Breadboard und Jumper-Kabel

## Pinbelegung

| Funktion       | WiringPi-Pin |
|----------------|--------------|
| SDI (Daten)    | 5            |
| RCLK (Latch)   | 4            |
| SRCLK (Takt)   | 1            |
| Digit 1        | 12           |
| Digit 2        | 3            |
| Digit 3        | 2            |
| Digit 4        | 0            |

## Kompilierung

Stelle sicher, dass `wiringPi` installiert ist (alternativ nutze ein Fork wie `pigpio` oder `wiringPi2`, falls `wiringPi` nicht verfügbar ist).

```bash
gcc -o zaehler zaehler.c -lwiringPi
