<<<<<<< HEAD

# -*- coding:utf-8 -*-

from functools import reduce

CHAR_TO_INT = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9
}

def str2int(s) :
    ints = map(lambda ch : CHAR_TO_INT[ch], s)
    return reduce(lambda x, y : x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0' : 0,
    '1' : 1,
    '2' : 2,
    '3' : 3,
    '4' : 4,
    '5' : 5,
    '6' : 6,
    '7' : 7,
    '8' : 8,
    '9' : 9,
    '.' : -1
}

def str2float(s) :
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n) :
        nonlocal point
        if n == -1 :
            point = 1
            return f
        if point == 0 :
            return f * 10 + n
        else :
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
=======
# -*- coding:utf-8 -*-
def f(x) :
	return x**2

r = map(f,  list(range(10)))

print(list(r)) 
# [1,4,9,16,25,36,49,64,81]

# 等价于
L = []
for n in range(10) :
	L.append(f(n))
print(L)

# 导入reduce
from functools import reduce
def add(x, y) :
	return x + y

# 求1-10的奇数总和
result = reduce(add, list(x for x in range(10) if x % 2 == 1))
print(result)

# 将1-10的所有奇数组成成一个整数13579
def fn(x, y) :
	return x * 10 + y

integer = reduce(fn, list(x for x in range(10) if x%2 == 1))
print(integer)

def char2num(s) :
	return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]

strtoint = reduce(fn, map(char2num, '13579'))
print(strtoint)	

# def str2int(s) ：
#   def fn(x, y) :
#   	  return x * 10 + y
#   def char2num(s) :
#   	  return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}[s]
#   return reduce(fn, map(char2num, s))

'''
  def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

  def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
'''

"""
利用map()函数,把用户输入的不规范的英文名字,
变为首字母大写,其他小写的规范名字。
输入:['adam', 'LISA', 'barT']
输出:['Adam', 'Lisa', 'Bart']
"""
def normalize(name) :
	return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

"""
Python提供的sum()函数可以接受一个list并求和,
请编写prod()函数,可以接受一个list并利用reduce()求积:
"""
def prod(L) :
  from operator import mul
  return reduce(mul, L)

print('3 * 5 * 7 * 9 = ', prod([3, 5, 7, 9]))
>>>>>>> origin/master
