from module_5_Class_House import *

h1 = House('ЖК Эльбрус', 10)
print(House.HousesHistory)

h2 = House('ЖК Акация', 20)
print(House.HousesHistory)

h3 = House('ЖК Матрёшки', 20)
print(House.HousesHistory)

del h2
del h3

print(House.HousesHistory)
