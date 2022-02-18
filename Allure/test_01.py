'''
Author: Lee
Descripttion: RTMart
Date: 2022-02-18 10:08:05
'''
import pytest

class TestCase:
    def test_01(self):
        print('---用例01---')
        assert 1
    def test_02(self):
        print('---用例02---')
        assert 1
    def test_03(self):
        print('---用例03---')
        assert 0
if __name__ == '__main__':
    pytest.main(['-s'])



# pytest .\test_01.py --alluredir ./report/result

# 一：allure generate 生成测试结果数据 -o 生成报告的路径 --clean
# --clean表示：如果已经存在生成报告路径文件夹时，再次使用会提示添加--clean参数来重写
# 如以下编写用例命令
# allure generate report/result/ -o report/html --clean
# allure open  生成报告的路径地址
# E:\auto_test\test_01>allure generate report/result/ -o report/html --clean
# Report successfully generated to report\html
# 这样就会自动打开allure报告信息

# 二：allure serve report/result
# 命令中allure serve 表示确定一个allure的服务，后面跟的是报告的路径内容