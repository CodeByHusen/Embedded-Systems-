# LED-Bargraph mit dem Raspberry Pi (C, wiringPi)

Dieses C-Programm steuert 10 LEDs über die GPIO-Pins eines Raspberry Pi mithilfe der `wiringPi`-Bibliothek. Es zeigt verschiedene LED-Muster an: ungerade LEDs, gerade LEDs und alle LEDs nacheinander.

## Programmbeschreibung

Das Programm besteht aus drei LED-Anzeigemustern:

- **oddLedBarGraph()**  
  Aktiviert nacheinander die LEDs mit den ungeraden Indizes (0, 2, 4, 6, 8).

- **evenLedBarGraph()**  
  Aktiviert nacheinander die LEDs mit den geraden Indizes (1, 3, 5, 7, 9).

- **allLedBarGraph()**  
  Aktiviert nacheinander alle LEDs von 0 bis 9.

Diese Muster laufen in einer Endlosschleife. Zu Beginn werden alle verwendeten GPIO-Pins als Ausgang gesetzt und auf LOW geschaltet.

---

## Pinbelegung (wiringPi → GPIO)

Die LED-Pins werden über ein Array festgelegt:

int pins[10] = {0,1,2,3,4,5,6,8,9,10};

Die LED-Pins im Code sind als int pins[10] = {0,1,2,3,4,5,6,8,9,10}; definiert. Das entspricht folgender Zuordnung:

| Index | wiringPi Pin | GPIO    | Physikalischer Pin | Beschreibung |
| ----- | ------------ | ------- | ------------------ | ------------ |
| 0     | 0            | GPIO 17 | Pin 11             | LED 1        |
| 1     | 1            | GPIO 18 | Pin 12             | LED 2        |
| 2     | 2            | GPIO 27 | Pin 13             | LED 3        |
| 3     | 3            | GPIO 22 | Pin 15             | LED 4        |
| 4     | 4            | GPIO 23 | Pin 16             | LED 5        |
| 5     | 5            | GPIO 24 | Pin 18             | LED 6        |
| 6     | 6            | GPIO 25 | Pin 22             | LED 7        |
| 7     | 8            | GPIO 2  | Pin 3              | LED 8        |
| 8     | 9            | GPIO 3  | Pin 5              | LED 9        |
| 9     | 10           | GPIO 8  | Pin 24             | LED 10       |


# Required Components
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/LED-Bar-Graph/pictures/Required%20Components.png)

# Build the circuit
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/LED-Bar-Graph/pictures/Build%20the%20circuit.png)
