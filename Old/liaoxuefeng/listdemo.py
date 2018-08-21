# -*- coding:utf-8 -*-

classmates = ['Michael','Bob','Tracy']
print(classmates)

print(len(classmates))

# 往list中追加元素到末尾
classmates.append('Adam')
print(classmates)

# 元素插入到指定的位置,比如索引号为1的位置
classmates.insert(1,'Jack')
print(classmates)

# 删除list末尾的元素,用pop()方法:
print(classmates.pop())
print(classmates)

# 删除指定位置的元素,用pop(i)方法,其中i是索引位置
