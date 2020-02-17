import unittest
from testcases.test_user import TestUser
from util.log import Log


if __name__ == '__main__':

    #加载日志信息
    log=Log()
    log.info('开始运行')

    #创建测试套件
    suite=unittest.TestSuite()

    #定义要执行的测试用例
    # test_cases=[TestUser('test_register'),TestUser('test_login')]
    # test_cases = unittest.TestLoader.loadTestsFromTestCase(TestUser)
    start_dir='./testcases/'
    test_cases=unittest.defaultTestLoader.discover(start_dir, pattern='test*.py', top_level_dir=None)

    #将要执行的测试用例加载到测试套件中
    suite.addTests(test_cases)

    #运行测试套件
    runner=unittest.TextTestRunner()
    runner.run(suite)

    log.info('运行结束')