import time
import board
import digitalio
import busio

print("Hello blinka!")
# Try to great a Digital input
pin = digitalio.DigitalInOut(board.D4)
print("Digital IO ok!")
# Try to create an I2C device
i2c = busio.I2C(board.SCL, board.SDA)
print("I2C ok!")
# Try to create an SPI device
spi = busio.SPI(board.SCLK, board.MOSI, board.MISO)
print("SPI ok!")

btnA = digitalio.DigitalInOut(board.D5)
btnA.pull = digitalio.Pull.UP

btnB = digitalio.DigitalInOut(board.D6)
btnB.pull = digitalio.Pull.UP

btnC = digitalio.DigitalInOut(board.D16)
btnC.pull = digitalio.Pull.UP

btnD = digitalio.DigitalInOut(board.D24)
btnD.pull = digitalio.Pull.UP

while True:
    if not btnA.value:
        print(f"A")
        time.sleep(1)
    if not btnB.value:
        print(f"B")
        time.sleep(1)
    # if not btnC.value:
    #     print(f"C")
    #     time.sleep(1)
    # if not btnD.value:
    #     print(f"D")
    #     time.sleep(1)
