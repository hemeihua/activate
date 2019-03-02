import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz2_homepage import  HomePage
from pageobjects.Discuz_base import DiscuzBase
from ddt import ddt,data,unpack

@ddt
class DiscuzSearch2(BaseTestCase):

    @data(["haotest"])
    @unpack
    def test_Discuz2_search(self,expect_value):
        homePage = HomePage(self.driver)
        discuzBase = DiscuzBase(self.driver)

        discuzBase.search("hemei","hemeihua")
        indexAssert = self.driver.find_element_by_css_selector(".vwmy a")
        assert "hemei" in indexAssert.text

        homePage.searchtiezi("haotest")
        n = homePage.verfiy()

        discuzBase.tuichu()
        result = n.test
        self.assertEqual(result,expect_value,msg=result)

if __name__=="__main__":
    unittest.main(verbosity=2)