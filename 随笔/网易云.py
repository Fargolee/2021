'''
Author: Lee
Descripttion: Myhome
Date: 2022-05-24 19:25:13
'''
from fileinput import filename
import requests
import re
import os

filename = 'music\\'
if not os.path.exists(filename):
    os.mkdir(filename)

url ='https://music.163.com/discover/toplist?id=3778678'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=headers)
# print(response.text)
html_data = re.findall('<a href="/song\?id=(\d+)">(.*?)</a>',response.text)
for num_id, title in html_data:
    music_url = f'https://music.163.com/song/media/outer/url?id={num_id}.mp3'
    
    music_connect = requests.get(url=music_url,headers=headers).content
    with open(filename +title + '.mp3',mode='wb') as f:
        f.write(music_connect)
    print(num_id,title)


# print(html_data)