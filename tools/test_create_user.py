# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 14:25
@Auth ： jiejia
@File ：create_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pytest
import requests
import os
from tools import test_admin_login
from tools.get_yaml import read_yml
test_headers= test_admin_login.test_headers()
def test_create_user():
    headers=test_headers
    url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
    dict1={
        'company': "勿删除",
        'company_short': "勿删",
        'logo': "",
        'password': "123456",
        'username': "wj_test"
    }
    res=requests.post(url=url,json=dict1,headers=headers)
    r=res.json()
    print(r)
    # print((r['data'])['id'])
    # return (r['data'])['id']

test_create_user()



