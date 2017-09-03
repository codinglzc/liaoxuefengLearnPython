# coding=utf-8
import math

# python中内置了很多函数，我们可以直接调用

# 求绝对值
print abs(100)
print abs(-20)
print abs(12.34)

# 比较函数cmp(x, y)，如果x<y，返回-1，如果x=y，返回0，如果x>y，返回1
print cmp(1, 2)
print cmp(1, 1)
print cmp(2, 1)

# 数据类型转换
print int('123')
print int(12.34)
print float('12.34')
print str(1.23)
print bool(1)
print bool(0)
print bool(-1)
print bool('')
print bool(' ')


# 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个别名
a = abs
print a(-1)


# 定义函数
def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

# 注意：
# 函数中如果没有return语句，函数执行完毕后也会返回结果，只是结果为None。
# return None 可以简写为 return


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用 pass 语句
def nop():
    pass
nop()


# 函数可以自动检查参数个数不对的错误，但无法检查参数类型不对的错误。
# 所以，我们定义函数的时候，需要手动检查参数类型
# 数据类型检查可以用内置函数 isinstance 实现：
def my_new_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x
# print my_new_abs("A")


# 返回多个值，实际上返回的就是一个tuple对象
def move(x, y, step, angle = 0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny
x, y = move(100, 100, 60, math.pi/6)
print x, y
print move(100, 100, 60, math.pi/6)


# 小结：

# 定义函数时，需要确定函数名和参数个数；

# 如果有必要，可以先对参数的数据类型做检查；

# 函数体内部可以用return随时返回函数结果；

# 函数执行完毕也没有return语句时，自动return None。

# 函数可以同时返回多个值，但其实就是一个tuple。


# 函数的参数

# 默认参数
# 默认参数可以简化函数的调用
# 注意：必选参数在前，默认参数在后
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print power(5, 2)
print power(5, 3)
print power(2)

def enroll(name, gender, age=6, city='Beijing'):
    print 'name', name
    print 'gender', gender
    print 'age', age
    print 'city', city
enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

# 可变参数，参数前面加 * 号
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print calc(1, 2)
print calc()
nums = [1, 2, 3]
print calc(*nums)

# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
kw = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=kw['city'], job=kw['job'])
person('Jack', 24, **kw)

# 混合组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，或者只用其中某些，但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 'a', 'b')
func(1, 2, 3, 'a', 'b', x=99)
args = (1, 2, 3, 4)
kw = {'x': 99}
func(*args, **kw)

# 小结：
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

# 默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！

# 要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；

# **kw是关键字参数，kw接收的是一个dict。

# 以及调用函数时如何传入可变参数和关键字参数的语法：

# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。


# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)
print fact(1)
print fact(5)
print fact(100)
# print fact(1000) 函数栈会溢出
# 解决方法是采用尾递归。
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。
# def fact_new(n):
#     return fact_iter(n, 1)
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
# fact_new(1000)
# 遗憾的是，大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化，所以，即使把上面的fact(n)函数改成尾递归方式，也会导致栈溢出。

