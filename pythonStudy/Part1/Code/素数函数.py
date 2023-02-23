'''
File    :   素数函数.py
Time    :   2023/02/23 22:07:10
Author  :   Z-JUNYE 
Version :   1.0
Comment :   判断素数函数
'''

def primeJuedge(num):
    isPrime = True
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            isPrime = False
            break
    return isPrime if num > 1 else False

