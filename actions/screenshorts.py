'''
测试截图配置文件
'''

import os
from util.basic_driver import driver


#创建一个保存测试截图的类
class Screeenshots(object):

    #创建一个文件夹保存测试截图文件
    def get_screenshots_path(self):
        root_path=os.path.dirname(os.path.dirname(__file__))  #__file__指的是当前文件路径
        screenshots_path=os.path.join(root_path,'screenshots')
        if not os.path.exists(screenshots_path):
            os.mkdir(screenshots_path)
        return screenshots_path

    #报错截图
    def  error_screenshots(self,filename):

        screenshots_path=self.get_screenshots_path()
        error_path=os.path.join(screenshots_path,'error_screenshots')
        if not os.path.exists(error_path):
            os.mkdir(error_path)
        file_path=os.path.join(error_path,filename+'.png')

        driver.save_screenshot(file_path)

    #正常截图
    def info_screenshots(self,filename):

        screenshots_path = self.get_screenshots_path()
        info_path=os.path.join(screenshots_path,'info_screenshots')
        if not os.path.exists(info_path):
            os.mkdir(info_path)
        file_path=os.path.join(info_path,filename+'.png')

        driver.save_screenshot(file_path)