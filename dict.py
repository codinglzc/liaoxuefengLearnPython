# coding=utf-8

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print d['Michael']

# 向字典中添加元素
d['Adam'] = 67
print d

# 修改字典中的元素
d['Adam'] = 77
print d

# 避免key不存在的错误
if 'Adam' in d:
    print d['Adam']
# 如果存在key为'Adam'的元素，则返回值;反之，返回默认值-1
print d.get('Adam', -1)
print d

# 删除一个key-value
d.pop('Adam')
print d
