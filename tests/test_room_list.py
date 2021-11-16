# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 14:57
@Auth ： jiejia
@File ：test_room_list.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#我的抖音号-直播记录列表#
import json
import os
import requests
import pytest
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
headers = gettoken()
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
print(url1)
def test_room_list():

    url=url1+"?uid=4340475669264183&start_at=2021-10-01&end_at=2021-10-31&limit=20&page=1&export=1"
    print(url)
    # dict = {
    #     "uid": "4340475669264183",
    #     "start_at": "2021 - 10 - 01",
    #     "end_at": "2021 - 10 - 31",
    #     "limit": 20,
    #     "page": 1,
    #     "export": 1
    # }
    res = requests.get(url=url,headers=headers)
    r = res.json()
    assert r['code'] == 200
    assert (((r['data'])[0])['douyin'])['nickname'] == "花印旗舰店"


if __name__=='__main__':
    pytest.main(['test_room_list.py'])


