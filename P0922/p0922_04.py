import requests
from bs4 import BeautifulSoup #웹 소싱한 파일을 HTML로 파싱

# res = requests.get("https://www.whatismybrowser.com/detect/what-is-my-user-agent/")
# res.raise_for_status()

# # print("에러 코드: ", res.status_code) #200으로 정상 처리됨
# print(res.text)

# # f = open ("google.txt", "w", encoding="utf8")
# # f.close()

# with open ("agent1.html", "w", encoding="utf8") as f:
#     f.write(res.text)



# url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# # res.raise_for_status()
# # print(res.text)
# print("저장 완료")
# with open ("agent2.html", "w", encoding="utf8") as f:
#     f.write(res.text)


# url = "https://www.melon.com/chart/index.htm"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
# res = requests.get(url, headers=headers)
# # res.raise_for_status()
# # print(res.text)
# print("저장 완료")
# with open ("melon3.html", "w", encoding="utf8") as f:
#     f.write(res.text)


url = "https://www.naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/153.0.0.0 Safari/537.36"}
res = requests.get(url, headers=headers)
# res.raise_for_status()
# print(res.text)
print("저장 완료")
with open ("naver1.html", "w", encoding="utf8") as f:
    f.write(res.text)



