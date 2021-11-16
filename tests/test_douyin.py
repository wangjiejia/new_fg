# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 11:41
@Auth ： jiejia
@File ：test_douyin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#抖音号详情#
#使用生成的用户对应的抖音号，查看抖音号详情#

from tools.get_yaml import read_yml
import os
import pytest
import requests
from tools.gettoken import gettoken
from tools.sql import select_sql1
uid = select_sql1("SELECT uid from douyin where manager_id = (select id from manager where username='wj_test' order by id desc) and off_at is null")
headers = gettoken()
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
def douyin():
    dict={
        "uid":uid[0]
    }
    print(dict)
    res = requests.post(url=url1,json=dict,headers=headers)
    r = res.json()
    print(r)

douyin()


