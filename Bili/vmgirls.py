'''
Author: Lee
Descripttion: Myhome
Date: 2022-06-27 22:11:51
'''


import  requests  
import re
import os
#请求网页
url = 'https://www.vmgirls.com/19509.html'

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response = requests.get(url=url,headers=header)
html = response.text
# print(response.text)

#解析网页

dir_name =re.findall('h1 class=".*?">(.*?)</h1>',html)[-1] 

if not os.path.exists(dir_name):
    os.mkdir(dir_name)
# print(dir_name)
urls = re.findall('<a rel=".*?" href="(.*?)" alt=".*?" title=".*?">',html)
print(urls)

for ur in urls:
    file_name = ur.split('/')[-1]
    response = requests.get(url= ur,headers=header)
    with open(dir_name+'/'+file_name,'wb') as f:
        f.write(response.content)

