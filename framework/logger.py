import logging
import time
import os.path
class Logger(object):
    def __init__(self,logger):
        #创建loggeer   logger用于提供应用程序直接使用的接口
        self.logger=logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)#设置日志级别
        #创建一个handler用于写入一个日志文件
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/"#项目更目录下/logs保存日志

        log_name=log_path+rq+".log"
        fh=logging.FileHandler(log_name)#Handler 将Loggers产生的日志传到指定位置
        fh.setLevel(logging.INFO)
        # 创建一个handler用于输出控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)

        formatter=logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
        #Formatter控制输出格式%（asctime）s默认的时间格式%Y-%m-%d %H-%M-%S  %（name）s条用logger记录器的名称%（levelname）s日志的等级，%（message）s日志信息
        fh.setFormatter(formatter)#日志输出格式
        ch.setFormatter(formatter)#控制台输出的格式
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)
    def getlog(self):
        return self.logger








