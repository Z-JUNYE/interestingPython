'''
File    :   正整数翻转.py
Time    :   2023/02/22 19:18:59
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
12345
得到1234和5， 生成5
得到123和4，生成54
得到12和3，生成543
得到1和2，生成5432
得到1，生成54321
'''

num = int(input('input a number :'))
revNumber = 0
while num != 0:
    revNumber  = revNumber * 10 + num % 10
    num = num // 10

print(revNumber)