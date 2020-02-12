import unittest #导入单元测试框架
from testcases.test_user import TestUser

if __name__ == '__main__':
    #创建测试套件并加载测试用例（控制测试用例执行顺序）
    suite=unittest.TestSuite()
    # suite.addTest(TestUser('test_register'))
    # suite.addTest(TestUser('test_login'))
    tests=[TestUser('test_register'),TestUser('test_login')]
    suite.addTests(tests)
    #使用TextTestRunner()类的run()方法，来运行测试套件TestSuite中的测试用例集合
    runner=unittest.TextTestRunner()
    runner.run(suite)

    # TestLoader()类来控制需要执行那些测试用例
    # loader=unittest.TestLoader()
    # loader.discover(patter='text*.py')
    # loader.loadTestsFromTestCase(TestUser)




