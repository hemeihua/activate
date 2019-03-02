from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time

class HomePage(BasePage):
    # 投票帖子
    home_page_button_morenfatie_search_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    home_page_button_votefatie_search_loc=(By.CSS_SELECTOR,".bw0 a img")
    home_page_input_title_search_log=(By.NAME,"subject")
    home_page_input_article_search_loc=(By.CSS_SELECTOR,"body")
    home_page_button_fapiaotiezi_search_loc=(By.CSS_SELECTOR,".ct2_a .mbw li:last-child a")
    #投票
    home_page_input_option_search_loc=(By.CSS_SELECTOR,".sppoll div:nth-child(4) p:nth-child(1) input")
    home_page_input_option1_search_loc = (By.CSS_SELECTOR, ".sppoll div:nth-child(4) p:nth-child(2) input")
    home_page_input_day_search_loc=(By.NAME,"expiration")
    home_page_button_resultwatch_search_loc=(By.NAME,"visibilitypoll")
    home_page_button_public_search_loc=(By.NAME,"overt")
    home_page_button_voteture_search_loc=(By.CSS_SELECTOR,".pnpost .pnc span:nth-child(1)")
    #建立投票
    home_page_button_setupvote_search_loc=(By.CSS_SELECTOR,".pslt input")
    home_page_button_votesubmit_search_loc=(By.CSS_SELECTOR,".pn span")
    def voteteizi(self,title,article):
        self.click(*self.home_page_button_morenfatie_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_votefatie_search_loc)
        time.sleep(2)
        self.sendkeys(title,*self.home_page_input_title_search_log)
        self.driver.switch_to.frame(0)
        self.sendkeys(article,*self.home_page_input_article_search_loc)

        time.sleep(2)
    def voteticket(self,option,option1,day):
        self.activate_window(0)
        self.click(*self.home_page_button_fapiaotiezi_search_loc)
        time.sleep(2)
        self.sendkeys(option,*self.home_page_input_option_search_loc)
        self.sendkeys(option1,*self.home_page_input_option1_search_loc)
        self.sendkeys(day,*self.home_page_input_day_search_loc)
        self.click(*self.home_page_button_resultwatch_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_public_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_voteture_search_loc)
        time.sleep(2)
    def setupvote(self):
        self.click(*self.home_page_button_setupvote_search_loc)
        self.click(*self.home_page_button_votesubmit_search_loc)
    def toupianxuanxiang(self):
        xuanpiao=self.driver.find_element_by_css_selector(".pcht table tbody tr:nth-child(1) td label")
        return xuanpiao
    def toupianxuanxiang1(self):
        xuanpiao1 = self.driver.find_element_by_css_selector(".pcht table tbody tr:nth-child(3) td label")
        return xuanpiao1
    def toupianxuanxiang2(self):
        bili = self.driver.find_element_by_css_selector(".pcht table tbody tr:nth-child(2) td:nth-child(2)")
        return bili
    def toupianxuanxiang3(self):
        bili1 = self.driver.find_element_by_css_selector(".pcht table tbody tr:nth-child(4) td:nth-child(2)")
        return bili1
    def toupianxuanxiang4(self):
        toupiaotitle = self.driver.find_element_by_css_selector(".vwthd  h1 span")
        return toupiaotitle












