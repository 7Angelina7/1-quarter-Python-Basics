li = [12, "cat", 55, True, 49, "dog"]
print(li)
print(li[0])
print(li[-1])
print(li[1:5:2])
print("before", li)
li[0],li[-1] = li[-1],li[0]
print("after",li)
print(li.count(12))
print(type(li[0]))

li = [12, "cat", 55, True, 49, "dog"]
for a in li:
    print(type(a))