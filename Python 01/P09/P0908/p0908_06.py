# 클래스 불러오기

# 다른 폴더에 있을 경우 from으로 불러오기

from project import student1
from project import student2

stus = student2.StuLog()
print(len(stus.slist))          # 결과값은 아직은 0


s1 = student1.Student(1, "이순신", 80, 90, 95)
# print(s1)
# # 결과값은 - 번호: 1, 이름: 이순신, 국어: 80, 영어: 90, 수학: 95, 총합: 265, 평균: 88.33


stus.add(s1)
s2 = student1.Student(2, "유관순", 1000, 70, 85)
stus.add(s2)

stus.print()