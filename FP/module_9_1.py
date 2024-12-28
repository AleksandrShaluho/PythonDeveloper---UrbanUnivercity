def apply_all_func(int_list, *functions):
    result = {}
    for function in functions:
        try:
            result[function.__name__] = function(int_list)
        except TypeError:
            print(f'В списке должны быть только числовые данные. Функция {function.__name__} не выполнена')
    return result


print(apply_all_func(['t', 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
