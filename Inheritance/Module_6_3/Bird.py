from random import randrange

from Inheritance.Module_6_3.Animal import Animal


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f'Here are(is) {randrange(1, 4)} eggs for you')
