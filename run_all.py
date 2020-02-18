import unittest #导入单元测试框架
from testcases.test_register import TestUser
import HTMLReport
# import HTMLTestRunner

if __name__ == '__main__':

    #TestSuite()-测试套件
    suite=unittest.TestSuite()
    test_cases=[TestUser('test_register'),TestUser('test_login')]
    suite.addTests(test_cases)
    # suite.addTest(TestUser('test_register'))
    # suite.addTest(TestUser('test_login'))

    # TestLoader()类来控制需要执行那些测试用例，但是这种方法是无法对case进行排序的
    # tests=unittest.TestLoader().loadTestsFromTestCase(TestUser)

    # unittest中的discover()方法可以批量加载用例
    # tests=unittest.defaultTestLoader.discover(TestUser, pattern='test*.py', top_level_dir=None)



    #使用TextTestRunner()类的run()方法，来运行测试套件TestSuite中的测试用例集合
    # runner=unittest.TextTestRunner()
    # runner.run(suite)

    #HTMLReport模块-输出html格式测试结果
    runner = HTMLReport.TestRunner(report_file_name='',  # 报告文件名，如果未赋值，将采用“test+时间戳”
                                   output_path='./report',  # 保存文件夹名，默认“report”
                                   title='测试报告',  # 报告标题，默认“测试报告”
                                   description='conde论坛登录注册功能测试',  # 报告描述，默认“测试描述”
                                   )
    runner.run(suite)

    #HTMLTestRunner
    # runner=HTMLTestRunner.HTMLTestRunner(stream='report',
    #                                      title='测试报告',
    #                                      description='测试用例执行报告')
    # runner.run(suite)











