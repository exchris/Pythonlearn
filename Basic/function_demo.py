# -*-coding:utf-8 -*-

"""
一个函数包括输入参数和输出参数
"""


# 定义函数
def calulus(x):
    y = x + 1
    return y


# 调用函数
result = calulus(2)
print(result)


# 参数必须要正确地写入函数中，函数的参数也可以为多个
def fruit_function(fruit1, fruit2):
    """
    fruits = fruit1 + " " + fruit2
    return fruits
    """

    lst = [];
    lst.append(fruit1)
    lst.append(fruit2)
    return lst


# 调用函数
result = fruit_function("apple", "banana")
print(result)


# 取绝对值
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# 调用函数
my_abs(-1)


# 空函数
def nop():
    pass


# 返回多个值，函数可以返回多个值吗？答案是肯定的额
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 乘方
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# 调用函数
print("2^5:%d" % power(2, 5))


def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())


# 函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n * n
    return sum


print(calc(1, 2, 3, 4, 5, 6))
nums = [1, 2, 3]
print(calc(*nums))


def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# *args是可变参数，args接收的是一个tuple;
# **kw是关键字参数,kw接收的是一个dict
def func(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)

args = (1, 2, 3, 4, 5)
kw = {'x': 99}
func(*args, **kw)


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print("5!=%d" %fact(5))

# 尾递归优化
def fact1(n):
    return fact_iter(n, 1)
def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

# 列表，偶数在前，奇数在后
def sortArrayByParity(A):
    list1 = []
    list2 = []
    result = []
    for i in A:
        if i % 2 == 0:
            list1.append(i)
        else:
            list2.append(i)
    result = list1 + list2
    return result

A = [3,1,2,4]
print(sortArrayByParity(A))
