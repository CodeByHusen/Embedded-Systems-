# LED-Bargraph-Steuerung mit dem Raspberry Pi

Dieses Python-Programm steuert 10 LEDs, die an den GPIO-Pins des Raspberry Pi angeschlossen sind. Es verwendet die `gpiozero`-Bibliothek, um nacheinander verschiedene LED-Muster darzustellen – etwa die Beleuchtung ungerader, gerader oder aller LEDs in Folge.

## Programmbeschreibung

Das Programm enthält vier Hauptfunktionen:

- **odd_led_bar_graph()**  
  Aktiviert nacheinander die LEDs mit ungeraden Indizes (0, 2, 4, 6, 8).

- **even_led_bar_graph()**  
  Aktiviert nacheinander die LEDs mit geraden Indizes (1, 3, 5, 7, 9).

- **all_led_bar_graph()**  
  Aktiviert alle LEDs der Reihe nach.

- **turn_off_all_leds()**  
  Schaltet alle LEDs aus (auch beim Programmende durch `Ctrl+C`).

Diese Funktionen werden in einer Endlosschleife aufgerufen. Nach jeder Abfolge wird eine kurze Pause gemacht, um den Übergang zwischen den Mustern zu verdeutlichen.

---

## Pinbelegung (GPIO)

Die LEDs sind wie folgt an die GPIO-Pins des Raspberry Pi angeschlossen:

| LED-Index | GPIO-Pin | Physikalischer Pin | Beschreibung       |
|-----------|----------|--------------------|--------------------|
| 0         | 18       | Pin 12             | Erste LED          |
| 1         | 23       | Pin 16             | Zweite LED         |
| 2         | 24       | Pin 18             | Dritte LED         |
| 3         | 25       | Pin 22             | Vierte LED         |
| 4         | 8        | Pin 24             | Fünfte LED         |
| 5         | 7        | Pin 26             | Sechste LED        |
| 6         | 12       | Pin 32             | Siebte LED         |
| 7         | 16       | Pin 36             | Achte LED          |
| 8         | 20       | Pin 38             | Neunte LED         |
| 9         | 21       | Pin 40             | Zehnte LED         |

> 💡 **Hinweis:** Achte darauf, in jedem LED-Kreis einen geeigneten Vorwiderstand (z. B. 220 Ω) zu verwenden, um die GPIOs vor Überlastung zu schützen.

---

# Required Components
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/LED-Bar-Graph/pictures/Required%20Components.png)

# Build the circuit
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/LED-Bar-Graph/pictures/Build%20the%20circuit.png)

## Voraussetzungen

- Raspberry Pi mit Raspbian OS
- Python 3
- Bibliothek `gpiozero` (i. d. R. vorinstalliert)

## Installation und Ausführung

```bash
sudo apt update
sudo apt install python3-gpiozero  # nur falls nötig
python3 led_bar_graph.py
