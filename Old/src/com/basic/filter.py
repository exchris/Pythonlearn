
# -*- coding:utf-8 -*-

'''
和map()类似,filter()也接收一个函数和一个序列。
和map()不同的是,filter()把传入的函数依次作用于每个元素,然后根据返回值是True还是False决定保留还是丢弃该元素
例如:在一个list中,删掉偶数,只保留奇数,可以这么写
'''
def is_odd(n) :
    return n % 2 == 1

odd = list(filter(is_odd, [1,2,4,5,6,9,10,15]))
print(odd) # 打印奇数

# 把一个序列中的空字符串删掉,可以这么写:
def not_empty(s) :
    return s and s.strip()

notEmpty = list(filter(not_empty, ['A','','B',None,'C','']))
print(notEmpty) # 结果: ['A','B','C']

# 注意到filter()函数返回的是一个Iterator,也就是一个惰性序列,所有要强迫filter()完成计算结果,需要用list()函数获得所有结果并返回list.

'''
用filter求素数
计算素数的一个方法是埃氏2筛法
'''
# 构造一个从3开始的奇数序列
def _odd_iter() :
    n = 1
    while True :
        n = n + 2
        yield n

# 定义一个筛选函数
def _not_divisible(n) :
    return lambda x : x % n > 0

# 最后定义一个生成器,不断返回下一个素数:
def primes() :
    yield 2
    it = _odd_iter() # 初始序列
    while True :
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

# 由于primes()也是一个无限序列,所以调用时需要设置一个退出循环的条件:
# 打印100以内的素数:

for n in primes() :
    if n < 100:
        print(n)
    else :
        break


# 回数是指从左向右读和从右向左读都是一样的数,例如12321,909.请利用filter()滤掉非回数
def is_palindrome(n) :
    return str(n) == str(n)[::-1]

output = filter(is_palindrome, range(11, 100))
print(list(output)) # 结果:[11,22,33,44,55,66,77,88,99]