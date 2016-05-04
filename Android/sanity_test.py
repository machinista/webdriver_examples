#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class sanityTest(unittest.TestCase):

	def setUp(self):
		#To-do: add a timeout catch
		print "Beginning setup phase..."
		desired_caps = {}
		desired_caps['name'] = 'Sanity Test'
		desired_caps['device'] = 'Android'
		desired_caps['browserName'] = ''
		desired_caps['version'] = '4.2'
		desired_caps['app'] = '/home/sqa/Downloads/07022014.apk'
		desired_caps['launch'] = 'true'
		desired_caps['app-package'] = 'com.connecthome.ui'
		#Depricated: desired_caps['app-package'] = 'com.amino.ui'
		desired_caps['app-activity'] = 'rtsp.connecthomestg.ui.SplashScreen'
		desired_caps['app-wait-activity'] = 'rtsp.connecthomestg.ui.LoginScreen'
		self.verificationErrors = []
		self.driver = webdriver.Remote('http://10.172.2.98:4723/wd/hub', desired_caps)

	def test_sanity_test(self):
		driver = self.driver				
		print "  > Test now in progress"
		for i in range(5):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				if currentActivity == "rtsp.connecthomestg.ui.LoginScreen": break
				print "> Waiting for Login screen"
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: App has failed to open")
		print "Logging-in..."
		
		elements = driver.find_elements_by_tag_name("EditText")
		elements[0].send_keys("rayressoak")
		elements[1].send_keys("planet07")
		driver.execute_script("mobile: keyevent",{ "keycode": 66 })
		#Check login was successful		
		for i in range(10):
			try:
				print "  * waiting for authentication"
				if "Ray" == driver.find_element_by_name("Ray").text: break
				#if "Ray" == driver.find_element_by_id("com.connecthome.ui:id/tvUser").text: break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Log-in failed")
		print "  > User has logged-in"
		
		print "Entering Camera UI..."
		elements = driver.find_elements_by_tag_name("Button")
		elements[2].click()
		#currentActivity = driver.execute_script("mobile: currentActivity")
		#print currentActivity
		for i in range(10):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				print "  * waiting for Camera UI"
				if currentActivity == "rtsp.connecthomestg.ui.CameraScrn": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Unable to open Camera UI")
		print "  > Now in Camera UI"
		#Need to wait for recordings list to load
		time.sleep(10)
		
		print "Opening Video Player..."
		elements = driver.find_elements_by_tag_name("Button")
		elements[3].click()
		#time.sleep(10)
		#currentActivity = driver.execute_script("mobile: currentActivity")
		#print currentActivity
		for i in range(15):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				print "  * waiting for Video Player to open"
				if currentActivity == ".VideoPlayer": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Unable to open Live video UI")
		print "  > Video Player is now open"
		print "Sleeping for 30s"
		time.sleep(30)
		#currentActivity = driver.execute_script("mobile: currentActivity")
		#print currentActivity
		print "Checking Video Player is still open..."
		for i in range(1):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				if currentActivity == ".VideoPlayer": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Video Player has failed")
		print "  > Video Player is still open"

		#Logout and check App closes
		print "Preparing to log-out..."
		#Send a 'BACK' keyboard event
		driver.execute_script("mobile: keyevent",{ "keycode": 4 })
		for i in range(10):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				print "  * waiting to exit Video Player"
				if currentActivity == "rtsp.connecthomestg.ui.CameraScrn": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Could not exit Video Player")
		driver.find_element_by_name("Settings").click()
		for i in range(5):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				if currentActivity == "rtsp.connecthomestg.ui.SettingsScrn": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: Unable to open Settings Menu")
		print "  > now in Settings Menu"
		print "Logging out and closing App..."
		#driver.find_element_by_id("com.connecthome.ui:id/btnLogout").click()		
		driver.find_element_by_name("Logout").click()
		for i in range(10):
			try:
				currentActivity = driver.execute_script("mobile: currentActivity")
				print "  * waiting for App to close"
				if currentActivity == "com.android.launcher2.Launcher": break
			except: pass
			time.sleep(1)
		else: self.fail("Timeout: App hasn't closed after 10 seconds")
		print "  > App has now closed \o/"

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
		self.driver.quit()
		self.assertEqual([], self.verificationErrors)
		

if __name__ == "__main__":
    unittest.main()
