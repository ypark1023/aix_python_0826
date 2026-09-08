total1 = 1000

send1=int(input("송금액을 입력하시오"))
print("잔액: {}".format(total1))
print("송금액: {}".format(send1))
print("총금액: {}".format(int(total1)+int(send1)))


kor = int(input("국어 점수를 입력하시오"))
eng = int(input("영어 점수를 입력하시오"))
math = int(input("수학 점수를 입력하시오"))
print("합계: {} 평균: {}".format(kor+eng+math, (kor+eng+math)/3))



name = input("이름을 입력하시오")
kor = int(input("국어 점수를 입력하시오"))
eng = int(input("영어 점수를 입력하시오"))
math = int(input("수학 점수를 입력하시오"))

total = kor+eng+math
avg = (kor+eng+math)/3
print("이름: {}, 합계: {}, 평균: {:.2f}".format(name, total, avg))



# a,b = 1,2
# print(a,b) 이런 형식은 가능함

# 2진수로 변경하는 명령로 bin() : print(bin(5)) 결과값은 101
# 2진수를 10진수로 출력하고자 할 때 : print(int("101",2)) 결과값은 5

a = 9
b = 2
print(a/b)
print(a//b) # 나눗셈 후 몫만 출력
print(a%b) # 나눗셈 후 나머지값만 출력
print(a%2==1) #홀수면 True, 짝수면 False 짝홀수 구분
