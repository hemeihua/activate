import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.baidu_homepage import HomePage
from selenium.webdriver.common.keys import Keys

class BaiduSearch(BaseTestCase):

    def test_baidu_search(self):
        homePage=HomePage(self.driver)
        homePage.search("hhhhhh"+Keys.RETURN)

if __name__=="__main__":
    unittest.main(verbosity=2)
