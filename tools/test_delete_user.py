# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 15:25
@Auth ： jiejia
@File ：delete_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#数据清理，在所有验证结束后；删除创建的所有数据#
import pytest
from tools.test_admin_login import test_headers
from tools.sql import select_sql,detete_sql

header=test_headers()
#删除用户#
def test_del_user():
    del_res = detete_sql("delete  from manager where username = 'wj_test' and deleted_at is null")

#搜索出创建成功的用户ID，再进行删除#
def test_seh_user():
    seh_res = select_sql("select * from manager where username='wj_test' order by id desc")
    manager_id = seh_res[0]
    return manager_id

#删除douyin_room里面关联的数据#
def test_del_douyin_room():
    manager_id = test_seh_user()
    sql = "delete from douyin_room where manager_id = %s",%manager_id
    print(sql)
    # del_res = detete_sql("delete from douyin_room where manager_id = %s",manager_id)

test_del_douyin_room()