class House:
    def __init__(self, name, floors):
        self.name = name
        self.NumberOfFloors = floors

    def GoTo(self,newFloor):
        if newFloor < 1 or newFloor > self.NumberOfFloors:
            print('Такого этажа не существует')
        else:
            for i in range(1,newFloor+1):
                print(f'Этаж {i}')

