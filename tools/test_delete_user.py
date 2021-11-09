# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 15:25
@Auth ： jiejia
@File ：delete_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
from tools.test_admin_login import test_headers
from tools.sql import select_sql,detete_sql
header=test_headers()
def test_del_user():
    del_res = detete_sql("delete  from manager where username = 'wj_test' and deleted_at is null")
test_del_user()