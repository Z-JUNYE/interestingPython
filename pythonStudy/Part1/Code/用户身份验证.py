'''
File    :   用户身份验证.py
Time    :   2023/02/20 21:31:13
Author  :   Z-JUNYE 
Version :   1.0
'''

username = input('input username: ')
passWD = input('input password: ')
if username == 'admin' and passWD == '123456':
    print('验证成功')
else:
    print('验证失败')