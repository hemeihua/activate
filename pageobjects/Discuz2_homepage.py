from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time

class HomePage(BasePage):
    # 搜索帖子
    home_page_input_searchtiezi_search_loc = (By.NAME, "srchtxt")
    home_page_button_search_search_loc = (By.CSS_SELECTOR, ".scbar_btn_td button")
    # 进入搜索帖子页面
    home_page_input_huifutiezi_search_loc = (By.NAME, "message")
    home_page_button_huifu_search_loc = (By.CSS_SELECTOR, ".ptm button")
    def searchtiezi(self, searchtiezi):
        self.sendkeys(searchtiezi, *self.home_page_input_searchtiezi_search_loc)
        self.click(*self.home_page_button_search_search_loc)
        time.sleep(2)
        self.activate_window(1)
        time.sleep(2)
        self.get_window_img()
    def verfiy(self):
        time.sleep(2)
        self.activate_window(1)
        return self.driver.find_element_by_css_selector(".pbw font")
