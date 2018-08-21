# -*- coding:utf-8 -*-

"""
 有四个数字:1、2、3、4,能组成多少个互不相同且无重复数字的三位数?各是多少?
 程序分析:可填在百位、十位、各位的数字都是1、2、3、4.组成所有的排列后再去掉不满足的排列
"""

for i in range(1, 5) :
    for j in range(1, 5) :
        for k in range(1, 5) :
            if (i != k) and (i != j) and (j != k) :
                print(i*100+j*10+k)

print()

# 使用列表形式,并计算总结

# 原答案没有指出三位数的数量,添加无重复三位数的数量
d = []
for a in range(1, 5):
    for b in range(1, 5) :
        for c in range(1, 5) :
            if (a!=b) and (a!=c) and (c!=b) :
                d.append([a,b,c])

print("总数量:", len(d))
print(d)

print()

# 将for循环和if语句综合成一句,直接打印出结果
list_num = [1,2,3,4]

list = [i*100+j*10+k for i in list_num for j in list_num for k in list_num if (j!=i and k!=j and i!=j)]
print(list)
