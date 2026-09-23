from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)

# m_year = "https://search.daum.net/search?w=tot&q=2026%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"

# for i in range(2016, 2027):
#     m_url = (f"https://search.daum.net/search?w=tot&q={i}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
#     print(m_url)

#     options = Options()
#     options.add_experimental_option("excludeSwitches", ["enable-automation"])
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("--disable-blink-features=AutomationControlled")
#     browser = webdriver.Chrome(options=options)
#     browser.maximize_window()
#     url = m_url
#     browser.get(url)
#     time.sleep(3)

#     soup = BeautifulSoup(browser.page_source,'lxml')
#     with open(f'file1/movie_{i}.html','w',encoding='utf-8') as f:
#             f.write(soup.prettify())
#             time.sleep(2)


options = Options()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
options.add_argument("--disable-blink-features=AutomationControlled")
browser = webdriver.Chrome(options=options)
browser.maximize_window()
# url = m_url
# browser.get(url)
# time.sleep(3)

soup = BeautifulSoup(browser.page_source,'lxml')
with open ("p0923/file1/movie_2022.html", "r", encoding="utf8") as f:
    soup = BeautifulSoup(f, "lxml")

mlist = soup.find("ul", {"class":"c-list-basic ty_flow35"})
lis = mlist.find_all("li")
print(len(lis))


for i in range(2016,2027) :
    print(f"p0923/file1/movie_{i}.html")
    mlist = soup.find("ul", {"class":"c-list-basic ty_flow35"})
    lis = mlist.find_all("li")
    with open (f"p0923/file1/movie_{i}.html", "r", encoding="utf8") as f:
        soup = BeautifulSoup(f, "lxml")

        for idx in range(5):
            titles = lis[idx].find('strong',{'class':'tit-g clamp-g'}).get_text(strip=True)
            audis = lis[idx].find("p", {"class":"conts-desc clamp-g"}).get_text(strip=True)
            audis1 = int(audis[3:-2].replace(",", ""))
            dates = lis[idx].find("span", {"class":"conts-subdesc clamp-g"}).get_text(strip=True)
            posters = lis[idx].find("img")["src"]
            print(f"제목: {titles} / 누적관객수: {audis1} / 개봉일: {dates} / 포스터: {posters}")

            # 이미지 저장하기
            img_res = requests.get(posters, headers=headers)
            img_res.raise_for_status()
            os.makedirs("./movies_img", exist_ok=True)
            # count = 1
            with open (f"movies_img/mov_{i}_{idx+1}.jpg", "wb") as ff:
                ff.write(img_res.content)
            print("이미지 저장 완료")
