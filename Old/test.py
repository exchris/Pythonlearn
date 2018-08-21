# -*- coding:utf-8 -*-
# author: exchris
# description: 今日头条文章python面试必考题(未知)

# 下面这段代码的输出结果是什么

def extendList(val, lst=[]):
    lst.append(val)
    return lst

list1 = extendList(10)
list2 = extendList(123,[])
list3 = extendList('a')

"""
print("list1 = %s" % list1)
print("list2 = %s" % list2)
print("list3 = %s" % list3)

输出结果:
list1 = [10,'a']
list2 = [123]
list3 = [10, 'a']
"""

