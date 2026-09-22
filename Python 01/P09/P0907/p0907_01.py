# 함수 복습하기

# def add():
#     sum = 0
#     for i in range(1,11) :
#         sum += i
#         print(sum, end = " ")      # print 위치가 어디냐에 따라 결과값 달라짐
# add()                              # 결과값은 1 3 6 10 15 21 28 36 45 5


# def add():
#     sum = 0
#     for i in range(1,11) :
#         sum += i
#     print(sum, end = " ")           # print 위치가 어디냐에 따라 결과값 달라짐
# add()                               # 결과값은 55 



# 입력한 숫자까지의 합 구하기

# # for 반복문으로 10번 반복하기
# for num in range(10) :        
#     num = int(input("숫자 입력: "))
#     sum = 0
#     for i in range(0,num+1) :
#         sum += i
#     print(sum)


# # 함수로 10번 반복하기 / for 반복문으로 반복해도 되지만, 함수가 코드를 재사용하기에 용이
# def add():
#     num = int(input("숫자 입력: "))
#     sum = 0
#     for i in range(0,num+1) :
#         sum += i
#     print(sum)

# for num in range(10) :  
#     add()


#######################################
# 매개변수 1개인 경우
def add2(num2):
    sum = 0
    for i in range(0,num2+1) :
        sum += i
    print(sum)
    # return sum        #이때는 의미없음


for i in range(10):
    num2 = int(input("숫자 입력: "))
    add2(num2)


#######################################
# 매개변수 2개인 경우
def add3(num3, num4):
    sum = 0
    for i in range(num3, num4+1) :
        sum += i
    print(sum)


for i in range(10):
    num3 = int(input("숫자 입력1: "))
    num4 = int(input("숫자 입력2: "))
    add3(num3,num4)


#######################################
def add4(num5, num6):
    sum = 0
    for i in range(num5, num6+1) :
        sum += i
    return sum


for i in range(10):
    num5 = int(input("숫자 입력1: "))
    num6 = int(input("숫자 입력2: "))
    sum = add4(num5,num6)
    print(sum)


