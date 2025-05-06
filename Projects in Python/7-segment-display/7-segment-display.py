from gpiozero import OutputDevice
from time import sleep

# GPIO-Pins (BCM-Nummerierung)
SDI   = OutputDevice(17)  # Datenleitung (DS)
RCLK  = OutputDevice(18)  # Latch/Speichertakt (STCP)
SRCLK = OutputDevice(27)  # Schiebetakt (SHCP)

# Segment-Codes für 0–9, A–F (gemeinsame Kathode)
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

# Hex-Zeichen zur Anzeige
hex_digits = "0123456789ABCDEF"

def hc595_shift(data):
    """Sendet 8 Bit an den 74HC595 (MSB zuerst)"""
    for bit in range(8):
        # MSB zuerst übertragen
        SDI.value = bool(data & (0x80 >> bit))
        SRCLK.on()
        sleep(0.001)
        SRCLK.off()
    # Ausgabe übernehmen
    RCLK.on()
    sleep(0.001)
    RCLK.off()

def main():
    try:
        while True:
            for i in range(16):
                hc595_shift(segCode[i])
                print(f"Anzeige: {hex_digits[i]} (0x{segCode[i]:02X})")
                sleep(0.5)

    except KeyboardInterrupt:
        print("\nProgramm beendet.")

# Starte das Programm
if __name__ == "__main__":
    main()
