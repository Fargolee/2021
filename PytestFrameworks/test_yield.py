'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-21 17:34:30
'''
'''
预处理和后处理
备注：

首先从结果上看验证了官方的解释，pytest执行测试函数前会寻找同名的固件加载运行；
connect_db固件中有yield，这里pytest默认会判断yield关键词之前的代码属于预处理，会在测试前执行，yield之后的代码则是属于后处理，将在测试后执行；

'''
import pytest


@pytest.fixture()
def connect_db():
    print("Connect Database in .......")
    yield
    print("Close Database out .......")


def read_database(key: str):
    p_info = {
        "name": "zhangsan",
        "address": "China Guangzhou",
        "age": 99
    }
    return p_info[key]


def test_count(connect_db):
    assert read_database("name") == "zhangsan"

