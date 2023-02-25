'''
File    :   集合添加删除元素.py
Time    :   2023/02/25 15:43:00
Author  :   Z-JUNYE 
Version :   1.0
Comment :   向集合添加元素和删除元素
'''

set1 = {1,2,3,4,5}
set1.add(7)
set1.add(10)
set1.update([11,12])
set1.discard(5)
print(set1) #{1, 2, 3, 4, 7, 10, 11, 12}
if 4 in set1:
    set1.remove(4)
print(set1) #{1, 2, 3, 7, 10, 11, 12}
set1.pop()
print(set1) #{2, 3, 7, 10, 11, 12}

