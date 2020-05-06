input = [(0, 1), (3, 5), (2, 4), (10, 12), (9, 10)]

for idx, el in enumerate(input):
    print(idx, el)

for i in range(len(input)):
    print(i + 1) #print 1 -> 5


#swap
a = 5
b = 7

a, b = b, a

print(a, b) # a = 7 b = 5