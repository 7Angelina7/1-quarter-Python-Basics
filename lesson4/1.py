from sys import argv
print(argv)
print(argv[1])
print(argv[2])
print(argv[3])
argv[1] = int(argv[1])
argv[2] = int(argv[2])
argv[3] = int(argv[3])

print(argv[1] * argv[2] + argv[3])
