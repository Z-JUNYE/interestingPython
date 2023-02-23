'''
File    :   变量作用域example.py
Time    :   2023/02/23 22:20:10
Author  :   Z-JUNYE 
Version :   1.0
Comment :   变量作用域example
'''

def foo():
    b = 'hello'

    # 函数内部嵌套函数
    def bar():
        c = True
        print(a)
        print(b)
        print(c)
    
    bar()

if __name__ == '__main__':
    a = 100
    foo()