#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from flask import Flask, render_template
import sqlite3
import os.path

app = Flask(__name__)

# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/index')
def index():
    # return render_template("index.html")
    return home()

@app.route('/movie')
def movie():
    '''
    注意：sqlite3.OperationalError: no such table: movie250
    大意是说，脚本正在打开并尝试连接另一个目录中的新数据库，该目录是空的，因此找不到表。所以访问数据库文件时应该使用绝对路径而不是相对路径。
    
    在python脚本的合适位置加上如下代码，问题得到解决：
    import os.path

    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "flaskr.db")
    
    更改后的连接数据库代码如下：
    
     return sqlite3.connect(db_path)
     
     源文：https://blog.csdn.net/weixin_43207777/article/details/105332134
    
    '''
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "movie.db")
    datalist = []
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html", moveis=datalist)

@app.route('/score')
def score():
    return render_template("score.html")

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")





if __name__ == '__main__':
    app.run()
