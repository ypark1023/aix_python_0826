import requests
from bs4 import BeautifulSoup

# url = "https://n.news.naver.com/article/094/0000013820?cds=news_media_pc&type=editn"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml') #html 소스 변경-css 문법 활용
# print("-"*50)
# # print("title: ", soup.title)        #태그로 정보를 찾을 수 있도록 해줌

# # print("a태그: ", soup.a)
# # print("a태그: ", soup.a["href"])
# # print("a태그: ", soup.a.attrs)

# # print("title: ", soup.title.get_text()) #태그에서 텍스만 들고옴

# # 파싱 후 저장하기
# print(soup.prettify())    #코드가 정렬돼서 저장됨
# # print(res.text)

######
url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml') #html 소스 변경-css 문법 활용
print("-"*50)
# print(soup.prettify())
# print(soup.title.get_text())
# print(soup.div.attrs)
# print(soup.tbody)
# print(soup.find("div",{"id":"header"}))
# print(soup.find("div",{"id":"util-menu"}))
# print(soup.find("tr",{"class":"lst50"}))
# print(soup.find("div",{"class":"wrap t_right"}))
# print(soup.find("input",{"class":"input_check d_checkall"})["title"])
print(soup.find("input",{"class":"input_check"})["title"])