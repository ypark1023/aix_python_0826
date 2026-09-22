# 복습 : 번호 이름 국어 영어 수학 입력받아 합계 평균 구하기, 성적 출력하기

no1 = int(input("번호 입력 : "))
name1 = input("이름 입력 : ")
kor1 = int(input("국어 점수 입력 : "))
eng1 = int(input("영어 점수 입력 : "))
math1 = int(input("수학 점수 입력 : "))
total1 = kor1+eng1+math1
avg1 = total1/3

no2 = int(input("번호 입력 : "))
name2 = input("이름 입력 : ")
kor2 = int(input("국어 점수 입력 : "))
eng2 = int(input("영어 점수 입력 : "))
math2 = int(input("수학 점수 입력 : "))
total2 = kor2+eng2+math2
avg2 = total2/3


print("[학생 성적 프로그램]")
print("-"*60)
print("번호 \t 이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
print("-"*60)
print("{} \t {} \t {} \t {} \t {} \t {} \t {:.2f}".format(no1, name1, kor1, eng1, math1, total1, avg1))
print("{} \t {} \t {} \t {} \t {} \t {} \t {:.2f}".format(no2, name2, kor2, eng2, math2, total2, avg2))







