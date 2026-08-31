import random

ran_num = random.randint(1,100)
mynums = []
count = 0

print("1~100 사이")
while True :
    no1 = int(input("숫자 입력: "))
    mynums.append(no1)
    if no1 == ran_num :
        print("입력숫자 : {}, 당첨!".format(no1))
        break
    elif no1 > ran_num :
        print("낮은 숫자 입력")
    elif no1 < ran_num :
        print ("높은 숫자 입력")
    count = count + 1


print("입력 숫자: {}".format(mynums))
print("입력 횟수: {}".format(count))