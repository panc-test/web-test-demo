'''
测试登录功能
'''

import unittest
from common.basic_driver import driver
from pom.login_page import Login_Page
from ddt import ddt,file_data
from util.log import Log


page = Login_Page()
log=Log()

@ddt
class Test_Login(unittest.TestCase):

    # 测试用例执行前的环境准备
    @classmethod
    def setUpClass(cls) -> None:
        driver.maximize_window()

    # 测试用例执行结束后的环境恢复
    @classmethod
    def tearDownClass(cls) -> None:
        driver.delete_all_cookies()
        driver.quit()

    @file_data('../data/data_login.yaml')
    def test_login(self,name,passwd,assert_text):
        #打开登录页面
        page.go_login()
        #执行测试用例
        page.login(loginname=name,password=passwd)


        #断言测试结果和预期结果
        result_text=page.get_login_result()

        self.assertEqual(result_text, assert_text)

        '''
        注意这种方法是不行的，虽然断言失败了，但是被except中定义的异常类捕获，测试用例仍然pas
        try:
            self.assertEqual(result_text,assert_text)
            image.info_screenshots()
        except  AssertionError as e:
            log.warn(e)
            image.error_screenshots()
        '''























