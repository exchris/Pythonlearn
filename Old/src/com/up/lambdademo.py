# -*- coding:UTF-8 -*-
# 关键字lambda表示匿名函数,冒号前面的x表示函数参数
from filecmp import cmp
lst1 = list(map(lambda x:x**2,list(range(1,10))))
print(lst1)

myabs = lambda x:-x if x < 0 else x
print(myabs(-1))

isNotEmpty = list(filter(lambda s:s and len(s.strip())>0,
['test',None,'','str',' ','END']))
print(isNotEmpty)
