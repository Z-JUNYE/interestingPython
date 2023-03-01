'''
File    :   工资结算.py
Time    :   2023/03/01 20:07:34
Author  :   Z-JUNYE 
Version :   1.0
Comment :   公司有三种员工
            部门经理工资固定15000
            程序员按时间结算 每小时150
            销售按底薪1200+销售额5%提成结算
'''

from abc import ABCMeta, abstractmethod

class Employee(object, metaclass = ABCMeta):
    '''员工'''
    def __init__(self, name):
        '''初始化方法'''
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @abstractmethod
    def get_salary(self):
        '''获得月薪'''
        pass

class Manager(Employee):
    '''部门经理'''

    def get_salary(self):
        return 15000.0

class Coder(Employee):
    '''程序员'''
    def __init__(self, name, working_hours = 0):
        super().__init__(name)
        self._working_hours = working_hours
    
    @property
    def working_hours(self):
        return self._working_hours
    
    @working_hours.setter
    def working_hours(self, workding_hour):
        self._working_hours = workding_hour if workding_hour > 0 else 0
    
    def get_salary(self):
        return self._working_hours * 150.0

class Salesman(Employee):
    '''销售'''
    def __init__(self, name, sales = 0):
        super().__init__(name)
        self._sales = sales
    
    @property
    def sales(self):
        return self._sales
    
    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0
    
    def get_salary(self):
        return self._sales * 0.05 + 1200

def main():
    emps = [
    Manager('刘备'), Coder('诸葛亮'),
    Manager('曹操'), Salesman('荀彧'),
    Salesman('吕布'), Coder('张辽'),
    Coder('赵云')
    ]
    for emp in emps:
        if isinstance(emp, Coder):
            emp.working_hours = int(input('输入本月工时: '))
        elif isinstance(emp, Salesman):
            emp.sales = int(input('输入本月销售额: '))
        print(f'{emp.name}本月工资为{emp.get_salary()}')

if __name__ == '__main__':
    main()