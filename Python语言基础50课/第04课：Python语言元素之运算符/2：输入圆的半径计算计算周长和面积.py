#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2021/12/27 21:43
# @File  : 2：输入圆的半径计算计算周长和面积.py
r = float(input("请输入圆的半径："))
L = 2 * 3.14159 * r
S = 3.14159 * r**2

print('圆的周长：%.2f' % L)
print("圆的面积：%.2f" % S)