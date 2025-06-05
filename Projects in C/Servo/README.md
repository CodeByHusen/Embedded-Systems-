# Servo-Steuerung mit Raspberry Pi und WiringPi

Dieses Programm steuert einen Servo-Motor über GPIO1 (WiringPi Pin 1) eines Raspberry Pi. Der Servo schwenkt dabei kontinuierlich von 0° bis 180° und zurück.

## Voraussetzungen

- Raspberry Pi (mit GPIO)
- WiringPi-Bibliothek (muss installiert sein)
- Ein Servo-Motor, angeschlossen an GPIO1
- C-Compiler (z. B. `gcc`)

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Servo/pictures/Komponenten.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Servo/pictures/Servo.png)


## Abhängigkeiten

Dieses Programm nutzt folgende Bibliotheken:

- `wiringPi.h`
- `softPwm.h`
- `stdio.h`

> Hinweis: `WiringPi` ist auf neueren Systemen nicht mehr vorinstalliert und muss ggf. manuell installiert werden.

## Kompilieren

```bash
gcc -o servo_control servo.c -lwiringPi
sudo ./servo_control
```

## Funktion
Das Programm:
1. Initialisiert WiringPi und den Software-PWM-Modus.
2. Steuert den Servo kontinuierlich in einer Schleife:
- von 0° auf 180°
- von 180° auf 0°
3. Nutzt softPwmWrite, um die Pulsweite entsprechend dem gewünschten Winkel anzupassen.

## Schaltplan (einfach)
- Servo-Signal: GPIO1 (WiringPi Pin 1)

- Servo-VCC: 5V-Pin des Raspberry Pi

- Servo-GND: GND des Raspberry Pi

![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Servo/pictures/Schematische%20Darstellung.png)
![Diagram](https://raw.githubusercontent.com/CodeByHusen/Embedded-Systems-/main/Projects%20in%20C/Servo/pictures/Schaltung.png)
