'''
File    :   定义类example.py
Time    :   2023/02/25 22:04:18
Author  :   Z-JUNYE 
Version :   1.0
Comment :   定义类：学生
'''

class Student(object):
    #__init__是一个特殊方法用于在创建对象时进行初始化操作
    #通过这个方法可以为学生对象绑定name和age两个基本属性
    def __init__(self, name, age):
        self.name = name
        self.age =age
    
    def study(self, courseName):
        print('%s正在学习%s.' % (self.name, courseName))
    # PEP 8要求标识符的名字用全小写多个单词用下划线连接
    #但是部分程序员和公司倾向于使用驼峰命名法
    def watchMovie(self):
        if self.age < 18:
            print(f'{self.name}只能看动画片')
        else:
            print(f'{self.name}正在看岛国片')

def main():
    #创建学生对象并指定姓名和年龄
    stu1 = Student('ZJY',30)
    stu1.study('Python基础')
    stu1.watchMovie()

    stu2 = Student('AKI',3)
    stu2.study('数数')
    stu2.watchMovie()

if __name__ == '__main__':
    main()

