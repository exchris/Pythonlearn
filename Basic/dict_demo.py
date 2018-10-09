#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键
值（key-value）
存储，具
有极快的查找速度。
"""
d = {
    'Michael':95,
    'Bob':75,
    'Tracy':85
}
print(d['Michael'])
d['Adam'] = 67
print(d)

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 88
print(d['Jack'])

# 如果key不存在，dict就会报错，要避免key不存在的错误，有两种方法,
# 一是通过in判断key是否存在:
print('Thomas' in d)
# 二是通过dict提供的get方法,如果key不存在,可以返回None,或者自定义的value
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 要删除一个key,用pop(key)方法,对应的value也会从dict中删除
print(d.pop('Bob'))
print(d)

"""
dict内部存放的顺序和key放入的顺序是没有关系的。
和list比较，dict有以下几个特点：
1. 查找和插入的速度极快，不会随着key的增加而增加；
2. 需要占用大量的内存，内存浪费多。
而list相反：
1. 查找和插入的时间随着元素的增加而增加；
2. 占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。
dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条
就是dict的key必须是不可变对象。
"""