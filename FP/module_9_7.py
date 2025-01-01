def is_prime(func):
    def wrapper(*numbers):
        number = func(*numbers)
        __is_prime = True
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    __is_prime = False
                    break
            if __is_prime:
                print('Простое')
            else:
                print('Составное')
        else:
            print('Ни простое, ни составное')
        return number
    return wrapper


@is_prime
def sum_three(*numbers):
    return sum(numbers)


result = sum_three(2, 3, 6)
print(result)
