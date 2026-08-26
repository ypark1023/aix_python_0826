
# 산술연산자

# 500원 동전 몇 개가 필요할까요?
money = 12340
result = money//500
print("500원 동전 개수: {}".format(result))
result2 = money//100
print("100원 동전 개수: {}".format(result2))



# 500원 동전, 100원 동전, 10원 동전 몇 개가 필요할까요?
money = 12340
result1 = money//500
result2 = (money%500)//100
result3 = (money%100)//10
print("500원 동전 개수: {}, 100원 동전 개수: {}, 10원 동전 개수: {}".format(result1, result2, result3))



# 관계연산자
# 결과값은 True, False 값으로 나옴

a = 10
b = 5
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)



# 아이디와 패스워드를 입력받아 맞는지 확인하기

id = input("아이디를 입력하시오 >>  ")
pw = input("비밀번호를 입력하시오 >>  ")
if(id=="aaa") and (pw=="1111"): 
    print("로그인이 되었습니다 메인페이지로 이동합니다") 
else: 
    print("아이디 또는 패스워드가 일치하지 않습니다")


# 프로그램 종료 시 대문자 X 또는 소문자 x를 입력하면 종료

str1 = input("프로그램을 종료하려면 X 또는 x를 입력하시오")
if(str1=="X") or (str1=="x"):
    print("프로그램이 종료되었습니다")
else:
    print("프로그램을 계속 실행합니다")



