# Imports
import pygame
from gpiozero import DistanceSensor
from buildhat import Motor, MotorPair

# Connecting accessories before we boot up Pygame
motors = MotorPair('A', 'B')
ultrasonic = DistanceSensor(echo=17, trigger=4)

# Pygame setup
pygame.init()
clock = pygame.time.Clock()

# Properly quits out of pygame upon error
try:

    # Our main logic loop
    while True:
        pygame.event.pump()
        
        # Motor Logic
        speed = (round((ultrasonic.distance - 0.25) * 100))
        deadzone = 5

        # Setting left motor speed
        if speed <= deadzone and speed >= (-1 * deadzone):
            speed = 0
            motors.stop()
        else:
            motors.start(speed, speed)
        
        # This is what shows us all the information in the terminal
        print(speed, ultrasonic.distance)
        
        clock.tick(10)
except KeyboardInterrupt:
    print("Quitting...")
finally:
    motors.stop()
    pygame.quit()