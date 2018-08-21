# -*- coding:UTF-8 -*-
import time; # 引入time模块

# 获取时间戳
ticks = time.time()
print(ticks)

# 获取本地时间
localtime = time.localtime(time.time())
print(localtime)

# 获取格式化的时间
formatlocaltime = time.asctime(time.localtime(time.time()))
print(formatlocaltime)

# 格式化成2016-03-20 11:45:49形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:23:24 2016形式
print(time.strftime("%a %b %d %H:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print(time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))