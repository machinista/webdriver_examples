#!/usr/bin/env python

from selenium import webdriver
from applitools.eyes import Eyes
from applitools import logger
from applitools.logger import StdoutLogger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


import time

def userLogin():
    #Set options so that Chrome starts fullscreen
    logger.set_logger(StdoutLogger())
    #options = webdriver.ChromeOptions();
    #options.add_argument("--start-maximized");

    eyes = Eyes()
    eyes.api_key = 'VOfLF4XBAbbMmsOLf0BxDx4APw7gCynQz7NjZwRG1076g110'
    #eyes.force_full_page_screenshot=True

    # Get a selenium web driver object.
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # Make sure to use the returned driver from this point on.
    # Use the following line for a specific viewport_size (WSVGA 16:9)
    driver = eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash', viewport_size={'width': 1024, 'height': 600})
    # No viewport size set - using fullscreen
    # driver = eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash')
    # Work-around for eyes SDK issue
    # eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash')
    
    
    driver.get('https://homereach.aminocom.com')
       
    # Visual validation point #1
    #eyes.check_window('Login Page')
        
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("rayres-trialsbeta1")
    driver.find_element_by_id("username").send_keys(u'\ue004')
    driver.find_element_by_id("userpassword").clear()
    driver.find_element_by_id("userpassword").send_keys("planet07")
    driver.find_element_by_id("cmdLogin").click()
       
    #selenium.webdriver.support.expected_conditions.invisibility_of_element_located(locator)
    #element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "divFlashVersion"))
    element = WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.ID, "divFlashVersion")))
    
    try:
        for i in range(20):
            try:
                flashCheck = driver.find_element_by_id("divFlashVersion")
                print flashCheck
                if flashCheck != driver.find_element_by_id("divFlashVersion"):
					print "Flash version check"
					print flashCheck
					time.sleep(1)
					continue
                elif flashCheck == driver.find_element_by_id("divFlashVersion"):
					print "No Flash check"
					print flashCheck
					if driver.find_element_by_id("flashImg1"):
						# Visual validation point #2
						#eyes.check_window('Dashboard')
						print "Found flashImg1"
						driver.find_element_by_link_text("Logout").click()
						print 'Logging out'
						break
            except Exception as e:
                print e
                print 'Wait..'
                time.sleep(1)
             
        # End visual testing. Validate visual correctness.
        eyes.close()

    except Exception as e:
        print e

    finally:
        driver.quit()
        eyes.abort_if_not_closed()

if __name__ == '__main__':
    userLogin()
