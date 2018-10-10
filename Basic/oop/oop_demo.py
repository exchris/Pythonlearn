# -*-coding:utf-8-*-
"""
面向对象编程
"""
# 创建类
class Person:
    # __init__()方法称为类的构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 通过self调用被封装的内容
    # def detail(self):
    #     print(self.name)
    #     print(self.age)

# 将"santos"和18分别封装到obj1及self的name和age属性
obj1 = Person('santos', 18)
# Python将obj1传给self参数，即:obj1.detail(obj1),此时内部self=obj1
# obj1.detail()

# 直接调用obj1对象的name属性
print(obj1.name)
# 直接调用obj1对象的age属性
print(obj1.age)
