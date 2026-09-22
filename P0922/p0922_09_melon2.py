import requests
from bs4 import BeautifulSoup
import os

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status

soup = BeautifulSoup(res.text, 'lxml')

# with open("melon_c3.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())

# print("저장")
print("-"*50)

s_tbody = soup.tbody
trs = s_tbody.find_all("tr")
# print(len(trs))

for idx, tr in enumerate(trs):
    tds = trs[idx].find_all("td")
    nos = tds[1].find("span", {"class":"rank"}).get_text()

    # try:
    #     nos = tds[1].find("span", {"class":"rank"}).get_text()
    # except:
    #     pass
    # except Exception as e:
    #     print(e)

    ttles = tds[5].find("a").get_text()
    albs = tds[6].find("a").get_text()
    sings =tds[5].find("span", {"class":"checkEllipsis"}).get_text()
    imgs = tds[3].find("img")["src"]
    imgs_res = requests.get(imgs, headers=headers)

    os.makedirs("./melon_img", exist_ok=True)

    with open (f"melon_img/melon_22_{idx+1}.jpg", "wb") as ff:
        ff.write(imgs_res.content)


    # s_as = tds[5].find_all("a")
    # ttles1 = s_as[0].get_text()     #곡명
    # sings1 = s_as[1].get_text()     #가수명

    # print(f"{nos}위 / {ttles} / {sings} / {albs} / {imgs}")
    # print("-"*50)

