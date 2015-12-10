from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Delete(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://aminointaadmin.intamac.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_delete(self):
        driver = self.driver
        driver.get("https://aminointaadmin.intamac.com")
        driver.find_element_by_id("MainContent_LoginControl_UserName").clear()
        driver.find_element_by_id("MainContent_LoginControl_UserName").send_keys("Amino")
        driver.find_element_by_id("MainContent_LoginControl_Password").clear()
        driver.find_element_by_id("MainContent_LoginControl_Password").send_keys("275642")
        driver.find_element_by_id("MainContent_LoginControl_LoginButton").click()
        driver.find_element_by_id("MainContent_txtUsername").clear()
        driver.find_element_by_id("MainContent_txtUsername").send_keys("rayres-trials1")
        driver.find_element_by_id("MainContent_btnSearch").click()
        driver.find_element_by_link_text("Select").click()
        driver.find_element_by_id("MainContent_btnLoadDeleteAccount").click()
        driver.find_element_by_id("MainContent_btnDeleteAccount").click()
        driver.find_element_by_id("MainContent_btnDeleteAccountYes").click()
        driver.find_element_by_id("HeadLoginView_HeadLoginStatus").click()
    
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
