def add_everything_up(a, b):
    try:
        return a+b
    except TypeError:
        return str(a) + str(b)
    finally:
        print(f'Исходные значения были: a = {a}, тип - {type(a)}; b = {b}, тип - {type(b)}')

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
print(add_everything_up('яблоко', 'мандарин'))
