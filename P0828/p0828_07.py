
# # 날짜 함수
# import datetime

# # 랜덤 함수
# import random


# now = datetime.datetime.now()

# print(now)
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)



# # 예제 : 3,4,5 봄 6,7,8 여름 9,10,11 가을 12,1,2 겨울
# import random
# r_num = random.randint(1,12)

# if 3 <= r_num <= 5 :
#     print ("봄")
# elif 6 <= r_num <= 8 :
#     print ("여름")
# elif 9 <= r_num <= 11 :
#     print ("가을")
# else :
#     print("겨울")
# print ("{}월".format(r_num))



# # 리스트 만들기
# alist1 = [0,0,0,0,0]
# print(alist1)
# alist2 = [0]*5
# print(alist2)
# alist3 = list(range(1,6))
# print(alist3)


# 예제 : 랜덤 숫자 뽑기
# import random
# a = random.randint(1,45)        #1~45까지 랜덤으로 1개 정수 뽑아옴

# arr1 = random.sample(range(1,46),5)  #1~45까지 중복 없이 랜덤으로 5개 정수 뽑아옴
# print(arr1)

# arr2 = random.sample([1,2,3,4,5], 2) #리스트에서 중복 없이 2개 정수 뽑아옴
# print(arr2)

# arr3 = [1,2,3,4,5]
# random.shuffle(arr3)       # 리스트에서 랜덤으로 섞어줌
# print(arr3)

# arr4 = [1,2,3,4,5,6]
# arr5 = random.choices(arr4, k=3)    #k값을 개수로 하여 가져옴, 중복으로 가져올 수 있음
# print(arr5)



# 예제 : 랜덤 5개 1~45 입력한 숫자 입력한 숫자 있으면 당첨, 없으면 꽝

# no1 = int(input("숫자 입력1: "))
# no2 = int(input("숫자 입력2: "))
# no3 = int(input("숫자 입력3: "))


# import random
# num1 = random.sample(range(1,46),5)

# if (no1 in num1) or (no2 in num1) or (no3 in num1) :
#     print ("당첨")
# else :
#     print ("꽝")
# print("입력 숫자: {},{},{}, 당첨 숫자: {}".format(no1,no2,no3, num1))



a = [1,2,3,4,5]
a[2] = 30
print(a)
# 결과값은 [1, 2, 30, 4, 5] / 해당 자리의 값이 변경됨

list11 = [10,20,30,40,50,60]
list11.pop(2)
list11.append(600)
print(list11)
# 결과값은 [10, 20, 40, 50, 60, 600] / pop으로 지우고, append로 추가 제일 뒤에