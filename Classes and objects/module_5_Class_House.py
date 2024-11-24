class House:
    HousesHistory = []

    def __new__(cls, *args, **kwargs):
        cls.HousesHistory.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, floors):
        self.name = name
        self.NumberOfFloors = floors

    def __del__(self):
        print(f'{self.name} снесен, но он останется в истории')

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.NumberOfFloors}'

    def __len__(self):
        return self.NumberOfFloors

    def __eq__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors == other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __lt__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors < other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __le__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors <= other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __gt__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors > other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __ge__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors >= other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __ne__(self, other):
        if isinstance(other, House):
            if self.NumberOfFloors != other.NumberOfFloors:
                return True
            else:
                return False
        else:
            return "Ошибка в типе данных. Для сравнения должен передаваться объект класса House"

    def __add__(self, value):
        if isinstance(value, int):
            self.NumberOfFloors = self.NumberOfFloors + value
            return self
        else:
            return "Ошибка в типе данных. Тип данных передаваемого параметра должен быть int"

    def __iadd__(self, value):
        if isinstance(value, int):
            self.NumberOfFloors += value
            return self
        else:
            return "Ошибка в типе данных. Тип данных передаваемого параметра должен быть int"

    # на данном примере можно увидеть, что python не будет сам выполнять проверку типов, даже если указать тип данных для аргумента функции.
    # Python воспримет это как желательныйЮ но необязательный. Если в коде программы указать value = 10.5 например, то ошибок python не увидит.
    def __radd__(self, value: int):
        if isinstance(value, int):
            self.NumberOfFloors += value
            return self
        else:
            return "Ошибка в типе данных. Тип данных передаваемого параметра должен быть int"

    def GoTo(self, newFloor):
        if newFloor < 1 or newFloor > self.NumberOfFloors:
            print('Такого этажа не существует')
        else:
            for i in range(1, newFloor + 1):
                print(f'Этаж {i}')
