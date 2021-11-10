# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 14:49
@Auth ： jiejia
@File ：update_version.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#因为在管理后台新增的用户都是已过期的，所以在使用之前；需要先修改用户版本号；此地是直接新建订单#
import os
import requests
from tools.get_yaml import read_yml
from tools.test_admin_login  import test_headers
from tools.sql import select_sql
def test_update_version():
    user_id = select_sql("select id from manager where username = 'wj_test'")
    url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
    header =  test_headers()
    dict={
        "pay_type":"rm",
        "type":0,
        "trade_on":"12121",
        "vip_type":3,
        "days_type":1,
        "append":0,
        "expired_at":"2021-12-09",
        "pay_price":439900,
        "is_hide":"0",
        "days_num":30,
        "days":30,
        "user_id":user_id[0],
        "edition_id":1,
        "img":"",
        "account_limit":20,
        "price":439900
    }
    try:
        res = requests.post(url=url, headers=header, json=dict)
        assert res.status_code == 200
    except:
        print("验证失败")




test_update_version()
