'''
File    :   三角形图案.py
Time    :   2023/02/21 20:24:10
Author  :   Z-JUNYE 
Version :   1.0
'''

row = int(input('input row count :' ))
'''
for i in range(row+1):
    print('*' * i)
'''

for i in range(row):
    for j in range(i+1):
        print('*', end = '')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()

for i in range(row):
    for j in range(row-i-1):
        print(' ', end = '')
    for j in range(2 * i +1):
        print('*', end = '')
    print()
