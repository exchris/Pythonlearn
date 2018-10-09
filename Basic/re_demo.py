#!/usr/bin/python
# coding:utf-8

import re
str = '<div class="nam">中国</div>'
res = re.findall(r'<div class=".*">(.*?)</div>', str)
print(res)


lst = [1,2,3,4,5]
list1 = []
def fn(s):
    return s ** 2

for i in map(fn, lst):
    if i > 10:
        list1.append(i)

print(list1)


def removeDiffStr(string1):
    # 将string转为set类型
    s = set(string1)
    # 转换为列表类型
    s = list(s)
    s.sort()
    return "".join(s)

s = "ajldjlajfdljfddd"
res = removeDiffStr(s)
print(res)
