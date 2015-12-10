#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

delay1 = 5
delay2 = 15
delay3 = 30
delay4 = 35

driver = webdriver.Firefox()
driver.implicitly_wait(delay2)
target = "https://homereach.aminocom.com"
#target = "http://stgbetaamino.intamac.com"

def getTime():
    try:
        driver.get(target)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres-prodlive1")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()

        WebDriverWait(driver, delay3).until(EC.invisibility_of_element_located((By.ID, "divFlashVersion")))

        driver.find_element_by_xpath("(//a[contains(text(),'Equipment')])[2]").click()

        if "Streaming" == driver.find_element_by_id("ctl00_bodyContent_grdViewViewEquipment_ctl02_lblStatusView").text:
            print("Camera is streaming")
            for loop in range(120):
                try:
                    begin = time.time()
                    if "Online" == driver.find_element_by_id("ctl00_bodyContent_grdViewViewEquipment_ctl02_lblStatusView").text:
                    print("Camera has stopped streaming")
                    end = time.time()
                    break

        else:
            print("Camera is not streaming")

    except Exception as e:
            print e
            driver.quit()

    finally:
            driver.quit()

if __name__ == '__main__':
    getTime()







