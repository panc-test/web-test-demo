#测试用例
import time
import unittest
from selenium import  webdriver
from util.basic_driver import driver
from pom.login_page import Login_Page


class Test_Login(unittest.TestCase):

    # 测试用例执行前的环境准备
    def setUp(self) -> None:
        driver.maximize_window()
        driver.get('http://39.107.96.138:3000/')
        time.sleep(2)

    # 测试用例执行结束后的环境恢复
    def tearDown(self) -> None:
        driver.quit()

    #test
    def test_login(self):
        #创建一个登录页面实例化对象
        lp = Login_Page()

        # 打开登录页面
        lp.go_login()
        #调用封装好的用户登录界面操作方法
        lp.login(loginname='aaa',password='bbb')



