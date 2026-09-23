from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup
import time
import os

# # 브라우저 열기
# browser = webdriver.Chrome()

# # 페이지 열기
url = "https://comic.naver.com/bestChallenge?sortType=starscore"
# browser.get(url)
# time.sleep(3)
# soup = BeautifulSoup(browser.page_source, 'lxml')
# with open("webtoon01.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
# print("완료")

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)

with open("webtoon01.html","r",encoding="utf8") as f :
    soup = BeautifulSoup(f, 'lxml')

toon = soup.find("ul", {"class":"BestChallengeView__challenge_list--sUqhh"})

lis = toon.find_all("li")
# print(len(lis))
v_total = 0
v_avg = 0

for i in range(30):
    imgs = toon.find("img")["src"]
    titles = lis[i].find("span", {"class":"ContentTitle__title--e3qXt"})
    titles1 = titles.find("span", {"class":"text"}).get_text(strip=True)
    authrs = lis[i].find("a", {"class":"ContentAuthor__author--CTAAP"}).get_text(strip=True)
    stars = lis[i].find("span", {"class":"Rating__star_area--dFzsb"})
    stars1 = float(stars.find("span", {"class":"text"}).get_text(strip=True))
    counts = lis[i].find("span", {"class":"Rating__view_area--GQb_S"})
    # counts1 = int(counts.find("span", {"class":"text"}).get_text(strip=True)[:-1].replace(",",""))
    counts1 = float(counts.find("span", {"class":"text"}).get_text(strip=True)[:-1].replace(",",""))
    counts2 = counts1*10000
    v_total += counts2
    print(f"제목: {titles1} / 작가: {authrs} / 별점: {stars1} / 조회수: {counts2} / 이미지소스: {imgs}")


    # print(f"제목: {titles1}")
    # print(f"작가: {authrs}")
    # print(f"별점: {stars1} / 조회수: {counts1}")

v_avg = v_total/3
print(f"평균 조회수: {v_avg}")

# # 이미지 저장하기
# t_img = lis[0].find("img")["src"]
# # print(t_img)
# img_res = requests.get(t_img, headers=headers)
# img_res.raise_for_status()
# os.makedirs("./toons_img", exist_ok=True)
# count = 1
# with open (f"toons_img/webtoon01_{count}.jpg", "wb") as ff:
#     ff.write(img_res.content)
# print("이미지 저장 완료")