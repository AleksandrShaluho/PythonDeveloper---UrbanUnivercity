def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных у элемента {number}. Для подсчета суммы элемент должен быть числом')
    return result, incorrect_data


def calculate_average(numbers):
    average = 0
    try:
        number_sum, incorrect_elem = personal_sum(numbers)
        average = number_sum / (len(numbers) - incorrect_elem)
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return
    except ZeroDivisionError:
        average = 0
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
