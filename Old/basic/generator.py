# -*- coding:utf-8 -*-

# 生成器,next方法获取元素值

g = (x*x for x in range(10))

for n in g :
    print(n)

# 斐波拉契数列用列表生成式写不出来,但是,用函数把它打印出来却很容易
def fib(max) :
    n, a, b = 0, 0, 1
    while n < max :
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

print(fib(6))

#fib函数实际上是定义了斐波拉契数列的推算规则,可以从第一个元素开始,推算出后续任意的元素,这种逻辑其实非常类似generator
# 也就是说,上面的函数和generator仅一步之遥。要把fib函数变成generator,只需要把print(b)改为yield b 就可以了:

def fib1(max) :
    n, a, b = 0, 0, 1
    while n < max :
      yield b
      a, b = b, a + b
      n = n + 1
    return 'done'

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)

def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


# 杨辉三角

def triangles() :
    line = [1]
    while True :
        yield line
        line = [x + y for x, y in zip([0] + line, line + [0])]

n = 0
for t in triangles() :
    print(t)
    n = n + 1
    if n == 10 :
        break

def triangle1() :
    L = [1] # 定义L为一个只包含一个元素的列表
    while True :
        yield L # 定义为生成器函数
        L = [1] + [L[n] + L[n-1] for n in range(1, len(L))] + [1]

i = 0
for t in triangle1() :
    print(t)
    i = i + 1
    if i == 10 :
        break