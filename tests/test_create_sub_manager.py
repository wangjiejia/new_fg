# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 17:46
@Auth ： jiejia
@File ：test_create_sub_manager.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#创建子账户#
import os
import requests
from tools.gettoken import gettoken
from tools.get_yaml import read_yml
url = (read_yml()).get(os.path.split(__file__)[-1].split(".")[0])
def test_create_sub_manager():
