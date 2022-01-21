#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-18 18:35:27
'''
'''
https://juejin.cn/post/7013949685992259591

Pytest编写规则:

测试文件以test_开头（以_test为结尾）
测试的类以Test开头；
测试的方法以test_开头
断言使用基本的assert
'''
import pytest

def count_num(a: list) -> int:
    return len(a)

def test_count():
    assert count_num([1,2,3]) ==3