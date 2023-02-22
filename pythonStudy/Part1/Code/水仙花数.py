'''
File    :   水仙花数.py
Time    :   2023/02/22 19:09:25
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
水仙花数：它是一个三位数，该数字每个位上数字的立方之和等于它本身
'''
for num in range(100,1000):
    if (num // 100)**3+(num // 10 % 10)**3+(num % 10)**3 == num:
        print(num)
