# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/8 15:14
@Auth ： jiejia
@File ：get_yaml.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#获取到yml文件中的数据#
from tools.file_name import file_name

import yaml
import os
def read_yml():
    with open('all.yml',encoding='UTF-8')as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        name="get_yaml"
        print(name)
        name1 = name = os.path.split(__file__)[-1].split(".")[0]
        print(name1)
        if name == name1:
            print(data)
        else:
            print("在yml文件中未找到对应的条件")


read_yml()

