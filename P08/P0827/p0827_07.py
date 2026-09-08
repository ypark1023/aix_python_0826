# # 리스트 (List) 타입
# # [ ] 대괄호로 묶음

# # a = 1
# # arr = [1,2,3,4,5]

# # print(a)
# # print(type(a)) #결과값은 int
# # print(arr)
# # print(type(arr)) #결과값은 list
# # print(arr[3]+1) #결과값은 5
# # print(len(arr)) #결과값은 5

# # 리스트는 0번부터 주소 시작
# # 리스트 안에는 모든 타입을 넣을 수 있음
# # 정수, 실수, 문자열, 불, 리스트, 튜플, 딕셔너리

# arr1 = [9, "안녕", 3.4, True, [1,2,3,4,5]]
# print(arr1[1], arr1[3], arr1[4])
# print(arr1[4][1]) #결과값은 2



# # 예제 : 리스트 만들기

# no1 = int(input("1과 10 사이 숫자 1: "))
# no2 = int(input("1과 10 사이 숫자 2: "))
# no3 = int(input("1과 10 사이 숫자 3: "))
# print("입력숫자: ", no1,no2,no3)

# arr = [0,0,0]
# arr[0] = int(input("1과 10 사이 숫자 1: "))
# arr[1] = int(input("1과 10 사이 숫자 2: "))
# arr[2] = int(input("1과 10 사이 숫자 3: "))
# print("입력숫자: ", arr)



# # 예제 : 리스트 안에 있다면 if 와 in

# a = "사과"
# b = "딸기"
# c = "수박"
# d = "참외"
# e = "복숭아"

# arr_f = [a,b,c,d,e]

# if "참외" in arr_f :
#     print("참외가 있습니다")
# else :
#     print("참외가 없습니다")



# # 예제 : 당첨 번호 맞추기
# import random
# r_num = random.randint(1,10)

# arr = []
# arr.append(int(input("1~10 중 숫자 입력 1: ")))
# arr.append(int(input("1~10 중 숫자 입력 2: ")))
# arr.append(int(input("1~10 중 숫자 입력 3: ")))
# print(arr)

# if r_num in arr :
#     print ("당첨")
# else :
#     print ("꽝")

# print("랜덤번호: ", r_num)


