# Relaissteuerung mit Python und GPIO Zero

Dieses Python-Skript steuert ein Relais über die GPIO-Pins eines Raspberry Pi mithilfe der `gpiozero`-Bibliothek. Es schaltet das Relais im Sekundentakt ein und aus, was sich ideal für einfache Automatisierungsaufgaben eignet, z. B. das Blinken einer angeschlossenen LED oder das Testen von Schaltkreisen.

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

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Relais/pictures/Komponenten.png)
---

## ⚙️ Funktionsweise

Das Skript erledigt Folgendes:

1. Initialisiert ein Relais am GPIO-Pin 17.
2. Schaltet das Relais im Wechsel **ein** (für 1 Sekunde) und **aus** (für 1 Sekunde).
3. Gibt dabei entsprechende Statusmeldungen in der Konsole aus.
4. Beendet sauber bei `Ctrl+C` durch Ausschalten des Relais.

---

## 💡 Schaltplan (Übersicht)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Relais/pictures/Schaltplan.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20Python/Relais/pictures/Schaltung.png)
