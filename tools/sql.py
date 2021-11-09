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
password='AyoufenbBwoca123',
db='douyin_livetools'
)
print(conn)


#查询数据,sql设置为参数，直接查询即可#
def select_sql(sel_sql):
    cur = conn.cursor()
    # sql = "select * from manager where username = 'wj_test' and deleted_at is null"
    # print(sql)
    cur.execute(sel_sql)
    print(sel_sql)
    res = cur.fetchone()
    print(res)
    cur.close()
    conn.close()
    return res


#删除数据#
def detete_sql(del_sql):
    cur = conn.cursor()
    try:
        cur.execute(del_sql)
        conn.commit()
    except Exception as e:
        print("操作异常:%s" % str(e))
        conn.rollback()
    finally:
        conn.close()




#更新数据#
def update_sql(update_sql):
    cur = conn.cursor()
    try:
        cur.execute(update_sql)
        conn.commit()
    except Exception as e:
        print("操作异常:%s" % str(e))
        conn.rollback()
    finally:
        conn.close()


#插入数据#
def insert_sql(insert_sql):
    cur = conn.cursor()
    try:
        cur.execute(insert_sql)
        conn.commit()
    except Exception as e:
        print("操作异常:%s" % str(e))
        conn.rollback()
    finally:
        conn.close()










