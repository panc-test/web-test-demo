'''
POM模型-用户登录界面的操作

'''

from util.basic_driver import driver
from selenium.common.exceptions import NoSuchElementException
from util.log import Log


log=Log()

class Login_Page(object):

    def __init__(self):
        self.login_name_id='name'
        self.login_pass_id='pass'
        self.login_button_css='input[type="submit"]'

    def go_login(self):
        driver.get('http://39.107.96.138:3000/signin')


    def login(self,loginname=None, password=None):
        try:
            login_name = driver.find_element_by_id('login_name_id')
            login_name.clear()
            login_name.send_keys('loginname')

            pass_wd = driver.find_element_by_id('login_pass_id')
            pass_wd.clear()
            pass_wd.send_keys('password')

            button = driver.find_element_by_css_selector('login_button_css')
            button.click()
        except NoSuchElementException:
            log.error('登录界面定位元素出错')
        except Exception:
            log.error('登录界面出现其它错误')
