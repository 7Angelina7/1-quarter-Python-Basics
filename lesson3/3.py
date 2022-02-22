def my_func(num1, num2, num3):
    print(f'Сумма двух наибольших аргументов равна: {num1 + num2 + num3 - min([num1, num2, num3])}')

my_func(int(input('Число 1:')),int(input('Число 2:')),int(input('Число 3:')))