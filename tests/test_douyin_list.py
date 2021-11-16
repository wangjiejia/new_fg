# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/15 15:29
@Auth ： jiejia
@File ：test_douyin_list.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import requests
import pytest
import os
import datetime
from tests.test_user_login import test_user_login
from tools.get_yaml import read_yml
url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
print(url1)

def test_douyin_list():
    url = "https://live-tools-qa1.youfenba.com/api/v1/douyin_v2?start_at=2021-10-17&end_at=2021-11-15"
    url1 = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
    headers1 = test_user_login()
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36', 'content-type': 'application/json',
               'authorization': 'Bearer {0}'.format(headers1)}
    print(headers)
    start_time = datetime.date.today()
    end_time = datetime.date.today() + datetime.timedelta(days=1)
    dict = {
        "start_at": str(start_time),
        "end_at":str(end_time)
    }
    r=requests.get(url=url,headers=headers)
    print(r.json())
test_douyin_list()
# if __name__=='__main__':
#     pytest.main(['test_douyin_list.py'])
