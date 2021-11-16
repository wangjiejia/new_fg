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
import pytest
import unittest
import os
from tools.get_yaml import read_yml
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
print(url)
import requests
def test_user_login():
    dict = {
        "username":"wj_test",
        "password":"123456"
    }
    res = requests.post(url=url,json=dict)
    header = ((res.json())['data'])['token']
    assert res.status_code == 200
    return header
def test_userisnull():
    dict1 = {
        "username":"",
        "password":"123456"
    }
    res = requests.post(url=url,json=dict1)
    r = (res.json())['message']
    assert r == "账户名必填"
    print(r)
def test_passwdisnull():
    dict2 = {
        "username": "wj_test",
        "password": " "
    }
    res = requests.post(url=url, json=dict2)
    r = (res.json())['message']
    print(r)
    assert r == "密码必填"
def test_allnull():
    dict3 = {
        "username": " ",
        "password": " "
    }
    res = requests.post(url=url, json=dict3)
    r = (res.json())['message']
    print(r)
    assert r == "账户名必填"
#用户未注册#
def test_nologin():
    dict4 = {
        "username": "xixiiix",
        "password": " 1212121"
    }
    res = requests.post(url=url, json=dict4)
    r = (res.json())['message']
    print(r)
    assert r == "用户名不存在,请先注册"

def test_passwderror():
    dict5 = {
        "username": "wj_test",
        "password": " 1212121"
    }
    res = requests.post(url=url, json=dict5)
    r = (res.json())['message']
    print(r)
    assert r == "密码不正确"

if __name__=='__main__':
    pytest.main(['test_user_login.py'])

