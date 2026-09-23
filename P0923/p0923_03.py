from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time

# 브라우저 열기
browser = webdriver.Chrome()

# 페이지 열기
url = ""
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source, 'lxml')
with open("01.html", "w", encoding="utf8") as f:
    f.write(soup.prettify())
print("완료")