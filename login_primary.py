#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import subprocess

pwd = subprocess.communicate("ls")
print pwd

class LoginPrimary(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://trials.aminocom.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_login_primary(self):
        driver = self.driver
        driver.get("https://trials.aminocom.com")
        driver.maximize_window()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        for i in range(60):
            try:
                if "rayres" == driver.find_element_by_id("ctl00_lblLoggedInName").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
	driver.get_screenshot_as_file("~/screenshots/login_secondary.png")
	driver.find_element_by_link_text("Logout").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
