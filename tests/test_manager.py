# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 15:33
@Auth ： jiejia
@File ：test_manager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#查看管理员账户信息#
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
from tools.sql import select_sql
import os
import requests
import json
import datetime
headers = gettoken()

url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])

def test_manager():
    res = requests.get(url=url,headers=headers)
    r=res.json()
    print(json.dumps(r,indent=4))
    assert r['code'] == 200
    assert  (r['data'])['username'] == 'wj_test'
    assert (r['data'])['name'] == '管理员'
    # end_time = datetime.date.today() + datetime.timedelta(days=30)
    #因为新增了一笔1个月的订单，所以过期时间等于当前时间往后+1个月#
    # expried_time = datetime((r['data'])['expired_at'])
    #
    # time1 = int(datetime.time.strftime("%Y%M%D", expried_time))
    # time2 = int(datetime.time.strftime("%Y%M%D", time3))

def test_update_manager_name():
    manager_id = select_sql("select id from manager where username='wj_test' and  deleted_at is null order by id desc ")




test_manager()
