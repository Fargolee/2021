#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/6 22:48
# @File  : 网易云词云图.py

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://music.163.com/#/song?id=1952182912')
driver.switch_to.frame(0)  # 切换至嵌套网页
# print(driver.page_source)  # 获取请求页面的html数据

js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight'

driver.execute_script(js)

divs = driver.find_elements_by_css_selector('.itm')
for div in divs:
    cnt = div.find_element_by_css_selector('.cnt.f-brk').text
    print(cnt)