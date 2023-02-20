'''
File    :   分段函数2.py
Time    :   2023/02/20 22:05:24
Author  :   Z-JUNYE 
Version :   1.0
'''

x = float(input('input value of x: '))
if x > 1:
    y = x * 3 - 5
else:
    if x < -1:
        y = 5 * x + 3
    else:
        y = x + 2
print('f(%.2f) = %.2f' % (x, y))