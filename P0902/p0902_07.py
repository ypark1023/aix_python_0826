# def print1():
#     print(1, end=" ")
#     print(2, end=" ")
#     print(3, end=" ")
#     print(4, end=" ")
#     print(5)

# # print1()        # 결과값은 1 2 3 4 5


# while True:
#     num1 = int(input("숫자 입력: "))
#     print1()




# def print2(num1) :
#     for i in range(num1) :
#         print("안녕")

# while True:
#     num1 = int(input("숫자 입력: "))
#     print2(num1)


# 매개변수, 웬만하면 동일하게 설정, 아래도 동일한 결과값이 나오긴 하지만...
# def print2(n) :
#     for i in range(n) :
#         print("안녕")

# while True:
#     num1 = int(input("숫자 입력: "))
#     print2(num1)




# def print2(num1,str1) :
#     for i in range(num1) :
#         print(i+1, str1)

# while True:
#     num1 = int(input("숫자 입력: "))
#     str1 = input("문구 입력: ")
#     print2(num1, str1)



# # 함수 리턴
# def add(num1, num2):
#     sum = num1+num2
#     return sum

# while True :
#     num1 = int(input("숫자 입력1: "))
#     num2 = int(input("숫자 입력2: "))
#     total = add(num1, num2)
#     print("결과값: ", total)



# 함수 리턴 연습
def cal(num1, num2, str1):
    result = 0
    if str1 == "+" :
        result = num1+num2
    elif str1 == "-" :
        result = num1-num2
    elif str1 == "*" :
        result = num1*num2
    elif str1 == "/" :
        result = num1/num2        
    return result


while True:
    num1 = int(input("숫자 입력1: "))
    num2 = int(input("숫자 입력2: "))
    str1 = input("+/-/*// 중 입력: ")
    result1 = cal(num1, num2, str1)
    print("값: ",result1)


