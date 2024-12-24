from Inheritance.Figure import Figure
from math import sqrt


class Triangle(Figure):
    sides_count=3

    def __init__(self, color, *sides):
        #добавляем маленькую проверку (можно ли из сторон сложить треугольник)
        #к общему алгоритму родителя, подменяя sides если проверка не пройдена
        if len(sides) ==3 and not self.__is_triangle(sides):
            self.set_sides_by_default()
        else:
            super().__init__(color, *sides)


    def __is_triangle(self,sides):
        a,b,c = sides
        if (a+b>c) and (a+c>b) and (b+c>a):
            return True
        else:
            return False


    def get_square(self):
        p = self.__len__()/2
        sides= self.get_sides()
        return sqrt(p*(p-sides[0])*(p-sides[1])*(p-sides[2]))
    