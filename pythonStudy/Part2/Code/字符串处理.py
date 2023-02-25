'''
File    :   字符串处理.py
Time    :   2023/02/25 12:41:33
Author  :   Z-JUNYE 
Version :   1.0
Comment :   字符串处理
'''

str1 = 'hello, world!'
#计算字符串长度
print(len(str1)) # 13
#获得字符串首字母大写的copy
print(str1.capitalize()) #Hello, world!
#获得字符串每个单词首字母大写的copy
print(str1.title()) #Hello, World!
#获得字符串大写的copy
print(str1.upper()) #HELLO, WORLD!
#从字符串中查找子串的为止
print(str1.find('or')) # 8
print(str1.find('shit')) # -1
#index也可以用来查找，但会引发异常一旦找不到子串
#print(str1.index('or'))
#print(str1.index('shit'))
#检查字符串是否以指定子串开头
print(str1.startswith('he')) # False
print(str1.startswith('hel')) # True
#检查字符串是否以指定的子串结尾
print(str1.endswith('!')) # True
#将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*')) 
# ******************hello, world!*******************
#将字符串以指定的宽度靠右放置并在左侧填充指定的字符
print(str1.rjust(50,'*'))
# *************************************hello, world!
#检查字符串是否由数字构成
str2 = '123abc'
print(str2.isdigit()) # False
#检查字符串是否由字母构成
print(str2.isalpha()) # False
#检查字符串是否由数字和字母组成
print(str2.isalnum()) # True
str3 = '    scarzjy@gmail.com  '
print(str3) #     scarzjy@gmail.com
# 获得字符串修剪左右空格之后的copy
print(str3.strip()) # scarzjy@gmail.com
