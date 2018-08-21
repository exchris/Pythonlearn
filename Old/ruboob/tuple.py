# 元组(tuple)与列表类似,不同之处在于元祖的元素不能修改。元素写在小括号(())里,元素之间用逗号隔开。
# 元素中的元素类型也可以不相同

tuple = ('abcd', 786, 2.23, 'runoob', 70.2)
tinytuple = (123, 'runoob')

print(tuple) # 输出完整元组
# result = ('abcd', 786, 2.23, 'runoob', 70.2)

print(tuple[0]) # 输出元组的第一个元素
# result = abcd

print(tuple[1:3]) # 输出从第二个元素开始到第三个元素
# result = (786, 2.23)

print(tuple[2:]) # 输出从第三个元素开始的所有元素
# result = (2.23, 'runoob', 70.2)

print(tinytuple * 2) # 输出两次元组
# result = (123, 'runoob', 123, 'runoob')

print(tuple + tinytuple) #连接元组
# result = ('abcd', 78.6, 2.23, 'runoob', 70.2, 123, 'runoob')