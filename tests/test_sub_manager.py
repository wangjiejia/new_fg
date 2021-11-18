# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 17:20
@Auth ： jiejia
@File ：test_sub_manager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#按员工进行分组，员工列表,子账号列表#

import os
import requests
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
headers=gettoken()
def test_sub_manager():
    dict={
        "page":1,
        "name":" ",
        "status":0
    }
    res = requests.get(url=url,json=dict,headers=headers)
    r=res.json()
    assert r['code'] == 200
    print(r)
    #查找冻结的员工#
def test_sub_manager_1():
    dict = {
        "page": 1,
        "name": " ",
        "status": 1
    }
    res = requests.get(url=url, json=dict, headers=headers)
    r = res.json()
    assert r['code'] == 200
    print(r)



