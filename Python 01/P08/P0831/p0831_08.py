# # 업다운 만들기
# import random

# # no1 = int(input("숫자 입력: "))
# mynums = []
# ran_num = random.randint(1,100)
# count = 0

# print("1~100 사이")
# while True :
#     no1 = int(input("숫자 1개 입력: "))
#     mynums.append(no1)
#     if no1 == ran_num :
#         print("당첨, 당첨숫자: {}".format(no1))
#         break
#     elif no1 > ran_num :
#         print("낮은 숫자 입력")
#     elif no1 < ran_num :
#         print("높은 숫자 입력")
#     count = count+1

# print("입력숫자: {}".format(mynums))
# print("숫자입력횟수: {}".format(count))




# # 로또 만들기
# import random
# lotto = random.sample(range(1,46), 6)

# i = 0
# mynums2 = []

# print("1~45 사이 6개 숫자 입력")
# while i < 6 :
#     no2 = int(input("번호 입력: "))
#     if no2 not in mynums2 :
#         mynums2.append(no2)
#         i = i+1
#     else :
#         print("번호 있음")

# answer = []
# count = 0

# for i in mynums2 :
#     if i in lotto :
#         count = count +1
#         answer.append(i)

# print ("당첨 번호: {}".format(lotto))
# print ("입력 번호: {}".format(mynums2))
# print ("맞춘 번호: {}".format(answer))
# print ("맞춘 개수: {}".format(count))
