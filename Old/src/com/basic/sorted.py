
# -*- coding:utf-8 -*-

'''
排序算法
内置的sorted()函数就可以对list进行排序
sorted()函数也是一个高级函数,它还可以接受一个key函数来实现自定义的排序,例如按绝对值大小排序
'''
L = sorted([36, 5, -12, 9, -21])
# 结果: [-21,-12,5,9,36]

lAbs = sorted([36, 5, -12, 9, -21], key=abs)
print(lAbs) # 结果: [5,9,-12,-21, 36]

# 默认情况下,对字符串排序,是按照ASCII的大小比较的,结果,大写字母Z会排在小写字母a的前面
sorted(['bob','about','Zoo','Credit'])
# 结果: ['Credit', 'Zoo', 'about', 'bob']

#我们给sorted传入key函数,即可实现忽略大小写的排序:
sorted(['bob','about','Zoo','Credit'], key=str.lower)
# 结果:['about','bob','Credit','Zoo']

# 进行反向排序,不必改动key函数,可以传入第三个参数reverse=True:
sorted(['bob','about','Zoo','Credit'], key=str.lower, reverse=True)
# 结果:['Zoo','Credit','bob','about']

L = [('Bob', 75),('Adam', 92),('Bart', 66),('Lisa', 88)]
# 按名字排序
def by_name(t) :
    # for key in t :
    #     return str.lower(key)
    return t[0]

# 成绩排序
def by_score(t) :
    return t[1]


L2 = sorted(L, key=by_score, reverse=True)
print(L2)