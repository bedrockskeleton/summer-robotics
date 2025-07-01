# Imports
import pygame
from buildhat import Motor, ColorSensor, Matrix

# Connecting accessories before we boot up Pygame
matrix = Matrix('B')
motors = [Motor('C'), Motor('D')]
color = ColorSensor('A')

# Pygame setup
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# Defining a class for our controller
class JoyStick:
    def __init__(self, id):
        self.jsobject = pygame.joystick.Joystick(id)
        self.jsobject.init()
        self.name = self.jsobject.get_name()

    def update(self):
        # Mappings are shown according to the 8BitDo SN30 Pro in X-input mode
        self.axes = [self.jsobject.get_axis(x) for x in range(self.jsobject.get_numaxes())]
        self.axesmap = ['L X', 'L Y', 'LT', 'R X', 'R Y', 'RT']
        self.buttons = [self.jsobject.get_button(x) for x in range(self.jsobject.get_numbuttons())]
        self.buttonsmap = ['B', 'A', 'Y', 'X', 'L', 'R', 'Select', 'Start', 'L Stick', 'R Stick', 'Home']
        self.hats = [self.jsobject.get_hat(x) for x in range(self.jsobject.get_numhats())]

# Properly quits out of pygame upon error
try:
    controller = JoyStick(0)

    # Our main logic loop
    while True:
        pygame.event.pump()
        controller.update()
        
        # Motor Logic
        current = color.get_color()
        speed = round(controller.axes[1] * 100)
        direction = round(controller.axes[0] * -100)
        if abs(speed) + abs(direction) > 100:
            direction = (direction / abs(direction)) * (100 - abs(speed))
        deadzone = 5

        # Setting motor speeds
        if current == "red":
            print("I see red!")
        elif (speed <= deadzone and speed >= (-1 * deadzone)) and (direction <= deadzone and direction >= (-1 * deadzone)): # Deadzone consideration
            # If your stick is within the deadzone, the inputs will be nullified and the robot will stop
            speed = 0
            direction = 0
            [motor.stop() for motor in motors] # Stopping motors using list comprehension
        else:
            motors[0].start(speed + direction)
            motors[1].start((speed * -1) + direction)
        
        
        # This is what shows us all the information in the terminal
        print(controller.name, controller.axes, controller.buttons, controller.hats, [motor.get_speed() for motor in motors], speed, direction)
        
        matrix.clear() # Wipe the matrix display
        matrix.set_pixel(tuple([x + 1 for x in controller.hats[0]]), ('yellow', 10)) # Sets a yellow light corresponding with d-pad coordinates

        # Set a matrix light according to a button press
        if controller.buttons[1]:
            matrix.set_pixel((1,1), ('red', 10), display=True)
        else:
            matrix.set_pixel((1,1), ('red', 0), display=True)
        clock.tick(1000)
except KeyboardInterrupt:
    print("Quitting...")
except pygame.error:
    print("Controller not found, connect before rerunning...")
finally:
    [motor.stop() for motor in motors]
    pygame.quit()