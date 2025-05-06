# 7-Segment-Anzeige mit 74HC595 und Raspberry Pi (C / wiringPi)

Dieses Projekt demonstriert die Ansteuerung einer **7-Segment-Anzeige** über ein **74HC595-Schieberegister** mithilfe eines **Raspberry Pi** und der Programmiersprache **C**. Ziel ist es, die hexadezimalen Zeichen **0–9 und A–F** nacheinander anzuzeigen.

---

## 📦 Inhalt

- [Überblick](#überblick)
- [Verwendete Hardware](#verwendete-hardware)
- [Schaltplan / Verdrahtung](#schaltplan--verdrahtung)
- [Segmentcode-Tabelle](#segmentcode-tabelle)
- [Voraussetzungen](#voraussetzungen)
- [Kompilierung und Ausführung](#kompilierung-und-ausführung)
- [Funktionsweise](#funktionsweise)
- [Autor & Lizenz](#autor--lizenz)

---

## Überblick

Das Programm sendet 8-Bit-Daten seriell vom Raspberry Pi an das Schieberegister **74HC595**, welches wiederum die 7-Segment-Anzeige steuert. Dabei werden die Ziffern **0–9** und Buchstaben **A–F** im Wechsel dargestellt.

---

## Verwendete Hardware

- Raspberry Pi (beliebiges Modell mit GPIOs)
- 74HC595 Schieberegister
- 1x 7-Segment-Anzeige (gemeinsame Kathode)
- 3 Jumperkabel für Datenleitungen
- 7–8 Widerstände (~220Ω) für Segmente
- Steckbrett & optional Stromversorgung

---

## Schaltplan / Verdrahtung

| Raspberry Pi GPIO (wiringPi-Nummer) | Pin am 74HC595 | Funktion                    |
|------------------------------------|----------------|-----------------------------|
| 0 (GPIO 17)                        | DS (Pin 14)     | Serieller Dateneingang      |
| 1 (GPIO 18)                        | STCP (Pin 12)   | Latch / Speichertakt        |
| 2 (GPIO 27)                        | SHCP (Pin 11)   | Schiebetakt                 |

Weitere wichtige Verbindungen:

- GND (Pi) → GND (Pin 8 am 74HC595)
- 3.3V/5V (Pi) → VCC (Pin 16 am 74HC595)
- Q0–Q7 (Pins 15, 1–7) → Segmente a–g und ggf. dp der 7-Segment-Anzeige (über Vorwiderstände)

---

## Segmentcode-Tabelle

Die Segmentcodes im Programm entsprechen der **gemeinsamen Kathoden-Konfiguration**. Jeder Bitwert (0–7) steht für ein Segment (a–g, dp).

```c
unsigned char SegCode[16] = {
    0x3f, // 0
    0x06, // 1
    0x5b, // 2
    0x4f, // 3
    0x66, // 4
    0x6d, // 5
    0x7d, // 6
    0x07, // 7
    0x7f, // 8
    0x6f, // 9
    0x77, // A
    0x7c, // B
    0x39, // C
    0x5e, // D
    0x79, // E
    0x71  // F
};
