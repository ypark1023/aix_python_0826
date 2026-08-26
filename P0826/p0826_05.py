
# 서로 다른 타입끼리의 연산은 TypeError가 남

# 문자열끼리의 연산
print ("Hello"+" World.")   # 연결
print("Go "*5)              # 반복


str1, str2, str3 = "100", "1.123", "999"
print(int(str1)+float(str2)+int(str3))


# 예제: 번호, 이름, 국어, 영어, 수학, 합계, 평균을 출력하시오.

no = input("번호를 입력하시오 >>  ")
name = input("이름를 입력하시오 >>  ")
kor = int(input("국어 점수를 입력하시오 >>  "))
eng = int(input("영어 점수를 입력하시오 >>  "))
math = int(input("수학 점수를 입력하시오 >>  "))
total = kor+eng+math
avg = total/3
print("번호: {} / 이름: {} / 국어: {} / 영어: {} / 수학: {} / 합계: {} / 평균: {:.2f}"\
      .format(no, name, kor, eng, math, total, avg))


no2 = input("번호를 입력하시오 >>  ")
name2 = input("이름를 입력하시오 >>  ")
kor2 = int(input("국어 점수를 입력하시오 >>  "))
eng2 = int(input("영어 점수를 입력하시오 >>  "))
math2 = int(input("수학 점수를 입력하시오 >>  "))
total2 = kor2+eng2+math2
avg2 = total2/3

print("번호\t이름\t국어\t영어\t수학\t합계\t평균")
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no, name, kor, eng, math, total, avg))
print("-"*60)
print("{}\t{}\t{}\t{}\t{}\t{}\t{:.2f}".format(no2, name2, kor2, eng2, math2, total2, avg2))



a=10
a+=5
print(a)


# 예제 : 원의 반지름을 입력받아 원의 넓이를 출력하시오
pi = 3.14
r1 = int(input("반지름을 입력하시오"))
print("원의 넓이 = {}".format((r1**2)*pi) + "cm2")
print("원의 둘레 = {}".format(2*r1*pi) + "cm")


pi = 3.14
r1 = int(input("반지름을 입력하시오"))
result1 = pi*(r1**2)
result2 = 2*r1*pi
print("원의 넓이 = {}".format(result1))
print("원의 둘레 = {}".format(result2))