MyList = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
# инициализируем переменную, чтобы гонять цикл по индексу списка
MylistIndex = 0

while MylistIndex != len(MyList) - 1:
    if MyList[MylistIndex] < 0:
        break
    elif MyList[MylistIndex] == 0:
        MylistIndex += 1
        continue
    else:
        print(MyList[MylistIndex])
        MylistIndex += 1
