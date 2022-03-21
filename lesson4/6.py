# from itertools import count
# n = int(input("Введите целое число:"))
#
# for el in count(n):
#     print(el)
#     if el == 10:
#         break


from itertools import cycle
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
i = 0
for el in cycle(a):
    i = i + 1
    print(el)
    if i > 100:
        break
