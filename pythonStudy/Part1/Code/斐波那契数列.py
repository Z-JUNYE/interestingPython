'''
File    :   斐波那契数列.py
Time    :   2023/02/23 13:16:57
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
斐波那契数列：数列从1，1开始，第三个数开始每个数都是前面两个数的和
'''

fList = [1,1]
for i in range(2,20):
    numi = fList[i-2]+fList[i-1]
    fList.append(numi)

print(fList)

