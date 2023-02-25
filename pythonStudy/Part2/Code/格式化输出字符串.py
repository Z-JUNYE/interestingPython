'''
File    :   格式化输出字符串.py
Time    :   2023/02/25 13:07:47
Author  :   Z-JUNYE 
Version :   1.0
Comment :   格式化输出字符串
'''

a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')