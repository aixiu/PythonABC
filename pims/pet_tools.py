#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
这是宠物信息管理系统的工具程序
"""

def show_menu():
    """
    显示系统菜单
    """
    print()
    print("宠物信息管理系统v1.0".center(25, "*"))
    print()
    print("1.新增宠物信息")
    print("2.显示全部宠物信息")
    print("3.搜索宠物信息")
    print()
    print("0.退出系统")
    print()
    print("*" * 33)   
    print()
    
def new_pet():
    """
    新增宠物信息
    """
    print("新增宠物信息".center(23, "="))
    
def show_all():
    """
    显示全部宠物信息
    """
    print("显示全部宠物信息")
    
def search_pet():
    """
    搜索宠物信息
    """
    print("搜索宠物信息")
    
    
if __name__ == '__main__':
    # show_menu()
    new_pet()
