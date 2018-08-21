# -*- coding:utf-8 -*-

# 传统方法
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 取前3个元素

# first -- 笨方法
L1 = [L[0], L[1], L[2]]

# two -- 循环
r = []
n = 3
for i in range(n) :
    r.append(L[i])
L1 = r

#切片(Slice)操作符,能大大简化这种操作

# 对应上面的问题,取前3个元素,用一行代码就可以完成切片
L1 = L[0:3]
L1 = L[:3]

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])