#!/usr/bin/env python

from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from applitools import logger
from applitools.logger import StdoutLogger

Eyes.api_key = 'VOfLF4XBAbbMmsOLf0BxDx4APw7gCynQz7NjZwRG1076g110' 
eyes = Eyes()
logger.set_logger(StdoutLogger())
driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver = eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash', viewport_size={'width': 1024, 'height': 600})

def userLogin():

    driver.get("https://homereach.aminocom.com")
    # Visual validation point #2
    # eyes.check_window('Dashboard')
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("rayres-trialsbeta1")
    driver.find_element_by_id("username").send_keys(u'\ue004')
    driver.find_element_by_id("userpassword").clear()
    driver.find_element_by_id("userpassword").send_keys("planet07")
    driver.find_element_by_id("cmdLogin").click()
    
    try:
        element = WebDriverWait(driver, 15).until(EC.invisibility_of_element_located((By.ID, "divFlashVersion")))
    except Exception as e:
        print e
    
    try:
        element = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "flashImg1")))
        # Visual validation point #2
        # eyes.check_window('Dashboard')
        driver.find_element_by_link_text("Logout").click()
    
    except Exception as e:
        print e
    
    finally:
        driver.quit()
        # End visual testing. Validate visual correctness.
        eyes.close()

if __name__ == '__main__':
    userLogin()
