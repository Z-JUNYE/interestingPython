'''
File    :   三角形周长和面积.py
Time    :   2023/02/20 22:16:35
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
海伦公式
S = (p(p-a)(p-b)(p-c))**0.5
p = (a+b+c)/2
'''

a = float(input('input length of first side of the triangle: '))
b = float(input('input length of second side of the triangle: '))
c = float(input('input length of third side of the triangle: '))

if a + b > c and a + c > b and b + c > a:
    p = (a + b + c)/2
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print('perimeter is %f' % (a + b + c))
    print('area is %f' % area)
else:
    print('input can not form a triangle')