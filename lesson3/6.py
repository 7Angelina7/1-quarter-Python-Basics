#Для строки
# def int_func(text):
#     return text.title()
# li_1 = []
# for word in input("Введите строку, где слова разделены пробелами:").split():
#     li_1.append(int_func(word))
# print(f"Новая строка:{' '.join(li_1)}")

#Одно слово
def int_func(word):
    return word.title()

word = input("Введите слово строчными буквами:")
int_func(word)
print(f'Новое слово:{word.title()}')
