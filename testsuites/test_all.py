import sys
sys.path.append(r"C:\Users\Administrator\PycharmProjects\search")
import unittest
import HTMLTestRunner
import os
import time
from testsuites.test_Discuz_search import DiscuzSearch
from testsuites.test_Discuz1_search import DiscuzSearch1
from testsuites.test_Discuz2_search import DiscuzSearch2
from testsuites.test_Discuz3_search import DiscuzSearch3


cur_path=os.path.dirname(os.path.realpath(__file__))
# cur_path=os.path.dirname(os.path.abspath("."))
report_path=os.path.join(cur_path,"report/")
if not os.path.exists(report_path): os.mkdir(report_path)

suite=unittest.TestSuite()
suite.addTest(unittest.makeSuite(DiscuzSearch))
suite.addTest(unittest.makeSuite(DiscuzSearch1))
suite.addTest(unittest.makeSuite(DiscuzSearch2))
suite.addTest(unittest.makeSuite(DiscuzSearch3))


if __name__=="__main__":
    now=time.strftime(("%Y-%m-%d-%H-%M-%S"),time.localtime(time.time()))
    html_report=report_path+now+"result1.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="单元测试报告",description="单元测试用例")
    runner.run(suite)