# coding=utf-8

# Python内置的sorted()函数就可以对list进行排序
print sorted([36, 5, 12, 9, 21])

# sorted()还可以接收一个比较函数来实现自定义的排序
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
print sorted([36, 5, 12, 9, 21], reversed_cmp)

# 字符串排序，按照ASCII的大小比较
print sorted(['bob', 'about', 'Zoo', 'Credit'])

# 字符串排序，忽略大小写
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'], cmp_ignore_case)


