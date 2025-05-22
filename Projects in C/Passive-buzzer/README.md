# Piezo-Musik mit wiringPi (C)

Dieses C-Programm spielt zwei einfache Melodien über einen Piezo-Buzzer, der über `wiringPi` auf einem Raspberry Pi angesteuert wird. Es eignet sich ideal für Mikrocontroller-Experimente oder kleine Musikprojekte mit einem Buzzer.

## 🛠️ Voraussetzungen

### Hardware
- Raspberry Pi (z. B. Pi 3, 4, Zero)
- Piezo-Buzzer
- Verbindung zu **GPIO Pin 0** (wiringPi-Nummerierung)

### Software
- [wiringPi](http://wiringpi.com/)
  - ⚠️ Hinweis: wiringPi ist offiziell veraltet, funktioniert aber weiterhin auf vielen Systemen.
- GCC (C-Compiler)

## 🔌 Schaltung

Der Piezo-Buzzer wird wie folgt angeschlossen:

- Signal: **GPIO 17** (wiringPi Pin 0)
- GND: GND vom Raspberry Pi

## ▶️ Kompilieren & Ausführen

```bash
gcc passive-buzzer.c -o passive-buzzer -lwiringPi
sudo ./passive-buzzer
```

## 🎶 Beschreibung
Das Programm spielt zwei voreingestellte Melodien in einer Endlosschleife. Jeder Ton wird durch eine Frequenz (in Hz) und eine entsprechende Dauer (Multiplikator × 500 ms) definiert.

Melodien
- song_1: Eingängige, fröhliche Melodie

- song_2: Ruhigere Melodie mit abfallenden Tonfolgen

## 🧠 Wichtige Konstanten

```c
#define CM3 330  // C in mittlerer Oktave
#define CH1 525  // C in hoher Oktave
#define CL5 196  // G in tiefer Oktave
```

## 🛑 Beenden
Das Programm läuft in einer Endlosschleife. Zum Beenden drücke Strg + C.