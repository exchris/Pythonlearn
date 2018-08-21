# -*- coding:utf-8 -*-

division = 17 / 3;
# 除法(/)永远返回一个浮点数。
print("除数值为:%f" %division);
divisor = 17 // 3;
print("除数值为:%d" %divisor);
remainder = 17 % 3;
print("余数值为:%d" %remainder);
# 幂乘方

# 5 squared
print("幂乘方为:%d" %(5 ** 2));

# 2 to the power of 7
print("幂乘方为:%d" %(2 ** 7));

# string

# 3 times 'un',followed by 'ium'
# * 重复只用于字符串文本
repeat =  3 * 'un' + 'ium'
print("string:%s" %repeat);

text = ('Put several strings within parentheses '
        'to have them joined together.')
print("text:%s" %text);

# 字符串检索截取
word = 'Python'
# character in position 0
print("first character:%c" %(word[0]));
# second-last character
print("second-last character:%c" %(word[-2]));
# 字符串切片
# characters from position 0 (included) to 2 (excluded)
print("characters from position 0 included to 2 excluded:%s" %(word[0:2]));
# characters from position 2 (included) to 5 (excluded)
print("characters from position 2 included to 5 excluded:%s" %(word[2:5]));
# s[:i] + s[i:] 用于等于 s
print("word[:i] + word[i:]:%s" %word);

# list 列表 写作中括号之间的一列逗号分隔的值。列表的元素不必是同一类型
squares = [1, 4, 9, 16, 25]
print(squares)
# 索引和切片
print("indexing returns the item:%d" %(squares[0]));
print("slicing returns a new list:", squares[3:]);
# 列表连接操作
print("list join", squares +[36, 49, 64, 81, 100])
# 列表可变,允许修改元素
# something's  wrong here
cubes = [1, 8, 27, 65, 125];
cubes[3] = 4 ** 3;
print("cubes",cubes);

# 在列表的末尾添加新的元素
cubes.append(215) # add the cube of 6
cubes.append(7 ** 3)
print("cubes append:", cubes);

# 对切片赋值,改变列表的尺寸
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E']
print("new letters:",letters);
# now remove them
letters[2:5] = []
print("remove letters:", letters);

# 斐波那契子序列
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

# **的优先级高于-,所以
print(-3**2)
# -9
print((-3)**2)
# 9