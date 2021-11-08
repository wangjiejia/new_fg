# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/8 11:47
@Auth ： jiejia
@File ：mysqldb.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#连接数据库#
import pymysql
db = pymysql.connect(
host='118.178.114.233',
port=30200,
user='root',
password='youfenbBwoca123',
db='douyin_livetools',
charset='utf8'
)
#查询数据#
cur = db.cursor()
sql = "select * from manager where id = 14915"

cur.execute(sql)
res = cur.fetchall()
print(res)

cur.close()
db.close()


# def select_test():



    # r = (res[0])[0]
    # print((res[0])[0])

    # return r

# select_test()
# cur = db.cursor()
#

# #获取第一行数据#
# res_1 = cur.fetchone()
# print(res_1)
# cur.close()
# db.close()

