from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time


class HomePage(BasePage):
    # 发帖
    home_page_button_morenfatie_search_loc = (By.CSS_SELECTOR, ".fl_tb h2 a")
    home_page_input_fatiename_search_loc = (By.NAME, "subject")
    home_page_input_fatiewenzhang_search_loc = (By.NAME, "message")
    home_page_button_fatie_search_search_loc = (By.CSS_SELECTOR, ".bm_c button")
    # 回帖
    home_page_input_huifutiezi_search_loc = (By.NAME, "message")
    home_page_button_huifu_search_loc = (By.CSS_SELECTOR, ".ptm button")

    def fatiesearch(self, fatiename, fatiewenzhang):
        self.click(*self.home_page_button_morenfatie_search_loc)
        self.sendkeys(fatiename, *self.home_page_input_fatiename_search_loc)
        self.sendkeys(fatiewenzhang, *self.home_page_input_fatiewenzhang_search_loc)
        self.click(*self.home_page_button_fatie_search_search_loc)
        time.sleep(2)

    def huitiesearch(self, huifutiezi):
        self.sendkeys(huifutiezi, *self.home_page_input_huifutiezi_search_loc)
        self.click(*self.home_page_button_huifu_search_loc)
        time.sleep(2)
