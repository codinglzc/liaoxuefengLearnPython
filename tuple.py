# coding=utf-8

# tuple和list非常类似，但是tuple一旦初始化就不能修改

classmates = ('Michael', 'Bob', 'Tracy')
print classmates

# 现在，classmates这个tuple不能变了，它也没有append()，insert()这样的方法。其他获取元素的方法和list是一样的，你可以正常地使用classmates[0]，classmates[-1]，但不能赋值成另外的元素。


# tuple和list的混合使用
t = ('a', 'b', ['A', 'B'])
print t
t[2][0] = 'X'
t[2][1] = 'Y'
print t