'''
File    :   排列组合..py
Time    :   2023/02/23 20:52:11
Author  :   Z-JUNYE 
Version :   1.0
Comment :   计算C(M,N)
'''

M = int(input('input number M : '))
N = int(input('input number N : '))

fM = 1
for i in range(1, M+1):
    fM *= i

fN = 1
for i in range(1, N+1):
    fN *= i

fM_N = 1
for i in range(1, M-N+1):
    fM_N *= i

print(fM / fN / fM_N)