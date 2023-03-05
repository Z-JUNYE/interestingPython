'''
File    :   json格式.py
Time    :   2023/03/05 21:59:35
Author  :   Z-JUNYE 
Version :   1.0
Comment :   以JSON格式保存
'''

import json

def main():
    my_dict = {
            "name": "zjy",
            "age": 33,
            "qq": 12345678,
            "friends": ["Aki", "LYN"],
            "cars": [
                {"brand": "BYD", "max_speed": 180},
                {"brand": "Audi", "max_speed": 280},
                {"brand": "Benz", "max_speed": 320}
                ]      
            }
    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(my_dict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成')

if __name__ == '__main__':
    main()
