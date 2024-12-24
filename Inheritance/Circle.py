from Inheritance.Figure import Figure
from math import pi


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        # радиус можно вычислить только после того как __sides установлен окончательно (после всех проверок и установки дефолтного значения
        # если это необходимо.
        self.__radius = self.get_sides()[0] / (2 * pi)

    def get_square(self):
        return pi * (self.__radius ** 2)
