# 웹 스크래핑


import requests

# # res.status_code 코드 확인
# # html 소스를 가져오기
# res = requests.get("http://www.melon.com")

# # print("html 소스: ", res.text) # 모든 데이터 읽어오기
# print("응답 에러 확인: ", res.raise_for_status) # 에러 나면 자동 종료
# print("응답 코드: ", res.status_code) # 에러 코드 확인
# print("프로그램 종료")


# if res.status_code != 200:
#     pass


res = requests.get("http://www.google.com")
res.raise_for_status()
print(res.text)
print(len(res.text))

with open ("google.html","w",encoding="utf8") as f:
    f.write(res.text)    

print("파일 저장 완료")