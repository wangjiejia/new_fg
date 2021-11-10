# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/10 16:53
@Auth ： jiejia
@File ：add_room.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pymysql
import pytest
import requests
from pymysql import NULL
from tools.sql import select_sql
def test_douyin_id():
    ids = select_sql("select id from douyin_room ORDER BY id desc LIMIT 1")
    id = ids[0] + 1
    print(id)
    return id
def test_add_douyin():
     id = test_douyin_id()
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
            "douyin_id": "mianchaokeji",
            "uid": "82914947908",
            "room_id": "飞瓜智投运营号",
            "auto_record": "https://p9.douyinpic.com/img/tos-cn-avt-0015/ed0098a80d03dd93d60cc8e2a1e042a0~c5_300x300.jpeg?from=2956013662",
            "is_history": "飞瓜数据旗下飞瓜智投",
            "delete_status": "0.00",
            "gmv": 32,
            "cost": 188,
            "order_num": 1244,
            "start_time": 0,
            "duration": 0,
            "plan_id": 0,
            "tab_id": NULL,
            "created_at": "2021-05-20 16:30:58",
            "updated_at": "2021-11-05 18:25:41",
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
