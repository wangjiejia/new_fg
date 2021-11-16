# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 11:07
@Auth ： jiejia
@File ：douyin_expired.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#授权管理列表#
from tools.gettoken import gettoken
import os
import requests
import pytest
from tools.get_yaml import read_yml
headers=gettoken()
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
print(url1)
def test_douyin_expired():
    url = url1+"?"+"limit=10000"
    res=requests.get(url=url,headers=headers)
    r = res.json()
    assert r['code'] == 200
    assert (((r['data'])['list'])[0])['nickname'] == "花印旗舰店"

def test_douyin_expired_error():
    url = url1
    res = requests.get(url=url1,headers=headers)
    r=res.json()
    assert r['code'] == 200
    assert (((r['data'])['list'])[0])['nickname'] == "花印旗舰店"

# test_douyin_expired_error()

if __name__=='__main__':
    pytest.main(['test_douyin_expired.py'])

