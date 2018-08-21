str = "Runoob"

print(str) # 输出字符串
# result = Runoob

print(str[0:-1]) # 输出第一个到倒数第二个的所有字符
# result = Runoo

print(str[0]) # 输出字符串第一个字符
# result = R

print(str[2:5]) # 输出从第三个开始到第5个的字符(不包括第5个字符)
# result = noo

print(str[2:]) # 输出从第三个开始的后的所有字符
# result = noob

print(str * 2) # 输出字符串两次
# result = RunoobRunoob

print(str + "TEST") # 连接字符串
# result = RunoobTEST

# Python使用反斜杠(\)转义特殊字符,如果你不想反斜杠发送转义,
# 可以在字符串前面添加一个r, 标识原始字符串
print ('Ru\noob')
# result
# Ru
# oob

print(r'Ru\noob')
# result = Ru\noob