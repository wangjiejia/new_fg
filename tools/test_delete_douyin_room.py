# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 11:01
@Auth ： jiejia
@File ：test_delete_douyin_room.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from tools.sql import detete_sql,select_sql

def test_delete_douyin_room():
    res_select = select_sql("select id from manager where username = 'wj_test' ORDER BY id desc LIMIT 1")
    manager_id = res_select[0]
    sql = "delete from douyin_room where manager_id = %s"%(manager_id)
    print(sql)
    exe_sql = detete_sql(sql)

test_delete_douyin_room()