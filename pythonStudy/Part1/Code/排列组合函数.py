'''
File    :   排列组合函数.py
Time    :   2023/02/23 21:03:59
Author  :   Z-JUNYE 
Version :   1.0
Comment :  用函数来计算C(M,N) 
'''

def fac(num):
    '''求阶乘'''
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

M = int(input('input number M : '))
N = int(input('input number N : '))

print(fac(M) / fac(N) / fac(M-N)
