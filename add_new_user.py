#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class AddNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
    
    def test_add_new_user(self):
        #login and check username
        driver = self.driver
        driver.get("https://trials.aminocom.com")
        driver.maximize_window()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        self.assertEqual("rayres", driver.find_element_by_id("ctl00_lblLoggedInName").text)
        #navigate to Friends menu and add new friend id
        driver.find_element_by_xpath("//div[@id='main']/div/div/div[2]/div[7]/div/a/b").click()
        self.assertEqual("My Friends", driver.find_element_by_css_selector("h1").text)
        driver.find_element_by_id("ctl00_bodyContent_btnPostCodeSearch").click()
        self.assertEqual("Add new friend", driver.find_element_by_css_selector("#ui-dialog-title-1 > h1").text)
        driver.find_element_by_id("txtFirstName").clear()
        driver.find_element_by_id("txtFirstName").send_keys("Ray")
        driver.find_element_by_id("txtSurname").clear()
        driver.find_element_by_id("txtSurname").send_keys("Res2")
        driver.find_element_by_id("txtEmail").clear()
        driver.find_element_by_id("txtEmail").send_keys("rayres@aminocom.com")
        driver.find_element_by_id("txtEmailConfirm").clear()
        driver.find_element_by_id("txtEmailConfirm").send_keys("rayres@aminocom.com")
        driver.find_element_by_id("btnFrmFriendSubmit").click()
        #check friend has been added
        self.assertEqual("Ray Res2", driver.find_element_by_xpath("//ul[@id='mycarousel']/li[2]/table/tbody/tr[2]/td[2]/div/a/h2").text)
        #add login details for newly added friend
        driver.find_element_by_css_selector("a.jqModalDlg.jqModalDlgHeight350 > img").click()
        driver.find_element_by_id("txtUsername").clear()
        driver.find_element_by_id("txtUsername").send_keys("rayres2")
        driver.find_element_by_id("txtPassword").clear()
        driver.find_element_by_id("txtPassword").send_keys("planet07")
        driver.find_element_by_id("txtSecurityQ").clear()
        driver.find_element_by_id("txtSecurityQ").send_keys("fave place")
        driver.find_element_by_id("txtSecurityA").clear()
        driver.find_element_by_id("txtSecurityA").send_keys("swavesey")
        driver.find_element_by_id("btnFrmLoginUserSubmit").click()
	#take a screenshot
	driver.get_screenshot_as_file("/home/rayres/screenshots/new_user.png")
        #logout
        driver.find_element_by_link_text("Logout").click()
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
