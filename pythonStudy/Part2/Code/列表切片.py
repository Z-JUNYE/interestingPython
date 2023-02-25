'''
File    :   列表切片.py
Time    :   2023/02/25 14:30:52
Author  :   Z-JUNYE 
Version :   1.0
Comment :   列表的切片
'''

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
#list切片
fruits2 = fruits[1:4]
print(fruits2) #['apple', 'strawberry', 'waxberry']
#可以通过完整切片来达到复制
fruits3 = fruits[:]
print(fruits3) #['grape', 'apple', 'strawberry', 'waxberry', 'pitaya', 'pear', 'mango']
fruits4 = fruits3[-3:-1]
print(fruits4) #['pitaya', 'pear']
#可以通过反向切片获得倒转后的列表的copy
fruits5 = fruits[::-1]
print(fruits5)
#['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']