#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-11 19:00:33
'''
'''
https://ceshiren.com/t/topic/16009
【每日一题0107】去重到底
给定一个由纯数字组成的列表，其中可能存在多个重复的数字，请编写一个函数，将相同数字中先出现的数字移除，只保留该重复数字的最后一个。返回去重后的列表。

示例：输入：[3, 4, 4, 3, 6, 3]，输出：[4, 6, 3]。因为对于数字3，索引是0和3的会被移除；对于数字4，索引1的会被移除。

def solution(nums: list) -> list:
    # your code

assert solution([3,4,4,3,6,3]) == [4,6,3]
assert solution([1,2,1,2,1,2,3]) == [1,2,3]
assert solution([1,2,3,4]) == [1,2,3,4]
'''

def solution(nums: list) -> list:
    nums.reverse()
    new = []
    for i in nums:
        if i not in new:
            new.append(i)
    new.reverse()
    return new

assert solution([3,4,4,3,6,3]) == [4,6,3]
assert solution([1,2,1,2,1,2,3]) == [1,2,3]
assert solution([1,2,3,4]) == [1,2,3,4]
 
 # 方法二
# 利用 fromkeys 创建新字典，seq 为反转后的 nums
# 这样会得到自动去重后的k-v，只取 key，再做反转
# return list(dict.fromkeys(nums[::-1]).keys())[::-1]

# 方法三
# 利用 sorted 排序规则，按照反转后的列表下标排序
# return sorted(list(set(nums[::-1])), key=nums[::-1].index)[::-1]