'''
File    :   九九乘法表.py
Time    :   2023/02/21 14:34:56
Author  :   Z-JUNYE 
Version :   1.0
'''

for i in range(1,10):
    for j in range(1,i + 1):
        print('%d * %d = %d' % (i, j, i * j), end = '\t')
    print()