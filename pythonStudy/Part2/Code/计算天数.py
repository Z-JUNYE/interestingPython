'''
File    :   计算天数.py
Time    :   2023/02/25 20:47:01
Author  :   Z-JUNYE 
Version :   1.0
Comment :   输入年月日，计算这是当年的第几天
'''

def isLeapYear(year):
    '''
    判断是否是闰年
    '''
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def whichDay(year, month, day):
    '''
    判断是第几天
    :param year
    :param month
    :param day
    :return : which day
    '''
    daysOfMonth = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][isLeapYear(year)]
    total = 0
    for index in range(month - 1):
        total += daysOfMonth[index]
    total += day
    return total
