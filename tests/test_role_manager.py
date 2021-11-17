# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 17:36
@Auth ： jiejia
@File ：test_role_manager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#根据角色排序#
import os
import requests
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
headers = gettoken()
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
def test_role_manager_():
    dict={
        "id":1,
        "type":1
    }
