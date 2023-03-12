'''
File    :   正则表达式2.py
Time    :   2023/03/12 20:42:29
Author  :   Z-JUNYE 
Version :   1.0
Comment :   从一段文字中提取出国内的手机号码
'''

import re

def main():
    pattern = re.compile(r'(?<=\D)1[34578]\d{9}(?=\D)')
    sentence = 