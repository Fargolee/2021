'''
Author: Lee
Descripttion: RTMart
Date: 2022-02-08 14:57:32
'''
'''
 给定一个不小心混进了字母的数字串，请编写一个函数，提取出其中的数字。

示例：
输入："a6b6c6"，输出：666。
输入："aa 112 3dd"，输出：1123。
'''

def get_int(words: str) -> int:
    return int(''.join([w for w in words if w.isdigit()]))

assert get_int("a1b2c3") == 123
assert get_int("aa1bb2cc3dd") == 123
assert get_int("hogwarts666") == 666