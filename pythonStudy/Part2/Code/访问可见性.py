'''
File    :   访问可见性.py
Time    :   2023/02/26 21:48:59
Author  :   Z-JUNYE 
Version :   1.0
Comment :   访问可见性
'''
'''
class Test:
    def __init__(self,foo):
        self.__foo = foo
    
    def __bar(self):
        print(self.__foo)
        print('__bar')
    
def main():
    test = Test('hello')
    #AttributeError: 'Test' object has no attribute '__bar'
    test.__bar()

    print(test.__foo)

if __name__ == '__main__':
    main()

'''
class Test:

    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')
    
def main():
    test = Test('hello')
    test._Test__bar()
    print(test._Test__foo)

if __name__ == '__main__':
    main()
