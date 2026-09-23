from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time
import os


# # 브라우저 열기
# browser = webdriver.Chrome()

# # 주식 페이지 열기
# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open("n_st_c01.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")


with open("n_st_c01.html","r",encoding="utf8") as f :
    soup = BeautifulSoup(f, 'lxml')

s_tbody = soup.tbody
trs = s_tbody.find_all("tr")

for idx, tr in enumerate(trs) :
    tds = trs[idx].find_all("td")
    rnks = tds[0].find("span", {"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
    prcs = tds[1].find("span", {"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
    print(f"종목: {rnks} / 현재가: {prcs}")


# rnks_list = []  # 순위들을 담을 빈 리스트 생성

# for tr in trs:
#     tds = tr.find_all("td")
#     if tds:
#         span = tds[0].find("span", {"class": "SingleLineText_text__HI_cb"})
#         if span:
#             rnks_list.append(span.get_text())  # 리스트에 추가

# print(rnks_list)