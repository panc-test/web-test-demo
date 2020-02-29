'''
POM模型-用户登录界面的操作

'''
from common.basic_driver import driver
from util.log import Log
from selenium.common.exceptions import NoSuchElementException
from util.image import Screeenshots

log=Log()
image=Screeenshots()

class Login_Page():

    def __init__(self):
        self.login_name_id='name'
        self.login_pass_id='pass'
        self.login_button_css='input[type="submit"]'

        self.login_success_css='span[class="user_name"]>a[class="dark"]'
        self.login_fail_css='div[class="alert alert-error"]>strong'

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

            image.info_screenshots()

        except  NoSuchElementException as e:
            log.error(e)
            image.error_screenshots()

        except  Exception as e:
            log.error(e)
            image.error_screenshots()

    #获取测试结果
    def get_login_result(self):
        """
        登录成功 页面跳转到首页，返回用户名  http://39.107.96.138:3000/
        登录失败 返回登录错误提示信息 http://39.107.96.138:3000/signin
        return: str
        """
        url=driver.current_url  #获取当前页面的url
        if 'signin' not in url:
            result_text=driver.find_element_by_css_selector(self.login_success_css).text
        else:
            result_text=driver.find_element_by_css_selector(self.login_fail_css).text

        return result_text










