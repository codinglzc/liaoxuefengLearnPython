# coding=utf-8

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print name

sum = 0
for x in [1, 2, 3, 4, 5]:
    sum = sum + x
print sum

# range()生成一个list序列
print range(5)

# 从raw_input()得到的内容永远都是字符串
birth = int(raw_input("birthday: "))
if birth < 2000:
    print '00前'
else:
    print '00后'