#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/4 20:57
# @Author : Lee
# @File  : 01.Requests一血.py
# @Software: PyCharm

import  requests

if __name__ == '__main__':
    url = "https://www.sogou.com/"
    response = requests.get(url=url)
    page_text = response.text
    print(page_text)
    with open('./sougou.html', 'w', encoding='utf-8') as fb:
        fb.write(page_text)