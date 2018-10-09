# -*- coding:utf-8 -*-

"""
数据类型
1.字符串(string)
2.数字(Number)
3.列表(list)
"""

# 1.字符串(string)
string1 = 'Python web Scrappy'
string2 = "by Santos"
string3 = string1 + " " + string2
print(string3)

# 2.数字(Number)
int1 = 7
float1 = 7.5
trans_int = int(float1)
print(trans_int)

# 3.列表(list)
list1 = ['Python', 'Web', 'Scrappy']
list2 = [1, 2, 3, 4, 5, 6]
list3 = ["a", 2, "c", 4]
print("list1+list2+list3:", (list1 + list2 + list3))
# 访问列表中的值，可以在方括号中标明相应的位置索引进行访问，索引从0开始
print("list1[0] : ", list1[0])
print("list2[1:3] : ", list2[1:3])
# 修改列表中的值
list1[1] = 'New'
print("list1", list1)
list1.append('Chris')
print('list1', list1)

# 4.字典(Dictionaries)

'''
字典是一种可变容器模型，key-value
每个存储的值都对应着一个键值key,key必须唯一，但是值可以不唯一，值可以取任何数据类型
'''
namebook = {
    "Name": "Alex",
    "Age" : 7,
    "Class" : "First"
}
# 可以把响应的键值放入方括号，提取值
print(namebook["Name"])
print(namebook)

# 循环提取整个dictionary的key和value
for key,value in namebook.items():
    print(key, value)
for key in namebook.keys():
    print(key, namebook[key])

# 条件语句和循环语句
# 定义字符串book
book = "python"
# 条件成立时输出
if book == "python":
    print("You are studying python.")
elif book == "jave":
    print("You ara studying java.")
else:
    # 条件不成立时输出
    print("Wrong.")

# for循环能在一个给定的顺序下重复执行
citylist = ["Beijing", "Shanghai", "Guangzhou", "Shenzhen"]
for eachcity in citylist:
    print(eachcity)
# while循环能不断重复执行,只要能满足一定条件
count = 0
while count < 3:
    # 打印出0，1，2
    print(count)
    # count = count + 1
    count += 1
