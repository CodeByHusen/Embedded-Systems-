# LED-Matrixsteuerung mit 74HC595 und Raspberry Pi

Dieses Python-Skript verwendet einen **Raspberry Pi** und ein **74HC595 Schieberegister**, um eine LED-Matrix über GPIO-Pins anzusteuern. Dabei werden vordefinierte Muster in einer Schleife vorwärts und rückwärts auf der Matrix angezeigt.

## Hardware-Komponenten

- Raspberry Pi (mit installiertem Raspbian OS)
- 74HC595 Schieberegister
- LED-Matrix (Anoden und Kathoden entsprechend verschaltet)
- Verbindungskabel

## GPIO-Pinbelegung

| Raspberry Pi GPIO | Funktion am 74HC595         |
|-------------------|-----------------------------|
| GPIO 17           | Serieller Dateneingang (SDI)|
| GPIO 18           | Register Clock (RCLK)       |
| GPIO 27           | Shift Clock (SRCLK)         |

## Funktionsweise

- `code_H` definiert das Anoden-Muster (Zeilen) der LED-Matrix.
- `code_L` definiert das Kathoden-Muster (Spalten).
- Die Funktion `hc595_shift()` sendet ein Byte seriell an das Schieberegister.
- Das Hauptprogramm (`main()`) läuft in einer Endlosschleife und zeigt die Muster in auf- und absteigender Reihenfolge an.

## Nutzung

1. **Python-Skript ausführbar machen:**
   ```bash
   chmod +x matrix_steuerung.py
   ```

2. **Skript starten:**
    ```bash
   python3 matrix_steuerung.py
   ```

   
