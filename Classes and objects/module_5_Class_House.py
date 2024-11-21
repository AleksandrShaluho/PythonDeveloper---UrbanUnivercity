class House:
    def __init__(self, name, floors):
        self.name = name
        self.NumberOfFloors = floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.NumberOfFloors}'

    def __len__(self):
       return self.NumberOfFloors

    def GoTo(self,newFloor):
        if newFloor < 1 or newFloor > self.NumberOfFloors:
            print('Такого этажа не существует')
        else:
            for i in range(1,newFloor+1):
                print(f'Этаж {i}')

