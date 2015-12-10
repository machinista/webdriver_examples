from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)
        self.base_url = "https://trials.aminocom.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_logout(self):
        driver = self.driver
        driver.get("https://trials.amincom.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        self.assertEqual("rayres", driver.find_element_by_id("ctl00_lblLoggedInName").text)
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
