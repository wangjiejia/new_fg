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
import allure
import os
def run():
    print("执行开始")
if __name__=='__main__':
    # pytest.main(["-v", "-s",
    #              "./test_admin_login.py","./test_create_user.py",
    #              "./test_update_version.py","./gettoken.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_user_login.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_add_douyin.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_add_room.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_douyin.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_douyin_list.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_douyin_room.py",
    #              # "C:\/Users\/1\/PycharmProjects\/new_fg\/tests\/test_douyin_expired.py",
    #              # "./test_delete_user.py"
    #              '--alluredir', './report/xml'])

    pytest.main(["-v", "-s",'--alluredir', './Outputs/result','./test_admin_login.py'])
    split = 'allure'+'generate'+'./Outputs/result'+'o'+'./Outputs/report' + '--clean'
    os.system(split)

