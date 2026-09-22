# C 언어, 자바 : 컴파일러 언어 - 모든 소스를 기계어로 번역 후 프로그램 진행
# 웹 개발은 주로 자바 언어로 개발 (라이브러리가 파이썬에 비해 훨씬 많음)
# 반면 파이썬 : 스크립트 언어 - 한 줄 씩 기계어로 번역 후 프로그램 진행

# # 함수 복습
# def print_d():
#     for i in range(1,11):
#         print(i)

# print_d()


# def hello_print():
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")
#     print("안녕하세요")

# hello_print()


##################################
# # 함수 리턴 연습
# def cal(num1, num2, str1):
#     result = 0
#     if str1 == "+" :
#         result = num1+num2
#     elif str1 == "-" :
#         result = num1-num2
#     elif str1 == "*" :
#         result = num1*num2
#     elif str1 == "/" :
#         result = num1/num2        
#     return result


# while True:
#     num1 = int(input("숫자 입력1: "))
#     num2 = int(input("숫자 입력2: "))
#     str1 = input("+/-/*// 중 입력: ")
#     result1 = cal(num1, num2, str1)
#     print("값: ",result1)



##################################
def cal1():
    while True:
        no1 = int(input("숫자 입력1: "))
        no2 = int(input("숫자 입력2: "))
        str1 = input("+ / - / * / / 중 입력(0입력 시 종료 ): ")
        if str1 == "+" :
            result = no1 + no2
        elif str1 == "-" :
            result = no1 - no2
        elif str1 == "*" :
            result = no1 * no2
        elif str1 == "/" :
            result == no1 / no2
        elif str1 == "0" :
            print("프로그램 종료")
            break
        else :
            print("기호 입력 오류")
        print("값: ", result)


cal1()


