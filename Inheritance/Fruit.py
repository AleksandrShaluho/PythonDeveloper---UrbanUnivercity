from Inheritance.Plant import Plant


class Fruit(Plant):
    edible = True

    def __init__(self, name):
        self.name = name
