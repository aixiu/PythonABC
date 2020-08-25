#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 根据用户输入的数值及运算符，运算结果。用空格隔开，如：6 * 7
num1, operator, num2 = input('Enter calculation: ').split()

num1 = int(num1)
num2 = int(num2)

if operator == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operator == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operator == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif operator == '/':
    print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('Use either + - * or / next time')


a = 0
for i in range(101):
    a += i
print(a)