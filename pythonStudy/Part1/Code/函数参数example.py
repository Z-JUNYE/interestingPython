'''
File    :   函数参数example.py
Time    :   2023/02/23 21:15:49
Author  :   Z-JUNYE 
Version :   1.0
Comment :   函数参数的默认值
'''

from random import randint

def rollDice(n=2):
    '''摇色子'''
    sumDice = 0
    for i in range(n):
        sumDice += randint(1,6)
    return sumDice

def add(a=0, b=0, c=0):
    '''三个数相加'''
    return a+b+c

print(rollDice())
print(rollDice(3))
print(add())
print(add(1))
print(add(1,2))
print(add(1,2,3))
