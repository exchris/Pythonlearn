# 与Python字符串不一样的是,列表中的元素是可以改变的

list = ['abcd', 786, 2.23, 'runoob', 70.2]
tinylist = [123, 'runoob']

print(list) # 输出完整列表
# result = ['abcd', 786, 2.23, 'runoob', 70.2]

print(list[0]) # 输出列表第一个元素
# result = abcd

print(list[1:3]) # 从第二个开始输出到第三个元素
# result = [786, 2.23]

print(list[2:]) # 输出从第三个元素开始的所有元素
# result = [2.23, 'runoob', 70.2]

print(tinylist * 2) # 输出两次列表
# result = [123, 'runoob', 123, 'runoob']

print(list + tinylist) # 连接列表
# result = ['abcd', 786, 2.23, 'runoob', 70.2, 123, 'ruboob']

a = [1, 2, 3, 4, 5, 6]
a[0] = 9
a[2:5] = [13, 14, 15]
print(a);
# result = [9, 2, 13, 14, 15, 6]

a[2:5] = [] # 删除从第3个元素到第5个元素
print(a);
# result = [9,2, 6]