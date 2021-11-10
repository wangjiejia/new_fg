# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 16:38
@Auth ： jiejia
@File ：test_add_douyin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os

from tools.sql import select_sql,insert_sql

def test_add_douyin():
    res_select = select_sql("select id from manager ORDER BY id desc LIMIT 1")
    manager_id = res_select[0]
    print(manager_id)

    # manager_id = res_select1[1]
    # print(manager_id)
    res_insert = insert_sql("insert into douyin (id,manager_id,account,uid,nickname,avatar,`desc`,praise,awemes,like_count,fan_count,with_shop,dou,balance,origin_uid,buyin_status,buyin_token,buyin_data,buyin_token_at,token,token_at,open_douyin_id,room_id,dou_monitor,live_monitor,`type`,sort,edition_id,auto_record,auto_record_at,expired_at,off_at,last_auth_at,is_first,qc_source,`exception`,created_at,updated_at,deleted_at) values (id,manager_id,'mianchaokeji','1754443783083283','飞瓜智投运营号','https://p9.douyinpic.com/img/tos-cn-avt-0015/ed0098a80d03dd93d60cc8e2a1e042a0~c5_300x300.jpeg?from=2956013662','飞瓜数据旗下飞瓜智投?\n飞瓜智投是专业的运营工具\n覆盖电商直播现场运营、投放监控、播后复盘\n助力精细化运营','0.00','32','188','1244','0','0','0',NULL,'4','','','2021-06-08 14:06:41',NULL,NULL,'0','0','0','1','0','2134','-1','-1','2021-11-05 18:25:41',NULL,NULL,'2021-05-24 14:06:41','0','0','0','2021-05-20 16:30:58','2021-11-05 18:25:41','2021-05-24 14:08:11')")





test_add_douyin()
