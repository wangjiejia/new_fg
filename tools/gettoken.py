# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 10:26
@Auth ： jiejia
@File ：gettoken.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
from tests.test_user_login import test_user_login
def gettoken():
    headers1 = test_user_login()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'content-type': 'application/json',
        'authorization': 'Bearer {0}'.format(headers1)}
    return headers
