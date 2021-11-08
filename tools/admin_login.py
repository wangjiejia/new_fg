# -*- coding: utf-8 -*-
"""
@Time ： 2021/10/29 13:46
@Auth ： jiejia
@File ：create_user.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#登录管理后台，获取管理后台token#
import pytest
import requests
def test_adminLogin():
    dict1={
        'username':'admin',
        'password':'123123'
    }
    url = " https://live-admin-qa1.youfenba.com/api/v1/login"
    res = requests.post(url=url,json=dict1)
    r=res.json()
    test_headers=(r['data'])['token']
    return test_headers

def test_headers():
    token = test_adminLogin()
    headers = {'user-agent': 'Mozilla/5.0','content-type': 'application/json;charset=UTF-8','Authorization': 'Bearer {0}'.format(token)}
    return headers
test_headers()




