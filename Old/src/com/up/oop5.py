# -*- coding:UTF-8 -*-
class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda: 'A'

p1 = Person('Bob', 80)
print p1.get_grade
print p1.get_grade()

class Person1(object):
    count = 0
    @classmethod
    def how_many(cls):
        return cls.count
    def __init__(self, name):
        self.name = name
        Person1.count = Person1.count + 1

print Person1.how_many()
p1 = Person1('Bob')
print Person1.how_many()

class Person2(object):

    __count = 0

    @classmethod
    def how_many(cls):
        return cls.__count
    def __init__(self,name):
        self.name = name
        Person2.__count = Person2.__count + 1

print Person2.how_many()

p1 = Person2('Bob')

print Person2.how_many()