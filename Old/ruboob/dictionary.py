# 字典是Python中另一个非常有用的内置数据类型
# 列表是有序的对象集合,字典是无序的对象集合。两种之间的区别在于:
#
# 字典当中的元素时通过键来存取的,而不是通过偏移存取的
# 字典是一种映射类型,字典用"{}"标识,它是一个无序的键(key):值(value)对集合
# 键(key)必须使用不可变类型
# 在同一个字典中,键(key)必须是唯一的

dict = {}
dict['one'] = "1 - 菜鸟教程"
dict[2] = "2 - 菜鸟工具"

tinydict = {'name': 'runoob', 'code':1, 'site': 'www.runoob.com'}

print(dict['one']) # 输出键为"one"的值
# result = 1 - 菜鸟教程

print(dict[2]) # 输出键为2的值
# result = 2 - 菜鸟工具

print(tinydict) # 输出完整的字典
# result = {'name':'runoob', 'code':1, 'site':'www.runoob.com'}

print(tinydict.keys()) # 输出所有键
# result = dict_keys(['name','site','code'])

print(tinydict.values()) # 输出所有值
# result = dict_values(['runoob',1,'www.runoob.com'])