'''
File    :   生成式和生成器.py
Time    :   2023/02/25 15:02:14
Author  :   Z-JUNYE 
Version :   1.0
Comment :   生成式和生成器
'''
import sys
f = [x for x in range(1,10)]
print(f) #[1, 2, 3, 4, 5, 6, 7, 8, 9]
f = [ x+y for x in 'ABCDE' for y in '1234567']
print(f)
#['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7']
#用list的生成表达式语法创建列表容器
#用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
f = [x**2 for x in range(1,1000)]
print(sys.getsizeof(f)) #8856

#请注意下面的代码创建的不是一个列表而是一个生成器对象
#通过生成器可以获取到数据到它不占用额外的空间存储数据
#每次需要数据的时候就通过内部的运算得到数据（需要额外花费时间）
f = (x**2 for x in range(1,1000))
print(sys.getsizeof(f)) #112
for val in f:
    print(val)

