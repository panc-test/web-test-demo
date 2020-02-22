'''
程序主入口
'''

import unittest     #加载单元测试框架
from util.log import Log    #调用日志封装的模块
# from testcases.test_register import Test_Register    #调用测试用例模块
from testcases.test_login import Test_Login
from BeautifulReport import  BeautifulReport    #E:\GitHub\Web_Framework\venv\Lib\site-packages



# 测试套件
def suite():

    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    test_cases=loader.loadTestsFromTestCase(Test_Login)
    suite.addTests(test_cases)
    return suite


log=Log()

if __name__ == '__main__':

    log.info('开始运行')

    suite=suite()
    result=BeautifulReport(suite)
    result.report(filename='cnode',description='cnode登录功能测试报告',report_dir='./report')

    log.info('运行结束')

