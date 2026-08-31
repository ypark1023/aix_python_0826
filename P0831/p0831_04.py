# for 반복문은 횟수만큼
# while 반복문은 조건이 참일 때 계속 반복



# for i in range(1, 11) :
#     print(i, end = " ")
# # 결과값은 1 2 3 4 5 6 7 8 9 10

# i = 1
# while(i<11):
#     print(i, end = " ")
#     i += 1
# # 결과값은 1 2 3 4 5 6 7 8 9 10
# # 조건식이 참(True)일 때 작동



# for i in range(1,11,2):
#     print(i, end=" ")

# i = 1
# while(i<11):
#     i += 2
#     print(i, end=" ")


# 모든 for문은 while문으로 변경 가능
# for문은 구간 지정 가능
# while문은 조건식이 있을 때 주로 사용 *무한 반복 가능


# alist = list(range(10))
# print(alist)
# # 결과값 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# i = 0
# while(i<10):
#     print(i, end=" ")
#     i += 1
# # 결과값 0 1 2 3 4 5 6 7 8 9 


# blist = ["바나나", "딸기", "수박"]

# i = 0
# while(i<len(blist)):
#     print("{}:{}".format(i,blist[i]))
#     i += 1

# 결과값은
# 0:바나나
# 1:딸기
# 2:수박




# i = 0
# while True:
#     print(i)

# print("프로그램 종료")


# i = 0
# while i < 10:
#     print(i)
#     i += 1


# i=0
# while True:
#     print(i)
#     if i%10 == 0:
#         input1 = input("프로그램을 종료할까요?")
#         if input1 == "x" :
#             print("프로그램 종료")
#             break
#     i += 1




while True:
    no1 = int(input("숫자 입력1: "))
    no2 = int(input("숫자 입력2: "))
    if (no1 == 0) or (no2 == 0) :
        print("0이 입력되었음")
        break 
    print("{}+{} / 합: {}".format(no1, no2, no1+no2))



