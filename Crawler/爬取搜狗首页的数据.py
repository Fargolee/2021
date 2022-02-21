'''
Author: Lee
Descripttion: RTMart
Date: 2022-02-21 17:58:27
'''

from urllib import response
import requests
if __name__=='__main__':
    url='https://www.moulem.com/'
    response = requests.get(url=url)

    page_text = response.text
    print(page_text)
    with open('./Crawler/moulem.html', 'w', encoding='utf-8') as fb:
        fb.write(page_text)
    print('爬取结束！')