# 7-Segment-Anzeige mit 74HC595 und Raspberry Pi (Python)

Dieses Projekt zeigt, wie man eine **7-Segment-Anzeige** mithilfe eines **74HC595-Schieberegisters** und einem **Raspberry Pi** steuert. Die Anzeige zeigt die hexadezimalen Ziffern **0–9** und **A–F** nacheinander an.

---

## 📦 Inhalt

- [Überblick](#überblick)
- [Verwendete Hardware](#verwendete-hardware)
- [Schaltplan / Verdrahtung](#schaltplan--verdrahtung)
- [Segmentcode-Tabelle](#segmentcode-tabelle)
- [Voraussetzungen](#voraussetzungen)


---

## Überblick

Das Programm sendet 8-Bit-Daten seriell vom Raspberry Pi an das 74HC595-Schieberegister, welches wiederum die 7-Segment-Anzeige steuert. Dabei werden die hexadezimalen Ziffern **0–9** und Buchstaben **A–F** im Wechsel angezeigt.

---

## Verwendete Hardware

- Raspberry Pi (beliebiges Modell mit GPIOs)
- 74HC595 Schieberegister
- 1x 7-Segment-Anzeige (gemeinsame Kathode)
- Jumperkabel für die Verbindung zwischen Raspberry Pi und 74HC595
- Widerstände (ca. 220Ω) für die Segmente der 7-Segment-Anzeige
- Steckbrett & optional Stromversorgung

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/7-segment-display/pictures/Komponenten.png)
---

## Schaltplan / Verdrahtung

| Raspberry Pi GPIO (BCM-Nummerierung) | Pin am 74HC595 | Funktion                    |
|-------------------------------------|----------------|-----------------------------|
| GPIO 17                             | DS (Pin 14)    | Serieller Dateneingang      |
| GPIO 18                             | STCP (Pin 12)  | Latch / Speichertakt        |
| GPIO 27                             | SHCP (Pin 11)  | Schiebetakt                 |

Zusätzliche Verbindungen:

- GND (Pi) → GND (Pin 8 am 74HC595)
- 3.3V/5V (Pi) → VCC (Pin 16 am 74HC595)
- Q0–Q7 (Pins 15, 1–7) → Segmente a–g und ggf. dp der 7-Segment-Anzeige (über Vorwiderstände)

---

## Segmentcode-Tabelle

Die Segmentcodes im Programm entsprechen der **gemeinsamen Kathoden-Konfiguration**. Jeder Bitwert (0–7) steht für ein Segment (a–g, dp):

```python
segCode = [
    0x3F,  # 0
    0x06,  # 1
    0x5B,  # 2
    0x4F,  # 3
    0x66,  # 4
    0x6D,  # 5
    0x7D,  # 6
    0x07,  # 7
    0x7F,  # 8
    0x6F,  # 9
    0x77,  # A
    0x7C,  # B
    0x39,  # C
    0x5E,  # D
    0x79,  # E
    0x71   # F
]
```

##  Voraussetzungen
- Betriebssystem: Raspberry Pi OS (Lite oder Desktop)

- Abhängigkeit: gpiozero (Python-Bibliothek zur Steuerung der GPIOs)

- Entwicklungsumgebung: Python 3 und ein Texteditor oder IDE

- Installierte Bibliotheken:

    - gpiozero: sudo pip3 install gpiozero
