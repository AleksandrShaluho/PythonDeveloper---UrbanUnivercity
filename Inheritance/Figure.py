class Figure:
    sides_count = 0
    # учитывая требование задачи создавать фигуры с единичными сторонами при ошбике в параметрах - введен атрибут класса
    # позволяющий это делать, при этом количество сторон будет определяться исходя из параметров наследника либо родителя.
    __default_side_size = [1]
    # по аналогии сделано для параметров цвета. Хотя в задаче нет такого требования, тем не менее ошибка возможно не только
    # в методе set_color, но и при создании объекта
    __default_color = (255, 255, 255)

    def __init__(self, color, *sides):
        #не осилил обобщить и сделать использование здесь метода set_sides
        if self.__is_valid_sides(sides):
            # в условиях задачи и выходных примерах сказано "СПИСОК". Значит список, хотя *args дает кортежи
            self.__sides = list(sides)
        else:
            self.set_sides_by_default()
        if len(color) != 3 or not self.__is_valid_color(*color):
            self.__color = self.__default_color
        else:
            self.__color = color
        self.filled = False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, R, G, B):
        if any(color > 255 or color < 0 for color in (R, G, B)):
            return False
        elif any(not isinstance(color, int) for color in (R, G, B)):
            return False
        else:
            return True

    def set_color(self, R, G, B):
        if self.__is_valid_color(R, G, B):
            self.__color = (R, G, B)

    def __is_valid_sides(self, sides):
        if any(side < 0 for side in sides) or (len(sides) != self.sides_count):
            return False
        else:
            return True

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            # в условиях задачи и выходных примерах сказано "СПИСОК". Значит список, хотя *args дает кортежи
            self.__sides = list(new_sides)

    def set_sides_by_default(self):
        self.__sides = self.__default_side_size * self.sides_count

    def __len__(self):
        return sum(self.__sides)

