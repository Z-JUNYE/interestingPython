'''
File    :   约瑟夫环问题.py
Time    :   2023/02/25 21:27:44
Author  :   Z-JUNYE 
Version :   1.0
Comment :   约瑟夫环
'''


def main():
    l1 = [x for x in range(1,31)]
    print(l1)
    for i in range(15):
        l1.remove(l1[8]) #扔掉第九个人
        l1 = l1[8:]+l1[:8] #从第十个人开始重新排序

    print(sorted(l1))

if __name__ == '__main__':
    main()
