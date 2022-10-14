import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import easyocr
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import cv2
from matplotlib import pyplot as plt
import numpy as np

def easyocr_text():
    IMAGE_PATH = 'index.png'
    reader = easyocr.Reader(['en'])
    result = reader.readtext(IMAGE_PATH,paragraph="False")
    return(result)





options = Options()
ua = UserAgent()
userAgent = ua.random
options.add_argument(f'user-agent={userAgent}')
s = Service("./chromedriver")
url = "URL"
browser = webdriver.Chrome(service=s,chrome_options=options)
browser.get(url)
delay=5
try:
    time.sleep(5)
    # WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'uid')))
    time.sleep(10)
    captcha_image = browser.find_element(By.CLASS_NAME,"auth-form__captcha-image")
    print(captcha_image)
    captcha_image.screenshot("index.png")
    captcha_text = easyocr_text()
    captcha_text = captcha_text[0][-1]
    captcha_text = captcha_text.replace(" ","")
    captcha = browser.find_element(By.NAME,"captcha")
    captcha.clear()
    captcha.send_keys(captcha_text)
    verify_button = browser.find_element(By.CLASS_NAME,"button_btn__1dRFj")
    verify_button.click()
    soap = browser.page_source
    soup = BeautifulSoup(soap,features="lxml")
    print(soup)
    time.sleep(5)



except Exception as e:
    print(e)
    browser.close()
browser.close()
