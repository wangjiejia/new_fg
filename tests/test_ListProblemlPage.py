import requests
import json

# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 15:37:40 2021

@author: HP
"""

import datetime
import time

import requests

url = "http://web.dcyun.com:10096/RiverMasterUpload/api/CitySent/ListProblemlPage"

day1 = input('请输入开始日期：格式为YY-MM-DD:')
day2 = input('请输入结束日期：格式为YY-MM-DD:')

time_array1 = time.strptime(day1, "%Y-%m-%d")
timestamp_day1 = int(time.mktime(time_array1))
time_array2 = time.strptime(day2, "%Y-%m-%d")
timestamp_day2 = int(time.mktime(time_array2))
result = (timestamp_day2 - timestamp_day1) // 60 // 60 // 24

infon = {'userName': 'jhpt',
         'authkey': '41FA7112',
         'token': '41FA7112',
         'startTime': day1,
         'endTime': day2,
         'problemStatus': '697A4330-189C-421B-98D5-6892369F38F2',
         'PageIndex': '1',
         'PageSize': '20'}

headers = {}

if (result < 30):

    response1 = requests.request("POST", url, headers=headers, data=infon)
    print('返回省平台问题下发列表接口返回值')

    print(response1.text.encode('utf8'))

    print("***********************")

else:
    print('输入的日期间隔不要超过1个月')


