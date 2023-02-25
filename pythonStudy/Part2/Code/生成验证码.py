'''
File    :   生成验证码.py
Time    :   2023/02/25 20:24:00
Author  :   Z-JUNYE 
Version :   1.0
Comment :   生成验证码
'''

import random

def generateCode(codeLength = 4):
    '''
    生成指定长度的验证码
    codelength 验证码长度，默认为4
    '''
    allChars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    allCharsLength = len(allChars)-1
    for i in range(codeLength):
        index = random.randint(0, allCharsLength)
        code += allChars[index]
    return code

print(generateCode(6))