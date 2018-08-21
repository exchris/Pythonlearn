# [1,2,3,4,5,6,7,8,9,10]
L1 = range(1,11)
print(L1)

L11 = []
for x in list(range(1,11)):
    L11.append(x*x)
L11
print(L11)

L12 = [x**2 for x in L1]
print(L12)

L13 = [x*x for x in L1]
print(L13)

L4 = [x*(x+1) for x in list(range(1,100,2))]
print(L4)