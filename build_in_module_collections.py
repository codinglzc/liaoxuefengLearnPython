# coding=utf-8

# 内建模块

################################################
# collections
# collections是Python内建的一个集合模块，提供了许多有用的集合类

# namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定量tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print p.x
print p.y
print isinstance(p, Point)
print isinstance(p, tuple)
# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle = namedtuple('Circle', ['x', 'y', 'r'])
################################################

################################################
# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.append('y')
print q
# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
################################################

################################################
# defaultdict
# 使用dict时，如果引用的key不存在，就会抛出KeyError。
# 如果希望key不存在时，返回一个默认值，就可以用defaultdict:
from collections import defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print dd['key1']  # key1存在
print dd['key2']  # key2不存在，返回默认值
# 注意默认值是调用函数返回的，而函数在创建defaultdict对象传入。
# 除了在key不存在时返回默认值，defaultdict的其他行为跟dict是完全一样的。
################################################

################################################
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict:
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
print d  # dict的key是无序的
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print od  # OrderedDict的Key是有序的
# 注意：OrderedDict的key会按照插入的顺序排序，不是key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print od
#################################################

#################################################
# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1

print c
#################################################
