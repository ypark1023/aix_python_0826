from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os

from dotenv import load_dotenv
# load_dotenv()
# print(os.getenv("naver_id"))


# 페이지 열기
browser = webdriver.Chrome()
url = "https://www.naver.com/"
browser.get(url)

# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# url = "https://www.naver.com/"


# # 자동화 구현1
# browser.find_element(By.CLASS_NAME, "MyView-module__link_login___VlF7z").click()
# time.sleep(3)
# elem = browser.find_element(By.ID, "id")
# elem.send_keys("aaa")
# elem2 = browser.find_element(By.ID, "pw")
# elem2.send_keys("1234")
# input()

# 자동화 구현2
elem = browser.find_element(By.ID, "query")
elem.send_keys("날씨")
elem.send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")
temp = soup.find('div',{'class':'temperature_text'}).get_text(strip=True)
print(temp)

# # CSS 셀렉터로 변경 (tag 제약 없이 클래스로만 탐색)
# # temperature_text 클래스를 가진 요소 안의 텍스트 추출
# deg_element = soup.select_one(".temperature_text")
# deg1 = deg_element.get_text(strip=True) if deg_element else "정보 없음"

# # 날씨 상태 클래스 탐색 (.weather 또는 .before_slash 등)
# stu_element = soup.select_one(".weather.before_slash")
# stu1 = stu_element.get_text(strip=True) if stu_element else "정보 없음"
# input()
