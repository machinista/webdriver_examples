#!/usr/bin/env python

from selenium import webdriver
from applitools.eyes import Eyes
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from applitools import logger
from applitools.logger import StdoutLogger
import time

delay1 = 5
delay2 = 15
delay3 = 30
delay4 = 35
eyes = Eyes()
eyes.api_key = 'VOfLF4XBAbbMmsOLf0BxDx4APw7gCynQz7NjZwRG1076g110'
logger.set_logger(StdoutLogger())
driver = webdriver.Firefox()
driver.implicitly_wait(delay2)
driver = eyes.open(driver=driver, app_name='Home Reach', test_name='Dashboard Navigation v2', viewport_size={'width': 1366, 'height': 768})
target = "https://homereach.aminocom.com"

def dashNav():
    try:
        driver.get(target)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres-prodlive1")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        
        element = WebDriverWait(driver, delay3).until(EC.invisibility_of_element_located((By.ID, "divFlashVersion")))
        
        element = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "flashImg1")))
        # Visual validation point
        eyes.check_window('Dashboard Home')
        
   
    except Exception as e:
            print e
            driver.quit()
            # End visual testing. Validate visual correctness.
            eyes.close()

    finally:
            driver.quit()
            # End visual testing. Validate visual correctness.
            eyes.close()

if __name__ == '__main__':
    dashNav()
