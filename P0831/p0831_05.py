# for i in range(50):
#     print(i, end = " ")
#     if i == 20 :
#         break
# # 결과값 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# for i in range(50):
#     print(i, end = " ")
#     if i == 20 :
#         continue


# i = 1
# no = []
# name = []
# while True:
#     n = input("{}. 이름 입력: ".format(i))
#     name.append(n)
#     no.append(i)
#     if n == "0":
#         break
#     i += 1

# print ("프로그램 종료")



import random
ran1 = random.randint(1, 10)
# print("랜덤숫자: {}".format(ran1))

no1 = 0
mylist = []
while True :
    no1 = int(input("숫자 입력: "))
    mylist.append(no1)

    if ran1 == no1 : 
        print("입력 숫자: {} / 당첨".format(no1))
        break

    elif no1 > ran1 :
        print("입력 숫자: {} / 입력 숫자가 큼".format(no1))

    elif no1 < ran1 :
        print("입력 숫자: {} / 입력 숫자가 작음".format(no1))

print("입력한 모든 숫자: {}".format(mylist))