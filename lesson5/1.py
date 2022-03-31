f = open("111.txt", "w", encoding = "utf - 8")
a = input("Введите текст \n")
while a:
    f.writelines(a)
    a = input("Введите текст \n")
    if not a:
        break

f.close()
f = open("111.txt", "r", encoding = "utf - 8")
text = f.readlines()
print(text)
f.close()