# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 15:25
@Auth ： jiejia
@File ：delete_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
import requests


# from tools import admin_login
# id = create_user.create_user()
# test_headers= admin_login.test_headers()
from tools.mysqldb import select_test
id = select_test()
def del_user():
    url='https://live-admin-qa1.youfenba.com/api/v1/manager/' + str(id)
    res=requests.delete(url=url)
    print(url)
    print(res)

del_user()