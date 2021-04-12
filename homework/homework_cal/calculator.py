# 1、将课上的计算器的相加相除功能 ，完善测试用例，使用fixture
# 实现 setup_class/teardown_class 功能（使用conftest.py文件保存 fixture）
# 2、添加测试步骤，生成测试报告，截图回复课程贴

class Calculator:
    # 加法
    def add(self, a, b):
        return a + b

    # 减法
    def sub(self, a, b):
        return a - b

    # 乘法
    def mul(self, a, b):
        return a * b

    # 除法
    def div(self, a, b):
        return a / b
