'''
File    :   最大公约数最小公倍数函数.py
Time    :   2023/02/23 21:46:17
Author  :   Z-JUNYE 
Version :   1.0
Comment :   最大公约数最小公倍数用函数实现
'''

def gcd(x,y):
    '''求最大公约数'''
    (x,y) = (y,x) if x > y else (x,y)
    for i in range(x,0,-1):
        print(i)
        if x % i == 0 and y % i == 0:
            return i
            break

def lcm(x,y):
    '''求最小公倍数'''
    return x * y // gcd(x,y)


print(gcd(24,18))
print(lcm(24,18))