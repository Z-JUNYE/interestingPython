'''
File    :   猜数字.py
Time    :   2023/02/21 14:19:10
Author  :   Z-JUNYE 
Version :   1.0
'''

import random

counter = 0
answer = random.randint(1,100)
while True:
    counter += 1
    guess = int(input('input your guess: '))
    if guess > answer:
        print('too big')
    elif guess < answer:
        print('too small')
    else:
        print('bingo~')
        break