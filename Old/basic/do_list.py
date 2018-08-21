# Python内置的一种数据类型是列表:list.list是一种有序的集合,可以随时添加和删除其中的元素

# 列出班里所有同学的名字,就可以用一个list表示:
classmates = ['Michael', 'Bob', 'Tracy']
print(classmates) # ['Michael','Bob','Tracy']

# 变量classmates就是一个list.用len()函数可以获得list元素的个数
print(len(classmates)) # 3

# 用索引来访问list中每一个位置的元素,记得索引是从0开始的:
classmates[0] # 'Michael'
classmates[1] # 'Bob'
classmates[2] # 'Tracy'
# classmates[3] python会报一个IndexError错误,所以,要确保索引不要越界

# list是一个可变的有序表,所以,可以往list中追加元素到末尾
classmates.append('Adam')
classmates # ['Michael','Bob','Tracy','Adam']

# 也可以把元素插入到指定的位置,比如索引号为1的位置:
classmates.insert(1, 'Jack')
classmates # ['Michael','Jack','Bob','Tracy','Adam']

# 要删除list末尾的元素,用pop()方法
classmates.pop() # 'Adam'
classmates # ['Michael','Jack','Bob','Tracy']

# 要删除指定位置的元素,用pop(i)方法,其中i是索引位置
classmates.pop(1) # 'Jack'
classmates # ['Michael', 'Bob', 'Tracy']

# 要把某个元素替换成别的元素,可以直接赋值给对应的索引位置:
classmates[1] = 'Sarah'
classmates # ['Michael','Sarah', 'Tracy']

# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
classmates.pop()
print('classmates =', classmates)

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0]) # Apple
print(L[1][1]) # Python
print(L[2][2]) # Lisa
