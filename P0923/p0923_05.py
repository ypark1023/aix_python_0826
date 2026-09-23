from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window() # 화면 최대창 확대
url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B2%BD%EC%A3%BC&checkIn=2026-09-23&checkOut=2026-09-24&personal=2"
browser.get(url)

# time.sleep(1)
# pre_h = browser.execute_script("return document.body.scrollHeight")
# print("최초 높이: ", pre_h)
# while True:
#     browser.execute_script("window.scroll(0, document.body.scrollHeight)")
#     time.sleep(2)

#     next_h = browser.execute_script("return document.body.scrollHeight")
#     print("변경된 높이: ", next_h)

#     if pre_h == next_h:  break
#     else : pre_h = next_h

# print("더 스크롤할 내용 없음")
# time.sleep(2)

soup = BeautifulSoup(browser.page_source, "lxml")
# with open ("GJ01.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# input()

with open ("GJ01.html", "r", encoding="utf8") as f:
    soup = BeautifulSoup(f, "lxml")

print("완료")

acc = soup.find("ul", {"class":"css-y5z6rw"})
lis = acc.find_all("li")

print(f"총 숙소 개수: {len(lis)}개")

i = 0
for i, li in enumerate(lis):
    print(f"{i+1}.")
    try :
        titles = li.find("h3", {"class": "gc-thumbnail-type-seller-card-title css-1gsfgy5"})
        titles1 = titles.get_text(strip=True)
        stars = li.find("span", {"class": "css-ry30z7"}).get_text(strip=True)
        stars1 = float(stars)
        reviews = li.find("span", {"class": "css-144z61f"}).get_text(strip=True)[:-4].replace(",","")
        reviews1 = float(reviews)
        prcs = li.find("span", {"class": "css-1llao6q"}).get_text(strip=True).replace(",","")
        prcs1 = int(prcs) 
        imgs = li.find("img")["src"]
        print(f"숙소명: {titles1} / 별점: {stars1} / 리뷰수: {reviews1} / 금액: {prcs1} / 이미지: {imgs}")
    except Exception as e:
        pass

input()

