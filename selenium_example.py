#!/usr/bin/python

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# go to the google home page
driver.get("https://trials.aminocom.com")

# find the element
username = driver.find_element_by_id("username")

# type name
username.send_keys("rayres")

# submit the form
#username.submit()

login = driver.find_element_by_value("Go")
login.click()
login.submit()

# the page is ajaxy so the title is originally this:
print driver.title

try:
    # we have to wait for the page to refresh, the last thing that seems to be updated is the title
    WebDriverWait(driver, 10).until(EC.title_contains("Amino"))

    # You should see "cheese! - Google Search"
    print driver.title

finally:
    driver.quit()
