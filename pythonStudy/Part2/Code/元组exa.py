'''
File    :   元组exa.py
Time    :   2023/02/25 15:17:09
Author  :   Z-JUNYE 
Version :   1.0
Comment :   元组example
'''

t = ('zjy', 38, True, '晴天')
print(t) #('zjy', 38, True, '晴天')
#获取元组中的元素
print(t[0]) #zjy
print(t[3]) #晴天
#遍历元素
for member in t:
    print(member)
#重新给元组赋值会覆盖原来的元组，原来的元组被垃圾回收
#将元组转换成列表
list1 = list(t)
print(list1) #['zjy', 38, True, '晴天']
#将列表转换成元组
list1[0] = 'yjz'
t = tuple(list1)
print(t) #('yjz', 38, True, '晴天')
