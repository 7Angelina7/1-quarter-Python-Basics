file = open("666.txt","r", encoding="utf-8")
string = file.read().split("\n")
print(string)

dict = {}

for i in string:
    key = i.split(" ")[0]
    value = i.split(" ")[1:]
    dict[key] = value
print(dict)
print("Общее количество занятий по предметам:")
for i in dict:
    list = dict[i]
    sum = 0
    list = str(list)
    import re
    list2 = re.findall(r'\d+', list)
    for el in list2:
        el = int(el)
        sum = sum + el
    print(i, sum)
file.close()


# str = "Информатика: 50(л) 30(пр) 20(лаб)"
# print("Оригинальная строка: " + str)
# num = 0
# for c in str:
#     if c.isdigit():
#         c = int(c)
#         num = num + c
#
# print("сумма чисел в строке: ", num)



# import re
# str = "Информатика: 50(л) 30(пр) 20(лаб)"
# print("Оригинальная строка: " + str)
# str2 = re.findall(r'\d+', str)
# print(str2)
# sum = 0
# for el in str2:
#     el = int(el)
#     sum = sum + el
# print(sum)

