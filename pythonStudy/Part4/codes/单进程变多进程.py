'''
File    :   单进程变多进程.py
Time    :   2023/03/12 21:07:00
Author  :   Z-JUNYE 
Version :   1.0
Comment :   
'''

from multiprocessing import Process
from os import getpid
from random import randint
from time import time, sleep

def download_task(filename):
    print('开始下载%s...' % filename)
    time_to_download = randint(5,10)
    sleep(time_to_download)
    print('%s下载完成，耗时%d秒' % (filename,time_to_download))

def main():
    start = time()
    
    p1 = Process(target = download_task, args = ('python.pdf',))
    p1.start()
    p2 = Process(target = download_task, args = ('peking_hot/avi',))
    p2.start()
    p1.join()
    p2.join()

    end = time()
    print('耗时%.2f秒' % (end - start))

if __name__ == '__main__':
    main()