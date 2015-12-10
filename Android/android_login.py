import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class LoginPrimary(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['device'] = 'Android'
		desired_caps['browserName'] = ''
		desired_caps['version'] = '4.4'
		desired_caps['app'] = ''
		desired_caps['app-package'] = 'com.amino.ui'
		desired_caps['app-activity'] = 'rtsp.connecthomestg.ui.SplashScreen'
		self.verificationErrors = []
		self.driver = webdriver.Remote('http://10.172.2.98:4723/wd/hub', desired_caps)

	def test_login_primary(self):
		driver = self.driver
		print "Waiting 10s"
		time.sleep(10)
		print "Finding Username element"
		driver.find_element_by_id("com.amino.ui:id/txtUserName")
		print "Entering Username"
		driver.find_element_by_id("com.amino.ui:id/txtUserName").send_keys("rayres")
		print "Finding Password element"
		driver.find_element_by_id("com.amino.ui:id/txtPassword").click()
		#driver.find_element_by_id("com.amino.ui:id/txtPassword").clear()
		print "Entering Password"
		driver.find_element_by_id("com.amino.ui:id/txtPassword").send_keys("planet07", "\ue007")
		for i in range(10):
			try:
				print "Checking User has bee logged in"
				if "Ray" == driver.find_element_by_id("com.amino.ui:id/tvUser").text: break
			except: pass
			time.sleep(1)
		else: self.fail("time out")

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
