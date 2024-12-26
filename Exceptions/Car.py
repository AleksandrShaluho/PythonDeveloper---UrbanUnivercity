from IncorrectVinNumber import *
from IncorrectCarNumber import *

class Car:

    def __init__(self,model,vin,numbers):
        self.model = model
        if self.__is_valid_vin(self, vin):
            self.__vin = vin
        if self.__is_valid_numbers(self, numbers):
            self.__numbers = numbers

    @staticmethod
    def __is_valid_vin(self,vin_number):
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not 1000000 <= vin_number <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    @staticmethod
    def __is_valid_numbers(self, numbers):
        if not isinstance(numbers,str):
            raise IncorrectCarNumber('Некорректный тип данных для номеров')
        if len(numbers) != 6:
            raise IncorrectCarNumber('Неверная длина номера')
        return True