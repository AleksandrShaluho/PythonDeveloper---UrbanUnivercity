Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = []
NotPrimes = []
IsPrime = False

# метод перебора делителей
for i in Numbers:
    if i > 1:
        for j in range(2, i + 1):
            if j * j <= i and IsPrime == False:
                if i % j == 0:
                    IsPrime = True
            elif IsPrime==False:
                Primes.append(i)
                break
            else:
                NotPrimes.append(i)
                break
print(Primes)
print(NotPrimes)
