import unittest     #加载单元测试框架
from testcases.test_register import Test_Register    #调用测试用例模块
from testcases.test_login import Test_Login
from util.log import Log    #调用日志封装的模块


log=Log()
#创建测试套件，并加载测试用例
def suite():
    suite = unittest.TestSuite()
    suite.addTest(Test_Register('test_register'))
    # suite.addTest(Test_Login('test_login'))
    return suite

#执行测试用例，记录日志，并输出测试结果
if __name__ == '__main__':
    log.info('开始运行')
    runner = unittest.TextTestRunner()
    runner.run(suite())
    log.info('运行结束')

