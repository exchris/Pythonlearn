# -*- coding:UTF-8 -*-
'''
Created on 2017年7月19日

@author: Administrator
'''
L = ['Adam', 'Lisa', 'Bart']
# list添加新元素
# append()总是把新的元素添加到list的尾部
L.append('Paul') 
print(L)

# L.insert(2,'Zet')的意思是,'Zet'将被添加到索引2的位置上,
# 而原来索引为2的Bart同学,以及后面的所有同学,都自动向后移动一位
L.insert(2, 'Zet')
print(L)

# list删除元素
L = ['Adam','Lisa','Bart','Paul']
L.pop() # 'Paul'
print(L)  # ['Adam','Lisa','Bart']
L.pop(2) # 'Bart'

# 替换元素
L = ['Adam', 'Lisa', 'Bart']
L[0] = 'Bart'
L[-1] = 'Adam'
print(L)


list = [1,2,3];
print(list[1:]);