'''
Author: Lee
Descripttion: Myhome
Date: 2022-06-27 23:08:50
'''

import requests
import re
import os



# url = 'https://jlow.ru/archives/JlowRu-20220302-1.html'
url = 'https://jlow.ru/archives/JlowRu-20211225-2.html'

header ={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

res = requests.get(url = url,headers= header)
html = res.text


dir_name = re.findall('<meta name="keywords" content="(.*?)" />',html)[-1]

if not os.path.exists(dir_name):
    os.mkdir(dir_name)

urls = re.findall('<img class=".*?" src=".*?" data-original="(.*?)" alt=".*?" title=".*?">',html)
print(urls)
for ur in urls:
    file_name = ur.split('/')[-1]
    res = requests.get(ur,headers=header)
    with open(dir_name +'/'+file_name+'.jpg','wb') as f:
        f.write(res.content)