#!/usr/bin/env python3
from gpiozero import OutputDevice
from time import sleep

# GPIO-Pins, die mit dem 74HC595 Schieberegister verbunden sind, definieren
SDI = OutputDevice(17)   # Serieller Dateneingang
RCLK = OutputDevice(18)  # Register Clock
SRCLK = OutputDevice(27) # Schieberegistertakt

# Muster für die Matrixanzeige definieren; ROWs sind Anoden (+), COLs sind Kathoden (-)
# Muster für ROWs (Anodensignale)
code_H = [0x01, 0xff, 0x80, 0xff, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff, 0xff]
# Muster für COLs (Kathodensignale)
code_L = [0x00, 0x7f, 0x00, 0xfe, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0xfe, 0xfd, 0xfb, 0xf7, 0xef, 0xdf, 0xbf, 0x7f]

# Daten an 74HC595 senden
def hc595_shift(dat):
   """ Daten an das 74HC595 Schieberegister senden, um auf der Matrix anzuzeigen. """
   for i in range(8):
      # SDI-Wert setzen und Schieberegistertakt auslösen
      SDI.value = 0x80 & (dat << i)
      SRCLK.on()
      SRCLK.off()
   # Register Clock auslösen, um die Anzeige zu aktualisieren
   RCLK.on()
   sleep(0.001)
   RCLK.off()

def main():
   """ Hauptloop, um durch die Anzeigemuster zu zyklen. """
   while True:
      # Durch die Muster in aufsteigender Reihenfolge zyklen
      for i in range(len(code_H)):
            hc595_shift(code_L[i])
            hc595_shift(code_H[i])
            sleep(0.1)

      # Durch die Muster in absteigender Reihenfolge zyklen
      for i in range(len(code_H)-1, -1, -1):
            hc595_shift(code_L[i])
            hc595_shift(code_H[i])
            sleep(0.1)

# Hauptloop ausführen, Tastaturunterbrechung elegant behandeln
try:
   main()
except KeyboardInterrupt:
   pass