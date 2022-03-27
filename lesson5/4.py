dic = {"One" : "Один", "Two" : "Два", "Three" : "Три", "Four" : "Четыре"}
new_file = []
with open("444.txt") as f_obj:

    for i in f_obj:
        i = i.split(" ",1)
        new_file.append(dic[i[0]]+" "+i[1])
print(new_file)

with open('4444.txt', 'w', encoding="utf-8") as f_obj_2:
    f_obj_2.writelines(new_file)






