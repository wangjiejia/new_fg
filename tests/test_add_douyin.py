# -*- coding: utf-8 -*-
"""
@Time ： 2021/11/9 16:38
@Auth ： jiejia
@File ：test_add_douyin.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
#直接使用插入语句添加抖音号#
#使用data进行传参，再传到入参里去#
#先把所有的values值都先用占位符替换，然后再执行sql语句时，再把所有的占位符用字典里的值替换掉#
import os
import pymysql
from pymysql import NULL
from tools.sql import select_sql,insert_sql
def test_douyin_id():
    ids =  select_sql("select id from douyin ORDER BY id desc LIMIT 1")
    id = ids[0]+1
    print(id)
    return id


def test_add_douyin():
    id = test_douyin_id()
    conn = pymysql.connect(
        host='118.178.114.233',
        port=31445,
        user='root',
        password='AyoufenbBwoca123',
        db='douyin_livetools'
    )
    print(conn)
    res_select = select_sql("select id from manager ORDER BY id desc LIMIT 1")
    manager_id = res_select[0]
    data = {
        "id":id,
        "manager_id": manager_id,
        "account":"mianchaokeji",
        "uid":"1754443783083283",
        "nickname":"飞瓜智投运营号",
        "avatar":"https://p9.douyinpic.com/img/tos-cn-avt-0015/ed0098a80d03dd93d60cc8e2a1e042a0~c5_300x300.jpeg?from=2956013662",
        "`desc`":"飞瓜数据旗下飞瓜智投",
        "praise":"0.00",
        "awemes":32,
        "like_count":188,
        "fan_count":1244,
        "with_shop":0,
        "dou":0,
        "balance":0,
        "origin_uid":NULL,
        "buyin_status":4,
        "buyin_token":"",
        "buyin_data":"",
        "buyin_token_at":"2021-06-08 14:06:41",
        "token":NULL,
        "token_at":"2021-12-08 14:06:41",
        "open_douyin_id":0,
        "room_id":"1000",
        "dou_monitor":0,
        "live_monitor":1,
        "type":0,
        "sort":2134,
        "edition_id":1,
        "auto_record":1,
        "auto_record_at":"2021-11-05 18:25:41",
        "expired_at":"2022-12-08 14:06:41",
        # "off_at": NULL，如果想要该字段，直接显示默认值，直接整个字段不传就行,
        "last_auth_at":"2021-05-24 14:06:41",
        "is_first":0,
        "qc_source":0,
        "exception":0,
        "created_at":"2021-05-20 16:30:58",
        "updated_at":"2021-11-05 18:25:41",
        "deleted_at":"2021-05-24 14:08:11"
    }
    table='douyin'
    # keys = data.keys()
    keys=','.join(data.keys())
    # values1 = ','.join(data.values())
    values1=','.join(['%s']*len(data))
    # values1=data.values()
    # print(len(data))
    # print(table)
    #
    # print(len(data.values()))
    # print(data['manager_id'])
    # res_insert = insert_sql("insert into douyin (id,manager_id,account,uid,nickname,avatar,`desc`,praise,awemes,like_count,fan_count,with_shop,dou,balance,origin_uid,buyin_status,buyin_token,buyin_data,buyin_token_at,token,token_at,open_douyin_id,room_id,dou_monitor,live_monitor,`type`,sort,edition_id,auto_record,auto_record_at,expired_at,off_at,last_auth_at,is_first,qc_source,`exception`,created_at,updated_at,deleted_at) values (id,manager_id,'mianchaokeji','1754443783083283','飞瓜智投运营号','https://p9.douyinpic.com/img/tos-cn-avt-0015/ed0098a80d03dd93d60cc8e2a1e042a0~c5_300x300.jpeg?from=2956013662','飞瓜数据旗下飞瓜智投?\n飞瓜智投是专业的运营工具\n覆盖电商直播现场运营、投放监控、播后复盘\n助力精细化运营','0.00','32','188','1244','0','0','0',NULL,'4','','','2021-06-08 14:06:41',NULL,NULL,'0','0','0','1','0','2134','-1','-1','2021-11-05 18:25:41',NULL,NULL,'2021-05-24 14:06:41','0','0','0','2021-05-20 16:30:58','2021-11-05 18:25:41','2021-05-24 14:08:11')")
    sql = 'insert into {table}({keys}) values ({values})'.format(table=table,keys=keys,values=values1)
    # update = ','.join(["{key}=%s".format(key=key) for  key in data])
    # sql+= update
    print(sql)
    cur = conn.cursor()
    try:
        # cur.execute(sql,tuple(data.values())*2)
        cur.execute(sql,tuple(data.values()))
        conn.commit()
    except Exception as e:
        print("操作异常:%s" % str(e))
        conn.rollback()
    finally:
        conn.close()

    # res_insert = insert_sql(sql,tuple(data.values())*2)
#
#


test_add_douyin()
