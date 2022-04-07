with open('333.txt', 'r', encoding = "utf-8") as file:
    a = []
    b = []
    list = file.read().split('\n')
    # print(type(list))
    # print(type(list[1]))
    # for i in range(len(list)):
    for i in list:
        i = i.split()
        if int(i[1]) < 20000:
            b.append(i[0])
        a.append(i[1])
print(f"Оклад меньше 20 000 {b}")
print(f"Средний оклад {sum(map(int, a))/len(a)}")