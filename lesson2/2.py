li = input("Введите список элементов:").split( )
print("before", (li))
for a in range(0,len(li)-1,2):
    li[a], li[a+1] = li[a+1], li[a]
print("after", li)


