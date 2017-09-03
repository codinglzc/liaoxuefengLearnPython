# coding=utf-8
from collections import Iterable
import os

# 在python中，代码越少越好，越简单越好。所以，python支持一些高级特性

#######################################
# 切片
# 取一个list或tuple的部分元素
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print L[0:3]  # 从索引0开始取，直到索引3为止，但不包括索引3。
print L[:3]   # 如果第一个索引是0,还可以省略。
print L[1:3]  # 也可以从索引1开始，取出2个元素出来。
print L[-2:]  # 倒数切片
print L[-2:-1]

L = range(100)
print L
print L[:10]    # 前10个数
print L[-10:]   # 后10个数
print L[10:20]  # 前11-20个数
print L[:10:2]  # 前10个数，每两个取一个
print L[::5]    # 所有数，每5个取一个

# tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple
print (0, 1, 2, 3, 4, 5)[:3]

# 字符串切片
print 'ABCDEFG'[:3]
print 'ABCDEFG'[::2]

##########################################
# 迭代：for ... in

# 字典
d = {'a': 1, 'b': 2, 'c': 3}
# 迭代key
for key in d:
    print key
# 迭代value
for value in d.itervalues():
    print value

# 字符串
for ch in 'ABC':
    print ch

# 判断对象是否可迭代
print isinstance('abc', Iterable)  # str是否可迭代
print isinstance([1, 2, 3], Iterable)  # list是否可迭代
print isinstance(123, Iterable)  # 整数是否可迭代

# 对list实现类似java那样的下标循环
for i, value in enumerate(['A', 'B', 'C']):
    print i, value

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print x, y

for x in [(1, 1), (2, 4), (3, 9)]:
    print x

##########################################
# 列表生成式：python内置的用来创建list的生成式
# 生成1-10的list
print range(1, 11)

# 生成[1*1, 2*2, 3*3, ..., 10*10]
print [x * x for x in range(1, 11)]

# for 循环后面还可以加上if判断
print [x * x for x in range(1, 11) if x % 2 == 0]

# 还可以使用两层循环，可以生成全排列
print [m + n for m in 'ABC' for n in 'XYZ']

# 列出当前目录下的所有文件和目录名
print [d for d in os.listdir('.')]

# for循环可以同时使用两个甚至多个变量
d = {'x': 'A', 'y': 'B', 'z': 'C'}
print [k + '=' + v for k, v in d.iteritems()]

# 把一个list中所有的字符串变成小写
L = ['Hello', 'World', 'IBM', 'Apple']
print [s.lower() for s in L]

#############################################
# 生成器
# 介绍：
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。
# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器（Generator）。

# 创建一个生成器generator，有很多种方法。

# 方法一：只要把一个列表生成式的[]改成()就可以了
g = (x * x for x in range(10))
print g
# 打印generator的每一个元素
for n in g:
    print n

# 方法二：如果推算的算法比较复杂，用类似列表生成器的for循环无法实现的时候，还可以用函数来实现。
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator。
# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
for n in fib(6):
    print n

# 小结：
# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。



