'''
Author: Lee
Descripttion: Myhome
Date: 2022-05-24 20:58:36
'''


import requests
import re
import os

filename = 'music\\'
if not os.path.exists(filename):
    os.mkdir(filename)

url = 'https://music.163.com/playlist?id=47260461&userid=50582744'
header = {
    'user-agent' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36',
    'cookie':'MUSIC_U=aa35e663ce320a88e058fac1134244b2c98b5ad14bd0c561764213edfb775c5e993166e004087dd3fde6fb95542eda3adc4b2f13080efb0957dafeb18bdecc06fd22ec0f3a5d88021b93ac14e0ed86ab'
}

response = requests.get(url=url, headers= header)
html_data =re.findall('<a href="/song\?id=(\d+)">(.*?)</a>',response.text)

for num_id, title in html_data:
    print(num_id,title)
    music_url = f"https://music.163.com/song/media/outer/url?id={num_id}.mp3"
    music_connect = requests.get(url= music_url,headers=header).content
    try:
        with open(filename+title+'.mp3', 'wb')as f:
            f.write(music_connect)
    except IOError:
        print(title+"下载失败")

# print(html_data)
# print(response.text)