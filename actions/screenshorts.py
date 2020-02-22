'''
测试截图配置文件
'''

import os
from util.basic_driver import driver
import time




#创建一个保存测试截图的类
class Screeenshots(object):


    #创建一个images文件夹保存测试截图
    def get_screenshots_path(self):
        root_path=os.path.dirname(os.path.dirname(__file__))  #__file__指的是当前文件路径
        images_path=os.path.join(root_path,'images')
        if not os.path.exists(images_path):
            os.mkdir(images_path)
        return images_path

    #报错截图
    def  error_screenshots(self):
        images_path=self.get_screenshots_path()
        error_path=os.path.join(images_path,'error_images')
        if not os.path.exists(error_path):
            os.mkdir(error_path)
        filename=time.strftime('%Y-%m-%d-%H-%M-%S')
        file_path=os.path.join(error_path,filename+'.png')
        driver.save_screenshot(file_path)

    #正常截图
    def info_screenshots(self):
        images_path = self.get_screenshots_path()
        info_path=os.path.join(images_path,'info_images')
        if not os.path.exists(info_path):
            os.mkdir(info_path)
        filename=time.strftime('%Y-%m-%d-%H-%M-%S')
        file_path=os.path.join(info_path,filename+'.png')
        driver.save_screenshot(file_path)