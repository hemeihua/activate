import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import  HomePage
from pageobjects.Discuz_base import DiscuzBase


class DiscuzSearch(BaseTestCase):

    def test_Discuz_search(self):
        homePage = HomePage(self.driver)
        discuzBase = DiscuzBase(self.driver)

        discuzBase.search("hemei", "hemeihua")
        indexAssert = self.driver.find_element_by_css_selector(".vwmy a")
        assert "hemei" in indexAssert.text

        homePage.fatiesearch("hhhhhh", "mmmmhhhhhhhhhhhhhhmm")
        indexAssert = self.driver.find_element_by_css_selector(".vwthd h1 span")
        assert "hhhhhh" in indexAssert.text

        homePage.huitiesearch("ii这是个好办法iii")

        discuzBase.tuichu()

if __name__=="__main__":
    unittest.main(verbosity=2)


