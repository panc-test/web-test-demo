'''
测试登录功能
'''

import time
import unittest
from util.basic_driver import driver
from pom.login_page import Login_Page
from actions.screenshorts import Screeenshots
from ddt import ddt,file_data


@ddt
class Test_Login(unittest.TestCase):

    page=Login_Page()
    image = Screeenshots()

    # 测试用例执行前的环境准备
    def setUp(self) -> None:
        self.driver=driver
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    # 测试用例执行结束后的环境恢复
    def tearDown(self) -> None:
        self.driver.delete_all_cookies()
        self.driver.quit()

    @file_data('../data/data_login.yaml')
    def test_login(self,name,passwd,assert_text):
        #打开登录页面
        self.page.go_login()
        #执行测试用例
        self.page.login(loginname=name,password=passwd)

    # def test_login(self):
    #     self.page.go_login()
    #     self.page.login(loginname='testuser1',password='123456')
    #     self.image.info_screenshots()






