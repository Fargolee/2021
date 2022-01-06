#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/27 21:49
# @File  : 3：输入年份判断是不是闰年.py

year = int(input("请输入年份："))

is_leap = year % 4 ==0 and year % 100 !=0 or year % 400 == 0
print(is_leap)