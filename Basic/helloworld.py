# -*- coding:utf-8 -*-

# hello world
print('hello world !')

# if
the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")

# introduction

# Number
print(2 + 2)
print(50 - 5 * 6)
print((50 - 5 * 6) / 4)
# division always returns a floating point number
print(8 / 5)
# classic division returns a float
print(17 / 3)
# floor division discards the fractional part
print(17 // 3)
# the % operator returns the remainder of the division
print(17 % 3)
# result * divisor + remainder
print(5 * 3 + 2)
# 5 squared
print(5 ** 2)
# 2 to the power of 7
print(2 ** 7)

tax = 12.5 / 100
price = 100.50
print('price * tax : ', price * tax)

print('完整格式输出九九乘法表')
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %2d" % (i, j, i*j), end=" ")
    print("\t")
