#测试用例
import unittest

class TestUser(unittest.TestCase):

    # 测试用例执行前的环境准备
    # @classmethod引入装饰器
    def setUp(self):
        print('test start')

    #测试用例执行结束后的环境恢复
    def tearDown(self):
        print('test end')

    def test_register(self):
        pass

    def test_login(self):
        pass

