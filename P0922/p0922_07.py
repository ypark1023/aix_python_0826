import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()


# with open ("melon_chart.html", "w", encoding="utf8") as f:
#     f.write(res.text)
# print("저장 완료")

soup = BeautifulSoup(res.text,'lxml')
print("-"*50)

# print(soup.tbody)
# s_tbody = soup.tbody
# print(s_tbody.find_all("tr",{"class":"lst50"}))
# trs = s_tbody.find_all("tr",{"class":"lst50"})
# trs = s_tbody.find("tr",{"class":"lst50"})
# tds = trs.find("td")
# inp = tds.find("input")['title']
# print(inp)


s_tbody = soup.tbody
trs = s_tbody.find_all("tr",{"class":"lst50"})

for i in range(50):
    tds = trs[i].find_all("td")
    # inps = tds[0].find("input")['title']
    inps = tds[5].find("a").get_text()
    # albs = tds[6].find("a")['title']
    albs = tds[6].find("a").get_text()
    nos = tds[1].find("span", {"class":"rank"}).get_text()
    # imgs = tds[3].find("img")["src"]
    sigs = tds[5].find("span", {"class":"checkEllipsis"}).get_text()
    print(f"{nos}: {inps} / {albs} / {sigs}")

