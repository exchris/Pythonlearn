# -*- coding:utf-8 -*-

# 输出一个随机数

__author__ = 'Exchris Tsai'

import random

print(random.random()) # 输出0-1之间的随机数

# 生成10到20之间的随机数
print(random.uniform(10, 20))

# 输出10-20之间的随机整数
print(random.randint(10, 20))