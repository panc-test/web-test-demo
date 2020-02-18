#测试用例
import time
import unittest
from selenium import  webdriver
from util.basic_driver import driver
from pom.register_page import Register_Page
from pom.login_page import Login_Page


class TestUser(unittest.TestCase):

    # 测试用例执行前的环境准备
    @classmethod
    def setUpClass(cls) -> None:
        driver.maximize_window()
        driver.get('http://39.107.96.138:3000/')
        time.sleep(2)

    # 测试用例执行结束后的环境恢复
    @classmethod
    def tearDownClass(cls) -> None:
        driver.quit()

    #test1
    def test_register(self):
        #创建一个注册页面实例化对象
        rp=Register_Page()

        #打开注册页面
        rp.go_register()
        #调用封装好的用户注册界面操作方法
        rp.register(loginname='aaa',password='bbb',repassword='bbb',email='ccc')


    #test2
    def test_login(self):
        #创建一个登录页面实例化对象
        lp = Login_Page()

        # 打开登录页面
        lp.go_login()
        #调用封装好的用户登录界面操作方法
        lp.login(loginname='aaa',password='bbb')



