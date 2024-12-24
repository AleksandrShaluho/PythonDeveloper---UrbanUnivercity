from Inheritance.Figure import Figure


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        # добавляем в конструктор и в метод set_sides доп. условие, если введена одна сторона, то
        # сразу превращаем ее в 12 одинаковых сторон. А потом отдаем методу родителя для необходимых проверок и создания
        # атрибута __sides
        if len(sides) == 1:
            sides = sides * self.sides_count
        super().__init__(color, *sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1:
            new_sides = new_sides * self.sides_count
        super().set_sides(*new_sides)

    def get_volume(self):
        # так как атрибут __sides приватный нигде в классе не создается, а для его создания используются методы родителя
        # то и пользоваться этим атрибутом напрамую нельзя только черз геттер (потому что все сидит в _Figure__sides),
        # который с помощью self проведет нас в класс Figure, где и хранится __sides
        # иная реализация потребует повтора кода в классе наследнике либо отказа от закрытости атрибута
        # до другого я не додумался)
        return self.get_sides()[0] ** 3
