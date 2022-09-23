#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
宠物系统主程序
"""

from pet_tools import *

def main():
    while True:
        # 1.显示系统菜单        
        show_menu()

        # 2.根据用户输入，调用不同的功能（函数）
        action = input("请选择希望执行的操作： ")
        if action in ["1", "2", "3"]:
            if action == "1":
                # TODO(4815563@qq.com) 1.新增宠物信息
                new_pet()
            elif action == "2":
                # TODO 2.显示全部信息
                show_all()
            elif action == "3":
                # TODO 3.搜索宠物信息
                search_pet()
        elif action == "0":
            print("欢迎再次使用【宠物信息管理系统】")
            break
        else:
            print("您输入的不正确请重新选择")

        # 3.不断的执行上述操作（循环）
    
if __name__ == '__main__':
    main()
