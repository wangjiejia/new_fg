# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 11:42
@Auth ： jiejia
@File ：testtest1.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
# -*- encoding: utf-8 -*-
##
#连接数据库#
import pymysql
conn = pymysql.connect(
host='118.178.114.233',
port=31445,
user='root',
password='youfenbBwoca123',
db='douyin_livetools'
)
print(conn)
#查询数据#
cur = conn.cursor()
sql = "select * from manager order by id desc limit 1"
print(sql)
cur.execute(sql)
res = cur.fetchone()
print(res)
cur.close()
conn.close()


