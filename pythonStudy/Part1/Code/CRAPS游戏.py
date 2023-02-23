'''
File    :   CRAPS游戏.py
Time    :   2023/02/23 12:26:04
Author  :   Z-JUNYE 
Version :   1.0
'''

'''
规则如下：每轮摇两次骰子
第一轮： 摇到7或者11，玩家胜，摇到2、3或者12点，庄家胜，其他点继续摇色子
第二轮： 摇到和第一轮一样的点数，玩家胜，摇到7点，庄家胜，其他点数继续摇色子
第三轮： 同第二轮
'''

from random import randint

def shakeDice():
    return randint(1,6)+randint(1,6)

def roundOneJudge():
    num = shakeDice()
    print('First Round Number : ', num)
    if num in [7, 11]:
        print('you win')
        return True
    elif num in [2, 3, 12]:
        print('you lose')
        return True
    else:
        print('next round')
        return num

def roundTwoJudge(roundOneNum):
    roundGoon = True
    while roundGoon:
        num2 = shakeDice()
        print('This Round Number : ', num2, 'First Round Number : ', roundOneNum)
        if num2 == 7:
            print('lose')
            roundGoon = False
        elif num2 == roundOneNum:
            print('win')
            roundGoon = False
        else:
            print('next round')
            roundGoon = True

def game():
    result = roundOneJudge()
    if result != True:
        roundTwoJudge(result)


game()



                






