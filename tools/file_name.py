# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/8 15:56
@Auth ： jiejia
@File ：file_name.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#获取当前文件的文件名#
import os
import sys
def file_name():
    name = os.path.split(__file__)[-1].split(".")[0]
    return name


file_name()




