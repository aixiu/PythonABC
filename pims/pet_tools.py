#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu

"""
这是宠物信息管理系统的工具程序
"""

pets_info = []  # 用来保存宠物信息
# 测试数据
# pets_info = [{'nickname': '豆豆', 'age': '2', 'sex': '雄性', 'weight': '12'}]  # 用来保存宠物信息

# pets_info = [{'nickname': '豆豆', 'age': '2', 'sex': '雄性', 'weight': '12'}, 
            #  {'nickname': '憨憨', 'age': '3', 'sex': '雌性', 'weight': '15'}]  # 用来保存宠物信息

header = ["昵称", "年龄", "性别", "体重"]

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
    # 1.提示用户输入宠物信息
    print()
    print("新增宠物信息".center(23, "="))
    nickname = input("请输入昵称： ")
    age = input("请输入年龄： ")
    sex = input("请输入性别（雄性/雌性）： ")
    weight = input("请输入体重（kg）： ")
    
    # 2.将输入的信息，保存为一个字典
    pet = {"nickname": nickname, "age": age, "sex": sex, "weight": weight}
    # {'nickname': '豆豆', 'age': '2', 'sex': '雄性', 'weight': '12'}
    # print(pet)
    
    # 3.将宠物信息的字典追加到列表中
    pets_info.append(pet)
    # print(pets_info)
    
    # 4.提示用户添加成功
    print(f"【添加 {nickname} 成功！】")
    
def show_all():
    """
    显示全部宠物信息
    """
    print()
    print("显示全部宠物信息".center(23, "="))
    
    # 判断宠物信息列表中是否为空
    if len(pets_info) == 0:
        print("【当前没有任何的宠物信息记录，请使用新增功能添加宠物信息！】")
        return
    # 打印表头
    for title in header:
        print(title, end="\t")
    print()
    print("-" * 31)
    # 逐一打印列表中的每个宠物信息
    for pet in pets_info:
        # print(f"{pet['nickname']}\t{pet['age']}\t{pet['sex']}\t{pet['weight']}")
        for value in pet.values():
            print(f"{value}", end="\t")
        print()

def deal_pet(find_pet):
    """
    处理查找到的宠物信息

    :param find_pet: 查找到的宠物信息
    """
    print()
    action = input("请选择要执行的操作：[1] 修改 [2] 删除 [3] 返回上级菜单 ")
    if action == "1":
        # 执行修改操作
        # find_pet["nickname"] = input("新的昵称： ")
        # find_pet["age"] = input("新的年龄： ")
        # find_pet["sex"] = input("新的性别（雄性/雌性）： ")
        # find_pet["weight"] = input("新的体重（kg）： ")
        find_pet["nickname"] = input_pet_info(find_pet["nickname"], "新的昵称：[回车不修改] ")
        find_pet["age"] = input_pet_info(find_pet["age"], "新的年龄：[回车不修改] ")
        find_pet["sex"] = input_pet_info(find_pet["sex"], "新的性别（雄性/雌性）：[回车不修改] ")
        find_pet["weight"] = input_pet_info(find_pet["weight"],"新的体重（kg）：[回车不修改] ")
        print(f"【修改{find_pet['nickname']}宠物信息成功】")
    elif action == "2":
        # 执行删除操作
        pets_info.remove(find_pet)
        print(f"【删除{find_pet['nickname']}宠物信息成功】")
        
def input_pet_info(pet_value, tip):
    """
    输入宠物信息的功能扩展

    :param pet_value: 字典中原有的值
    :param tip: 输入的提示文字内容
    :return: 如果用户输入了内容，就返回新的内容，否则返回字典中原有的值
    """
    # 1.提示用户输入信息
    result = input(tip)
    # 2.用户输入的内容不为空，返回输入的值
    if len(result) > 0:
        return result
    # 3.如果用户输入的为空，返回宏物信息原有的值
    else:
        return pet_value

def search_pet():
    """
    搜索宠物信息
    """
    print()
    print("搜索宠物信息".center(23, "="))
    
    # 1.引导用户输入要搜索的宠物昵称
    find_name = input("请输入要搜索的宠物昵称： ")
    
    # 2.在宠物信息列表中查找对应昵称的宠物信息
    for pet in pets_info:
        # 3.如果找到了，就打印输出列表
        if pet["nickname"] == find_name:
            # 打印表头
            print()
            for title in header:
                print(title, end="\t")
            print()
            print("-" * 29)
            
            # 打印宠物的详细信息
            for value in pet.values():
                print(f"{value}", end="\t")
            print()
            # 提示用户对于找到的信息，进行操作选择
            deal_pet(pet)
            break
     # 4.如果没找到，就打印输出提示信息
    else:
        print(f"抱歉，没有找到叫{find_name}的宠物")
    
    
if __name__ == '__main__':
    # show_menu()
    # new_pet()
    # show_all()
    search_pet()
