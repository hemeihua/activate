import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz_homepage import  HomePage
from pageobjects.Discuz_base import DiscuzBase

class DiscuzSearch(BaseTestCase):

    def test_Discuz_search(self):
        homePage = HomePage(self.driver)
        discuzBase = DiscuzBase(self.driver)
        discuzBase.search("hemei", "hemeihua")
        homePage.fatiesearch("hhhhhh", "mmmmhhhhhhhhhhhhhhmm")
        homePage.huitiesearch("ii这是个好办法iii")
        discuzBase.tuichu()

if __name__=="__main__":
    unittest.main(verbosity=2)


