'''
File    :   斐波那契数列.py
Time    :   2023/02/25 15:14:35
Author  :   Z-JUNYE 
Version :   1.0
Comment :   
'''

def fib(n):
    a,b = 0, 1
    for i in range(n):
        a,b = b, a+b
        yield a

def main():
    for val in fib(20):
        print(val)

if __name__ == '__main__':
    main()