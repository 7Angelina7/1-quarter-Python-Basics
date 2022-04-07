# через исключение
def fun(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "Ошибка! Делить на ноль нельзя"
a = int(input("Введите первое число:"))
b = int(input("Введите второе число:"))
print(fun(a, b))




# через if
def fun():
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число:"))
    if b == 0:
        print("На ноль делить нельзя")
    c = a / b
    c = int(c)
    print(c)

fun()