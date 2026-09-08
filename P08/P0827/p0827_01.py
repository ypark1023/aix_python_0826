# 복습
# 학생 두 명의 성적을 입력받아 출력하시오.
# 번호, 이름, 국어, 영어 수학 점수를 입력받아 합계, 평균과 함께 출력하시오.

no = input("번호를 입력하시오")
name = input("이름을 입력하시오")
kor = int(input("국어 점수를 입력하시오"))
eng = int(input("영어 점수를 입력하시오"))
math = int(input("수학 점수를 입력하시오"))
total = kor+eng+math
avg = total/3

no2 = input("번호를 입력하시오")
name2 = input("이름을 입력하시오")
kor2 = int(input("국어 점수를 입력하시오"))
eng2 = int(input("영어 점수를 입력하시오"))
math2 = int(input("수학 점수를 입력하시오"))
total2 = kor2+eng2+math2
avg2 = total2/3

print("번호: {} \t 이름: {} \t 국어: {} \t 영어: {} \t 수학: {} \t 합계: {} \t 평균: {:.2f}".format(no, name, kor, eng, math, total, avg))
print("번호: {} \t 이름: {} \t 국어: {} \t 영어: {} \t 수학: {} \t 합계: {} \t 평균: {:.2f}".format(no2, name2, kor2, eng2, math2, total2, avg2))