# нужна рекурсивная функция с условиями определяющими заход во вложенные структуры
def CalculateStructureSum(DataStructure):
  for each in DataStructure:
    if isinstance(each,dict)

DataStructure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(CalculateStructureSum(DataStructure))