#!/usr/bin/env python
# -*- coding: utf-8 -*-
#@Author : Aixiu


"""
内容回顾：
    1、函数可以做为参数进行传道
    2、 函数可以作为返回值进行返回
    3、函数名称可以当时变量一样可以赋值操作
    
装备器： -> 要求记住最后的结论
    装饰器本质上是一个闭包
    作用：
        在不改变原有函数调用的情况下，给函数增加新的功能。
        直白：可以在原函数前后添加新功能，但是不改原来的代码。
        
    在用户登录的地方，日志等。
    
    通用装饰器的写法：
        def wrapper(fn):  wrapper: 装饰器， fn: 目标函数
            def inner(*args, **kwargs):
                # 在目标函数执行之前....
                ret = fn(*args, **kwargs) # 执行目标函数（原函数）
                # 在目标函数执行之后....
                return ret
            return inner  # 返回函数名，别加小括号()
            
        @wrapper
        def target():
            pass
            
        target() => inner()
        
    一个函数可以被多个装饰器装饰
    
    @wrapper1 
    @wrapper2
    def target():
        print('我是目标')
        
    规则和规律： wrapper1 wrapper2 target wrapper2 wrapper1
"""

# 1、函数可以做为参数传递
# def func():
#     print('我是函数')
    
# def ggg(fn): # fn要求是个函数
#     fn()   # func()

# ggg(func)


# 2、 函数可以作为返回值进行返回
# def func():
#     def inner():
#         print('123')
#     return inner

# ret = func()
# ret()


# 3、函数名称可以当时变量一样可以赋值操作
# def func1():
#     print('我是函数1')
    
# def func2():
#     print('我是函数2')
    
# func1 = func2

# func1()


#装饰器

# def guanjia(game):
#     def inner():
#         print('打开外挂')
#         game()   # 玩起来了, game就是之前的未经封装的原函数，并存储在这
#         print('关闭外挂')
#     return inner

# @guanjia   # 相当于 play_dnf = guanjia(play_dnf)
# def play_dnf():
#     print('你好啊，我是超级赛亚人，今天是美好的一天')

# @guanjia
# def play_lol():
#     print('德玛西亚！！！！')
 
# # play_dnf = guanjia(play_dnf)  # 让管家把dnf游戏重新封装一遍，我这边把原来的游戏替换了
# # play_lol = guanjia(play_lol)  # 让管家把dnf游戏重新封装一遍，

# play_dnf() # 此时运行的是管家给的内层函数 inner
# play_lol() # 此时运行的是管家给的内层函数 inner



#装饰器详解

# def guanjia(game):
#     #  inner里的 *和** 表示接收所有参数，打包成元组和字典
#     def inner(*args, **kwargs):  # inner 添加了参数，args 一定是元组， kwargs 一定是字典
#         print('打开外挂')
#         #  game里的 *和** 表示把inner传过来的 args元组和 kwargs 字典打散成位置参数及关键字参数传递进去
#         game(*args, **kwargs)   # 玩起来了, game就是之前的未经封装的原函数，并存储在这
#         print('关闭外挂')
#     return inner

# @guanjia   # play_dnf = guanjia(play_dnf)
# def play_dnf(username, password):
#     print('我要开始玩dnf了。', username, password)
#     print('你好啊，我是超级赛亚人，今天是美好的一天')

# @guanjia
# def play_lol(username, password, hero):
#     print('我要开始玩lol了。', username, password, hero)
#     print('德玛西亚！！！！')
 


# play_dnf('admin', '123456')   # inner
# play_lol("admin", '456789', "大盖伦")



#装饰器的返回值

# def guanjia(game):
#     #  inner里的 *和** 表示接收所有参数，打包成元组和字典
#     def inner(*args, **kwargs):  # inner 添加了参数，args 一定是元组， kwargs 一定是字典
#         print('打开外挂')
#         #  game里的 *和** 表示把inner传过来的 args元组和 kwargs 字典打散成位置参数及关键字参数传递进去
#         # game(*args, **kwargs)   # 玩起来了, game就是之前的未经封装的原函数，并存储在这,这个地方可以从原函数拿到返回值的，需用一个变量接收一下  即：ret = game(*args, **kwargs)
#         ret = game(*args, **kwargs)
#         return ret
#         print('关闭外挂')
#     return inner

# @guanjia   # play_dnf = guanjia(play_dnf)
# def play_dnf(username, password):
#     print('我要开始玩dnf了。', username, password)
#     print('你好啊，我是超级赛亚人，今天是美好的一天')
#     return '一把屠龙刀'

# @guanjia
# def play_lol(username, password, hero):
#     print('我要开始玩lol了。', username, password, hero)
#     print('德玛西亚！！！！')
 


# ret = play_dnf('admin', '123456')   # inner
# print(ret)



#函数被多个装饰器装饰

def wrapper1(fn):  # fn: wrapper2.inner
    def inner(*args, **kwargs):
        print('这里是wrapper1 进入')    # 1运行
        ret = fn(*args, **kwargs)  # wrapper2.inner
        print('这里是wrapper1 出去')  # 5运行
        return ret
    return inner
    
def wrapper2(fn):   # fn: target
    def inner(*args, **kwargs):
        print('这里是wrapper2 进入')  # 2运行
        ret = fn(*args, **kwargs)  # target
        print('这里是wrapper2 出去')  # 4运行
        return ret
    return inner

@wrapper1  # target = wrapper1( wrapper2.inner)  => target: wrapper1.inner
@wrapper2  # 谁离目标函数近谁先运行    target = wrapper2(target)  => target: wrapper2.inner
def target():
    print('我是目标')  # 3运行
    
target()

"""
运行顺序直白：
    wrapper1 wrapper2 target wrapper2 wrapper1
这里是wrapper1 进入
这里是wrapper2 进入
我是目标
这里是wrapper2 出去
这里是wrapper1 出去
"""