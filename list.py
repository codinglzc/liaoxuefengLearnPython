# coding=utf-8

classmates = ['Michael', 'Bob', 'Tracy']
print classmates

print len(classmates)

print classmates[0]
print classmates[1]
print classmates[2]

# 负数做索引
print classmates[-1]
print classmates[-2]
print classmates[-3]

# 往list中追加元素到末尾
classmates.append('Adam')
print classmates

# 把指定元素插入到指定的位置
classmates.insert(1, 'Jack')
print classmates

# 删除list末尾的元素
classmates.pop()
print classmates

# 删除指定位置的元素
classmates.pop(1)
print classmates

# 把某个元素替换成别的元素
classmates[1] = 'Sarah'
print classmates

# list里面的元素的数据类型也可以不同
L = ['Apple', 123, True]
print L

S = ['python', 'java', ['asp', 'php'], 'scheme']
print len(S)
print S

