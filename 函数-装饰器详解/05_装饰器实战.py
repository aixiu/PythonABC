#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

login_flag = False    # 记录登录状态

def login_verify(fn):
    def inner(*args, **kwargs):
        global login_flag
        if login_flag == False:
            # 这里完成登录校验
            print('先登录后操作')
            while True:
                username = input('username >>> ')
                password = input('password >>> ')
                if username == 'admin' and password == '123':
                    print('登录成功')
                    login_flag = True
                    break
                else:
                    print('登录失败,用户名或密码错误')
        ret = fn(*args, **kwargs) #后续的程序执行
        return ret
    return inner

@login_verify
def add():
    print('添加员工信息')
    
def delete():
    print('删除员工信息')
    
def upd():
    print('修改员工信息')
    
def search():
    print('查询员工信息')
    
add()

upd()

delete()

search()