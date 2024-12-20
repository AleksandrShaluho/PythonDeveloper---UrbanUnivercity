
# где тут использовать *args - не придумал. Почему-то получилось без этого.
def CalculateStructureSum(DataStructure):
  """Функция CalculateStructureSum.

  Предназначена для подсчета суммы значений элементов в структуре данных.
  Элементы могут быть целочисленные (тогда берутся их значения) либо строковыми (тогда подсчитывается длина строки).
  Иные типы данных для элементов - не допускаются.

  Функция обрабатывает любую структуру данных (множество, словарь, список, кортеж) любой степени вложенности
  """

  Total = 0
  for element in DataStructure:
    if isinstance(element,str):
      Total+=len(element)
      continue
    elif isinstance(element, (int)):
      Total+= element
      continue

# пробовал как-то обойтись без обработки словаря отдельно, но ничего не придумал. Не хватает общего у структур данных)
# единственно что - подменил "element", преобразовав словарь в список (объединил список ключей и список значений)
# благодаря чему можно было использовать тот же рекурсивный алгоритм что и для списков, кортежей, множеств
    elif isinstance(element,dict):
      element = list(element.keys()) + list(element.values())

#тут кроется возможный крах при появлении неожиданного типа данных. Например, если элемент будет НЕ целым числом, то алгоритм выдаст ошибку.
# поэтому либо в начале функции делать блок проверки соответствия типа входных параметров (что лучше всего - проверить ДО обработки)
# либо в процессе отработать исключения, прервать алгоритм и выдать предупреждение (хотя по принципам -- корректность данных обеспечивает передающая сторона))
#как иначе этого избежать - не придумал
    Total+=CalculateStructureSum(element)
  return Total

DataStructure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

#такой список без проверки на входе приведет к незаметной ошибке. Логический тип данных элемента True. Элемент будет воспринят как числовой и повлияет на итог
#хотя никаких правил обработки логических значений алгоритмом не предусмотрено.
# DataStructure = [
#   [1, True, 3],
#   {'a': 4, 'b': 5},
#   (6, {'cube': 7, 'drum': 8}),
#   "Hello",
#   ((), [{(2, 'Urban', ('Urban2', 35))}])
# ]

print(f'Сумма элементов: {CalculateStructureSum(DataStructure)}')

#как можно вывести описание функции
#print(CalculateStructureSum.__doc__)
