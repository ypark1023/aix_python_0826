# mynum = []

# for i in range(6):
#     no = int(input("숫자 입력: "))
#     if no not in mynum :
#         mynum.append(no)
#     else :
#         print("동일한 번호 입력됨")

# print("나의 입력 숫자: {}".format(mynum))

# 이 경우 동일한 숫자가 입력될 시 6개 번호 채울 수 없음 - while문을 활용하면 됨


# i = 0
# mynum = []
# while i < 6 :
#     no = int(input("숫자 입력: "))
#     if no not in mynum :
#         mynum.append(no)
#         i = i+1
#     else :
#         print("동일한 번호 입력됨")
# print("나의 입력 숫자: {}".format(mynum))


# import random
# a = random.randint(1,45)
# print(a)

# alist = list(range(1,45))
# random.shuffle(alist)
# print(alist)

# alist = list(range(1,45))
# ranArr = random.sample(range(1,46),6)
# print(ranArr)

# ranArr2 = random.choices(range(1,46), k=6)
# print(ranArr2)



# import random
# lotto = random.sample(range(1,46), 6)

# no1 = int(input("번호 입력: "))
# if no1 in lotto :
#     print ("입력숫자: {}, 당첨".format(no1))
# else :
#     print ("입력숫자: {}, 꽝".format(no1))

# print("로또 번호: {}".format(lotto))



import random
lotto = random.sample(range(1,46),6)

mynums = []
i = 0
while i < 6 :
    no = int(input("번호 입력: "))
    if no not in mynums :
        mynums.append(no)
        i = i+1
    else : 
        print("번호 있음")

print("나의 입력 숫자: {}".format(mynums))

answer = []
count = 0

for i in mynums :
    if i in lotto :
        count = count+1
        answer.append(i)
    

print("로또번호: {}".format(lotto))
print("나의 입력 숫자: {}".format(mynums))
print("맞춘 숫자: {}".format(answer))
print("맞춘 개수: {}".format(count))