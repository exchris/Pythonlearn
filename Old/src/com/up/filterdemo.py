# -*- coding:UTF-8 -*-
'''
filter()函数接收一个函数f和一个list,这个函数f的作用
是对每个元素进行判断,返回True或False,
filter()根据判断结果自动过滤掉不符合条件的元素,
返回有符合条件元素组成的新list
'''

'''
要从一个list[1,4,6,7,9,12,17]中删除偶数,保留奇数
'''
import math

def is_odd(x):
    return x%2 == 1

#[1,7,9,17]
print(list(filter(is_odd, [1,4,6,7,9,12,17])))

# 利用filter(),删除None或者空字符串
def is_not_empty(s):
    return s and len(s.strip()) > 0

print(is_not_empty('None'))
print(list(filter(is_not_empty, ['test','None','','str','','END'])))


def is_sqr(x):
    # v = math.sqrt(x)
    # return int(v) == v
    return math.sqrt(x)%1 == 0

print(list(filter(is_sqr,list(range(1,101)))))


