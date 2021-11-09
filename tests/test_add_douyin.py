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
    res_select1 = select_sql("select id,manager_id from douyin ORDER BY id desc limit 1")
    id = res_select1[0] + 1
    manager_id = res_select1[1]
    res_insert = insert_sql("insert into douyin(id,manager_id,account,uid,nickname,avatar,desc,praise,awemes,like_count,fan_count,with_shop,dou,balance,origin_uid,buyin_status,buyin_token,buyin_data,buyin_token_at,token,token_at,open_douyin_id,room_id,dou_monitor,live_monitor,type,sort,edition_id,auto_record,auto_record_at,expired_at,off_at,last_auth_at,is_first,qc_source,exception,created_at,updated_at,deleted_at)values (id,manager_id,'baicaoweitv','4503247944683967','杭州优瓜科技','https://p3.huoshanimg.com/img/aweme-avatar/douyin-user-file_cf4f74c669506031dae132e2ef420876~c5_300x300.jpeg?from=2956013662','这里是百草味零食直播专场哟！\/n每天都有爆款零食福利等待大家\/n加入粉丝团，与百草味一起玩耍吧','0.00','11','365','2688','0','0','0','','5','livetools_token:buyin:26194585a0f8f6629df82e523f788067_lf','','2021-10-27 15:10:53','','','0','0','0','1','0','7063','-1','1','2021-11-08 17:05:41','','','2021-10-12 15:10:53','0','0','0','2021-08-24 17:58:55', '2021-11-09 16:55:55','')")





test_add_douyin()
