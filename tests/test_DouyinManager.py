# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/22 14:50
@Auth ： jiejia
@File ：test_DouyinManaget.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#按抖音号分组#
import pytest
import os
import requests
import json
from  tools.gettoken import gettoken
from tools.get_yaml import read_yml
headers = gettoken()
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
def test_DouyinManager():
    dict={}
    res=requests.get(url=url,json=dict,headers=headers)
    r=res.json()
    # m=json.dumps( r,indent=2,ensure_ascii=False)
    assert r['code'] == 200
    assert (((r['data'])['list'])[0])['nickname'] == '花印旗舰店'

test_DouyinManager()
