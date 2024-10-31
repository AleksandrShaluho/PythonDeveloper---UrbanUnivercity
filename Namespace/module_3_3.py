def PrintParams(a=1, b='строка', c=True):
    print(a, b, c)


ValuesList = [25, 'The Best', [0, 0, 0]]
ValuesList2 = [25, 'The Best']
ValuesDict = {'a': 10, 'b': 'daddy', 'c': [1, 1, 1]}

PrintParams(c=[1, 2, 3])
PrintParams(*ValuesList)
PrintParams(**ValuesDict)
PrintParams(*ValuesList2, 42)
