# -*- coding:UTF-8 -*-
'''
Created on 2017年7月19日

@author: Administrator
'''
months = set(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
x1 = 'Feb'
x2 = 'Sun'

if x1 in months:
    print('x1: ok')
else:
    print('x1: error')

if x2 in months:
    print('x2: ok')
else:
    print('x2: error')
    
s1 = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for x in s1:
    print("%s:%d"%(x))
    
# set更新
s = set(['Adam', 'Lisa', 'Paul'])
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for key in L:
    if key in s:
        s.remove(key)
    else:
        s.add(key)
print(s)