# Imports
import pygame
from buildhat import Motor, ColorSensor, Matrix

# Connecting accessories before we boot up Pygame
matrix = Matrix('B')
motors = [Motor('C'), Motor('D')]

# Pygame setup
pygame.init()
pygame.joystick.init()
clock = pygame.time.Clock()

# Defining a class for our controller
class JoyStick:
    def __init__(self, id):
        self.jsobject = pygame.joystick.Joystick(id)
        self.jsobject.init()

    def update(self):
        self.axes = [self.jsobject.get_axis(x) for x in range(self.jsobject.get_numaxes())]
        self.axesmap = ['L X', 'L Y', 'LT', 'R X', 'R Y', 'RT']
        self.buttons = [self.jsobject.get_button(x) for x in range(self.jsobject.get_numbuttons())]
        self.buttonsmap = ['B', 'A', 'Y', 'X', 'L', 'R', 'Select', 'Start', 'L Stick', 'R Stick', 'Home']
        self.hats = [self.jsobject.get_hat(x) for x in range(self.jsobject.get_numhats())]

# Properly quits out of pygame upon error
try:
    controller = JoyStick(0)

    # 
    while True:
        pygame.event.pump()
        controller.update()
        
        # Motor Logic
        speeds = [round(controller.axes[0] * 100) * -1, round(controller.axes[1] * 100) * -1]
        deadzone = 5

        if speeds[0] <= deadzone and speeds[0] >= (-1 * deadzone):
            speeds[0] = 0
            motors[0].stop()
        else:
            motors[0].start(speeds[0])

        if speeds[1] <= deadzone and speeds[1] >= (-1 * deadzone):
            speeds[1] = 1
            motors[1].stop()
        else:
            motors[1].start(speeds[1])
        
        print(controller.axes, controller.buttons, controller.hats, [motor.get_speed() for motor in motors], speeds)
        
        matrix.clear() # Wipe the matrix display
        matrix.set_pixel(tuple([x + 1 for x in controller.hats[0]]), ('yellow', 10)) # Sets a yellow light corresponding with d-pad coordinates

        if controller.buttons[1]:
            matrix.set_pixel((1,1), ('red', 10), display=True)
        else:
            matrix.set_pixel((1,1), ('red', 0), display=True)
        clock.tick(100)
except KeyboardInterrupt:
    print("Quitting...")
except pygame.error:
    print("Controller not found, connect before rerunning...")
finally:
    [motor.stop() for motor in motors]
    pygame.quit()