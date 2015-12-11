from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class JulianDay(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        #self.driver.get("qa-test2/testpages/julianDay.html")

    def test_title(self):
        driver = self.driver
        self.driver.get("qa-test2/testpages/julianDay.html")
        self.assertTrue("Julian Days", driver.title)

    def test_dayNumber(self):
        driver = self.driver
        self.driver.get("qa-test2/testpages/julianDay.html")
        self.assertTrue("145", driver.find_element_by_id("julianDay").text)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
