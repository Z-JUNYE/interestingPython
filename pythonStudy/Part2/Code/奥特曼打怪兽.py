'''
File    :   奥特曼打怪兽.py
Time    :   2023/03/01 19:04:43
Author  :   Z-JUNYE 
Version :   1.0
Comment :   
'''

from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass = ABCMeta):
    '''战斗者'''

    #通过__slots__魔法限定对象可以绑定的成员变量
    __slots__ = ('_name', '_hp')

    def __init__(self, name, hp):
        '''
        初始化方法
        :param name
        :param hp
        '''
        self._name = name
        self._hp = hp
    
    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp
    
    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0
    
    @property
    def alive(self):
        return self._hp > 0
    
    @abstractmethod
    def attack(self, other):
        '''攻击
        :param other
        '''
        pass

class Ultraman(Fighter):
    '''奥特曼'''

    __slots__ = ('_name', '_hp', '_mp')
    
    def __init__(self, name, hp, mp):
        '''初始化方法
        :param name
        :param hp
        :param mp
        '''
        super().__init__(name, hp)
        self._mp =mp
    def attack(self, other):
        other.hp -= randint(15,25)
    
    def huge_attck(self, other):
        '''必杀技
        造成至少50点或对方血量四分之三的伤害
        :param other
        :return ：使用成功返回True
        '''
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp *3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self, others):
        '''魔法攻击
        :param other
        :return 使用魔法成功返回True
        '''
        if self._mp >= 20:
            self._mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10,15)
            return True
        else:
            return False
    
    def resume(self):
        '''回复魔法'''
        incr_point = randint(1,10)
        self._mp += incr_point
        return incr_point
    
    def __str__(self):
        return f'~~~{self._name}奥特曼 生命值：{self._hp} 魔法值 : {self._mp}'
    
class Monster(Fighter):
    '''小怪兽'''

    __slots__ = ('_name', '_hp')
    def attack(self, other):
        other.hp -= randint(10,20)
    
    def __str__(self):
        return f'~~~{self._name}小怪兽 生命值 : {self._hp}'

def is_any_alive(monsters):
    '''判断有没有小怪兽存活'''
    for monster in monsters:
        if monster.alive > 0:
            return True
    return False

def select_alive_one(monsters):
    '''选中一只活着的怪兽'''
    monsters_count = len(monsters)
    while True:
        index = randrange(monsters_count)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ultraman, monsters):
    '''显示奥特曼和小怪兽的信息'''
    print(ultraman)
    for monster in monsters:
        print(monster, end = '')

def main():
    u = Ultraman('zjy', 1000, 150)
    m1 = Monster('AAA', 500)
    m2 = Monster('BBB', 700)
    m3 = Monster('CCC', 500)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print(f'=====第{fight_round}回合=====')
        m = select_alive_one(ms) #选中一只怪兽
        skill = randint(1,10) #随意概率使用技能
        if skill <= 6: #60%概率普通攻击
            print(f'{u.name}使用普通攻击打击了{m.name}')
            u.attack(m)
            print(f'{u.name}魔法值回复了{u.resume()}')
        elif skill <= 9: #30概率魔法攻击群体
            if u.magic_attack(ms):
                print(f'{u.name}使用了魔法攻击')
            else:
                print(f'{u.name}使用魔法攻击失败')
        else: #10%概率使用必杀技
            if u.huge_attck(m):
                print(f'{u.name}使用了必杀技')
            else:
                print(f'{u.name}使用普通攻击')
                print(f'{u.name}魔法回复了{u.resume()}')
        if m.alive > 0: #小怪兽存活就可以反击
            print(f'{m.name}回击了{u.name}')
            m.attack(u)
        display_info(u, ms)
        fight_round += 1
    print('\n=====战斗结束=====\n')
    if u.alive > 0:
        print(f'{u.name}奥特曼胜利')
    else:
        print(f'{u.name}奥特曼被怪兽打败了')

if __name__ == '__main__':
    main()








