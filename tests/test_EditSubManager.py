# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/22 15:52
@Auth ： jiejia
@File ：test_EditSubManager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
import requests
from tools.get_yaml import read_yml
from tools.gettoken import gettoken
from tests.test_sub_manager import test_sub_manager
manager_id = test_sub_manager()
headers=gettoken()
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
def test_EditSubManager():
    dict={
        "id":
    }
    res = requests.post(url=)
