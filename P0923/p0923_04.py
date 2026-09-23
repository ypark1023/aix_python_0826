from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

# 2. selenium : 자동화 구현
# 상단 제어창문구 삭제
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.yeogi.com/domestic-accommodations?sortType=RECOMMEND&keyword=%EA%B2%BD%EC%A3%BC&personal=2&checkIn=2026-09-23&checkOut=2026-09-24&category=2"
browser.get(url)
time.sleep(1)
# 자바스크립트를 통해 브라우저 높이 가져오기
pre_height = browser.execute_script('return document.body.scrollHeight')
print("처음 높이 : ",pre_height)
while True:
    # 스크롤 내리기
    browser.execute_script('window.scroll(0,document.body.scrollHeight)')
    time.sleep(2) # 내용 추가하는 데 시간대기

    # 다시 높이 가져오기
    next_height = browser.execute_script('return document.body.scrollHeight')
    print('변경된 높이 : ',next_height)

    if pre_height==next_height: break
    else : pre_height = next_height

print('더 이상 높이 변경이 없음')

soup = BeautifulSoup(browser.page_source, "lxml")
acc = soup.find("ul", {"class":"css-y5z6rw"})
lis = acc.find_all("li")

for i, li in enumerate(lis):
    print(f"{i+1}.")
    try :
        titles = lis[i].find("h3", {"class": "gc-thumbnail-type-seller-card-title css-1gsfgy5"})
        titles1 = titles.get_text(strip=True)
        stars = lis[i].find("span", {"class": "css-ry30z7"}).get_text(strip=True)
        stars1 = float(stars)
        reviews = lis[i].find("span", {"class": "css-144z61f"}).get_text(strip=True)[:-4].replace(",","")
        reviews1 = float(reviews)
        prcs = lis[i].find("span", {"class": "css-1llao6q"}).get_text(strip=True).replace(",","")
        prcs1 = int(prcs) 
        imgs = lis[i].find("img")["src"]
        print(f"숙소명: {titles1} / 별점: {stars1} / 리뷰수: {reviews1} / 금액: {prcs1} / 이미지: {imgs}")
    except Exception as e:
        pass

input()

