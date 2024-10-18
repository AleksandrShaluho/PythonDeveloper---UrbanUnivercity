first = int(input("Введите пожалуйста первое ЦЕЛОЕ ЧИСЛО:"))
second = int(input("Введите пожалуйста второе ЦЕЛОЕ ЧИСЛО:"))
third = int(input("Введите пожалуйста третье ЦЕЛОЕ ЧИСЛО:"))

if first==second==third:
    print(3)
elif first==second or second==third or first==third:
    print(2)
else:
    print(0)
