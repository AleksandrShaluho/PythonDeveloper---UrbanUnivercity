# нужна рекурсивная функция с условиями определяющими заход во вложенные структуры
def CalculateStructureSum(DataStructure):
  SumOfElements = 0
  for element in DataStructure:
  #почему float - потому что мы не знаем, будут ли только целые числа или попадутся дробные.
    if isinstance(element, float) or isinstance(element, int):
      SumOfElements +=element
    elif isinstance(element,str):
      SumOfElements +=len(element)
    #else:
    #  CalculateStructureSum(element)
  return SumOfElements

DataStructure = [1.2,2,3,'mommy',(1,2)]

#DataStructure = [
#  [1, 2, 3],
#  {'a': 4, 'b': 5},
#  (6, {'cube': 7, 'drum': 8}),
#  "Hello",
#  ((), [{(2, 'Urban', ('Urban2', 35))}])
#]

print(CalculateStructureSum(DataStructure))
#print(list(DataStructure))