'''
File    :   继承和多态.py
Time    :   2023/02/28 21:50:56
Author  :   Z-JUNYE 
Version :   1.0
Comment :   继承和多态
'''

class Person(object):
    '''人'''
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, age):
        self._age = age
    
    def watchTv(self):
        if self._age >= 18:
            print(f'{self._name}正在看动作片')
        else:
            print(f'{self._name}正在看龙珠')

class Student(Person):
    '''学生'''
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, grade):
        self._grade = grade
    
    def study(self, course):
        print(f'{self._name}正在学习{course}')

class Teacher(Person):
    '''老师'''
    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        self._title = title
    
    def teach(self, course):
        print(f'{self._name}正在讲{course}')
    
def main():
    stu = Student('Aki', 3, '幼稚园')
    stu.study('识字')
    stu.watchTv()

    t = Teacher('zjy',30,'砖家')
    t.teach('识字')
    t.watchTv()

if __name__ == '__main__':
    main()
