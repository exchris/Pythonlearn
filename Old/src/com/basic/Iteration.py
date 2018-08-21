# -*- coding:UTF-8 -*-
'''
如果给的一个list或tuple，我们可以通过for循环来遍历这个list或tuple,
这种遍历我们称为迭代(Iteration)

集合是指包含一组元素的数据结构,
1.有序集合:list,tuple,str和unicode
2.无序集合:set
3.无序集合且具有key-value对:dict

迭代永远是取出元素本身,而非元素的索引
'''

# 输出1-100的7的倍数
for i in range(1,101):
	if (i%7)==0:
		print(i)

# 对于有序集合,元素确实是有索引的。我们确实想在for循环中拿到索引
# 方法是enumerate()函数:
L = ['Adam','Lisa','Bart','Paul']
for index,name in enumerate(L):
	print(index,'-',name)

list1 = zip([10,20,30],['A','B','C'])
print(list(list1))
# print list1 python2

# 在迭代['Adam','Lisa','Bart','Paul']时,如果我们想打印名次-名字(名次从1开始)
list2 = list(zip([x for x in range(0,4)],L))
for index,name in list2[1:]:
	print(index,'-',name)

d = {'Adam':95,'Lisa':85,'Bart':59,'Paul':74}
sum = 0.0
for v in d.values():
	sum = sum + v

print(sum/len(d))

sum1 = 0.0
for k, v in d.items():
	sum1 = sum1 + v
	print(k,':',v)
print('average',':',sum1/len(d))
