'''
File    :   修改全局变量.py
Time    :   2023/02/23 22:28:01
Author  :   Z-JUNYE 
Version :   1.0
Comment :   修改全局变量
'''

def foo():
    global a
    a = 200
    print(a)

if __name__ == '__main__':
    a = 100
    foo()
    print(a)

