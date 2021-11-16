# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/15 15:29
@Auth ： jiejia
@File ：test_douyin_list.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#抖音号管理列表#
import requests
import pytest
import os
import datetime
import json

from tools.get_yaml import read_yml
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
print(url1)
from tools.gettoken import gettoken
headers = gettoken()
def test_douyin_list():
    url = "https://live-tools-qa1.youfenba.com/api/v1/douyin_v2?start_at=2021-10-17&end_at=2021-11-15"
    url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
    start_time = datetime.date.today()
    end_time = datetime.date.today() + datetime.timedelta(days=1)
    dict = {
        "start_at": str(start_time),
        "end_at":str(end_time)
    }
    r=requests.get(url=url,headers=headers)
    res = r.json()
    # r = json.dumps(res,indent=2,ensure_ascii=False)
    assert res['code'] == 200
    assert (((res['data'])['list'])[0])['nickname'] == '三只松鼠'





#使用json对结果进行缩进输出#

test_douyin_list()
# if __name__=='__main__':
#     pytest.main(['test_douyin_list.py'])
