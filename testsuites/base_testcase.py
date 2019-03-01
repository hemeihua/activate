import unittest
from framework.browser_engine import BrowserEngine
class BaseTestCase(unittest.TestCase):

    def setUp(self):
        browser=BrowserEngine()
        self.driver=browser.open_brower()

    def tearDown(self):
        self.driver.quit()