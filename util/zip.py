'''
封装压缩文件操作
'''

import os
from  zipfile import  ZipFile


#传入一个测试截图目录，把该目录下的所有测试截图文件路径以列表的形式返回
def get_files_path():

    dir = r'E:\GitHub\Web_Framework\images'
    file_paths = []
    for root, dirs, files in os.walk(dir):  #os.walk()方法,遍历时指将指定的目录下的全部目录包括子目录以及文件访问一遍
        for filename in files:
            file_path = os.path.join(root, filename)
            file_paths.append(file_path)
    return file_paths

#创建一个等待邮件发送的压缩文件，将测试报告和测试截图添加到压缩文件
def get_zipfile():

    # 获取测试截图文件和测试报告文件路径
    files = get_files_path()
    report_file=r'E:\GitHub\Web_Framework\report\cnode.html'
    try:
        # 向指定的压缩文件（没有得话会创建一个空的zip文件）中添加测试截图和测试报告
        filename=r'E:\GitHub\Web_Framework\email_files\report.zip'
        myzip=ZipFile(file=filename, mode='w')
        for file in files:
            myzip.write(file)
        # zip cnode.html
        myzip.write(report_file)
        myzip.close()
        print('zip success')
    except:
        print('zip fail')

