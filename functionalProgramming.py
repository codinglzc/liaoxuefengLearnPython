# coding=utf-8
import functools
# 函数式编程，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

# 高阶函数

# 变量可以指向函数
print abs
f = abs
print f
print f(-10)

# 函数名也是变量

# 传入函数
def add(x, y, f):
    return f(x) + f(y)
print add(-5, 6, abs)

##############################################
# map/reduce
# python内建了map()和reduce()函数

# map:map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。
def f(x):
    return x * x
print map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])

print map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])

# reduce:reduce()把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# 对一个序列球和
def add(x, y):
    return x + y
print reduce(add, [1, 3, 5, 7, 9])
# 把序列[1,3,5,7,9]变换成整数13579
def fn(x, y):
    return x * 10 + y;
print reduce(fn, [1, 3, 5, 7, 9])
# 配合map()函数
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
print str2int('123456')

################################################
# 函数作为返回值
# 该函数为求和的例子，返回的是求和的函数，而不是已经求和的值。
# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum
f = lazy_sum(1, 3, 5, 7, 9)
print f
print f()
print lazy_sum(1, 3, 5, 7, 9)()

# 闭包
# 注意到返回的函数在其定义内部引用量局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs
print count()
for i in count():
    print i()
# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 牢记：返回函数不要引用任何循环变量，或者后续会发生变化的变量

# 如果一定要引用循环变量，方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何改变，已绑定到函数参数的值不会变
def count():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j
            return g
        fs.append(f(i))
    return fs
f1, f2, f3 = count()
print f1()
print f2()
print f3()

############################################
# 匿名函数
# 当我们在传入函数时，有些时候，不需要显示地定义函数，直接传入匿名函数更方便
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。
# 匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。
print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数
f = lambda x: x * x
print f
print f(5)
# 同样，也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda : x * x + y * y
print build(1, 2)()

#################################################
# 装饰器
def now():
    print '2013-12-25'
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字
print now.__name__
print f.__name__
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。
# 我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now():
    print '2013-12-25'
# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志：
now()
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数。
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s()' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log('execute')
def now():
    print '2013-12-25'
now()
# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print now.__name__
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
# 或者针对带参数的decorator
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator

####################################################
# 偏函数
# int()函数可以把字符串转换为整数，当仅传入字符串时，int()函数默认按十进制转换：
print int('12345')
# 但int()函数还提供额外的base参数，默认值为10。如果传入base参数，就可以做N进制的转换：
print int('12345', base=8)
print int('99999', base=16)
# 假设要转换大量的二进制字符串，每次都传入int(x, base=2)非常麻烦，于是，我们想到，可以定义一个int2()的函数，默认把base=2传进去：
def int2(x, base=2):
    return int(x, base)
print int2('100000000')
print int2('1010101')
# functools.partial 就是帮助我们创建一个偏函数，不需要我们自己定义int2()：
int2 = functools.partial(int, base=2)
print int2('1000000')
print int2('1010101')
# 所以，简单总结functools.partial的作用就是，把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单。
print int2('1000000', base=10)
# 最后，创建偏函数时，实际上可以接收函数对象，*args和**kw这三个参数。
