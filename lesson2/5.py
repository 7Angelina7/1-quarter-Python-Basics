rating = [8,5,4,2,1]
print(f"Рейтинг - {rating}")
a = int(input("Введите число от 0 до 9 - "))
while a != 0:
    for el in range(len(rating)):
        if rating[el] == a:
            rating.insert(el + 1, a)
            break
        elif rating[0] < a:
            rating.insert(0,a)
        elif rating[-1] > a:
            rating.append(a)
        elif rating[el] > a and rating[el + 1] < a:
            rating.insert(el + 1,a)
    print(f"Новый рейтинг - {rating}")
    a = int(input("Введите число от 0 до 9 - "))



