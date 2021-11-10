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
     res_select = select_sql("select id from manager ORDER BY id desc LIMIT 1")
     manager_id = res_select[0]
     print(manager_id)
     data = {
            "id": id,
            "manager_id": manager_id,
            "douyin_id": douyin_id,
            "uid": "82914947908",
            "room_id": "7018488034958002980",
            "title":"三只松鼠坚果礼上新，假期旅游囤货必备！",
            "auto_record": 1,
            "is_show":1,
            "is_history": 0,
            "delete_status": 0,
            "gmv": 20079290,
            "cost": 4959861,
            "order_num": 1558,
            "start_time": '1634119334',
            "duration": 28733,
            "plan_id": 0,
            "tab_id": 0,
            "updated_at": "2021-11-05 18:25:41",
            "created_at": "2021-05-20 16:30:58",
            "deleted_at": "2021-05-24 14:08:11"
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
