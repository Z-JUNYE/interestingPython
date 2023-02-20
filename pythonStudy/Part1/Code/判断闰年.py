'''
File    :   判断闰年.py
Time    :   2023/02/20 21:12:07
Author  :   Z-JUNYE 
Version :   1.0
'''

year = int(input('input year: '))
isLeap = year%4 == 0 and year % 100 != 0 or year % 400 == 0
print(isLeap)