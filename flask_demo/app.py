#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

# 路由解析，通过用户访问的路径，匹配相应的函数
# @app.route('/')
# def hello_world():
#     return "hello world!"

# debug模式开启

@app.route("/index")
def hello():
    return "你好"

# 通过访问路径，获取用户的字符串参数
@app.route("/user/<name>")
def welcom(name):
    return "你好,{}".format(name)

# 通过访问路径，获取用户的整型参数  此外还有 float类型
@app.route("/user/<int:id>")
def welcom2(id):
    return "你好,{}号的会员".format(id)

# 路由路径不能重复，用户只能通过唯一路访问特定的函数


# 返回给用户渲染网页文件
# @app.route("/")
# def index2():
#     return render_template("index.html")

# 向页面传递一个变量
@app.route("/")
def index2():
    time = datetime.date.today()  # 普通变量
    name = ["小张", "小王", "小赵"]  #列表类型
    task = {"任务": "打扫卫生", "时间": "3小时"}  #字典类型
    return render_template("index.html", var=time, list = name, task=task)


# 表达提交
@app.route("/test/register")
def register():
    return render_template("test/register.html")

# 接收表单提交的路由，需要指定 methonds 为 post
@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == "POST":
        result = request.form
        return render_template("test/result.html", result=result)
    else:
        return "不是POST请求"  # 可以不要，也可以是其它东西

if __name__ == 'main':
    app.run(debug=0)
