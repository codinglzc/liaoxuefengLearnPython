# coding=utf-8

# 内置模块

# Base64是一种用64个字符来表示任意二进制数据的方法。

# Python内置的base64可以直接进行base64的编解码：
import base64
print base64.b64encode('binary\x00string')
print base64.b64decode('YmluYXJ5AHN0cmluZw==')

# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种'urlsafe'的base64编码，其实就是把字符+和/分别编程-和_:
print base64.b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64encode('i\xb7\x1d\xfb\xef\xff')
print base64.urlsafe_b64decode('abcd--__')

# Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。

# Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。

# 小结：
# Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。
