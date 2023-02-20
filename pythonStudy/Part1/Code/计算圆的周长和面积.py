'''
File    :   计算圆的周长和面积.py
Time    :   2023/02/20 21:08:39
Author  :   Z-JUNYE 
Version :   1.0
'''
import math
radius = float(input('input circle\'s radius: '))
perimeter = radius*2*math.pi
area = math.pi*radius**2
print('perimeter is : %.2f' % perimeter)
print('area is : %.2f' % area)