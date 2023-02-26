'''
File    :   定义一个类描述时钟.py
Time    :   2023/02/26 22:00:39
Author  :   Z-JUNYE 
Version :   1.0
Comment :   数字时钟
'''

from time import sleep

class Clock(object):
    '''数字时钟'''
    def __init__(self, hour = 0, minute = 0, second = 0):
        '''
        初始化方法
        :param hour
        :param minute
        :param second
        '''
        self._hour = hour
        self._minute = minute
        self._second = second
    
    def run(self):
        '''时钟走字'''
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
            if self._minute == 60:
                self._minute = 0
                self._hour += 1
                if self._hour == 24:
                    self._hour = 0
    
    def show(self):
        '''显示时间'''
        return f'{self._hour}:{self._minute}:{self._second}'
    
def main():
    clock = Clock(23,58,50)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()
    
if __name__ == '__main__':
    main()