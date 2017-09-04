# coding=utf-8

from collections import Iterable

from types import MethodType

# 面向对象的高级编程

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，这就是动态语言的灵活性。先定义class：
class Student(object):
    pass
# 然后，尝试给实例绑定一个属性：
s = Student()
s.name = 'Michael'  # 动态给实例绑定一个属性
print s.name
# 还可以尝试给实例绑定一个方法：
def set_age(self, age):
    self.age = age

s.set_age = MethodType(set_age, s, Student)  # 给实例动态绑定一个方法
s.set_age(25)  # 调用实例方法
print s.age
# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student()
# s2.set_age(25)
# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score
Student.set_score = MethodType(set_score, None, Student)

####################################################
# 使用__slots__
# 为了达到限制class的属性的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性的名称
# 然后，我们试试：
s = Student()
s.name = 'Michael'
s.age = 25
# s.score = 99  # 报错
# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 9999
# 除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。

########################################################
# 使用@property
# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：
# 这样一来，既能检查参数，又可以用类似属性这样简单的方式来访问类的变量
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0~100!')
        self._score = value

s = Student()
s.score = 60  # 实际转化为s.set_score(60)
print s.score  # 实际转化为s.get_score()

#######################################################
# 多重继承
class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

class Dog(Mammal, Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

#################################################
# 定制类：类似__xxx__的变量或者函数是有特殊用途的。
# __slots__：限制类的属性
# __len__()：能让class作用于len()函数
# __str__：类似于java中object.toString()方法
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
print Student('Michael')
# __iter__：生成迭代对象。如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a,b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:  # 推出循环的条件
            raise StopIteration
        return self.a  # 返回下一个值
for n in Fib():
    print n
print isinstance(Fib(), Iterable)
# __getitem__：可以使类的对象按下标取值(这个下标可以是任何基本数据类型，只是需要自己判断)
# 还可以添加切片的功能
class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return n
f = Fib()
print f[0]
print f[1]
print f[2]
print f[3]
# __getattr__：只有当调用类的属性不存在时，才会调用这个函数。
# __getattr__默认返回的是None。
class Student(object):
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99
s = Student()
print s.name
print s.score
# __call__：实现类似instance()，在实例本身上调用。
class Student(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print 'My name is %s.' % self.name
s = Student('Michael')
s()
# 判断一个对象是否可以被调用，能被调用的对象就是一个Callable对象。
print callable(s)
print callable(max)
print callable([1, 2, 3])
print callable(None)
print callable('String')

#######################################################
# 使用元类

# type()
# 动态语言和静态语言最大的不同，就是函数和类的定义，不是编译时定义的，而是运行时动态创建的。
class Hello(object):
    def hello(self, name='world'):
        print 'Hello, %s.' % name
h = Hello()
h.hello()
print type(Hello)
print type(h)
# 由上，可以看出：type()函数可以查看一个类型或变量的类型，Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello。
# 我们说class的定义是运行时动态创建的，而创建class的方法就是使用type()函数。
# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义：
# 要创建一个class对象，type()函数依次传入3个参数：
# 1.class的名称；
# 2.继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3.class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
# 通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()函数创建出class。
# 正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上都是动态编译，会非常复杂。
def fn(self, name='world'):  # 先定义函数
    print 'Hello, %s.' % name
Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()
print type(Hello)
print type(h)

# metaclass
# 元类：先定义metaclass，就可以创建类，最后创建实例。
# 我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
# 定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
# metaclass是创建类，所以必须从'type'类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(list):
    __metaclass__ = ListMetaclass  # 指示使用ListMetaclass来指定类
# 当我们写下__metaclass__ = ListMetaclass语句时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接收到的参数依次是：
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
# 测试一下MyList是否可以调用add()方法：
L = MyList()
L.add(1)
print L
