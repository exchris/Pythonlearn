# -*- coding:UTF-8 -*-
'''
题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
'''

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i!=k) and (i!=j) and (j!=k):
                print("%d,%d,%d"%(i,j,k))
print()           
            
# 用集合去除重复元素
import pprint

list_num = ['1','2','3','4']
list_result = []
for i in list_num:
    for j in list_num:
        for k in list_num:
            if len(set(i+j+k)) == 3:
                list_result += [int(i+j+k)]
print("能组成%d个互补相同且无重复数字的三位数:"%(len(list_result)))
pprint.pprint(list_result)

# 原答案没有指出三位数的数量,添加无重复三位数的数量
d = [] 
for a in range(1, 5):
    for b in range(1, 5):
        for c in range(1, 5):
            if (a!=b) and (a!=c) and(c!=b):
                d.append([a,b,c])
print("总数量:",len(d))
print()

from itertools import permutations
for i in permutations([1,2,3,4],3):
    k = ''
    for j in range(len(i)):
        k = k + str(i[j])
    print(int(k))

for i in permutations([1,2,3,4],3):
    print(i)