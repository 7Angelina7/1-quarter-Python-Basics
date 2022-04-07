from functools import reduce
a = [el for el in range(100,1001,2)]
print(a)
print(reduce(lambda x,y: x*y, a))
