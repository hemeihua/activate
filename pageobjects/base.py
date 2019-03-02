from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from framework.logger import Logger
# import logging
import time
import os.path
logger=Logger(logger="BasePage").getlog()#判断是哪个class输出的日志信息
class BasePage(object):

    def __init__(self,driver):
        self.driver=driver

    def back(self):
        self.driver.back()
        logger.info("Click back on current page.")
        self.get_window_img()

    def forword(self):
        self.driver.forward()
        logger.info("Click back on current page.")
        self.get_window_img()

    def open_url(self,url):
        self.driver.get(url)

    def activate_window(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])

    def quit_browser(self):
        self.driver.quit()

    def close(self):
        try:
            self.driver.close()
        except Exception as e:
            print()

    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc))
            ele=self.driver.find_element(*loc)
            return ele
            logger.info("找到页面元素-->%s"%ele)
            self.get_window_img()
        except:
            logger.error("%s页面中未能找到%s元素"%(self,loc))
            self.get_window_img()

    def get_window_img(self):
        file_path=os.path.dirname(os.path.abspath("."))+"/screenshots/"
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        screen_name=file_path+rq+".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("Had take screenshot and save to folder:/screenshots")
        except Exception as e:
            self.driver.get_screenshot_as_file(screen_name)
            logger.error("Failed to take screenshot! %s"%e)

    def sendkeys(self,text,*loc):
        el=self.find_element(*loc)

        try:
            el.clear()
            el.send_keys(text)
            logger.info("输入内容%s"%text)
        except Exception as e:
            logger.error("Failed to type in input boxwith %s"%e)
            self.get_window_img()

    def clean(self,*loc):
        el=self.find_element(*loc)
        try:
            el.clear()
        except Exception as e:
            self.get_window_img()

    def click(self,*loc):
        el=self.find_element(*loc)
        try:
            el.click()
            logger.info("this element %s was clicked"%el.text)
            self.get_window_img()
        except Exception as e:
            logger.error("Failed to click the element with %s"%e)
            self.get_window_img()
