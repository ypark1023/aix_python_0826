# 예제 : 입력한 숫자가 양수인지 음수인지 출력하시오

a = int(input("숫자 입력: "))
if (a > 0) :
    print ("양수입니다")
else :
    print ("음수입니다")

print ("입력값은 {}".format(a))


# 예제 : 입력한 숫자가 2의 배수인지 확인하시오

b = int(input("숫자 입력: "))
if (b % 2 == 0) :
    print ("2의 배수다")
else :
    print ("2의 배수 아니다")
print("입력값은 {}".format(b))


# # 랜덤함수 import random / random.randint(1, 100) : 1에서 100 사이 정수 하나 랜덤으로 주겠다
# num = random.randint(1, 100)
# print(num)

import random           #명령을 먼저 내려야 한다
num = random.randint(1,10)
input1 = int(input("1~10 사이 정수 입력: "))
if (num == input1) :
    print ("당첨")
else :
    print ("꽝")
print("랜덤값: {}, 입력값: {}".format(num, input1))


import random
num = random.randint(1,10)
input1 = int(input("1~10 사이 정수 입력1: "))
input2 = int(input("1~10 사이 정수 입력2: "))
if (num == input1) or (num == input2) :
    print ("당첨")
else :
    print ("꽝")
print("랜덤값: {}, 입력값: {}, {}".format(num, input1, input2))