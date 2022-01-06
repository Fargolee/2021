#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/27 21:37
# @File  : 1：华氏温度转换为摄氏温度.py

# 华氏温度到摄氏温度的转换公式为：`C = (F - 32) / 1.8
f = float(input('请输入华氏摄氏度：'))
c = (f - 32)/1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')