# # 함수 변수
# def func1():
#     a = 10             # 함수 내 변수 '지역변수'
#     print("func1 a : ", a)

# def func2():
#     print("func2 a : ", a)
# a = 20                  # 함수 밖 변수 '전역변수'

# # 비교
# func1()     # 결과값은 func1 a :  10
# func2()     # 결과값은 func2 a :  20

# # 지역변수를 먼저 찾아보고, 없으면 전역변수를 적용함



# # gobal - 전역변수에 선언돼있는 링크 가져옴
# def func1():
#     global a        # <전역변수 a>를 가져옴
#     a = 10             
#     print("func1 a : ", a)

# def func2():
#     print("func2 a : ", a)
# a = 20                  

# # 비교
# func1()     # 결과값은 func1 a :  10
# func2()     # 결과값은 func2 a :  10!!!!!!!!!



# # return / 매개변수

# def func1(a):
#     print(a)        
#     return a+10

# result = func1(10)
# print(result)          # 결과값은 10 20 




# def func0(*num):
#     sum = 0
#     for n in num:
#         sum += n
#     return sum


def func0(a, b, *num):
    sum = 0
    sum = a + b
    for n in num :
        sum =+ n
    return sum


print(func0(1,2,3))
print(func0(1,2))
print(func0(10,20,30,40,50))



