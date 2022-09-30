#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

from flask import Flask


app = Flask(__name__)

# 路由解析，通过用户访问的路径，匹配相应的函数
@app.route('/')
def hello_world():
    return "hello world!"


if __name__ == '__main__':
    app.run()
  