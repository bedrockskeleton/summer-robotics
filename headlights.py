from gpiozero import LED
from time import sleep

headlights = LED(5)
button = True

# Pretend that this is your game loop
while True:
    # This is the state of your button
    if button and not prevButton:
        # Toggles headlights on and off
        headlights.toggle()
    prevButton = button # Tracks the state of the previous button-press (prevents rapid toggling when button is held for more than a frame)
