## 语言元素
***
### 变量和类型
变量是一种存储数据的载体。计算机中的变量是实际存在的数据或者是存储器中存储数据的一块内存空间，变量的值可以被读取和修改，这是所有计算和控制的基础。
Python中的常用数据类型：
* 整型 Int
* 浮点型 Float
* 字符串型 String
* 布尔型 Boolean
* 复数型 Complex
***
#### 变量命名
Python中的变量命名的硬性规则与建议遵守的非硬性规则：
* 硬性规则
    * 变量由字母、数字和下划线构成，数字不能开头
    * 大小写敏感
    * 不要跟关键字和系统保留字(函数、模块名等)冲突
* PEP 8规则
    * 用小写字母拼写，多个单词用下划线连接。
    * 受保护的实例属性用单个下划线开头。
    * 私有的实例属性用两个下划线开头。

Python中可以使用`type`函数检查变量的类型。
```py
'''
File    :   变量1.py
Time    :   2023/02/18 22:24:37
Author  :   Z-JUNYE 
Version :   1.0
'''
a = 100
b = 1.1
c = 1+2j
d = 'abcd'
e = True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
```
输出结果如下：
```py
<class 'int'>
<class 'float'>
<class 'complex'>
<class 'str'>
<class 'bool'>
```
Python中可以使用内置的函数对变量类型进行转换：
* int(): 转换为整型
* float():转换为浮点型
* str():转换为字符串
* chr():将整型转换成该编码对应的字符串
* ord():将字符串转换成对应的编码
***
#### 运算符
Python支持多种运算符。

##### 赋值运算符
赋值运算符将右边的值赋予左边的变量。
```py
'''
File    :   赋值运算符.py
Time    :   2023/02/18 22:32:03
Author  :   Z-JUNYE 
Version :   1.0
'''
a = 3
b = 4
c = a+b
a += b
print(a == c)

d = a*b
a *= b
print(a == d)
```
运行结果如下：
```py
True
True
```
##### 比较运算符和逻辑运算符
比较运算符会产生布尔值， `True`或者`False`。  
逻辑运算有三个，`and`、`or`和`not`。 
```py
'''
File    :   比较运算符和逻辑运算符.py
Time    :   2023/02/18 23:25:10
Author  :   Z-JUNYE 
Version :   1.0
'''
flag0 = 1 == 1
flag1 = 2 > 1
flag2 = 2 < 1
flag3 = flag0 and flag2
flag4 = flag0 or flag1
flag5 = not flag0

print('flag0 =',flag0)
print('flag1 =',flag1)
print('flag2 =',flag2)
print('flag3 =',flag3)
print('flag4 =',flag4)
print('flag5 =',flag5)
```
运行结果如下
```py
flag0 = True
flag1 = True
flag2 = False
flag3 = False
flag4 = True
flag5 = False
```
***
##### 运算符优先级
比较运算符的优先级高于赋值运算符。

