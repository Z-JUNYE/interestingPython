'''
File    :   添加元素移除元素.py
Time    :   2023/02/25 14:13:07
Author  :   Z-JUNYE 
Version :   1.0
Comment :   添加元素和移除元素
'''

list1 = [1, 3, 5, 7, 100]
#添加元素
list1.append(200)
list1.insert(1,400)
#合并两个list
list1.extend([1000,2000])
# list1 += [1000,2000]
print(list1) #[1, 400, 3, 5, 7, 100, 200, 1000, 2000]
#判断元素是否存在后删除
if 3 in list1:
    list1.remove(3)
print(list1) #[1, 400, 5, 7, 100, 200, 1000, 2000]
#从指定位置删除
list1.pop(0)
list1.pop(len(list1)-1)
print(list1) #[400, 5, 7, 100, 200, 1000]
#清空list
list1.clear()
print(list1) #[]

