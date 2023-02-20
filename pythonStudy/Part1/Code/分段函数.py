'''
File    :   分段函数.py
Time    :   2023/02/20 21:55:25
Author  :   Z-JUNYE 
Version :   1.0
'''

x = float(input('input value of x : '))
if x > 1:
    y = x * 3 - 5
elif x < -1:
    y = x * 5 +3
else:
    y = x + 2
print('f(%.2f) = %.2f' % (x, y))
