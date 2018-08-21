# 对于单个字符的编码,
# python提供了ord()函数获取字符的整数
# chr()函数把编码转换为对于的字符
ord('A') # 65
ord('中') # 20013
chr(66) # 'B'
chr(25991) # '文'

# 如果知道字符的整数编码,还可以用十六进制这么写str:
'\uee2d\u6587' # '中文'

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
'ABC'.encode('ascii') # b'ABC'
'中文'.encode('utf-8') # b'\xe4\xb8\xad\xe6\x96\x87'

# 注意:纯英文的str可以用ASCII编码为bytes,内容是一样的,
# 含有中文的str可以用UTF-8编码为bytes。含有中文的str无法用ASCII编码
# 因为中文编码的范围超过了ASCII编码的范围,Python会报错

# 要把bytes变为str,就需要用decode()方法
b'ABC'.decode('ascii') # 'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8') # '中文'

# str包含多少个字符,可以用len()函数
len('ABC') # 3
len('中文') # 2
len(b'ABC') # 3
len(b'\xe4\xb8\xad\xe6\x96\x87') # 6
len('中文'.encode('utf-8')) # 6

# 格式化
print('小明的成绩提高了：%2.1f%%' % ((85-72)/72*100))
# 小明的成绩提高了:18.1%
