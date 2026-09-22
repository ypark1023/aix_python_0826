# # import random : 랜덤하게 불러오기

# # import datetime : 현재 시각을 불러오기 / from datetime import datetime 이렇게도 표현할 수 있음

# import datetime
# now = datetime.datetime.now()
# print(now)

# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)


print("연도: ", now.year)
print("월: ", now.month)
print("일: ", now.day)
print("시간: ", now.hour)
print("분: ", now.minute)
print("초: ", now.second)

# # 예제: 2026년 8월 27일 11시 12분
# print("{}년 {}월 {}일 {}시 {}분".format(now.year, now.month, now.day, now.hour, now.minute))
# print(f"{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분")



# 예제 : 1~6월 상반기, 7~12월 하반기

import datetime
now = datetime.datetime.now()
month1 = now.month

if month1 <= 6 :
    print("{}월 : 상반기입니다".format(month1))
else :
    print("{}월 : 하반기입니다".format(month1))
