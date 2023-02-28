'''
File    :   静态方法.py
Time    :   2023/02/28 20:35:58
Author  :   Z-JUNYE 
Version :   1.0
Comment :   静态方法
'''

from math import sqrt

class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def isValid(a, b, c):
        return a + b > c and b + c > a and a + c > b
    
    def perimeter(self):
        return self._a + self._b + self._c
    
    def area(self):
        half = self.perimeter() / 2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用
    if Triangle.isValid(a,b,c):
        t = Triangle(a,b,c)
        print(t.perimeter())
        #也可以通过给类发消息来调用对象方法但是要传入接受消息的对象作为参数
        print(Triangle.perimeter(t))

        print(t.area())
        print(Triangle.area(t))

    else:
        print('can not form triangle')

if __name__ == '__main__':
    main()
