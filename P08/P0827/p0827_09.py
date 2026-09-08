# 퀴즈 
# 1~100 랜던숫자 3개를 받아서 
# 입력한 숫자 1개가 있는지를 확인
# 있으면 당첨 없으면 꽝
# 랜덤숫자 리스트 출력, 입력숫자 출력


import random
r_num1 = random.randint(1,100)
r_num2 = random.randint(1,100)
r_num3 = random.randint(1,100)

list_a = [r_num1, r_num2, r_num3]
list_a.sort()

no = int(input("1~100 중 숫자 한 개 입력 :  "))

if no in list_a :
    print ("당첨")
else :
    print ("꽝")
print("랜덤숫자 : {}, 입력숫자: {}".format(list_a, no))





# random.sample(range(1,101),3)