'''
程序主入口
'''

import unittest     #单元测试框架
from util.log import Log    #日志
from testcases.test_login import Test_Login #测试用例
from BeautifulReport import  BeautifulReport    #测试报告
from util.email import send_email


# 测试套件
def suite():

    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    test_cases=loader.loadTestsFromTestCase(Test_Login)
    suite.addTests(test_cases)
    return suite


#加载测试套件并生成测试报告
if __name__ == '__main__':

    log = Log()
    log.info('开始运行')

    suite=suite()
    result=BeautifulReport(suite)
    result.report(filename='cnode',description='cnode登录功能测试报告',report_dir='./report')
    send_email(subject='conde论坛登录功能测试报告')

    log.info('运行结束')

