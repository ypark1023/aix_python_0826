import random 

ran_num = random.randint(1,100)
my_nums = []
count = 0


print("1~100 사이 숫자 입력")
while True :
    my_num = int(input("숫자 입력: "))
    my_nums.append(my_num)
    if ran_num == my_num :
        print("입력 숫자: {} / 당첨 숫자:{} / 당첨!".format(my_num, ran_num))
        break
    elif ran_num > my_num :
        print("입력 숫자: {} / 더 큰 수를 입력하세요!".format(my_num))
    elif ran_num < my_num :
        print("입력 숫자: {} / 더 작은 수를 입력하세요!".format(my_num))

    count = count + 1


print("입력 숫자: {}".format(my_nums))
print("입력 횟수: {}".format(count))
