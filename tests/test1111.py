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
def test_douyin_list():
    url = "https://live-tools-qa1.youfenba.com/api/v1/douyin_v2?start_at=2021-10-17&end_at=2021-11-15"
    headers = {"headers": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9saXZlLXRvb2xzLXFhMS55b3VmZW5iYS5jb21cL2FwaVwvdjFcL2F1dGhfbG9naW5fdG9rZW4iLCJpYXQiOjE2MzY5NjE3MDAsImV4cCI6MTYzNzU2NjUwMCwibmJmIjoxNjM2OTYxNzAwLCJqdGkiOiJoRnRFWkRLZ3hvY1RtUjd1Iiwic3ViIjoxNDk0OSwicHJ2IjoiMjc4YTcyZTEyNGVmM2I5NzRiNGI3ZGEwYjg5M2RlOWE2N2ZmYjhlYyJ9.M6I-Vz6f2t4V7B37GeDC7sak9pVMORkib8xLJcBvl4E"}
    # start_time = datetime.date.today()
    # end_time = datetime.date.today() + datetime.timedelta(days=1)
    # dict = {
    #     "start_at": str(start_time),
    #     "end_at":str(end_time)
    # }
    r=requests.get(url=url,headers=headers)
    print(r)
test_douyin_list()
