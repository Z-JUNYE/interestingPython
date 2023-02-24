'''
File    :   字符串运算符.py
Time    :   2023/02/24 22:14:09
Author  :   Z-JUNYE 
Version :   1.0
Comment :   字符串运算符
'''
s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' in s1)

str2 = 'abc123456'
print(str2[2])
print(str2[2:5])
print(str2[2:])
print(str2[2::2])
print(str2[::2])
print(str2[::-1])
print(str2[-3:-1])



