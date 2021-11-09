# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 14:40
@Auth ： jiejia
@File ：user_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#前台用户登录，获取token；进行后续的操作#
import requests
import os
from tools.get_yaml import read_yml
import requests
def user_login():
    url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
    print(url)
    dict = {
        "username":"wj_test",
        "password":"123456"
    }
    res = requests.post(url=url,json=dict)
    header = ((res.json())['data'])['token']
    assert res.status_code == 200
    return header

