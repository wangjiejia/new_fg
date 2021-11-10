# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/10 14:31
@Auth ： jiejia
@File ：test110.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import pymysql
from pymysql import NULL
data = {
    "id": 12435,
    "manager_id": 11,
    "account": "mianchaokeji",
    "uid": "1754443783083283",
    "nickname": "飞瓜智投运营号",
    "avatar": "https://p9.douyinpic.com/img/tos-cn-avt-0015/ed0098a80d03dd93d60cc8e2a1e042a0~c5_300x300.jpeg?from=2956013662",
    "desc": "飞瓜数据旗下飞瓜智投",
    "praise": "0.00",
    "awemes": "32",
    "like_count": "188",
    "fan_count": "1244",
    "with_shop": "0",
    "dou": "0",
    "balance": "0",
    "origin_uid": NULL,
    "buyin_status": "4",
    "buyin_token": "",
    "buyin_data": "",
    "buyin_token_at": "2021-06-08 14:06:41",
    "token": NULL,
    "token_at": NULL,
    "open_douyin_id": "0",
    "room_id": "0",
    "dou_monitor": "0",
    "live_monitor": "1",
    "type": "0",
    "sort": "2134",
    "edition_id": "-1",
    "auto_record": "-1",
    "auto_record_at": "2021-11-05 18:25:41",
    "expired_at": NULL,
    "off_at": NULL,
    "last_auth_at": "2021-05-24 14:06:41",
    "is_first": "0",
    "qc_source": "0",
    "exception": "0",
    "created_at": "2021-05-20 16:30:58",
    "updated_at": "2021-11-05 18:25:41",
    "deleted_at": "2021-05-24 14:08:11"
}
key=','.join(data.keys())
# val = data.values()
val=values=','.join(['%s']*len(data))
print(key)
