# 예제: 구구단을 출력하시오

# for i in range(2,10) :
#     for j in range(1,10) :
#         print("{}x{}={}".format(i,j,i*j), end=" ")
#     print()



# # 예제: 구구단을 출력하시오2

# for i in range(2,10) :
#     print("[{}단]".format(i), end=" ")
# print()
# for i in range(1,10) :
#     for j in range(2,10) :
#         print("{}x{}={}".format(j,i,i*j), end=" ")
#     print()


# # 결과값은 아래와 같다
# [2단] [3단] [4단] [5단] [6단] [7단] [8단] [9단] 
# 2x1=2 3x1=3 4x1=4 5x1=5 6x1=6 7x1=7 8x1=8 9x1=9 
# 2x2=4 3x2=6 4x2=8 5x2=10 6x2=12 7x2=14 8x2=16 9x2=18 
# 2x3=6 3x3=9 4x3=12 5x3=15 6x3=18 7x3=21 8x3=24 9x3=27 
# 2x4=8 3x4=12 4x4=16 5x4=20 6x4=24 7x4=28 8x4=32 9x4=36 
# 2x5=10 3x5=15 4x5=20 5x5=25 6x5=30 7x5=35 8x5=40 9x5=45 
# 2x6=12 3x6=18 4x6=24 5x6=30 6x6=36 7x6=42 8x6=48 9x6=54 
# 2x7=14 3x7=21 4x7=28 5x7=35 6x7=42 7x7=49 8x7=56 9x7=63 
# 2x8=16 3x8=24 4x8=32 5x8=40 6x8=48 7x8=56 8x8=64 9x8=72 
# 2x9=18 3x9=27 4x9=36 5x9=45 6x9=54 7x9=63 8x9=72 9x9=81 



# # 예제 : 합계 출력하기
# sum = 0
# for i in range(1,11):
#     sum = sum + i
# print("합계: {}".format(sum))
# # 결과값은 합계 : 55


# result = 1
# for i in range(1,11):
#     result = result * i
# print("곱하기: {:,}".format(result))
# # 결과값은 곱하기 : 3,628,800


# # 예제 : 합계 20 넘을 때
# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     if sum > 20 :
#         break    
#     else :
#         pass
# print("합계: {}, 몇번째 : {}".format(sum,i))

# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     if sum > 100 :
#         break    
#     else :
#         pass
# print("합계: {}, 몇번째 : {}".format(sum,i))

# # 결과값
# # 합계: 21, 몇번째 : 6
# # 합계: 105, 몇번째 : 14



# sum = 0
# for i in range(1,11):
#     sum = sum + i
#     if sum > 20 :
#         break    
# print("합계: {}, 몇번째 : {}".format(sum,i))

# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     if sum > 100 :
#         break    
# print("합계: {}, 몇번째 : {}".format(sum,i))



# sum = 0
# for i in range(1,101):
#     sum = sum + i
#     if sum > 100 :
#         break    
# print("합계: {}, 몇번째 : {}".format(sum,i))
# print("100 미만 합계: {}, 몇번째 : {}".format(sum-i,i-1))

# # 결과값은
# # 합계: 105, 몇번째 : 14
# # 100 미만 합계: 91, 몇번째 : 13






# 예제 : 1~100까지 합계

# sum = 0
# for i in range(1,101):
#     sum = sum + i
# print("합계: {}".format(sum))


# # 예제 : 홀수 합 구하기
# sum = 0
# for i in range(1,101,2) :
#         sum = sum + i
# print("홀수합: {}".format(sum)) 
# # 결과값 홀수합: 2500


# sum = 0
# for i in range(1,101):
#     if i%7 == 0 :
#         print(i, end=" ")
#         sum = sum + i
# print("7의배수 합계: {}".format(sum))
# # 결과값 7 14 21 28 35 42 49 56 63 70 77 84 91 98 7의배수 합계: 735



# # 예제: 입력받은 세 숫자의 합을 구하시오

# sum = 0
# list_a = []
# for no1 in range(3):
#     no1 = int(input("숫자 입력: "))
#     list_a.append(no1)
#     sum = sum + no1
# print ("입력숫자: {} / 합계 : {}".format(list_a, sum))



# # 예제 : 입력한 두 개 숫자 합을 구하시오

# a1 = int(input("숫자입력1: "))
# b1 = int(input("숫자입력2: "))
# # print("합계: {}".format(a1+b1))

# sum = 0
# for i in range(a1, b1+1):     # 뒤에 +1을 넣어줘야 함
#     sum = sum+i
# print("합계: {}".format(sum))



# # 변수 선언해주기
# a1 = int(input("숫자입력1: "))
# b1 = int(input("숫자입력2: "))
# c1 = 0
# if a1 > b1 :
#     c1 = a1
#     a1 = b1
#     b1 = c1


# sum = 0
# for i in range(a1, b1+1):     # 뒤에 +1을 넣어줘야 함
#     sum = sum+i
# print("합계: {}".format(sum))





# # 구구단 출력하기

# for i in range(2,10) :
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j), end=" ")
#     print()



# # 숫자를 입력받아 그 숫자부터 구구단

# no1 = int(input("숫자 입력: "))
# if no1 >= 11 :
#     print("1~10 사이 값을 입력하시오")

# for i in range(no1,10) :
#     for j in range(1,10):
#         print("{}x{}={}".format(i,j,i*j), end=" ")
#     print()



# fruits = ["바나나", "딸기", "사과"]

# for i in range(3) :
#     fruits.append(input("과일 입력: "))

# for i in fruits :
#     print(i, end = " ")

# 결과값 : 바나나 딸기 사과 수박 포도 복숭아 




# # 번호 달기
# fruits = ["바나나", "딸기", "사과"]
# j = 1
# for i in fruits:
#     print(j, ":", i)
#     j = j+1

# # 결과값은
# # 1 : 바나나
# # 2 : 딸기
# # 3 : 사과


# fruits = ["바나나", "딸기", "사과"]
# for i, value in enumerate(fruits):
#     print(i, ":", value)

# # 결과값은
# # 0 : 바나나
# # 1 : 딸기
# # 2 : 사과

# fruits = ["바나나", "딸기", "사과"]
# for i, value in enumerate(fruits):
#     print(i+1, ":", value)

# # 결과값은
# # 1 : 바나나
# # 2 : 딸기
# # 3 : 사과


# fruits = ["바나나", "딸기", "사과"]
# for i in range(3):
#     print(i+1, ":", fruits[i])

# # 결과값은
# # 1 : 바나나
# # 2 : 딸기
# # 3 : 사과


# fruits = ["바나나", "딸기", "사과", "복숭아"]
# for i in range(len(fruits)) :
#     print(i+1, ":", fruits[i])

# # 결과값은
# # 1 : 바나나
# # 2 : 딸기
# # 3 : 사과
# # 4 : 복숭아


# 예제 : 이름, 점수 세 개

name = []
kor = []
eng = []
math = []
total = []
avg = []

for i in range(3) :
    name.append(input("이름: "))
    kor1=int(input("국어: "))
    kor.append(kor1)
    eng1=int(input("영어: "))
    eng.append(eng1)
    math1=int(input("수학: "))
    math.append(math1)
    total.append(kor1+eng1+math1)
    avg.append(kor1+eng1+math1/3)

print("[학생 성적]")
print("이름 \t 국어 \t 영어 \t 수학 \t 합계 \t 평균")
for i in range(len(name)) :
    print("{} \t {} \t {} \t {} \t {} \t {:.2f}".format(name[i], kor[i], eng[i], math[i], total[i], avg[i]))

