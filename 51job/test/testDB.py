#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

import sqlite3

dbpath = "./51job.db"


def init_db(dbpath):
    # id表示属性名  integer表示属性类型  primary key表示这个属性是主键  autoincrement表示这个值是自动增加的， 默认开始值是1
    sql = '''
        create table job
        (
            id integer primary key autoincrement,  
            job_link text,
            jname text,
            cname varchar,
            area varchar,
            salary text,
            educate text,
            info text
            
        )
    '''  # 创建数据表
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()
    
# init_db(dbpath)

# 保存数据到 SQLITE数据库
def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()
    
    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index ==5:
                continue
            data[index] = '"'+data[index]+'"'  # 给每一条数据加上双引号
        sql = '''
            insert into movie250 (info_link, pic_link, cname, ename, score, rated, instroduction, info)
            values(%s)
        '''%",".join(data)
        
        print(sql)
            
        cur.execute(sql)   # 执行上边的语句
        conn.commit()  # 提交数据
    cur.close()
    conn.close()