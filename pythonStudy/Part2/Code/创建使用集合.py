'''
File    :   创建使用集合.py
Time    :   2023/02/25 15:39:47
Author  :   Z-JUNYE 
Version :   1.0
Comment :   创建使用集合
'''

set1 = {1,2,3,3,3,4}
print(set1) #{1, 2, 3, 4}
print('length =', len(set1)) #4
#创建集合的构造器语法
set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))
print(set2, set3) #{1, 2, 3, 4, 5, 6, 7, 8, 9} {1, 2, 3}
#创建集合的推导式语法
set4 = {num for num in range(1,100) if num % 3 == 0 and num % 5 == 0}
print(set4) # {75, 45, 15, 90, 60, 30}
