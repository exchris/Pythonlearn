# Set(集合)
# 集合(set)是一个无序不重复元素的序列
# 基本功能是进行关系测试和删除重复元素
# 可以使用大括号{}或者set()函数创建集合,
# 注意
# 创建一个空集合必须用set()而不是{},因为{}是用来创建一个空字典

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}

print(student) # 输出集合,重复的元素会被自动去掉

# 成员测试
if ('Rose' in student) :
    print('Rose在集合中')
else :
    print('Rose不在集合中')

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)
# result = {'a', 'b', 'd', 'c', 'r'}

print(a - b) # a和b的差集
# result = {'b', 'd', 'r'}

print(a | b) # a和b的并集
# result = {'a', 'b', 'l', 'd', 'c', 'r', 'z', 'm'}

print(a & b) # a和b的交集
# result = {'c', 'a'}

print(a ^ b) # a和b中不同时存在的元素
# result = {'l','b','d','r','z','m'}