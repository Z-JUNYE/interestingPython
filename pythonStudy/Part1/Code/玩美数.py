'''
File    :   玩美数.py
Time    :   2023/02/23 13:34:25
Author  :   Z-JUNYE 
Version :   1.0
Comment :   完美数：它的所有真因子的和恰好是它本身
'''


def perfectNum(num):
    factorList = []
    for i in range(1, num):
        if num % i == 0:
            factorList.append(i)
    if sum(factorList) == num:
        return num

for i in range(1,10000):
    if perfectNum(i) != None:
        print(perfectNum(i))

