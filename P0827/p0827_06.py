# 조건문
# if문 안에 if문

a = 75
if a > 50 :
    if a < 100 :
        print ("50보다 크고, 100보다 작은 수")
    else :
        print ("50보다 크고, 100보다 큰 수")
else : 
    print ("50보다 작은 수")



# 조건문 여러 개 만들기 elif

score1 = int(input("점수를 입력하시오 : "))

if score1 >= 90 :
    print ("A")
elif score1 >= 80 :
    print ("B")
elif score1 >= 70 :
    print ("C")
elif score1 >= 60 :
    print ("D")
else :
    print ("F")



# 예제 : 양수인지 음수인지 랜덤으로 뽑아서 양수인지 음수인지 출력하시오

import random
num = random.randint(-10, 10)
print("랜덤숫자: {}".format(num))


if num > 0 :
    print ("양수입니다")
elif num == 0 :
    print ("0입니다")
else :
    print ("음수입니다")



# 예제 : 0~100점 랜덤숫자 생성
import random
score2 = random.randint(0,100)

if score2 >= 60 :
    print ("{}점, 합격".format(score2))
elif 50 <= score2 < 60 :
    print ("{}점, 재시험".format(score2))
else :
    print ("{}점, 불합격".format(score2))



# 예제 : 랜덤점수 생성, 성적 90점 A, 80점 B, 70점 C, 60점 D, 그 이하 F

import random
score = random.randint(0,100)

if score >= 90 :
    if score >= 98 : 
        print ("{}점: A+".format(score))
    elif score < 93 :
        print ("{}점: A-".format(score))
elif score >= 80 :
    if score >= 88 : 
        print ("{}점: B+".format(score))
    elif score < 83 :
        print ("{}점: B-".format(score))
elif score >= 70 :
    if score >= 78 : 
        print ("{}점: C+".format(score))
    elif score < 73 :
        print ("{}점: C-".format(score))
elif score >= 60 :
    print("{}점 : D". format(score))
else :
    print("{}점 : F". format(score))    





# 출력할 것이 없을 시 pass
if 조건문 : (공백이면 에러남) pass


예제 : 월에 따라 봄 여름 가을 겨울 출력하시오

import datetime
now = datetime.datetime.now()
month = now.month

if (month == 12) or (month == 1) or (month == 2):
    print ("겨울")
elif (month == 3) or (month == 4) or (month == 6):
    print("봄")
elif (month == 7) or (month == 8) or (month == 9):
    print("여름")
else : 
    print("가을")
print (now.month)


if (month == 3) or (month == 4) or (month == 5):
    print("봄")
elif (month == 6) or (month == 7) or (month == 8):
    print("여름")
elif (month == 9) or (month == 10) or (month == 11):
    print("가을")
else : 
    print("겨을")
print ("{}월".format(now.month))


월을 입력하도록 하기
month = int(input("월을 입력하시오: "))

if (month == 3) or (month == 4) or (month == 5):
    print("봄")
elif (month == 6) or (month == 7) or (month == 8):
    print("여름")
elif (month == 9) or (month == 10) or (month == 11):
    print("가을")
else : 
    print("겨을")
print ("{}월".format(month))






# 예제 : 점수가 60점 이상이면 합격

score3 = int(input("점수: "))
if score3 >= 60 :
    print("합격")
else : 
    print("불합격")

# 위와 동일, print가 한 줄이기 때문
if score3 >= 60 : print("합격")
else : print("불합격")

score3 = 65
result = "합격" if score3 >= 60 else "불합격"