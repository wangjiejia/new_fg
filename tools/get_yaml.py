# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/8 15:14
@Auth ： jiejia
@File ：get_yaml.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#获取到yml文件中的数据#
from distutils.log import info
#直接输出文件名对应的URL#
import yaml
import os
def read_yml():
    with open('all.yml',encoding='UTF-8')as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        name = os.path.split(__file__)[-1].split(".")[0]
        print(data.get(name))
read_yml()

