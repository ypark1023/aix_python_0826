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

# # REQUEST로 열기
url = "https://nol.yanolja.com/discovery/list/PRODUCT_CATEGORY_KOREA_ACCOMMODATION/HOTEL/900584"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
# soup = BeautifulSoup(res.text,'lxml')
# print("저장 완료")

# # SELENIUM으로 열기
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EC%A0%9C%EC%A3%BC&personal=2&checkIn=2026-09-28&checkOut=2026-09-29&typoCorrect=true&nonAffiliated=true&category=2&sortType=RECOMMEND"
# options = Options()
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--disable-blink-features=AutomationControlled")
# browser = webdriver.Chrome(options=options)
# browser.maximize_window() # 화면 최대창 확대
# browser.get(url)

# time.sleep(2)
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

# # SELENIUM으로 열기2
# soup = BeautifulSoup(browser.page_source,'lxml')
# with open('p0928/file1/yeo1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# 파일 BeautifulSoup변환
with open('p0928/file1/yeo1.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
# print(soup)

acc = soup.find("ul", {"class":"css-y5z6rw"})
lis = acc.find_all("li")

print(f"총 숙소 개수: {len(lis)}개")


i = 0
count01 = 0
for i, li in enumerate(lis):
    # print(f"{i+1}.")
    try :
        titles = li.find("h3", {"class": "gc-thumbnail-type-seller-card-title css-1gsfgy5"})
        titles1 = titles.get_text(strip=True)
        stars = li.find("span", {"class": "css-ry30z7"}).get_text(strip=True)
        stars1 = float(stars)
        reviews = li.find("span", {"class": "css-144z61f"}).get_text(strip=True)[:-4].replace(",","")
        reviews1 = float(reviews)
        prcs = li.find("span", {"class": "css-1llao6q"}).get_text(strip=True).replace(",","")
        prcs1 = int(prcs) 
        h_imgs = li.find("img")["src"]
        if prcs1 >= 200000:
            if stars1 > 9.0:
                count01 += 1
                print(f"숙소명: {titles1} / 별점: {stars1} / 리뷰수: {reviews1} / 금액: {prcs1} / 이미지 소스: {h_imgs}")
                img_res = requests.get(h_imgs, headers=headers)
                img_res.raise_for_status()
                os.makedirs("./p0928/hotels_img", exist_ok=True)
                with open (f"p0928/hotels_img/h_img_{i}.jpg", "wb") as ff:
                    ff.write(img_res.content)
        else : pass
    except Exception as e:
        pass
print(f"조건(금액 20만 원 이상, 별점 9.0 초과)에 해당하는 호텔 수: {count01}개")
input()

