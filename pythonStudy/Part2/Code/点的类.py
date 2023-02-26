'''
File    :   点的类.py
Time    :   2023/02/26 22:11:09
Author  :   Z-JUNYE 
Version :   1.0
Comment :   定义点的类并提供计算两点距离的方法
'''

class Point(object):

    def __init__(self, x = 0, y = 0):
        '''
        初始化方法
        :param x
        :param y
        '''
        self.x = x
        self.y = y
    
    def moveTo(self, x, y):
        '''
        移动到指定位置
        :param x
        :param y
        '''
        self.x = x
        self.y = y
    
    def moveBy(self, dx, dy):
        '''
        移动指定的增量
        :param dx
        :param dy
        '''
        self.x += dx
        self.y += dy
    
    def distanceBet(self, otherPoint):
        '''
        计算两点间的距离
        '''
        dx = self.x - otherPoint.x
        dy = self.y - otherPoint.y
        return (dx**2+dy**2)**0.5
    
    def __str__(self):
        return f'{str(self.x)}, {str(self.y)}'

def main():
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.moveBy(-1,2)
    print(p2)
    print(p1.distanceBet(p2))

if __name__ == '__main__':
    main()
