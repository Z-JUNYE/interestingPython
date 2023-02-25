'''
File    :   集合的运算.py
Time    :   2023/02/25 19:59:56
Author  :   Z-JUNYE 
Version :   1.0
Comment :   集合的运算
'''

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}
print(set1 & set2) #{3, 4, 5}
print(set1.intersection(set2))
print(set1 | set2) #{1, 2, 3, 4, 5, 6, 7}
print(set1.union(set2))
print(set1 - set2) #{1, 2}
print(set1.difference(set2))
print(set1 ^ set2) #{1, 2, 6, 7}
print(set1.symmetric_difference(set2))
#判断子集和超集
print(set2 <= set1)
print(set1 >= set2)
