'''
POM模型-用户注册界面的操作

'''

from common.basic_driver import driver
from util.log import Log
from selenium.common.exceptions import NoSuchElementException


log=Log()

class Register_Page():

    def __init__(self):
        self.register_name_id='loginname'
        self.register_pass_id='pass'
        self.register_repass_id='re_pass'
        self.register_email_id='email'
        self.register_button_css='input[type="submit"]'

    def go_register(self):
        driver.get('http://39.107.96.138:3000/signup')

    def register(self,loginname=None, password=None, repassword=None, email=None):
        try:
            name = driver.find_element_by_id(self.register_name_id)
            name.clear()
            name.send_keys(loginname)

            pass_wd = driver.find_element_by_id(self.register_pass_id)
            pass_wd.clear()
            pass_wd.send_keys(password)

            repass_wd = driver.find_element_by_id(self.register_repass_id)
            repass_wd.clear()
            repass_wd.send_keys(repassword)

            register_email = driver.find_element_by_id(self.register_email_id)
            register_email.clear()
            register_email.send_keys(email)

            button = driver.find_element_by_css_selector(self.register_button_css)
            button.click()

        except  NoSuchElementException:
            log.error('注册页面元素定位异常')

        except  Exception:
            log.error('注册页面其它异常')








