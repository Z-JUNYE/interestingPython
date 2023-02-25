'''
File    :   冒泡法.py
Time    :   2023/02/25 20:42:17
Author  :   Z-JUNYE 
Version :   1.0
Comment :   冒泡法
'''

def maxTwo(x):
    m1,m2 = (x[0],x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2

print(maxTwo([6,7,3,2,9,10]))


