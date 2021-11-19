# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 17:46
@Auth ： jiejia
@File ：test_create_sub_manager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#创建子账户#
import os
import requests
from tests.test_douyin_list import test_douyin_list
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
headers=gettoken()
id = test_douyin_list()
print(id)
#新增一个子账户#
def test_create_sub_manager():
    dict = {
        "name":"wangjiejia接口新增1",
        "douyin_ids":id
    }
    print(dict)
    res=requests.post(url=url,headers=headers,json=dict)
    r=res.json()
    assert r['code'] == 200

#新增过的子账户提示已存在#
def test_CreateSubManagerExisted():
    dict = {
        "name": "wangjiejia接口新增1",
        "douyin_ids": id
    }
    res = requests.post(url=url,json=dict,headers=headers)
    r=res.json()
    assert r['code'] != 200
    assert r['message'] == "该员工已存在"
#未填写员工姓名，创建失败#
def test_CreateFail1():
    dict={
        "name":"",
        "douyin_ids":id
    }
    res=requests.post(url=url,headers=headers,json=dict)
    r=res.json()
    assert r['code'] != 200
    assert r['message'] == "请填写员工姓名"
    #未选择抖音号，添加成功#
def test_CreateSub():
    dict = {
        "name": "test1",
        "douyin_ids": []
    }
    res = requests.post(url=url, headers=headers, json=dict)
    r = res.json()
    assert r['code'] == 200


    #添加成功后的
def test_CreateSubManagerSearch():


