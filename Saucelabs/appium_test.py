import os
from selenium import webdriver

desired_caps = {}
desired_caps['device'] = 'Android'
desired_caps['browserName'] = ''
desired_caps['version'] = '4.2'
desired_caps['app'] = 'sauce-storage:8HRb170114.zip'
desired_caps['app-package'] = 'com.amino.ui'
desired_caps['app-activity'] = 'com.amino.ui.login'

SAUCE_USERNAME = 'rayres'
SAUCE_ACCESS_KEY = '3892ef3f-6917-476f-aa3c-bb7efd45c1b2'

driver = webdriver.Remote('http://%s:%s@ondemand.saucelabs.com:80/wd/hub' % (SAUCE_USERNAME, SAUCE_ACCESS_KEY), desired_caps)

el = driver.find_element_by_test("Home")
#el.click()

#el = driver.find_element_by_tag_name("textfield")
#el.send_keys("This is a new note!")

#el = driver.find_element_by_name("Save")
#el.click()

#els = driver.find_elements_by_tag_name("text")
#assert els[2].text == "This is a new note!"

#els[2].click()

#def tearDown(self):
#print("Link to your job: https://saucelabs.com/jobs/%s" % self.driver.session_id)
driver.quit()

