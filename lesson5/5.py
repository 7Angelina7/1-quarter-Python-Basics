with open(r"555.txt","w",encoding="utf-8") as f:
    line = input('Введите цифры через пробел: ')
    f.writelines(line)
    numb = line.split()
    print("Сумма чисел:",sum(map(int, numb)))

