
from configparser import ConfigParser

config = ConfigParser()
config.read('C:/Users/Administrator/PycharmProjects/untitled/config/config.ini')
browser = config.get("testServer", "URL")
c=config.get("browserType","browserName")
print(browser)
print(c)