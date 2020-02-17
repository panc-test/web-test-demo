import logging


class Log(object):

    # 创建一个logger对象
    logger = logging.getLogger()

    def __init__(self):
        #设置日志级别
        self.logger.setLevel(logging.INFO)
        #设置handler文件流
        handler=logging.FileHandler(filename='./logs/app.log',  encoding='utf-8')
        #设置handler文件流格式
        formatter=logging.Formatter('%(asctime)s  -%(levelname)s -%(name)s -%(message)s')
        handler.setFormatter(formatter)
        #将logger加载到handler文件流
        self.logger.addHandler(handler)


    def debug(self,messages):
        self.logger.debug(messages)

    def info(self,messages):
        self.logger.info(messages)

    def warn(self,messages):
        self.logger.warnings(messages)

    def error(self,messages):
        self.logger.error(messages)
