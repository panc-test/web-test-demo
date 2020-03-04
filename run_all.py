'''
程序主入口
'''

import unittest     #单元测试框架
from util.log import Log
from testcases.test_cnode import Cnode
from BeautifulReport import  BeautifulReport
from util.zip import get_zipfile
from util.send_email import send_email


# 测试套件
def suite():
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    testcases=loader.loadTestsFromTestCase(Cnode)
    suite.addTest(testcases)
    return suite


#加载测试套件并执行测试用例，生成测试报告
if __name__ == '__main__':

    log = Log()
    log.info('开始运行')

    suite=suite()
    result=BeautifulReport(suite)
    result.report(filename='cnode',description='cnode测试报告',report_dir='./report')
    #压缩文件
    get_zipfile()
    #发送邮件
    send_email()

    log.info('运行结束')

