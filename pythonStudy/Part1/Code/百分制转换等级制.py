'''
File    :   百分制转换等级制.py
Time    :   2023/02/20 22:12:54
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
如果成绩大于等于90分，等级A
如果成绩大于等于80小于90，等级B
如果成绩大于等于70小于80，等级C
如果成绩大于等于60小于70，等级D
如果成绩小于60，等级E
'''
score = float(input('input score :'))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'

print('Grade is:', grade)