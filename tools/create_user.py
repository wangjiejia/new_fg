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
from tools import admin_login
test_headers= admin_login.test_headers()
def create_user():
    headers=test_headers
    url = "https://live-admin-qa1.youfenba.com/api/v1/manager"
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



