# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 14:15
@Auth ： jiejia
@File ：test_douyin_room.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#我的直播间--直播间列表#
import os
import pytest
import requests
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
headers= gettoken()
def test_douyin_room():
    dict= {
        "monitor": 1,
        "uid": 4340475669264183,
        "start_at": 2021 - 11 - 10,
        "end_at": 2021 - 11 - 16,
        "page": 1,
        "limit": 20
    }
    res = requests.get(url=url1,json=dict,headers=headers)
    r = res.json()
    assert r['code'] == 200
    assert (((r['data'])[0])['douyin'])['nickname'] == '花印旗舰店'
    print(res.json())
test_douyin_room()
#查看正在直播中#
if __name__=='__main__':
    pytest.main(['test_douyin_room.py'])
