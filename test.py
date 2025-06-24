# Importing necessary libraries
from buildhat import ColorSensor, Matrix
import random

color = ColorSensor('A')
matrix = Matrix('B')

example = [
    [('green', 10), ('red', 10), ('red', 10)],
    [('red', 10), ('green', 10), ('red', 10)],
    [('red', 10), ('red', 10), ('blue', 10)]
]

try:
    while True:
        current = color.get_color()

        if current == 'black':
            current = 'white'
        if current == 'violet':
            current = 'lilac'

        print(current)
        matrix.clear((current, 10))
        #matrix.set_pixels(example)
except KeyboardInterrupt:
    print("Exiting loop...")