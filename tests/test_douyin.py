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
def test_douyin():
    url = url1+"/"+uid[0]

    res = requests.get(url=url,headers=headers)
    r = res.json()
    assert r['code'] == 200
    assert (((r['data'])['list'])[0])['nickname'] == '花印旗舰店'

    print(r)


#我的直播间-侧边栏抖音号展示#
def test_douyin_1():
    url = url1 +  "limit=1000"+"&"+"live_end=1"

    res = requests.get(url=url,headers=headers)
    r=res.json()
    assert r['code'] == 200
    assert (((r['data'])['list'])[0])['nickname'] == "花印旗舰店"


# test_douyin()


if __name__=='__main__':
    pytest.main(['test_douyin.py'])


