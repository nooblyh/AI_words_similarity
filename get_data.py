#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import re

def get_data():
    # 打开数据库连接
    db = MySQLdb.connect("222.200.184.74", "ai_user", "123456", "ai_all_data", charset='utf8')

    # 使用cursor()方法获取操作游标 
    cursor = db.cursor()
    text=[]
    sql = "SELECT * FROM AI_Academic_2019"
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        ctx=row[2]
        ctx=ctx.strip()
        ctx=re.sub("[\.\!\/_,$%^*(+\"\']+|[+——！，。?？、~@·#￥%……&*（：）\)-]+", " ",ctx)
        ctx=ctx.split()
        text.append(ctx)

    # 关闭数据库连接
    db.close()
    return text;