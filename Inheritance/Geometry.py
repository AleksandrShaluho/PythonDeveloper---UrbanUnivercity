from Circle import *
from Cube import *
from Triangle import *

#testing Cube...
#testing Cube.__init__ ...
cube1 = Cube((222, 35, 130), 6)
print(f'Test Cube.__init__ - normal sides {cube1.get_sides()} and color {cube1.get_color()}')
cube2 = Cube((222, 35, 130), 6, 7)
print(f'Test Cube.__init__ - too much sides {cube2.get_sides()}')
cube3 = Cube((222, 35, 130), -5, -5)
print(f'Test Cube.__init__ - negative sides {cube3.get_sides()}')
cube4 = Cube((222, 35, 330), 6)
print(f'Test Cube.__init__ - color out of range {cube4.get_color()}')
cube5 = Cube((222, 13), 6)
print(f'Test Cube.__init__ - missing argument of color {cube5.get_color()}')
#testing Cube.set_sides ...
cube1.set_sides(15)
print(f'Test Cube.set_sides - normal side {cube1.get_sides()}')
cube1.set_sides(6,6,11)
print(f'Test Cube.set_sides - too much sides {cube1.get_sides()}')
cube1.set_sides(-5,-5)
print(f'Test Cube.set_sides - negative side {cube1.get_sides()}')
#testing Cube.set_color ...
cube1.set_color(100, 100, 100)
print(f'Test Cube.set_color - normal color {cube1.get_color()}')
cube1.set_color(300,6,-1)
print(f'Test Cube.set_color - color out of range {cube1.get_color()}')
cube1.set_color(300,6.6,-1)
print(f'Test Cube.set_color - float type in parameters of color {cube1.get_color()}')
print(f'Test Cube.get_volume {cube1.get_volume()}')

#testing Circle...
circle1 = Circle((222, 35, 130), 15)
print(f'Test Circle - normal sides {circle1.get_sides()} and color {circle1.get_color()}')
print(f'Test Circle - get_square {circle1.get_square()}')

#testing Triangle...
triangle1 = Triangle((222,35,130),33,33,33)
print(f'Test Triangle - normal sides {triangle1.get_sides()} and color {triangle1.get_color()}')
triangle2 = Triangle((222,35,130),1,2,3)
print(f'Test Triangle - incorrect sides for triangle {triangle2.get_sides()}')
print(f'Test Triangle - get_square {triangle1.get_square()}')