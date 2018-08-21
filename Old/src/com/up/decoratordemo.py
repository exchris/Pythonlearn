# -*- coding:UTF-8 -*-
'''
    def f1(x):
        return x*2
    def new_fn(f):
        def fn(x):
            print('call ' + f.__name__+'()')
            return f(x)
        return fn
    
    g1 = new_fn(f1)
    print(g1(5))
    
    f1 = new_fn(f1)
    print(f1(5))
    
    # Python内置的@语法就是为了简化装饰器调用
    @new_fn 
    def f2(x):
        return x*2
'''

'''
Python中编写无参数decorator
考查一个@log的定义:
def log(f):
    def fn(x):
        print('call ' + f.__name__ + '()...')
        return f(x)
    return fn

# 对于阶乘函数,@log工作得很好
@log
def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

print(factorial(10))

# 结果:
call factorial()...
3628800

 
'''
   
# 编写一个@performance,它可以打印出函数调用的时间
from functools import reduce
import time

def performance(f):
    def print_time(*args, **kw):
        print('call '+f.__name__+'() in '+time.strftime('%Y-%m-%d',time.localtime(time.time())))
        return f(*args, **kw)
    return print_time 

@performance
def factorial(n):
    return reduce(lambda x,y:x*y, range(1,n+1))

print(factorial(10))