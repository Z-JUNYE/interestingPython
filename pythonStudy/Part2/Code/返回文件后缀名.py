'''
File    :   返回文件后缀名.py
Time    :   2023/02/25 20:31:41
Author  :   Z-JUNYE 
Version :   1.0
Comment :   返回文件后缀名
'''

def getSuffix(fileName, hasDot = False):
    '''
    返回文件后缀名
    :param fileName :文件名
    :param hasDot : 返回的后缀名是否需要带点
    :return :文件的后缀名
    '''
    dotPos = fileName.rfind('.')
    if 0<dotPos< len(fileName)-1:
        index = dotPos if hasDot else dotPos+1
        return fileName[index:]
    else:
        return ''

print(getSuffix('zjy.png'))