class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = round(weight,1)
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'

