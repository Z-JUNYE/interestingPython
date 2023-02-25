'''
File    :   字典example.py
Time    :   2023/02/25 20:06:27
Author  :   Z-JUNYE 
Version :   1.0
Comment :   字典example
'''

#创建字典
scores = {'zjy':60, 'AKI':100, 'Sony':80}
print(scores) #{'zjy': 60, 'AKI': 100, 'Sony': 80}
#创建字典的构造器语法
items1 = dict(one = 1, two = 2, three = 3, four = 4)
print(items1) #{'one': 1, 'two': 2, 'three': 3, 'four': 4}
items2 = dict(zip(['a','b','c'],'123'))
print(items2) #{'a': '1', 'b': '2', 'c': '3'}
#可以通过键获取字典中对应的值
print(scores['zjy']) #60
#对字典中所有键值对进行遍历
for key in scores:
    print(f'{key}:{scores[key]}')
'''
60
zjy:60
AKI:100
Sony:80
'''
#更新字典中的元素
scores['Apple'] = 90
scores['Yamaha'] = 95
print(scores) #{'zjy': 60, 'AKI': 100, 'Sony': 80, 'Apple': 90, 'Yamaha': 95}

scores.update(Ibanez=90, Fender = 90)
print(scores) #{'zjy': 60, 'AKI': 100, 'Sony': 80, 'Apple': 90, 'Yamaha': 95, 'Ibanez': 90, 'Fender': 90}

#get方法也是通过键获取对应的值但是可以设置默认值
print(scores.get('Gibson', 80)) #80
#删除字典中的元素
print(scores.popitem()) #('Fender', 90)
print(scores.popitem()) #('Ibanez', 90)
print(scores.pop('zjy', 60)) #60
print(scores) #{'AKI': 100, 'Sony': 80, 'Apple': 90, 'Yamaha': 95}
#清空字典
scores.clear()
print(scores) #{}

