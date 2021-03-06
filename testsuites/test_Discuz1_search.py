import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz1_homepage import  HomePage
from pageobjects.Discuz_base import DiscuzBase

class DiscuzSearch1(BaseTestCase):

    def test_Discuz1_search(self):
        homePage = HomePage(self.driver)
        discuzBase=DiscuzBase(self.driver)

        discuzBase.search("admin","hemeihua")
        indexAssert = self.driver.find_element_by_css_selector(".vwmy a")
        assert "admin" in indexAssert.text

        homePage.deletesearch()

        homePage.managesearch("hemeihua")
        indexAssert = self.driver.find_element_by_css_selector(".uinfo em")
        assert "admin" in indexAssert.text

        homePage.setupmodule("nows")

        homePage.close()

        discuzBase.search("hemei","hemeihua")

        homePage.fatiesearch("holle","good,good,good,good,good,good,good,good,good,good,good,good,good,good,")

        homePage.huitiesearch("this is a good,this is a good")


if __name__=="__main__":
    unittest.main(verbosity=2)