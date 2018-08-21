#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s1 = set([1, 1, 2, 2, 3, 3])
print(s1) # [1,2,3]
s2 = set([2, 3, 4])
print(s1 & s2)  # [2,3] s1与s2的并集
print(s1 | s2) # [1,2,3,4] s1与s2的交集

# set可以看成数学意义上的无序和无重复元素的集合,add(key)方法可以添加元素到set中,可以重复添加,但不会有效果,remove(key)可以删除元素

# dict如果key不存在,dict就会报错,要避免key不存在的错误,有两种方法,
# 一是通过in判断Key是否存在 'Thomas' in dict
# 二是通过dict提高的get方法,如果key不存在,可以返回None,或者自己指定的value: d.get('Thomas', -1)

