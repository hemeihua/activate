import unittest
from testsuites.base_testcase import BaseTestCase
from pageobjects.Discuz3_homepage import  HomePage
from pageobjects.Discuz_base import DiscuzBase
from ddt import ddt,data,unpack

@ddt
class DiscuzSearch3(BaseTestCase):

    @data(["1.  this is good","2.  this not is good","100.00% (1)","0.00% (0)","title"])
    @unpack
    def test_Discuz4_search(self,expect_value,expect_value1,expect_value2,expect_value3,expect_value4):
        homePage = HomePage(self.driver)
        discuzbase=DiscuzBase(self.driver)

        discuzbase.search("admin","hemeihua")
        indexAssert = self.driver.find_element_by_css_selector(".vwmy a")
        assert "admin" in indexAssert.text

        homePage.voteteizi("title","good good good good good goodgoodgood goodgoodgood")

        homePage.voteticket("this is good","this not is good","1")

        homePage.setupvote()

        a=homePage.toupianxuanxiang()

        a1 = homePage.toupianxuanxiang1()

        a2 = homePage.toupianxuanxiang2()

        a3= homePage.toupianxuanxiang3()

        a4 = homePage.toupianxuanxiang4()

        result = a.text
        result1 = a1.text
        result2 = a2.text
        result3 = a3.text
        result4 = a4.text
        self.assertEqual(result, expect_value, msg=result)
        self.assertEqual(result1, expect_value1, msg=result1)
        self.assertEqual(result2, expect_value2, msg=result2)
        self.assertEqual(result3, expect_value3, msg=result3)
        self.assertEqual(result4, expect_value4, msg=result4)

        discuzbase.tuichu()
        indexAssert = self.driver.find_element_by_css_selector(".vwmy a")
        assert "hemei" not in indexAssert.text
if __name__=="__main__":
    unittest.main(verbosity=2)