'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-20 16:31:17
'''
from urllib import response
import requests

url = 'https://api.oick.cn/lishi/api.php'

re = requests.get(url)
print(re)