'''
File    :   类方法.py
Time    :   2023/02/28 20:44:53
Author  :   Z-JUNYE 
Version :   1.0
Comment :   类方法
'''

from time import time, localtime, sleep

class Clock(object):
    '''数字时钟'''
    def __init__(self, hour = 0, minute = 0, second = 0):
        self._hour = hour
        self._minute = minute
        self._second = second
    
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
    
    def run(self):
        '''走字'''
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
    clock = Clock.now()
    while True:
        print(clock.show())
        sleep(0.5)
        print(Clock.show(clock))
        sleep(0.5)
        clock.run()

if __name__ ==  '__main__':
    main()



