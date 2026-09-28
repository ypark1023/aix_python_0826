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
# id = os.getenv("id") # 데이터를 안전하게 활용 가능

# REQUEST로 열기
url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,'lxml')
print("저장 완료")

# SELENIUM으로 열기
url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대

# SELENIUM으로 열기2
browser.get(url)
time.sleep(3)
soup = BeautifulSoup(browser.page_source,'lxml')
with open('p0928/file1/ya1.html','w',encoding='utf-8') as f:
    f.write(soup.prettify())


# # 파일 BeautifulSoup변환
# with open('p0928/file1/ya1.html','r',encoding='utf-8') as f:
#     soup = BeautifulSoup(f,'lxml')
# # print(soup)

# a_list = soup.find("div", {"data-testid":"virtuoso-item-list"})
# # print(a_list)

# yadb = a_list.find_all("div", {"data-known-size":"228"})
# # print(yadb)
# # print(len(yadb))
