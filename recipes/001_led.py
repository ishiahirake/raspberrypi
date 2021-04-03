from time import sleep
from gpiozero import LED

light = LED(17)

while True:
    light.on()
    sleep(1)
    light.off()
    sleep(1)
