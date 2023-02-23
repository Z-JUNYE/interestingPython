'''
File    :   回文数函数.py
Time    :   2023/02/23 21:59:45
Author  :   Z-JUNYE 
Version :   1.0
Comment :   回文数
'''

def isPalindrome(num):
    '''判断是否回文数'''
    numOrign = num
    revNumber = 0
    while num != 0:
        revNumber  = revNumber * 10 + num % 10
        num = num // 10
    return revNumber == numOrign

print(isPalindrome(12321))

