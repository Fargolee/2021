'''
Author: Lee
Descripttion: RTMart
Date: 2022-01-18 18:42:57
'''
'''
1.指定运行测试用例，可以通过::显示标记（文件名::类名::方法名）（文件名::函数名）
pytest test_example3.py::test_odd
复制代码
2.指定一些测试用例测试运行，可以使用-k模糊匹配
pytest -k example
'''
import random
import pytest

# 3.通过pytest.mark.skip()或者pytest.makr.skipif()条件表达式，跳过指定的测试用例

test_flag = False

@pytest.mark.skip()
def test_odd():
    num = random.randint(0,100)
    print(num)
    assert num  % 2 ==1

@pytest.mark.skipif(test_flag is False ,reason= "test_flag is False")
def test_even():
    num = random.randint(0,100)
    print(num)
    assert num % 2 == 0

# 4.通过pytest.raises()捕获测试用例可能抛出的异常
def test_zero():
    num = 0
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    exc_msg = e.value.args[0]
    print(exc_msg)
    assert num == 0

# 5.预先知道测试用例会失败，但是不想跳过，需要显示提示信息，使用pytest.mark.xfail()
@pytest.mark