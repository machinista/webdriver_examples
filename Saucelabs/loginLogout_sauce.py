import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['version'] = '11'
        desired_capabilities['platform'] = 'Windows 8.1'
        desired_capabilities['name'] = 'Login Logout Testing at Sauce Labs'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://rayres:3892ef3f-6917-476f-aa3c-bb7efd45c1b2@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_login_logout(self):
        driver = self.driver
        driver.get("https://trials.aminocom.com")
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayressoak")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        self.assertEqual("rayressoak", driver.find_element_by_id("ctl00_lblLoggedInName").text)
        driver.find_element_by_link_text("Logout").click()

    def tearDown(self):
        print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
