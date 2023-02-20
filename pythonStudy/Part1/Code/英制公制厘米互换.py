'''
File    :   英制公制厘米互换.py
Time    :   2023/02/20 22:08:26
Author  :   Z-JUNYE 
Version :   1.0
'''

value = float(input('input value : '))
unit = input('input unit : ')
if unit == 'in' or unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or unit == '厘米':
    print('%f厘米= %f英寸' % (value, value / 2.54))
else:
    print('please input valid unit')