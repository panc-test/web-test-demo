'''
POM模型-用户登录界面的操作

'''
from util.basic_driver import driver
from util.log import Log
from selenium.common.exceptions import NoSuchElementException


log=Log()

class Login_Page():

    def __init__(self):
        self.login_name_id='name'
        self.login_pass_id='pass'
        self.login_button_css='input[type="submit"]'

    def go_login(self):
        driver.get('http://39.107.96.138:3000/signin')

    def login(self,loginname=None, password=None):
        try:
            name = driver.find_element_by_id(self.login_name_id)
            name.clear()
            name.send_keys(loginname)

            pass_wd = driver.find_element_by_id(self.login_pass_id)
            pass_wd.clear()
            pass_wd.send_keys(password)

            button = driver.find_element_by_css_selector(self.login_button_css)
            button.click()

        except  NoSuchElementException:
            log.error('登录页面元素定位异常')

        except  Exception:
            log.error('登录页面其它异常')








