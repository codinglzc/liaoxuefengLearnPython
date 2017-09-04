# coding=utf-8

import types

# 面向对象
# 定义类是通过class关键字
# class后面紧接着是类名，及Student，类名通常是大写开头的单词
# 紧接着是(object)，表示该类是从哪个类继承下来的。
# 所有类最终都会继承object
# __init__方法可以理解成类的构造函数，该方法的第一个参数永远是self，表示创建的实例本身。
# 有了__init__方法，在创建实例的时候，就不能传入空的参数量，必须传入与__init__方法匹配的参数，但self不需要传。
# 和普通函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且调用时，不用传递该参数。
class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s: %s' % (self.name, self.score)

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()
print bart.get_grade()
print bart

#########################################################
# 访问限制
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__。
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量，只有内部可以访问，外部不能访问：
# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__,__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

bart = Student('Bart Simpson', 98)
# 强烈建议不要这么干
# print bart._Student__name

##################################################################
# 继承和多态

class Animal(object):

    def run(self):
        print 'Animal is running...'

class Dog(Animal):

    def run(self):
        print 'Dog is running...'

    def eat(self):
        print 'Eating meat...'

class Cat(Animal):

    def run(self):
        print 'Cat is running...'

    def eat(self):
        print 'Eating fishes...'

dog = Dog()
dog.run()
cat = Cat()
cat.run()
print isinstance(dog, Dog)

####################################################
# 获取对象信息
# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型，有哪些方法呢？
# 使用type()
print type(123)
print type(1.23)
print type('str')
print type(u'str')
print type(None)
print type(abs)
print type([])
print type(())
print type({})

print type(123) == type(456)
print type('abc') == type('123')
print type('abc') == type(123)

print type('abc') == types.StringType
print type(u'abc') == types.UnicodeType
print type([]) == types.ListType
# 有一种类型就叫TypeType，所有类型本身的类型就是TypeType.
print type(str) == types.TypeType
print type(int) == type(str) == types.TypeType
# 但最好使用isinstance()函数来判断类型

# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list：
print dir('ABC')
print dir(dog)
# 仅仅把属性和方法列出来是不够的，配合getattr(),setattr()以及hasattr()，我们可以直接操作一个对象的状态：
class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x
obj = MyObject()
print hasattr(obj, 'x')
print obj.x
print hasattr(obj, 'y')
setattr(obj, 'y', 19)
print hasattr(obj, 'y')
print getattr(obj, 'y')
print obj.y
print hasattr(obj, 'power')

# 小结：
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
sum = obj.x + obj.y
# 就不要写
sum = getattr(obj, 'x') + getattr(obj, 'y')
