from gpiozero import LED as Horn
from time import sleep

horn = Horn(13)

while True:
    horn.on()
    sleep(0.001)
    horn.off()
    sleep(0.001)