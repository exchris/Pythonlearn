a = 21
b = 10
c = 0

c = a + b
print("1 - c 的值为：", c)

c = a - b
print("2 - c 的值为：", c)

c = a * b
print("3 - c 的值为：", c)

c = a / b
print("4 - c 的值为：", c)

c = a % b
print("5 - c 的值为：", c)

# 修改变量 a 、b 、c
a = 2
b = 3
c = a ** b
print("6 - c 的值为：", c)

a = 10
b = 5
c = a // b
print("7 - c 的值为：", c)

if (a == b):
    print("1 - a 等于 b")
else:
    print("1 - a 不等于 b")

if (a != b):
    print("2 - a 不等于 b")
else:
    print("2 - a 等于 b")

if (a < b):
    print("3 - a 小于 b")
else:
    print("3 - a 大于等于 b")

if (a > b):
    print("4 - a 大于 b")
else:
    print("4 - a 小于等于 b")

# 修改变量 a 和 b 的值
a = 5;
b = 20;
if (a <= b):
    print("5 - a 小于等于 b")
else:
    print("5 - a 大于  b")

if (b >= a):
    print("6 - b 大于等于 a")
else:
    print("6 - b 小于 a")

c = a + b
print("1 - c 的值为：", c)

c += a
print("2 - c 的值为：", c)

c *= a
print("3 - c 的值为：", c)

c /= a
print("4 - c 的值为：", c)

c = 2
c %= a
print("5 - c 的值为：", c)

c **= a
print("6 - c 的值为：", c)

c //= a
print("7 - c 的值为：", c)

a1 = 60  # 60 = 0011 1100
b1 = 13  # 13 = 0000 1101
c1 = 0

c1 = a1 & b1;  # 12 = 0000 1100
print("1 - c1 的值为：", c1)

c1 = a1 | b1;  # 61 = 0011 1101
print("2 - c1 的值为：", c1)

c1 = a ^ b;  # 49 = 0011 0001
print("3 - c1 的值为：", c1)

c1 = ~a1;  # -61 = 1100 0011
print("4 - c1 的值为：", c1)

c1 = a1 << 2;  # 240 = 1111 0000
print("5 - c1 的值为：", c1)

c1 = a1 >> 2;  # 15 = 0000 1111
print("6 - c1 的值为：", c1)