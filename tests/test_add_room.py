# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/10 16:53
@Auth ： jiejia
@File ：add_room.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#为该抖音号添加直播间#
#douyin_room中新增一条记录，将原始的所有数据都关联到新的用户，原来的抖音号下#
#更新#
import pymysql
import pytest
import requests
from pymysql import NULL
from tools.sql import select_sql,select_sql1
def test_douyin_id():
    ids = select_sql("select id from douyin_room ORDER BY id desc LIMIT 1")
    id = ids[0] + 1
    print(id)
    return id
def test_add_douyin():
     id = test_douyin_id()
     douyin_id = select_sql1("select id from douyin ORDER BY id desc LIMIT 1")
     conn = pymysql.connect(
         host='118.178.114.233',
         port=31445,
         user='root',
         password='AyoufenbBwoca123',
         db='douyin_livetools'
        )
     res_select = select_sql("select id from manager where username = 'wj_test' ORDER BY id desc LIMIT 1")
     manager_id = res_select[0]
     print(manager_id)
     data = {
            "id": id,
            "manager_id": manager_id,
            "douyin_id": douyin_id,
            "uid": "4340475669264183",
            "room_id": "7024331948672011021",
            "title":"在等11.11日？双十一好物已经开抢啦！",
            "auto_record": 1,
            "is_show":1,
            "is_history": 0,
            "delete_status": 0,
            "gmv": 466970,
            "cost": 613908,
            "order_num": 76,
            "start_time": '1635480035',
            "duration": 18022,
            "plan_id": 0,
            "tab_id": 0,
            "updated_at": "2021-10-29 17:14:41",
            "created_at": "2021-10-29 12:02:03",
            # "deleted_at": "2021-05-24 14:08:11"
        }
     table = 'douyin_room'
     keys = ','.join(data.keys())
     values1 = ','.join(['%s'] * len(data))
     sql = 'insert into {table}({keys}) values ({values})'.format(table=table, keys=keys, values=values1)
     cur = conn.cursor()
     try:
         cur.execute(sql,tuple(data.values()))
         conn.commit()
         conn.commit()
     except Exception as e:
         print("操作异常：%s" % str(e))
         conn.rollback()
     finally:
         conn.close()
test_add_douyin()
