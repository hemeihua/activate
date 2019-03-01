from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
from framework.browser_engine import BrowserEngine
import time
class HomePage(BasePage):
    # 删除帖子
    home_page_button_morenfatie_search_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    home_page_button_gouxuan_search_loc = (By.CSS_SELECTOR, ".o input")
    home_page_button_delete_search_loc = (By.CSS_SELECTOR, ".bm_c  p a")
    home_page_button_ture_search_loc = (By.CSS_SELECTOR, ".o  button span")
    # 进入管理中心
    home_page_button_mangecenter_search_loc = (By.XPATH, "//body/div[6]/div/div/div/p/a[6]")
    home_page_input_truepassword_search_loc = (By.XPATH, "//form/p[4]/input")
    home_page_button_truepassword_search_loc = (By.XPATH, "//form/p[9]/input")
    home_page_button_BBS_search_loc = (By.XPATH, "//ul/li[7]/em/a")
    # 建立新的模块
    home_page_button_setupmodule_search_loc = (By.CSS_SELECTOR, ".lastboard .addtr")
    home_page_input_write_search_loc = (By.XPATH, "//html/body/div[3]/form/table/tbody[3]/tr/td[3]/div/input")
    home_page_button_submit_search_loc = (By.NAME, "editsubmit")
    # 管理中心关闭
    home_page_button_managequit_search_loc = (By.CSS_SELECTOR, ".mainhd div p a")
    home_page_button_first_search_loc = (By.CSS_SELECTOR, ".wp .a a")
    home_page_button_quit_search_loc = (By.XPATH, "//p/a[7]")
    #在新的模块发帖
    home_page_button_newmodule_search_loc = (By.CSS_SELECTOR,"table tbody .fl_row:nth-last-child(2) h2 a")
    home_page_input_fatiename_search_loc = (By.NAME, "subject")
    home_page_input_fatiewenzhang_search_loc = (By.NAME, "message")
    home_page_button_fatie_search_search_loc = (By.CSS_SELECTOR, ".bm_c button")
    # 回帖
    home_page_input_huifutiezi_search_loc = (By.NAME, "message")
    home_page_button_huifu_search_loc = (By.CSS_SELECTOR, ".ptm button")

    def deletesearch(self):
        self.click(*self.home_page_button_morenfatie_search_loc)
        self.click(*self.home_page_button_gouxuan_search_loc)
        self.click(*self.home_page_button_delete_search_loc)
        self.click(*self.home_page_button_ture_search_loc)
        time.sleep(2)
    def managesearch(self,password):
        self.click(*self.home_page_button_mangecenter_search_loc)
        time.sleep(2)
        #激活第二个页面
        self.activate_window(1)
        time.sleep(5)
        self.sendkeys(password,*self.home_page_input_truepassword_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_truepassword_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_BBS_search_loc)
        time.sleep(2)
    def setupmodule(self,writemodule):
        time.sleep(2)
        self.activate_window(1)
        self.driver.switch_to.frame(0)
        self.click(*self.home_page_button_setupmodule_search_loc)
        time.sleep(2)
        self.sendkeys(writemodule,*self.home_page_input_write_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_submit_search_loc)
        time.sleep(2)
        # self.driver.switch_to.frame(0)
    def close(self):
        self.activate_window(1)
        self.click(*self.home_page_button_managequit_search_loc)
        time.sleep(2)
        self.activate_window(0)
        time.sleep(5)
        self.click(*self.home_page_button_first_search_loc)
        self.click(*self.home_page_button_quit_search_loc)
        time.sleep(2)
    def fatiesearch(self,fatiename,fatiewenzhang):
        self.click(*self.home_page_button_newmodule_search_loc)
        time.sleep(2)
        self.sendkeys(fatiename, *self.home_page_input_fatiename_search_loc)
        time.sleep(2)
        self.sendkeys(fatiewenzhang, *self.home_page_input_fatiewenzhang_search_loc)
        time.sleep(2)
        self.click(*self.home_page_button_fatie_search_search_loc)
        time.sleep(2)
    def huitiesearch(self,huifutiezi):
        self.sendkeys(huifutiezi, *self.home_page_input_huifutiezi_search_loc)
        self.click(*self.home_page_button_huifu_search_loc)
        time.sleep(2)