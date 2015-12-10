#!/usr/bin/env python

import urllib2
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyvirtualdisplay import Display
import time

display = Display(visible=0, size=(1366, 768))
display.start()

#Email config
smtpServer = 'smtp.gmail.com:587'
server = smtplib.SMTP(smtpServer)
fromAddr = 'amino.monitoring@gmail.com'
toAddr = 'monitor1@aminocom.com'
username = 'amino.monitoring@gmail.com'
password = 'C0meGe750me!'
target = "http://stgbetaamino.intamac.com"
#target = "https://homereach.aminocom.co.uk"

delay1 = 5
delay2 = 15
delay3 = 30
delay4 = 35

driver = webdriver.Firefox()
driver.implicitly_wait(delay2)

def dashNav():
    try:
        startTimer = time.time()
        driver.get(target)
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rayres-prodlive1")
        driver.find_element_by_id("username").send_keys(u'\ue004')
        driver.find_element_by_id("userpassword").clear()
        driver.find_element_by_id("userpassword").send_keys("planet07")
        driver.find_element_by_id("cmdLogin").click()
        #element = WebDriverWait(driver, delay3).until(EC.invisibility_of_element_located((By.ID, "divFlashVersion")))
        element = WebDriverWait(driver, 0).until(EC.presence_of_element_located((By.ID, "flashImg1")))
        driver.find_element_by_link_text("Logout").click()
        endTimer = time.time()
        timer = round(endTimer - startTimer, 2)
        print timer

        if timer >= 10 and timer < 20:
            msg = MIMEMultipart()
            msg['From'] = fromAddr
            msg['To'] = toAddr
            msg['Subject'] = "Alert: prod-live login @ %s" % timer + "s"
            #send email with result
            mailBody = ""
            #Message body will be sent as plain text
            msg.attach(MIMEText(mailBody, 'plain'))
            #Identifying call to server
            server.ehlo()
            #Enter TLS encryption mode
            server.starttls()
            #Repeat ehlo as good practice
            server.ehlo()
            server.login(username, password)
            mailContent = msg.as_string()
            server.sendmail(fromAddr, toAddr, mailContent)
            server.quit()

        elif timer >= 20:
            msg = MIMEMultipart()
            msg['From'] = fromAddr
            msg['To'] = toAddr
            msg['Subject'] = "Warning: prod-live login @ %s" % timer + "s"
            #send email with result
            mailBody = ""
            #Message body will be sent as plain text
            msg.attach(MIMEText(mailBody, 'plain'))
            #Identifying call to server
            server.ehlo()
            #Enter TLS encryption mode
            server.starttls()
            #Repeat ehlo as good practice
            server.ehlo()
            server.login(username, password)
            mailContent = msg.as_string()
            server.sendmail(fromAddr, toAddr, mailContent)
            server.quit()

    except urllib2.URLError as e:
        print e
        driver.quit()
        display.stop()

    except urllib2.HTTPError as e:
        print e
        driver.quit()
        display.stop()

    except Exception as e:
        print e
        driver.quit()
        display.stop()

    finally:
        driver.quit()
        display.stop()
            
if __name__ == '__main__':
    dashNav()
