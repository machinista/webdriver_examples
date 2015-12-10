#! /usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class TempDeleteUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://trials.aminocom.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_temp_delete_user(self):
        driver = self.driver
        driver.get("https://trials.aminocom.com")
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
        driver.find_element_by_xpath("//div[@id='main']/div/div/div[2]/div[7]/div/a/b").click()
        for i in range(60):
            try:
                if "My Friends" == driver.find_element_by_css_selector("h1").text: break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("input.btnThin.float-right").click()
        for i in range(60):
            try:
                if self.is_element_present(By.CSS_SELECTOR, "#ui-dialog-title-1 > h1"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_id("btnFrmDeleteSubmit").click()
        for i in range(60):
            try:
                if not self.is_element_present(By.XPATH, "//body/div[2]/div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        driver.find_element_by_css_selector("#ctl00_bodyContent_divTimer > div").click()
        for i in range(60):
            try:
                if not self.is_element_present(By.CSS_SELECTOR, "#ctl00_bodyContent_divTimer > div"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
        for i in range(60):
            try:
                if self.is_element_present(By.LINK_TEXT, "Logout"): break
            except: pass
            time.sleep(1)
        else: self.fail("time out")
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
