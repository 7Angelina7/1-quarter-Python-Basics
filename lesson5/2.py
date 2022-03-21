f = open("222.txt", "r", encoding = "utf-8")
text = f.read()
print(f'Запись в файле: \n {text}')

f = open("222.txt", "r", encoding = "utf-8")
text = f.readlines()
print(f'1 Количество строк в файле - {len(text)}')

f = open("222.txt", "r", encoding = "utf-8")
text = f.readlines()
for i in range(len(text)):
    print(f'2 Количество символов {i + 1}-ой строки: {len(text[i])}')

f = open('222.txt', 'r', encoding = 'utf-8')
text = f.read()
text = text.split()
print(f'3 Общее количество слов - {len(text)}')
f.close()
