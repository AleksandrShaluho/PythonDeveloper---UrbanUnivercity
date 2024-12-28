first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(elem[0]) - len(elem[1]) for elem in zip(first, second) if len(elem[0]) - len(elem[1]))
second_result = (len(first[elem]) == len(second[elem]) for elem in range(len(first)))

print(list(first_result))
print(list(second_result))
