'''
File    :   装饰器.py
Time    :   2023/02/27 22:35:09
Author  :   Z-JUNYE 
Version :   1.0
Comment :   property 装饰器
'''

class Person(object):

    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    # 访问器 getter方法
    @property
    def age(self):
        return self._age
    
    # 访问器 getter方法
    def name(self):
        return self._name
    
    # 修改器 setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print(f'{self._name}正在玩飞行棋')
        else:
            print(f'{self._name}正在玩斗地主')

def main():
    person = Person('ZJY',3)
    person.play()
    person.age = 22
    person.play()

if __name__ == '__main__':
    main()
