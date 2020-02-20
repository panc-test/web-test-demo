#测试用例
import time
import unittest
from selenium import  webdriver
from util.basic_driver import driver
from pom.register_page import Register_Page


class Test_Register(unittest.TestCase):

    # 测试用例执行前的环境准备

    def setUp(self) -> None:
        driver.maximize_window()
        driver.get('http://39.107.96.138:3000/')
        time.sleep(2)

    # 测试用例执行结束后的环境恢复
    def tearDown(self) -> None:
        driver.quit()

    #test1
    def test1_register(self):
        #创建一个注册页面实例化对象
        register1=Register_Page()
        #打开注册页面
        register1.go_register()
        #执行测试用例
        register1.register(loginname='aaa',password='bbb',repassword='bbb',email='ccc')



