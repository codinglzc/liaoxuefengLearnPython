# coding=utf-8

"""
mysql
"""

# 导入MySQL驱动：
import mysql.connector

# 注意把password设为你的root口令：
conn = mysql.connector.connect(user='root', password='123456', database='test', use_unicode=True)

# cursor = conn.cursor()

conn.close()

