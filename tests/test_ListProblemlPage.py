import datetime
import time

import requests

import prettytable as PrettyTable

url = "http://web.dcyun.com:10096/RiverMasterUpload/api/CitySent/ListProblemlPage"

# 日期间隔的计算
# 2021-10-10
# 2021-10-20
day1 = input('请输入开始日期：格式为YY-MM-DD')
day2 = input('请输入结束日期：格式为YY-MM-DD')
# day1='2021-11-10'
# day2='2021-11-20'
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
# 日期小于1个月

if (result < 30):

    response = requests.request("POST", url, headers=headers, data=infon)
    print('返回省平台问题下发列表接口返回值')
    response1 = response.json()

    response2 = response1['rows']
    print(len(response2))
    # 总的值
    total = response1['total']
    # 定义一个表格
    tb = PrettyTable.PrettyTable()
    # 表头
    tb.field_names = ['省平台问题编号', '上报时间', '问题更新时间', '问题状态', '问题类型', '是否来源于省平台']

    print('共查询到', total, '条记录')
    for i in range(0, len(response2)):

        # 转化为文字，Problem_Status
        if (response2[i]['Problem_Status'] == '697A4330-189C-421B-98D5-6892369F38F2'):
            response2[i]['Problem_Status'] = '已处理'
        elif (response2[i]['Problem_Status'] == '79B5DF25-CBD1-493E-B4B3-E2EB19C62D41'):
            response2[i]['Problem_Status'] = '未处理'
        else:
            response2[i]['Problem_Status'] = response2[i]['Problem_Status']

        # Problem_Type
        if (response2[i]['Problem_Type'] == '1F36CDF4-A247-47F8-BF69-99EDF292BE3F'):
            response2[i]['Problem_Type'] = '巡查上报'
        elif (response2[i]['Problem_Type'] == '52AE95C6-BB8F-4355-AE7F-2B63D81C5B88'):
            response2[i]['Problem_Type'] = '交办'
        elif (response2[i]['Problem_Type'] == 'D1036ABD-2B35-4C1A-A701-0615F1563760'):
            response2[i]['Problem_Type'] = '督查'