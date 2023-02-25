'''
File    :   屏幕显示跑马灯.py
Time    :   2023/02/25 20:19:09
Author  :   Z-JUNYE 
Version :   1.0
Comment :   屏幕显示跑马灯
'''

import os
import time

def main():
    content = 'abcdefg'
    while True:
        #清理屏幕上的输出
        os.system('cls')
        print(content)
        #休眠20毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()

