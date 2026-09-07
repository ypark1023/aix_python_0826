# 함수 이해하기 반복

# # 형태1
# def hap():
#     num1 = int(input("숫자 입력1: "))
#     num2 = int(input("숫자 입력2: "))
#     sum = num1+num2
#     print(sum)

# hap()


# # 형태2
# def hap():
#     num1 = int(input("숫자 입력1: "))
#     num2 = int(input("숫자 입력2: "))
#     sum = num1+num2
#     return sum

# sum = hap()
# print(sum)
# print("프로그램 종료")



# # 형태3
# def hap(num1, num2):
#     sum = num1+num2
#     return sum

# num1 = int(input("숫자 입력1: "))
# num2 = int(input("숫자 입력2: "))
# sum = hap(num1, num2)
# print(sum)
# print("프로그램 종료")



#######################################
# # 반복 연습

import p0907_func

# # 형태1
# p0907_func.hap1()
# print("합1 완료")


# # 형태2
# sum = p0907_func.hap2()
# print(sum)
# print("합2 완료")


# # 형태3
# num1 = int(input("숫자 입력1: "))
# num2 = int(input("숫자 입력2: "))
# p0907_func.hap3(num1, num2)
# print("합3 완료")

# # 형태4
# num1 = int(input("숫자 입력1: "))
# num2 = int(input("숫자 입력2: "))
# sum = p0907_func.hap4(num1, num2)
# print(sum)
# print("합4 완료")

# #######################################
# # 함수 호출 시 별칭 쓰기
import p0907_func as fn

# 형태1
fn.hap1()
print("합1 완료")


#######################################
# from 써서 함수 호출하기
from p0907_func import hap4

# 형태4
num1 = int(input("숫자 입력1: "))
num2 = int(input("숫자 입력2: "))
sum = hap4(num1, num2)
print(sum)
print("합4 완료")