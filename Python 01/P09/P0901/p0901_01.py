# # 구구단 만들기

# for i in range(2, 10) :
#     for j in range(1, 10) :
#         print ("{}x{}={}".format(i, j, i*j), end=" ")


# # 1~100 사이 숫자 맞추기 업다운

# import random
# ranNo = random.randint(1,100)
# myNos = []
# count = 0

# print("1~100 사이 숫자 입력")
# while True :
#     myNo = int(input("숫자 입력: "))
#     myNos.append(myNo)
#     if ranNo == myNo :
#         print("입력 숫자: {}, 당첨!".format(myNo))
#         break
#     elif ranNo > myNo :
#         print("입력 숫자: {} 큰 수 입력".format(myNo))
#     elif ranNo < myNo :
#         print("입력 숫자: {} 작은 수 입력".format(myNo))
#     count = count+1
# print("입력 숫자: {}".format(myNos))
# print("입력 횟수 : {}".format(count))



# # 1~100 사이 숫자 맞추기 업다운 (반복연습)

# import random
# ran_num = random.randint(1,100)
# mynums = []
# count = 0

# print("1~100 사이 숫자 입력")
# while True :
#     my_num = int(input("숫자 입력: "))
#     mynums.append(my_num)
#     if my_num == ran_num :
#         print("입력 숫자: {}, 당첨!".format(my_num))
#         break
#     if my_num > ran_num :
#         print("입력 숫자: {}, 작은 수 입력하라".format(my_num))
#     if my_num < ran_num :
#         print("입력 숫자: {}, 큰 수 입력하라".format(my_num))
#     count = count+1
# print("입력 숫자 전체: {}".format(mynums))
# print("입력 횟수 : {}".format(count))






# 로또 맞추기

import random
lotto = random.sample(range(1,46),6)
# print(lotto)

i = 0
mylist = []
count = 0
answer = []

print("1~45 사이 숫자 입력")
while i < 6 : 
    mynum = int(input("숫자 입력: "))
    if mynum not in mylist :
        mylist.append(mynum)
        i = i+1
    else :
        print("번호 있음")

for i in mylist :
    if i in lotto :
        count = count+1
        answer.append(i)
    
print("당첨 번호: {}".format(lotto))
print("입력 번호: {}".format(mylist))
print("맞춘 개수: {}".format(count))
print("맞춘 번호: {}".format(answer))

