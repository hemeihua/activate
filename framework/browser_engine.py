import os.path
from configparser import ConfigParser
from selenium import webdriver
from framework.logger import Logger

logger=Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):
    dir=os.path.dirname(os.path.abspath("."))
    #进入浏览器的驱动模块
    chrome_driver_path=dir+"/tools/chromedriver.exe"
    ie_driver_path=dir+"/tools/IEDriverServer.exe"
    firefox_driver_path=dir+"/tools/geckodriver.exe"

    def open_brower(self):
        config = ConfigParser()#用于读取配置信息
        # file_path=os.path.dirname(os.path.abspath(".")+"config/config.ini")
        config.read("C:/Users/Administrator/PycharmProjects/untitled/config/config.ini")
        # config.read(file_path)
        url = config.get("testServer", "URL")
        browser = config.get("browserType", "browserName")

        logger.info("The test server url is :%s" % browser)#将使用的浏览器写入日志文件

        logger.info("The test server url is :%s"% url)#将网址写入日志文件
        #根据配置文件选择的浏览器选择打开该浏览器的驱动模块
        if browser=="Firefox":
            self.driver=webdriver.Firefox(executable_path=self.firefox_driver_path)
            logger.info("Starting firefox brower.")
        elif browser=="Chrome":
            self.driver=webdriver.Chrome(self.chrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser=="IE":
            self.driver=webdriver.Ie(self.ie_driver_path)
            logger.info("Starting IE browser.")

        self.driver.get(url)#打开网址
        logger.info("Open url:%s"%url)#将网址输入到日志文件
        self.driver.maximize_window()#窗口最大化
        logger.info("Maximize the current window.")
        self.driver.implicitly_wait(10)#隐士等待10秒
        logger.info("Set implicitly wate 10 seconds.")
        return self.driver

    def quit_browser(self):
        logger.info("Now,Close and quit the browser.")
        self.driver.quit()#关闭网页
if __name__=="__main__":
    b=BrowserEngine()
    b.open_brower()