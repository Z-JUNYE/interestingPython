'''
File    :   列表定义列表遍历列表下标运算.py
Time    :   2023/02/25 14:03:40
Author  :   Z-JUNYE 
Version :   1.0
Comment :   列表
'''
list1 = [1, 3, 5, 7, 100]
print(list1) # [1, 3, 5, 7, 100]

list2 = ["hello"] * 3
print(list2) # ['hello', 'hello', 'hello']
# len函数计算list的元素个数
print(len(list1)) # 5
# 下标\索引运算
print(list1[0]) # 1
print(list1[-1]) # 100

list1[2] = 200
print(list1) # [1, 3, 200, 7, 100]
#通过循环用下标遍历列表元素
for index in range(len(list1)):
    print(list1[index])
'''
1
3
200
7
'''
#通过循环遍历列表
for elem in list1:
    print(elem)

#通过enumerate函数处理列表后再遍历可以同时获得元素索引和值
for index, elem in enumerate(list1):
    print(index, elem)
'''
0 1
1 3
2 200
3 7
4 100
'''