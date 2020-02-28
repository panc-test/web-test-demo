'''
测试登录功能
'''

import unittest
from util.basic_driver import driver
from pom.login_page import Login_Page
from actions.image import Screeenshots
from ddt import ddt,file_data

page = Login_Page()
image = Screeenshots()

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
        #测试结果截图
        image.info_screenshots()

        #断言测试结果和预期结果








