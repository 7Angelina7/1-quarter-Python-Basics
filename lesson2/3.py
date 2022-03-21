# со списком
a = input("Введите порядковый номер месяца:")
a = int(a)
li = ['зима','весна','лето','осень']
if a == 12 or a == 1 or a == 2:
    print(li[0])
elif a == 3 or a == 4 or a == 5:
    print(li[1])
elif a == 6 or a == 7 or a == 8:
    print(li[2])
elif a == 9 or a == 10 or a == 11:
    print(li[3])
else: print("неверно введен месяц")

# со словарем
a = input("Введите порядковый номер месяца:")
a = int(a)
di = {1: "зима", 2 : "весна", 3: "лето", 4: "осень"}
if a == 12 or a == 1 or a == 2:
    print(di.get(1))
elif a == 3 or a == 4 or a ==5:
    print(di.get(2))
elif a == 6 or a == 7 or a == 8:
    print(di.get(3))
elif a == 9 or a == 10 or a == 11:
    print(di.get(4))
else: print("неверно введен месяц")

