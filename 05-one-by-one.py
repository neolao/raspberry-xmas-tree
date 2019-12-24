from tree import RGBXmasTree
from colorzero import Color
from time import sleep

tree = RGBXmasTree()
tree.brightness = 0.05
#tree.color = Color('red')

colors = [Color('red'), Color('green'), Color('blue')]

try:
    while True:
        for color in colors:
            #tree.color = color
            for pixel in tree:
                #pixel.on()
                pixel.color = color
                #print pixel.color
                #sleep(1)
except KeyboardInterrupt:
    tree.close()
