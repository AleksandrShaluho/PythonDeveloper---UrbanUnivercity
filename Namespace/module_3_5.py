import random


def GetMultipliedDigits(Number):
    StringOfDigits = str(Number)
    FirstDigit = int(StringOfDigits[0])
    # я подумал, что если в примере. приведенном в условии, пропускаются нули в середине числа, то они должны пропускаться и в конце. Иначе нелогично
    if len(StringOfDigits) == 1 or StringOfDigits[1:] == '0':
        return FirstDigit
    else:
        return FirstDigit * GetMultipliedDigits(int(StringOfDigits[1:]))

# можно раскомментировать и попробовать случайные числа. Строка с числом 360 - отработка задачи выкинуть ноль в конце
# Number = random.randint(1,1000)
Number = 360
print(f'Исходное число: {Number}')
print(f'Произведение цифр в числе (исключая все нули): {GetMultipliedDigits(Number)}')
