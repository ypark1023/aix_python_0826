from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# SELENIUM으로 열기
url = "https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
browser.get(url)
time.sleep(5)

# 아이디와 패스워드 입력하기 자동화
# //*[@id="id"] = 아이디 input XPath
# /html/body/div[1]/div[2]/main/div/div/form/ul/li[1]/div/div/input = 아이디 full XPath

# browser.find_element(By.XPATH, '//*[@id="id"]').click()
# browser.find_element(By.XPATH, '//*[@id="id"]').send_keys("aaa")
# browser.find_element(By.XPATH, '//*[@id="pw"]').click()
# browser.find_element(By.XPATH, '//*[@id="pw"]').send_keys("1234")

load_dotenv()
n_id = os.getenv("n_id")
n_pw = os.getenv("n_pw")

input_js = 'document.getElementById("id").value = "{id}";\
            document.getElementById("pw").value = "{pw}";\
            '.format(id=n_id,pw=n_pw)

browser.execute_script(input_js)
time.sleep(3)
browser.find_element(By.XPATH, '//*[@id="loginBtn_row"]').click()
input()