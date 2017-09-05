# coding=utf-8

# 文件读写

# 读文件：内置open()函数，传入文件名和标示符。
f = open('/home/lzc/PycharmProjects/liaoxuefengLearnPython/test.txt', 'r')
# 调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：
print f.read()
# 最后一步是调用close()方法关闭文件。
f.close()
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open('/home/lzc/PycharmProjects/liaoxuefengLearnPython/test.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()
# 但是每次都这么写实在太繁琐，所以，Python引入量with语句来自动帮我们调用close()方法：
# 这和前面的try ... finally是一样的，但是代码更加简洁，并且不必调用f.close()方法。
with open('/home/lzc/PycharmProjects/liaoxuefengLearnPython/test.txt', 'r') as f:
    print f.read()
# 调用read(size)方法，每次最多读取size个字节的内容。
# 调用readline()可以每次读取一行内容。
# 调用readlines()一次读取所有内容并按行返回list
# 所以，给出如下选择：
# 1.如果文件很小，read()一次性读取最方便;
# 2.如果不能确定文件大小，反复调用read(size)比较保险;
# 3.如果是配置文件，调用readlines()最方便。

###############################################
# 二进制文件
# 前面讲的默认都是读取文本文件，并且是ASCII编码的文本文件。要读取二进制文件，比如图片，视频等，用'rb'模式打开文件既可：
# with open('/home/lzc/PycharmProjects/liaoxuefengLearnPython/test.jpg', 'rb') as f:
    # print f.read()

#######################################################
# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
with open('/home/lzc/PycharmProjects/liaoxuefengLearnPython/test.txt', 'w') as f:
    f.write('Hello, world!')

# 小结：
# 在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。



########################################################
# 操作文件和目录

# 使用os模块的基本功能：
import os
print os.name  # 操作系统名字
print os.uname()  # 获取详细的系统信息
# 注意：uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个dict中，可以直接查看：
print os.environ
# 获取某个环境变量的值，可以调用os.getenv()函数：
print os.getenv('PATH')


# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
# 查看当前目录的绝对路径：
print os.path.abspath('.')
# 在某个目录下创建一个新目录
# 首先把新目录的完整路径表示出来：
old_path = os.path.abspath('.')
new_path = os.path.join(old_path, 'testdir')
# 然后创建一个目录：
os.mkdir(new_path)
# 删掉一个目录：
os.rmdir(new_path)
# 把两个路径合成一个时，不要直接拼接字符串，而是通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
# 同样的道理，要拆分路径时，也不要直接取拆字符串，而是通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print os.path.split(old_path)
# os.path.splitext()可以直接获得文件扩展名：
print os.path.splitext('/path/to/file.txt')
# 这些合并，拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 文件操作使用下面的函数。假设当前目录下有一个test.txt文件：
# 对文件重命名：
# os.rename('test.txt', 'test_rename.txt')
# 删掉文件：
# os.remove('test_rename.txt')

# 列出当前目录下的所有目录：
print [x for x in os.listdir('.') if os.path.isdir(x)]
# 列出所有的.py文件：
print [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']


####################################################
# 序列化
# 定义：把变量从内存中变成可存储或传输的过程。
# Python提供两个模块来实现序列化：cPickle和pickle。
# 这两个模块功能是一样的，区别在于cPickle是C语言写的，速度快，pickle是纯Python写的，速度慢，跟cStringIOheh和StringIO一个道理。
# 用的时候，先尝试导入cPickle，如果失败，再导入pickle：
try:
    import cPickle as pickle
except ImportError:
    import pickle
# 尝试把一个对象序列化并写入文件：
# pickle.dumps()方法把任意对象序列化成一个str，然后，就可以把这个str写入文件。
d = dict(name='Bob', age=20, score=80)
print pickle.dumps(d)
# 另一个方法，pickle.dump()直接把对象序列化后写入一个流中：
with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)
# 反序列化，pickle.loads()或者pickle.load()，同上：
with open('dump.txt', 'rb') as f:
    print pickle.load(f)

#################################################
# JSON
# JSON类型------Python类型
# {}            dict
# []            list
# "string"      'str'或u'unicode'
# 1234.56       int或float
# true/false    True/False
# null          None
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。
import json
d = dict(name='Bob', age=22, score=88)
print json.dumps(d)  # Python对象转成一个JSON
print json.loads(json.dumps(d))  # JSON转成Python对象
# 注意一点：json.loads()返回的对象中所有的字符串对象默认都是unicode而不是str

# JSON进阶
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
s = Student('Bob', 23, 99)
# 通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义量__slots__的class。
print json.dumps(s, default=lambda obj: obj.__dict__)
# 反过来：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print json.loads(json_str, object_hook=dict2student)
