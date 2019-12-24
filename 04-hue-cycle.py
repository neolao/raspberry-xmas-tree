from tree import RGBXmasTree
from colorzero import Color, Hue

tree = RGBXmasTree()

tree.color = Color('red')

try:
    while True:
        tree.color += Hue(deg=5)
except KeyboardInterrupt:
    tree.close()
