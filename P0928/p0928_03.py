from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup
import time
import os
from dotenv import load_dotenv


# for i in range(1,6):
#     page = i
#     url = f"https://search.danawa.com/dsearch.php?query=%EB%85%B8%ED%8A%B8%EB%B6%81&originalQuery=%EB%85%B8%ED%8A%B8%EB%B6%81&checkedInfo=N&volumeType=allvs&page={page}&limit=40&sort=saveDESC&list=list&boost=true&tab=goods&addDelivery=N&simpleDescOpen=Y&mode=simple&isInitTireSmartFinder=N&recommendedSort=N&defaultUICategoryCode=112758&defaultPhysicsCategoryCode=860%7C869%7C10580%7C0&defaultVmTab=104290&defaultVaTab=8809942&isZeroPrice=Y&quickProductYN=N&priceUnitSort=N&priceUnitSortOrder=A"
#     headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36'}
#     res = requests.get(url,headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text,'lxml')
#     ul = soup.find('ul',{'class':'product_list'})
#     lis = ul.find_all('li',{'class':'prod_item'})
#     with open(f'p0928/file2/coms_{i}.html','w',encoding='utf-8') as f:
#         f.write(soup.prettify())
#         time.sleep(2)
#     print("-"*50)
#     print(i,":",len(lis))



for i in range(1,6):
    page = i
    print(f"page {i}")
    with open (f'p0928/file2/coms_{i}.html', "r", encoding="utf8") as f:
        soup = BeautifulSoup(f, "lxml")
    ul = soup.find('ul',{'class':'product_list'})
    lis = ul.find_all('li',{'class':'prod_item'})

    for idx in range(len(lis)):
        try :
            p_names = lis[idx].find("p", {"class":"prod_name"}).get_text(strip=True)
            p_prcs = lis[idx].find("p", {"class":"price_sect"})
            p_prcs0 = p_prcs.find("a").get_text(strip=True).replace(",", "")
            p_prcs1 = int(p_prcs0[:-1])
            p_strs = lis[idx].find("span", {"class":"text__score"}).get_text(strip=True)
            p_rinks = lis[idx].find("p", {"class":"prod_name"})
            p_rinks1 = p_rinks.find("a")["href"]
            if p_prcs1 <= 1500000: 
                print(f"상품명: {p_names} / 가격: {p_prcs1} / 별점: {p_strs}")
                print(f"링크: {p_rinks1}")
            else :
                print("150만 원 이상 제외")
        except:
            print('값 없음')
        print("-"*10)
    print(i,":",len(lis))