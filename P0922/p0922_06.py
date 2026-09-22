import requests
from bs4 import BeautifulSoup

# url = "https://www.google.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*50)

# print(soup.title.get_text())                        # 결과값은 Google
# print(soup.find("a", {"class":"gb_6"}).get_text())  # 결과값은 Gmail


#########################
# url = "https://www.naver.com"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text,'lxml')
# print("-"*50)

# print(soup.title.get_text())


#########################
url = "https://www.daum.net/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,'lxml')
print("-"*50)

print(soup.find("h2", {"id":"mainServiceTitle"}))


