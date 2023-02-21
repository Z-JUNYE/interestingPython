'''
File    :   判断素数.py
Time    :   2023/02/21 14:37:27
Author  :   Z-JUNYE 
Version :   1.0
'''

import math
num = int(input('input a number: '))
numSqrt = int(math.sqrt(num))
isPrime = True

if num < 2:
    print('not prime')
else:
    for i in range(2,numSqrt+1):
        if num % i == 0:
            isPrime = False
            break

if isPrime:
    print('prime')
else:
    print('not prime')
