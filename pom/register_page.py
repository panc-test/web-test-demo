'''
POM模型-用户注册登录界面的操作

'''

from util.basic_driver import driver
from selenium.common.exceptions import NoSuchElementException
from util.log import Log


log=Log()

class Register_Page(object):

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
            login_name = driver.find_element_by_id('register_name_id')
            login_name.clear()
            login_name.send_keys('loginname')

            pass_wd = driver.find_element_by_id('register_pass_id')
            pass_wd.clear()
            pass_wd.send_keys('password')

            repass_wd = driver.find_element_by_id('register_repass_id')
            repass_wd.clear()
            repass_wd.send_keys('repassword')

            email = driver.find_element_by_id('register_email_id')
            email.clear()
            email.send_keys('email')

            button = driver.find_element_by_css_selector('register_button_css')
            button.click()

        except NoSuchElementException:
            log.error('注册界面元素定位出错')
        except  Exception:
            log.error('注册界面出现其它错误')


