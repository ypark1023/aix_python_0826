from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time
import os

# 브라우저 열기
browser = webdriver.Chrome()

# 네이버 페이지 열기
url = "http://www.naver.com"
browser.get(url)

# 브라우저 위치값 찾아서 클릭
elem = browser.find_element(By.ID,'query')
elem.click()
elem.send_keys("뉴스")
elem.send_keys(Keys.ENTER)
time.sleep(3)
elem2 = browser.find_element(By.CLASS_NAME,'sds-comps-text')
elem2.click()
input()

