#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class hmcSanityTests(unittest.TestCase):
	def setUp(self):
		print "Test: Home Reach App - Login -> Logout"
		print "======================================"
		print "Waiting for App to install and launch..."
		desired_caps = {}
		desired_caps['name'] = 'Android_v2.2: Login/Logout'
		desired_caps['device'] = 'Android'
		desired_caps['browserName'] = ''
		#4.2 API level 17 is the lowest level of API supported by Appium-Webdriver.  Use Appium-Selendroid for API versions <17)
		#SauceLabs @04/03/14 support Android 2.3, 4.0, 4.1, 4.2, 4.3
		desired_caps['version'] = '4.2'
		#desired_caps['app'] = 'sauce-storage:homereach.zip'
		desired_caps['app'] = '/home/sqa/Downloads/07022014.apk'
		#desired_caps['launch'] = 'true'
		desired_caps['app-package'] = 'com.connecthome.ui'
		#Depricated: desired_caps['app-package'] = 'com.amino.ui'
		desired_caps['app-activity'] = 'rtsp.connecthomestg.ui.SplashScreen'
		#desired_caps['app-wait-activity'] = 'rtsp.connecthomestg.ui.LoginScreen'
		self.verificationErrors = []
		#SAUCE_USERNAME = 'rayres'
		#SAUCE_ACCESS_KEY = '3892ef3f-6917-476f-aa3c-bb7efd45c1b2'
		#SAUCE_USERNAME = 'amino-slabs1'
		#SAUCE_ACCESS_KEY = 'be2b4708-75d6-4ed2-a7cd-947615b39bce'
		#self.driver = webdriver.Remote('http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (SAUCE_USERNAME, SAUCE_ACCESS_KEY), desired_caps)
		self.driver = webdriver.Remote('http://10.172.2.98:4723/wd/hub', desired_caps)
	
	def test_loginLogout(self):
		driver = self.driver				
		print ">"
		print "Test now in progress:"
		print "> Waiting for Login screen..."
		for i in range(5):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				if currentActivity == "rtsp.connecthomestg.ui.LoginScreen": break
				print ">"
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: App has failed to open")
		print "   @ Login screen"		
		elements = driver.find_elements_by_tag_name("EditText")
		elements[0].send_keys("rayressoak")
		elements[1].send_keys("planet07")
		#driver.execute_script("mobile: tap",{ "touchCount": 1, "x": 298,"y": 455 })
		#time.sleep(1)
		driver.execute_script("mobile: keyevent",{ "keycode": 66 })
		#Check login was successful		
		print "> Logging-in..."
		for i in range(15):
			try:
				if "Ray" == driver.find_element_by_name("Ray").text: break
				#if "Ray" == driver.find_element_by_id("com.conn ecthome.ui:id/tvUser").text: break
				print ">"
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: log-in failed")
		print "   * User has logged-in"
		
		#Enter Settings Menu
		print "> Entering Settings Menu..."
		driver.find_element_by_name("Settings").click()
		time.sleep(5)
		currentActivity = driver.execute_script("mobile: currentActivity")
		if currentActivity == "rtsp.connecthomestg.ui.SettingsScrn":
			print "   @ Settings Menu"
		else: self.fail("Timeout: Unable to find Settings Menu")
		
		#Logout and check App closes
		print "> Logging-out and closing App..."
		driver.find_element_by_name("Logout").click()
		for i in range(10):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				print ">"
				if currentActivity == "com.android.launcher2.Launcher": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: App hasn't closed after 10 seconds")
		print "   * App has now closed"

	#Exception handler for elements that can't be found
	def is_element_present(self, how, what):
		try: self.driver.find_element(by=how, value=what)
		except NoSuchElementException, e: return False
		return True
    #Exception handler for an alert that can't be found
	def is_alert_present(self):
		try: self.driver.switch_to_alert()
		except NoAlertPresentException, e: return False
		return True
    
    #Capture alert text if present
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
    
    #Quit test and print any errors
	def tearDown(self):
		#self.driver.execute_script("mobile: reset")
		print "> Tear-down..."
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)		

if __name__ == "__main__":
    unittest.main()
