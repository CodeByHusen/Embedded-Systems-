# Relaissteuerungs-Programm mit WiringPi

Dieses C-Programm dient zur Steuerung eines Relaismoduls über einen Raspberry Pi mithilfe der WiringPi-Bibliothek. Das Relais wird in einer Endlosschleife regelmäßig ein- und ausgeschaltet. Dies kann beispielsweise verwendet werden, um einfache Automatisierungsaufgaben durchzuführen, wie das zeitgesteuerte Schalten von Geräten.

---
## 🔧 Verwendete Komponenten

- 🖥️ Raspberry Pi (mit GPIO-Unterstützung)
- 🔌 1 × Relaismodul
- 💡 1 × LED
- 🔁 1 × 1N4007-Diode (zum Schutz vor Spannungsspitzen)
- 🟦 1 × Widerstand (220 Ω – für die LED)
- 🟨 1 × Widerstand (1 kΩ – für Steuerkreis)
- 🔌 Mehrere Jumper-Kabel
- 🔲 1 × Breadboard
  
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Relais/pictures/Komponenten.png)
---

## 📌 Funktionsweise

Nach dem Start des Programms wird zunächst überprüft, ob die WiringPi-Bibliothek korrekt initialisiert wurde. Anschließend wird der entsprechende GPIO-Pin (GPIO17 bzw. WiringPi-Pin 0) als Ausgang konfiguriert. In einer Endlosschleife erfolgt dann abwechselnd:

- **Relais einschalten (aktivieren)**  
  Das Relais wird über den GPIO-Pin eingeschaltet (`digitalWrite(RelayPin, LOW)`), was bedeutet, dass Strom fließt und das angeschlossene Gerät aktiviert wird.

- **1 Sekunde warten**

- **Relais ausschalten (deaktivieren)**  
  Das Relais wird ausgeschaltet (`digitalWrite(RelayPin, HIGH)`), wodurch der Stromkreis unterbrochen wird.

- **1 Sekunde warten**

Während jeder Schaltaktion gibt das Programm Statusmeldungen auf der Konsole aus, um den aktuellen Zustand des Relais zu dokumentieren.

---



## 🔌 Hardware-Verdrahtung

| Raspberry Pi GPIO (BCM) | WiringPi-Pin | Funktion          |
|--------------------------|---------------|-------------------|
| GPIO17                   | Pin 0         | Steuerung des Relais |

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Relais/pictures/Schaltplan.png)

### Beispielverbindung:

- **VCC** des Relais → **5V** am Raspberry Pi  
- **GND** des Relais → **GND** am Raspberry Pi  
- **IN** des Relais → **GPIO17** (WiringPi-Pin 0)

> ⚠️ Achtung: Verwende ein Relais-Modul, das für den Raspberry Pi geeignet ist. Achte auf Pegelkompatibilität (3,3V vs. 5V).

---

## 🛠️ Kompilieren und Ausführen

### Kompilieren:

```bash
gcc -o relais relais.c -lwiringPi
sudo ./relais
```
