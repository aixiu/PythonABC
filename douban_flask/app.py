#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from flask import Flask, render_template

app = Flask(__name__)

# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
