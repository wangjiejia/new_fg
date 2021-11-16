# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/16 16:17
@Auth ： jiejia
@File ：run.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#批量执行多个py文件#
import pytest
import report
import rerun as rerun


def run():
    print("执行开始")

if __name__=='__main__':
    pytest.main(["-v", "-s", "./tools/test_admin_login/", "./tools/test_create_user/", "./tools/test_delete_user/", "--html=" + report, "--reruns", rerun])
