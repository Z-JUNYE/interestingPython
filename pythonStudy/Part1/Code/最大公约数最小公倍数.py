'''
File    :   最大公约数最小公倍数.py
Time    :   2023/02/21 20:08:29
Author  :   Z-JUNYE 
Version :   1.0
'''

x = int(input('input number x: '))
y = int(input('input number y: '))

if x > y:
    x, y = y, x
for factor in range(x,0,-1):
    if x % factor == 0  and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break
