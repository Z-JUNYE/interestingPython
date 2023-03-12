'''
File    :   正则表达式1.py
Time    :   2023/03/12 20:36:26
Author  :   Z-JUNYE 
Version :   1.0
Comment :   验证输入用户名和QQ号是否有效并给出对应的提示信息。
'''

'''
要求：
用户名必须由字母、数字或下划线构成且长度在6~20字符之间
QQ号必须是5~12位的数字且首位不为0
'''

import re

def main():
    unsername = input('input username:')
    qq = input('input qq number:')

    m1 = re.match(r'^[0-9a-zA-Z]{6,20}$', unsername)
    if not m1:
        print('请输入正确用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效QQ')
    if m1 and m2:
        print('输入信息有效')

if __name__ == '__main__':
    main()