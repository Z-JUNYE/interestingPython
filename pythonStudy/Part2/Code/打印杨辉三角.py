'''
File    :   打印杨辉三角.py
Time    :   2023/02/25 20:53:36
Author  :   Z-JUNYE 
Version :   1.0
Comment :   打印杨辉三角
'''

def main():
    num = int(input('input number of rows:'))
    yh = [[]]*num
    for row in range(len(yh)):
        yh[row] = [None] * (row+1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
            print(yh[row][col], end = '\t')
        print()
    
if __name__ == '__main__':
    main()
