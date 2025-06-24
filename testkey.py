from buildhat import ColorSensor, Matrix
import random

color = ColorSensor('A')
matrix = Matrix('B')

example = [[('green', 10), ('red', 10), ('red', 10)],
           [('red', 10), ('green', 10), ('red', 10)],
           [('red', 10), ('red', 10), ('blue', 10)]]

try:
    while True:
        current = color.get_color()
        out = [[(current, 10) for x in range(3)] for y in range(3)]
        matrix.set_pixels(example)
except KeyboardInterrupt:
    print("Exiting loop...")