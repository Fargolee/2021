'''
Author: Lee
Descripttion: RTMart
Date: 2022-03-03 18:25:13
'''

import os

# file_name = 'weibo'
# if not os.path.exists(file_name):
#     os.mkdir(file_name)


def exists(path):                                # 路径不存在则创建
    try:
        file_dir = os.path.split(path)[0]        # 获取路径目录
        if not os.path.isdir(file_dir):          # 目录是否存在
            os.makedirs(file_dir)                # 不存在则创建
            return True
    except:
        print(IOError)
        print('判断路径是否存在失败')
        return False
exists('/weibo')