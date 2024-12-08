class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _DANGER_LEVEL = 5

    def __init__(self, speed):
        self._cords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if dz * self.speed < 0:
            print('It''s too deep, i can''t dive :(')
            return
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < self._DANGER_LEVEL:
            print('Sorry, i''m peaceful :)')
        else:
            print('Be careful, i''m attacking you 0_0')

    def speak(self):
        print(self.sound)
