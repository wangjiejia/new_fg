# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/17 11:56
@Auth ： jiejia
@File ：test_ListProblemlPage.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#省平台问题下发列表接口#
import requests

def test_ListProblemlPage():
    url = "http://web.dcyun.com:10096/RiverMasterUpload/api/CitySent/ListProblemlPage"
    dict = {
        "userName":"jhpt",
        "authKey":"41FA7112",
        "token":"41FA7112",
        "startTime":"2021-10-17",
        "endTime":"2021-11-17",
        "problemStatus":1,
        "PageIndex":"1",
        "PageSize":"20"
    }
    res = requests.post(url=url,json=dict)
    r= res.json()
    print(r)


def test_GetProblemlDetail():
    url = "http://web.dcyun.com:10096/RiverMasterUpload/api/CitySent/GetProblemlDetail"
    dict = {
        "userName":"jhpt",
        "authKey":"41FA7112",
        "token":"41FA7112",
        "problemID":"f9269a05-8afc-4ae4-8db7-f1c2ef76cfb3",
    }
    res = requests.post(url=url,json=dict)
    r= res.json()
    print(r)

# test_ListProblemlPage()
test_GetProblemlDetail()
