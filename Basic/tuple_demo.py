#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
另一种有序列表叫元组:tuple。
tuple和list非常相似，但是tuple一旦初始化就不能修改
比如同样是列表同学的名字：
"""
classmates = ('Michael', 'Bob', 'Tracy')

# 因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple
# tuple的陷阱：当您定义一个tuple时，在定义的时候，tuple的元素就必须被确定下来
t = (1, 2)
print(t)
# 定义一个空的tuple，可以写成():
t = ()
print(t)
# 要定义一个只有1个元素的tuple，如果您这么定义
t = (1)
print(t)
# 定义的不是tuple，是1 这个数！这是因为括号() 既可以表示tuple，又可以表示数学公式中的小括号，这就产生了
# 歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1 。

# 所以，只有1个元素的tuple定义时必须加一个逗号','，来消除歧义
t = (1, )
print(t)

# 最后来看一个"可变的"tuple
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)