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
# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text,'lxml')
# print("저장 완료")

# with open('p0928/file1/flgith1.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


# SELENIUM으로 열기
# url = "https://flight.naver.com/flights/domestic/SEL:city-CJU:airport-20261006/CJU:airport-SEL:city-20261008?adult=1&fareType=YC"
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
# with open('p0928/file1/flight2.html','w',encoding='utf-8') as f:
#     f.write(soup.prettify())


with open('p0928/file1/flight2.html','r',encoding='utf-8') as f:
    soup = BeautifulSoup(f,'lxml')
# print(soup)

flights = soup.find_all("div", {"class":"domestic_Flight__8bR_b"})
print(len(flights))


# names = flights[0].find("span", {"class":"airline_text__WWkbY"})
# names1 = names.get_text(strip=True)
# times = flights[0].find_all("b", {"class":"route_time__xWu7a"})
# times1 = times[0].get_text(strip=True)
# times2 = times[1].get_text(strip=True)
# prices = flights[0].find("i", {"class":"domestic_num__ShOub"})
# prices1 = int(prices.get_text(strip=True).replace(",", ""))
# print(f"항공사: {names1} / 출발시간: {times1} / 도착시간: {times2} / 가격: {prices1}")

i = 0
for i in range(len(flights)):
    try:
        names = flights[i].find("span", {"class":"airline_text__WWkbY"})
        names1 = names.get_text(strip=True)
        times = flights[i].find_all("b", {"class":"route_time__xWu7a"})
        times1 = times[0].get_text(strip=True)
        times2 = times[1].get_text(strip=True)
        prices = flights[i].find("i", {"class":"domestic_num__ShOub"})
        prices1 = int(prices.get_text(strip=True).replace(",", ""))

        if prices1 <= 70000:
            # print(f"항공사: {names1} / 출발시간: {times1} / 도착시간: {times2} / 가격: {prices1}")
            print(f"{names1}/{times1}/{times2}/{prices1}")
        else : pass
    except Exception as e:
        pass