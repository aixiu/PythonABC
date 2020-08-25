#!/usr/bin/env python
# -*- coding: utf-8 -*-

print('Hello world!')

myName = input('what is your name? ')

print('It is good to meet you {}'.format(myName))
print(f'It is good to meet you {myName}')

print('The length of your name is {}'.format(len(myName)))
print(f'The length of your name is {len(myName)}')

print('what is your age?')

myAge = int(input('请输入你的年龄：'))
print('You wil be {}'.format(myAge + 1))
print(f'You wil be {myAge + 1}')

