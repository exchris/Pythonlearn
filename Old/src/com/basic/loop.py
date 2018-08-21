# -*- coding:UTF-8 -*-
'''
Created on 2017年7月19日

@author: Administrator
'''
# for循环
L = [75, 92, 59, 68]
sum = 0.0
for score in L:
    sum = sum + score
print(sum / 4)

# while循环
sum1 = 0
x = 1
while x <= 100:
    sum1 = sum1 + x
    x = x + 2
print(sum1)

# 计算 1 + 2 + 4 + 8 + 16 + ... 的前20项的和。
sum2 = 0
x2 = 1
n2 = 1
while True:
    sum2 = sum2 + x2
    x2 = pow(2, n2)
    n2 = n2 + 1
    if n2 > 20:
        break
print(sum2)

# 计算0-100的奇数和
sum3 = 0
x3 = 0
while True:
    x3 = x3 + 1
    if x3 > 100:
        break
    
    if(x3%2==0):
        continue
    sum3=sum3+x3
    
print(sum3)

for x in range(1,10):
    for y in range(x+1,10):
        print(10*x+y)
        
