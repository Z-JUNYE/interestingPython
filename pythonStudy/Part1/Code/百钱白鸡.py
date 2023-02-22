'''
File    :   百钱白鸡.py
Time    :   2023/02/22 22:13:31
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
公鸡5元一只，母鸡3元一只，小鸡一只3元，100元买100只鸡
'''

for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print('%d只公鸡 %d只母鸡 %d只小鸡' % (x, y, z))