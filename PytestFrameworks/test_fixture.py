'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-21 17:27:44
'''
'''
固件就是一些预处理的函数，pytest会在执行测试函数前（或者执行后）加载运行这些固件，常见的应用场景就有数据库的连接和关闭（设备连接和关闭）

按照官方的解释就是当运行测试函数，会首先检测运行函数的参数，搜索与参数同名的fixture，一旦pytest找到，就会运行这些固件，获取这些固件的返回值（如果有），并将这些返回值作为参数传递给测试函数；
'''
import pytest
@pytest.fixture()
def postcode():
    return "hello"

def test_count(postcode):
    assert postcode == 'hello'