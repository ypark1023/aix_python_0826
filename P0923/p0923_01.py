from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time
import os

# browser = webdriver.Chrome()

# url = "https://stock.naver.com/market/stock/kr/stocklist/priceTop"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open ("n_st_c02.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")


with open ("n_st_c02.html", "r", encoding="utf8") as f:
    soup = BeautifulSoup(f, 'lxml')


s_tbody = soup.tbody
trs = s_tbody.find_all("tr")

for idx, tr in enumerate(trs):
    tds = trs[idx].find_all("td")
    rnks = tds[0].find("span", {"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
    prcs = tds[1].find("span", {"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
    amnts = tds[3].find("span", {"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
    prcs2 = tds[4].find("span", {"class":"SingleLinePrice_price__g_6VV"}).get_text(strip=True)
    total = tds[7].find("span", {"class":"SingleLineText_text__HI_cb"}).get_text(strip=True)
    print(f"종목 : {rnks} / 현재가: {prcs} / 거래량: {amnts} / 거래대비: {prcs} / 시가총액: {total}")


