a = input("Введите целое положительное число:")
a = int(a)
max = 0
while a > 0:
    b = a % 10
    a = a // 10
    if b > max:
        max = b
    if max == 9:
        break
print(max)