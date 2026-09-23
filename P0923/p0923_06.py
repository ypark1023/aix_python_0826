from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


m_year = "https://search.daum.net/search?w=tot&q=2026%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

for i in range(2022, 2027):
    m_url = (f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
    print(m_url)

    options = Options()
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument("--disable-blink-features=AutomationControlled")
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    url = m_url
    browser.get(url)
    time.sleep(3)

    soup = BeautifulSoup(browser.page_source,'lxml')
#     with open(f'file1/movie_{i}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#         time.sleep(2)


# with open ("file1/movie_2022.html", "r", encoding="utf8") as f:
#     soup = BeautifulSoup(f, "lxml")

# mlist = soup.find("ul", {"class":"c-list-basic ty_flow35"})
# lis = mlist.find_all("li")

# print(len(lis))
# titles = lis[0].find('strong',{'class':'tit-g clamp-g'}).get_text(strip=True)
# audis = lis[0].find("p", {"class":"conts-desc clamp-g"}).get_text(strip=True)
# audis1 = int(audis[3:-2].replace(",", ""))
# dates = lis[0].find("span", {"class":"conts-subdesc clamp-g"}).get_text(strip=True)
# posters = lis[0].find("img")["src"]
# print(titles)
# print(audis1)
# print(dates)
# print(posters)


for i in range(2022,2027) :
    print(f"file1/movie_{i}.html")
    mlist = soup.find("ul", {"class":"c-list-basic ty_flow35"})
    lis = mlist.find_all("li")
    with open (f"file1/movie_{i}.html", "r", encoding="utf8") as f:
        soup = BeautifulSoup(f, "lxml")

        for idx in range(5):
            titles = lis[idx].find('strong',{'class':'tit-g clamp-g'}).get_text(strip=True)
            audis = lis[idx].find("p", {"class":"conts-desc clamp-g"}).get_text(strip=True)
            audis1 = int(audis[3:-2].replace(",", ""))
            dates = lis[idx].find("span", {"class":"conts-subdesc clamp-g"}).get_text(strip=True)
            posters = lis[idx].find("img")["src"]
            print(f"제목: {titles} / 누적관객수: {audis1} / 개봉일: {dates} / 포스터: {posters}")