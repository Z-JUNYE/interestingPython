'''
File    :   多态.py
Time    :   2023/02/28 22:10:10
Author  :   Z-JUNYE 
Version :   1.0
Comment :   
'''

from abc import ABCMeta, abstractmethod

class Pet(object, metaclass = ABCMeta):
    '''宠物'''
    def __init__(self, nickname):
        self._nickname = nickname
    
    @abstractmethod
    def makeVoice(self):
        '''发出声音'''
        pass

class Dog(Pet):
    '''狗狗'''
    def makeVoice(self):
        print(f'{self._nickname}:汪汪汪')

class Cat(Pet):
    '''猫咪'''
    def makeVoice(self):
        print(f'{self._nickname}:喵喵喵')

def main():
    pets = [Dog('小白'), Cat('小黑猫'), Dog('狗小黑')]
    for pet in pets:
        pet.makeVoice()

if __name__ == '__main__':
    main()