# Traurige Melodie mit TonalBuzzer

Dieses Python-Skript spielt eine einfache, traurige Melodie in a-Moll über einen TonalBuzzer, der an einen Raspberry Pi angeschlossen ist. Es eignet sich für kleine Embedded-Projekte, Musikexperimente oder als Einstieg in das Thema Soundausgabe mit GPIO.

## Voraussetzungen

- **Hardware**: Raspberry Pi (z. B. Pi 3, 4, Zero), TonalBuzzer oder passender Piezo-Summer am GPIO 17
- **Software**:
  - Python 3
  - `gpiozero`-Bibliothek (`pip install gpiozero`)

## Aufbau

Der TonalBuzzer wird über den GPIO-Pin 17 angesteuert. Das Skript definiert eine traurige Melodie mit Noten und deren Dauer. Mithilfe der Funktion `play()` werden die Töne nacheinander abgespielt.

## Melodie

Die Melodie basiert auf der A-Moll-Tonleiter und ist durch ruhige Intervalle und Pausen gekennzeichnet, um eine melancholische Stimmung zu erzeugen.

## Verwendung

1. Verbinde deinen TonalBuzzer mit dem GPIO-Pin 17 und GND.
2. Stelle sicher, dass Python 3 und `gpiozero` installiert sind.
3. Führe das Skript aus:

```bash
python3 traurige_melodie.py
```
Die Melodie wird abgespielt. Mit Strg + C kann der Vorgang jederzeit abgebrochen werden.
