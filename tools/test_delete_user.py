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

#删除douyin_room里面关联的数据#
def test_del_douyin_room():
    del_res = detete_sql("delete from douyin_room where manager_id = %s",)

test_del_user()