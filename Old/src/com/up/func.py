# -*- coding:UTF-8 -*-
from _functools import reduce
def f():
    print('call f()...')
    # 定义函数g:
    def g():
        print('call g()...')
    # 返回函数g:
    return g

x = f() # 调用f()
# call f()...

x # 变量x是f()返回的函数:
# <function g at 0x1337bf320>

x() # x指向函数,因此可以调用
# call g()... x 调用x()就是指向g()函数定义的代码
from functools import reduce
def calc_prod(lst):
    '''
    def f():
        return reduce(lambda x, y : x*y, lst)
    return f
    '''
    '''
    def prod(x1, x2):
        return x1 * x2
    def f():
        return reduce(prod, lst)
    return f
    '''
    def f():
        def prod(x, y):
            return x*y
        return reduce(prod, lst)
    return f        

f = calc_prod([1, 2, 3, 4])
print(f())