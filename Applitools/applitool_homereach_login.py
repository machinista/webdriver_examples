#!/usr/bin/env python2.7.9

from selenium import webdriver
from applitools.eyes import Eyes
#from applitools import logger
#from applitools.logger import StdoutLogger
from selenium.webdriver.common.keys import Keys
import time

def userLogin():
    #Set options so that Chrome starts fullscreen
    logger.set_logger(StdoutLogger())
    options = webdriver.ChromeOptions();
    options.add_argument("--start-maximized");

    eyes = Eyes()
    eyes.api_key = 'VOfLF4XBAbbMmsOLf0BxDx4APw7gCynQz7NjZwRG1076g110'
    eyes.force_full_page_screenshot=True

    # Get a selenium web driver object.
    # driver = webdriver.Chrome(chrome_options=options)
    driver = webdriver.Firefox()
    # driver = webdriver.Chrome()
    # Make sure to use the returned driver from this point on.
    # Use the following line for a specific viewport_size (WSVGA 16:9)
    eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash', viewport_size={'width': 1136, 'height': 640})
    # No viewport size set - using fullscreen
    # driver = eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash')
    # Work-around for eyes SDK issue
    # eyes.open(driver=driver, app_name='Home Reach', test_name='Login to Dash')

    try:
        driver.get('https://homereach.aminocom.com')

        # Visual validation point #1
        eyes.check_window('Login Page')

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres-prodlive1")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()

        for i in range(10):
            try:
                if driver.find_element_by_id("flashImg1"):
                    # Visual validation point #2
                    #eyes.check_window('Dashboard')
                    driver.find_element_by_link_text("Logout").click()
                    print 'Logging out'
                    break
            except Exception as e:
                print 'Wait..'
                time.sleep(1)
        else:
            return 'Element not found'

        # End visual testing. Validate visual correctness.
        eyes.close()

    except Exception as e:
        print e

    finally:
        driver.quit()
        eyes.abort_if_not_closed()

if __name__ == '__main__':
    userLogin()
