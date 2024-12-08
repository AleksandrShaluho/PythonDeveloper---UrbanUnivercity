from Inheritance.Module_6_3.AquaticAnimal import AquaticAnimal
from Inheritance.Module_6_3.Bird import Bird
from Inheritance.Module_6_3.PoisonousAnimal import PoisonousAnimal


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed):
        self.sound = 'click-click-click'
        super().__init__(speed)

    def dive_in(self, dz):
        if self._cords[2] > 0:
            print('I''m in the air right now, can''t dive in. Need to splash down first')
        else:
            super().dive_in(dz)

    def splash_down(self):
        self._cords[2] = 0
