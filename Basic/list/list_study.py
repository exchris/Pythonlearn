#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Python内置的一种数据类型是列表:list
list是一种有序的集合，可以随时添加和删除其中的元素
比如:列表班里所有同学的名字，就可以用一个list表示
'''
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)

# 用len()函数可以获得list元素的个数
print(len(classmates))

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的
print("first element:%s" %classmates[0])
print("two element:%s" %classmates[1])
print("three element:%s" %classmates[2])
'''
print("four element:%s" %classmates[3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
'''

# 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素
print(classmates[-1])

# list是一个可变的有序列表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 也可以把元素插入到指定的位置，比如索引号为1的位置
classmates.insert(1, 'Jack')
print(classmates)

# 要删除list末尾的元素,用pop()方法
classmates.pop() # 'Adam'
print(classmates)

# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置
classmates.pop(1) # 'Jack'
print(classmates)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
classmates[1] = 'Sarah'
print(classmates)

# list里面的元素的数据类型也可以不同，比如
L = ['Apple', 123, True]
print("123's index is %d" %L.index(123))
# list元素也可以是另一个list
s = ['python', 'java', ['asp','php'], 'scheme']
print(len(s))

# 如果一个list中一个元素也没有，就是一个空的list,它的长度为0
L = []
print(len(L))


# 组合
s1 = [1,2,3]
s2 = [4,5,6]
print("s1 + s2:", s1 + s2)
# 重复
print(['Hi!']*4)
# 元素是否在列表中
print(3 in [1,2,3])
# 迭代
for x in [1,2,3]:print(x,end="\r\n")

# python列表函数&方法
print("max(list) is %d" %max([1,2,3]))
print("min(list) is %d" %min([1,2,3]))

# list.append(obj) 在列表末尾添加新的对象
list1 = ['Google','Runoob','Taobao']
list1.append('Baidu')
print("更新后的列表:",list1)
# list.count(obj) 统计某个元素在列表中出现的次数
aList = [123,'Google','Runoob','Taobao',123]
print("123元素个数:",aList.count(123))
print("Runoob元素个数:",aList.count('Runoob'))
# list.extend(seq) 在列表末尾一次性追加到另一个序列中的多个值(用新列表扩展原来的列表)
list1 = ['Goole','Runoob','Taobao']
list2 = list(range(5)) # 创建0-4的列表
list1.extend(list2) #扩展列表
print("扩展后的列表:", list1)
# list.index(obj) 从列表中找出某个值第一个匹配项的索引位置
list1 = ['Google', 'Runoob', 'Taobao', 'Taobao']
print ('Runoob 索引值为', list1.index('Runoob'))
print ('Taobao 索引值为', list1.index('Taobao'))
# list.insert(index,obj) 将对象插入列表
list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('列表插入元素后为 : ', list1)
# list.pop([index=-1]) 移除列表中的一个元素(默认最后一个元素)，并且返回该元素的值
list1 = ['Google', 'Runoob', 'Taobao']
list1.pop()
print ("列表现在为 : ", list1)
list1.pop(1)
print ("列表现在为 : ", list1)
# list.remove(obj) 移除列表中某个值得第一个匹配项
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("列表现在为 : ", list1)
list1.remove('Baidu')
print ("列表现在为 : ", list1)
# list.reverse() 反向列表中元素
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("列表反转后: ", list1)
# list.sort(cmp=Noe,key=None,reverse=False) 对原列表进行排序
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']

aList.sort()
print("List : ", aList)
# 列表
vowels = ['e', 'a', 'u', 'o', 'i']

# 降序
vowels.sort(reverse=True)

# 输出结果
print('降序输出:', vowels)


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print('排序列表：', random)
# list.clear() 清空列表
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print ("列表清空后 : ", list1)
# list.copy() 复制列表
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list2 列表: ", list2)