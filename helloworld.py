# coding=utf-8

# IO: raw_input and print

print 'hello world!'

print 'The quick brown fox', 'jumps over', 'the lazy dog'

print 300

print 100 + 200

print '100 + 200 =', 100 + 200


# name = raw_input('please enter your name: ')

# print 'hello,', name

print '\\\t\\'

print r'\\\t\\'

print '''line1
line2
line3'''


print True and True

print True and False

print False and False


print True or True

print True or False

print False or False


age = 19
if age >= 18:
    print 'adult'
else:
    print 'teenager'


a = 'ABC'
b = a
a = 'XYZ'
print b


# 常量的表示一般都用大写
PI = 3.14159265359


print 10/3
print 10.0/3


# ord() 和 chr()函数，可以把字母和对应的数字相互转换
print ord('A')
print chr(65)

# 以Unicode表示的字符串用u'...'表示，
print u'中文'
print u'ABC'.encode('utf-8')
print u'中文'.encode('utf-8')

# len()函数可以返回字符串的长度
print len(u'ABC')
print len('ABC')
print len(u'中文')

# 格式化输出
print 'Hello, %s' % 'World'
print 'Hi, %s, you have $%d.' % ('Michael', 1000000)

print '%2d-%02d' % (3, 1)
print '%.2f' % 3.1415926

print 'Age: %s. Gender: %s' % (25, True)

print 'growth rate: %d%%' % 7

