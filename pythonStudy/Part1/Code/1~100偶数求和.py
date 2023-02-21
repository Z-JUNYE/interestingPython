'''
File    :   1~100偶数求和.py
Time    :   2023/02/21 14:03:09
Author  :   Z-JUNYE 
Version :   1.0
'''

sum = 0
for i in range(0,101,2):
    sum += i
print(sum)

sum = 0
for i in range(0,101):
    if i % 2 == 0:
        sum += i
print(sum)
