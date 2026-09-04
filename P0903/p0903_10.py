import os
# print("운영 체제: ", os.name)
# print("현재 폴더: ", os.getcwd())
# print("폴더 속 파일: ", os.listdir())

# os.mkdir("abc")   # 폴더 생성


# 텍스트 파일 불러오기
# news = open("new.txt", "r")
# while True :
#     str = news.readline()   #한줄씩 읽어오겠음
#     if str == "" : break
#     print(str, end=" ")
# news.close


news = open("stu.txt", "r", encoding="utf-8")
while True :
    str = news.readline()   #한줄씩 읽어오겠음
    if str == "" : break
    print(str, end=" ")
news.close



import time
print(1)
print(2)
print(3)
print(4)
time.sleep(3)       # 출력 시 3초간 대기
print(5)
print(6)

