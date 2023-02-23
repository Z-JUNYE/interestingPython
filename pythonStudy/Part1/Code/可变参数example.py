'''
File    :   可变参数example.py
Time    :   2023/02/23 21:21:51
Author  :   Z-JUNYE 
Version :   1.0
Comment :   可变参数example
'''

def add(*args):
    result = 0
    for i in args:
        result += i
    return result

print(add(1,2,3,4,5,6))
