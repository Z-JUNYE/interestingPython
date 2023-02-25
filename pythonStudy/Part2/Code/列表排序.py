'''
File    :   列表排序.py
Time    :   2023/02/25 14:48:17
Author  :   Z-JUNYE 
Version :   1.0
Comment :   列表排序
'''

list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
list2 = sorted(list1)
print(list2) #['apple', 'blueberry', 'internationalization', 'orange', 'zoo']
#sorted函数返回list排序后的copy，并不会对原list产生影响
#函数的设计就应该向sorted一样尽可能不产生副作用
list3 = sorted(list1, reverse = True)
#通过关键字参数指定排序
list4 = sorted(list1, key = len)
print(list3) #['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
print(list4) #['zoo', 'apple', 'orange', 'blueberry', 'internationalization']
#给list对象发出排序消息直接在list中进行排序
list1.sort(reverse=True)
print(list1) #['zoo', 'orange', 'internationalization', 'blueberry', 'apple']
