from selenium.webdriver.common.by import By
from pageobjects.base import BasePage
import time
class DiscuzBase(BasePage):
    # 用户登录
    home_page_input_username_search_loc = (By.NAME, "username")
    home_page_input_password_search_loc = (By.NAME, "password")
    home_page_button_search_loc = (By.CSS_SELECTOR, ".fastlg_l button em")
    # 退出
    home_page_button_tuichu_search_loc = (By.LINK_TEXT, "退出")
    def search(self,content,content1):
        self.sendkeys(content,*self.home_page_input_username_search_loc)
        self.sendkeys(content1,*self.home_page_input_password_search_loc)
        self.click(*self.home_page_button_search_loc)
        time.sleep(2)
    def tuichu(self):
        self.activate_window(0)
        self.click(*self.home_page_button_tuichu_search_loc)

