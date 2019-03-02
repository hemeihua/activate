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

        homePage.voteteizi("title","good good good good good goodgoodgood goodgoodgood")

        homePage.voteticket("this is good","this not is good","1")

        homePage.setupvote()

        a=homePage.toupianxuanxiang()
        n = ""
        n1 = ""
        n2 = ""
        n3 = ""
        n4 = ""
        for i in a:
            n=i.text
        a = homePage.toupianxuanxiang1()
        for i in a:
            n1 = i.text
        a = homePage.toupianxuanxiang2()
        for i in a:
            n2 = i.text
        a = homePage.toupianxuanxiang3()
        for i in a:
            n3 = i.text
        a = homePage.toupianxuanxiang4()
        for i in a:
            n4 = i.text
        result = n
        result1 = n1
        result2 = n2
        result3 = n3
        result4 = n4
        self.assertEqual(result, expect_value, msg=result)
        self.assertEqual(result1, expect_value1, msg=result1)
        self.assertEqual(result2, expect_value2, msg=result2)
        self.assertEqual(result3, expect_value3, msg=result3)
        self.assertEqual(result4, expect_value4, msg=result4)
        discuzbase.tuichu()

if __name__=="__main__":
    unittest.main(verbosity=2)